# Software Engineering Demo — Testing, Quality & Proprietary Libraries

## Overview

Build a **Supply Chain Inventory** app using React + Express.js + Lakebase, then teach Claude a proprietary SDK it was never trained on.

**Problem:** Build a Medical Supply Inventory Management App
**Stack:** React frontend + Express.js backend + Lakebase database
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
- **IMPORTANT:** When creating new files, use the `generated-` prefix (e.g., `generated-app/`)
- **CRITICAL — Databricks CLI:** Always pass `-p {profile}` on every `databricks` command. The user sets their profile at the start of the session. Never use the default profile — it may point to a different workspace.

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

The app uses Lakebase (Postgres-compatible) for persistence. It's configured as a resource in `app.yaml` and the connection string is injected via environment variable.

**Create a Lakebase database before deploying:**
```bash
databricks lakebase databases create {db_name} -p {profile}
```

**app.yaml resource binding:**
```yaml
resources:
  - name: lakebase-db
    type: lakebase
    config:
      database: {db_name}
env:
  - name: DATABASE_URL
    valueFrom: lakebase-db
```

The app should read `DATABASE_URL` from the environment and connect with `pg` (node-postgres). Tables are created automatically on first startup (CREATE TABLE IF NOT EXISTS).

## Coding Standards

- ES modules (`import`/`export`), `const`/`let` only, async/await
- Functional React components with hooks
- Express middleware for cross-cutting concerns, validate all inputs
- Parameterize all SQL queries — never concatenate user input
- Use environment variables for secrets
- Test both success and error paths with descriptive names

### Architecture (follow these to avoid common issues)

- Add `helmet` middleware for security headers
- Add `cors` middleware with explicit origin (not wildcard `*`)
- Add `GET /api/health` endpoint that checks DB connectivity
- Add `morgan` or `pino` for request logging
- Validate all request bodies with explicit checks (type, required fields, length)
- Use `express-async-errors` or wrap async handlers in try/catch
- Include a `.databricksignore` in the app root (exclude `node_modules/`, `.git/`, `src/`, `__tests__/`)
- Include a `.gitignore` in the app root (exclude `node_modules/`, `dist/`, `.env`)

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
    ├── setup_demo_data.py
    └── generated-*/             # Created during demo
```
