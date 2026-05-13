---
title: Organizations — Folder Guide
type: readme
created: 2026-05-12
updated: 2026-05-12
tags: [readme, folder-guide]
---

# Entities/Organizations/

One canonical note per **organization** the DS team interacts with —
employers, parent/sibling companies, vendors, customers, regulators,
open-source foundations, research labs.

Distinct from:
- `Entities/Teams/` — sub-units WITHIN an Organization (e.g. `Data Science Team` under `Cybereason`)
- `Entities/Systems/` — products/components (a System has an Owner that is an Organization wikilink)
- `Entities/People/` — humans (a Person's `org:` field wikilinks here)

### Examples

- `Cybereason.md` — current parent (post-acquisition)
- `Level Blue.md` — acquirer (Nov 2025)
- `Trustwave.md` — sister acquisition (now Level Blue)
- `AT&T.md` — historical parent of Level Blue's MSSP business
- `SoftBank.md`, `WillJam Ventures.md`, `Liberty Strategic Capital.md` — investors
- `Anthropic.md`, `OpenAI.md`, `LangChain Inc.md` — LLM vendors
- `MITRE.md`, `OASIS.md` — standards bodies
- `SpiderLabs.md` — formerly Trustwave research arm

### Filename

`<Organization name>.md` — exact display name. Ampersands OK
(`AT&T.md`). No legal-entity suffixes (`Inc.`, `Ltd.`) in filename
unless they're part of the canonical name.

### Frontmatter

```yaml
---
title: <Organization>
type: organization
tags: [organization, wiki]
kind: <employer | parent | acquirer | sibling | vendor | customer | investor | regulator | standards-body | open-source>
hq: <city, country>
parent: ["[[<Org>]]"]            # if subsidiary
acquired_by: ["[[<Org>]]"]       # if acquired
acquired_on: YYYY-MM-DD          # if acquired
website: https://...
related_teams: ["[[<Team>]]"]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <Organization>

> One-sentence orientation: what they do, why the DS team cares.

## What they do

## Relationship to DS team

(Employer / parent / vendor / customer / partner. Cite the moment the
relationship started.)

## Key people

(Bulleted wikilinks to People who work at this Org or are key contacts.)

## Teams

(Bulleted wikilinks to sub-units in `Entities/Teams/`.)

## Systems

(Bulleted wikilinks to products/services this Org owns or runs.)

## Open questions
```

### Update workflow

Created or extended by `/ingest` when a source mentions a new org. Org
pages should always be wikilink-targets, never wikilink-sources for the
acquisition chain — link upward via `parent:` / `acquired_by:`
frontmatter, not via prose.
