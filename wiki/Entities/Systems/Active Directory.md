---
title: Active Directory
type: system
tags: [system, wiki]
owner: Microsoft
vendor: Microsoft
integration_surface: [LDAP, Kerberos, replication, event-logs]
related_projects: ["[[IRCA]]", "[[UEBA (USMA)]]", "[[Rebuild UEBA in Phoenix XDR]]"]
last_updated: 2026-05-13
---

# Active Directory

> Microsoft's enterprise identity + access directory service ("AD") — LDAP store + Kerberos KDC + group-policy distribution — the single biggest target surface in every Windows-shop incident.

## Owner / vendor

Microsoft (introduced Windows 2000; Azure AD / Entra ID is the cloud counterpart, distinct product).

## Integration surface

- **LDAP/LDAPS** — query users, groups, computers, OUs.
- **Kerberos KDC** — TGT issuance + service-ticket exchange (port 88).
- **Replication / DCSync** — DCs replicate the directory using the Drsuapi protocol — abused for credential theft.
- **Event channels** — Security log + `Directory Service` channel + Sysmon for change tracking.

## Data flow

Domain-joined hosts → DC over Kerberos + LDAP → group-policy pull (SYSVOL) → audit events into the local Security log → Cybereason sensor ETW pickup → [[Phoenix]] / [[Core]] backend. On the LevelBlue side, [[USMA]] correlation rules ingest DC event streams directly.

## Current usage

- [[IRCA]] incident narratives almost always cite an AD account / group / OU pivot as the central enterprise context.
- [[UEBA (USMA)]] modelled per-user behavioural baselines over AD logon + access-pattern events.
- [[Rebuild UEBA in Phoenix XDR]] inherits AD-driven identity-correlation as a core input.

## Known issues

- DCSync, Golden-Ticket, and Kerberoasting attacks are not directly visible from standard endpoint telemetry — require DC-side log collection or replication-traffic inspection.
- Stale group memberships and orphaned service accounts inflate UEBA false-positive rates.

## Related entities

[[IRCA]], [[UEBA (USMA)]], [[Rebuild UEBA in Phoenix XDR]], [[Local Security Authority]], [[Credential Theft]], [[Lateral Movement]]

## Open questions

- DC-side event collection coverage across Cybereason customers — what fraction ship `4662` (object access) + `4769` (Kerberos service ticket) at scale?
