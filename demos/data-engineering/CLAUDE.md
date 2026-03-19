# Data Engineering Demo Project

## Overview

This is a Databricks Asset Bundles (DABs) project for the Vibe Coding Hackathon.
It demonstrates ETL job creation using both Lakeflow Jobs and Delta Live Tables (DLT).

**This demo showcases Claude Code features including:**
- Custom skills (`/deploy`, `/run-job`, `/validate-data`, `/create-pr`)
- Auto-triggered skills (data quality, demo data setup)
- Specialized subagents (optimizer, debugger, code reviewer)
- Hooks for automatic code formatting
- MCP integrations (Databricks via uc-function-mcp, GitHub, Obsidian, Brave Search, Context7, Memory)

## Rules

- **ONLY use local skills** from this project's `.claude/skills/` directory — do NOT use `fe-databricks-tools`, `fe-workflows`, or any other external plugin skills. This demo must be self-contained.
- ALWAYS check `.claude/skills/` directory before implementing any task manually
- When user mentions "setup demo data" or "data quality", use the corresponding skill
- Read the skill file and follow its instructions exactly before writing any code
- **IMPORTANT:** When creating new files, use the `generated-` prefix (e.g., `generated-etl_daily_metrics.py`) to distinguish demo-created files from template files

## Environment

### Databricks Workspace

- Platform: Azure Databricks
- Unity Catalog enabled
- DBR Version: 14.3 LTS or higher

### Data Sources

- **Catalog:** `{catalog}` - Replace with your catalog
- **Schema:** `{schema}` - Replace with your schema

> **First time?** Run "setup demo data in {catalog}.{schema}" to create the tables.

### Key Tables

| Table | Description | Row Count |
|-------|-------------|-----------|
| `{catalog}.{schema}.orders` | Order transactions | 10,000 |
| `{catalog}.{schema}.order_products` | Order line items | ~35,000 |
| `{catalog}.{schema}.products` | Product catalog | 50 |
| `{catalog}.{schema}.departments` | Product departments | 21 |
| `{catalog}.{schema}.aisles` | Product aisles | 100 |

---

## Claude Code Features

### Custom Skills

This project includes custom skills in `.claude/skills/`:

| Command | Description |
|---------|-------------|
| `/deploy` | Deploy the DABs bundle to dev/staging/prod |
| `/run-job` | Run a job and monitor execution |
| `/validate-data` | Check data quality of output tables |
| `/create-pr` | Create a pull request with changes |

**Example usage:**

```
/deploy              # Deploy to dev
/run-job             # Run the daily_metrics_job
/validate-data       # Check output data quality
```

### Skills

Skills in `.claude/skills/` activate automatically based on context:

| Skill | Triggers On |
|-------|-------------|
| `data-quality-check` | "data quality", "null check", "validate output" |
| `setup-demo-data` | "setup demo data", "create mock data" |

**Example:** Just say "check the data quality" and the skill activates.

### Subagents (Specialists)

Specialized agents in `.claude/agents/` for complex tasks:

| Agent | Purpose |
|-------|---------|
| `spark-optimizer` | Analyze code for performance improvements |
| `job-debugger` | Diagnose and fix failed job runs |
| `code-reviewer` | Review code for best practices |

**Example:** "Delegate to the spark-optimizer to analyze my code"

### Hooks (Automation)

Hooks in `.claude/settings.json` run automatically:

| Hook | Trigger | Action |
|------|---------|--------|
| PostToolUse:Write | After writing .py files | Auto-format with Ruff |
| PostToolUse:Edit | After editing .py files | Auto-lint with Ruff |

### MCP Integrations

Verify with `claude mcp list`. See `.claude/mcp-config.example.json` for setup.

**Required:**

| Server | Capabilities |
|--------|-------------|
| **uc-function-mcp** | Query Databricks tables via SQL, explore schemas |
| **github** | Create PRs, issues, manage repositories |

**Optional (nice-to-have):**

| Server | Capabilities |
|--------|-------------|
| **confluence** | Read/write Confluence pages for documentation |
| **context7** | Get up-to-date library documentation |
| **brave-search** | Search for Spark/Databricks best practices |
| **memory** | Persist learnings and facts across sessions |
| **obsidian** | Document pipelines, write notes and summaries |

---

## Coding Standards

### PySpark

- Use DataFrame API over SQL strings when possible
- Always use `F.col()` from `pyspark.sql.functions` for column references
- Avoid `spark.sql()` with string interpolation - use DataFrame API instead
- Avoid `collect()` on large datasets
- Do NOT use `.cache()` or `.persist()` — not supported on serverless compute

### Delta Lake

- Use Delta format for all output tables
- Enable change data feed where appropriate
- Set appropriate partition columns for large tables
- Use OPTIMIZE and ZORDER for query performance

### Unity Catalog

- Always use three-part naming: `catalog.schema.table`
- Never use `hive_metastore` - use Unity Catalog only
- Set appropriate table/column comments
- Use tags for data classification

### Code Quality

- Add type hints to functions
- Use logging instead of print for production code
- Include data quality checks before writing
- Handle errors gracefully with informative messages

---

## DABs Commands

```bash
# Validate bundle configuration
databricks bundle validate

# Deploy to development
databricks bundle deploy --target dev

# Run a specific job
databricks bundle run daily_metrics_job --target dev

# Check job status
databricks bundle run daily_metrics_job --target dev --no-wait

# Destroy resources (cleanup)
databricks bundle destroy --target dev
```

---

## File Structure

- `CLAUDE.md` — This file (project context)
- `README.md` — Demo script for presenter
- `.claude/skills/` — Skills: `/deploy`, `/run-job`, `/validate-data`, `/create-pr`, plus auto-triggered (data-quality-check, setup-demo-data)
- `.claude/agents/` — Subagents: spark-optimizer, job-debugger, code-reviewer
- `src/setup_demo_data.py` — Setup script (upload to Databricks)
- `src/generated-*.py` — Created live during demo (gitignored)
- `resources/jobs/generated-*.yml` — Job definitions created during demo (gitignored)
