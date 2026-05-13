---
title: Remote Desktop Protocol
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[UEBA (USMA)]]", "[[Rebuild UEBA in Phoenix XDR]]", "[[Hunter]]"]
related_systems: ["[[Active Directory]]"]
last_updated: 2026-05-13
---

# Remote Desktop Protocol

> Microsoft's interactive remote-session protocol ("RDP", TCP 3389) — the most common interactive [[Lateral Movement]] vector and a high-signal anomaly source for UEBA.

## What it is

Encrypted screen + input streaming session between an RDP client (`mstsc`) and a Windows host's `TermService`. Attackers prefer RDP for interactive lateral movement because it leaves an authenticated session, looks like normal admin behaviour, and bypasses many script-based detections. Defender signals: Windows Security event IDs 4624 (logon type 10), 4778/4779 (session reconnect), `Microsoft-Windows-TerminalServices-LocalSessionManager` operational log, and net-flow connection-to-3389 patterns.

## Why we care

- [[UEBA (USMA)]] flagged anomalous-login patterns over RDP as a core detection use case — same pattern surfaces in [[Rebuild UEBA in Phoenix XDR]].
- [[Hunter]] analyst playbooks pivot on cross-host RDP graph patterns (one source → many destinations within minutes).
- RDP brute-force + credential reuse from [[Credential Theft]] is the canonical attack chain in customer incidents.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Cross-tenant RDP-anomaly baselining inside [[Phoenix]] — is per-tenant per-user enough, or do we need an industry-vertical prior?
