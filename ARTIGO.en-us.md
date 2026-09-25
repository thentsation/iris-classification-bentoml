[🇧🇷 Português](ARTIGO.md) | 🇺🇸 English

# A BentoML service that claimed to follow SOLID but had zero tests

The project already had the right shape: data, model and service layers, abstract interfaces, a factory. The README listed all five SOLID principles one by one. What it lacked was proof any of it actually worked — zero tests, a `bentofile.yaml` pointing at a file that didn't exist, and a CI that only ran `ruff check`.

## What I had

An Iris classifier using SVM (`scikit-learn`), served through BentoML, with `DataLoader`, `DataPreprocessor`, `IrisModel` (implementing `ModelInterface`), `ModelFactory`, and `IrisClassifierService`. Two pipelines (`pipeline_python.yaml`, `pipeline_docker.yaml`), neither running a single test, type check, or dependency scan — just lint and build. `config/requirements.txt` unpinned (`bentoml`, `scikit-learn`, nothing else — it was even missing `joblib`, which the code imports directly). And `bentoml/bentofile.yaml` pointed at `service.py:IrisClassifier`, a path that never existed in the repo; the Dockerfile didn't even use that file, so the error stayed invisible until I read both side by side.

## The test that exposed the real architectural problem

Before writing any test, I tried instantiating `IrisClassifierService` directly, the way the README itself suggested for local use. It didn't work: the `@bentoml.service` decorator replaces the class with a BentoML `Service` object, and calling `IrisClassifierService(model=...)` doesn't run the original `__init__` — it hits the wrapper's `__call__`, which doesn't accept that argument.

This is the SRP and DIP the README claimed, being violated in practice: the classification logic was welded to the service framework. I split the two apart — `IrisClassifier` (a plain class, accepting an injected `ModelInterface`, with no BentoML dependency at all) and `IrisClassifierService` (a thin wrapper decorated with `@bentoml.service`, delegating to `IrisClassifier` internally):

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

Only after this split did dependency-injection tests (training a real `IrisModel` and handing it to `IrisClassifier`) make sense — without mocking anything, since training an SVM on 150 Iris samples is fast and deterministic enough to be worth testing against the real model.

## Coverage per layer, without touching the BentoML runtime

`test_data_loader.py` and `test_data_preprocessor.py` cover the data layer (shapes, classes, preprocessor identity). `test_iris_model.py` trains, predicts, and round-trips save/load with `tmp_path`. `test_model_factory.py` covers the happy path (case-insensitive) and the `ValueError` for an unknown type. `test_iris_service.py` tests `IrisClassifier` with the injected model. `test_main.py` runs `train_and_save_model()` end to end and checks that the saved model predicts correctly after being reloaded. Result: 91% line coverage, with a 90% CI floor.

## Fixing the rest: `bentofile.yaml`, types, requirements

I fixed `bentofile.yaml` to point at the real service (`src.services.iris_service:IrisClassifierService`) and at the correct `requirements.txt` under `config/`. I added `ModelInterface` as the return type of `ModelFactory.create_model` (it had no annotation, so `mypy` couldn't catch an invalid `model_type` statically). I pinned `bentoml`, `scikit-learn`, and `joblib` in `config/requirements.txt` and generated a `config/requirements.lock` with `uv pip compile`, audited with `pip-audit` — clean.

## Docker: training the model is a build-time concern

The Dockerfile is now multi-stage (`python:3.12-slim`), installs from the lockfile, trains the model (`RUN python src/main.py`) **during the build**, and only then switches to a non-root user — so the final image comes up with the model already in the local model store, without depending on a training step in production.

## CI, dependabot and release, but manual deploy for now

The full pipeline (ruff, pytest with a 90% floor, mypy, pip-audit, Docker+Trivy+GHCR, dependabot with auto-merge, dependency dashboard, weekly lockfile refresh, semantic release) follows the same pattern as the other projects in the organization. `deploy.yaml`, though, is a manual `workflow_dispatch`: it only pulls the published image and checks `/readyz`, without bringing anything up in production automatically. This service would actually make sense to keep running continuously (it's a real API, not a batch script), but I'd rather the decision to expose a port on production infrastructure be explicit, not a side effect of a `git push`.
