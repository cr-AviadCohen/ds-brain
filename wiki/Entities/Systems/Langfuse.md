---
title: Langfuse
type: system
tags: [system, wiki]
owner: open-source
vendor: Langfuse GmbH
integration_surface: [python-sdk, js-sdk, http-api]
related_projects: ["[[Owlint-Sigma]]", "[[AI Assistant]]", "[[AIDRA]]", "[[OWLINT]]"]
last_updated: 2026-05-12
---

# Langfuse

> Open-source LLM observability and tracing platform — DS team uses it to capture prompt/completion traces, token + cost accounting, and prompt-versioning across agent projects.

## Owner / vendor

Langfuse GmbH. Available as open-source self-host or hosted SaaS. License permits self-hosted deployment inside Cybereason / Level Blue infra.

## Integration surface

- Python SDK (primary — wrapped via project-local `observability.py` helpers)
- JS SDK
- HTTP REST API for trace ingestion and dashboard queries

## Data flow

LLM call traces (prompt, completion, token counts, latency, embedding ops) → Langfuse backend → dashboard for cost tracking, prompt evaluation (LLM-as-a-judge), and debugging multi-step agent runs.

In [[Owlint-Sigma]] the integration is gated on env vars: when Langfuse keys are configured, `_init_langfuse()` lazy-loads the client and the pipeline emits traces for every LLM + embedding call; otherwise it's a no-op.

## Current usage

- [[Owlint-Sigma]] — production tracing path via `observability.py` (`_init_langfuse`, `flush`).
- [[AI Assistant]] — recommended observability platform in Guardrails Deep Research; planned for token accounting and continuous prompt evaluation alongside DeepEval.
- [[AIDRA]] — referenced as part of the multi-agent observability stack.
- [[OWLINT]] — Project Proposal calls out Langfuse as the per-tenant cost-tracking layer paired with LangGraph orchestration.

## Known issues

(none documented yet)

## Related entities

- Projects: [[Owlint-Sigma]], [[AI Assistant]], [[AIDRA]], [[OWLINT]]
- Systems: [[LangGraph]] (frequently paired — orchestration + observability)

## Open questions

- Self-host vs SaaS for production — has a deployment target been chosen?
- Where do Langfuse traces live for the Owlint-Sigma pipeline today (project-local instance, shared org instance)?
- Retention policy + PII review for prompts containing customer log data.
