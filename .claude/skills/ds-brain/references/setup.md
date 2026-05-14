# Data Science Brain — MCP setup

One-time install. Each DS team member runs this on their own machine. Takes ~5 minutes if Obsidian is already installed.

Both MCPs are **required** — the skill won't read the brain without the Obsidian MCP, and won't write to INBOX without the GitHub MCP. There is no filesystem or Bash fallback.

## What you'll install

| MCP | Purpose | Backend |
|-----|---------|---------|
| `obsidian` | Search / read / traverse the wiki | Obsidian's Local REST API plugin |
| `github` | Create INBOX files on the remote repo via GitHub API | `@modelcontextprotocol/server-github` + your own GitHub fine-grained token |

Both register as **user-scoped** MCP servers in `~/.claude.json`. Credentials stay on your machine and are **per-user** — each member generates their own; never share, never commit.

---

## Prerequisites

Confirm each:

```bash
# Obsidian Desktop installed and the ds-brain vault opened in it
ls ~/Code/ds-brain/wiki/INDEX.md     # adjust path if you cloned elsewhere

# uv (provides uvx) installed — needed for the Obsidian MCP
which uvx                            # should print a path like /opt/homebrew/bin/uvx

# npx installed — needed for the GitHub MCP
which npx
```

If `uvx` is missing: `brew install uv` (macOS) or see https://docs.astral.sh/uv/.

A local clone of `ds-brain` is only needed to give Obsidian a vault to open. Writes go through the GitHub API and do not touch any local clone. If you don't have a clone yet:

```bash
git clone git@github.com:cr-AviadCohen/ds-brain.git ~/Code/ds-brain
```

---

## Step 1 — Install the Obsidian Local REST API plugin

1. Open Obsidian. Open the `ds-brain` vault.
2. Settings → Community plugins → Browse → search **"Local REST API"** (author: Adam Coddington).
3. Install → Enable.
4. Settings → Local REST API. Copy the **API key** shown there. Keep the page open — you'll paste the key in Step 2.
5. Leave the default port (27124 for HTTPS).

The plugin runs an HTTPS server on `127.0.0.1:27124` while Obsidian is open. It dies when Obsidian closes — so keep Obsidian running while you use the skill.

Sanity check from your terminal:

```bash
curl -sk -H "Authorization: Bearer <YOUR_KEY>" https://127.0.0.1:27124/ | head
# Expect: "status": "OK", "authenticated": true
```

---

## Step 2 — Register the Obsidian MCP

Use the absolute path to `uvx` — Claude Code's MCP subprocess doesn't inherit Homebrew's PATH.

```bash
UVX=$(which uvx)
claude mcp add obsidian -s user \
  -e OBSIDIAN_API_KEY=<YOUR_KEY_FROM_STEP_1> \
  -- "$UVX" mcp-obsidian
```

---

## Step 3 — Generate your own GitHub fine-grained token

**Hard rule.** Every team member generates their own token. Never share it, never commit it, never paste it into any chat or shared doc. A token authors commits as the GitHub user who created it — sharing one destroys audit trail and creates a single point of failure on revocation.

1. Go to https://github.com/settings/personal-access-tokens/new (fine-grained — preferred over classic).
2. **Token name:** `ds-brain-mcp` or anything you'll recognize.
3. **Expiration:** as short as your security policy allows (90 days is reasonable).
4. **Resource owner:** the org / user owning the repo (`cr-AviadCohen`).
5. **Repository access → Only select repositories →** check `cr-AviadCohen/ds-brain` only. Do not grant access to all repositories.
6. **Repository permissions:**
   - **Contents: Read and write** (required — creates INBOX files)
   - **Metadata: Read-only** (auto-required by GitHub)
   - Optional: **Pull requests: Read and write** — only needed if you want the skill to open PRs for INBOX entries instead of direct commits.
7. Generate the token. **Copy it once** — GitHub won't display it again. Save it to your password manager.

## Step 4 — Register the GitHub MCP

Replace the placeholder with your token from Step 3:

```bash
claude mcp add github -s user \
  -e GITHUB_PERSONAL_ACCESS_TOKEN=<your-token-from-step-3> \
  -- npx -y @modelcontextprotocol/server-github
```

The token lands in `~/.claude.json` under the `github` server's `env` block. That file is on your machine only and is not part of any repo. Confirm its permission mode:

```bash
chmod 600 ~/.claude.json
ls -l ~/.claude.json   # expect -rw------- (owner only)
```

## Step 5 — Verify

```bash
claude mcp list
```

Expect both `obsidian` and `github` to show **✓ Connected**.

If one shows ✗ Failed to connect → see Troubleshooting below.

---

## Step 6 — Restart Claude Code

New MCP tools only surface on session start. Quit Claude Code, reopen. Then test:

- **Read test:** "What do we know about Tipper?" — should pull from the wiki via Obsidian MCP.
- **Write test:** "Save a quick smoke-test note to the brain." — should create an INBOX file via the GitHub MCP and return a commit SHA. Confirm on GitHub that the commit was authored by your GitHub user.

---

## Troubleshooting

### `✗ Failed to connect` — Obsidian

Likely causes, in order:

1. **Obsidian not running / vault not loaded.** Open Obsidian, open the `ds-brain` vault.
2. **Local REST API plugin not enabled.** Settings → Community plugins. Re-enable.
3. **Wrong API key.** Settings → Local REST API. Regenerate, then:
   ```bash
   claude mcp remove obsidian -s user
   claude mcp add obsidian -s user -e OBSIDIAN_API_KEY=<NEW_KEY> -- "$(which uvx)" mcp-obsidian
   ```
4. **PATH issue — `uvx` not found.** Always register with the absolute path: `$(which uvx)` resolves at registration time. If you registered with a bare `uvx`, the MCP subprocess can't find it. Remove and re-add with absolute path.

### `✗ Failed to connect` — GitHub

1. **Token typo or expired.** Regenerate the fine-grained token per Step 3, then:
   ```bash
   claude mcp remove github -s user
   claude mcp add github -s user -e GITHUB_PERSONAL_ACCESS_TOKEN=<new-token> -- npx -y @modelcontextprotocol/server-github
   ```
2. **`npx` not in PATH.** Rare on macOS. If so, register with the absolute path of `npx`.

### `OBSIDIAN_API_KEY environment variable required`

The MCP subprocess didn't receive the env var. Re-run the `claude mcp add obsidian` command — the `-e KEY=VAL` flag stores it in `~/.claude.json` under the server's `env` block.

### Write fails — `401 Unauthorized`

Your token is invalid, expired, or revoked. Regenerate per Step 3 and re-register per Step 4.

### Write fails — `403 Forbidden`

Your token lacks `Contents: Read and write` on `cr-AviadCohen/ds-brain`, **or** you aren't a collaborator on that repo. Fix the scope per Step 3. If you don't have collaborator access, ask the maintainer.

### Write fails — `404 Not Found`

The skill targeted a wrong `owner` / `repo` / `branch`. Defaults: `cr-AviadCohen` / `ds-brain` / `unified`. If your team uses a different branch, tell the skill explicitly.

### Write fails — `409 Conflict` / stale SHA

Someone updated the same file while you were composing. The skill should re-fetch the latest SHA and retry. If it keeps failing, the file isn't actually new — pick a different slug.

### Write fails — `422 Unprocessable Entity`

Usually a branch-protection rule (e.g., direct push blocked, PR required). Either ask the maintainer to allow direct push to `unified` for `INBOX/`, or have the skill open a PR per INBOX entry instead.

### Rate limit hit

GitHub fine-grained tokens get 5000 requests/hour. Wait for the reset window (shown in response headers).

### Lost or leaked token

Treat any token that's been pasted into chat, screen-shared, or printed in logs as compromised.

1. https://github.com/settings/tokens → revoke immediately.
2. Generate a fresh one per Step 3.
3. Re-register per Step 4.

### "I can't see Obsidian / GitHub tools in my session"

You haven't restarted Claude Code. The tool list is fixed at session start.

---

## Uninstall

```bash
claude mcp remove obsidian -s user
claude mcp remove github -s user
```

Then revoke your GitHub token at https://github.com/settings/tokens if you won't use it elsewhere. Optionally disable the Local REST API plugin in Obsidian.

---

## Why user scope, not project scope?

Both the Obsidian API key and the GitHub fine-grained token are **per-user** credentials. Committing a project-scoped `.mcp.json` to the repo would either leak each member's secrets or force everyone to share one credential — both unacceptable (the GitHub token in particular would erase audit trail since every commit would be authored by the token's owner). User scope keeps each credential in `~/.claude.json` on its owner's machine, while the skill itself ships via the repo and works for any member who completes this one-time setup.
