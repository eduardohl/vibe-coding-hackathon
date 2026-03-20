# Software Engineering Demo — Testing, Quality & Proprietary Libraries

## Overview

Build a **Supply Chain Inventory** app using Express.js + Lakebase with a plain HTML frontend, then teach Claude a proprietary SDK it was never trained on.

**Origin:** The app spec comes from a casual Slack conversation in `src/conversation.md` — read it first to understand the requirements.
**Stack:** Plain HTML/CSS/JS frontend + Express.js backend + Lakebase database
**Deployment:** Databricks Apps

**This demo showcases Claude Code features including:**
- Custom skills (`/deploy-app`, `/run-tests`, `/lint`, `/create-pr`)
- Skills with bundled documentation (SupplyTrackSDK)
- Auto-triggered skills (API testing, demo data setup)
- Specialized subagents (code reviewer, security auditor, API debugger)
- Hooks for automatic code formatting (Prettier + ESLint)
- MCP integrations (Databricks via uc-function-mcp, Context7, Memory)

## Rules

- **ONLY use local skills** from this project's `.claude/skills/` directory — do NOT use `fe-databricks-tools`, `fe-workflows`, or any other external plugin skills. This demo must be self-contained.
- ALWAYS check `.claude/skills/` directory before implementing any task manually
- When user mentions "setup demo data" or "test api", use the corresponding skill
- Read the skill file and follow its instructions exactly before writing any code
- **IMPORTANT:** When creating new files, use the `generated-` prefix inside `src/` (e.g., `src/generated-app/`)
- **CRITICAL — Databricks CLI:** Always pass `-p {profile}` on every `databricks` command. The user sets their profile at the start of the session. Never use the default profile — it may point to a different workspace.
- **SDK DEFERRAL:** When scaffolding the app from the conversation, do NOT include SupplyTrackSDK integration. Only build the basic CRUD app with low-stock badges. The SDK (reserve endpoint, warehouse capacity) is added in a later step when the user explicitly asks.

## Environment

### Databricks Workspace

- Unity Catalog enabled, Databricks Apps enabled, Lakebase available
- **Catalog:** `{catalog}` — Replace with your catalog
- **Schema:** `{schema}` — Replace with your schema

> **First time?** Run "setup demo data in {catalog}.{schema}" to create the tables.

### Key Tables

| Table | Description | Row Count |
|-------|-------------|-----------|
| `{catalog}.{schema}.products` | Product catalog | 50 |
| `{catalog}.{schema}.orders` | Order transactions | 10,000 |
| `{catalog}.{schema}.order_products` | Order line items | ~35,000 |
| `{catalog}.{schema}.departments` | Product departments | 21 |
| `{catalog}.{schema}.aisles` | Product aisles | 100 |

## Claude Code Features

### Custom Skills

| Skill | Triggers On |
|-------|-------------|
| `/deploy-app` | User invokes `/deploy-app` |
| `/run-tests` | User invokes `/run-tests` |
| `/lint` | User invokes `/lint` |
| `/create-pr` | User invokes `/create-pr` |
| `api-testing` | "test api", "test endpoint", "integration test" |
| `setup-demo-data` | "setup demo data", "create mock data" |
| `supply-track-sdk` | "SupplyTrackSDK", "supply track", "warehouse SDK" |

### Subagents (Specialists)

| Agent | Purpose |
|-------|---------|
| `code-reviewer` | Review code for quality, testing, and best practices |
| `api-debugger` | Debug API endpoints and database connectivity |
| `security-auditor` | Audit code for OWASP vulnerabilities |

### Hooks (Automation)

| Hook | Trigger | Action |
|------|---------|--------|
| PostToolUse:Write | After writing .js/.ts/.jsx/.tsx files | Auto-format with Prettier + ESLint |
| PostToolUse:Write | After writing .py files | Auto-format with Ruff |

### MCP Integrations

Verify with `claude mcp list`. See `.claude/mcp-config.example.json` for setup.

**Required:**

| Server | Capabilities |
|--------|-------------|
| **uc-function-mcp** | Query Databricks tables via SQL, explore schemas |

**Optional (nice-to-have):**

| Server | Capabilities |
|--------|-------------|
| **confluence** | Read/write Confluence pages for documentation |
| **context7** | Get up-to-date library documentation |
| **brave-search** | Search for best practices |
| **memory** | Persist facts across sessions |
| **obsidian** | Document architecture, write notes and summaries |

## SupplyTrackSDK

A fictional proprietary SDK for real-time warehouse inventory operations. Claude has **never seen this library** — it learns it from the bundled docs in `.claude/skills/supply-track-sdk/`.

**Demo flow:**
1. Ask: "What do you know about SupplyTrackSDK?" — Claude reads the bundled docs
2. Ask Claude to add an inventory endpoint using the SDK — it writes correct code

See `.claude/skills/supply-track-sdk/api-reference.md` for the full API.

## Lakebase (Database)

The app uses Lakebase (Postgres-compatible) for persistence. Lakebase is configured as a resource in `databricks.yml` (DABs), and the platform auto-sets `PG*` environment variables (`PGHOST`, `PGPORT`, `PGDATABASE`, `PGSSLMODE`, `PGUSER`).

**Create a Lakebase project before deploying:**
```bash
databricks api post '/api/2.0/postgres/projects?project_id={app_name}' \
  -p {profile} --json '{"display_name": "{app_name}"}'
```

> **Note:** The CLI does not have a `lakebase` subcommand. Use the REST API via `databricks api post` as shown above.

**app.yaml** (only `command` and `env` are valid fields — NO `resources` block):
```yaml
command:
  - node
  - server.js
env:
  - name: DATABASE_URL
    valueFrom: lakebase-db
```

**databricks.yml** (Lakebase resource binding goes here, not in app.yaml):
```yaml
bundle:
  name: {app_name}

resources:
  apps:
    app:
      name: {app_name}
      description: "Supply Chain Inventory Management"
      source_code_path: .
      resources:
        - name: lakebase-db
          postgres:
            branch: projects/{app_name}/branches/production
            database: databricks_postgres
            permission: CAN_CONNECT_AND_CREATE

targets:
  dev:
    default: true
```

**Dependency installation:** The platform auto-runs `npm install` when it detects `package.json`. Do NOT put `npm install` in the command. Do NOT upload `node_modules/`.

**Lakebase authentication in server.js:** The platform sets `PG*` vars but the password requires an OAuth token. Use the Databricks service principal credentials:
```javascript
import pg from 'pg';
const { Pool } = pg;

// DATABRICKS_HOST may or may not include https:// — always normalize
const dbHost = process.env.DATABRICKS_HOST?.startsWith('http')
  ? process.env.DATABRICKS_HOST
  : `https://${process.env.DATABRICKS_HOST}`;

const pool = new Pool({
  // PGHOST, PGPORT, PGDATABASE, PGSSLMODE, PGUSER are auto-set by the platform
  password: async () => {
    const res = await fetch(`${dbHost}/oidc/v1/token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: process.env.DATABRICKS_CLIENT_ID,
        client_secret: process.env.DATABRICKS_CLIENT_SECRET,
        scope: 'all-apis',
      }),
    });
    const { access_token } = await res.json();
    return access_token;
  },
  ssl: { rejectUnauthorized: false },
  // Lakebase restricts CREATE on the public schema — use a dedicated schema
  options: '-c search_path=inventory,public',
});
```

**Lakebase schema setup:** Lakebase does NOT allow `CREATE TABLE` on the default `public` schema. The app must create a dedicated schema on startup:
```javascript
let dbReady = false;
async function initDb() {
  await pool.query('CREATE SCHEMA IF NOT EXISTS inventory');
  await pool.query('CREATE TABLE IF NOT EXISTS inventory.supplies (...)');
  // ... seed data if empty
  dbReady = true;
}

// Lazy init middleware — retries DB setup on first API request if startup init fails
app.use('/api', async (req, res, next) => {
  if (req.path === '/health') return next();
  if (!dbReady) {
    try { await initDb(); }
    catch (err) { return res.status(503).json({ error: 'Database not ready: ' + err.message }); }
  }
  next();
});
```

## Coding Standards

- ES modules (`import`/`export`), `const`/`let` only, async/await
- **Plain HTML/CSS/JS frontend** — no React, no build step, no JSX
- Express serves static files from a `public/` directory
- Express middleware for cross-cutting concerns, validate all inputs
- Parameterize all SQL queries — never concatenate user input
- Use environment variables for secrets
- Test both success and error paths with descriptive names

### Architecture (follow these to avoid common issues)

- Add `helmet` middleware for security headers
- Add `cors` middleware with explicit origin (not wildcard `*`)
- Add `GET /api/health` endpoint that checks DB connectivity
- Validate all request bodies with explicit checks (type, required fields, length)
- Wrap async handlers in try/catch
- **NEVER use `window.confirm()`, `window.alert()`, or `window.prompt()`** in the frontend — these browser dialogs block Chrome DevTools MCP during UI testing. Use custom HTML modals instead (a simple `<div>` overlay with confirm/cancel buttons)
- Include a `.gitignore` in the app root (exclude `node_modules/`, `.env`, `.bundle/`)
- **No build step** — the app runs directly with `node server.js`
- **Port:** The Express server MUST listen on `process.env.PORT || 8000` and bind to `0.0.0.0` — Databricks Apps injects the `PORT` env var at runtime
- **Dependencies:** The platform auto-runs `npm install` from `package.json` during deployment. Do NOT upload `node_modules/` or put `npm install` in the app.yaml command

### App Structure (keep it minimal)

```
src/generated-app/
├── server.js           # Express server + API routes (single file)
├── public/             # Static frontend (served by Express)
│   ├── index.html      # Single page — table, form, status bar
│   └── style.css       # Simple clean CSS
├── package.json        # express, pg, helmet, cors (minimal deps)
├── app.yaml            # Databricks Apps runtime config (command + env only)
├── databricks.yml      # DABs bundle config (app resource + Lakebase binding)
└── .gitignore          # Exclude node_modules, .env, .bundle
```

**Key:** The entire app is ~3 files of logic (server.js, index.html, style.css). No bundler, no transpiler, no framework. This keeps scaffolding fast and deployment simple.

## File Structure

```
├── CLAUDE.md                    # This file
├── README.md                    # Demo script
├── .gitignore                   # Ignores generated files
├── .claude/
│   ├── settings.json            # Hooks and permissions
│   ├── mcp-config.example.json  # MCP server reference
│   ├── agents/                  # Specialized subagents
│   │   ├── code-reviewer.md
│   │   ├── api-debugger.md
│   │   └── security-auditor.md
│   └── skills/
│       ├── deploy-app/SKILL.md
│       ├── run-tests/SKILL.md
│       ├── lint/SKILL.md
│       ├── create-pr/SKILL.md
│       ├── api-testing/SKILL.md
│       ├── setup-demo-data/SKILL.md
│       └── supply-track-sdk/    # Proprietary SDK docs
│           ├── SKILL.md
│           ├── api-reference.md
│           └── examples.md
└── src/
    ├── conversation.md          # App spec (casual Slack conversation)
    ├── setup_demo_data.py
    └── generated-*/             # Created during demo
```
