---
title: Multi-Agent Orchestration
type: concept
tags: [concept, wiki]
domain: ai-infra
related_projects: ["[[AI Assistant]]", "[[AIDRA]]", "[[Pixel Agents]]", "[[OwlHub]]"]
related_systems: ["[[LangGraph]]", "[[Langfuse]]"]
last_updated: 2026-05-12
---

# Multi-Agent Orchestration

> Workflow patterns for coordinating multiple LLM agents to solve a
> task — router, supervisor / hierarchical, consensus / debate, and
> pipeline / DAG patterns.

## What it is

When a single LLM call is insufficient (long-horizon task, multiple
tool surfaces, need for specialization), multiple agents are
coordinated via an orchestration layer. Common patterns:

- **Router** — top-level agent dispatches to a specialist agent based on intent.
- **Supervisor / hierarchical** — coordinator decomposes tasks and delegates to worker agents.
- **Consensus / debate** — multiple agents vote or critique each other; final answer aggregated.
- **Pipeline / DAG** — fixed graph of stages, each implemented as an agent or tool call (this is the [[LangGraph]] default).

## Why we care

- [[LangGraph]] is the team's de-facto orchestration runtime.
- [[AI Assistant]] uses orchestration to route between platform query, hunt, and explain workflows.
- [[AIDRA]] is multi-agent by design — risk assessment decomposed across specialist agents.
- [[Pixel Agents]] is the team's autonomous multi-agent framework — replaces single-agent Claude Code with coordinated agents.
- [[OwlHub]] is the orchestration platform layer for autonomous agents.
- Observability via [[Langfuse]].

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.

## Open questions

- Shared agent-protocol contract across DS-team projects (or each project bespoke)?
- When is multi-agent worth the latency + cost vs. a single more capable model?
