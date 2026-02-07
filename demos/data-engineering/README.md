# Demo: Claude Code + PySpark & SDP + Lakeflow Jobs

## Overview

**Duration:** 45 minutes
**Track:** Data Engineering - Job Orchestration & CI/CD
**Audience:** Data Engineers, Platform Engineers

## Demo Objectives

By the end of this demo, participants will see how Claude Code can:
1. Scaffold a complete DABs (Databricks Asset Bundles) project
2. Help right-size clusters based on workload
3. **Create TWO versions of the same ETL pipeline:**
   - **Traditional PySpark job** (batch processing with Lakeflow Jobs)
   - **Delta Live Tables (DLT/SDP) pipeline** (declarative, streaming-ready)
4. Optimize Spark jobs for performance
5. Diagnose and fix job failures
6. Create PRs via **GitHub MCP**
7. Query live data via **Databricks MCP (uc-function-mcp)**

---

## Getting Started

### Prerequisites

1. Open terminal in `demos/data-engineering/` directory
2. Run `claude mcp list` to verify all MCPs are connected
3. Have Databricks workspace open in browser
4. Clear any previous Claude Code sessions: `claude /clear`

### Features You'll Use

| Feature | When It Appears |
|---------|-----------------|
| **Hooks** | Step 4 (auto-format on file write), Step 9 (bundle validate on commit) |
| **Subagents** | Step 5 (spark-optimizer), Step 9 (code-reviewer), Part 7 (job-debugger) |
| **MCP** | Steps 2-3 (Databricks), Step 6 (Context7), Step 8 (Memory), Step 9 (GitHub) |

---

## Step-by-Step Guide

### Step 0: Setup Demo Data (if needed)

If you don't have sample data yet, create it:

**Option A - Via Claude (Recommended):**

```
Setup demo data in {catalog}.{schema}
```

Replace `{catalog}.{schema}` with your target location (e.g., `users.my_name`).

This creates 5 tables (departments, aisles, products, orders, order_products) with mock grocery data.

**Note:** This data is shared with the Data Science demo - set it up once and use the same catalog.schema for both.

**Option B - Via Databricks:**

1. Upload `src/setup_demo_data.py` to Databricks workspace
2. Run the notebook with your target catalog/schema
3. Update CLAUDE.md with the correct catalog/schema

### Step 1: Start Claude Code

```bash
cd demos/data-engineering
claude .
```

### Step 2: Verify MCP Connection

```
What MCP servers do you have access to?
```

Claude will list connected servers (github, uc-function-mcp, brave-search, etc.).

### Step 3: Explore Data with Databricks MCP

```
Using the Databricks MCP, show me what tables are in {catalog}.{schema}
```

Then explore the data:

```
Show me 5 sample rows from the orders table
```

Claude queries your live Databricks workspace via the MCP connection.

### Step 4: Create TWO ETL Job Versions

Ask Claude to create both versions in parallel:

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

**Generated files:**

| Version | Source Code | Job Definition |
|---------|-------------|----------------|
| PySpark | `src/generated-etl_daily_metrics.py` | `resources/jobs/generated-daily_metrics_job.yml` |
| DLT/SDP | `src/generated-dlt_daily_metrics.py` | `resources/jobs/generated-daily_metrics_dlt.yml` |

> **Hooks in action:** When Claude writes .py files, they get auto-formatted with Ruff via the PostToolUse hook in `.claude/settings.json`.

### Step 5: Use Spark Optimizer Subagent

```
Delegate to the spark-optimizer agent to review my PySpark code for performance issues
```

The spark-optimizer subagent will:

- Analyze shuffle operations
- Check for partition skew
- Suggest broadcast joins for small tables
- Recommend caching strategies

### Step 6: Look Up Documentation with Context7

```
Using context7, show me the Delta Lake documentation for MERGE operations
```

Context7 provides up-to-date documentation from official sources.

### Step 7: Deploy and Run

```
Deploy this bundle to {profile_name} and run the job
```

Replace `{profile_name}` with your Databricks CLI profile (e.g., `default`).

Claude will:
1. Deploy the bundle using `databricks bundle deploy --profile {profile_name}`
2. Run the job using `databricks bundle run --profile {profile_name}`
3. Return the job run URL

Check the Databricks UI to see the job running.

### Step 8: Save to Memory

```
Remember that our target schema is {catalog}.{schema} and the orders table has 10K rows
```

The memory MCP persists information across sessions - useful for long-running projects.

### Step 9: Commit and Push

```
Commit and push these changes
```

Claude will stage, commit, and push to the remote repository.

### Step 10: Try Claude Code Features

**Checkpoints - safe experimentation:**

```
Let me try adding a gold layer aggregation to the DLT pipeline
```

After Claude makes changes, press `Esc` twice to show the checkpoint menu. You can roll back if needed.

**Compact - summarize long conversations:**

```
/compact
```

---

## Summary

By following this guide, you will have:

- Queried live Databricks data
- Created TWO complete ETL pipelines (PySpark AND DLT) in parallel
- Used subagents for optimization and code review
- Deployed and ran both versions
- Created a PR

---

## Bonus: Example Prompts

### Databricks SQL (uc-function-mcp)

```
What tables are available in {catalog}.{schema}?
Show me a sample of 5 rows from the orders table
What's the distribution of orders by day of week?
```

### Context7 - Documentation Lookup

```
Using context7, show me the latest Delta Lake MERGE syntax
What's the recommended way to handle SCD Type 2 in Delta Lake?
```

### Brave Search - Research

```
Search for best practices for PySpark partition pruning
Find recent articles about Databricks Photon optimization
```

### Memory - Persist Learnings

```
Remember that the orders table has 10K rows
What do you remember about this project?
```

### GitHub - Version Control

```
Create a GitHub issue for "Add data quality checks to pipeline"
Create a PR for my changes with experiment results in the description
```

---

## Files in This Demo

```
demos/data-engineering/
├── README.md                    # This file
├── CLAUDE.md                    # Project context for Claude
├── databricks.yml               # DABs bundle configuration
├── .gitignore                   # Ignores generated files
├── src/
│   ├── setup_demo_data.py       # Setup script for demo data
│   ├── generated-etl_daily_metrics.py      # (PySpark version - created by Claude)
│   └── generated-dlt_daily_metrics.py      # (DLT version - created by Claude)
└── resources/
    └── jobs/
        ├── generated-daily_metrics_job.yml # (PySpark job def - created by Claude)
        └── generated-daily_metrics_dlt.yml # (DLT pipeline def - created by Claude)
```

> **Note:** The `generated-*` files are created live during the demo by Claude Code. They are gitignored so each participant generates their own.

### Generated Files Summary

| File | Type | Description |
|------|------|-------------|
| `src/generated-etl_daily_metrics.py` | PySpark | Traditional batch ETL with explicit read/transform/write |
| `src/generated-dlt_daily_metrics.py` | DLT/SDP | Declarative pipeline with `@dlt.table` decorators |
| `resources/jobs/generated-daily_metrics_job.yml` | Job YAML | Lakeflow Jobs definition for PySpark |
| `resources/jobs/generated-daily_metrics_dlt.yml` | Pipeline YAML | DLT pipeline definition with quality expectations |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| uc-function-mcp not connecting | Check `claude mcp list`, verify Databricks token and URL |
| github MCP fails | Check GitHub token permissions (repo, write:org) |
| Bundle deploy fails | Run `databricks bundle validate` first |
| Job timeout | Increase cluster size or add autoscaling |
| Permission denied | Check Unity Catalog grants |
| Memory MCP empty | Memory persists only within the configured graph file |

---

## Claude Code Features Used

| Feature | What It Does | Location |
|---------|--------------|----------|
| Slash Commands | `/deploy`, `/run-job`, `/validate-data` | `.claude/commands/` |
| CLAUDE.md | Project context auto-loaded | Project root |
| Skills | Auto-triggered optimization & data quality | `.claude/skills/` |
| Subagents | Spark optimizer, job debugger, code reviewer | `.claude/agents/` |
| MCP | Query Databricks, create PRs, search docs | Connected servers |
| Hooks | Auto-format Python, validate bundle | `.claude/settings.json` |
| Checkpoints | Esc+Esc to rewind changes | Built-in |

### Customization

You can extend this project by:

- Adding custom slash commands for your workflows
- Creating new skills for domain-specific automation
- Configuring subagents for specialized tasks
- Adding hooks for team-specific validation
- Extending CLAUDE.md with project context

---

## Next Steps

1. Use this project as a template
2. Modify for your own ETL use cases
3. Explore the `.claude/` folder to customize commands, skills, and agents
