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

Click path in GitHub:

1. **GitHub user settings → Developer Settings → Personal Access Tokens → Fine-Grained Tokens → Generate New Token**
2. **Token name:** `DS-Brain` (or whatever you want).
3. **Resource Owner:** `cybereason-labs`.
4. **Expiration:** `366 days`.
5. **Repository access →** change to `Only select repositories` → choose `ds-brain`.
6. **Permissions → Add permissions → select `Contents` →** change Contents access to `Read and Write`. (GitHub auto-adds `Metadata: Read-only`.)
7. Click **Generate token**. **Copy it once** — GitHub won't display it again. Save it to your password manager.

Optional: also add **Pull requests: Read and write** if you plan to have the skill open PRs for INBOX entries instead of direct commits.

### Step 1a — Wait for IT / org approval

Because `cybereason-labs` is an organization with fine-grained PAT approval enabled, generating the token does **not** grant access immediately. After clicking **Generate token** you will see a banner like:

> *Your fine-grained personal access token has been created and is pending approval by the organization owners.*

The token string is real and copy-able, but every API call will return `403 Forbidden — pending approval` until an org admin / IT approves the request.

What to do:

1. After clicking **Generate token**, GitHub auto-files a request to org admins.
2. Notify IT / your team's GitHub admin out-of-band (Slack, email) that a `DS-Brain` fine-grained PAT request is pending for `cybereason-labs`. Include the token name and your GitHub handle so they can find it under **Organization settings → Personal access tokens → Pending requests**.
3. **Wait for approval.** You will get an email from GitHub: *"Your personal access token request has been approved"*. Until that email arrives, do **not** continue to Step 2 — the MCP will register fine but every read/write will fail with `403`.
4. If denied, the email will explain why; iterate with IT and regenerate (or request approval of the same token again from the **Pending requests** UI).

You can check status any time at **GitHub user settings → Developer Settings → Personal Access Tokens → Fine-Grained Tokens → `DS-Brain`** — the row shows `Pending` / `Active` / `Denied`.

## Step 2 — Register the GitHub MCP

> **Do not start this step until your token shows `Active` in the GitHub UI and you have received the approval email from GitHub.** Registering with a `Pending` token wastes time — `claude mcp list` may show `✓ Connected` (the MCP server itself starts) but every brain operation will fail with `403`.


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

Three possible causes — check in order:

1. **PAT still pending org approval.** Most common right after onboarding. Fine-grained PATs against `cybereason-labs` require approval from an org admin / IT. Check status at **GitHub user settings → Developer Settings → Personal Access Tokens → Fine-Grained Tokens → `DS-Brain`**:
   - `Pending` → IT hasn't approved yet. Ping IT / your team's GitHub admin. The token will not work until status flips to `Active` (you'll also receive an email: *"Your personal access token request has been approved"*).
   - `Denied` → re-request approval from the **Pending requests** page or regenerate with adjusted scope.
   - `Active` → move on to the next cause.
2. **Wrong scope.** Token lacks `Contents: Read and write` on `cybereason-labs/ds-brain`. Fix per Step 1.
3. **Not a collaborator.** You aren't a member / outside collaborator on `cybereason-labs/ds-brain`. Ask the maintainer to add you.

Also: a read that worked yesterday but suddenly returns `403` today usually means the token's approval was revoked, expiration hit, or org policy changed. Check the Fine-Grained Tokens UI before regenerating.

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
