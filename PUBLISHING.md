# Publishing starter-kit packages

Each of `almasix-starter-kit-web`, `almasix-starter-kit-api`, and
`almasix-starter-kit-spa` is versioned together in this monorepo (currently
**0.1.0**).

## Prerequisites

1. Almasix **≥ 0.9.4** published (provides `Kit.stub_root` + `almasix.kits` discovery).
2. PyPI **Trusted Publishing** for each project, pointing at this repo’s
   `Publish` workflow and the `pypi` environment (same pattern as
   [almasix](https://github.com/almasix-dev/almasix/blob/main/.github/workflows/publish.yml)).

## Cut a release

```bash
# After Almasix 0.9.4 is on PyPI:
git tag v0.1.0
git push origin v0.1.0
gh release create v0.1.0 --title "v0.1.0" --notes "Initial starter-kit packages."
```

The `Publish` workflow builds each package and uploads via OIDC.

## Manual / TestPyPI

Actions → **Publish** → Run workflow → `testpypi` or `pypi`.
