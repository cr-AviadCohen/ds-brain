---
title: Master Boot Record
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[NGAV]]", "[[META]]"]
related_systems: []
last_updated: 2026-05-13
---

# Master Boot Record

> First 512 bytes of a legacy-partitioned disk ("MBR") — boot code + partition table — historically the most invisible [[Persistence]] target for bootkits and the wipe-target of choice for destructive ransomware.

## What it is

Pre-OS code executed by BIOS firmware before any operating-system protection is in place. Attackers (Petya, NotPetya, GoldenEye, HermeticWiper variants) overwrite the MBR to either chain-load attacker code before Windows boots, encrypt the file system partition table to extort, or destroy boot integrity outright. Modern UEFI systems use GPT + Secure Boot, but plenty of fielded estates still boot MBR. Detection relies on volume write-access monitoring + integrity baselines.

## Why we care

- [[NGAV]] predictive-ransomware-protection module watches raw-disk writes that overwrite the MBR sector — a high-confidence kill signal.
- [[META]] training-set labels include MBR-targeting wipers as a distinct family for the VirusTotal-consensus classifier.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Coverage of UEFI/GPT-targeting bootkits — does [[NGAV]] generalise from the MBR signal or need a separate firmware-write monitor?
