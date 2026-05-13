---
title: Teams — Folder Guide
type: readme
created: 2026-05-12
updated: 2026-05-12
tags: [readme, folder-guide]
---

# Entities/Teams/

One canonical note per **team / sub-unit** within an Organization. A Team
sits inside an Organization and contains People; it owns Projects and
consumes/produces Systems.

Distinct from:
- `Entities/Organizations/` — the legal/parent entity. A Team's `org:`
  field wikilinks there.
- `Entities/People/` — individuals. A Person's `team:` field wikilinks
  here.

### Examples

- `Data Science Team.md` — DS team (the wiki's owners)
- `Security Research.md` — Cybereason SR org-unit
- `Spider Labs.md` — Trustwave/Level Blue threat research
- `Engineering.md` — Cybereason engineering org-unit
- `Security Operations Center.md` — Cybereason SOC
- `Labs.md` — Cybereason Labs sub-unit
- `Phoenix Team.md` — Cross-functional product team owning [[Phoenix]]
- `Fusion 2 Team.md` — Level Blue analyst-platform team

### Filename

`<Team name>.md` — Title Case English. No abbreviations unless
canonical (e.g. `SOC.md` would be `Security Operations Center.md`; abbr
fine in body prose).

### Frontmatter

```yaml
---
title: <Team>
type: team
tags: [team, wiki]
org: ["[[<Organization>]]"]
lead: ["[[<Person>]]"]
members: ["[[<Person>]]"]
mission: <one-sentence mission>
related_projects: ["[[<Project>]]"]
related_systems: ["[[<System>]]"]
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <Team>

> One-sentence mission.

## Mission

(2-4 lines. What this team is responsible for.)

## Members

(Bulleted wikilinks to People. Lead first, then alphabetical.)

## Projects

(Bulleted wikilinks to Projects this team owns or contributes to.)

## Systems

(Bulleted wikilinks to Systems this team operates or integrates with.)

## Working norms

(Optional — cadences, on-call, shared rituals.)

## Open questions
```

### Update workflow

A Team page is created the first time `/ingest` encounters a named team
in a source. Membership is append-only — when someone leaves, edit the
Person page to mark history but keep the Team page accurate to current
state.
