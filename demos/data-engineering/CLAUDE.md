# Data Engineering Demo Project

## Overview

This is a Databricks Asset Bundles (DABs) project for the Vibe Coding Hackathon.
It demonstrates ETL job creation using both Lakeflow Jobs and Delta Live Tables (DLT).

**This demo showcases Claude Code features including:**
- Custom slash commands (`/deploy`, `/run-job`, `/validate-data`, `/create-pr`)
- Auto-triggered skills (data quality, Spark optimization)
- Specialized subagents (optimizer, debugger, code reviewer)
- Hooks for automatic code formatting
- MCP integrations (Databricks via uc-function-mcp, GitHub, Obsidian, Brave Search, Context7, Memory)

## Rules

- ALWAYS check `.claude/skills/` directory before implementing any task manually
- When user mentions "setup demo data", "data quality", or "optimize", use the corresponding skill
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
| `{catalog}.{schema}.order_products` | Order line items | ~60,000 |
| `{catalog}.{schema}.products` | Product catalog | 50 |
| `{catalog}.{schema}.departments` | Product departments | 21 |
| `{catalog}.{schema}.aisles` | Product aisles | 100 |

---

## Claude Code Features

### Custom Slash Commands

This project includes custom slash commands in `.claude/commands/`:

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

### Skills (Auto-Triggered)

Skills in `.claude/skills/` activate automatically based on context:

| Skill | Triggers On |
|-------|-------------|
| `data-quality-check` | "data quality", "null check", "validate output" |
| `spark-optimization` | "slow job", "optimize", "performance issue" |
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
- Cache DataFrames that are reused multiple times

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

```
├── CLAUDE.md                    # This file - project context
├── README.md                    # Demo script for presenter
├── .gitignore                   # Ignores generated files
├── .claude/
│   ├── commands/                # Custom slash commands
│   │   ├── deploy.md
│   │   ├── run-job.md
│   │   ├── validate-data.md
│   │   └── create-pr.md
│   ├── skills/                  # Auto-triggered skills
│   │   ├── data-quality-check.md
│   │   ├── spark-optimization.md
│   │   └── setup-demo-data.md
│   ├── agents/                  # Specialized subagents
│   │   ├── spark-optimizer.md
│   │   ├── job-debugger.md
│   │   └── code-reviewer.md
│   ├── settings.json            # Hooks and permissions
│   └── mcp-config.example.json  # MCP server reference template
├── src/
│   ├── setup_demo_data.py       # Setup script (upload to Databricks)
│   └── generated-*.py           # Created during demo by Claude
└── resources/
    └── jobs/
        └── generated-*.yml      # Created during demo by Claude
```

> **Note:** Files with `generated-` prefix are created live during the demo and are gitignored.

---

## Widget Parameters

Both notebooks support these configurable parameters:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `catalog` | (user-specified) | Unity Catalog name |
| `schema` | (user-specified) | Schema with demo data and output tables |

---

## Output Tables

### daily_order_metrics

Aggregated order metrics by day of week and hour of day.

| Column | Type | Description |
|--------|------|-------------|
| `day_of_week` | INT | 0 (Sunday) to 6 (Saturday) |
| `hour_of_day` | INT | 0 to 23 |
| `total_orders` | LONG | Count of orders |
| `unique_customers` | LONG | Distinct user count |
| `avg_days_since_prior_order` | DOUBLE | Average days between orders |
| `first_time_orders` | LONG | Orders with no prior order |
| `avg_items_per_order` | DOUBLE | Average basket size |
| `avg_reordered_items_per_order` | DOUBLE | Average reorder items |
| `max_items_in_order` | INT | Largest basket size |
| `processed_at` | TIMESTAMP | Processing timestamp |

