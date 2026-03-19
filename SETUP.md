# Workshop Setup Guide

> Get Claude Code + Databricks working in ~10 minutes. Mac and Windows instructions below.

---

## Step 1: Install Claude Code

[Full docs](https://code.claude.com/docs/en/setup)

**Requires:** A Claude Pro, Max, Teams, or Enterprise subscription.

**Mac:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

**Verify:**
```bash
claude --version
```

**Authenticate** — run `claude` and a browser opens for login. Sign in with your Claude account. Done.

---

## Step 2: Install Databricks CLI

[Full docs](https://docs.databricks.com/en/dev-tools/cli/install.html)

**Mac:**
```bash
brew tap databricks/tap
brew install databricks
```

**Windows (PowerShell):**
```powershell
winget install Databricks.DatabricksCLI
```

**Verify:**
```bash
databricks -v
```

---

## Step 3: Authenticate Databricks CLI (OAuth)

[Full docs](https://docs.databricks.com/en/dev-tools/auth/oauth-u2m.html)

Use OAuth — no tokens to manage, auto-refreshes.

```bash
databricks auth login --host https://YOUR-WORKSPACE.cloud.databricks.com
```

A browser opens. Log in to your Databricks account. That's it.

**With a named profile** (recommended if you have multiple workspaces):
```bash
databricks auth login --host https://YOUR-WORKSPACE.cloud.databricks.com --profile my-profile
```

**Verify:**
```bash
databricks clusters list
```

If you see your clusters, authentication is working.

---

## Step 4: Connect Claude Code to Databricks (MCP)

This lets Claude query your Unity Catalog tables, run SQL, and explore schemas — all through natural language.

### Option A: Databricks Managed MCP (simplest)

[Full docs](https://docs.databricks.com/en/generative-ai/mcp/managed-mcp.html)

Your workspace exposes MCP endpoints at `https://YOUR-WORKSPACE/api/2.0/mcp/sql`. Add it to Claude Code:

**Mac/Windows:**
```bash
claude mcp add uc-function-mcp \
  --transport http \
  --url https://YOUR-WORKSPACE.cloud.databricks.com/api/2.0/mcp/sql \
  --header "Authorization: Bearer $(databricks auth token --host https://YOUR-WORKSPACE.cloud.databricks.com | jq -r .access_token)"
```

> **Note:** The OAuth token auto-refreshes via the Databricks CLI. If the token expires during a long session, re-run the command above.

### Option B: Community MCP via uv (auto-refreshing auth)

[Full docs](https://github.com/databrickslabs/mcp)

This runs locally and automatically uses your Databricks CLI OAuth credentials — no token management.

**Install uv first:**

Mac: `brew install uv` | Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

**Then:**
```bash
claude mcp add databricks-uc \
  -- uv run --with unitycatalog-mcp unitycatalog-mcp \
  -s YOUR_CATALOG.YOUR_SCHEMA
```

Replace `YOUR_CATALOG.YOUR_SCHEMA` with your actual catalog and schema.

---

## Step 5: Add GitHub MCP (optional, for PR workflows)

```bash
claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

Set your GitHub token:
```bash
export GITHUB_TOKEN=ghp_your_token_here
```

---

## Step 6: Install Ruff (for auto-formatting hooks)

The demos auto-format Python files using [Ruff](https://docs.astral.sh/ruff/).

**Mac:**
```bash
brew install ruff
```

**Windows:**
```powershell
pip install ruff
```

**Verify:** `ruff --version`

---

## Verify Everything

```bash
# Claude Code
claude --version

# Databricks CLI
databricks -v

# Databricks auth
databricks clusters list

# MCP servers
claude mcp list

# End-to-end test — start Claude Code and ask:
claude
# Then type: "What MCP servers do you have access to?"
# Then type: "Show me tables in YOUR_CATALOG.YOUR_SCHEMA"
```

If Claude returns your table listing, you're ready for the workshop.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `claude: command not found` | Restart your terminal after installing |
| `databricks: command not found` | Restart terminal, or check `brew`/`winget` output |
| OAuth browser doesn't open | Copy the URL from the terminal and paste into browser manually |
| MCP shows "failed" | Re-run the `claude mcp add` command; check workspace URL |
| Token expired | Re-run `databricks auth login` to refresh |
| `uv: command not found` | Install uv: `brew install uv` (Mac) or see [uv docs](https://docs.astral.sh/uv/) |
| Permission denied on tables | Ask your workspace admin for Unity Catalog grants |

---

## What's Next?

Pick your demo track and follow the README:

- [Productivity Demo](demos/productivity/README.md) — no Databricks needed, best first demo
- [Data Engineering Demo](demos/data-engineering/README.md) — DABs + PySpark + DLT
- [Data Science Demo](demos/data-science/README.md) — MLflow + XGBoost
- [Software Engineering Demo (Node.js)](demos/software-engineering/README.md) — React + Express + Lakebase
- [Software Engineering Demo (Java)](demos/software-engineering-java/README.md) — Spring Boot + JUnit 5, no cloud
