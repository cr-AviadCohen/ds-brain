# Data Science Brain — MCP setup

One-time install. Each DS team member runs this on their own machine. Takes ~5 minutes.

The GitHub MCP is **required** — the skill won't read or write the brain without it. There is no filesystem, Bash, or local-git fallback. No Obsidian dependency.

## What you'll install

| MCP | Purpose | Backend |
|-----|---------|---------|
| `github` | Read, search, and write the brain via the GitHub API | `@modelcontextprotocol/server-github` + your own GitHub fine-grained token |

The MCP registers as a **user-scoped** server in `~/.claude.json`. Credentials stay on your machine and are **per-user** — each member generates their own; never share, never commit.

---

## Prerequisites

Confirm:

```bash
# npx installed — needed for the GitHub MCP
which npx
```

If `npx` is missing, install Node.js (https://nodejs.org/) or via `brew install node`.

A local clone of `ds-brain` is **not needed** — all reads and writes go through the GitHub API.

---

## Step 1 — Generate your own GitHub fine-grained token

**Hard rule.** Every team member generates their own token. Never share it, never commit it, never paste it into any chat or shared doc. A token authors commits as the GitHub user who created it — sharing one destroys audit trail and creates a single point of failure on revocation.

1. Go to https://github.com/settings/personal-access-tokens/new (fine-grained — preferred over classic).
2. **Token name:** `ds-brain-mcp` or anything you'll recognize.
3. **Expiration:** as short as your security policy allows (90 days is reasonable).
4. **Resource owner:** the org / user owning the repo (`cybereason-labs`).
5. **Repository access → Only select repositories →** check `cybereason-labs/ds-brain` only. Do not grant access to all repositories.
6. **Repository permissions:**
   - **Contents: Read and write** (required — reads notes and creates INBOX files)
   - **Metadata: Read-only** (auto-required by GitHub)
   - Optional: **Pull requests: Read and write** — only needed if you want the skill to open PRs for INBOX entries instead of direct commits.
7. Generate the token. **Copy it once** — GitHub won't display it again. Save it to your password manager.

## Step 2 — Register the GitHub MCP

Replace the placeholder with your token from Step 1:

```bash
claude mcp add github -s user \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token-from-step-1> \
  -- npx -y @modelcontextprotocol/server-github
```

The token lands in `~/.claude.json` under the `github` server's `env` block. That file is on your machine only and is not part of any repo. Confirm its permission mode:

```bash
chmod 600 ~/.claude.json
ls -l ~/.claude.json   # expect -rw------- (owner only)
```

## Step 3 — Verify

```bash
claude mcp list
```

Expect `github` to show **✓ Connected**.

If it shows ✗ Failed to connect → see Troubleshooting below.

---

## Step 4 — Restart Claude Code

New MCP tools only surface on session start. Quit Claude Code, reopen. Then test:

- **Read test:** "What do we know about Tipper?" — should pull from the wiki via `mcp__github__search_code` + `mcp__github__get_file_contents`.
- **Write test:** "Save a quick smoke-test note to the brain." — should create an INBOX file via `mcp__github__create_or_update_file` and return a commit SHA. Confirm on GitHub that the commit was authored by your GitHub user.

---

## Troubleshooting

### `✗ Failed to connect` — GitHub

1. **Token typo or expired.** Regenerate the fine-grained token per Step 1, then:
   ```bash
   claude mcp remove github -s user
   claude mcp add github -s user -e GITHUB_PERSONAL_ACCESS_TOKEN=<new-token> -- npx -y @modelcontextprotocol/server-github
   ```
2. **`npx` not in PATH.** Rare on macOS. If so, register with the absolute path of `npx`:
   ```bash
   NPX=$(which npx)
   claude mcp add github -s user -e GITHUB_PERSONAL_ACCESS_TOKEN=<token> -- "$NPX" -y @modelcontextprotocol/server-github
   ```

### Read fails — `404 Not Found`

The skill targeted a wrong path or branch. Defaults: `owner=cybereason-labs`, `repo=ds-brain`, `ref=unified`. If your team uses a different branch, tell the skill explicitly.

### Search returns nothing for a recent commit

GitHub code-search index lags ~1 minute and skips files >384 KB. Wait a beat and retry, or have the skill fall back to a directory listing via `get_file_contents` on the parent folder.

### Write fails — `401 Unauthorized`

Your token is invalid, expired, or revoked. Regenerate per Step 1 and re-register per Step 2.

### Write fails — `403 Forbidden`

Your token lacks `Contents: Read and write` on `cybereason-labs/ds-brain`, **or** you aren't a collaborator on that repo. Fix the scope per Step 1. If you don't have collaborator access, ask the maintainer.

### Write fails — `404 Not Found`

The skill targeted a wrong `owner` / `repo` / `branch`. Defaults: `cybereason-labs` / `ds-brain` / `unified`. If your team uses a different branch, tell the skill explicitly.

### Write fails — `409 Conflict` / stale SHA

Someone updated the same file while you were composing. The skill should re-fetch the latest SHA and retry. If it keeps failing, the file isn't actually new — pick a different slug.

### Write fails — `422 Unprocessable Entity`

Usually a branch-protection rule (e.g., direct push blocked, PR required). Either ask the maintainer to allow direct push to `unified` for `INBOX/`, or have the skill open a PR per INBOX entry instead.

### Rate limit hit

GitHub fine-grained tokens get 5000 requests/hour. Wait for the reset window (shown in response headers).

### Lost or leaked token

Treat any token that's been pasted into chat, screen-shared, or printed in logs as compromised.

1. https://github.com/settings/tokens → revoke immediately.
2. Generate a fresh one per Step 1.
3. Re-register per Step 2.

### "I can't see GitHub tools in my session"

You haven't restarted Claude Code. The tool list is fixed at session start.

---

## Uninstall

```bash
claude mcp remove github -s user
```

Then revoke your GitHub token at https://github.com/settings/tokens if you won't use it elsewhere.

---

## Why user scope, not project scope?

The GitHub fine-grained token is a **per-user** credential. Committing a project-scoped `.mcp.json` to the repo would either leak each member's secret or force everyone to share one credential — both unacceptable (the GitHub token in particular would erase audit trail since every commit would be authored by the token's owner). User scope keeps each credential in `~/.claude.json` on its owner's machine, while the skill itself ships via the repo and works for any member who completes this one-time setup.
