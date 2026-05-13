---
title: Sources — Folder Guide
type: readme
created: 2026-05-11
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Sources/

One-page summary per external source the wiki cites (paper, blog post,
talk, slack export, customer interview). Created at `/ingest` time when
the source is external.

### Existing seeds

Two already in place:
- `Karpathy — LLM Wiki Gist.md` — canonical spec for this vault
- `LevelBlue — Acquisition of Cybereason.md` — active org context

Both need a Phase 2.14 retag pass to add the mandatory `wiki` tag.

### Filename

`<slug>.md` — title-case OK; year suffix optional. No path slashes.

### Frontmatter

```yaml
---
title: <full title>
type: source
tags: [source, wiki, source_type/<paper|talk|blog|slack|interview|deck>]
authors: [<name>, <name>]
year: YYYY
url: https://...
raw_path: raw/<tab>/<file>     # post-ingest location
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <full title>

> One-sentence headline finding.

## Summary

3–8 bullet points — synthesised takeaways, not a verbatim abstract.

## Why we care

## Cited from

(Append-only. Wikilink per citing page.)

## Open questions
```
