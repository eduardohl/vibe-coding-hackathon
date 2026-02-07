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
| `{catalog}.{schema}.order_products` | Order line items | ~35,000 |
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

### Plugin Bundle

This demo includes a complete plugin (`plugin.yaml`) that bundles all features:

```yaml
name: databricks-data-science
components:
  commands: [train, evaluate, tune, create-pr]
  skills: [mlflow-logging, hyperparameter-tuning]
  agents: [feature-engineer, model-evaluator, experiment-analyzer]
  hooks: [ruff format, ruff check]
```

**Plugins let you package and share Claude Code workflows with your team.**

### MCP Integrations

Pre-configured MCP servers (verify with `claude mcp list`):

| Server | Capabilities |
|--------|-------------|
| **uc-function-mcp** | Query Databricks tables via SQL, explore data |
| **github** | Create PRs, issues, manage repositories |
| **obsidian** | Document experiments, write notes and summaries |
| **brave-search** | Search for ML research and best practices |
| **context7** | Get up-to-date library documentation (XGBoost, MLflow) |
| **memory** | Persist experiment learnings across sessions |
| **puppeteer** | Visual verification of MLflow UI |
| **filesystem** | File operations outside the project |

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
│   ├── plugin.yaml                # Plugin bundle definition
│   └── mcp-config.example.json    # MCP configuration template
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

---

## Demo Scenarios

### Scenario 1: Train and Evaluate

```
You: /train
Claude: [Trains model with MLflow logging]
       [Logs parameters, metrics, and artifacts]

You: /evaluate
Claude: [Evaluates model on test set]
       [Shows metrics and feature importance]
```

### Scenario 2: Hyperparameter Tuning

```
You: Help me tune the hyperparameters
Claude: [Hyperparameter tuning skill activates]
       [Runs grid search with cross-validation]
       [Logs all trials to MLflow]
```

### Scenario 3: Feature Engineering

```
You: I need better features for my model
Claude: [Delegates to feature-engineer agent]
       [Analyzes data and suggests features]
       [Implements time and product features]
```

### Scenario 4: Analyze Experiments

```
You: Compare my MLflow runs and find the best model
Claude: [Delegates to experiment-analyzer agent]
       [Compares metrics across runs]
       [Identifies best configuration]
```

### Scenario 5: Model Debugging

```
You: My model is overfitting, can you help?
Claude: [Delegates to model-evaluator agent]
       [Analyzes train vs val curves]
       [Suggests regularization strategies]
```

### Scenario 6: Safe Experimentation (Checkpoints)

```
You: git checkout -b experiment/new-features
Claude: [Creates branch for safe experimentation]

You: Add interaction features to the model
Claude: [Implements changes on experiment branch]

You: That didn't improve things, let's go back
You: git checkout main
Claude: [Clean return to main branch - no harm done]
```

### Scenario 7: CLI Power Features

```bash
# Start Claude Code in your project
claude .

# Check what Claude remembers about experiments
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
| Memory error with toPandas | Sample data or aggregate in Spark first |
| MLflow experiment not found | Check experiment name path, create if needed |
| Model registration fails | Ensure models schema exists in Unity Catalog |
| Slow training | Use sample_fraction parameter, reduce data size |
| Overfitting | Add regularization, reduce model complexity |
| Permission denied | Check Unity Catalog grants on source tables |

---

## MCP Integration Examples

### Query Data (uc-function-mcp)

```
Using the Databricks MCP, show me the reorder rate by department

What's the distribution of order_hour_of_day in the orders table?

Show me 5 sample rows from order_products joined with products
```

### Look Up Documentation (context7)

```
Using context7, show me XGBoost documentation for early stopping

What's the MLflow autolog syntax for scikit-learn?
```

### Search Best Practices (brave-search)

```
Search for feature engineering best practices for demand forecasting

Find recent papers on XGBoost hyperparameter tuning
```

### Create Documentation (obsidian)

```
Create a note in my Obsidian vault under "ML Experiments/Demand Forecast" with:
- Hypothesis tested
- Model configuration
- Results and next steps
```

### Persist Learnings (memory)

```
Remember that log-transforming the target improved RMSE by 15%
and optimal learning_rate was 0.1

What hyperparameters worked best in our experiments?
```

### Create PR (github)

```
Create a GitHub PR for the improved training code with experiment results

Create a GitHub issue for "Investigate feature interactions"
```

---

## Testing Checklist

- [ ] MLflow experiment is created and accessible
- [ ] Training completes without errors
- [ ] Metrics are logged to MLflow
- [ ] Model artifact is saved
- [ ] Feature importance is logged
- [ ] Can compare multiple runs in MLflow UI
