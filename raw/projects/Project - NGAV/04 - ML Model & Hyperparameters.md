---
tags: [ngav, ml, lightgbm, model]
type: reference
project: ngav-pipeline
---

# ML Model & Hyperparameters

## The model
**LightGBM** binary classifier (`malicious` vs `benign`). One model per `(files_type, PE_type)` cross — though training is unified across EXE+DLL and only validation/test/threshold are PE-type-specific.

## Hyperparameters (`lgbm_metaparams.py`)

```python
metaparams = {
    'n_estimators':        300,
    'num_leaves':          300,
    'scale_pos_weight':    1,
    'min_child_weight':    10,
    'min_data_in_leaf':    10,
    'subsample':           0.65,
    'colsample_bytree':    0.8,
}
```

### Why these values (interpretation)

| Param | Value | Why it matters |
|-------|-------|----------------|
| `n_estimators` | 300 | Moderately deep ensemble. With 300 leaves per tree, this is already very high-capacity — there's a real overfitting risk if the dataset gets too small. |
| `num_leaves` | 300 | **Aggressive**. LightGBM's `num_leaves` controls tree complexity; 300 is way above the typical 31–127. The pipeline relies on the size of the dataset (target ≥ 1M training rows for unmanaged) to absorb that capacity. |
| `scale_pos_weight` | 1 | No class imbalance reweighting. The pipeline relies on the **enforced 50/50 distribution** in `data_preparation.py` instead. If you change `malicious_benign_distribution_min`, revisit this. |
| `min_child_weight` | 10 | Conservative leaf-stability constraint — prevents 1-row leaves. |
| `min_data_in_leaf` | 10 | Same idea; both are anti-overfit guardrails for the high `num_leaves`. |
| `subsample` | 0.65 | Row bagging. Adds variance reduction. |
| `colsample_bytree` | 0.8 | Feature bagging. Mild — most features are kept per tree. |

> **Mental model:** "wide and bagged" — high tree complexity, but with row/feature subsampling and minimum-leaf-weight to keep individual trees from memorising. Effective only because the upstream pipeline guarantees ≥1M (unmanaged) / ≥500K (managed) training rows (`minimal_training_total_amount_of_samples`).

## Inputs (features)
Produced by `ngav-stool-featuregen` on Windows. Tabular, dense. They include (per the codebase's references):
- PE structural fields (sections, entropy, sizes)
- Imports / exports table
- Version-info strings
- Certificate / signing metadata
- BitDefender's own score (used both as a feature and as a runtime co-decision in `combine_model_prediction_with_AV`)

> The full feature schema lives in the `featuresinfra` package; treat it as black-box from the pipeline's POV.

## Output
- `predict_proba(X)` → `(P_benign, P_malicious)` per sample.
- `pred_by_threshold(model, X, thr)` (in `pipeline_utils.py`) gates on `P_malicious ≥ thr`.

## Combined decision in production
At inference, the pipeline tests its model **combined** with BitDefender:

```
combine_model_prediction_with_AV(model_pred, av_pred)
```

Effectively: trust BitDefender's "malicious" call AND the model's own threshold. The model is therefore tuned to **add precision on top of an existing AV signal**, not to replace it.

## Optional sample weighting
`data_preparation.py` computes `calculates_weights_time_resolution_based()` — newer samples get more weight, day-resolution. Weights sum to 1.0. **The `--weights` flag is commented out in `train_model.py`'s call to `crossguard.train.train`** — so weighting is built but currently disabled. Likely was tried, didn't help convergence, and was shelved.

## Acceptance bar (built-in)
Beyond the [[06 - Decision Gate]] AUC comparison:
- Test recall must be ≥ validation_recall − 2pp.
- Test FPR must be ≤ validation_FPR + 10pp.
  (warned, not enforced — see [[10 - Technical Debt & Open Issues]])

## Related
- [[05 - Configuration Reference]] — dataset-size constants that justify these hyperparameters.
- [[06 - Decision Gate]] — the model promotion check.
- [[07 - Threshold Optimization]] — operating-point selection.
