---
title: Command and Control
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[Owlint-Sigma]]", "[[AIDRA]]", "[[Hunter]]"]
related_systems: ["[[Phoenix]]", "[[Tipper]]"]
last_updated: 2026-05-13
---

# Command and Control

> Attacker-controlled communication channel ("C2") that an implanted RAT or beacon uses to receive instructions and exfiltrate data — [[MITRE ATT&CK]] tactic TA0011.

## What it is

The persistent network channel between a compromised endpoint and the adversary's infrastructure. Patterns range from polling HTTP(S) beacons (Cobalt Strike, Sliver) to DNS tunnelling, MQTT (legitimate IoT brokers re-purposed), and domain-fronted CDN abuse. Detection focuses on traffic shape (beacon-interval jitter, JA3/JA4 fingerprints, rare destinations) and on host-side process/network correlation.

## Why we care

C2 traffic shows up across the team's pipelines:
- [[AIDRA]] — script analysis maps C2 callbacks back to threat-intel for IOC enrichment.
- [[Owlint-Sigma]] — Tipper threat reports almost always include C2 indicators that translate to Sigma rules.
- [[Hunter]] — analyst-facing hunting prompts target C2-shaped DNS/HTTP patterns.
- [[Phoenix]] — sensor telemetry feeds the correlation engine where C2 sequences become Malops.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Which detection layer in [[Phoenix]] owns ML-based beacon-interval scoring vs deterministic Sigma rules from [[Owlint-Sigma]]?
- Is there a shared C2-IOC store across [[Tipper]], [[AIDRA]], and the upcoming [[Rebuild UEBA in Phoenix XDR]]?
