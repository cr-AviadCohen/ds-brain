---
title: LLM hallucination as a shared risk across agent projects
type: connection
tags: [connection, wiki]
instances: ["[[AIDRA]]", "[[Hunter]]", "[[AI Assistant]]", "[[Owlint-Sigma]]", "[[2026-04-30 — Aviad and Pawel intro]]", "[[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]]", "[[2026-05-07 — Deterministic Sigma HQ Translation with LLM Fallback]]"]
last_updated: 2026-05-11
---

# LLM hallucination as a shared risk across agent projects

> Every team building an LLM-driven security workflow eventually hits hallucinated outputs (fake IDs, fabricated tool calls, ungrounded claims) and converges on the same mitigation shape: grounding constraints, multi-step validators, agentic retry loops, and deterministic engines as the primary path.

## Instances

- [[AIDRA]] — ships an explicit `HallucinationGuard` plus `ScriptGroundingSystem` that enforces every claim be grounded in actual input lines.
- [[Hunter]] — "main pain is prompt optimisation to keep the model from hallucinating IDs or faking VirusTotal calls" (per the 2026-04-30 Aviad/Pawel intro).
- [[AI Assistant]] — every query passes through a Guardrails layer before orchestration; success metric includes "guardrails passing on benchmark".
- [[Owlint-Sigma]] — uses red-team review, repair loops, and self-healing validation as built-in steps in rule generation.
- [[2026-04-30 — Aviad and Pawel intro]] — meeting where the hallucination concern in Hunter was raised concretely.
- [[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]] — decided to replace single-prompt with an agentic, validated workflow precisely because of the hallucination class.
- [[2026-05-07 — Deterministic Sigma HQ Translation with LLM Fallback]] — multi-layer LLM validation pass with up to three retries before finalising; LLM is fallback, not primary.

## What we infer

Single-prompt LLM calls are not a viable production architecture for security-sensitive output. The team should treat agentic validation loops, deterministic engines as the primary path, and explicit grounding/guardrail layers as the default starting design — not optional enhancements. Any new LLM project that lacks an explicit hallucination-mitigation story should be treated as incomplete in design review.

## Open questions

- Is there a shared validators/guardrails library we should extract once the patterns stabilise across AIDRA, AI Assistant, Owlint-Sigma, and a future Hunter rewrite?
- What's the right benchmark suite for "guardrails passing" that generalises across these projects?
