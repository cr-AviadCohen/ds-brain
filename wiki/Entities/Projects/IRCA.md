---
title: IRCA
type: project
tags: [project, wiki]
status: active
lead: [[Guy Kassorla]]
team: ["[[Aviad Cohen]]", "[[Guy Kassorla]]"]
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - IRCA/
last_updated: 2026-05-12
---

# IRCA

> Incident Response & Compromise Assessment — automated end-to-end IR flow that pulls data from Cybereason, runs AI-driven threat analysis, generates a customer-ready PDF report, and executes whitelisted remediation actions after analyst approval.

## Goal

Replace manual, slow, inconsistent EDR incident response (pivoting between tools, writing narratives, mapping to MITRE ATT&CK, generating reports, executing remediations one-by-one) with an automated flow so analysts respond to incidents in minutes rather than hours/days — keeping MTTR low and report quality consistent.

## Approach

Four-stage pipeline (Python 3.11, Streamlit UI, LangGraph agent): (1) `data_collector.py` pulls malops/detection events/process details from Cybereason REST APIs (`/rest/detection/inbox`, `/detection/details`, `/crimes/unified`, `/visualsearch/query/simple`) and `json_arranger.py` normalises them; (2) `prompt_builder.py` + Azure OpenAI (GPT-5) produces threat assessment, chronological narrative, and MITRE ATT&CK mapping grounded in the JSON; (3) `report_generator_figma.py` renders a branded PDF (ReportLab); (4) a LangGraph agent (`agent.py`) parses recommended remediations into a whitelisted action set (KILL_PROCESS, QUARANTINE_FILE, DELETE_REGISTRY_KEY, ISOLATE_MACHINE, UNQUARANTINE_FILE) and executes via the Cybereason API after analyst approval. Two UIs: PoC and live ops.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- LLM determinism — results may vary across runs (mitigated by observation but not eliminated).

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — POC completed; Q2 Low priority (may change after presentation); Jira ENG-9972; owner [[Guy Kassorla]].
- 2026-05-12 — [[2026-05-12 — Aviad and Jose intro]] — explicitly blocked: [[Phoenix]] engineering is at full capacity and cannot integrate IRCA; integration deferred.

## Open questions
