# ds-brain (branch: unified)

Data Science team second brain based on Karpathy-style LLM Wiki
(https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f). The brain
runs continuously on a team Ubuntu VM; Obsidian Desktop and Claude Code both
read/write the same repo.

## Quick start (DS member, laptop)

1. Clone: `git clone git@github.com:<org>/ds-brain.git && cd ds-brain`
2. `git checkout unified`
3. Open `ds-brain/` as an Obsidian vault. Enable Smart Connections (already
   in `.obsidian/community-plugins.json`).
4. Drop a new source into `INBOX/` and run `/ingest` in Claude Code. The
   SessionStart hook will remind you if INBOX/ has unprocessed files.
5. Read `CLAUDE.md` for the layer model and `wiki/<folder>/README.md` for
   the conventions of each folder.

## Slash commands (in `.claude/commands/`)

| Command | Purpose |
| --- | --- |
| `/ingest <path>` | Process a source from INBOX/ (or any raw/ note) into wiki/ |
| `/query <question>` | Synthesise a cited answer against the wiki |
| `/lint` | Deterministic + LLM health checks |
| `/remove <topic>` | Two-pass removal with reference cleanup |
| `/braindump <thoughts>` | Append free-form thought stream; Claude files it |

## Layers (Karpathy)

| Layer | Where | Who writes |
| --- | --- | --- |
| Raw | `raw/`, `INBOX/` | Humans (immutable to Claude — guarded by PreToolUse hook) |
| Wiki | `wiki/{Entities,Meetings,Decisions,Ideas,Research,Syntheses,Sources,Connections,🔥 Hot Notes,🗺️ Maps,📦 Archive,Memories,Log}/` | Claude |
| Schema | `CLAUDE.md`, `.claude/`, `tools/`, `server/` | DS leadership + Claude |

## Tooling (`.claude/hooks/`, `tools/`, `server/`)

- `.claude/hooks/guard_immutable.py` — PreToolUse guard blocking writes to
  `raw/` and `INBOX/`
- `tools/lint/run_all.py` — deterministic lint (frontmatter / orphans /
  stale links) with thread-pooled fan-out
- `tools/convert/` — `.docx` and `.xlsx` → Markdown converters for ingest
- `server/` — Ubuntu VM automation runtime: systemd-driven `auto-ingest`
  (every 5 min) + `auto-lint` (weekly). See `server/README.md`.

## Triggers

- **SessionStart** — `.claude/hooks/inbox-check.py` flags unprocessed INBOX/
  files
- **PreToolUse (Bash, Write, Edit)** — `.claude/hooks/guard_immutable.py`
  enforces raw/ immutability
- **Ubuntu VM (systemd user timers)** — `server/jobs/auto_ingest.py` every
  5 min ingests new `INBOX/` files via `claude -p "/auto-ingest …"`;
  `server/jobs/auto_lint.py` weekly (Sun 03:00) runs `claude -p "/auto-lint"`.
  Both open `PR Auto-Inject - …` / `PR Auto-Lint - …` PRs and auto-squash-merge
  when blast-radius caps pass.

## License

Internal — Cybereason / Level Blue Data Science.
