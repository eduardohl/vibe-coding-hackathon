# Demo: Claude Code + Classic ML on Databricks

## Overview

**Duration:** 45 minutes
**Track:** Data Science - Experimentation & Logging
**Audience:** Data Scientists, ML Engineers

## Demo Objectives

By the end of this demo, participants will see how Claude Code can:
1. Explore data using the **Databricks MCP (uc-function-mcp)**
2. Build a complete ML training pipeline from scratch
3. Engineer features with help from specialized subagents
4. Train models with proper MLflow logging
5. Iterate on hyperparameters automatically
6. Create PRs with experiment results via **GitHub MCP**

---

## Getting Started

### Prerequisites

1. Open terminal in `demos/data-science/` directory
2. Run `claude mcp list` to verify all MCPs are connected
3. Have Databricks workspace open in browser (MLflow UI ready)
4. Clear any previous Claude Code sessions: `claude /clear`

### Features You'll Use

| Feature | When It Appears |
|---------|-----------------|
| **Hooks** | Step 6 (auto-format on file write) |
| **Subagents** | Step 5 (feature-engineer), Step 8 (model-evaluator) |
| **MCP** | Steps 2-3 (Databricks), Step 5 (Context7), Step 9 (Memory), Step 11 (GitHub) |

---

## Step-by-Step Guide

### Step 0: Setup Demo Data (if needed)

If you don't have sample data yet, create it:

**Option A - Via Claude (Recommended):**

```
Setup demo data in {catalog}.{schema}
```

Replace `{catalog}.{schema}` with your target location (e.g., `samples.my_schema`).

This creates 5 tables (departments, aisles, products, orders, order_products) with mock grocery data.

**Note:** This data is shared with the Data Engineering demo - if you already set it up there, just use the same catalog.schema here.

**Option B - Via Databricks:**

1. Upload `src/setup_demo_data.py` to Databricks workspace
2. Run the notebook with your target catalog/schema
3. Update CLAUDE.md with the correct catalog/schema

### Step 1: Start Claude Code

```bash
cd demos/data-science
claude .
```

### Step 2: Verify MCP Connection

```
What MCP servers do you have access to?
```

Claude will list connected servers (github, uc-function-mcp, brave-search, etc.).

### Step 3: Explore Data with Databricks MCP

```
Using the Databricks MCP, what does the schema of {catalog}.{schema}.orders look like?
```

Then explore the data:

```
What's the distribution of orders by day of week?
```

Claude queries your live Databricks workspace via the MCP connection.

### Step 4: Use Feature Engineer Subagent

```
Delegate to the feature-engineer agent to design features for a demand forecasting model using the demo data and create a notebook with the feature engineering code  (e.g., demos/data-science/src/generated-feature_engineering.py)
```

The feature-engineer subagent will:
- Analyze the data schema
- Suggest cyclical time features
- Recommend target transformations
- Propose aggregation features

### Step 5: Look Up Documentation with Context7

```
Using context7, show me XGBoost documentation for early stopping
```

Context7 provides up-to-date documentation from official sources.

### Step 6: Build the Training Pipeline

```
Create an XGBoost demand forecasting model that:
- Reads from {catalog}.{schema}.orders and order_products
- Implements the features we discussed
- Uses proper train/val/test splits
- Logs everything to MLflow
- Use a small sample for speed
```

Claude will create `src/generated-train_demand_model.py` from scratch.

> **Hooks in action:** When Claude writes .py files, they get auto-formatted with Ruff via the PostToolUse hook.

### Step 7: Train the Model

```
Create and upload a combined training script (features and training) on Databricks and run it as a Job.
```

Claude runs the training and logs all parameters, metrics, and artifacts to MLflow.

Check the MLflow UI to see the logged run.

### Step 8: Use Model Evaluator Subagent

```
Delegate to the model-evaluator agent to analyze the model performance and diagnose any issues
```

The model-evaluator subagent will:
- Analyze metrics across train/val/test
- Identify overfitting/underfitting
- Suggest regularization strategies
- Recommend next steps

### Step 9: Hyperparameter Tuning

```
The RMSE is high. Run 5 hyperparameter tuning trials, varying learning_rate and max_depth. Log each trial to MLflow.
```

Claude iterates autonomously - this is "autopilot" mode for ML experimentation.
Check the experiment again.

### Step 10: Save to Memory

```
Remember that the best hyperparameters were learning_rate=0.1, max_depth=6, and that log-transforming the target improved RMSE by 15%
```

The memory MCP persists information across sessions - useful for long-running projects.

### Step 11: Commit and Push

```
Commit and push these changes
```

Claude will stage, commit, and push to the remote repository.

### Step 12: Try Claude Code Features

**Checkpoints - safe experimentation:**

```
Let me try adding polynomial features to the model
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
- Built an ML training pipeline from scratch
- Used subagents for feature engineering and model evaluation
- Trained models with MLflow logging
- Run automated hyperparameter tuning
- Created a commit with experiment results

---

## Bonus: Example Prompts

### Databricks SQL (uc-function-mcp)

```
What columns are in {catalog}.{schema}.order_products?
What's the average number of items per order?
Show me the top 10 most reordered products
```

### Context7 - Documentation Lookup

```
Using context7, show me XGBoost documentation for early stopping
What's the MLflow autolog syntax for scikit-learn?
```

### Brave Search - Research

```
Search for recent papers on demand forecasting with gradient boosting
Find best practices for feature engineering in retail ML
```

### Memory - Persist Learnings

```
Remember that log-transforming the target variable improved RMSE by 15%
What hyperparameters worked best in our previous experiments?
```

### GitHub - Version Control

```
Create a GitHub issue for "Investigate feature interactions for demand model"
Create a PR for my changes with experiment results in the description
```

---

## Files in This Demo

```
demos/data-science/
├── README.md                      # This file
├── CLAUDE.md                      # Project context for Claude
├── .gitignore                     # Ignores generated files
├── .claude/
│   ├── commands/                  # Custom slash commands
│   │   ├── train.md
│   │   ├── evaluate.md
│   │   ├── tune.md
│   │   └── create-pr.md
│   ├── skills/                    # Auto-triggered skills
│   │   ├── setup-demo-data.md
│   │   ├── hyperparameter-tuning.md
│   │   └── mlflow-logging.md
│   ├── agents/                    # Specialized subagents
│   │   ├── model-evaluator.md
│   │   ├── feature-engineer.md
│   │   └── experiment-analyzer.md
│   ├── settings.json              # Hooks and permissions
│   ├── plugin.yaml                # Plugin bundle definition
│   └── mcp-config.example.json    # MCP configuration template
└── src/
    ├── setup_demo_data.py         # Setup script for demo data
    └── generated-*.py             # Created during demo by Claude
```

> **Note:** The `generated-*` files are created live during the demo by Claude Code. They are gitignored so each participant generates their own.

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| uc-function-mcp not connecting | Check `claude mcp list`, verify Databricks token and URL |
| github MCP fails | Check GitHub token permissions (repo, write:org) |
| MLflow experiment not found | Check experiment name and user permissions |
| Training OOM | Reduce batch size or sample data |
| Model not improving | Check for data leakage, try different features |
| Memory MCP empty | Memory persists only within the configured graph file |

---

## Claude Code Features Used

| Feature | What It Does | Location |
|---------|--------------|----------|
| Slash Commands | `/train`, `/evaluate`, `/tune`, `/create-pr` | `.claude/commands/` |
| CLAUDE.md | Project context auto-loaded | Project root |
| Skills | Auto-triggered for hyperparameter tuning, MLflow logging | `.claude/skills/` |
| Subagents | Model evaluator, feature engineer, experiment analyzer | `.claude/agents/` |
| MCP | Query Databricks, create PRs, search docs | Connected servers |
| Hooks | Auto-format Python with Ruff | `.claude/settings.json` |
| Checkpoints | Esc+Esc to rewind changes | Built-in |

### Customization

You can extend this project by:

- Adding custom slash commands for your ML workflows
- Creating new skills for domain-specific automation
- Configuring subagents for specialized analysis
- Adding hooks for team-specific validation
- Extending CLAUDE.md with experiment context

---

## Next Steps

1. Use this project as a template
2. Modify for your own ML use cases
3. Explore the `.claude/` folder to customize commands, skills, and agents
