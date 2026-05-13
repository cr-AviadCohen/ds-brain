---
title: 50-50 DS Bandwidth Split Between Phoenix and Spider Labs
type: decision
tags: [decision, wiki]
date: 2026-05-06
deciders: ["[[Inbar Dekel]]", "[[Santiago Cortes Diaz]]"]
status: accepted
related_projects: ["[[Phoenix Review]]"]
last_updated: 2026-05-11
---

# 50-50 DS Bandwidth Split Between Phoenix and Spider Labs — 2026-05-06

## Context

At the 2026-05-06 DS team / Santi handover, Santi pushed for a guaranteed slice of DS-team time on internal threat-intelligence research, citing the risk of being entirely consumed by [[Phoenix]] platform PMs who are "always in a hurry". Inbar needed a defensible bandwidth model that protected both the platform commitment and the new Spider Labs project portfolio.

## Decision

Approximately 50/50 split of DS-team bandwidth between [[Phoenix]] platform work and Spider Labs internal projects, with the explicit commitment to keep at least one high-priority internal project actively moving at all times. Elasticity is reserved for urgent platform needs but the internal-projects share is not allowed to collapse to zero.

## Why

The DS team's value is split between platform feature work (where PM-driven deadlines dominate) and internal capability work (where compound returns accrue more slowly). A formal split prevents the typical failure mode where short-term PM pressure crowds out internal capability investment, and codifies Santi's working principle that engineering bandwidth should be partially insulated from product roadmaps.

## Alternatives considered

- Pure on-demand allocation against PM-driven Phoenix tickets — rejected: would predictably starve Spider Labs internal projects.
- A more aggressive Spider Labs tilt (e.g. 70/30) — not requested; Inbar wanted to preserve responsiveness to Phoenix.

## Consequences

- Phoenix-side commitments must be planned around half of nominal DS capacity, not full capacity.
- At least one Spider Labs internal project (initially the Martin News OSINT chatbot) is always in active flight.
- Future capacity discussions can reference this baseline rather than re-negotiating per project.

## Open questions

- How is "elasticity for urgent platform needs" governed in practice — who calls it, and against what limit?
- How does the split adjust if the team adds headcount or a Spider Labs project enters a heavy delivery phase?
