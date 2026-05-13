---
title: VirusTotal
type: system
tags: [system, wiki]
owner: Google (vendor)
vendor: Google
related_projects: ["[[META]]", "[[MLAV]]", "[[NGAV]]", "[[AIDRA]]", "[[CMD Classification]]"]
seeds:
  - raw/projects/Project - META/01 - Project Overview.md
  - raw/projects/Project - MLAV/Project MLAV.docx.md
  - raw/projects/Project - NGAV/01 - Project Overview.md
  - raw/projects/Project - AIDRA/AIDRA.md
last_updated: 2026-05-11
---

# VirusTotal

> Multi-engine antivirus aggregator (Google) whose per-sample report (~70 engine verdicts plus tags and metadata) is the primary external signal for the team's label pipelines and meta classifiers.

## Owner / vendor

Google (acquired from VirusTotal/Hispasec).

## Integration surface

- VirusTotal BigQuery feed (consumed for sample labels in NGAV and MLAV pipelines).
- Public API for live IOC lookups (used by AIDRA's Threat Intelligence agent).
- VirusTotal Retrohunt (integration point in Detection Engineering Hub).

## Data flow

VT BigQuery → NGAV pipeline pulls labelled PE samples (EXE/DLL, managed/unmanaged) → static features generated on Windows worker → LightGBM training. META consumes per-engine verdicts as its core feature space (level-0 signals for a stacking meta classifier).

## Current usage

- [[NGAV]]: source of training samples + labels (managed/unmanaged EXE/DLL).
- [[META]] (`virustotalclassifier`): consumes ~70 AV-engine verdicts as input feature space.
- [[MLAV]]: trains on hacking-tool samples; complements VT-based labelling.
- [[AIDRA]]: live IOC lookups during script analysis.
- [[CMD Classification]]: 10K .bat files collected from VT for labelling experiments.
- Sage (downloads VirusTotal data daily per data-science-main).

## Known issues

- Engines exhibit bias, echoing (cross-licensed signatures), and detection delays.
- Some engines over- or under-detect — requires referee selection and outlier-robust thresholding (handled in META).

## Related entities

[[META]], [[NGAV]], [[MLAV]], [[AIDRA]], [[CMD Classification]], [[Sage]], [[BigQuery]]

## Open questions
