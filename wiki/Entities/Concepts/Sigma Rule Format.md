---
title: Sigma Rule Format
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[Owlint-Sigma]]", "[[Detection Engineering Hub]]"]
related_systems: ["[[MITRE ATT&CK]]"]
last_updated: 2026-05-12
---

# Sigma Rule Format

> Open-source YAML schema for SIEM detection rules — a vendor-neutral
> intermediate representation that translates to many SIEM query
> languages.

## What it is

A YAML rule schema (originated by Florian Roth + Thomas Patzke) with a
fixed structure: `title`, `id`, `status`, `description`, `logsource`,
`detection` (selection blocks + condition expression), `falsepositives`,
`level`. The Sigma toolchain converts rules into Splunk SPL, Elastic
Lucene/EQL, KQL (Sentinel/Defender), Snowflake SQL, etc.

For Level Blue specifically, Sigma is the converging lingua franca across
multiple SIEM/MDR platforms — see [[sigma-as-cross-vendor-detection-lingua-franca]].

## Why we care

- [[Owlint-Sigma]] — DS-team's flagship Sigma-related project: generate Sigma rules from threat-intel + translate to vendor backends.
- [[Detection Engineering Hub]] — Sigma is one of the rule families the hub manages.
- [[2026-05-07 — Sigma as Common Detection Language]] — decision pinning Sigma as Level Blue's cross-SIEM lingua franca.
- [[2026-05-07 — Deterministic Sigma HQ Translation with LLM Fallback]] — translation strategy: deterministic-first, LLM fallback.

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.
- See [[sigma-as-cross-vendor-detection-lingua-franca]] for cross-project pattern.

## Open questions

- Sigma 2.0 (sigmaHQ rewrite) adoption — when does the team migrate from `sigma-cli` v1?
- Coverage gaps: which SIEM backends ship without official Sigma translation modules and need DS-team-authored ones?
