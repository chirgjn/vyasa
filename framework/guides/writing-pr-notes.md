# Writing PR Change Notes

How to write `docs/archive/pr-reviews/pr-<number>-changes.md` files — reviewer-facing
explanations of the decisions and constraints that shaped a non-trivial PR. For the
taxonomy that places these in `docs/archive/pr-reviews/`, see
`framework/managing-project-information.md` § "Ephemeral."

---

## When to Write One

Write a PR change notes file when the PR contains decisions a reviewer can't reconstruct
from the diff alone — non-obvious dependency choices, module splits, import constraints,
tradeoffs accepted and why.

**Write one when:**

- A dependency was promoted from optional to hard, or added where none existed
- A module was split or restructured for reasons not visible in the code (e.g. import cycles)
- One approach was chosen over a plausible alternative
- A constraint shaped the implementation (licence restriction, build-time error, API
  limitation)
- The PR spans multiple logical changes that need independent explanation

**Don't write one when:**

- Every change is self-evident from the diff and commit messages
- The PR is a pure mechanical change (rename, reformat, version bump)

---

## Format

One section per logical change. Number them sequentially starting from 0.

```markdown
# PR <number> — Change Notes

## Change 0 — <short title>

**What:** One sentence describing the change.

**Why:** The problem, constraint, or goal that motivated it. Include rejected
alternatives if the choice was non-obvious.

---

## Change 1 — <short title>

**What:** ...

**Why:** ...
```

---

## Section-by-section guidance

### What

One sentence. Describe the observable change — what was added, removed, or restructured.
Not how it works, not why. If you need more than one sentence, the change probably
deserves two sections.

**Bad:** "Extracted session.py and thread_utils.py from socket_mode.py and updated all
imports to use the new paths, fixing the circular import that occurred at startup when
mention_handler and command_handler were loaded."

**Good:** "Extracted `session.py` and `thread_utils.py` from `socket_mode.py`."

### Why

The motivation. This is where the reasoning lives — what problem existed, what constraint
forced the approach, what alternatives were rejected and why. Write enough that a reviewer
understands the decision without reading the full diff.

Include:

- The problem that forced the change ("circular import at startup")
- Constraints that ruled out simpler approaches ("lazy imports remain unavoidable for X
  because...")
- Rejected alternatives when the choice was non-obvious

Omit:

- Implementation steps — describe the decision, not the sequence of edits
- Commit hashes or timestamps — use git log for history
- Details self-evident from the code
- Execution order and iteration history — write the final state of the decision, not
  how you arrived at it; a reviewer evaluates the outcome, not the journey

## Audience

The reader is a reviewer evaluating whether each decision was sound. Write to answer
the question they'll have when they see the diff: "why is it shaped this way?" — not
"what steps were taken?" The change notes complement the diff; they explain motivation
and constraints the code itself cannot communicate.

---

## Naming

```
docs/archive/pr-reviews/pr-<number>-changes.md
```

Examples: `pr-37-changes.md`, `pr-112-changes.md`

For iterative review loops (review comments → fixes → re-review), use round suffixes:

```
pr-<number>-review-r<round>.md   — reviewer feedback for round N
pr-<number>-fixes-r<round>.md    — fix log for round N
```

---

## Relationship to ADRs

PR change notes are ephemeral — they explain the PR to reviewers and are archived after
merge. If a decision in the notes has wider impact (others might apply the same reasoning
elsewhere, or reverse the decision without knowing why), extract it as an ADR in
`docs/decisions/`. See `framework/guides/writing-decision-records.md`.

The test: will this reasoning matter to someone working in a different part of the codebase
six months from now? If yes, ADR. If no, the change note is enough.
