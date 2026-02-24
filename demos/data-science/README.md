# Demo: Data Science with Claude Code

> **45 min** | XGBoost + MLflow + Feature Engineering | [Full Claude Code Docs](https://code.claude.com/docs/en/overview)
>
> **Prerequisite:** Run the [Data Engineering demo](../data-engineering/README.md) first. It covers Skills, MCP verification, and demo data setup — this demo skips those steps.

---

## Quick Reference — Prompts to Type

| Step | Prompt | Feature Shown |
|------|--------|---------------|
| 0 | *Start Claude Code in `demos/data-science/`* | Setup |
| 1 | `Using the Databricks MCP, what does the schema of {catalog}.{schema}.orders look like?` | MCP (live query) |
| 2 | `Delegate to the feature-engineer agent to design features...` *(see below)* | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 3 | `Using context7, show me XGBoost documentation for early stopping` | MCP (docs lookup) |
| 4 | `Create an XGBoost demand forecasting model...` *(see below)* | Code generation + [Hooks](https://code.claude.com/docs/en/hooks) |
| 5 | `Create and upload a combined training script on Databricks and run it` | CLI automation |
| 6 | `Delegate to the model-evaluator agent to analyze performance` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 7 | `Run 5 hyperparameter tuning trials, varying learning_rate and max_depth` | Autonomous iteration |
| 8 | `Remember that the best hyperparameters were learning_rate=0.1, max_depth=6` | [Memory](https://code.claude.com/docs/en/memory) |
| 9 | `Commit and push these changes` | Git workflow |
| 10 | *Press `Esc` twice* | [Checkpoints](https://code.claude.com/docs/en/overview) |

---

## Prerequisites

1. **Data Engineering demo completed** — demo data and MCP already verified
2. Terminal open in `demos/data-science/`
3. **Verify your Databricks MCP (`uc-function-mcp`) is configured to the correct workspace/profile** — run `databricks auth env --profile {profile_name}` to confirm
4. Databricks workspace open in browser (MLflow UI ready)
5. Fresh session: start `claude`, then type `/clear`

---

## Walkthrough

### Step 0: Start Claude Code

```bash
cd demos/data-science
claude .
```

Tell Claude your environment (same catalog/schema as the DE demo):

```
My catalog is {catalog} and my schema is {schema}. Remember this for the rest of our session.
My Databricks CLI profile is {profile_name}. Only operate on this profile's workspace — no other workspaces are allowed.
```

> Demo data and MCP verification were covered in the Data Engineering demo — no need to repeat.

---

### Step 1: Explore Live Data

```
Using the Databricks MCP, what does the schema of {catalog}.{schema}.orders look like?
```

Then:

```
What's the distribution of orders by day of week?
```

> **Observe:** That's your *live* Databricks workspace queried via MCP — schemas, samples, aggregations, all through natural language.

**Try your own:** Ask Claude anything — "How many unique products?" "What's the reorder rate?"

---

### Step 2: Feature Engineering with a Subagent

```
Delegate to the feature-engineer agent to design features for a demand forecasting model using the demo data and create a notebook with the feature engineering code (e.g., demos/data-science/src/generated-feature_engineering.py)
```

> **Observe:** Claude delegates to a [subagent](https://code.claude.com/docs/en/sub-agents) with its own domain expertise. Notice it suggests cyclical encoding and log transforms — that's the agent's prompt guiding its reasoning. What features would *you* have created? How do these compare?

---

### Step 3: Look Up Documentation

```
Using context7, show me XGBoost documentation for early stopping
```

> **Observe:** Context7 fetches *current* library docs via [MCP](https://code.claude.com/docs/en/mcp) — not stale training data. Try it with MLflow too.

---

### Step 4: Build the Training Pipeline

```
Create an XGBoost demand forecasting model that:
- Reads from {catalog}.{schema}.orders and order_products
- Implements the features we discussed
- Uses proper train/val/test splits
- Logs everything to MLflow
- Use a small sample for speed
```

> **Observe:** (1) Claude builds a complete pipeline referencing features from Step 2, and (2) each `.py` gets auto-formatted — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) firing Ruff.

---

### Step 5: Train the Model

```
Create and upload a combined training script (features and training) on Databricks and run it as a Job.
```

> **Observe:** Claude uploads the notebook, triggers a run, and returns the URL.

**While it runs:** Open the MLflow UI — can everyone find the experiment? Check the logged parameters and metrics.

---

### Step 6: Evaluate with a Subagent

```
Delegate to the model-evaluator agent to analyze the model performance and diagnose any issues
```

> **Observe:** Another [subagent](https://code.claude.com/docs/en/sub-agents) — this one compares train/val/test metrics and diagnoses overfitting. Each agent is a `.md` file with its own instructions.

---

### Step 7: Autonomous Hyperparameter Tuning

```
The RMSE is high. Run 5 hyperparameter tuning trials, varying learning_rate and max_depth. Log each trial to MLflow.
```

> **Observe:** "Autopilot mode" — Claude iterates through 5 trials autonomously, logging each to MLflow. What other hyperparameters would you tune? What strategy would you use at scale?

**While it runs:** Open the MLflow experiment — watch the runs appear. Compare them side-by-side.

---

### Step 8: Persist Knowledge with Memory

```
Remember that the best hyperparameters were learning_rate=0.1, max_depth=6, and that log-transforming the target improved RMSE by 15%
```

> **Observe:** [Memory](https://code.claude.com/docs/en/memory) persists across sessions. Next time, ask "What hyperparameters worked best?" and Claude recalls it.

---

### Step 9: Commit and Push

```
Commit and push these changes
```

> **Observe:** Claude stages the right files and writes a commit message with experiment context — it understands the ML workflow.

---

### Step 10: Safe Experimentation with Checkpoints

```
Let me try adding polynomial features to the model
```

After Claude makes changes, press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot before every edit. Roll back instantly — perfect for ML experimentation.

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
What's the average number of items per order?
Show me the top 10 most reordered products
Search for recent papers on demand forecasting with gradient boosting
Create a GitHub issue for "Investigate feature interactions for demand model"
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP not connecting | `claude mcp list`, verify token and URL |
| MLflow experiment not found | Check experiment name and user permissions |
| Training OOM | Reduce sample size or aggregate in Spark first |
| Model not improving | Check for data leakage, try different features |

---

## Features Cheat Sheet

| Feature | What It Does | Where It Lives | Docs |
|---------|--------------|----------------|------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) | Project context, auto-loaded | `CLAUDE.md` | [Memory](https://code.claude.com/docs/en/memory) |
| [Slash Commands](https://code.claude.com/docs/en/slash-commands) | `/train`, `/evaluate`, `/tune` | `.claude/commands/` | [Commands](https://code.claude.com/docs/en/slash-commands) |
| [Skills](https://code.claude.com/docs/en/skills) | Auto-triggered (MLflow logging, tuning) | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| [Subagents](https://code.claude.com/docs/en/sub-agents) | Feature engineer, model evaluator, experiment analyzer | `.claude/agents/` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| [MCP](https://code.claude.com/docs/en/mcp) | Databricks, GitHub, search, docs | Connected servers | [MCP](https://code.claude.com/docs/en/mcp) |
| [Hooks](https://code.claude.com/docs/en/hooks) | Auto-format Python with Ruff | `.claude/settings.json` | [Hooks](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](https://code.claude.com/docs/en/overview) | `Esc+Esc` to rewind changes | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
