---
title: Privilege Escalation
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[AI Assistant]]", "[[IRCA]]", "[[AIDRA]]", "[[NGAV]]"]
related_systems: []
last_updated: 2026-05-13
---

# Privilege Escalation

> Attacker techniques to gain higher permissions than the initial foothold provided — [[MITRE ATT&CK]] tactic TA0004 — the step between landing on a host and owning it.

## What it is

Two flavours. **Local** — user → SYSTEM / root via kernel CVE, unquoted-service-path abuse, DLL search-order hijack, named-pipe impersonation, token theft from a privileged process. **Domain** — standard user → Domain Admin via [[Active Directory]] misconfig (DCSync rights, AdminSDHolder, AS-REP-roastable accounts) or vulnerability (Zerologon, PetitPotam, ESC1–ESC8 in AD CS).

## Why we care

- [[IRCA]] severity scoring jumps when EoP evidence appears alongside [[Credential Theft]] in the same Malop.
- [[AI Assistant]] analyst flows need to surface the *escalation chain* — not just the final SYSTEM event — to be useful.
- [[AIDRA]] script analysis flags EoP-helper invocations (PrintNightmare exploitation snippets, `RoguePotato` chains).
- [[NGAV]] behavioural rules combine EoP signals with [[Persistence]] establishment as a high-confidence Malop trigger.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Coverage on AD CS (ESC1–ESC8) certificate-template-abuse detection — currently weak signal end-to-end.
