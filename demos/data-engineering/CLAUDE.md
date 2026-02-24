# Data Engineering Demo Project

## Overview

This is a Databricks Asset Bundles (DABs) project for the Vibe Coding Hackathon.
It demonstrates ETL job creation using both Lakeflow Jobs and Lakeflow SDP (DLT).

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
| PreCommit | Before git commit | Validate DABs bundle |

### Plugin Bundle

This demo includes a complete plugin (`plugin.yaml`) that bundles all features:

```yaml
name: databricks-data-engineering
components:
  commands: [deploy, run-job, validate-data, create-pr]
  skills: [data-quality-check, spark-optimization]
  agents: [spark-optimizer, job-debugger, code-reviewer]
  hooks: [ruff format, ruff check, bundle validate]
```

**Plugins let you package and share Claude Code workflows with your team.**

### MCP Integrations

Pre-configured MCP servers (verify with `claude mcp list`):

| Server | Capabilities |
|--------|-------------|
| **uc-function-mcp** | Query Databricks tables via SQL, explore schemas |
| **github** | Create PRs, issues, manage repositories |
| **obsidian** | Document pipelines, write notes and summaries |
| **brave-search** | Search for Spark/Databricks best practices |
| **context7** | Get up-to-date library documentation |
| **memory** | Persist learnings and facts across sessions |
| **puppeteer** | Visual verification of Databricks UI |
| **filesystem** | File operations outside the project |

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
├── databricks.yml               # DABs bundle configuration
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
│   └── plugin.yaml              # Plugin bundle definition
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

---

## Demo Scenarios

### Scenario 1: Deploy and Run

```
You: Read CLAUDE.md then /deploy
Claude: [Validates and deploys bundle to dev]

You: /run-job
Claude: [Runs job and monitors completion]

You: /validate-data
Claude: [Checks output data quality]
```

### Scenario 2: Optimize Slow Job

```
You: My job is taking too long, can you optimize it?
Claude: [Spark optimization skill activates]
       [Analyzes code and suggests improvements]
```

### Scenario 3: Debug Failed Job

```
You: The job failed, can you debug it?
Claude: [Delegates to job-debugger agent]
       [Analyzes logs and provides fix]
```

### Scenario 4: Code Review and PR

```
You: Review my code changes
Claude: [Delegates to code-reviewer agent]

You: /create-pr
Claude: [Creates PR via GitHub MCP]
```

### Scenario 5: Safe Experimentation (Checkpoints)

```
You: git checkout -b experiment/add-gold-layer
Claude: [Creates branch for safe experimentation]

You: Add a gold layer to the DLT pipeline
Claude: [Implements changes on experiment branch]

You: That's not what I wanted, let's go back
You: git checkout main
Claude: [Clean return to main branch - no harm done]
```

### Scenario 6: CLI Power Features

```bash
# Start Claude Code in your project
claude .

# Check what Claude remembers about this project
claude /memory

# See token usage
claude /cost

# Compact a long conversation
claude /compact

# Check MCP server status
claude /mcp
```

---

## Common Issues

| Issue | Solution |
|-------|----------|
| Permission denied | Check Unity Catalog grants on source tables |
| Schema not found | Verify target schema exists or create it |
| Job timeout | Increase timeout in job YAML or reduce data scope |
| Cluster start failure | Check compute quota and instance availability |

---

## MCP Integration Examples

### Query Data (uc-function-mcp)

```
Using the Databricks MCP, show me the schema for {catalog}.{schema}.orders

Query the top 10 products by order count from the demo data

What tables are available in {catalog}.{schema}?
```

### Look Up Documentation (context7)

```
Using context7, show me the Delta Lake MERGE documentation

What's the PySpark syntax for window functions?
```

### Search Best Practices (brave-search)

```
Search for Spark partition pruning best practices

Find recent articles on Delta Lake optimization
```

### Create Documentation (obsidian)

```
Create a note in my Obsidian vault under "Pipelines/Daily Metrics" with:
- Purpose and data flow
- Input/output tables
- Schedule and monitoring
```

### Persist Learnings (memory)

```
Remember that {catalog}.{schema}.orders has 10K rows
and our target schema is {catalog}.{schema}

What do you remember about this project?
```

### Create PR (github)

```
Create a GitHub PR for my changes with a summary of what was modified

Create a GitHub issue for "Add data quality monitoring to pipeline"
```
