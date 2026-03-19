# Claude Code Feature Guide for Databricks

> Quick reference for all Claude Code features used in this workshop. Every feature is demonstrated live across the [five demo tracks](demos/).

---

## At a Glance

| Feature | How It Works | Context Cost | Databricks Example | Docs |
|---------|-------------|-------------|-------------------|------|
| [CLAUDE.md](#claudemd) | **Auto** — loaded every turn | **High** — full file in context | Catalog, schema, conventions | [Docs](https://code.claude.com/docs/en/memory) |
| [Skills](#skills) | **User-invoked** (`/cmd`) or **auto-triggered** by intent | **Low** — loaded once when matched | `/deploy` runs bundle deploy; "setup demo data" auto-triggers | [Docs](https://code.claude.com/docs/en/skills) |
| [Subagents](#subagents) | **Manual** — "delegate to..." | **Zero** — isolated context | Spark optimizer reviews PySpark code | [Docs](https://code.claude.com/docs/en/sub-agents) |
| [MCP Servers](#mcp-servers) | **Auto** — Claude calls as needed | **Medium** — tool defs per turn | Query Unity Catalog via SQL | [Docs](https://code.claude.com/docs/en/mcp) |
| [Hooks](#hooks) | **Auto** — fires on events | **Zero** — shell commands | Ruff format on every `.py` write | [Docs](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](#checkpoints) | **Manual** — `Esc + Esc` | **Zero** — git refs | Rewind a failed DLT experiment | [Docs](https://code.claude.com/docs/en/checkpointing) |
| [Headless / CLI](#headless-mode) | **Manual** — `claude -p "..."` | **N/A** — separate invocation | Pipe job output for analysis | [Docs](https://code.claude.com/docs/en/cli-reference) |

> **Context cost** = how much of Claude's context window a feature consumes. Keep CLAUDE.md lean; prefer low/zero-cost features for heavy content.

---

## CLAUDE.md

[Full docs](https://code.claude.com/docs/en/memory)

Markdown file auto-loaded into every conversation. Gives Claude persistent project context.

```markdown
## Environment
- Catalog: `main`, Schema: `grocery`
- Compute: Serverless — use `%pip install` + `dbutils.library.restartPython()` for non-standard libs
- Deploy: `databricks bundle deploy --target dev`
```

- Lives at project root (subdirectory CLAUDE.md files merge hierarchically)
- Keep under 500 lines — everything here costs context on every turn
- Put stable facts here (catalog, schema, conventions), not session-specific notes
- See also: [Auto Memory](https://code.claude.com/docs/en/memory) — Claude automatically persists learnings in `~/.claude/projects/` across sessions

---

## Skills

[Full docs](https://code.claude.com/docs/en/skills)

Skills replace the old "slash commands" (`.claude/commands/`). A skill is a directory at `.claude/skills/{name}/SKILL.md` with instructions and optional supporting files.

**Two invocation modes:**

| Mode | How | Example |
|------|-----|---------|
| **User-invoked** | Type `/name` | `/deploy`, `/run-tests`, `/todo` |
| **Auto-triggered** | Claude matches intent from description/keywords | "setup demo data" triggers `setup-demo-data` skill |

**Skills in this repo:**

| Demo | User-Invoked | Auto-Triggered |
|------|-------------|----------------|
| Data Engineering | `/deploy`, `/run-job`, `/validate-data`, `/create-pr` | data-quality-check, setup-demo-data |
| Data Science | `/train`, `/evaluate`, `/tune`, `/create-pr` | mlflow-logging, hyperparameter-tuning, setup-demo-data |
| Software Engineering (Node.js) | `/deploy-app`, `/run-tests`, `/lint`, `/create-pr` | api-testing, setup-demo-data, supply-track-sdk |
| Software Engineering (Java) | `/run-tests`, `/create-pr` | supply-track-sdk |
| Productivity | `/todo`, `/draft-reply` | email-parser, message-drafter, slide-creator, spreadsheet-creator |

**Bundled documentation:** Skills can include supporting files (API references, examples). The `supply-track-sdk` skill bundles a full API reference for a fictional SDK Claude was never trained on — teaching it a proprietary library on the fly.

**SKILL.md frontmatter:**

```yaml
---
name: deploy
description: Deploy the DABs bundle to Databricks
# Optional:
user-invocable: true          # show in /menu (default: true)
disable-model-invocation: true # only user can trigger (default: false)
allowed-tools: Bash, Read      # restrict available tools
context: fork                  # run in isolated subagent
---
```

---

## Subagents

[Full docs](https://code.claude.com/docs/en/sub-agents)

Specialized Claude instances with isolated context. Claude delegates to them for focused analysis.

**Where they live:** `.claude/agents/{name}.md`

**Subagents in this repo:**

| Demo | Agents |
|------|--------|
| Data Engineering | spark-optimizer, job-debugger, code-reviewer |
| Data Science | feature-engineer, model-evaluator, experiment-analyzer |
| Software Engineering (Node.js) | code-reviewer, api-debugger, security-auditor |
| Software Engineering (Java) | code-reviewer, security-auditor |
| Productivity | *(none)* |

**Invoke:** "Delegate to the spark-optimizer to review my code"

**Agent frontmatter:**

```yaml
---
name: spark-optimizer
description: Analyze PySpark code for performance improvements
tools: Read, Glob, Grep        # tool allowlist (optional)
model: sonnet                   # model override (optional)
---
```

---

## MCP Servers

[Full docs](https://code.claude.com/docs/en/mcp)

Live connections to external tools. Claude calls them automatically when it needs real-time data.

**Config:** `claude mcp add` or `.claude/mcp-config.example.json`

| Server | Purpose | Example |
|--------|---------|---------|
| **uc-function-mcp** | Query Databricks via SQL | "Show me the schema of orders" |
| **github** | PRs, issues, repos | "Create a PR for these changes" |
| **context7** | Up-to-date library docs | "Show me XGBoost early stopping docs" |
| **memory** | Persist facts across sessions | "Remember the best hyperparameters" |
| **brave-search** | Web search | "Search for Spark partition pruning tips" |
| **confluence** | Documentation | "Create a Confluence page for this pipeline" |

**Verify:** `claude mcp list`

---

## Hooks

[Full docs](https://code.claude.com/docs/en/hooks) | [Guide](https://code.claude.com/docs/en/hooks-guide)

Shell commands that fire automatically on lifecycle events. Deterministic automation — not AI.

**Where they live:** `.claude/settings.json`

**Key events:**

| Event | When | Can Block? |
|-------|------|-----------|
| `PreToolUse` | Before tool execution | Yes (exit non-zero) |
| `PostToolUse` | After tool succeeds | No |
| `UserPromptSubmit` | User submits prompt | Yes (exit 2) |
| `Stop` | Claude finishes responding | Yes (exit 2) |
| `SessionStart` | New session / resume / clear | No |

**This repo uses:**

```jsonc
// .claude/settings.json — auto-format Python on every write
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write|Edit",
      "hooks": [{
        "type": "command",
        "command": "[ \"${CLAUDE_FILE_PATH##*.}\" = \"py\" ] && ruff format \"$CLAUDE_FILE_PATH\" || true"
      }]
    }]
  }
}
```

Other demos use Prettier (JS/TS) and google-java-format (Java) with the same pattern.

---

## Checkpoints

[Full docs](https://code.claude.com/docs/en/checkpointing)

Automatic file snapshots before every edit, stored in local git refs. Press `Esc + Esc` to open the menu and roll back instantly.

- Covers file changes only — can't undo external side effects (job runs, table writes, MLflow logs)
- No `git stash` or `git checkout .` needed

---

## Headless Mode

[Full docs](https://code.claude.com/docs/en/cli-reference)

Run Claude non-interactively from the terminal. Useful for CI/CD and automation.

```bash
# Review a Spark job
cat src/etl_daily_metrics.py | claude -p "Review this PySpark code for performance"

# Analyze a failed job run
databricks jobs get-run 12345 --output JSON | claude -p "Why did this job fail?"
```

Key flags: `--output-format json`, `--max-turns`, `--allowedTools`

---

## File Layout (Inside Each Demo)

```
demos/{track}/
├── CLAUDE.md                  # Project context (auto-loaded)
├── README.md                  # Live demo script
└── .claude/
    ├── skills/                # User-invoked (/deploy) + auto-triggered (setup-demo-data)
    │   └── {name}/SKILL.md    # Skill instructions + optional supporting files
    ├── agents/                # Subagents: spark-optimizer, code-reviewer, etc.
    │   └── {name}.md
    ├── settings.json          # Hooks configuration
    └── mcp-config.example.json  # MCP server reference (where applicable)
```

---

*Full official docs: [code.claude.com/docs](https://code.claude.com/docs/en/overview) | [Features overview](https://code.claude.com/docs/en/features-overview) | [Built-in commands](https://code.claude.com/docs/en/commands)*
