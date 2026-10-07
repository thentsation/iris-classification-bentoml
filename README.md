# Iris Classifier Service

[![Python CI](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_python.yaml/badge.svg)](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_python.yaml)
[![Docker CI/CD](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_docker.yaml/badge.svg)](https://github.com/thentsation/iris-classification-bentoml/actions/workflows/pipeline_docker.yaml)

> Leia em [português](README.pt-br.md).

An Iris classification service built with [BentoML](https://www.bentoml.com/) and scikit-learn, structured in layers (data → model → service) following SOLID principles.

An in-depth write-up of the productization of this project is available in [ARTIGO.md](ARTIGO.md) (pt-br) / [ARTIGO.en-us.md](ARTIGO.en-us.md) (en-us).

## Project structure

```text
src/
├── data/                  # DataLoader, DataPreprocessor
├── models/                 # ModelInterface, IrisModel (SVC), ModelFactory
├── services/                # ClassifierServiceInterface, IrisClassifier (plain, testable)
│                             and IrisClassifierService (the @bentoml.service wrapper)
├── config/config.py         # Config (model type/version)
└── main.py                  # trains the model and saves it to the BentoML model store
```

`IrisClassifier` holds the actual classification logic and accepts an injected `ModelInterface`, so it's tested without the BentoML service runtime. `IrisClassifierService` is a thin `@bentoml.service`-decorated wrapper around it that exposes the HTTP API.

## Getting started

```bash
make install    # creates .venv and installs deps
make train      # trains the SVC model and saves it to the BentoML model store
make serve      # trains (if needed) and starts `bentoml serve` with --reload
```

- Swagger UI: http://localhost:3000/docs
- API endpoint: `POST http://localhost:3000/classify`
- Readiness probe: `GET http://localhost:3000/readyz`

Run with Docker instead (the image trains the model at build time):

```bash
make docker-build
make docker-run
```

## Development

```bash
make test        # pytest
make coverage     # pytest with coverage report
make lint         # ruff check
make format       # ruff format
make typecheck    # mypy
```

CI runs ruff, pytest (coverage gate), mypy and pip-audit on every push/PR, plus a scheduled daily run. Docker images are built, scanned with Trivy, and published to GHCR on `main`. Dependabot keeps pip, the Docker base image, and GitHub Actions up to date, with patch/minor bumps auto-merged. Releases are tagged automatically with [python-semantic-release](https://python-semantic-release.readthedocs.io/).

## SOLID principles applied

1. **SRP** — data loading, preprocessing, model, and the HTTP layer are all separate classes.
2. **OCP** — new model types plug into `ModelFactory` without touching existing code.
3. **LSP** — any `ModelInterface` implementation can replace `IrisModel`.
4. **ISP** — small, focused interfaces (`ModelInterface`, `ClassifierServiceInterface`).
5. **DIP** — `IrisClassifier` depends on the `ModelInterface` abstraction, injected at construction time, not on a concrete model or the BentoML runtime.
