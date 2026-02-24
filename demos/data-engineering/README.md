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
| 6 | `/deploy` then `/run-job` | [Slash Commands](https://code.claude.com/docs/en/slash-commands) |
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

> **Observe:** You didn't point to any file — Claude matched your intent to the skill's keywords automatically. That's [Skills](https://code.claude.com/docs/en/skills).

---

### Step 1: Verify MCP

```
What MCP servers do you have access to?
```

> **Observe:** These are live tool connections — Databricks, GitHub, docs, and more. No API code needed.

---

### Step 2: Explore Live Data

```
Using the Databricks MCP, show me what tables are in {catalog}.{schema}
```

Then:

```
Show me 5 sample rows from the orders table
```

> **Observe:** That's your *actual* Databricks workspace, queried in real time via MCP.

**Try your own:** Ask Claude anything — "What's the busiest hour?" "Any null values in orders?"

---

### Step 3: Create TWO ETL Pipelines

This is the main event:

```
Create TWO versions of an ETL pipeline that:
- Reads from {catalog}.{schema}.orders
- Aggregates daily order metrics by day of week and hour
- Writes to {catalog}.{schema}.daily_order_metrics

Create both:
1. A traditional PySpark batch job
2. A Delta Live Tables (DLT/SDP) pipeline

Include a databricks.yml bundle config so we can deploy this.
Use the project structure in this directory.
```

> **Observe:** (1) Multiple files generated in one shot, and (2) each `.py` gets auto-formatted — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) firing Ruff on every write. How many files did Claude create? Can you spot the Ruff formatting in the terminal?

**Expected files:**

| File | Purpose |
|------|---------|
| `databricks.yml` | DABs bundle config (needed for deploy) |
| `src/generated-etl_daily_metrics.py` | PySpark batch job |
| `src/generated-dlt_daily_metrics.py` | DLT pipeline |
| `resources/jobs/generated-daily_metrics_job.yml` | PySpark job definition |
| `resources/jobs/generated-daily_metrics_dlt.yml` | DLT job definition |

---

### Step 4: Optimize with a Subagent

```
Delegate to the spark-optimizer agent to review my PySpark code for performance issues
```

> **Observe:** Claude delegates to a [subagent](https://code.claude.com/docs/en/sub-agents) with its own isolated context. Notice how the recommendations are structured — that's the agent's prompt at work. Do you agree with them? What would you add?

---

### Step 5: Look Up Documentation

```
Using context7, show me the Delta Lake documentation for MERGE operations
```

> **Observe:** Context7 fetches *current* library docs via [MCP](https://code.claude.com/docs/en/mcp) — not stale training data.

---

### Step 6: Deploy and Run

Now use the slash commands we built for this:

```
/deploy
```

> You may need to specify your Databricks CLI profile (e.g., `default`).

Then:

```
/run-job
```

> **Observe:** These are [Slash Commands](https://code.claude.com/docs/en/slash-commands) — pre-written prompts in `.claude/commands/`. You typed `/deploy` instead of explaining what to do. Claude followed the instructions in `deploy.md` automatically.

**While it runs:** Open the Databricks UI — can everyone find the running job?

---

### Step 7: Persist Knowledge with Memory

```
Remember that our target schema is {catalog}.{schema} and the orders table has 10K rows
```

> **Observe:** [Memory](https://code.claude.com/docs/en/memory) persists across sessions. Next time, ask "What do you remember?" and Claude recalls it.

---

### Step 8: Commit and Push

```
Commit and push these changes
```

> **Observe:** Claude stages the right files, writes a meaningful commit message, and pushes — it reads context from the diff.

---

### Step 9: Safe Experimentation with Checkpoints

```
Let me try adding a gold layer aggregation to the DLT pipeline
```

After Claude makes changes, press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot your files before every edit. Roll back instantly without touching git.

**Try it:** Rewind, then try a different approach.

**Bonus — compact a long conversation:**

```
/compact
```

---

> **Reflect with the group:** What surprised you most? What would you try first in your own workflow?

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
