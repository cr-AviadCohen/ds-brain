---
title: AIDRA
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: [[Aviad Cohen]]
started: 2026-05-11
systems: ["[[LangGraph]]", "[[VirusTotal]]"]
related_decisions: []
raw_path: raw/projects/Project - AIDRA/
last_updated: 2026-05-12
---

# AIDRA

> Advanced Intelligence-Driven Risk Assessment — a multi-agent AI system that analyses potentially malicious scripts (primarily PowerShell) and produces structured threat reports with MITRE ATT&CK mapping and PDF output.

## Goal

Accept a script (PowerShell, batch, other) and run it through an orchestrated pipeline of specialised LLM agents whose findings are merged via a weighted consensus engine. Produce evidence-grounded findings with deobfuscation, IOC extraction, threat-intel lookups, and false-positive mitigation — rendered as both a rich terminal report and a professional PDF.

## Approach

Custom fine-tuned CodeLlama-7B (LoRA) orchestrator coordinates seven specialised agents (Functional, Deobfuscation, Network, Behavioral, Malware, Threat Intelligence, Risk Assessment) implemented on LangGraph `StateGraph` with `MemorySaver` and an internal AgentBus. All models run locally with 4-bit quantisation (`bitsandbytes`, 8192-token context). HallucinationGuard + ScriptGroundingSystem enforce every claim is grounded in actual input lines. Deterministic MITRE mapper, live IOC lookups against VirusTotal / AlienVault OTX / MalwareBazaar, ReportLab PDF output.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — POC completed; Q2 Low priority (may change after presentation); Jira ENG-9972; owner [[Itamar Hershko]].

## Open questions
