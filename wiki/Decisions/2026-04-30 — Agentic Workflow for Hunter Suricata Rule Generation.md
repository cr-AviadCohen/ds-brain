---
title: Agentic Workflow for Hunter Suricata Rule Generation
type: decision
tags: [decision, wiki]
date: 2026-04-30
deciders: ["[[Aviad Cohen]]", "[[Pawel Knapczyk]]"]
status: accepted
related_projects: ["[[Hunter]]"]
last_updated: 2026-05-11
---

# Agentic Workflow for Hunter Suricata Rule Generation — 2026-04-30

## Context

In the 2026-04-30 Aviad/Pawel intro, Pawel described how his team drives [[Hunter]] via API to auto-generate Suricata IDS rules from vulnerability inputs like Nuclei templates. The current design is a single-prompt LLM call, and the main observed pain is the LLM hallucinating IDs or faking VirusTotal calls.

## Decision

Replace the single-prompt design with an agentic, validated workflow for Hunter-driven Suricata IDS rule generation — adding double-checking and validation steps before any candidate signature is surfaced to the analyst or pushed downstream.

## Why

Single-prompt LLM rule generation has no internal validation loop, so hallucinated IDs or fabricated tool calls survive into the output. An agentic workflow with explicit validators (and the option to retry/self-correct) brings the same hallucination-mitigation pattern already used by Owlint-Sigma and AIDRA to Pawel's IDS pipeline.

## Alternatives considered

- Keep single-prompt and rely solely on prompt engineering — rejected as insufficient given the observed hallucination class (fake CVE IDs, faked VT lookups).

## Consequences

- Aviad will share the team's multi-agent assistant architecture with Pawel so Hunter's Suricata flow can plug into it.
- Integration depends on resolving VPN/access so Pawel's tools can connect to Aviad's orchestrator.
- Sets a precedent: any LLM-to-signature generation flow inside Level Blue should default to a validated agentic pipeline, not single-shot prompting.

## Open questions

- How quickly can VPN/access be resolved to enable the orchestrator hookup?
- Which validators are mandatory (syntax, CVE existence, simulated traffic) before a Suricata rule is published?
