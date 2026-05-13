---
title: Palo Alto
type: system
tags: [system, wiki]
owner: Palo Alto Networks
vendor: Palo Alto Networks
integration_surface: [next-gen firewall, prisma cloud, cortex xdr]
related_projects: []
last_updated: 2026-05-12
---

# Palo Alto

> Palo Alto Networks suite — firewall + cloud security + Cortex XDR competitor referenced across Cybereason integration / interop docs.

## Owner / vendor

Palo Alto Networks (NASDAQ: PANW) — independent vendor.

## Integration surface

- Next-Generation Firewall (NGFW) — perimeter / segmentation appliance and VM-Series.
- Prisma Cloud — cloud-workload + posture security.
- Cortex XDR — endpoint + XDR platform; competitor and occasional interop partner for Cybereason.

## Data flow

External — Cybereason and Level Blue customers may run Palo Alto products in parallel. Telemetry surfaces are mostly outbound to PA platforms; potential ingest into Cybereason / Level Blue stacks via log forwarders.

## Current usage

External reference only — appears in Cybereason interop and competitive-analysis docs. No DS-team integration yet.

## Known issues

(none captured)

## Related entities

(none yet)

## Open questions

- Which Palo Alto product is the actual competitor / integration target for [[Phoenix]]?
- Are any Level Blue customers consuming both stacks (interop opportunity)?
