# vyasa

> **AI agent?** Read [AGENTS.md](AGENTS.md) first.

Opinionated documentation framework for AI-assisted projects — a taxonomy for where information lives, guides for writing each doc type, and an audit process for finding problems.

## What it contains

| Path                                        | What it is                                                                                                                    |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `framework/managing-project-information.md` | The placement authority — taxonomy, directory structure, and routing table for all writing guides                             |
| `framework/auditing-anti-patterns.md`       | What broken docs look like — wrong placement, missing framing, duplication, broken discoverability                            |
| `framework/guides/`                         | Writing guides for each doc type: prose style, conventions, diagrams, AGENTS.md, layout.md, ADRs, specs, designs, maintenance |

## How to use it

**Setting up docs for a new project:** start at `framework/managing-project-information.md`. It answers what type of doc you're writing, where it lives, and which guide covers how to write it well.

**Finding and fixing problems in existing docs:** start at `framework/auditing-anti-patterns.md`.

**Writing a specific doc type:** go directly to the relevant guide in `framework/guides/`.

## License

[MIT](LICENSE)
