---
description: Ask a question of the wiki and synthesise a cited answer
argument-hint: <question>
---

Answer this question against the wiki: **$ARGUMENTS**

Workflow:

1. **Read `wiki/INDEX.md` first** to find candidate pages.
2. **Drill into the 2–5 most-relevant wiki pages — read them all in a
   SINGLE message (parallel `Read` calls).** Optionally consult Smart
   Connections in the same batch for semantically nearest `raw/` notes.
3. **Synthesise an answer** — every claim cited with `[[wikilinks]]`. No
   uncited claims. If something can't be cited, say so explicitly.
4. **End by asking whether to file** this as
   `wiki/Syntheses/<YYYY-MM-DD> — <question>.md`.

Don't write any files until the user says yes to filing.

## When filing (after approval)

- Create the page using the template in `wiki/Syntheses/README.md` (include
  `derived_from: [<page A>, <page B>, ...]` frontmatter).
- Update `wiki/INDEX.md`.
- Prepend `## [YYYY-MM-DD] query | <question>` to `wiki/Log/wiki-ops.md`
  (newest on top, below the `---` preamble separator).
- Stage, commit `query | <question>`, push to `origin/unified`.

## Heuristics for whether filing is worth it

- Did the answer surface a connection not previously known?
- Would the team want to find this answer again in 6 months?
- Did it prompt new follow-up questions worth tracking?

If none, suggest skipping the file step.
