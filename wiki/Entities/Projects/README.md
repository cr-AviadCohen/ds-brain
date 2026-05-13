---
title: Projects — Folder Guide
type: readme
created: 2026-05-05
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Entities/Projects/

One synthesised canonical note per active DS project. Source artifacts
(decks, drawio, design docs) stay under
`raw/projects/{Project,Itamar Project} - <name>/`.

### Filename

`<Project name>.md` — drop the `Project - ` or `Itamar Project - ` prefix
from the raw folder. Use the team's canonical short name.

### Frontmatter

```yaml
---
title: <Project name>
type: project
tags: [project, wiki]
status: <proposed | active | paused | completed | archived>
lead: [[<First Last>]]
team: [[<First>]], [[<Last>]]
started: YYYY-MM-DD
target_ship: YYYY-MM-DD
systems: [[Tipper]], [[URLDeep]]
related_decisions: [[2026-04-15 — go on AIDRA]]
raw_path: raw/projects/Project - <name>/
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <Project name>

> One-sentence problem statement.

## Goal

## Approach

## Status

## Decisions

## Risks

## Mentions

## Open questions
```
