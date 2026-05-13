---
title: NGAV
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - NGAV/
last_updated: 2026-05-11
---

# NGAV

> `ngav/pet_ops/pipeline` — the MLOps pipeline that produces the NGAV (Next-Gen Antivirus) static-analysis classifier, a LightGBM model that decides "malicious vs benign" for Windows PE files.

## Goal

Retrain the NGAV malware classifier as the threat landscape changes, keep every shipped model honest (only ship if test-AUC ≥ the previously shipped model's AUC), maintain a separate allowlist of high-confidence benigns for production, and produce reproducible, versioned artefacts (model + thresholds + allowlist) consumable by the production C++ NGAV components.

## Approach

Jenkins-driven pipeline that: (1) pulls labelled PE samples from the VirusTotal BigQuery feed (separately for EXE and DLL, managed and unmanaged); (2) generates static-analysis features on a Windows worker via the internal `ngav-stool-featuregen` tool; (3) cleans, deduplicates, and balances the dataset (50/50); (4) trains a LightGBM binary classifier with optional time-decay sample weighting; (5) optimises three thresholds (cautious/moderate/aggressive) on validation set; (6) generates a low-FPR allowlist over a pool of likely-benign samples; (7) gates the model on test-AUC; (8) exports `.features.conf` and `.model.conf` to JFrog Artifactory with versioned paths (`{files_type}_{major}.{minor}_{dd-mm-yyyy}`). Linux/Docker side orchestrated by `utils/Jenkinsfile`; Windows-only feature-gen via a separate Jenkins job; inter-stage data plane is the GCS bucket `lin-win-ngav`.

## Status

active — seeded from raw 2026-05-11.

**Core variant** (a.k.a. "NGAV Core") — in production per the DS Team project tracker.

**Phoenix variant** (a.k.a. "NGAV Phoenix") — Q2 High-priority team-effort port to [[Phoenix]]; status "waiting for devops to reutilies the model training pipeline" per the DS Team project tracker. Engineering contact: [[Ortal Keizman]]. Jira ENG-9969.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — Core variant in production; Phoenix variant Q2 High-priority team-effort blocked on devops reusing the model-training pipeline; engineering contact [[Ortal Keizman]]; Jira ENG-9969.

## Open questions
