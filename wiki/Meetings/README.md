---
title: Meetings — Folder Guide
type: readme
created: 2026-05-05
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Meetings/

Distilled outcomes from `raw/meetings/meeting_*` transcripts. One note per
meeting. Source filenames are inconsistent (`meeting_2026-01-29_X`,
`meeting_2026.04.27_x_y.txt`) — normalise the wiki filename.

### Filename

`YYYY-MM-DD — <topic>.md`.

### Frontmatter

```yaml
---
title: <topic>
type: meeting
tags: [meeting, wiki]
date: YYYY-MM-DD
participants: [[<First Last>]], [[<First Last>]]
related_projects: [[Project A]]
related_decisions: []
source: raw/meetings/meeting_<original>.txt
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <topic> — YYYY-MM-DD

> One-sentence outcome.

## Decisions

## Action items

- [ ] <task> — [[<owner>]] — due YYYY-MM-DD

## Discussion notes

(Distil, never transcribe.)

## Open questions
```
