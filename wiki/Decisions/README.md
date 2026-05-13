---
title: Decisions — Folder Guide
type: readme
created: 2026-05-05
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Decisions/

DS-leadership decisions / ADRs (org design, hiring, budget, project
go/no-go, scoping). Always include WHY + tradeoff.

### Filename

`YYYY-MM-DD — <decision title>.md`.

### Frontmatter

```yaml
---
title: <decision title>
type: decision
tags: [decision, wiki]
date: YYYY-MM-DD
deciders: [[<First Last>]]
status: <proposed | accepted | superseded | reversed>
supersedes: [[YYYY-MM-DD — <old decision>]]
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <decision title> — YYYY-MM-DD

## Context

## Decision

## Why

## Alternatives considered

## Consequences

## Open questions
```
