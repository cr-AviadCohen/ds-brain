---
title: Credential Theft
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[IRCA]]", "[[Hunter]]", "[[AIDRA]]"]
related_systems: ["[[Active Directory]]"]
last_updated: 2026-05-13
---

# Credential Theft

> Adversary techniques to steal credential material — plaintext passwords, NTLM hashes, Kerberos tickets, OAuth tokens, browser-stored secrets — covering [[MITRE ATT&CK]] tactic TA0006.

## What it is

The on-host bridge from initial access to enterprise-wide impact. Major sub-techniques: LSASS memory dump (Mimikatz / comsvcs), DCSync against a domain controller, Kerberoasting service tickets, browser-credential / cookie steal, token impersonation via SeImpersonatePrivilege, and post-2024 OS-Credential-Manager / Workplace-Join attacks. Detection blends sensor signals on the [[Local Security Authority]] process, [[Active Directory]] replication anomalies, and ticket-format heuristics.

## Why we care

- [[IRCA]] elevates incident severity sharply when LSASS-handle or DCSync evidence is in the timeline.
- [[Hunter]] hunting prompts include canonical credential-access TTPs.
- [[AIDRA]] PowerShell analysis flags `Invoke-Mimikatz`, `Get-WindowsCredentials`, and DPAPI-key-extraction calls.
- Credential theft directly enables [[Lateral Movement]] (via [[Remote Desktop Protocol]], pass-the-hash, WinRM).

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Cross-product shared "credential-theft severity" model — does [[Phoenix]] correlation already weight these signals consistently with [[IRCA]]'s LLM scoring?
