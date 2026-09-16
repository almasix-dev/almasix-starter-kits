# Publishing starter-kit packages

Each of `almasix-starter-kit-web`, `almasix-starter-kit-api`, and
`almasix-starter-kit-spa` is versioned together in this monorepo (currently
**0.1.0**).

## Why three workflows?

PyPI **pending** trusted publishers are unique on
`(owner, repo, workflow filename, environment)` — not on project name. A single
`publish.yml` cannot back three pending publishers. This repo uses one workflow
file per package so all three can be registered before the first upload.

## Prerequisites

1. Almasix **≥ 0.9.4** on PyPI (`Kit.stub_root` + `almasix.kits` discovery).
2. GitHub Environment **`pypi`** on this repository.
3. Three **pending publishers** at https://pypi.org/manage/account/publishing/
   (logged in as the PyPI owner):

| PyPI Project Name | Owner | Repository | Workflow name | Environment |
| --- | --- | --- | --- | --- |
| `almasix-starter-kit-web` | `almasix-dev` | `almasix-starter-kits` | `publish-web.yml` | `pypi` |
| `almasix-starter-kit-api` | `almasix-dev` | `almasix-starter-kits` | `publish-api.yml` | `pypi` |
| `almasix-starter-kit-spa` | `almasix-dev` | `almasix-starter-kits` | `publish-spa.yml` | `pypi` |

## Cut a release

```bash
# After Almasix 0.9.4 is on PyPI and versions in packages/*/pyproject.toml match:
git tag v0.1.0
git push origin v0.1.0
gh release create v0.1.0 --title "v0.1.0" --notes "Initial starter-kit packages."
```

A published GitHub Release runs all three Publish workflows.

If `v0.1.0` already exists: Actions → run **Publish web** / **Publish api** /
**Publish spa** with target `pypi` (after the pending publishers are registered).

## Manual / TestPyPI

Actions → **Publish web** (or api / spa) → Run workflow → `testpypi` or `pypi`.
