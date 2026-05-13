---
title: Persistence
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[NGAV]]", "[[Owlint-Sigma]]", "[[Hunter]]", "[[AIDRA]]"]
related_systems: ["[[Phoenix]]"]
last_updated: 2026-05-13
---

# Persistence

> Attacker techniques to maintain foothold across reboots, re-logons, and remediation attempts — [[MITRE ATT&CK]] tactic TA0003.

## What it is

Mechanisms that re-launch attacker code after the obvious entry point closes: Run/RunOnce keys, scheduled tasks, services, WMI event subscriptions, COM-hijack, [[Master Boot Record]] tampering, browser-extension installs, BITS jobs. Detection straddles file-system, registry, and [[Event Tracing for Windows]] telemetry.

## Why we care

- [[NGAV]] behavioural rules score persistence indicators alongside execution + defence-evasion signals to escalate a Malop.
- [[Owlint-Sigma]] translates Sigma rules whose `logsource` targets Windows-registry / scheduled-task events.
- [[Hunter]] hunting queries look for persistence-establishment events in the [[Phoenix]] event stream.
- [[AIDRA]] script analysis flags persistence-establishment calls inside PowerShell scripts.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Coverage gap analysis: which TA0003 sub-techniques does the current [[NGAV]] rule pack miss?
