# Repo Maintenance

How this repo's tooling and docs stay accurate. Use this when adding a new tool, changing a lint script, investigating why a check isn't running, or auditing docs for staleness. For the generic documentation maintenance guide (enforcement hierarchy, update triggers, checklists for any project), see `framework/guides/maintenance.md`.

---

## Enforcement Layers

Three layers ensure code quality — each catches what the previous one missed:

| Layer                 | Scope         | Behavior                       | Config                               |
| --------------------- | ------------- | ------------------------------ | ------------------------------------ |
| **Claude Code hooks** | modified file | fix + lint on every Write/Edit | `.claude/settings.json`              |
| **Git hooks**         | staged files  | fix + lint on every commit     | `.pre-commit-config.yaml` (via prek) |
| **CI**                | all files     | lint-only (no fix)             | `.github/workflows/lint.yml`         |

All three layers use the same wrapper scripts in `scripts/tools/`. Most scripts auto-fix first, then check — so hooks fix issues automatically while CI only reports them.

---

## Update Triggers

| When you...                                                                                     | Update                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Add or rename a top-level directory                                                             | `AGENTS.md` structure map, `layout.md` Contents section                                                                                                                          |
| Add or rename a script or tool                                                                  | `layout.md` Contents section                                                                                                                                                     |
| Add a script to `scripts/tools/`                                                                | `scripts/tools/README.md` scripts table                                                                                                                                          |
| Add a new doc to `docs/` or `framework/guides/`                                                 | `AGENTS.md` routing table                                                                                                                                                        |
| Accept a spec                                                                                   | `docs/decisions/` — write an ADR recording why this approach was chosen                                                                                                          |
| Complete a plan (all files done)                                                                | Write or verify an ADR for non-obvious decisions; move spec to `docs/specs/live/`; archive plan to `docs/archive/plans/`; update `docs/specs/index.md` and `docs/plans/index.md` |
| Make a non-obvious architectural decision about the framework                                   | `docs/decisions/` — write or supersede an ADR                                                                                                                                    |
| Add a new writing guide                                                                         | `AGENTS.md` routing table                                                                                                                                                        |
| Change taxonomy, placement rules, or conventions in `framework/managing-project-information.md` | `framework/auditing-anti-patterns.md` — the audit guide is self-contained by design (all detection info inline, no hops mid-audit), so it must stay in sync                      |
| Change a lint/format script in `scripts/tools/`                                                 | `.pre-commit-config.yaml`, `.github/workflows/lint.yml`, `.claude/settings.json` (if affected)                                                                                   |
| Add a new linter or formatter                                                                   | `pyproject.toml` (dep), new script in `scripts/tools/`, `scripts/tools/README.md`, hook in `.pre-commit-config.yaml`, step in `.github/workflows/lint.yml`                       |
| Change Python version requirement                                                               | `pyproject.toml` requires-python, `.github/workflows/lint.yml`                                                                                                                   |
| Add a new project dev setup script                                                              | `scripts/setup/setup.sh` (step), `scripts/setup/README.md` (table + dependency tree)                                                                                             |

---

## Keeping Docs Accurate

Update docs in the same PR as the code change they describe. A guide change without a corresponding AGENTS.md update (or vice versa) creates drift.

### What to check after any change

1. Does `AGENTS.md`'s structure map still match the actual directory layout?
1. Does every file in `docs/` and `framework/guides/` appear in the routing table?
1. Does every routing table entry match an actual file?
1. Do the conventions in `AGENTS.md` match what the guides teach? If a guide says "do X" but AGENTS.md doesn't mention it, either add it or the guide is wrong.
1. Does `framework/managing-project-information.md` still reflect how this repo actually organizes information?
1. When a framework design choice changes, is there an ADR in `docs/decisions/` superseding the old one?

### Detecting staleness

| Check                                        | Command                                                                                           |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Broken file references in docs               | `grep -rn 'docs/' AGENTS.md docs/`                                                                |
| Files missing from routing table             | Compare `ls docs/ framework/guides/` against AGENTS.md routing table                              |
| AGENTS.md conventions not followed by guides | Read each convention, verify guides follow it                                                     |
| Guides referencing removed tools or scripts  | `grep -rn 'scripts/' framework/guides/` and verify paths exist                                    |
| `layout.md` Contents out of date             | Compare `layout.md` Contents against actual `ls framework/guides/ scripts/tools/ docs/decisions/` |
