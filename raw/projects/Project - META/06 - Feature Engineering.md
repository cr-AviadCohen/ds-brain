---
tags: [virustotalclassifier, features, transformers]
type: reference
project: virustotalclassifier-meta
---

# Feature Engineering

The transformers that turn a raw VT report row into the inputs of the estimators. Module: `meta/features_transformers.py`.

## The three transformers

```
                   raw VT report row
                          │
        ┌─────────────────┼──────────────────┐
        ▼                 ▼                  ▼
  scans (verdicts)   scans (results)        tags
        │                 │                  │
        ▼                 ▼                  ▼
 VerdictTransformer  EnginesTokens     TagsTransformer
                     Transformer
        │                 │                  │
        ▼                 ▼                  ▼
   binary matrix     softmax(token         many-hot
   samples × engines  count) per class      encoded
                                            tag set
```

## 1. `VerdictTransformer`
**Input:** the `scans` column — list of dicts `[{name, detected, result}, ...]` per sample.
**Output:** binary matrix `samples × engines` — `True` if engine detected, `False` otherwise.

Steps:
1. Unstack the nested dict-list into a flat DataFrame.
2. Pivot: rows = samples, columns = engine names.
3. Drop engines with > 95% null values (low coverage).
4. Fill NaN with `False` (assumption: missing detection = not detected = benign-from-this-engine's-POV).

**This is the input to the binary phase.** The binary estimator wraps `VirusTotalAnalyzer` over this matrix.

Key parameters:
- `extracted_value` — usually `'detected'` (the boolean field).
- `fillna` — default `False`.

## 2. `EnginesTokensTransformer`
**Input:** the `scans` column — but this time the `result` field (the malware **name** the engine assigned).
**Output:** for each multiclass label, a softmax-normalised score reflecting how much engine names "look like" that class.

Steps:
1. For each sample, concatenate all engine results into one document.
2. Tokenize: lowercase, strip punctuation, drop tokens shorter than 4 chars or all-digit.
3. Replace class words (`downloader`, `dropper`, `exploit`, …) with themselves (canonicalise).
4. `CountVectorizer(min_df=0.0005, use_idf=False)` → bag-of-words across the corpus.
5. For each class, find the **10 most similar tokens** using `difflib.get_close_matches(cutoff=0.7)`. Recursive: similar to similar to similar, building a small token cluster per class.
6. Sum the counts of those tokens per sample → raw score per class.
7. **Softmax** across classes → normalised probability per class.

Output columns: `token_downloader`, `token_dropper`, `token_exploit`, etc. (one per configured class).

**Mental model:** "Most engines name malware in human-readable strings (`Trojan.Downloader.X`, `Backdoor.Dropper.Y`). The tokens in those names are themselves a signal of class. Use the engines as implicit labellers."

## 3. `TagsTransformer`
**Input:** the `tags` column — VirusTotal-curated tags like `cve-2022-12345`, `macros`, `powershell`, `download`, `exploit`, …
**Output:** many-hot encoded indicator features.

Steps:
1. Apply `ManyHotEncoder` (each tag → its own boolean column, multiple tags per sample possible).
2. **Aggregate related tags**:
   - `cve-*` (any specific CVE tag) → unified `cve` column.
   - `macros` + `powershell` → `marcos_plus_powershell` column.
3. Output columns: `tag_download`, `tag_exploit`, `tag_cve`, `tag_marcos_plus_powershell`, …

**Mental model:** "VT has already done some classification work via tags. We use that work as features."

## How they're combined in the multiclass pipeline

```python
DataFrameMapper([
   (['tags'],  TagsTransformer()),
   (['scans'], FeatureUnion([
       VerdictTransformer(extracted_value='detected'),
       EnginesTokensTransformer(extracted_value='result', classes=...)
   ])),
])
```

So a multiclass sample's feature vector is:
- many-hot tag indicators
- engine verdict booleans
- per-class softmax token scores

These all flow into `MetaMultiEstimator` for rule evaluation.

## Special transformer: `VTAnalyzerMinMaxScore`
Not used to compute features for the model directly — used **inside** `MetaBinaryEstimator` to scale the maliciousness score. Fits a `MinMaxScaler` only on samples with `positives ≤ 30` (avoids saturation from extreme cases). Used to normalise the score to `[0, 1]` for thresholding.

## Mental model
> "Two signals from VT: who-detected-it (verdicts) and what-they-called-it (names + tags). Verdicts feed the binary phase; names + tags feed the multiclass phase."

## Edge cases / caveats
- The 95% null threshold for VerdictTransformer drops new / experimental engines that haven't built coverage yet.
- The 0.0005 `min_df` in `EnginesTokensTransformer` means tokens must appear in at least 0.05% of samples. With < 50K samples, a token has to appear in ≥ 25 samples to be kept.
- `difflib.get_close_matches` with cutoff 0.7 is fairly permissive — can pull in noisy tokens. Worth audit if a class has surprising performance.
- TagsTransformer's hand-crafted aggregations (`marcos_plus_powershell` typo and all) are configuration-driven but not strongly validated.

## Related
- [[03 - Meta Model Concept]] — why we have two channels (verdicts + tokens).
- [[07 - Binary Estimator]] — consumes the VerdictTransformer output.
- [[08 - Multiclass Estimator]] — consumes all three.
