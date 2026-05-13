#!/bin/bash
# Weekly LLM lint via Claude Code in non-interactive mode.
set -euo pipefail

cd /home/dsbrain/ds-brain
git fetch --quiet origin unified
git reset --hard origin/unified

mkdir -p logs
claude -p "/lint" --output-format=json 2>&1 | tee -a "logs/lint-$(date +%F).log"
