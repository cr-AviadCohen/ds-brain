---
tags: [ngav, decision-gate, model-promotion, qa]
type: note
project: ngav-pipeline
---

# Decision Gate

The single most important pipeline stage. Without it, retraining could silently ship regressions.

## What it is
`pipeline_scripts/decision_gate.py` — a stage that compares the **freshly trained model** against the **previously shipped model** and decides whether to ship.

## The check (in plain English)
1. Load `current_model = *_model.classifier.pkl` from the in-progress run.
2. Find the previous shipped model: walk the Artifactory namespace one level up from the current `model_ID` and grab the immediately previous version's classifier pickle.
3. Run **both** models on the **same EXE test set** (same features, same labels).
4. Compute `calc_auc_score_wrapper()` for each → `curr_auc`, `last_auc`.
5. Decide:
   - `curr_auc > last_auc` → write `is_valuable_model=true`, continue.
   - `curr_auc ≤ last_auc` and `--upload-lower-auc` flag NOT set → write `is_valuable_model=false`, **`exit(1)`** (whole pipeline fails, nothing uploaded).
   - `curr_auc ≤ last_auc` and `--upload-lower-auc` flag SET → write `is_valuable_model=false`, continue (manual override; a human decided to ship a regression knowingly).
6. Also computes & logs DLL AUC for traceability — but **does not gate on DLL**. (See [[10 - Technical Debt & Open Issues]].)

## Why a single metric (AUC)?
- AUC is **threshold-independent** — it summarises the model's ranking quality across all possible thresholds. Since the pipeline picks thresholds *downstream* of the gate, comparing on AUC is the right primitive.
- Using accuracy / precision / recall would couple the gate to a specific threshold, which would be circular.
- **Limitation:** AUC can mask local failures. A model that's globally better but worse in the operational regime (low FPR) will still pass.

## Why only EXE?
The gate compares *only* on the EXE test set. DLL is logged but ignored. This was almost certainly a pragmatic choice — EXE volume dominates user impact — but it leaves a real hole: a regression localised to DLL would ship undetected.

## The override flag
`--upload-lower-auc` is a release-engineering escape hatch. Used when:
- The previous model has a known issue (e.g. it shipped an over-aggressive cautious threshold).
- You want to ship a known-slightly-worse model to avoid blocking a release.
- The drop is within noise.

## What "is_valuable_model" actually does
That file is read by the Jenkins post-stage logic. It controls the **Artifactory upload step**:
- `true` → uploaded to a "promoted" path that the production engine consumes.
- `false` (with override) → uploaded to a "research" path that's still inspectable but isn't auto-consumed.

## Failure modes worth knowing
- **First-ever run for a `files_type`**: there is no previous model. Code currently expects to find one one-level-up; if missing, the gate either crashes or falls through. Worth checking before kicking off a new product line.
- **Previous model trained on incompatible features**: AUC comparison is only meaningful if both models accept the **same feature set**. Major feature-schema bumps invalidate the comparison — typically gated manually with `--upload-lower-auc` for the version-bump release.
- **Test set leakage**: if the new training set's date window overlaps the test set window, `curr_auc` is inflated. The pipeline doesn't enforce a strict temporal split between training and test windows; relies on operator discipline.

## Mental model
> "Every retrain has to **prove on a holdout set** that it's at least as good as the model it replaces, on the AUC of the dominant file type. Anything else is a manual override."

## Related
- [[02 - Pipeline Architecture]] — where the gate sits.
- [[04 - ML Model & Hyperparameters]] — the model being judged.
- [[10 - Technical Debt & Open Issues]] — DLL-blindness, first-run handling.
