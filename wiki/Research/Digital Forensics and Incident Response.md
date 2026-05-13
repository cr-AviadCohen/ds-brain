---
title: Digital Forensics and Incident Response
type: research
tags: [research, wiki]
domain: security
related_projects: ["[[IRCA]]", "[[AIDRA]]", "[[Hunter]]"]
last_updated: 2026-05-13
---

# Digital Forensics and Incident Response

> Operational discipline ("DFIR") that combines live-host telemetry collection, artefact triage, root-cause analysis, and remediation — the analyst workflow that every DS-team incident product replaces or accelerates.

## What it is

DFIR sits at the intersection of two activities. **Digital forensics** is the disciplined collection and analysis of host + network artefacts (memory dumps, MFT timelines, registry hives, ETW captures, packet captures, image disks). **Incident response** is the operational lifecycle around an active intrusion — scoping, containment, eradication, recovery, lessons-learned (the NIST SP 800-61 / SANS PICERL playbooks). Tooling spans open-source ([[Velociraptor]], KAPE, Volatility) and the EDR-native action set ([[Phoenix]] remediation API, isolate/kill-process/quarantine-file commands).

## Why we care

- [[IRCA]] automates the analyst's narrative-writing + remediation-execution loop end-to-end against the [[Cybereason]] action surface.
- [[AIDRA]] applies the same investigative posture to artefact-level (script) analysis — agent-graph chain that mirrors a manual analyst playbook.
- [[Hunter]] arms analysts with retrieval-grounded hunting before incidents are confirmed.
- [[Incident Investigation (for Fusion 2)]] folds AI pre-analysis into the [[Fusion 2]] analyst workflow upstream of human review.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Tensions

- Speed vs auditability — automating containment risks irreversible actions on false positives; every DS-team incident product enforces analyst-in-the-loop before destructive ops.

## Open questions

- Shared evidence-ground-truth schema across [[IRCA]], [[AIDRA]], and [[Incident Investigation (for Fusion 2)]] — does the team need a single Evidence / Verdict / Reasoning structure to make outputs comparable?
- DFIR-grade reproducibility for LLM-driven narratives: which inputs must be pinned so a re-run reproduces the same report?
