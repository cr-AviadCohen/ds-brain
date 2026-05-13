#!/bin/bash
# SessionStart hook: if INBOX/ has files (other than README.md), inject a
# system reminder telling Claude to run /ingest.
set -e

INBOX_DIR="${CLAUDE_PROJECT_DIR:-.}/INBOX"
files=$(ls -1 "$INBOX_DIR" 2>/dev/null | grep -v '^README\.md$' || true)

if [ -z "$files" ]; then
  exit 0
fi

count=$(printf '%s\n' "$files" | wc -l | tr -d ' ')

jq -n --arg files "$files" --arg count "$count" '{
  hookSpecificOutput: {
    hookEventName: "SessionStart",
    additionalContext: ("INBOX has \($count) unprocessed file(s) waiting for ingest:\n\($files)\n\nRun /ingest to process them into the wiki layer per CLAUDE.md.")
  }
}'
