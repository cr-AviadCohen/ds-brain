---
title: Concepts — Folder Guide
type: readme
created: 2026-05-12
updated: 2026-05-12
tags: [readme, folder-guide]
---

# Entities/Concepts/

Atomic named ideas, techniques, terminology, or frameworks the team
references. Lighter-weight than `wiki/Research/` — Concepts is a
glossary/atom layer; Research is page-length analysis with citations.

Examples: `LoRA.md`, `Prompt Injection.md`, `Sigma Rule Format.md`,
`Embedding Similarity.md`, `RAG.md`, `Function Calling.md`.

When a Concept page grows past ~1 screen of synthesis or gets ≥3
external citations, promote it to `wiki/Research/`.

### Filename

`<Concept>.md` — Title Case English. No emoji. Use the canonical
spelling the team uses.

### Frontmatter

```yaml
---
title: <Concept>
type: concept
tags: [concept, wiki]
domain: <ml | nlp | security | ops | eval | ai-infra>
related_projects: ["[[<Project>]]"]
related_systems: ["[[<System>]]"]
derived_from: ["[[<Source>]]"]   # if seeded from a wiki/Sources/ page
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <Concept>

> One-sentence definition.

## What it is

(2-4 lines. Minimal working example or analogy.)

## Why we care

(How it shows up in DS team's work. Wikilinks to Projects, Systems,
Decisions.)

## Manifestations

(Append-only — every wikilink-with-date where this concept showed up.)

## Tensions

(If sources disagree, list both with wikilinks.)

## Open questions
```

### Update workflow

Concepts are created or appended by `/ingest` when a source introduces a
new term. Promote to `Research/` once the page outgrows the schema.
