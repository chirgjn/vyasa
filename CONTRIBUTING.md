# Contributing to vyasa

## Prerequisites

- macOS or Linux
- [Claude Code](https://claude.ai/code) CLI installed and authenticated
- Git

## Getting started

Run the setup script to install the full dev environment:

```bash
scripts/setup/setup.sh
```

This installs: uv + Python >=3.14, jq, taplo, yamllint/yamlfix/actionlint, gh, pnpm, prettier, and Claude Code plugins used in this repo.

To verify the setup worked:

```bash
scripts/setup/verify-setup.sh
```

## Repo structure

```
framework/        — The documentation framework
scripts/tools/    — Linter/formatter wrappers for CI and local hooks
scripts/setup/    — Dev environment setup scripts
docs/             — Dev-facing reference docs (decisions, specs)
.github/          — CI workflows
```

For the full directory map, see `layout.md`.

## Running checks

All checks use wrapper scripts in `scripts/tools/`:

```bash
framework/tools/prettier-fix.sh     # format markdown
scripts/tools/ruff-fix.sh           # lint + fix Python
scripts/tools/basedpyright-lint.sh  # typecheck Python
scripts/tools/pytest-run.sh         # run tests
scripts/tools/shellcheck-lint.sh    # lint shell scripts
scripts/tools/yamllint-fmt.sh       # fix + lint YAML
scripts/tools/taplo-fmt.sh          # format TOML
scripts/tools/actionlint-lint.sh    # lint GitHub Actions
```

These run automatically on every commit (pre-commit hooks) and in CI. Locally they auto-fix; CI is check-only.

## Making changes

When adding or changing things, update the relevant docs in the same PR. See `docs/maintenance.md` for the full update triggers table.
