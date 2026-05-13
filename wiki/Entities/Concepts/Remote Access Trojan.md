---
title: Remote Access Trojan
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[AIDRA]]", "[[NGAV]]", "[[META]]", "[[Hunter]]"]
related_systems: ["[[BitDefender]]"]
last_updated: 2026-05-13
---

# Remote Access Trojan

> Malware family ("RAT") that gives an attacker interactive control over a compromised host — keystroke logging, screen capture, file/registry access, lateral pivot.

## What it is

A persistent backdoor with a [[Command and Control]] channel. Classic families: njRAT, Quasar, AsyncRAT, Remcos, DarkComet. Modern variants ship as .NET or PowerShell loaders and chain into commodity stealers. Distinguishing trait from generic implants: human-in-the-loop tasking via the C2 console.

## Why we care

- [[NGAV]] static + behavioural classifiers must flag RAT installers before execution; [[META]] supplies the VirusTotal consensus signal.
- [[AIDRA]] script analysis routinely surfaces PowerShell RAT droppers — Functional + Behavioral agents look for [[Code Obfuscation]] + persistence handles.
- [[Hunter]] analysts pivot from RAT-IOC alerts to host-process timelines.
- A RAT on a domain controller almost always precedes [[Credential Theft]] and [[Lateral Movement]].

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Do we have a shared RAT-family taxonomy between [[META]], [[AIDRA]], and [[NGAV]]?
