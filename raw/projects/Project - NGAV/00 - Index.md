---
tags: [ngav, pipeline, MOC, ml-ops, malware-classification]
type: MOC
created: 2026-05-05
---

# NGAV Pipeline — Map of Content

> Source: `ngav/pet_ops/pipeline` on `cybereason-labs/research` (branch `python3`).
> What it is: a production ML pipeline that trains, validates, and ships the **NGAV (Next-Generation Antivirus)** binary malware classifier for Windows PE files.

## Read in order
1. [[01 - Project Overview]] — what it is, why it exists
2. [[02 - Pipeline Architecture]] — end-to-end data flow (the canonical diagram)
3. [[03 - Pipeline Stages]] — what each script does
4. [[04 - ML Model & Hyperparameters]] — LightGBM, the actual model
5. [[05 - Configuration Reference]] — `configuration.py` constants, the project's "constitution"
6. [[06 - Decision Gate]] — the AUC gate that blocks bad models
7. [[07 - Threshold Optimization]] — cautious / moderate / aggressive operating points
8. [[08 - Infrastructure & Deployment]] — GCP, Jenkins, Docker, Artifactory
9. [[09 - Testing Strategy]] — validation gates between stages
10. [[10 - Technical Debt & Open Issues]] — what's smelly
11. [[11 - Glossary]] — domain terms (vhash, broccoli, stool, …)

## Quick mental model
- **Input:** raw PE files (EXE/DLL) sampled from VirusTotal feed.
- **Output:** a LightGBM `.classifier.pkl` + thresholds + an allowlist + `.features.conf` / `.model.conf` for the production scanner.
- **Two host platforms:** Linux (data prep + training) and Windows (PE feature extraction via `ngav-stool-featuregen`).
- **Two file types per run:** Win32 EXE and Win32 DLL (handled side-by-side, often with different parameters).
- **Two label dimensions:** managed (.NET) vs unmanaged (native) — picked at run start, not mixed.
- **Three operating thresholds:** aggressive (low-FPR allowlist gen), moderate, cautious.

## Cross-project links
- This is the **production pipeline**. Compare it to the experimental [[../virustotalclassifier-meta/00 - Index|virustotalclassifier (meta models)]] which classifies via AV-engine consensus rather than PE features.
