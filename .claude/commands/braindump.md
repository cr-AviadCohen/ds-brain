---
description: Append a free-form thought stream; Claude files it into appropriate wiki/ pages
argument-hint: <free-form thoughts, any length>
---

Take this braindump and file it into the wiki: **$ARGUMENTS**

## Workflow

1. **Acknowledge what was said.** Restate in 2–3 bullets to confirm
   understanding. Ask one clarifying question only if intent is ambiguous.

2. **Classify the content** into one or more buckets:
   - new fact about a Person / Project / System
   - new Idea / hypothesis
   - new Decision
   - new Connection (cross-domain pattern)
   - new Hot Note (active focus)
   - new entry on an existing page
   - candidate Source pointer

3. **Plan the writes.** List the wiki pages you'll create or modify, one
   line each. Wait for go-ahead.

4. **After approval, execute — parallelise independent writes.** Same
   Phase A / B / C / D structure as `/ingest`. Skip the raw/ move (no
   INBOX/ file involved unless the braindump references an attached file).

5. Prepend `## [YYYY-MM-DD] braindump | <one-line subject>` to
   `wiki/Log/wiki-ops.md` (newest on top, directly below the `---` preamble
   separator and the append-only convention note). Commit
   `braindump | <subject>`, push.

## Hard rules

- Wikilinks only. Frontmatter required. `wiki` tag mandatory.
- A braindump may seed a new Idea or Connection, but never a new Decision
  unless the user explicitly says "we decided X".
