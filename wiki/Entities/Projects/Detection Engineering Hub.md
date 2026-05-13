---
title: Detection Engineering Hub
type: project
tags: [project, wiki]
status: active
lead: [[Itamar Hershko]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
related_projects: ["[[Owlint-Sigma]]"]
raw_path: raw/projects/Itamar Project - Detection Engineering Hub/
last_updated: 2026-05-13
---

# Detection Engineering Hub

> Unified platform for managing the complete lifecycle of detection rule content — upload, validate, test, and publish across multiple engines and formats.

## Goal

Replace scattered scripts, manual workflows, and tribal knowledge with a structured, auditable detection-rule pipeline used by SOC teams, Threat Intel Analysts, and Detection Engineers — supporting BEP, Fileless, VPP, VFP engines and rule formats including YARA, Sigma, JSON, and BOSS.

## Approach

FastAPI backend + Streamlit UI + PostgreSQL + Docker/Helm deployment, with integrations to VirusTotal Retrohunt, Confluence KB, Jira Epics, and Jupyter notebooks. JWT auth with 6 role levels (RBAC), full audit logging, and a release-workflow lifecycle (upload → parse → validate → publish → confirm).

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
