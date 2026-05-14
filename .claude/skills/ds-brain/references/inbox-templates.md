# INBOX Templates

Use these when filing a new note under `INBOX/`. Pick the closest `source_type`; if no template fits, use the free-form one and let the server-side ingest route it.

All templates assume filename pattern `INBOX/YYYY-MM-DD-<kebab-slug>.md`.

---

## Meeting note

```markdown
---
title: <Meeting topic — short>
created_at: 2026-05-14
created_by: <user email>
source_type: meeting
status: inbox
meeting_date: 2026-05-14
participants:
  - "[[Inbar Dekel]]"
  - "[[Aviad Cohen]]"
related_projects:
  - "[[Tipper]]"
related_people: []
tags: [inbox, meeting]
---

# <Meeting topic>

## Context
One short paragraph: why this meeting happened, what triggered it.

## Decisions
- Decision 1 — who decided, what scope.
- Decision 2.

## Discussion highlights
- Key point A.
- Key point B.

## Action items
- [ ] <person> — <action> — due <date>
- [ ] <person> — <action>

## Open questions
- Question 1.
- Question 2.

## Raw notes (optional)
Verbatim fragments worth preserving — quotes, numbers, links.
```

---

## Insight / conversation capture

For "save this conversation" or "remember this for the team."

```markdown
---
title: <Insight in 5–10 words>
created_at: 2026-05-14
created_by: <user email>
source_type: insight
status: inbox
related_projects: []
related_people: []
tags: [inbox, insight]
---

# <Insight title>

## TL;DR
One or two sentences — the takeaway someone reading cold should walk away with.

## Context
What were we discussing? What problem prompted this?

## The insight
The substantive content. Distilled, not a transcript dump.

## Assumptions
- Assumption 1 — and why it might be wrong.

## Open questions
- What we still don't know.

## Action items (optional)
- [ ] Follow-up to validate.
```

---

## Raw material drop

For uploaded docs, transcripts, exported files, pasted content the user wants in the brain.

```markdown
---
title: <Short description of the artifact>
created_at: 2026-05-14
created_by: <user email>
source_type: raw
status: inbox
origin: <where the artifact came from — Slack DM, email, Drive, etc.>
related_projects: []
related_people: []
tags: [inbox, raw]
---

# <Artifact title>

## Origin
Where this came from, when, who shared it, what context.

## Why it's worth filing
One sentence — what makes this brain-worthy.

## Content
<paste / summarize the artifact here. If it's a large binary, reference it and note that the binary should be added separately by a maintainer.>
```

---

## Link / external reference

```markdown
---
title: <Title of the resource>
created_at: 2026-05-14
created_by: <user email>
source_type: link
status: inbox
url: https://example.com/path
author: <if known>
related_projects: []
related_people: []
tags: [inbox, reference]
---

# <Title>

**URL:** https://example.com/path

## Why it matters
One paragraph — what's in the link, why a DS-team reader should care, what it connects to (`[[Concept]]`, `[[Project]]`).

## Notes
Optional: quotes, key points, your reactions.
```

---

## Decision draft

For decisions the user wants to *propose* — the final canonical Decision page is owned by the server-side ingest.

```markdown
---
title: <Decision in 5–10 words>
created_at: 2026-05-14
created_by: <user email>
source_type: decision-draft
status: inbox
decision_date: 2026-05-14
deciders:
  - "[[Inbar Dekel]]"
related_projects: []
tags: [inbox, decision]
---

# Decision: <title>

## Context
What's the situation that demanded a decision?

## Options considered
- Option A — pros / cons.
- Option B — pros / cons.

## Decision
What we chose, and why.

## Consequences
- Positive: …
- Negative: …
- Reversible? Yes / No / Partial.

## Open questions
- What we still need to validate.
```

---

## Wiki update request

For "update the X page" — never edit wiki directly; file the request.

```markdown
---
title: Update request — <target page>
created_at: 2026-05-14
created_by: <user email>
source_type: wiki-update-request
status: inbox
target: "[[Aviad Cohen]]"
tags: [inbox, update-request]
---

# Update request: [[Aviad Cohen]]

## Field(s) to change
- `title`: "Senior AI Architect" → "Principal AI Architect"

## Reason
Promotion effective 2026-05.

## Evidence
- HRIS update screenshot in Slack (link if available)
- Confirmed by [[Inbar Dekel]]
```

---

## Delete / removal request

For "remove this from the brain."

```markdown
---
title: Removal request — <target>
created_at: 2026-05-14
created_by: <user email>
source_type: wiki-update-request
status: inbox
target: "[[Stale Project Name]]"
removal_mode: archive   # or "hard-delete" — server-side ingest decides
tags: [inbox, removal-request]
---

# Removal request: [[Stale Project Name]]

## Reason
Project was cancelled 2026-Q1. Note is no longer accurate and no one is maintaining it.

## Scope
- The project entity page.
- Backlinks from related meetings and decisions should be updated, not deleted.
```

---

## Free-form (when nothing else fits)

```markdown
---
title: <Short title>
created_at: 2026-05-14
created_by: <user email>
source_type: free-form
status: inbox
tags: [inbox]
---

# <Title>

Whatever the user wanted captured. The server-side ingest will route it.
```
