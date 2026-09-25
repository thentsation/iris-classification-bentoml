🇧🇷 Português | [🇺🇸 English](ARTIGO.en-us.md)

# Um serviço BentoML que dizia seguir SOLID, mas não tinha um teste sequer

O projeto já tinha a estrutura certa: camadas de dados, modelo e serviço, interfaces abstratas, uma factory. O README listava os cinco princípios SOLID um por um. O que faltava era a prova de que isso funcionava — zero testes, um `bentofile.yaml` apontando para um arquivo que não existia, e um CI que só rodava `ruff check`.

## O que eu tinha em mãos

Um classificador Iris com SVM (`scikit-learn`), servido via BentoML, com `DataLoader`, `DataPreprocessor`, `IrisModel` (implementando `ModelInterface`), `ModelFactory` e `IrisClassifierService`. Dois pipelines (`pipeline_python.yaml`, `pipeline_docker.yaml`), nenhum dos dois rodando teste, tipo ou dependência algum — só lint e build. `config/requirements.txt` sem versão pinada (`bentoml`, `scikit-learn`, nada mais — faltava até o `joblib` que o código importa diretamente). E o `bentoml/bentofile.yaml` referenciava `service.py:IrisClassifier`, um caminho que nunca existiu no repositório; o Dockerfile nem usava esse arquivo, então o erro ficou invisível até eu ler os dois lado a lado.

## O teste que expôs o problema real da arquitetura

Antes de escrever qualquer teste, tentei instanciar `IrisClassifierService` diretamente, como o próprio `README` sugeria para uso local. Não funcionou: o decorator `@bentoml.service` substitui a classe por um `Service` do BentoML, e chamar `IrisClassifierService(model=...)` não executa o `__init__` original — ele bate num `__call__` do wrapper que não aceita esse argumento.

Isso é o SRP e o DIP que o README reivindicava sendo violados na prática: a lógica de classificação estava soldada ao framework de serviço. Separei os dois — `IrisClassifier` (classe pura, aceita um `ModelInterface` injetado, sem nenhuma dependência do BentoML) e `IrisClassifierService` (wrapper fino decorado com `@bentoml.service`, delegando pro `IrisClassifier` por dentro):

```python
class IrisClassifier(ClassifierServiceInterface):
    def __init__(self, model: ModelInterface | None = None) -> None:
        self.model = model or load_default_model()

    def classify(self, input_data: np.ndarray) -> np.ndarray:
        return self.model.predict(input_data)


@bentoml.service(resources={"cpu": "1", "memory": "2Gi"})
class IrisClassifierService:
    def __init__(self) -> None:
        self._classifier = IrisClassifier()

    @bentoml.api
    def classify(self, input_series: ... = Field(default=DEFAULT_INPUT)) -> np.ndarray:
        return self._classifier.classify(input_series)
```

Só depois dessa separação os testes de injeção de dependência (treinar um `IrisModel` de verdade e passá-lo pro `IrisClassifier`) fizeram sentido — sem mockar nada, porque treinar SVM em 150 amostras do Iris é rápido e determinístico o suficiente para valer testar contra o modelo real.

## Cobertura por camada, sem tocar no BentoML runtime

`test_data_loader.py` e `test_data_preprocessor.py` cobrem a camada de dados (shapes, classes, identidade do preprocessador). `test_iris_model.py` treina, prediz e faz round-trip de save/load com `tmp_path`. `test_model_factory.py` cobre o caminho feliz (case-insensitive) e o `ValueError` de tipo desconhecido. `test_iris_service.py` testa `IrisClassifier` com o modelo injetado. `test_main.py` roda `train_and_save_model()` de ponta a ponta e confere que o modelo salvo prediz corretamente depois de recarregado. Resultado: 91% de cobertura de linha, com piso de CI em 90%.

## Consertando o resto: `bentofile.yaml`, tipos, requirements

Corrigi o `bentofile.yaml` para apontar pro serviço real (`src.services.iris_service:IrisClassifierService`) e pro `requirements.txt` correto em `config/`. Adicionei `ModelInterface` como tipo de retorno de `ModelFactory.create_model` (estava sem anotação, então o `mypy` não pegava um `model_type` inválido em tempo de checagem estática). Pinei `bentoml`, `scikit-learn` e `joblib` em `config/requirements.txt` e gerei um `config/requirements.lock` com `uv pip compile`, auditado com `pip-audit` — limpo.

## Docker: treinar o modelo é parte do build

O Dockerfile agora é multi-stage (`python:3.12-slim`), instala a partir do lockfile, treina o modelo (`RUN python src/main.py`) **durante o build**, e só depois troca para o usuário não-root — assim a imagem final já sobe com o modelo pronto no model store local, sem depender de um passo de treino em produção.

## CI, dependabot e release, mas deploy manual por enquanto

O pipeline completo (ruff, pytest com piso de 90%, mypy, pip-audit, Docker+Trivy+GHCR, dependabot com auto-merge, dashboard de dependências, atualização semanal de lockfile, release semântico) segue o mesmo padrão dos outros projetos da organização. O `deploy.yaml`, porém, ficou como `workflow_dispatch` manual — ele só puxa a imagem publicada e confere o `/readyz`, sem subir nada em produção automaticamente. Esse serviço até faz sentido ficar no ar continuamente (é uma API real, não um script batch), mas prefiro que a decisão de expor uma porta na infraestrutura de produção seja explícita, não uma consequência de um `git push`.
