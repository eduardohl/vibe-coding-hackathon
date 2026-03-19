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

| Server | Capabilities |
|--------|-------------|
| **uc-function-mcp** | Query Databricks tables via SQL |
| **context7** | Library documentation (optional) |
| **memory** | Persist facts across sessions (optional) |

## SupplyTrackSDK

A fictional proprietary SDK for real-time warehouse inventory operations. Claude has **never seen this library** — it learns it from the bundled docs in `.claude/skills/supply-track-sdk/`.

**Demo flow:**
1. Ask: "What do you know about SupplyTrackSDK?" — Claude reads the bundled docs
2. Ask Claude to add an inventory endpoint using the SDK — it writes correct code

See `.claude/skills/supply-track-sdk/api-reference.md` for the full API.

## Coding Standards

- ES modules (`import`/`export`), `const`/`let` only, async/await
- Functional React components with hooks
- Express middleware for cross-cutting concerns, validate all inputs
- Parameterize all SQL queries — never concatenate user input
- Use environment variables for secrets
- Test both success and error paths with descriptive names

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
