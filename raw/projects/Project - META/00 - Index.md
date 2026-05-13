---
tags: [virustotalclassifier, meta-models, MOC, malware-classification]
type: MOC
created: 2026-05-05
---

# virustotalclassifier (Meta Models) — Map of Content

> Source: `virustotalclassifier/` on `cybereason-labs/research` (branch `python3`).
> What it is: a **meta-classifier** system for malware. Instead of classifying files from raw bytes/features, it classifies them from **the consensus of ~70 AV engines on VirusTotal**.

## Read in order
1. [[01 - Project Overview]] — what it is, why it exists
2. [[02 - Architecture - Five Subsystems]] — meta / broccoli / olive / ginger / snitch
3. [[03 - Meta Model Concept]] — the central idea ("classifier of classifiers")
4. [[04 - Meta Pipeline Flow]] — end-to-end data flow inside `meta/`
5. [[05 - Referee Selection]] — how AV engines are chosen as "voters"
6. [[06 - Feature Engineering]] — VerdictTransformer, EnginesTokensTransformer, TagsTransformer
7. [[07 - Binary Estimator]] — `MetaBinaryEstimator` (the workhorse)
8. [[08 - Multiclass Estimator]] — `MetaMultiEstimator` (rule-based)
9. [[09 - Sister Projects (olive, ginger, snitch)]] — domain-specific configurations
10. [[10 - Broccoli Subsystem]] — KNN/Annoy alternative
11. [[11 - Data Sources]] — VirusTotal, BigQuery, InnoDB
12. [[12 - ML Stack]] — sklearn, dill, annoy, internal libs
13. [[13 - Technical Debt & Observations]]
14. [[14 - Glossary]]

## Quick mental model
- **Input:** a VirusTotal report row (sha1, scans dict, tags, positives, type, vhash).
- **Pipeline (meta):**
  - **Phase 1 (binary, always):** classify malicious / benign using a *learned* classifier over engine verdicts.
  - **Phase 2 (multiclass, only if Phase 1 says malicious):** classify into a fine-grained class (downloader / dropper / exploit / …) using a *rule-based* engine over engine-name tokens + VT tags.
- **Output:** a label and (sometimes) probabilities.
- **Sister wrappers (olive, ginger, snitch):** thin entry points that load a domain-specific JSON config and call `meta.run()`.

## Core insight
Single AV engines are noisy and biased. The system encodes "which engines you trust depends on what you're classifying" via:
1. Statistical **referee selection** (top engines by F-β, β=0.5).
2. **Echo grouping** (engines that always agree are merged into one vote).
3. A **3-zone rule** layered on top of the learned score (low-detection → benign, high-detection → malicious, mid-zone → use the model).

## Cross-project links
- [[../ngav-pipeline/00 - Index|ngav-pipeline]] — production sibling project. Classifies from PE static features instead of AV verdicts. Both projects exist; they're complementary, not competitive.
