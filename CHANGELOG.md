# CHANGELOG

<!-- version list -->

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
