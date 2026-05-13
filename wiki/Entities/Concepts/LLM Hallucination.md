---
title: LLM Hallucination
type: concept
tags: [concept, wiki]
domain: eval
related_projects: ["[[AIDRA]]", "[[Hunter]]", "[[AI Assistant]]", "[[Owlint-Sigma]]", "[[OWLINT]]"]
related_systems: ["[[Azure AI Foundry]]"]
last_updated: 2026-05-12
---

# LLM Hallucination

> An LLM generating plausible-sounding but unsupported or false claims —
> i.e., output not grounded in input context, retrieved evidence, or
> reality.

## What it is

Hallucination = output that fails grounding. Two practical buckets:
- **Intrinsic** — the output contradicts the provided context.
- **Extrinsic** — the output makes claims about the world that are false / unverifiable.

Mitigations: [[RAG]] (ground in retrieved evidence), tool calls
(replace generated facts with tool-fetched ones), structured output +
validation, eval harnesses that flag ungrounded claims.

## Why we care

Hallucination is the shared risk across every DS-team LLM-driven
workflow — see [[llm-hallucination-as-shared-risk]] for the
cross-project pattern.

- [[AIDRA]] — risk-assessment claims must be defensible.
- [[Hunter]] — fabricated detection logic is a security-correctness bug.
- [[AI Assistant]] — analysts trust output; fabricated indicators are dangerous.
- [[Owlint-Sigma]] — generated Sigma rules must reference real fields + real ATT&CK IDs.
- [[OWLINT]] — generated CTI summaries must not invent IOCs.

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.
- See [[llm-hallucination-as-shared-risk]] for cross-project pattern.

## Open questions

- Shared hallucination eval harness across DS-team projects?
- Per-project tolerance budget — what hallucination rate is acceptable for analyst-facing vs. autonomous workflows?
