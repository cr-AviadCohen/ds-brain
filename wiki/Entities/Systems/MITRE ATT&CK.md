---
title: MITRE ATT&CK
type: system
tags: [system, wiki]
owner: MITRE Corporation (vendor)
vendor: MITRE Corporation
related_projects: ["[[AIDRA]]", "[[IRCA]]", "[[OWLINT]]", "[[AI Assistant]]"]
seeds:
  - raw/projects/Project - AIDRA/AIDRA.md
  - raw/projects/Project - IRCA/IRCA - Gate 1 - Research Impact & Feasibility.docx.md
  - raw/projects/Project - OWLINT/
last_updated: 2026-05-11
---

# MITRE ATT&CK

> Publicly maintained knowledge base of adversary tactics and techniques (plus D3FEND for defences, CAPEC for attack patterns, CWE for weaknesses) — the team's canonical mapping target for threat narratives and analyst-facing reports.

## Owner / vendor

MITRE Corporation (public framework).

## Integration surface

- Technique IDs used as tags throughout DS-generated reports.
- Deterministic pattern-matching mappers (AIDRA) and LLM-driven mappers (IRCA).
- MITRE ATT&CK / D3FEND / CAPEC / CWE agents (AI Assistant has dedicated per-framework agents).

## Data flow

Findings from agents (AIDRA, IRCA) → mapping step → ATT&CK technique IDs attached to evidence (line numbers, code snippets, log records) → rendered into the PDF / portal report.

## Current usage

- [[AIDRA]]: deterministic ATT&CK mapper with evidence provenance per finding.
- [[IRCA]]: LLM-driven ATT&CK mapping in narrative reports.
- [[OWLINT]]: tagging generated YARA rules.
- [[AI Assistant]]: dedicated MITRE ATT&CK, D3FEND, CAPEC, CWE agents.
- MITRE dry-runs used as the IRCA evaluation harness on a dedicated sensor environment.

## Known issues

- LLM-driven mapping is non-deterministic; deterministic pattern mappers preferred where coverage allows.

## Related entities

[[AIDRA]], [[IRCA]], [[OWLINT]], [[AI Assistant]]

## Open questions
