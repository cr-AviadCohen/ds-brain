---
title: Locations — Folder Guide
type: readme
created: 2026-05-11
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Entities/Locations/

One canonical note per geographic / office location the DS team operates from
or hires into. Locations are first-class entities so we can ask "who is in
Tel-Aviv?" and "what time zone is the Spain crew in?" by wikilink, not by
grep.

### Filename

`<Location>.md` — exact display name. `Tel-Aviv`, `Spain`, `Tokyo`, `Remote`,
`Warsaw Office`, `Waterloo Office`, `United States`.

Map raw values to canonical filenames:
- `Tel-Aviv` → `Tel-Aviv.md`
- `Remote Office` → `Remote.md`
- `Spain` → `Spain.md`
- `New Zealand` → `New Zealand.md`
- `Warsaw Office` → `Warsaw Office.md`
- `United States` → `United States.md`
- `Waterloo Office` → `Waterloo Office.md`
- `Tokyo` → `Tokyo.md`

### Frontmatter

```yaml
---
title: <Location>
type: location
tags: [location, wiki]
country: <country>
timezone: <IANA tz or short label>
office_type: <office | remote | hybrid>
last_updated: YYYY-MM-DD
---
```

### Body shape

```markdown
# <Location>

> One-sentence orientation: what this location is, why it matters to the team.

## People

Append-only. Wikilinks to every Person whose seed lists this Location.

- <Person wikilink> — <role>

## Notes

(Anything site-specific: time zone overlap, hiring nuances, office logistics.)

## Open questions
```

### Update workflow

When a new Person seed mentions a new Location, `/ingest` should create the
Location page if missing and append the Person to its `## People` section.
