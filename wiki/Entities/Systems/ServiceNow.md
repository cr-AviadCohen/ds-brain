---
title: ServiceNow
type: system
tags: [system, wiki]
owner: ServiceNow Inc.
vendor: ServiceNow
integration_surface: [api, webhook, table-api]
related_projects: []
last_updated: 2026-05-12
---

# ServiceNow

> Enterprise IT service management + incident ticketing platform — integration target for incident workflow and customer ticket sync.

## Owner / vendor

ServiceNow Inc. (NYSE: NOW) — independent SaaS vendor.

## Integration surface

- REST API + Table API — CRUD on incidents, change tickets, CMDB items.
- Webhooks — outbound events on ticket state changes.
- ITSM workflow engine — escalation, routing, SLA tracking.

## Data flow

External — customers may use ServiceNow as their ticketing system of record. Cybereason / Level Blue incident output can sync into ServiceNow via API/webhook bridges.

## Current usage

External reference only — appears in customer integration discussions. No DS-team integration yet.

## Known issues

(none captured)

## Related entities

(none yet)

## Open questions

- Which Level Blue customers consume incident output into ServiceNow today?
- Is there a candidate DS-team project around incident enrichment before push to ServiceNow?
