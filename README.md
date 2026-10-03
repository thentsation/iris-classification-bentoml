# Iris Classifier Service

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

CI and deploy run on the platform's Jenkins (`Jenkinsfile` → `appPipeline` from the `platform` Shared Library, repo devops-platform), triggered by webhooks; there are no GitHub Actions.

- **PRs and branches** — contract validation; `docker build --target test` (`ruff check`, `ruff format --check`, `mypy`, `pytest` with ≥90% coverage on Python 3.11 and 3.12, tool versions from `config/requirements-dev.txt`); `pip-audit` on `config/requirements.lock`; Trivy (CRITICAL/HIGH) on the runtime image.
- **main** — all of the above, then build, smoke test, push to OCIR, deploy behind Traefik at https://iris-bentoml.137-131-175-7.sslip.io with automatic rollback, release with python-semantic-release (version, CHANGELOG, tag and GitHub release) and a rebuild of the portfolio. Also rebuilt every Monday to pick up security patches.
- **Dependencies** — Renovate (Jenkins job `platform/renovate`, `renovate.json` → devops-platform preset): daily updates, weekly lockfile maintenance, Dependency Dashboard issue and auto-merge of patch/minor after Jenkins passes.

## SOLID principles applied

1. **SRP** — data loading, preprocessing, model, and the HTTP layer are all separate classes.
2. **OCP** — new model types plug into `ModelFactory` without touching existing code.
3. **LSP** — any `ModelInterface` implementation can replace `IrisModel`.
4. **ISP** — small, focused interfaces (`ModelInterface`, `ClassifierServiceInterface`).
5. **DIP** — `IrisClassifier` depends on the `ModelInterface` abstraction, injected at construction time, not on a concrete model or the BentoML runtime.
