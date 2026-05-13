---
title: Syntheses — Folder Guide
type: readme
created: 2026-05-05
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Syntheses/

LLM-generated answers worth keeping (file-back-queries pattern from
Karpathy). Created from `/query` when filing is approved, or at monthly
cadence to capture "what's shifted" overviews.

### Filename

`YYYY-MM-DD — <question or theme>.md`.

### Frontmatter

```yaml
---
title: <question or theme>
type: synthesis
tags: [synthesis, wiki]
derived_from: [[Page A]], [[Page B]], [[Page C]]
asker: [[<First Last>]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <question or theme>

> One-sentence headline answer.

## Answer

(Every claim cited inline via [[wikilink]]. No uncited claims.)

## Follow-up questions
```
