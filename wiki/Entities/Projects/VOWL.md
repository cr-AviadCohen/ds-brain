---
title: VOWL
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Itamar Project - VOWL/
last_updated: 2026-05-11
---

# VOWL

> Production-grade security vulnerability scanner that uses LLM-powered static analysis to detect 130+ vulnerability patterns, generates safe exploit mocks to verify findings in isolated Docker containers, and produces patched code.

## Goal

Eliminate false positives in vulnerability scanning and provide actionable fixes — by combining LLM static analysis with verification in sandboxed containers and an automated patching step.

## Approach

LLM-based static analysis pipeline targeting 130+ vulnerability patterns, paired with an exploit-mock generator that executes safely inside isolated Docker containers to verify each finding before reporting. Outputs both a verified-finding report and patched code suggestions. Codebase under `cybereason-labs/itamar-h` (Vuln branch).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
