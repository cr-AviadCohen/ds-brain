---
title: Alert Logic
type: system
tags: [system, wiki]
owner: Level Blue (inherited via Fortra acquisition, 2025)
vendor: Level Blue
integration_surface: [saas, log-pipeline]
related_projects: []
related_decisions: ["[[2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects]]"]
last_updated: 2026-05-12
---

# Alert Logic

> Managed MDR / XDR / WAF platform inherited by Level Blue via the 2025 Fortra acquisition — surfaced as a candidate DS-team scope (ML log-review pipeline) by Pawel Knapczyk in April 2026.

## Owner / vendor

Originally Alert Logic (independent MSSP, founded 2002), acquired by Fortra; passed to Level Blue as part of the 2025 Fortra's Alert Logic managed-services acquisition. Now sits under Level Blue's managed security services portfolio alongside Cybereason and Trustwave assets.

## Integration surface

- SaaS — managed detection & response, web application firewall, log analytics.
- Customer log ingestion endpoints feed an internal ML pipeline used for compliance log review and anomaly detection.

## Data flow

Customer logs → Alert Logic ingestion → managed-detection pipeline (including an autonomous ML anomaly-detection stage for compliance review) → analyst triage / response.

The ML pipeline has run autonomously for over a year without retuning (per [[Pawel Knapczyk]], 2026-04-30). High-level discussions involving Ziv Mador and Keith are exploring integration of that pipeline into [[Phoenix]].

## Current usage

External — Level Blue customer base via the Alert Logic managed service. No current DS-team integration. Referenced by [[2026-04-30 — Aviad and Pawel intro]] and [[2026-05-06 — DS team and Santi handover]] as a candidate platform for DS-team takeover or improvement.

## Known issues

- ML log-review pipeline running autonomously > 12 months without retuning (per Pawel, 2026-04-30) — drift risk unmeasured.

## Related entities

- People: [[Pawel Knapczyk]] (raised the opportunity), [[Aviad Cohen]].
- Systems: [[Phoenix]] (potential integration target).
- Meetings: [[2026-04-30 — Aviad and Pawel intro]], [[2026-05-06 — DS team and Santi handover]].
- Decisions: [[2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects]].

## Open questions

- Scope of the ML pipeline — model architecture, training data, evaluation metrics?
- Ownership transfer feasibility (is the pipeline within Level Blue boundary or still managed by Fortra remnants)?
- Integration target — Phoenix vs. standalone refresh?
- Brownbag scheduling — Pawel invited a session; when does it land on the team calendar?
