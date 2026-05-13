---
title: Entities — Folder Guide
type: readme
created: 2026-05-11
updated: 2026-05-12
tags: [readme, folder-guide]
---

# Entities/

Every nameable thing the DS team cares about. Split by type:

- `Entities/People/` — humans (team members, stakeholders, vendors, candidates)
- `Entities/Teams/` — sub-units within an Organization (DS Team, SLR, Spider Labs, Engineering, …)
- `Entities/Organizations/` — companies, vendors, customers, investors, standards bodies (Cybereason, Level Blue, Trustwave, Anthropic, MITRE, …)
- `Entities/Projects/` — DS-owned R&D efforts
- `Entities/Systems/` — third-party / platform components the team
  integrates with (Tipper, Mail Marshal, URLDeep, …)
- `Entities/Concepts/` — atomic named ideas / techniques / frameworks (LoRA, Prompt Injection, Sigma Rule Format) — lighter-weight than `wiki/Research/`
- `Entities/Locations/` — geographic / office locations the team operates from

Each sub-folder has its own README defining its page template.

### Relationship layering

```
Organization → contains Teams → contains People
Team → owns Projects → consumes/produces Systems
Project / System / Decision → manifest Concepts
Person → has Location
```

Wikilinks freely cross all 7 layers.

### Cross-cutting rules

- Filename = canonical English display name (Projects: drop the
  `Project - ` / `Itamar Project - ` prefix).
- `wiki` tag mandatory; second tag is the entity type (`person`, `team`,
  `organization`, `project`, `system`, `concept`, `location`).
- Every entity page ends with `## Open questions`.
- Entities reference each other freely via Obsidian-style wikilinks.
