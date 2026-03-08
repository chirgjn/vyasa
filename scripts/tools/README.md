# Dev Tools

Linter and formatter wrappers used by this repo's pre-commit hooks, Claude Code hooks, and CI.
These scripts are dev infrastructure for vyasa itself — not part of the framework content.

## Scripts

| Script                       | Tool               | What it does                                                                                                             |
| ---------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `ruff-fix.sh`                | ruff               | Lint Python — auto-fix then check locally; `--check` skips the fix (used in CI)                                          |
| `basedpyright-lint.sh`       | basedpyright       | Typecheck Python                                                                                                         |
| `pytest-run.sh`              | pytest             | Run the test suite                                                                                                       |
| `shellcheck-lint.sh`         | shellcheck         | Lint shell scripts in `scripts/`                                                                                         |
| `yamllint-fmt.sh`            | yamllint + yamlfix | Fix + lint YAML (yamlfix skips `.github/`) — auto-fix then check locally; `--check` skips the fix (used in CI)           |
| `actionlint-lint.sh`         | actionlint         | Lint GitHub Actions workflows                                                                                            |
| `taplo-fmt.sh`               | taplo              | Format TOML — auto-fix locally; `--check` skips the fix (used in CI)                                                     |
| `post-write-lint.sh`         | —                  | Dev PostToolUse hook: routes Write/Edit to the right linter by file extension; flags `.md` files for deferred formatting |
| `stop-prettier.sh`           | prettier           | Dev Stop hook: runs prettier once on all `.md` files touched during the turn, then clears the flag                       |
| `block-no-verify.sh`         | —                  | Hook that blocks `git commit --no-verify`                                                                                |
| `uv-sync-if-lock-changed.sh` | uv                 | Re-sync the venv when `uv.lock` changes                                                                                  |
