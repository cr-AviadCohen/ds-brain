---
description: Drop free-form text (or given content) into INBOX/ as a structured Markdown note for later ingest
argument-hint: <text-or-path-or-empty-for-conversation-context>
---

File `$ARGUMENTS` into `INBOX/` as a new note per `CLAUDE.md` § Operations
and the `ds-brain` skill's `references/inbox-templates.md`.

This command is the **thin write-only counterpart** to `/ingest`. It never
touches `wiki/`, `raw/`, or any structural file — it only deposits a
well-formed source note that the server-side ingest pipeline
(`server/jobs/auto_ingest.py` → `/auto-ingest`) picks up later.

## Input modes

- `$ARGUMENTS` is a **file path** → read the file, treat as raw artifact
  drop (`source_type: raw`).
- `$ARGUMENTS` is **inline text** (a sentence, paragraph, URL, paste) →
  treat as the body to capture; pick `source_type` by heuristic (see
  below).
- `$ARGUMENTS` is **empty** → capture the recent conversation context. Ask
  one short clarifying question only if intent is ambiguous: "Drop this
  conversation into INBOX as an insight, a meeting note, or free-form?"

## Source-type heuristic

Pick automatically; fall back to `free-form` if unsure:

| Signal | `source_type` |
|--------|---------------|
| Single URL or URL + short note | `link` |
| "we decided / we will / adopted / rejected" + decider names | `decision-draft` |
| "meeting with X / standup / sync" + participants + date | `meeting` |
| "update the [[X]] page", "X's title changed", "fix on [[Y]]" | `wiki-update-request` |
| "remove / archive / delete [[X]]" | `wiki-update-request` (`removal_mode`) |
| Distilled takeaway from a discussion | `insight` |
| Uploaded artifact / pasted long content | `raw` |
| Anything else | `free-form` |

## Workflow

1. **Resolve content.** Read the file if path-mode; otherwise capture the
   inline text or conversation distillation. Do not dump verbatim
   transcript — distill if it's a conversation.

2. **Compose the note** using the matching template in
   `.claude/skills/ds-brain/references/inbox-templates.md`. Required
   frontmatter (minimum):

   ```yaml
   ---
   title: <short descriptive title>
   created_at: <today YYYY-MM-DD>
   created_by: <git config user.email>
   source_type: <meeting | insight | raw | link | decision-draft | wiki-update-request | free-form>
   status: inbox
   tags: [inbox, <source_type>]
   ---
   ```

   Add the optional fields the template lists (`participants`,
   `related_projects`, `url`, `meeting_date`, `target`, `removal_mode`,
   `origin`) when the signal is in the input. Wikilinks only (`[[Name]]`).

3. **Filename.** `INBOX/<YYYY-MM-DD>-<kebab-slug>.md`. Date = event date
   if explicit in input, else today. Slug = 3–6 words, lowercase, kebab.
   Bail if the file already exists; append a `-2` suffix and retry.

4. **Write + commit + push.**
   - `Write` the file under `INBOX/`.
   - `git add` only that file.
   - `git commit -m "inbox | <subject>"` (lowercase op, pipe, subject —
     matches existing convention).
   - `git push origin unified`.

5. **Final report.** One-line summary: filename, `source_type`, commit
   SHA, push result. Tell user the server-side `auto-ingest` daemon will
   process it on its next tick.

## Hard rules

- **Write only under `INBOX/`.** Never `wiki/`, `raw/`, `.claude/`,
  `tools/`, `server/`. The `guard_immutable.py` PreToolUse hook blocks
  `raw/`; the other paths are off-limits by convention.
- **No `/ingest` invocation.** This command files; ingest is a separate
  cycle.
- **No subagents, no parallel dispatch.** Single file, single commit.
- **Never `git push --force`. Never `--no-verify`.**
- Op token in commit message is `inbox` (distinct from `ingest`,
  `auto-ingest`, `lint`, `remove`) so the audit trail separates raw
  deposits from synthesis events.
- One file per `/inbox` invocation. Multi-source drops → call `/inbox`
  per source.

## What this command is NOT

- Not `/ingest`. Filing ≠ synthesis. Wiki pages are never created here.
- Not a wiki editor. Wiki changes go through INBOX as
  `wiki-update-request` notes; the central ingest decides whether to
  apply.
- Not interactive triage. For multi-file decisions and destination
  routing, use `/ingest`.
