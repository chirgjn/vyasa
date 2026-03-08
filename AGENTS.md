# vyasa

Opinionated documentation framework — how to structure, write, and maintain project docs so AI coding agents find the right information fast.

## Structure

```
framework/                      — The documentation framework
framework/managing-project-information.md — Central index: taxonomy, placement, directory structure, and routing table for all writing guides
framework/auditing-anti-patterns.md       — Pragmatic audit guide: broad but not exhaustive, self-contained
framework/guides/               — Writing guides: prose style, conventions, diagrams, AGENTS.md, layout.md, ADRs, specs, designs, maintenance
docs/                           — This repo's reference docs, decisions, and designs
scripts/setup/                  — Project dev setup scripts (uv, Python, deps, taplo, gh, etc.)
scripts/tools/                  — Dev-only linter/formatter wrappers for hooks and CI
.github/workflows/              — CI (lint.yml runs all checks)
```

## Commands

```bash
framework/tools/prettier-fix.sh       # format markdown (auto-fix + check)
scripts/tools/ruff-fix.sh             # lint + auto-fix Python
scripts/tools/basedpyright-lint.sh    # typecheck Python
scripts/tools/shellcheck-lint.sh      # lint shell
scripts/tools/yamllint-fmt.sh         # fix + lint YAML
scripts/tools/actionlint-lint.sh      # lint GitHub Actions
scripts/tools/taplo-fmt.sh            # format TOML
scripts/tools/pytest-run.sh           # run tests (defaults to tests/)
scripts/setup/setup.sh                # full project dev setup
```

## Conventions

- `AGENTS.md` is the canonical file; `CLAUDE.md` is a symlink (`ln -s AGENTS.md CLAUDE.md`) — never edit `CLAUDE.md` directly, never maintain two copies
- Every reference doc opens with a scoped "what this covers and when to read it" line — never jump straight into content
- Routing table entries use task phrasing ("When you are..."), not filenames — never "Read docs/foo.md"
- Each convention includes what NOT to do — a convention without a negative constraint doesn't prevent the mistake
- One canonical home per concept — never duplicate content over 3 lines across files, link instead
- Use Mermaid for diagrams, not ASCII art — never represent flows, lifecycles, or relationships as plain-text boxes and arrows

## Tooling

- **Python**: >=3.14, managed via uv
- **Formatting**: prettier (markdown), taplo (TOML), yamlfix (YAML), ruff (Python)
- **Linting**: ruff + basedpyright (Python), shellcheck (shell), yamllint (YAML), actionlint (GHA)
- **Project dev setup**: `scripts/setup/setup.sh` installs the full project dev environment; individual scripts in `scripts/setup/`

## Routing

**Any doc work — writing, editing, placing, or auditing:** start at `framework/managing-project-information.md`.
It answers: what type of doc is this, where does it live, and which guide covers how to write it well.
Skipping it is the primary source of misplaced content, wrong doc types, and missing conventions.
For finding and fixing problems in docs that already exist, see `framework/auditing-anti-patterns.md`.

**This repo:**

| When you are...                                                                                | Read                              |
| ---------------------------------------------------------------------------------------------- | --------------------------------- |
| Getting a structural map of the repo — what lives where before making changes                  | `layout.md`                       |
| Understanding what each dev tool script does (ruff, prettier, CI checks, etc.)                 | `scripts/tools/README.md`         |
| Understanding project dev setup scripts or install dependencies                                | `scripts/setup/README.md`         |
| Checking this repo's update triggers, enforcement layers, or release process                   | `docs/maintenance.md`             |
| Keeping basedpyright warnings at zero in pytest test files — `tmp_path`, `cast()`, unused vars | `docs/python-type-annotations.md` |
