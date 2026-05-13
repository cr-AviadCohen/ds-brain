---
title: LangGraph
type: system
tags: [system, wiki]
owner: LangChain Inc.
vendor: LangChain Inc.
integration_surface: [python-sdk]
related_projects: ["[[AI Assistant]]", "[[AIDRA]]", "[[IRCA]]", "[[OWLINT]]", "[[VOWL]]"]
last_updated: 2026-05-12
---

# LangGraph

> LangChain Inc.'s state-machine / DAG framework for orchestrating multi-step LLM agents — the de-facto orchestration runtime for DS team agent projects.

## Owner / vendor

LangChain Inc. Open-source Python library on top of LangChain primitives. Permissive license; usable inside Cybereason / Level Blue stack.

## Integration surface

- Python SDK — declarative graph builder (nodes = LLM calls / tools / Python fns, edges = conditional or sequential transitions, state = typed dict).
- Integrates with LangChain tools, retrievers, and model wrappers.

## Data flow

Workflow author defines a typed graph (nodes + edges); at runtime the LangGraph executor walks the graph, persists state between nodes, handles conditional branching, and exposes hooks for tracing (commonly paired with [[Langfuse]]).

In [[AI Assistant]] the orchestrator layer is built on LangGraph (per the architecture drawio). In [[OWLINT]] LangGraph powers the per-tenant pipeline graph (`graph.py`).

## Current usage

- [[AI Assistant]] — orchestrator layer.
- [[AIDRA]] — multi-agent consensus / arbitration flow.
- [[IRCA]] — incident-response copilot agent graph.
- [[OWLINT]] — pipeline orchestration (`graph.py`).
- [[VOWL]] — agent workflow runtime.

## Known issues

(none documented yet — state management at scale + cost-per-tenant attribution are open concerns flagged in OWLINT proposal)

## Related entities

- Systems: [[Langfuse]] (paired for tracing / cost), [[MCP]] is consumed alongside in agent tool layers.
- Projects: [[AI Assistant]], [[AIDRA]], [[IRCA]], [[OWLINT]], [[VOWL]].

## Open questions

- Versioning + upgrade strategy across projects (each project pins its own LangGraph version today).
- Standard state-schema patterns for the team — should a shared library emerge?
- Checkpointing / resumability story for long-running agent runs.
