# Databricks + Claude Code Hackathon

Hands-on workshop introducing **"Vibe Coding"** — AI-assisted development where Claude Code works alongside engineers to rapidly build data solutions on Databricks.

---

## What Is This?

A practical workshop teaching AI-assisted development with Claude Code and Databricks. Participants will learn to leverage Claude Code with MCP integrations to accelerate data engineering and data science workflows.

### Why?

- **Productivity Gains** — Demonstrate how AI-assisted development speeds up common data tasks
- **Skill Building** — Practical knowledge of Claude Code, MCP servers, and Databricks workflows
- **Hands-On Experience** — Real coding challenges using production-grade tools

---

## Two Tracks

| Track | Focus | Technology Stack | Key Tasks |
|-------|-------|------------------|-----------|
| **Data Engineering** | Job Orchestration & CI/CD | DABs, PySpark, Lakeflow, Unity Catalog | Create jobs, optimize workflows, auto-PRs |
| **Data Science** | Experimentation & Logging | MLflow, XGBoost, Feature Engineering | Train models, track experiments, log results |

### Track Details

**Data Engineering**: Build an Automated Product Reorder Alert Pipeline
- Create ETL jobs with PySpark
- Deploy with Databricks Asset Bundles (DABs)
- Use Delta Live Tables for streaming
- Orchestrate with Lakeflow Jobs

**Data Science**: Build a Demand Forecasting Model
- Engineer features from order history
- Train XGBoost regression models
- Track experiments with MLflow
- Optimize hyperparameters

---

## Project Structure

```
databricks-claude-code-hackathon/
├── README.md              # This file
├── CLAUDE.md              # Project context for Claude Code
├── demos/                 # Reference implementations
│   ├── data-engineering/  # DABs + PySpark + DLT demo
│   │   ├── CLAUDE.md      # Project-specific context
│   │   ├── README.md      # Live demo script
│   │   ├── .claude/       # Commands, skills, agents, hooks
│   │   └── src/           # Generated code (created live in demo)
│   └── data-science/      # MLflow + XGBoost demo
│       ├── CLAUDE.md      # Project-specific context
│       ├── README.md      # Live demo script
│       ├── .claude/       # Commands, skills, agents, hooks
│       └── src/           # Generated code (created live in demo)
└── hackathon/             # Problem statements & instructions
    ├── instructions.md
    ├── data-engineering-problem.md
    └── data-science-problem.md
```

---

## Quick Start

### For Participants

```bash
# 1. Copy demo template to your workspace
cp -r demos/data-engineering participants/team-{name}/
# OR
cp -r demos/data-science participants/team-{name}/

# 2. Navigate to your team folder
cd participants/team-{name}/

# 3. Update CLAUDE.md with your team schema
# Replace {catalog} and {schema} with your assigned values

# 4. Read the problem statement
# hackathon/data-engineering-problem.md OR
# hackathon/data-science-problem.md

# 5. Start Claude Code
claude .

# 6. Setup demo data
# Say: "Setup demo data in {catalog}.{schema}"
```

### For Facilitators

```bash
# View demo scripts
cat demos/data-engineering/README.md
cat demos/data-science/README.md

# Each demo README contains step-by-step presenter notes
```

---

## Demo Data

Both tracks use the same grocery store dataset. Run once to create all tables:

```
Setup demo data in {catalog}.{schema}
```

This creates:

| Table | Description | Row Count |
|-------|-------------|-----------|
| `orders` | Order transactions | ~10,000 |
| `order_products` | Order line items | ~35,000 |
| `products` | Product catalog | 50 |
| `departments` | Product departments | 21 |
| `aisles` | Product aisles | 50 |

**Key columns:**
- `orders`: order_id, user_id, order_dow (0-6), order_hour_of_day (0-23)
- `order_products`: order_id, product_id, add_to_cart_order, reordered (0/1)
- `products`: product_id, product_name, aisle_id, department_id

---

## Expected Outcomes

By the end of this hackathon, participants will:

1. **Understand Vibe Coding** — Effectively prompt and collaborate with Claude Code
2. **Use MCP Integrations** — Connect Claude to Databricks, GitHub, and documentation tools
3. **Master Claude Code Features** — Commands, skills, agents, hooks, and CLAUDE.md
4. **Build Working Solutions** — Complete a data engineering or data science challenge
5. **Share Learnings** — Demo and discuss approaches (focus on learning, not competition)

---

## Claude Code Features Used

| Feature | Location | Description |
|---------|----------|-------------|
| **CLAUDE.md** | Project root | Auto-loaded project context and rules |
| **Slash Commands** | `.claude/commands/` | Custom commands like `/deploy`, `/train` |
| **Skills** | `.claude/skills/` | Auto-triggered for keywords like "setup demo data" |
| **Agents** | `.claude/agents/` | Specialized subagents for complex tasks |
| **Hooks** | `.claude/settings.json` | Auto-run on events (e.g., format on save) |
| **MCP Servers** | External | Databricks, GitHub, Obsidian, Brave Search, Context7, Memory |

---

## Resources

### Hackathon Materials
- [Instructions](hackathon/instructions.md) - Getting started guide
- [Data Engineering Problem](hackathon/data-engineering-problem.md) - DE track challenge
- [Data Science Problem](hackathon/data-science-problem.md) - DS track challenge

### Demo References
- [Data Engineering Demo Script](demos/data-engineering/README.md) - Step-by-step walkthrough
- [Data Science Demo Script](demos/data-science/README.md) - Step-by-step walkthrough

### Documentation
- [Claude Code Guide](claude_code_guide.md) - Features reference
- [Root CLAUDE.md](CLAUDE.md) - Project-wide context

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP not connecting | Run `claude mcp list`, check authentication |
| Catalog not found | Run `SHOW CATALOGS` to see available catalogs |
| Permission denied | Check Unity Catalog grants on tables |
| Missing Python libraries | Add `%pip install xgboost scikit-learn matplotlib seaborn` + `dbutils.library.restartPython()` at notebook start |
| Job fails on serverless | Ensure library installation cells are at the top of notebook |
| Context too long | Use `/compact` to summarize conversation |

---

## Questions?

Contact the event organizers or check the Slack channel.
