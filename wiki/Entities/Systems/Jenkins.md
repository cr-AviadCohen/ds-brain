---
title: Jenkins
type: system
tags: [system, wiki]
owner: Cybereason internal (CI/CD)
related_projects: ["[[MLAV]]", "[[NGAV]]"]
seeds:
  - raw/projects/Project - MLAV/Project MLAV.docx.md
  - raw/projects/Project - NGAV/01 - Project Overview.md
last_updated: 2026-05-11
---

# Jenkins

> Cybereason's internal CI/CD orchestrator (`jenkins-irelease.eng.cybereason.net`) — runs the long-running MLOps pipelines for MLAV and NGAV.

## Owner / vendor

Cybereason internal — Data Science view of the cluster lives at `jenkins-irelease.eng.cybereason.net/view/Data Science/`.

## Integration surface

- Jenkinsfile-driven jobs.
- Linux side (Docker-isolated) + Windows-only workers for PE feature extraction.
- GCS bucket `lin-win-ngav` as the inter-stage data plane.
- JFrog Artifactory as the artifact destination.

## Data flow

For NGAV: Linux Jenkins job (controlled by `utils/Jenkinsfile`) coordinates dataset pulls, dataset cleaning, training, threshold optimisation, allowlist generation, the decision gate, and artifact upload. Windows-only feature-gen runs as a separate job and shuttles features back through the GCS bucket.

## Current usage

- [[MLAV]]: `mlav-model-generator` job — full pipeline takes ~20 hours.
- [[NGAV]]: dual-OS pipeline (Linux + Windows) producing versioned `.features.conf` / `.model.conf` artefacts.

## Known issues

- Long pipeline durations (NGAV multi-hour, MLAV ~20h).
- Windows worker (`windows-jenkins-ngav-slave-2`) replaced from c2-standard-60 to N2D-standard-64.

## Related entities

[[MLAV]], [[NGAV]], [[BigQuery]] (source), [[VirusTotal]] (label source)

## Open questions
