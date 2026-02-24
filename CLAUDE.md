# Databricks + Claude Code Hackathon

## Project Overview

This repository contains materials for training and hackathon sessions demonstrating **Claude Code with Databricks workflows**. The event teaches "vibe coding" - using AI assistants for rapid development of data engineering and data science solutions.

**Format:** Half-day workshop (morning training + afternoon hackathon)

---

## Repository Structure

```
databricks-claude-code-hackathon/
├── CLAUDE.md                    # This file - project memory
├── README.md                    # Quick start guide
├── demos/                       # Demo templates (code generated live)
│   ├── data-engineering/        # DABs + PySpark + DLT demo
│   │   ├── CLAUDE.md            # Project context for Claude
│   │   ├── README.md            # Live demo script
│   │   ├── .claude/             # Claude Code customizations
│   │   │   ├── commands/        # Custom slash commands
│   │   │   ├── skills/          # Auto-triggered skills
│   │   │   └── agents/          # Specialized subagents
│   │   ├── src/                 # generated-*.py created during demo
│   │   └── resources/jobs/      # generated-*.yml created during demo
│   └── data-science/            # MLflow + XGBoost demo
│       ├── CLAUDE.md            # Project context
│       ├── README.md            # Demo script
│       ├── .claude/             # Commands, skills, agents, hooks
│       └── src/                 # Training code
└── claude_code_guide.md         # Claude Code features reference
```

> **Note:** Demo folders contain templates only. Code is generated live by Claude during demos using `generated-` prefix.

---

## Two Tracks

### Track 1: Data Engineering
**Problem:** Build an Automated Product Reorder Alert Pipeline

| Component | Technology |
|-----------|------------|
| Project Structure | Databricks Asset Bundles (DABs) |
| ETL Jobs | PySpark |
| Streaming/CDC | Delta Live Tables (DLT) |
| Data Catalog | Unity Catalog |
| Orchestration | Lakeflow Jobs |

**Demo Features:**
- Custom slash commands (`/deploy`, `/run-job`, `/validate-data`)
- Auto-triggered skills (data quality, Spark optimization)
- Specialized subagents (spark-optimizer, job-debugger, code-reviewer)
- Hooks for auto-formatting Python with Ruff

### Track 2: Data Science
**Problem:** Build a Demand Forecasting Model

| Component | Technology |
|-----------|------------|
| Model Training | XGBoost |
| Experiment Tracking | MLflow |
| Feature Engineering | PySpark → Pandas |
| Model Registry | Unity Catalog |

---

## Data Sources

### Demo Data (Shared Between Both Tracks)

**Important:** Both Data Engineering and Data Science demos use the **same data**. Set it up once and use the same catalog.schema for both.

To create demo data in your own catalog/schema:
- Say "setup demo data in {catalog}.{schema}" to trigger the skill, OR
- Run `demos/*/src/setup_demo_data.py` in Databricks with your target catalog/schema

**Tables (after setup):**

| Table | Description | Sample Size |
|-------|-------------|-------------|
| `{catalog}.{schema}.orders` | Order transactions | 10,000 |
| `{catalog}.{schema}.order_products` | Order line items | ~35,000 |
| `{catalog}.{schema}.products` | Product catalog | 50 |
| `{catalog}.{schema}.departments` | Product departments | 21 |
| `{catalog}.{schema}.aisles` | Product aisles | 100 |

**Key Columns:**
- `orders`: order_id, user_id, order_dow (0-6), order_hour_of_day (0-23), days_since_prior_order
- `order_products`: order_id, product_id, add_to_cart_order, reordered (0/1)
- `products`: product_id, product_name, aisle_id, department_id

---

## MCP Integrations

This project uses multiple [MCP](https://code.claude.com/docs/en/mcp) servers. See `demos/*/.claude/mcp-config.example.json` for setup.

**Required:**

| Server | Purpose | Example Use |
|--------|---------|-------------|
| **uc-function-mcp** | Query Databricks via SQL | "Show me tables in catalog.schema" |
| **github** | Create PRs, issues | "Create a PR for my changes" |

**Optional (nice-to-have):**

| Server | Purpose | Example Use |
|--------|---------|-------------|
| **confluence** | Documentation | "Create a Confluence page documenting my pipeline" |
| **context7** | Library documentation | "Using context7, show Delta Lake MERGE syntax" |
| **brave-search** | Search best practices | "Search for Spark optimization tips" |
| **memory** | Persist facts across sessions | "Remember that X" |
| **obsidian** | Note-taking | "Create a note in my vault" |

**Verify connections:** `claude mcp list`

---

## Claude Code Features Demonstrated

| Feature | Location | Description |
|---------|----------|-------------|
| **Slash Commands** | `.claude/commands/` | /deploy, /run-job, /validate-data, /create-pr |
| **Skills** | `.claude/skills/` | Auto-triggered for "data quality", "setup demo data", "tune" |
| **Subagents** | `.claude/agents/` | spark-optimizer, job-debugger, code-reviewer |
| **Hooks** | `.claude/settings.json` | Auto-format Python, validate bundle pre-commit |
| **CLAUDE.md** | Project root | Project context auto-loaded by Claude |
| **Checkpoints** | Built-in | Press Esc twice to rewind changes |
| **/compact** | Built-in | Summarize long conversations |
| **/cost** | Built-in | Check token usage |

---

## Demo Script Highlights

### Data Engineering Demo (~45 min)

0. **Setup Demo Data** - "Setup demo data in {catalog}.{schema}"
1. **Verify MCP** - "What MCP servers do you have access to?"
2. **Explore Data** - "Show me what tables are in {catalog}.{schema}"
3. **Create ETL Pipelines** - PySpark batch + DLT side by side
4. **Optimize** - Delegate to spark-optimizer subagent
5. **Look Up Docs** - "Using context7, show me Delta Lake MERGE docs"
6. **Deploy & Run** - Deploy bundle and run the job
7. **Memory** - "Remember that our target schema is..."
8. **Commit & Push** - Git workflow
9. **Checkpoints** - Press Esc+Esc to rewind

### Data Science Demo (~45 min)

0. **Setup Demo Data** - "Setup demo data in {catalog}.{schema}"
1. **Verify MCP** - "What MCP servers do you have access to?"
2. **Explore Data** - Query distributions and patterns
3. **Feature Engineering** - Delegate to feature-engineer subagent
4. **Look Up Docs** - "Using context7, show me XGBoost early stopping"
5. **Build Pipeline** - Create XGBoost training code
6. **Train Model** - Upload and run on Databricks
7. **Evaluate** - Delegate to model-evaluator subagent
8. **Tune** - 5 hyperparameter trials with MLflow
9. **Memory** - "Remember the best hyperparameters"
10. **Commit & Push** - Git workflow
11. **Checkpoints** - Press Esc+Esc to rewind

---

## Important Notes

### Catalog Setup
The demos use `{catalog}.{schema}` placeholders throughout. Before running demos:

1. Check available catalogs: `SHOW CATALOGS`
2. Pick a catalog you have write access to
3. Run "setup demo data in {catalog}.{schema}" or use `demos/*/src/setup_demo_data.py` to create mock data

### Team Schemas
For hackathon participants, each team gets their own schema:
- Format: `{catalog}.team_{team_name}`
- Example: `samples.team_alpha`

### Safe Experimentation
Always create a branch before major experiments:
```bash
git checkout -b experiment/my-idea
# ... make changes ...
git checkout main  # to revert
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Catalog not found | Run `SHOW CATALOGS` to see available catalogs |
| MCP not connecting | Run `claude mcp list`, check authentication |
| Permission denied | Check Unity Catalog grants |
| Context too long | Use `/compact` to summarize |
| Job timeout | Increase timeout or reduce data scope |
| Preview not updating | Close and reopen VS Code preview tab |
| **Missing Python libraries** | Use ML Runtime 14.3+ OR add `%pip install xgboost scikit-learn matplotlib seaborn` + `dbutils.library.restartPython()` at start of notebook |
| Job fails on serverless | Ensure library installation cells are at the top of notebook, before imports |

---

## Contact

For questions about this hackathon, contact the facilitator or check the event Slack channel.
