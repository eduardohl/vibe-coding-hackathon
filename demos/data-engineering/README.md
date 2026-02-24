# Demo: Data Engineering with Claude Code

> **45 min** | PySpark + DLT + Lakeflow Jobs | [Full Claude Code Docs](https://code.claude.com/docs/en/overview)

---

## Quick Reference — Prompts to Type

| Step | Prompt | Feature Shown |
|------|--------|---------------|
| 0 | `Setup demo data in {catalog}.{schema}` | [Skills](https://code.claude.com/docs/en/skills) |
| 1 | `What MCP servers do you have access to?` | [MCP](https://code.claude.com/docs/en/mcp) |
| 2 | `Using the Databricks MCP, show me what tables are in {catalog}.{schema}` | MCP (live query) |
| 3 | `Create TWO versions of an ETL pipeline...` *(see below)* | Code generation + [Hooks](https://code.claude.com/docs/en/hooks) |
| 4 | `Delegate to the spark-optimizer agent to review my PySpark code` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 5 | `Using context7, show me the Delta Lake documentation for MERGE` | MCP (docs lookup) |
| 6 | `Deploy this bundle and run the job` | CLI automation |
| 7 | `Remember that our target schema is {catalog}.{schema}` | [Memory](https://code.claude.com/docs/en/memory) |
| 8 | `Commit and push these changes` | Git workflow |
| 9 | *Press `Esc` twice* | [Checkpoints](https://code.claude.com/docs/en/overview) |

---

## Prerequisites

1. Terminal open in `demos/data-engineering/`
2. `claude mcp list` — all servers connected
3. Databricks workspace open in browser
4. Fresh session: start `claude`, then type `/clear`

---

## Walkthrough

### Step 0: Start Claude Code & Setup Demo Data

```bash
cd demos/data-engineering
claude .
```

> Skip the data setup below if you already created demo data for the other track.

```
Setup demo data in {catalog}.{schema}
```

This triggers the [setup-demo-data skill](https://code.claude.com/docs/en/skills) in `.claude/skills/`. It creates 5 tables with mock grocery data.

> **Observe:** Claude found and activated the skill automatically — you didn't have to tell it where the skill was. That's how skills work: Claude matches your intent to the skill's trigger keywords.

---

### Step 1: Verify MCP

```
What MCP servers do you have access to?
```

> **Observe:** Claude lists all connected [MCP servers](https://code.claude.com/docs/en/mcp). These give Claude live access to external tools — Databricks, GitHub, search engines, and more. No API code needed.

---

### Step 2: Explore Live Data

```
Using the Databricks MCP, show me what tables are in {catalog}.{schema}
```

Then:

```
Show me 5 sample rows from the orders table
```

> **Observe:** Claude is querying your *actual* Databricks workspace in real time. This isn't static data — it's a live SQL connection via the `uc-function-mcp` server.

---

### Step 3: Create TWO ETL Pipelines

This is the main event. Ask Claude to generate both approaches side by side:

```
Create TWO versions of an ETL pipeline that:
- Reads from {catalog}.{schema}.orders
- Aggregates daily order metrics by day of week and hour
- Writes to {catalog}.{schema}.daily_order_metrics

Create both:
1. A traditional PySpark batch job
2. A Delta Live Tables (DLT/SDP) pipeline

Use the project structure in this directory.
```

> **Observe:** Watch for two things:
> 1. Claude generates multiple files — source code and job definitions — in one shot
> 2. Each `.py` file gets **auto-formatted with Ruff** as it's written — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) in `.claude/settings.json` firing automatically

**Generated files:**

| Version | Source Code | Job Definition |
|---------|-------------|----------------|
| PySpark | `src/generated-etl_daily_metrics.py` | `resources/jobs/generated-daily_metrics_job.yml` |
| DLT/SDP | `src/generated-dlt_daily_metrics.py` | `resources/jobs/generated-daily_metrics_dlt.yml` |

---

### Step 4: Optimize with a Subagent

```
Delegate to the spark-optimizer agent to review my PySpark code for performance issues
```

> **Observe:** Claude delegates to a specialized [subagent](https://code.claude.com/docs/en/sub-agents) defined in `.claude/agents/spark-optimizer.md`. The subagent has its own isolated context and expertise. Notice how the recommendations are structured and prioritized — that's the agent's prompt at work.

---

### Step 5: Look Up Documentation

```
Using context7, show me the Delta Lake documentation for MERGE operations
```

> **Observe:** Context7 is an [MCP server](https://code.claude.com/docs/en/mcp) that fetches up-to-date library docs. Claude gets the *current* API reference, not stale training data.

---

### Step 6: Deploy and Run

```
Deploy this bundle and run the job
```

> **Note:** If no `databricks.yml` exists yet, Claude will create one as part of the deploy. You may need to specify your Databricks CLI profile (e.g., `default`).

> **Observe:** Claude runs `databricks bundle deploy` and `databricks bundle run` for you and returns the job run URL. Check the Databricks UI to see it running.

---

### Step 7: Persist Knowledge with Memory

```
Remember that our target schema is {catalog}.{schema} and the orders table has 10K rows
```

> **Observe:** The [Memory MCP](https://code.claude.com/docs/en/memory) persists facts across sessions. Next time you start Claude Code, ask "What do you remember about this project?" and it will recall this.

---

### Step 8: Commit and Push

```
Commit and push these changes
```

> **Observe:** Claude stages the right files, writes a meaningful commit message, and pushes. It understands git context from the diff, not just file names.

---

### Step 9: Safe Experimentation with Checkpoints

```
Let me try adding a gold layer aggregation to the DLT pipeline
```

After Claude makes changes, press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot your files before every edit. You can roll back instantly without touching git. Try it — rewind, then try a different approach.

**Bonus — compact a long conversation:**

```
/compact
```

---

## Bonus Prompts

Try these if you have extra time:

```
What tables are available in {catalog}.{schema}?
What's the distribution of orders by day of week?
Search for best practices for PySpark partition pruning
Create a GitHub issue for "Add data quality checks to pipeline"
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP not connecting | `claude mcp list`, verify token and URL |
| Bundle deploy fails | Run `databricks bundle validate` first |
| Permission denied | Check Unity Catalog grants |
| Job timeout | Increase cluster size or reduce data scope |

---

## Features Cheat Sheet

| Feature | What It Does | Where It Lives | Docs |
|---------|--------------|----------------|------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) | Project context, auto-loaded | `CLAUDE.md` | [Memory](https://code.claude.com/docs/en/memory) |
| [Slash Commands](https://code.claude.com/docs/en/slash-commands) | `/deploy`, `/run-job`, `/validate-data` | `.claude/commands/` | [Commands](https://code.claude.com/docs/en/slash-commands) |
| [Skills](https://code.claude.com/docs/en/skills) | Auto-triggered (data quality, optimization) | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Spark optimizer, job debugger, code reviewer | `.claude/agents/` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| [MCP](https://code.claude.com/docs/en/mcp) | Databricks, GitHub, search, docs | Connected servers | [MCP](https://code.claude.com/docs/en/mcp) |
| [Hooks](https://code.claude.com/docs/en/hooks) | Auto-format Python with Ruff | `.claude/settings.json` | [Hooks](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](https://code.claude.com/docs/en/overview) | `Esc+Esc` to rewind changes | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
