---
tags: [ngav, tech-debt, observations]
type: note
project: ngav-pipeline
---

# Technical Debt & Open Issues

What's smelly in the codebase, ordered by likely impact. Useful when reading the code or planning refactors.

## High impact

### 1. Live merge conflict in `data_preparation.py` 🔴
Git conflict markers (`<<<<<<< HEAD` / `=======` / `>>>>>>> 5e38efc...`) are visible in the file at the weighting block. The code branches on dataset enumeration vs. simple weight calculation depending on which side "wins". Resolving this is **the first thing to do** before trusting the file.

### 2. `model_test.py` doesn't halt on validation/test mismatch 🟠
The pipeline checks that test recall ≥ validation_recall − 2pp and test FPR ≤ validation_FPR + 10pp, but `exit(1)` is commented out. Mismatches log warnings only — no enforcement. Either:
- the gate was intentionally relaxed (rare events causing false alarms), or
- it was disabled to debug and never re-enabled.

Recommendation: re-enable, but make it bypassable via a `--allow-validation-drift` flag instead of being silently disabled.

### 3. `decision_gate` only gates on EXE AUC 🟠
DLL AUC is computed and logged, but **not gated**. A DLL-localised regression ships unnoticed. See [[06 - Decision Gate]] for context.

### 4. Time-decay weighting is built but disabled 🟡
`data_preparation.py` computes `*_training_set_weights.pkl`, but the `--weights` flag in `train_model.py`'s call to `crossguard.train.train` is **commented out**. Weighting is shelved.

Either:
- delete the weighting code (dead code), or
- re-enable it with metrics tracking the contribution.

The middle state (compute-but-don't-use) is the worst — it consumes test budget for no production value.

## Medium impact

### 5. Hardcoded `broccoli_compensator` thresholds 🟡
In `build_dataset.py`: relabel `(benign, positives ≥ 15) → malicious`, drop `(malicious, positives ≤ 4)`. These magic numbers compensate for a known broccoli labeller bug. They should be:
- linked to the broccoli docs explicitly,
- moved to `configuration.py`,
- ideally retired by fixing broccoli labelling at the source.

### 6. Allowlist size cap of 1500 is arbitrary 🟡
`GenerateAllowlistTest.test_size`: `< 1500`. No comment justifies the number. Likely a "if it's much bigger, something went wrong" sanity check.

### 7. No data-loss enforcement, only warning 🟡
`data_preparation.py` flags when > 15% of samples are dropped, but doesn't fail. A run that hemorrhages 50% of samples will continue.

### 8. BigQuery query is inline, parameter-light, ~200 lines 🟡
`build_dataset.py` generates a giant CTE inline. Hard to test, hard to version, hard to read. Consider:
- moving the query to `.sql` files,
- using parameterized queries explicitly,
- testing against a query plan / explain.

## Low impact

### 9. Hardcoded credentials paths 🟢
Both Linux and Windows GCS credential paths are hardcoded in `gcp_bucket_utils.py`. Should be env-var-overridable.

### 10. Hardcoded GCS bucket name 🟢
`lin-win-ngav` is hardcoded. Same fix.

### 11. Error-message aggregation is per-script 🟢
Multiple `error_messages_{exe,dll}.txt` files accumulate in different stages and are only merged into PDFs at `model_extraction`. Could be centralised into a single structured log.

### 12. Manual cond-post-bd skip for DLL 🟢
`create_datasets.py` disables `--cond-post-bd` for DLL because of "lack of data". This is a hardcoded exception that hides a coverage issue in VirusTotal's DLL feed — worth periodically rechecking whether DLL coverage has improved enough to remove.

### 13. First-run handling 🟢
[[06 - Decision Gate]] assumes a previous model exists in Artifactory one level up. For a brand-new `files_type`, the gate breaks. Should fail gracefully or auto-pass with a warning.

### 14. Test set ↔ training set temporal leakage not enforced 🟢
The pipeline relies on operator-set date ranges for `training_dates_range`, `test_dates_range`, `validation_dates_range` — there's no programmatic check that test/validation date ranges don't overlap training. Easy to spot in review, but easy to miss.

## Categorical observations

### Patterns of strength
- Test-as-gate model is solid — every stage validates its output before the next stage starts.
- Versioning discipline (major/minor/date) is consistent and self-documenting.
- AUC-on-EXE gate, while imperfect, is **the right primitive** for blind A/B over a holdout.

### Patterns of debt
- A lot of "computed but unused" outputs (DLL AUC, weights, validation/test comparison).
- Many magic numbers in tests that should be in `configuration.py`.
- Reliance on hardcoded paths makes local development hard.

## Suggested refactor batches
1. **Resolve merge conflict + re-enable model_test gate** (1–2 days, high value).
2. **Promote magic numbers to configuration.py** (allowlist cap, broccoli compensator thresholds, data-loss threshold).
3. **Make GCS bucket + credential paths env-driven** + rip out OS-specific branches.
4. **Decide on weighting**: delete it or re-enable it with experiments.
5. **Either gate DLL AUC, or document why it's intentionally not gated**.

## Related
- [[03 - Pipeline Stages]] — context.
- [[06 - Decision Gate]] — the EXE-only AUC gate.
- [[09 - Testing Strategy]] — test gate map.
