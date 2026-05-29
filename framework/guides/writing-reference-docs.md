# Writing Reference Docs

How to structure, cross-link, and size reference docs (`docs/*.md`), and how to decide what belongs in any section. For doc type placement — which bucket a piece of information belongs in — see `framework/managing-project-information.md`.

______________________________________________________________________

## Structure Template

Every reference doc should follow this skeleton:

```markdown
# [Topic Name]

[1-2 sentences: what this doc covers and when to read it.]
[Optional: "For [related topic], see `docs/other.md`."]

## [Core content sections]

...

## Common Patterns

[2-3 examples of the most frequent use cases.]

## Pitfalls

[What goes wrong and how to avoid it. Skip if nothing non-obvious.]
```

______________________________________________________________________

## What belongs in a doc

Before writing any section, ask three questions. They apply to any doc type — spec, reference, guide, architecture doc.

**Does it save real reading time?** A section earns its place by saving time a reader would otherwise spend recovering the same information from code or other sources. The ratio test: if the doc text is more than five times the size of the code it describes, the section is likely noise — a reader could open the file directly and be done. When the ratio flips, the doc is clearly earning its place. Use this not just to decide whether to write a section, but how terse to make it: field names inline instead of a JSON block, a sentence instead of a table.

**Does it preserve the why?** Always keep the why, regardless of ratio. Design decisions, non-obvious constraints, tradeoffs that were consciously made — none of these are recoverable from code. If the only record of *why* a constraint exists is in someone's head, it belongs in the doc (or an ADR linked from it). Even a short block of code earns documentation when the doc explains why it exists, not just what it does.

**Would losing it cause mistakes?** The strongest case for any piece of content: without it, a reader would make a wrong assumption causing a bug or a bad design decision. Non-obvious error codes, edge cases in sequencing, invariants not enforced by types — these cause real mistakes when undocumented. Content that merely mirrors readable code does not.

______________________________________________________________________

## What Makes a Reference Doc Useful

| Quality | What it means | Failure mode without it |
|---|---|---|
| **Self-contained** | Usable without reading other docs — include minimum context (commands, paths) | Reader bounces to another doc and loses track |
| **Task-oriented** | Organized by what the reader wants to do, not by system component | A doc organized by module is a code tour, not a guide |
| **Example-heavy** | At least one concrete example per pattern | Abstract rules get misapplied |
| **Scoped opening** | First 2 lines: what this doc is for and what it's not | Reader wastes time on the wrong doc |
| **When before how** | Sections open with when, then succinct why, then how | Reader can't tell if a section applies without reading all of it |
| **Cross-linked** | Related docs acknowledged: "this is for X, that is for Y" | Reader finds the wrong doc |

______________________________________________________________________

## Cross-Linking with Disambiguation

When two docs cover related ground, each should acknowledge the other and explain when to use which:

```markdown
<!-- At the top of docs/setup.md -->
This guide covers dev environment setup from scratch.
For deploying to staging/production, see `docs/deployment.md`.
```

```markdown
<!-- At the top of docs/api.md -->
This guide covers API endpoint conventions and request/response patterns.
For the auth flow specifically, see the sequence diagram in this doc under "Authentication."
For error response conventions, see `docs/guides/error-handling.md`.
```

Don't just say "see also" — explain when to read which.

______________________________________________________________________

## Self-Contained Files

Each doc should be usable without reading other docs. Don't write "See setup.md for how to run tests" — include the command here too.

**Repetition test:** Under 3 lines and saves a hop → repeat it. Over 3 lines → link to canonical source.

______________________________________________________________________

## Sizing

| Length | Action |
|---|---|
| Under ~15 lines | Too thin — merge into a related doc |
| 15–200 lines | Ideal range for a single reference doc |
| 200–400 lines | Consider splitting, but only if sections are independently useful |
| Over 400 lines | Split into a subdirectory. Each file should stand alone |

When splitting, each file needs its own scoped opening and must stand alone.

______________________________________________________________________

## Writing Tutorials

Use when creating step-by-step guides — setup docs, onboarding, "getting started." Tutorials prioritize clarity over completeness. Best written your first week on a team, when you don't know what to assume.

### Process

1. Go through the process yourself, taking notes
1. Write every step assuming zero domain knowledge
1. State prerequisites at the top
1. Edit down to only user actions

### Rules

- **Number only user actions** — not system responses
- **Combine atomic actions** — no decision between them = one step
- **Commands and output on separate lines, in monospace**
- **Never skip auth, permissions, or environment setup** — these cause "step 4 errors"

### Example

**Bad** — numbers system responses, splits atomic actions:

```
4. The system will authenticate you
5. A database named "baz" will be created
6. Test the database
7. Type: CREATE DATABASE my_db;
```

**Good** — only user actions, combined steps:

```
3. Run the script. The system authenticates and creates database "baz".
   $ cd ~; foobar.sh

4. Test the database:
   baz:$ CREATE DATABASE my_db;
```
