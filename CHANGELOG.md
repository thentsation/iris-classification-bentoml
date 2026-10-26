# CHANGELOG

<!-- version list -->

## v1.0.6 (2026-10-26)

### Bug Fixes

- **deps**: Upgrade lockfile and use --upgrade in lockfile workflow
  ([#27](https://github.com/thentsation/iris-classification-bentoml/pull/27),
  [`ee0e82b`](https://github.com/thentsation/iris-classification-bentoml/commit/ee0e82b3c0efe10ba6aa8dad076d38ed52374f2c))

- **deps**: Use --upgrade when regenerating the lockfile
  ([#27](https://github.com/thentsation/iris-classification-bentoml/pull/27),
  [`ee0e82b`](https://github.com/thentsation/iris-classification-bentoml/commit/ee0e82b3c0efe10ba6aa8dad076d38ed52374f2c))

### Chores

- **ci**: Bump astral-sh/setup-uv from 10.2.0 to 10.3.0
  ([#23](https://github.com/thentsation/iris-classification-bentoml/pull/23),
  [`94ed221`](https://github.com/thentsation/iris-classification-bentoml/commit/94ed221fc4d32632720b526a5540aacb9fedcb7e))

- **ci**: Bump astral-sh/setup-uv from 10.3.0 to 10.3.2
  ([#26](https://github.com/thentsation/iris-classification-bentoml/pull/26),
  [`3f054ff`](https://github.com/thentsation/iris-classification-bentoml/commit/3f054ffe2253612487ef7f24052a8f2129d04413))

- **deps**: Bump ruff from 0.16.10 to 0.17.0 in /config
  ([#22](https://github.com/thentsation/iris-classification-bentoml/pull/22),
  [`bc97677`](https://github.com/thentsation/iris-classification-bentoml/commit/bc97677738465275a22697ab85541a752304e267))

- **deps**: Bump ruff from 0.17.0 to 0.17.1 in /config
  ([#24](https://github.com/thentsation/iris-classification-bentoml/pull/24),
  [`fa2c7d7`](https://github.com/thentsation/iris-classification-bentoml/commit/fa2c7d76194a0fb6d83f441fd2cae84b1c59f0ee))

- **deps**: Bump ruff from 0.17.1 to 0.17.2 in /config
  ([#25](https://github.com/thentsation/iris-classification-bentoml/pull/25),
  [`8b75662`](https://github.com/thentsation/iris-classification-bentoml/commit/8b75662565bbedd789a1c16906a8d5d3860aa46d))

- **deps**: Refresh pip-compile outputs
  ([#18](https://github.com/thentsation/iris-classification-bentoml/pull/18),
  [`61b3bb6`](https://github.com/thentsation/iris-classification-bentoml/commit/61b3bb6409aa0f09f96dba7b1bae051a80a420b6))

- **deps**: Update dependency mypy to v2.4.0
  ([#16](https://github.com/thentsation/iris-classification-bentoml/pull/16),
  [`267b044`](https://github.com/thentsation/iris-classification-bentoml/commit/267b044e5b0490a7ae4458396f714eddedf7076e))

- **deps**: Update dependency ruff to v0.16.10
  ([#15](https://github.com/thentsation/iris-classification-bentoml/pull/15),
  [`ab9bbc6`](https://github.com/thentsation/iris-classification-bentoml/commit/ab9bbc60661d9c58fd37d9650a695c55599d872a))

- **deps**: Update lockfile
  ([#27](https://github.com/thentsation/iris-classification-bentoml/pull/27),
  [`ee0e82b`](https://github.com/thentsation/iris-classification-bentoml/commit/ee0e82b3c0efe10ba6aa8dad076d38ed52374f2c))

- **deps**: Update lockfile
  ([#21](https://github.com/thentsation/iris-classification-bentoml/pull/21),
  [`e2a8edc`](https://github.com/thentsation/iris-classification-bentoml/commit/e2a8edc504f8a6913aaf510d1c4f7db7168d04d3))

### Continuous Integration

- Pipeline da Shared Library da plataforma e Renovate
  ([#14](https://github.com/thentsation/iris-classification-bentoml/pull/14),
  [`560df36`](https://github.com/thentsation/iris-classification-bentoml/commit/560df36b5e8643ece6aa208435527561e2ea1e3d))

- Remove workflow notify-portfolio (token sem acesso; o portfolio atualiza pelo cron diário)
  ([#20](https://github.com/thentsation/iris-classification-bentoml/pull/20),
  [`358158d`](https://github.com/thentsation/iris-classification-bentoml/commit/358158d49e15d04848e26eaae3d821b89366c9d7))


## v1.0.5 (2026-09-28)

### Bug Fixes

- **ci**: Open lockfile PRs with RELEASE_PAT so CI runs on them
  ([`75385d6`](https://github.com/thentsation/iris-classification-bentoml/commit/75385d612c9a00feb9ee23ab3fbdca2d9f091a9d))

### Chores

- **deps**: Update joblib requirement in /config
  ([#10](https://github.com/thentsation/iris-classification-bentoml/pull/10),
  [`b1f67fd`](https://github.com/thentsation/iris-classification-bentoml/commit/b1f67fddc3560828907c58fd4643fd4e60793fd3))


## v1.0.4 (2026-09-28)

### Bug Fixes

- Use RELEASE_PAT so dependabot auto-merge can write to PRs
  ([`f844f1d`](https://github.com/thentsation/iris-classification-bentoml/commit/f844f1d5db510146be94305e5d65826eed52fc77))

### Chores

- **deps**: Bump ruff from 0.16.3 to 0.16.9 in /config
  ([#11](https://github.com/thentsation/iris-classification-bentoml/pull/11),
  [`cecc9c1`](https://github.com/thentsation/iris-classification-bentoml/commit/cecc9c1dafefdf6cb89643a6fa8f3a09a6f35751))


## v1.0.3 (2026-09-26)

### Bug Fixes

- Broaden Trivy's pip/_vendor skip-dirs to a recursive glob
  ([`768e490`](https://github.com/thentsation/iris-classification-bentoml/commit/768e490d00764b22e28076fd546bc055fdd5f569))


## v1.0.2 (2026-09-26)

### Bug Fixes

- Set PYTHONPATH so bentoml serve resolves bare src imports
  ([`420ec2a`](https://github.com/thentsation/iris-classification-bentoml/commit/420ec2ac413ebd8ffcba5858da93e5309d716099))


## v1.0.1 (2026-09-25)

### Bug Fixes

- Skip pip's vendored msgpack copy in the Trivy scan
  ([`0da3fd1`](https://github.com/thentsation/iris-classification-bentoml/commit/0da3fd1cb787dee9bd9d121ff0eed178e068815e))

### Chores

- **deps**: Bump python from 3.12-slim to 3.14-slim in /docker
  ([#6](https://github.com/thentsation/iris-classification-bentoml/pull/6),
  [`5ebd528`](https://github.com/thentsation/iris-classification-bentoml/commit/5ebd528922db659c7d3ce163fe0f18c54f6bb2d0))

- **deps**: Update bentoml requirement in /config
  ([#7](https://github.com/thentsation/iris-classification-bentoml/pull/7),
  [`8afd3f5`](https://github.com/thentsation/iris-classification-bentoml/commit/8afd3f583e056b9917f94a9307e86b6007274394))

- **deps**: Update scikit-learn requirement in /config
  ([#9](https://github.com/thentsation/iris-classification-bentoml/pull/9),
  [`d61eb83`](https://github.com/thentsation/iris-classification-bentoml/commit/d61eb83e19a5f942a5e357810f29f29a5a52710c))
