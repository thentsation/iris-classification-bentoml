# Iris Classifier Service

[![Python CI](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_python.yaml/badge.svg)](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_python.yaml)
[![Docker CI/CD](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_docker.yaml/badge.svg)](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_docker.yaml)

> Read in [English](README.md).

Um serviço de classificação da base Iris construído com [BentoML](https://www.bentoml.com/) e scikit-learn, estruturado em camadas (dados → modelo → serviço) seguindo os princípios SOLID.

Um artigo detalhado sobre a produtização deste projeto está disponível em [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Estrutura do projeto

```text
src/
├── data/                  # DataLoader, DataPreprocessor
├── models/                 # ModelInterface, IrisModel (SVC), ModelFactory
├── services/                # ClassifierServiceInterface, IrisClassifier (puro, testável)
│                             e IrisClassifierService (o wrapper @bentoml.service)
├── config/config.py         # Config (tipo/versão do modelo)
└── main.py                  # treina o modelo e salva no model store do BentoML
```

`IrisClassifier` contém a lógica real de classificação e aceita um `ModelInterface` injetado, por isso é testável sem o runtime do BentoML. `IrisClassifierService` é um wrapper fino decorado com `@bentoml.service` que expõe a API HTTP em cima dele.

## Como rodar

```bash
make install    # cria o .venv e instala as deps
make train      # treina o modelo SVC e salva no model store do BentoML
make serve      # treina (se necessário) e sobe `bentoml serve` com --reload
```

- Swagger UI: http://localhost:3000/docs
- Endpoint da API: `POST http://localhost:3000/classify`
- Readiness probe: `GET http://localhost:3000/readyz`

Rodando com Docker (a imagem treina o modelo durante o build):

```bash
make docker-build
make docker-run
```

## Desenvolvimento

```bash
make test        # pytest
make coverage     # pytest com relatório de cobertura
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

O CI roda ruff, pytest (com piso de cobertura), mypy e pip-audit em todo push/PR, além de uma execução diária agendada. Imagens Docker são construídas, escaneadas com Trivy e publicadas no GHCR na `main`. O Dependabot mantém pip, imagem base do Docker e GitHub Actions atualizados, com bumps patch/minor mesclados automaticamente. Releases são versionados automaticamente com [python-semantic-release](https://python-semantic-release.readthedocs.io/).

## Princípios SOLID aplicados

1. **SRP** — carregamento de dados, pré-processamento, modelo e camada HTTP são classes separadas.
2. **OCP** — novos tipos de modelo entram via `ModelFactory` sem tocar código existente.
3. **LSP** — qualquer implementação de `ModelInterface` pode substituir `IrisModel`.
4. **ISP** — interfaces pequenas e focadas (`ModelInterface`, `ClassifierServiceInterface`).
5. **DIP** — `IrisClassifier` depende da abstração `ModelInterface`, injetada na construção, não de um modelo concreto nem do runtime do BentoML.
