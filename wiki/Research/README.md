---
title: Research — Folder Guide
type: readme
created: 2026-05-05
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Research/

ML / AI / security concept notes (papers, frameworks, theories, evaluation
methodologies). Equivalent to `wiki/concepts/` in the reference vault,
scoped to DS subject matter.

### Filename

`<concept>.md`.

### Frontmatter

```yaml
---
title: <concept>
type: research
tags: [research, wiki]
domain: <ml | nlp | security | ops | eval>
derived_from: [[Source A]], [[Source B]]
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <concept>

> One-paragraph orientation.

## What it is

## Why we care

## Manifestations

(Append-only. Each entry: date, wikilink, one-line context.)

## Tensions

(If sources disagree, list both with wikilinks.)

## Open questions
```
