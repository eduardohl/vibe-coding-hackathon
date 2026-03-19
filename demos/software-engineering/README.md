# Demo: Software Engineering with Claude Code

> **45 min** | Databricks Apps + Lakebase + Node.js/React | [Full Claude Code Docs](https://code.claude.com/docs/en/overview)
>
> **Focus:** Testing, code quality tooling, and teaching Claude proprietary libraries

---

## Quick Reference — Prompts to Type

| Step | Prompt | Feature Shown |
|------|--------|---------------|
| 0 | `My catalog is {catalog}, schema is {schema}, CLI profile is {profile}` + `Setup demo data` | [Skills](https://code.claude.com/docs/en/skills) |
| 1 | `What MCP servers do you have? Show me the products table schema and 5 sample rows` | [MCP](https://code.claude.com/docs/en/mcp) |
| 2 | `Create a Databricks App with React frontend and Express backend...` *(see below)* | Code gen + [Hooks](https://code.claude.com/docs/en/hooks) |
| 3 | `What do you know about SupplyTrackSDK?` | [Skills](https://code.claude.com/docs/en/skills) (bundled docs) |
| 4 | `Write unit tests for the API routes and React components, including the SDK integration` | Testing + [Hooks](https://code.claude.com/docs/en/hooks) |
| 5 | `/run-tests` | [Skills](https://code.claude.com/docs/en/skills) |
| 6 | `Delegate to the code-reviewer agent to review my code` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 7 | `Delegate to the security-auditor agent to check for vulnerabilities` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 8 | `/deploy-app` | [Skills](https://code.claude.com/docs/en/skills) |
| 9 | `Commit and push these changes` / *Press `Esc` twice* | Git + [Checkpoints](https://code.claude.com/docs/en/overview) |
| 10 | `Open the deployed app in Chrome and test it for bugs` | [MCP](https://code.claude.com/docs/en/mcp) (Chrome DevTools) |

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
My catalog is {catalog} and my schema is {schema}. Remember this for the rest of our session.
My Databricks CLI profile is {profile_name}. Only operate on this profile's workspace.
```

```
Setup demo data in my catalog and schema
```

> **Observe:** Claude matched your intent to the skill's keywords. That's [Skills](https://code.claude.com/docs/en/skills). And it already knows the project context from [CLAUDE.md](https://code.claude.com/docs/en/memory).

---

### Step 1: Explore Live Data via MCP

```
What MCP servers do you have access to? Then show me the products table schema and 5 sample rows from {catalog}.{schema}.products
```

> **Observe:** Live tool connections to Databricks and more — no API code needed. That's your *live* workspace queried via [MCP](https://code.claude.com/docs/en/mcp).

---

### Step 2: Scaffold the App

```
Create a Databricks App for supply chain inventory management with a React frontend and Express.js backend:
- Connects to Lakebase for persistence
- CRUD for medical supplies (list, view, add, edit, delete) with SKU, stock level, reorder point
- Simple order analytics dashboard
- app.yaml for Databricks Apps deployment
- Uses the products and departments from {catalog}.{schema}

Structure as generated-app/ with server.js, src/ (React + Vite), package.json, and app.yaml.
Don't deploy yet.
```

> **Observe:** (1) Full-stack app generated in one shot. (2) Each `.js`/`.jsx` file gets auto-formatted — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) firing Prettier on every write.

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

### Step 4: Write Tests

```
Write tests for the app:
1. Unit tests for the API route handlers (mock the database)
2. Tests for the SupplyTrackSDK integration endpoints (mock the SDK client)
3. A simple React component test for the product list
Use Jest. Test both success and error paths.
```

> **Observe:** Claude generates tests following CLAUDE.md patterns — mocked DB, mocked SDK, proper assertions. The hooks auto-format each test file.

---

### Step 5: Run the Tests

```
/run-tests
```

> **Observe:** The [Skill](https://code.claude.com/docs/en/skills) runs `npm test`, checks coverage, and reports results. You typed `/run-tests` instead of explaining what to do.

---

### Step 6: Code Review with a Subagent

```
Delegate to the code-reviewer agent to review my code for quality, test coverage, and best practices
```

> **Observe:** A [subagent](https://code.claude.com/docs/en/sub-agents) with its own isolated context and specialized checklist. It reviews code quality, testing patterns, and error handling. Do you agree with the findings?

---

### Step 7: Security Audit with a Subagent

```
Delegate to the security-auditor agent to check my API for OWASP vulnerabilities
```

> **Observe:** Another [subagent](https://code.claude.com/docs/en/sub-agents) — checks for SQL injection, XSS, missing input validation, and error leakage. Each agent is a `.md` file with specialized instructions. What would you add?

---

### Step 8: Deploy

```
/deploy-app
```

> **Observe:** The [Skill](https://code.claude.com/docs/en/skills) builds, tests, and deploys to Databricks Apps.

---

### Step 9: Commit & Checkpoints

```
Commit and push these changes
```

Then try something experimental:

```
Add a dark mode toggle to the React app
```

Press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot before every edit. Roll back instantly. Bonus: `/compact` to summarize a long conversation.

---

### Step 10: Automated UI Testing via Chrome

> **Prereq:** The presenter has connected a Chrome DevTools MCP server on the side. No setup needed from participants.

```
Open the deployed app in Chrome and test it for bugs. Click through every page, try the CRUD operations, and check the console for errors.
```

> **Observe:** Claude autonomously navigates the app in Chrome — clicking buttons, filling forms, reading console logs, and reporting bugs. It's doing manual QA without a human. That's [MCP](https://code.claude.com/docs/en/mcp) connecting Claude to a real browser.

---

> **Reflect with the group:** How does teaching Claude a proprietary library change what's possible? What internal tools or SDKs would you bundle as skills? How do subagents compare to your current code review process?

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
