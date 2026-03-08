---
docs: docs/
---

# vyasa

Structural map of the vyasa repo — the opinionated documentation framework for AI-assisted
projects. Read this to orient before adding files, moving things, or understanding where
a concern belongs.

## Contents

```
layout.md                        — this file
AGENTS.md                        — navigation, commands, conventions, routing table
CLAUDE.md -> AGENTS.md           — symlink; never edit directly
README.md                        — human entry point: what vyasa is, what it contains
pyproject.toml                   — Python tooling config (ruff, basedpyright)
pyrightconfig.json               — basedpyright settings
package.json                     — Node.js dev dependencies (prettier)
pnpm-lock.yaml                   — pnpm lockfile

framework/                       — the documentation framework
  managing-project-information.md — placement authority: taxonomy, directory structure, routing table
  auditing-anti-patterns.md      — pragmatic audit guide: misplacement, duplication, discoverability
  guides/                        — writing guides for each doc type
    writing-agents-md.md
    writing-layout-md.md
    writing-conventions.md
    writing-reference-docs.md
    writing-decision-records.md
    writing-architecture-docs.md
    writing-specs.md
    writing-design-docs.md
    writing-prose-style.md
    diagrams.md
    mermaid.md
    maintenance.md
    staleness.md
  layout.md                      — structural map of framework/
  README.md                      — what the framework contains and how it's used

scripts/
  setup/                         — full project dev setup: orchestrator + individual install scripts
    setup.sh                     — entry point: runs all install steps in order
    README.md                    — script table and dependency tree
    install-*.sh, verify-setup.sh — individual install and verification scripts
  tools/                         — dev-only linter/formatter wrappers; used by hooks and CI → scripts/tools/README.md

docs/
  maintenance.md                 — this repo's update triggers, enforcement layers
  python-type-annotations.md     — how to keep basedpyright warnings at zero in pytest test files
  decisions/                     — ADRs: reasoning behind non-obvious framework design choices
  designs/                       — design docs: pre-approval problem + alternatives + recommendation
  plans/                         — active implementation plans (archive to docs/archive/plans/ after merge)
  archive/
    plans/                       — completed implementation plans
```

## What Lives Here

- `pyproject.toml` — shared Python tooling config (not per-directory)
- `package.json` — Node.js dev dependencies (prettier)

## What Doesn't Live Here

- Consumer-project docs → this repo contains the framework, not the docs of projects that use vyasa
- Plugin agents, hooks, commands, scripts → those live in `vyasa-agent`

## Guides

| When you are...                                                 | Read                      |
| --------------------------------------------------------------- | ------------------------- |
| Reading why a framework design decision was made                | `docs/decisions/`         |
| Checking update triggers or enforcement layers                  | `docs/maintenance.md`     |
| Understanding project dev setup scripts or install dependencies | `scripts/setup/README.md` |
