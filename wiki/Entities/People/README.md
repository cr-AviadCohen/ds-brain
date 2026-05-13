---
title: People — Folder Guide
type: readme
created: 2026-05-05
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Entities/People/

One canonical synthesised note per person the team interacts with. Source
seeds live in `raw/people/<First Last>.md`; this folder holds the richer
evolving note.

### Filename

`<First Last>.md` — exact display name, English. No emoji, no
parenthetical role.

### Frontmatter

```yaml
---
title: <First Last>
type: person
tags: [person, wiki]
role: <current role>
org: <Cybereason | Level Blue | vendor | external>
team: <team name>             # optional
seeds: [raw/people/<First Last>.md]
related_projects: [[Project A]], [[Project B]]
first_seen: YYYY-MM-DD
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <First Last>

> One-sentence orientation in DS context.

## Background

## Mentions

Append-only timeline.
- 2026-05-08 — [[2026-05-08 — Tipper rollout retro]] — proposed fallback
  classifier path

## Related entities

## Open questions
```

### Update workflow

Appended to by `/ingest` (Phase B) when an external source mentions them.
Never rewrite the whole page — append `## Mentions` rows and bump
`last_updated`.
