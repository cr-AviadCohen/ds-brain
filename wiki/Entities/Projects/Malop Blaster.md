---
title: Malop Blaster
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Itamar Project - Malop Blaster/
last_updated: 2026-05-11
---

# Malop Blaster

> PowerShell-based proof-of-concept tool for cybersecurity professionals to test and validate security posture on Windows endpoints by simulating malicious operations.

## Goal

Provide an interactive, menu-driven PowerShell tool that runs 11 simulated MalOps with unified logging on Windows 10+ (PowerShell 5.1+, Administrator privileges) — used for PoC validation of detection coverage.

## Approach

Single-file PowerShell script (~602 lines) with modular, array-driven architecture. V3 introduces unified logging, verbose/minimal output modes, session-aware query, animated UI, and silent execution (MalOps always log as executed for PoC accuracy).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
