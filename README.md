# Almasix starter kits

Official starter-kit overlays for [`almasix new --kit`](https://docs.almasix.com/starter-kits/).

Kits live in this monorepo as separate packages, discovered by Almasix through the
`almasix.kits` entry-point group. The blank `none` kit stays built into core.

| Package | Kits | Depends on |
| --- | --- | --- |
| [`almasix-starter-kit-web`](packages/web) | `web` | [almasix-conduit](https://github.com/almasix-dev/almasix-conduit) |
| [`almasix-starter-kit-api`](packages/api) | `api` | Signet (in Almasix core) |
| [`almasix-starter-kit-spa`](packages/spa) | `react`, `vue`, `svelte` | [almasix-inertia](https://github.com/almasix-dev/almasix-inertia) |

## Install

```bash
# All kits
pip install 'almasix[kits]'

# Or pick one
pip install almasix-starter-kit-web
pip install almasix-starter-kit-api
pip install almasix-starter-kit-spa
```

Then:

```bash
almasix new my-app --kit web
almasix new my-spa --kit react
```

## Develop

```bash
git clone https://github.com/almasix-dev/almasix-starter-kits.git
cd almasix-starter-kits
pip install -e packages/web
pip install -e packages/api
pip install -e packages/spa
```

Requires a recent Almasix that supports `Kit.stub_root` and `almasix.kits` discovery.

## License

[MIT](LICENSE)
