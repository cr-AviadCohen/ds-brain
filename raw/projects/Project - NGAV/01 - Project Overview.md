---
tags: [ngav, overview]
type: note
project: ngav-pipeline
---

# Project Overview

## One-sentence summary
`ngav/pet_ops/pipeline` is the **MLOps pipeline** that produces the NGAV (Next-Gen Antivirus) static-analysis classifier — a LightGBM model that, given a Windows PE file, decides "malicious vs benign".

## What it actually does
A Jenkins-driven pipeline that:
1. Pulls labelled PE samples from the **VirusTotal BigQuery feed** (separately for EXE and DLL, separately for managed / unmanaged).
2. Generates **static-analysis features** from each PE binary on a Windows worker via the internal `ngav-stool-featuregen` tool.
3. Cleans, deduplicates, and balances the dataset (50/50 malicious/benign).
4. Trains a **LightGBM** binary classifier with optional time-decay sample weighting.
5. Optimises **three thresholds** (cautious / moderate / aggressive) on the validation set.
6. Generates an **allowlist** (very-low-FPR malicious predictions over a pool of likely-benign samples).
7. **Gates the model**: only ships if its test-AUC ≥ the previously shipped model's AUC.
8. Exports the model into the production-consumable formats (`.features.conf`, `.model.conf`).
9. Uploads everything to **JFrog Artifactory** with a versioned path.

## Why it exists
NGAV ships as part of Cybereason's endpoint product. The pipeline exists to:
- Retrain the malware classifier as the threat landscape changes.
- Keep the model honest: every retrain has to **prove it's better** than the one it replaces (see [[06 - Decision Gate]]).
- Maintain a **separate** allowlist of high-confidence benigns for production consumption.
- Produce reproducible, versioned artefacts (model + thresholds + allowlist) that the engine can consume.

## What it is *not*
- Not a real-time scanner — it's the **trainer**. The actual scanning happens in C++ NGAV components consuming the exported `.model.conf`.
- Not a DL pipeline — it's classical ML (LightGBM on tabular PE features).
- Not the [[../virustotalclassifier-meta/00 - Index|virustotalclassifier]] meta-model: that one classifies *based on AV-engine consensus*; this one classifies *based on PE static features*. They are independent systems.

## Key actors
- **Jenkins** orchestrates (`utils/Jenkinsfile`, plus a Windows-only feature-gen job).
- **Docker** isolates the Linux side (`utils/Dockerfile`).
- **GCS bucket `lin-win-ngav`** is the inter-stage data plane (datasets, features, allowlists shuttled between Linux and Windows jobs via this bucket).
- **JFrog Artifactory** is the artefact store (`ngav-pipeline/{files_type}/{model_ID}/`).

## File-type axis
Every run produces two parallel artefact families: one for **Win32 EXE**, one for **Win32 DLL**. They share the training set but have different validation/test sets and different threshold-validity bands (see [[05 - Configuration Reference]]).

## Run inputs (Jenkins parameters)
- `files_type`: `unmanaged` or `managed`
- `exe_datasets_dates_range`, `dll_datasets_dates_range` — sampling windows
- `training_samples_amount` — target training-set size
- `conditions` — optional dataset filters (post_bd, replace_bd, stark_labels, ransomware, dotnet, cert_test)
- `starting_point` — restart at any pipeline stage
- `upload-lower-auc` — override the [[06 - Decision Gate]]

## Versioning scheme
`{files_type}_{major}.{minor}_{dd-mm-yyyy}` e.g. `unmanaged_3.7_05-05-2026`.
- **Minor** bumps on data-only re-runs (no code change since last build).
- **Major** bumps when the pipeline code itself changed.
- Decided automatically from `last_modified_artifact()` + git changeset detection.
