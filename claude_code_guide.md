# Claude Code Feature Guide for Databricks

> Every feature below is demonstrated live in the [data-engineering](demos/data-engineering/) and [data-science](demos/data-science/) demos.

---

## At a Glance

| Feature | Trigger | Context Cost | Databricks Example |
|---------|---------|-------------|-------------------|
| [CLAUDE.md](#1-claudemd--project-memory) | **Auto** — every turn | **High** — full file loaded into every message | Catalog/schema, conventions |
| [Slash Commands](#2-slash-commands) | **Manual** — you type `/cmd` | **Low** — injected once when invoked | `/deploy` runs bundle deploy |
| [Skills](#3-skills) | **Auto** — Claude matches intent | **Low** — injected once when matched | "setup demo data" → SQL gen |
| [Subagents](#4-subagents) | **Manual** — "delegate to..." | **Zero** — runs in isolated context | Spark optimizer reviews code |
| [MCP Servers](#5-mcp-servers) | **Auto** — Claude calls as needed | **Low** — tool defs at startup, results per-call | Query Unity Catalog via SQL |
| [Hooks](#6-hooks) | **Auto** — fires on events | **Zero** — runs outside Claude (shell) | Ruff format on every `.py` write |
| [Checkpoints](#7-checkpoints) | **Manual** — `Esc + Esc` | **Zero** — stored in git refs | Rewind failed DLT experiment |
| [Headless Mode](#8-headless-mode) | **Manual** — `claude -p "..."` | **N/A** — separate invocation | Pipe job output for analysis |

> **Context cost** = how much of Claude's limited context window a feature consumes. High-cost features reduce how much conversation history Claude can "remember." Keep CLAUDE.md lean; prefer low/zero-cost features for heavy content.

---

## 1. CLAUDE.md — Project Memory

[Docs](https://code.claude.com/docs/en/memory)

A markdown file auto-loaded into every conversation. Use it to give Claude persistent context about your project — what catalog to use, how to deploy, what conventions to follow.

**Where it lives:** `CLAUDE.md` at project root (and optionally in subdirectories — Claude merges them hierarchically).

**Databricks example** — tell Claude your environment once, use it forever:

```markdown
## Environment
- Catalog: `main`
- Schema: `grocery`
- Compute: Serverless (use `%pip install` + `dbutils.library.restartPython()` for non-standard libs)
- Deploy: `databricks bundle deploy --target dev`
```

**Tips:**
- Keep it under 500 lines — everything here consumes context on every turn
- Put stable facts here (catalog, schema, team conventions), not session-specific notes
- Subdirectory CLAUDE.md files override parent settings for that scope

---

## 2. Slash Commands

[Docs](https://code.claude.com/docs/en/slash-commands)

Pre-written prompts stored as `.md` files that you trigger manually. Think of them as team-shared macros.

**Where they live:** `.claude/commands/`

**Databricks examples from this repo:**

| Command | What It Does |
|---------|-------------|
| `/deploy` | Validates and deploys the DABs bundle |
| `/run-job` | Triggers a Lakeflow Job and monitors it |
| `/validate-data` | Runs data quality checks on output tables |
| `/train` | Trains a model with MLflow logging |
| `/create-pr` | Creates a PR via the GitHub MCP |

**How to create one:** Add a markdown file to `.claude/commands/`. The filename becomes the command name. The file content becomes the prompt.

```markdown
<!-- .claude/commands/deploy.md -->
Run `databricks bundle validate` first.
If valid, run `databricks bundle deploy --target dev`.
Report the deploy URL when done.
```

---

## 3. Skills

[Docs](https://code.claude.com/docs/en/skills)

Domain expertise that Claude discovers and activates *automatically* based on your intent. You don't invoke skills — Claude reads their trigger keywords and decides when to use them.

**Where they live:** `.claude/skills/`

**How they differ from slash commands:** Slash commands are manual (`/deploy`). Skills are automatic — say "setup demo data" and Claude finds and follows the skill without you pointing to it.

**Databricks examples from this repo:**

| Skill | Triggers When You Say... | What It Does |
|-------|-------------------------|-------------|
| `setup-demo-data` | "setup demo data", "create mock data" | Generates 5 tables via SQL |
| `data-quality-check` | "check data quality", "validate output" | Runs null/duplicate/freshness checks |
| `spark-optimization` | "optimize", "slow job" | Applies Spark tuning patterns |
| `mlflow-logging` | "log to MLflow", "track experiment" | Sets up proper MLflow logging |
| `hyperparameter-tuning` | "tune", "grid search" | Runs structured HP search with logging |

**How to create one:** Add a `.md` file to `.claude/skills/` with trigger keywords and step-by-step instructions. Claude reads the metadata and activates the skill when it detects a match.

---

## 4. Subagents

[Docs](https://code.claude.com/docs/en/sub-agents)

Specialized Claude instances with their own isolated context. Claude delegates to them for focused analysis. Each subagent has its own system prompt defining its expertise.

**Where they live:** `.claude/agents/`

**Databricks examples from this repo:**

| Agent | Expertise | Example Prompt |
|-------|-----------|---------------|
| `spark-optimizer` | PySpark performance (skew, shuffle, caching) | "Delegate to the spark-optimizer to review my code" |
| `feature-engineer` | ML feature design for demand forecasting | "Delegate to the feature-engineer to design features" |
| `model-evaluator` | Train/val/test metric analysis, overfitting diagnosis | "Delegate to the model-evaluator to analyze performance" |
| `code-reviewer` | Best practices, Unity Catalog conventions | "Delegate to the code-reviewer to check my pipeline" |
| `job-debugger` | Lakeflow Job failure diagnosis | "Delegate to the job-debugger to investigate the failure" |
| `experiment-analyzer` | Compare MLflow runs, find best configurations | "Delegate to the experiment-analyzer to compare my runs" |

**Key pattern:** Subagents analyze (read-only) while the main Claude executes (writes code). This keeps control in one place while leveraging specialized reasoning.

---

## 5. MCP Servers

[Docs](https://code.claude.com/docs/en/mcp)

Live connections to external tools and services. Claude calls them automatically when it needs real-time data. MCP (Model Context Protocol) is an open standard — any tool that implements it can plug into Claude Code.

**Configuration:** Set up via `claude mcp add` (see `.claude/mcp-config.example.json` for reference)

**Servers used in this repo:**

| Server | What It Enables | Example |
|--------|----------------|---------|
| **uc-function-mcp** | Query Databricks via SQL | "Show me the schema of orders" |
| **github** | PRs, issues, repos | "Create a PR for these changes" |
| **context7** | Up-to-date library docs | "Show me XGBoost early stopping docs" |
| **memory** | Persist facts across sessions | "Remember the best hyperparameters" |
| **brave-search** | Web search | "Search for Spark partition pruning tips" |
| **obsidian** | Note-taking | "Document this pipeline in my vault" |

**Why this matters for Databricks:** The `uc-function-mcp` server lets Claude query your Unity Catalog directly. No copy-pasting schemas, no describing table structures — Claude sees your live data.

---

## 6. Hooks

[Docs](https://code.claude.com/docs/en/hooks)

Shell commands that fire automatically on lifecycle events. They're deterministic (not AI) — just scripts that run on triggers.

**Where they live:** `.claude/settings.json`

**Events:**
- `PreToolUse` — before Claude uses a tool (can block with non-zero exit)
- `PostToolUse` — after Claude uses a tool
- `Stop` — when Claude finishes a response

**Databricks examples from this repo:**

```jsonc
// .claude/settings.json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "[ \"${CLAUDE_FILE_PATH##*.}\" = \"py\" ] && ruff format \"$CLAUDE_FILE_PATH\" || true"
          },
          {
            "type": "command",
            "command": "[ \"${CLAUDE_FILE_PATH##*.}\" = \"py\" ] && ruff check --fix \"$CLAUDE_FILE_PATH\" || true"
          }
        ]
      }
    ]
  }
}
```

**Other Databricks-relevant hook ideas:**
- `PreToolUse` on `Bash(git commit)` — run `databricks bundle validate` before every commit
- `PostToolUse` on `Write(*.py)` — run `mypy` or `pylint` on new Spark code
- `Stop` — post a Slack notification when a long training run finishes

**Key distinction from subagents:** Hooks are deterministic automation ("always do X"). Subagents are intelligent delegation ("analyze this and advise me").

---

## 7. Checkpoints

[Docs](https://code.claude.com/docs/en/overview)

Automatic file snapshots before every edit, stored in local Git refs. Press `Esc + Esc` to open the checkpoint menu and roll back instantly.

**Databricks use case:** You ask Claude to add a gold layer to your DLT pipeline. It doesn't work out. Press `Esc + Esc`, pick the checkpoint before the change, and you're back instantly — no `git stash`, no `git checkout .`.

**Limitations:** Checkpoints only cover file changes. They can't undo external side effects like Databricks job runs, table writes, or MLflow experiment logs.

---

## 8. Headless Mode

[Docs](https://code.claude.com/docs/en/cli)

Run Claude non-interactively from the terminal. Pipe input in, get structured output back. Useful for CI/CD, automation scripts, and batch processing.

```bash
# Review a Spark job for performance issues
cat src/etl_daily_metrics.py | claude -p "Review this PySpark code for performance"

# Analyze a failed job run
databricks jobs get-run 12345 --output JSON | claude -p "Why did this job fail?"

# Generate a commit message from staged changes
git diff --staged | claude -p "Write a concise commit message"
```

---

## Putting It All Together

Here's how the features compose in a typical Databricks workflow:

```
CLAUDE.md defines your catalog, schema, and conventions
        |
        v
You say "setup demo data" -----> Skill activates, generates SQL
        |
        v
Claude queries Unity Catalog --> MCP server runs live SQL
        |
        v
You say "/deploy" -------------> Slash command deploys the bundle
        |
        v
Claude writes Python ----------> Hook auto-formats with Ruff
        |
        v
"Review my Spark code" --------> Subagent analyzes for performance
        |
        v
Something goes wrong? ---------> Checkpoint rolls back instantly
```

---

## File Layout (Inside Each Demo)

```
demos/data-engineering/        # or demos/data-science/
├── CLAUDE.md                  # Project memory (auto-loaded)
├── README.md                  # Live demo script
└── .claude/
    ├── commands/              # Slash commands: /deploy, /run-job, /train, etc.
    ├── skills/                # Auto-triggered: setup-demo-data, data-quality, etc.
    ├── agents/                # Subagents: spark-optimizer, feature-engineer, etc.
    ├── settings.json          # Hooks configuration
    └── mcp-config.example.json  # MCP server reference template
```

---

*For the full official documentation, visit [code.claude.com/docs](https://code.claude.com/docs/en/overview)*
