---
title: Velociraptor
type: system
tags: [system, wiki]
owner: Velocidex (open-source — now Rapid7)
vendor: open-source / Rapid7
integration_surface: [endpoint agent, VQL queries, artifact collection]
related_projects: []
last_updated: 2026-05-12
---

# Velociraptor

> Open-source DFIR endpoint agent — referenced by AI Assistant + Cybereason core docs as a complementary forensics tool.

## Owner / vendor

Originally Velocidex (Mike Cohen) — acquired by Rapid7 in 2021. Remains open-source under AGPL.

## Integration surface

- Endpoint agent (cross-platform) — Windows / macOS / Linux.
- VQL (Velociraptor Query Language) — SQL-like artefact / hunt queries across deployed endpoints.
- Artifact collection — file, registry, memory, log harvest with custom artifacts.

## Data flow

External — analysts/IR teams deploy the Velociraptor agent on hosts of interest, then hunt across them via VQL. Output is artefact collections returned to a central server. Referenced in Cybereason internal docs and the [[AI Assistant]] roadmap as a complementary deep-forensics tool alongside Core / Phoenix telemetry.

## Current usage

External reference only — not deployed inside Cybereason / Level Blue stacks. Mentioned as a tool analysts may invoke during incident triage.

## Known issues

(none captured)

## Related entities

- Projects: [[AI Assistant]] (referenced in roadmap).

## Open questions

- Is there a concrete integration plan from [[AI Assistant]] into Velociraptor (VQL generation, artefact ingest)?
- Would Level Blue analysts ever consume Velociraptor output back into [[Phoenix]] / [[Core]]?
