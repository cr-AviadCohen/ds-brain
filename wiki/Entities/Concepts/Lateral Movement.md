---
title: Lateral Movement
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[RCE-NG]]", "[[XDR Correlation for Phoenix]]", "[[UEBA (USMA)]]", "[[Hunter]]"]
related_systems: ["[[Active Directory]]"]
last_updated: 2026-05-13
---

# Lateral Movement

> Adversary techniques that pivot between hosts inside a compromised environment — [[MITRE ATT&CK]] tactic TA0008 — the step that distinguishes a single-host incident from a domain-wide compromise.

## What it is

Most common vectors: [[Remote Desktop Protocol]] interactive logon, [[Windows Management Instrumentation]] remote process create over DCOM/WinRM, SMB admin shares (`\\target\C$`) + `PsExec` / `SCM`, pass-the-hash + pass-the-ticket using credentials lifted from [[Local Security Authority]], remote scheduled task creation, and DCOM-object abuse (`MMC20.Application`, `ShellWindows`). The defender signal pattern: short-burst authentication events fanning out from a single source within minutes.

## Why we care

- [[RCE-NG]] is built around correlating per-host detection events into the cross-host attack story — lateral-movement edges are the spine of every Malop graph.
- [[XDR Correlation for Phoenix]] ports the same correlation onto Phoenix's new schema.
- [[UEBA (USMA)]] modelled cross-host login graphs for lateral-movement anomaly detection.
- [[Hunter]] hunting queries seed on lateral-movement signatures across customer telemetry.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Cross-vendor [[Identity Correlation]] is the hardest sub-problem — how does the team plan to share an identity resolver between [[RCE-NG]], [[Rebuild UEBA in Phoenix XDR]], and [[Smart Asset Correlation]]?
