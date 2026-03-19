# Demo: Data Science with Claude Code

> **45 min** | XGBoost + MLflow + Feature Engineering | [Full Claude Code Docs](https://code.claude.com/docs/en/overview)

---

## Quick Reference — Prompts to Type

| Step | Prompt | Feature Shown |
|------|--------|---------------|
| 0 | `Setup demo data in {catalog}.{schema}` | [Skills](https://code.claude.com/docs/en/skills) |
| 1 | `What MCP servers do you have access to?` | [MCP](https://code.claude.com/docs/en/mcp) |
| 2 | `Using the Databricks MCP, what does the schema of {catalog}.{schema}.orders look like?` | MCP (live query) |
| 3 | `Delegate to the feature-engineer agent to design features...` *(see below)* | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 4 | `Using context7, show me XGBoost documentation for early stopping` | MCP (docs lookup) |
| 5 | `Create an XGBoost demand forecasting model...` *(see below)* | Code generation + [Hooks](https://code.claude.com/docs/en/hooks) |
| 6 | `Create and upload a combined training script on Databricks and run it` | CLI automation |
| 7 | `Delegate to the model-evaluator agent to analyze performance` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| 8 | `Run 5 hyperparameter tuning trials, varying learning_rate and max_depth` | Autonomous iteration |
| 9 | `Remember that the best hyperparameters were learning_rate=0.1, max_depth=6` | [Memory](https://code.claude.com/docs/en/memory) |
| 10 | `Commit and push these changes` | Git workflow |
| 11 | *Press `Esc` twice* | [Checkpoints](https://code.claude.com/docs/en/overview) |

---

## Prerequisites

> **First time?** Follow the [Setup Guide](../../SETUP.md) to install Claude Code, Databricks CLI, and MCP.

1. Terminal open in `demos/data-science/`
2. `claude mcp list` — Databricks and GitHub servers connected
3. Databricks workspace open in browser (MLflow UI ready)
4. Fresh session: start `claude`, then type `/clear`

---

## Walkthrough

### Step 0: Start Claude Code & Setup Demo Data

```bash
cd demos/data-science
claude .
```

```
My catalog is {catalog} and my schema is {schema}. My Databricks CLI profile is {profile_name}. Only operate on this profile's workspace. Remember this for the rest of our session.
```

Then: `Setup demo data in my catalog and schema`

> **Observe:** Claude matched your intent to the skill's keywords. That's [Skills](https://code.claude.com/docs/en/skills).

---

### Step 1: Verify MCP

```
What MCP servers do you have access to?
```

> **Observe:** These are live tool connections — Databricks, GitHub, docs, and more. No API code needed.

---

### Step 2: Explore Live Data

```
Using the Databricks MCP, what does the schema of {catalog}.{schema}.orders look like?
```

Then: `What's the distribution of orders by day of week?`

> **Observe:** That's your *live* Databricks workspace queried via MCP — schemas, samples, aggregations, all through natural language. Try your own: "How many unique products?" "What's the reorder rate?"

---

### Step 3: Feature Engineering with a Subagent

```
Delegate to the feature-engineer agent to design features for a demand forecasting model using the demo data and create a notebook with the feature engineering code (e.g., demos/data-science/src/generated-feature_engineering.py)
```

> **Observe:** Claude delegates to a [subagent](https://code.claude.com/docs/en/sub-agents) — notice it suggests cyclical encoding and log transforms. That's the agent's prompt guiding its reasoning.

---

### Step 4: Look Up Documentation

```
Using context7, show me XGBoost documentation for early stopping
```

> **Observe:** Context7 fetches *current* library docs via [MCP](https://code.claude.com/docs/en/mcp) — not stale training data. Try it with MLflow too.

---

### Step 5: Build the Training Pipeline

```
Create an XGBoost demand forecasting model that:
- Reads from {catalog}.{schema}.orders and order_products
- Implements the features we discussed
- Uses proper train/val/test splits
- Logs everything to MLflow
- Use a small sample for speed
```

> **Observe:** Claude builds a complete pipeline, and each `.py` gets auto-formatted — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) firing Ruff.

---

### Step 6: Train the Model

```
Create and upload a combined training script (features and training) on Databricks and run it as a Job.
```

> **Observe:** Claude uploads the notebook, triggers a run, and returns the URL. Open the MLflow UI — can everyone find the experiment?

---

### Step 7: Evaluate with a Subagent

```
Delegate to the model-evaluator agent to analyze the model performance and diagnose any issues
```

> **Observe:** Another [subagent](https://code.claude.com/docs/en/sub-agents) — compares train/val/test metrics and diagnoses overfitting. Each agent is a `.md` file with its own instructions.

---

### Step 8: Autonomous Hyperparameter Tuning

```
The RMSE is high. Run 5 hyperparameter tuning trials, varying learning_rate and max_depth. Log each trial to MLflow.
```

> **Observe:** "Autopilot mode" — Claude iterates autonomously, logging each trial to MLflow. Open the experiment to watch runs appear.

---

### Step 9: Persist Knowledge with Memory

```
Remember that the best hyperparameters were learning_rate=0.1, max_depth=6, and that log-transforming the target improved RMSE by 15%
```

> **Observe:** [Memory](https://code.claude.com/docs/en/memory) persists across sessions. Next time, ask "What hyperparameters worked best?" and Claude recalls it.

---

### Step 10: Commit and Push

```
Commit and push these changes
```

> **Observe:** Claude stages the right files and writes a commit message with experiment context — it understands the ML workflow.

---

### Step 11: Safe Experimentation with Checkpoints

```
Let me try adding polynomial features to the model
```

After Claude makes changes, press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot before every edit. Roll back instantly — perfect for ML experimentation.

**Bonus:** Type `/compact` to summarize a long conversation.

---

> **Reflect with the group:** What surprised you most? What would you try first in your own workflow?

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

| Feature | Where It Lives | Docs |
|---------|----------------|------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) — project context | `CLAUDE.md` | [Memory](https://code.claude.com/docs/en/memory) |
| [Skills](https://code.claude.com/docs/en/skills) — `/train`, `/evaluate`, `/tune`, `/create-pr` | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| [Subagents](https://code.claude.com/docs/en/sub-agents) — feature engineer, model evaluator, experiment analyzer | `.claude/agents/` | [Subagents](https://code.claude.com/docs/en/sub-agents) |
| [MCP](https://code.claude.com/docs/en/mcp) — Databricks, GitHub, search, docs | Connected servers | [MCP](https://code.claude.com/docs/en/mcp) |
| [Hooks](https://code.claude.com/docs/en/hooks) — auto-format with Ruff | `.claude/settings.json` | [Hooks](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](https://code.claude.com/docs/en/overview) — `Esc+Esc` to rewind | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
