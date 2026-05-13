---
title: USMA
type: system
tags: [system, wiki]
owner: "[[LevelBlue]]"
vendor: "[[LevelBlue]]"
integration_surface: [correlation-rules, suricata-signatures]
related_projects: ["[[UEBA (USMA)]]"]
last_updated: 2026-05-12
---

# USMA

> Unified Security Management (Anywhere) — the legacy MSSP platform inherited from [[AlienVault]] → [[AT&T]] → [[LevelBlue]]; primary detection engine for Level Blue managed-security customers, driven by hand-authored correlation rules and [[Suricata Signatures]].

## Owner / vendor

[[LevelBlue]] — inherited from [[AT&T]] (via the May 2024 cybersecurity-arm spinout) and originally built at [[AlienVault]] before the AT&T acquisition. "USMA" = "USM Anywhere", the cloud-hosted variant of the older USM (Unified Security Management) appliance.

## Integration surface

- Hand-authored correlation rules (Jose's team) — pattern-match across normalised customer telemetry.
- [[Suricata Signatures]] — IDS rule format authored by Jose and shipped into the USMA detection stack.
- Managed-customer telemetry ingest from across Level Blue's MSSP footprint.

## Data flow

Customer telemetry → normalisation → correlation-rule engine + Suricata IDS → alarms surfaced to Level Blue SOC analysts for managed-security customers. Historically also fed an unsupervised-ML UBA component for anomalous-login / exfiltration / lateral-movement detection — see [[UEBA (USMA)]] history below.

## Current usage

Active production platform for Level Blue's managed-security customer base. Level Blue engineering is strictly focused on maintaining USMA until the migration to [[Phoenix]] completes — they cannot take on new AI deployments in the meantime ([[2026-05-12 — Aviad and Jose intro]]). [[Jose Manuel Martin Rodriguez]] has spent ~10 years writing the correlation rules and Suricata signatures that drive USMA detections.

## Known issues

- Original [[UEBA (USMA)]] / UBA capability on USMA was abandoned ~2 years ago after the AT&T data-science team turnover; the abandoned model still emits noisy alarms and generates customer complaints.
- Engineering bandwidth is strictly maintenance-mode pending the Phoenix migration — no headroom for new AI features inside USMA.

## Related entities

- [[LevelBlue]] — current operator
- [[AT&T]] — historical parent
- [[AlienVault]] — original vendor
- [[Suricata Signatures]] — primary rule format
- [[UEBA (USMA)]] — abandoned UBA capability that was built on top of USMA
- [[Phoenix]] — migration target

## Open questions

- What is the Phoenix-migration target date for USMA customers, and how does it gate any [[UEBA (USMA)]] rebuild?
- Can a UEBA capability be rebuilt inside Phoenix without re-creating it on USMA in the meantime — see [[Rebuild UEBA in Phoenix XDR]]?
- Are any USMA Suricata signatures candidate inputs to DS-team Sigma / [[Owlint-Sigma]] work?
