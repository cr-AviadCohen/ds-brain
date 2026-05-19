---
title: URL System
type: system
tags: [system, wiki, url-scan, threat-intel]
owner: "[[Labs]]"
vendor: internal (Level Blue / SLR)
integration_surface: [ioi-pipeline, url-scan]
related_projects: ["[[Infrastructure of Interest]]"]
last_updated: 2026-05-19
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
---

# URL System

> Internal URL-scanning service used as an enrichment source inside [[Infrastructure of Interest]]. Functional equivalent of urlscan.io / VT-URL but operated by SLR Labs so observations stay inside the [[LevelBlue]] perimeter and don't tip off threat actors monitoring public URL-scan queues.

## Owner / vendor

Internal SLR Labs service.

## Integration surface

- Input: domain / URL observations awaiting enrichment in IOI.
- Output: rendered-page artifacts, content morphology fingerprints, screenshots, sub-resource graph — consumed by the [[Infrastructure of Interest]] flag-scoring stage and downstream by [[Campaign Assembler]] (content-morphology evidence dimension).

## Current usage

- Standard enrichment hop for every observation in [[Infrastructure of Interest]] post-whitelist.
- Complements external Shodan IP scans (URL System covers HTTP layer; Shodan covers transport / banners / TLS).

## Why internal

Public URL-scan submissions are observable by attackers. Submitting a freshly-flagged suspicious URL to urlscan.io can warn the operator and trigger infrastructure teardown before customer protections deploy. The internal URL System avoids this leak.

## Related entities

- Projects: [[Infrastructure of Interest]].
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- Stack / framework (Chromium headless? Playwright? Custom?).
- Retention policy on rendered artifacts.
- Could this surface be exposed to other Level Blue / Cybereason teams (DS, IRCA, AI Assistant)?
