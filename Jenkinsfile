// Pipeline da plataforma (Shared Library "platform", repo devops-platform/jenkins-lib).
// PRs e branches: validação, CI (docker build --target test), pip-audit e Trivy.
// main: build, smoke test, push, deploy atrás do Traefik com rollback, release
// (semantic-release), rebuild do portfolio e rebuild semanal.
@Library('platform') _

appPipeline(
    name: 'iris-classification-bentoml',
    host: 'iris-bentoml.137-131-175-7.sslip.io',
    healthPath: '/healthz',
    // O /healthz do BentoML não devolve a versão.
    healthExpectsVersion: false,
    deployBranch: 'main',
    notify: [[repo: 'ntsation/portfolio', event: 'rebuild']],
)
