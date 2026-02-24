# Data Science Demo Project

## Overview

This project demonstrates ML experimentation workflows using Claude Code
with MLflow for experiment tracking on Databricks.

**Problem:** Demand Forecasting - Predict order counts for products
**Model Type:** Regression (XGBoost)
**Tracking:** MLflow experiments

**This demo showcases Claude Code features including:**
- Custom slash commands (`/train`, `/evaluate`, `/tune`, `/create-pr`)
- Auto-triggered skills (MLflow logging, hyperparameter tuning)
- Specialized subagents (feature engineer, model evaluator, experiment analyzer)
- Hooks for automatic code formatting
- MCP integrations (Databricks via uc-function-mcp, GitHub, Obsidian, Brave Search, Context7, Memory)

## Rules

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

> **Note:** This demo uses the **same data** as the Data Engineering demo. If you already ran "setup demo data" for data-engineering, just use the same catalog.schema here - no need to recreate.

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
| `/train` | Train a model with MLflow logging |
| `/evaluate` | Evaluate model performance metrics |
| `/tune` | Run hyperparameter tuning |
| `/create-pr` | Create a pull request with experiment results |

**Example usage:**

```
/train              # Train with default config
/evaluate           # Evaluate latest model
/tune               # Run hyperparameter search
```

### Skills (Auto-Triggered)

Skills in `.claude/skills/` activate automatically based on context:

| Skill | Triggers On |
|-------|-------------|
| `mlflow-logging` | "mlflow", "log experiment", "track experiment" |
| `hyperparameter-tuning` | "tune", "hyperparameter", "grid search" |
| `setup-demo-data` | "setup demo data" |

**Example:** Just say "log this to MLflow" and the skill activates.

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

### Experiment Naming Convention
```
/Users/{your_email}/hackathon-demand
```

To get your username in a notebook:
```python
username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
experiment_name = f"/Users/{username}/hackathon-demand"
mlflow.set_experiment(experiment_name)
```

### Required Logging

Every training run must log:

| Category | What to Log |
|----------|-------------|
| **Parameters** | All hyperparameters (learning_rate, max_depth, n_estimators, etc.) |
| **Metrics** | train_rmse, val_rmse, test_rmse, train_mae, val_mae, test_mae, r2 |
| **Artifacts** | feature_importance.csv, model file |
| **Tags** | model_type, env, owner, data_version, problem_type |

### Model Registry

- Use Unity Catalog Model Registry for production models
- Path: `{catalog}.models.{model_name}`
- Always add model description and input/output signatures

Note: The `models` schema must exist. Create if needed:
```sql
CREATE SCHEMA IF NOT EXISTS {catalog}.models;
```

---

## Coding Standards

### Databricks Notebooks

- **ALWAYS start with library installation** for non-standard libraries (xgboost, scikit-learn, matplotlib, seaborn)
- Use `%pip install` followed by `dbutils.library.restartPython()` in first cells
- Place library installation BEFORE configuration and imports
- Standard structure: Install → Restart → Config → Imports → Code

### Python

- Use type hints for function signatures
- Follow PEP 8 style guide
- Use `logging` module instead of print statements in production
- Add docstrings to functions

### Data Processing

- Use Spark for large datasets, pandas for aggregated/small datasets
- Aggregate in Spark before converting to pandas with `toPandas()`
- Check data size before `toPandas()` to avoid memory issues
- Always validate data shapes after transformations

### ML Best Practices

- Split data: 70% train, 15% validation, 15% test
- Use time-based splits for time series data (no random shuffle)
- Always check for data leakage
- Log all preprocessing steps
- Use log transforms for skewed targets (demand data)

---

## File Structure

```
├── CLAUDE.md                      # This file - project context
├── README.md                      # Demo script for presenter
├── .gitignore                     # Ignores generated files
├── .claude/
│   ├── commands/                  # Custom slash commands
│   │   ├── train.md
│   │   ├── evaluate.md
│   │   ├── tune.md
│   │   └── create-pr.md
│   ├── skills/                    # Auto-triggered skills
│   │   ├── mlflow-logging.md
│   │   ├── hyperparameter-tuning.md
│   │   └── setup-demo-data.md
│   ├── agents/                    # Specialized subagents
│   │   ├── feature-engineer.md
│   │   ├── model-evaluator.md
│   │   └── experiment-analyzer.md
│   ├── settings.json              # Hooks and permissions
│   └── mcp-config.example.json    # MCP server reference template
└── src/
    ├── setup_demo_data.py         # Setup script (upload to Databricks)
    └── generated-*.py             # Created during demo by Claude
```

> **Note:** The `generated-*` files are created live during the demo by Claude Code. They are gitignored so each participant generates their own.

---

## Quick Start Commands

### Set MLflow Experiment
```python
import mlflow

username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
mlflow.set_experiment(f"/Users/{username}/hackathon-demand")
```

### Start a Training Run
```python
with mlflow.start_run(run_name="my-experiment"):
    mlflow.log_params(params)
    mlflow.log_metrics(metrics)
    mlflow.xgboost.log_model(model, "model")
```

### Search Past Runs
```python
runs = mlflow.search_runs(
    experiment_names=[f"/Users/{username}/hackathon-demand"],
    order_by=["metrics.val_rmse ASC"]
)
```

### Load a Model
```python
model = mlflow.xgboost.load_model(f"runs:/{run_id}/model")
```

---

## Evaluation Metrics

### For Regression (Demand Forecasting)

| Metric | Description | Goal |
|--------|-------------|------|
| **RMSE** | Root Mean Square Error | Lower is better (primary) |
| **MAE** | Mean Absolute Error | Lower is better |
| **R²** | Coefficient of determination | Higher is better (closer to 1) |
| **MAPE** | Mean Absolute Percentage Error | Lower is better |

### Baseline Performance

A good baseline model should achieve:
- Val RMSE: ~0.85 (on log-transformed target)
- Test R²: > 0.5

---

## Feature Engineering Ideas

### Product Features
- Total historical orders
- Reorder rate (% of orders that are reorders)
- Average cart position
- Department/aisle popularity

### Time Features
- Day of week (0-6)
- Hour of day (0-23)
- Is weekend (binary)
- Cyclical encoding: `sin(2π * hour/24)`, `cos(2π * hour/24)`

### Advanced Features
- Product rank within department
- Customer purchase frequency
- Interaction features (department × time)

