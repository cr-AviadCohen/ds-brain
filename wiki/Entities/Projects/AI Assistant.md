---
title: AI Assistant
type: project
tags: [project, wiki]
status: active
lead: [[Guy Kassorla]]
team: ["[[Aviad Cohen]]", "[[Guy Kassorla]]"]
started: 2026-05-11
systems: ["[[LangGraph]]", "[[Azure AI Foundry]]", "[[Langfuse]]", "[[Phoenix]]"]
related_decisions: []
raw_path: raw/projects/Project - AI Assistant/
last_updated: 2026-05-13
---

# AI Assistant

> Natural-language interface that sits on top of the Cybereason platform, letting analysts retrieve information and execute investigation actions from a single conversational flow.

## Goal

Reduce the friction of analysts switching between multiple tools and manually orchestrating investigation steps. Deeply integrate with internal platform APIs and external threat-intelligence sources so the assistant goes beyond Q&A and performs real, end-to-end investigation actions. Success measured by orchestrator agent-selection accuracy >80%, tool-selection accuracy >80%, guardrails passing on benchmark, and real analyst adoption.

## Approach

Centralised hierarchical multi-agent system: an Orchestrator agent manages specialised, independent agents (each with its own system prompt, tools, and LLM choice). Every query goes through Guardrails → Orchestration & Routing → Execution → Response composition → Tracing & observability. Built in Python with LangChain and LangGraph, integrated with Azure AI Foundry (GPT-5.2 / GPT-5.4 with lighter alternatives). Configurable via a central config layer covering guardrails, tracing, agent composition, and per-agent model selection.

## Status

active — seeded from raw 2026-05-11.

**Core variant** (a.k.a. "AI-Assistant") — POC completed; Q2 Low priority (may change after presentation); Jira ENG-7774. Owner: [[Guy Kassorla]]. POC presentations to SLR / Spider Labs and Phoenix product pending.

**Phoenix variant** (a.k.a. "AI-Assistant for Phoenix") — Q2 Medium priority; status TBD. Blocker: Phoenix lacks an API gateway and uses gRPC; DB access has been offered as a temporary workaround. Jira ENG-9972. Owner: [[Guy Kassorla]].

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — Core variant POC completed (Q2 Low, ENG-7774), pending presentations to SLR + Phoenix product; Phoenix variant Q2 Medium TBD, blocked on Phoenix gRPC / API-gateway gap (ENG-9972). Owner [[Guy Kassorla]].
- 2026-05-12 — [[2026-05-12 — Aviad and Jose intro]] — explicitly blocked: [[Phoenix]] engineering is at full capacity and cannot integrate AI Assistant; integration deferred.

## Open questions
