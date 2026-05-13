---
title: BitDefender
type: system
tags: [system, wiki]
owner: BitDefender (vendor)
vendor: BitDefender
related_projects: ["[[NGAV]]", "[[MLAV]]"]
seeds:
  - raw/projects/Project - MLAV/Project MLAV.docx.md
  - INBOX/converted/data-science-main.md
last_updated: 2026-05-11
---

# BitDefender

> Third-party antivirus engine embedded as the first detection layer in the Cybereason sensor — NGAV acts on the ~15% of samples BitDefender leaves undecided.

## Owner / vendor

BitDefender (commercial AV vendor).

## Integration surface

- AV engine integrated into the Cybereason sensor.
- Receives PE/DLL file input from the sensor; emits classifications consumed by downstream detection engines.

## Data flow

PE/DLL on endpoint → BitDefender AV engine → if decided (~85% of samples), it's classified by BitDefender; if undecided, NGAV acts as the second-layer ML detector. NGAV's training set is built from BitDefender-benign samples (then re-labelled Malicious/Benign by [[META]] / Broccoli).

## Current usage

- [[NGAV]]: first-layer AV decision; NGAV only runs on BitDefender-undecided samples and uses BitDefender-benign as a training pool.
- [[MLAV]]: explicitly designed not to depend on BitDefender (parallel detector path).

## Known issues

- BitDefender accuracy ~85% — undetected malicious files in the remaining 15% are the gap NGAV is built to close.

## Related entities

[[NGAV]], [[MLAV]], [[Core]]

## Open questions
