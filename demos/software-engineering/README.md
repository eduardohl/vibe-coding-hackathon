# Demo: Software Engineering with Claude Code

> **35 min** | Databricks Apps + Lakebase + Node.js | [Full Claude Code Docs](https://code.claude.com/docs/en/overview)
>
> **Focus:** Testing, code quality tooling, and teaching Claude proprietary libraries

---

## Quick Reference — Prompts to Type

| Step | Prompt | Feature Shown |
|------|--------|---------------|
| 0 | `My catalog is {catalog}, schema is {schema}, CLI profile is {profile}. Remember this.` + `Setup demo data` | [Skills](https://code.claude.com/docs/en/skills) |
| 1 | `What MCP servers do you have? Show me the products table schema and 5 sample rows` | [MCP](https://code.claude.com/docs/en/mcp) |
| 2 | `Read the conversation in src/conversation.md and build the app they describe...` *(see below)* | Code gen + [Hooks](https://code.claude.com/docs/en/hooks) |
| 3 | `What do you know about SupplyTrackSDK?` + integrate it | [Skills](https://code.claude.com/docs/en/skills) (bundled docs) |
| 4 | `Write tests...` + `/run-tests` | Testing + [Skills](https://code.claude.com/docs/en/skills) |
| 5 | `Delegate to the code-reviewer and security-auditor agents in the background...` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 6 | `/deploy-app` | [Skills](https://code.claude.com/docs/en/skills) |
| 7 | `Open the deployed app in Chrome and test it for bugs` | [MCP](https://code.claude.com/docs/en/mcp) (Chrome DevTools) |
| 8 | `Commit and push these changes` / *Press `Esc` twice* | Git + [Checkpoints](https://code.claude.com/docs/en/overview) |

---

## Prerequisites

> **First time?** Follow the [Setup Guide](../../SETUP.md) to install Claude Code, Databricks CLI, and MCP.

1. Terminal open in `demos/software-engineering/`
2. `claude mcp list` — Databricks MCP server connected
3. Node.js 18+ installed (`node --version`)
4. Databricks workspace open in browser
5. Fresh session: start `claude`, then type `/clear`

---

## Walkthrough

### Step 0: Start + Setup Data

```bash
cd demos/software-engineering
claude .
```

Set your environment and create demo data:

```
My catalog is {catalog}, my schema is {schema}, and my Databricks CLI profile is {profile_name}. Only operate on this profile's workspace. Remember this for the rest of our session.
```

Then: `Setup demo data in my catalog and schema`

> **Observe:** Claude matched your intent to the skill's keywords. That's [Skills](https://code.claude.com/docs/en/skills). And it already knows the project context from [CLAUDE.md](https://code.claude.com/docs/en/memory).

---

### Step 1: Explore Live Data via MCP

```
What MCP servers do you have access to? Then show me the products table schema and 5 sample rows from {catalog}.{schema}.products
```

> **Observe:** Live tool connections to Databricks and more — no API code needed. That's your *live* workspace queried via [MCP](https://code.claude.com/docs/en/mcp).

---

### Step 2: Read Conversation & Scaffold the App

```
Read the conversation in src/conversation.md — Jordan and Priya are discussing an inventory tracker app. Build exactly what they describe:
- Create a Lakebase database for the app
- Express.js backend with plain HTML frontend (no React, no build step)
- Connects to Lakebase via PG* env vars (auto-set when Lakebase resource is bound)
- CRUD for supplies, low-stock badges, the works
- Use the products data from {catalog}.{schema}
Structure as src/generated-app/ with server.js, public/ folder, package.json, app.yaml, and databricks.yml. Don't deploy yet.
```

> **Observe:** (1) Claude reads a casual conversation and extracts real requirements from it — this is how natural language becomes working software. (2) Each `.js` file gets auto-formatted — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) firing Prettier on every write. (3) No build step — plain HTML means instant scaffolding.

---

### Step 3: Teach Claude a Proprietary Library

```
What do you know about SupplyTrackSDK?
```

> **Observe:** Claude reads the bundled docs from `.claude/skills/supply-track-sdk/` — a library it was **never trained on**. It can describe the API, methods, and error handling. This is how you teach Claude your internal libraries using [Skills with bundled documentation](https://code.claude.com/docs/en/skills).

Now integrate it:

```
Add a POST /api/supplies/:sku/reserve endpoint using SupplyTrackSDK to check stock and reserve items. Also add GET /api/warehouses/capacity. Mock the client since we don't have a real server.
```

> **Observe:** Claude writes code using the SDK's constructor pattern, method signatures, and error types — all learned from the bundled docs. **This is the key insight for proprietary codebases.**

---

### Step 4: Write & Run Tests

```
Write unit tests for the API route handlers — mock the database and the SDK client. Use Jest + supertest. Test both success and error paths. Then run them.
```

> **Observe:** Claude generates tests following CLAUDE.md patterns — mocked DB, mocked SDK, proper assertions. The hooks auto-format each test file. Then Claude runs `npm test` and fixes any failures.

---

### Step 5: Code Review & Security Audit (Background)

```
Delegate to the code-reviewer and security-auditor agents in the background. The code-reviewer should check quality, test coverage, and best practices. The security-auditor should check for OWASP vulnerabilities. While they run, continue with the next steps.
```

> **Observe:** Two [subagents](https://code.claude.com/docs/en/sub-agents) launch in the background — each with its own isolated context and specialized checklist. You don't have to wait. Claude keeps working while they run in parallel, and reports back when they finish. Each agent is a `.md` file with specialized instructions.

---

### Step 6: Deploy

```
/deploy-app
```

> **Observe:** The [Skill](https://code.claude.com/docs/en/skills) tests and deploys to Databricks Apps. No build step needed — plain HTML goes straight to production.

---

### Step 7: Automated UI Testing via Chrome

> **Prereq:** The presenter has connected a Chrome DevTools MCP server on the side. No setup needed from participants.

```
Open the deployed app in Chrome and test it for bugs. Click through every page, try the CRUD operations, and check the console for errors. Also check the Databricks Apps logs to verify everything is working on the backend. If you find any bugs, fix the app, redeploy, and update the tests.
```

> **Observe:** Claude autonomously navigates the app in Chrome — clicking buttons, filling forms, reading console logs, and reporting bugs. It's doing manual QA without a human. That's [MCP](https://code.claude.com/docs/en/mcp) connecting Claude to a real browser.

---

### Step 8: Commit & Checkpoints

```
Commit and push these changes
```

Then try something experimental:

```
Add a dark mode toggle to the app
```

Press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot before every edit. Roll back instantly. Bonus: `/compact` to summarize a long conversation.

---

> **Reflect with the group:** How does turning a casual conversation into a working app change your development process? How does teaching Claude a proprietary library change what's possible? What internal tools or SDKs would you bundle as skills?

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP not connecting | `claude mcp list`, verify token and workspace URL |
| `npm install` fails | Check Node.js version (`node --version`, need 18+) |
| App deploy fails | Verify `app.yaml` + `databricks.yml` in app root, check `databricks apps get {name}` |
| Lakebase connection error | Check Lakebase resource in `databricks.yml`, verify Lakebase project exists |
| Tests fail with module errors | Run `npm install` first, check `package.json` for missing deps |
| Prettier hook not firing | Verify `.claude/settings.json` exists and has PostToolUse hook |
| Chrome UI test not working | Ensure Chrome DevTools MCP is connected (`claude mcp list`) |

---

## Features Cheat Sheet

| Feature | What It Does | Where It Lives | Docs |
|---------|--------------|----------------|------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) | Project context, auto-loaded | `CLAUDE.md` | [Memory](https://code.claude.com/docs/en/memory) |
| [Skills](https://code.claude.com/docs/en/skills) | `/deploy-app`, `/run-tests`, SupplyTrackSDK docs, API testing | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Code reviewer, API debugger, security auditor | `.claude/agents/` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| [MCP](https://code.claude.com/docs/en/mcp) | Databricks, docs | Connected servers | [MCP](https://code.claude.com/docs/en/mcp) |
| [Hooks](https://code.claude.com/docs/en/hooks) | Auto-format JS/TS with Prettier, Python with Ruff | `.claude/settings.json` | [Hooks](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](https://code.claude.com/docs/en/overview) | `Esc+Esc` to rewind changes | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
