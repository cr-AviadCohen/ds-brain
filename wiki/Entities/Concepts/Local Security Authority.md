---
title: Local Security Authority
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[IRCA]]", "[[AIDRA]]", "[[NGAV]]"]
related_systems: ["[[Active Directory]]"]
last_updated: 2026-05-13
---

# Local Security Authority

> Windows subsystem ("LSA"; user-mode component is `lsass.exe`) that authenticates users, enforces local security policy, and caches credential material in memory — the prime target for [[Credential Theft]].

## What it is

LSA brokers all Windows logon flows: it validates passwords / Kerberos tickets / NTLM responses, issues access tokens, and caches recent credentials (plaintext via WDigest in legacy configs, NTLM hashes, Kerberos TGTs). Attackers use Mimikatz, comsvcs.dll `MiniDump`, or direct `MiniDumpWriteDump` on the `lsass.exe` process to pull this cache. [[Event Tracing for Windows]] + EDR sensor hooks watch handle-open + memory-read patterns on `lsass.exe`.

## Why we care

- [[IRCA]] incident-narrative generation flags LSASS access as a high-severity credential-theft step.
- [[NGAV]] behavioural rules treat unauthorised `lsass.exe` handle-opens as one of the strongest endpoint signals.
- [[AIDRA]] PowerShell analysis spots LSASS-dump calls including obfuscated Win32 API wrappers.
- LSA compromise is the bridge from initial access to [[Lateral Movement]] across [[Active Directory]].

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Does [[Phoenix]] surface LSA Protection (RunAsPPL) configuration state as a tenant-level posture signal?
