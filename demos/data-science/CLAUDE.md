# Data Science Demo Project

## Overview

This project demonstrates ML experimentation workflows using Claude Code
with MLflow for experiment tracking on Databricks.

**Problem:** Demand Forecasting - Predict order counts for products
**Model Type:** Regression (XGBoost)
**Tracking:** MLflow experiments

**This demo showcases Claude Code features including:**
- Custom skills (`/train`, `/evaluate`, `/tune`, `/create-pr`)
- Auto-triggered skills (MLflow logging, hyperparameter tuning)
- Specialized subagents (feature engineer, model evaluator, experiment analyzer)
- Hooks for automatic code formatting
- MCP integrations (Databricks via uc-function-mcp, GitHub, Obsidian, Brave Search, Context7, Memory)

## Rules

- **ONLY use local skills** from this project's `.claude/skills/` directory — do NOT use `fe-databricks-tools`, `fe-workflows`, or any other external plugin skills. This demo must be self-contained.
- ALWAYS check `.claude/skills/` directory before implementing any task manually
- When user mentions "setup demo data", "mlflow", "tune", or "hyperparameter", use the corresponding skill
- Read the skill file and follow its instructions exactly before writing any code
- **IMPORTANT:** When creating new files, use the `generated-` prefix (e.g., `generated-train_model.py`) to distinguish demo-created files from template files
- **CRITICAL:** When creating new Databricks notebooks that use ML libraries (xgboost, scikit-learn, matplotlib, seaborn), ALWAYS add library installation cells at the very beginning BEFORE any imports:
  ```python
  # MAGIC %pip install xgboost scikit-learn matplotlib seaborn --quiet
  dbutils.library.restartPython()
  ```
  These libraries are NOT pre-installed on serverless compute and must be installed explicitly.

## Environment

### Databricks Workspace

- Platform: Azure Databricks
- Unity Catalog enabled
- MLflow tracking enabled (automatic in Databricks)
- Compute: Serverless (default for hackathon)

**Non-Standard Libraries Required:**
- xgboost, scikit-learn, matplotlib, seaborn
- Must be installed in notebook via `%pip install` + `dbutils.library.restartPython()`
- Always add installation cells at the start of any new notebook

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

| Skill | Description | Triggers On |
|-------|-------------|-------------|
| `/train` | Train a model with MLflow logging | User invokes `/train` |
| `/evaluate` | Evaluate model performance metrics | User invokes `/evaluate` |
| `/tune` | Run hyperparameter tuning | User invokes `/tune` |
| `/create-pr` | Create a pull request with experiment results | User invokes `/create-pr` |
| `mlflow-logging` | Auto-triggered MLflow logging | "mlflow", "log experiment", "track experiment" |
| `hyperparameter-tuning` | Auto-triggered hyperparameter tuning | "tune", "hyperparameter", "grid search" |
| `setup-demo-data` | Auto-triggered demo data setup | "setup demo data" |

**Example usage:**

```
/train              # Train with default config
/evaluate           # Evaluate latest model
/tune               # Run hyperparameter search
```

**Auto-trigger example:** Just say "log this to MLflow" and the mlflow-logging skill activates.

### Subagents (Specialists)

Specialized agents in `.claude/agents/` for complex tasks:

| Agent | Purpose |
|-------|---------|
| `feature-engineer` | Create and optimize features for ML models |
| `model-evaluator` | Analyze model performance and diagnose issues |
| `experiment-analyzer` | Compare MLflow runs and find best configurations |

**Example:** "Delegate to the feature-engineer to create time-based features"

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
| **uc-function-mcp** | Query Databricks tables via SQL, explore data |
| **github** | Create PRs, issues, manage repositories |

**Optional (nice-to-have):**

| Server | Capabilities |
|--------|-------------|
| **confluence** | Read/write Confluence pages for documentation |
| **context7** | Get up-to-date library documentation (XGBoost, MLflow) |
| **brave-search** | Search for ML research and best practices |
| **memory** | Persist experiment learnings across sessions |
| **obsidian** | Document experiments, write notes and summaries |

---

## MLflow Configuration

- **Experiment path:** `/Users/{your_email}/hackathon-demand`
- **Required logging:** parameters (all hyperparameters), metrics (train/val/test RMSE, MAE, R²), artifacts (feature_importance.csv, model), tags (model_type, env, owner)
- **Model Registry:** `{catalog}.models.{model_name}` (create schema first: `CREATE SCHEMA IF NOT EXISTS {catalog}.models`)

---

## Coding Standards

### Databricks Notebooks

- **ALWAYS start with library installation** for non-standard libraries (xgboost, scikit-learn, matplotlib, seaborn)
- Use `%pip install` followed by `dbutils.library.restartPython()` in first cells
- Place library installation BEFORE configuration and imports
- Standard structure: Install → Restart → Config → Imports → Code

### Python & Data Processing

- Use type hints; follow PEP 8 (auto-enforced by Ruff hook)
- Aggregate in Spark before `toPandas()` — check data size first
- Split data: 70% train, 15% validation, 15% test
- Use log transforms for skewed targets (demand data)
- Always check for data leakage

---

## File Structure

- `CLAUDE.md` — This file (project context)
- `README.md` — Demo script for presenter
- `.claude/skills/` — Skills: `/train`, `/evaluate`, `/tune`, `/create-pr`, plus auto-triggered (mlflow-logging, hyperparameter-tuning, setup-demo-data)
- `.claude/agents/` — Subagents: feature-engineer, model-evaluator, experiment-analyzer
- `src/setup_demo_data.py` — Setup script (upload to Databricks)
- `src/generated-*.py` — Created live during demo (gitignored)
