---
title: Systems — Folder Guide
type: readme
created: 2026-05-07
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Entities/Systems/

One synthesised note per product / component / external system the team
integrates with. Distinct from `Projects/` — Systems covers stable product
surfaces, third-party tools, and platform components consumed or extended
by the team.

### Filename

`<System name>.md` (no prefix).

### Frontmatter

```yaml
---
title: <System name>
type: system
tags: [system, wiki]
owner: <Cybereason team | vendor | open-source>
vendor: <if external>
integration_surface: [API, file-drop, message-bus]
related_projects: [[Project A]]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <System name>

> One-sentence: what this system does.

## Owner / vendor

## Integration surface

## Data flow

## Current usage

## Known issues

## Related entities

## Open questions
```
