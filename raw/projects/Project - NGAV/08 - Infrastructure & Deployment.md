---
tags: [ngav, infra, jenkins, docker, gcp, artifactory]
type: reference
project: ngav-pipeline
---

# Infrastructure & Deployment

The "where does this run, and how does the bytes get from VirusTotal to a shipped scanner" view.

## Hosts

| Job | Host kind | Files | Why |
|---|---|---|---|
| Linux pipeline | `lin-jenkins-ngav-slave` (Linux, dockerised) | `utils/Jenkinsfile`, `utils/Dockerfile` | data prep, training, evaluation, packaging |
| Windows feature gen | `ngav-generate-features-windows` Jenkins agent | `utils/Jenkinsfile_windows_job` | `ngav-stool-featuregen` only runs on Windows |

## Jenkins (Linux master)
`utils/Jenkinsfile`. Pipeline-as-code. Stages (one-line each):

1. **Clone** `cybereason-labs/research` (`dotnet-pipeline` branch in current Jenkinsfile — note: not `python3`).
2. **Determine model_ID / version** — calls Artifactory's `last_modified_artifact` API; bumps minor on data-only re-run, major on git changeset.
3. **Build/pull Docker image** `cybereason/linux_ngav_pipeline:ngav_model_generator`.
4. **`create_datasets`** stage.
5. **Trigger Windows job** (`generate_features`) and wait.
6. **`data_preparation`**.
7. **`train_model`**.
8. **`threshold_optimization`**.
9. **`model_test`**.
10. **`generate_allowlist`**.
11. **`decision_gate`**.
12. **`model_extraction`**.
13. **Upload to Artifactory** via `curl` with API token to `${ARTIFACTORY_URL}/ngav-pipeline/{files_type or research}/{model_ID}/`.

### Jenkins parameters (the knobs you set when triggering)
- `files_type` — `unmanaged` | `managed`
- `exe_datasets_dates_range` / `dll_datasets_dates_range`
- `training_samples_amount`
- `conditions` — flags like `post_bd`, `replace_bd`, `stark_labels`, `ransomware`, `dotnet`, `cert_test`
- `starting_point` — restart at any stage
- `upload-lower-auc` — override the [[06 - Decision Gate]]

## Docker image
`utils/Dockerfile`:

- Base: **python:3.8-slim-buster**.
- System deps: `pdftk`, `wkhtmltopdf` (used to merge error-message PDFs in `model_extraction`).
- Python deps installed from internal Cybereason **JFrog PyPI**:
  - `pandas_extras==3.4.29`, `sklearn_extras`, `binstore`, `hanabase==3.4.204` (BigQuery), `vtutils`, `cyberlib==3.0.378`, `featuresinfra`, `ultima`.
- `WORKSPACE → /output`, `PYTHONPATH` includes the cloned research/ngav paths.
- Runs as root.

The Docker image is **opinionated and pinned** — pinning major Cybereason internal libs is what allows the pipeline's behaviour to be reproducible across reruns.

## Storage layers

```
                BigQuery
                vt_file_report_feed_1
                       │ (build_dataset)
                       ▼
                  ┌───────────┐
                  │   GCS     │   bucket: lin-win-ngav
                  │  (data    │     - datasets
                  │   plane)  │     - features
                  │           │     - allowlists
                  └─────┬─────┘
                        │ (output of pipeline)
                        ▼
                ┌──────────────┐
                │ Artifactory  │   ngav-pipeline/{files_type}/{model_ID}/
                │  (model      │     - *.classifier.pkl
                │   registry)  │     - thresholds_*.pkl
                │              │     - allowlist_final_*.csv
                │              │     - *.features.conf, *.model.conf
                │              │     - reports.pdf
                └──────────────┘
                        │
                        ▼
                  NGAV scanner
                  (production C++ binary)
```

## GCP integration (`utils/gcp_bucket_utils.py`)
- **Bucket name**: `lin-win-ngav` (hardcoded — see [[10 - Technical Debt & Open Issues]]).
- **Credential paths** (OS-aware, hardcoded):
  - Linux: `/opt/jenkins/workspace/ngav-model-generator/research/ngav/pet_ops/pipeline/utils/gcs_bucket_credentials.json`
  - Windows: `C:/users/admin/pipeline_creds/gcs_bucket_credentials.json`
- Uses `google.cloud.storage` Python SDK.
- **BigQuery** uses a separate credential (`vt_feeder_credentials.json`) and the `hanabase` wrapper.

## Artifactory layout
`{ARTIFACTORY_URL}/ngav-pipeline/{files_type | "research"}/{model_ID}/<file>`

`model_ID` is `{files_type}_{major}.{minor}_{dd-mm-yyyy}`.

The `decision_gate` looks **one level up** to find sibling versions, picks the immediately previous, and pulls its classifier pickle for AUC comparison.

## Quicklib package (`quicklib_setup.yml`)
The pipeline is published as a Cybereason internal package via `quicklib`.
- Entry point: `ngav-pipeline-script = pipeline:path_to`
- Declared deps include: `cr-crossguard` (training core), `ngav-samplesets`, `ngav-protect` (model export), `awscli`.

## Mental model
> "Jenkins orchestrates two hosts (Linux + Windows) talking through one GCS bucket. Linux trains and gates; Windows extracts features. Output lands in Artifactory under a versioned path that the production scanner pulls from."

## Related
- [[02 - Pipeline Architecture]]
- [[06 - Decision Gate]]
- [[11 - Glossary]] for `quicklib`, `hanabase`, etc.
