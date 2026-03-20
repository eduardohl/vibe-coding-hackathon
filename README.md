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

## Five Tracks

| Track | Focus | Technology Stack | Key Tasks |
|-------|-------|------------------|-----------|
| **Productivity** | Daily Task Automation | Claude Code skills only — no infra | Parse emails, draft messages, create slides & spreadsheets |
| **Data Engineering** | Job Orchestration & CI/CD | DABs, PySpark, Lakeflow, Unity Catalog | Create jobs, optimize workflows, auto-PRs |
| **Data Science** | Experimentation & Logging | MLflow, XGBoost, Feature Engineering | Train models, track experiments, log results |
| **Software Engineering** | Full-Stack Apps & Testing | Databricks Apps, Express, Lakebase | Build apps, write tests, security audit |
| **Software Engineering (Java)** | Testing & Proprietary Libraries | Spring Boot, JUnit 5, H2 — no cloud | Build APIs, teach Claude proprietary SDKs, automated testing |

### Track Details

**Productivity** *(best as the first demo — zero setup)*: Turn a Messy Email into Organized Deliverables
- Parse an email into a prioritized todo checklist
- Draft professional messages to colleagues
- Create an HTML slide deck and a CSV spreadsheet
- Write a Python script to answer a technical question
- No Databricks, no MCP, no tokens — just Claude Code

**Data Engineering**: Build an Automated Product Reorder Alert Pipeline
- Create ETL jobs with PySpark
- Deploy with Declarative Automation Bundles (DABs)
- Use Lakeflow Declarative Pipelines for streaming
- Orchestrate with Lakeflow Jobs

**Data Science**: Build a Demand Forecasting Model
- Engineer features from order history
- Train XGBoost regression models
- Track experiments with MLflow
- Optimize hyperparameters

**Software Engineering**: Build a Supply Chain Inventory Management App
- Read a casual conversation and turn it into a working app
- Scaffold an Express.js app with plain HTML frontend (no build step)
- Connect to Lakebase (Postgres-compatible) for persistence
- Teach Claude a proprietary SDK (SupplyTrackSDK) via bundled docs
- Write unit tests and API tests with Jest
- Run security audits (OWASP Top 10)
- Deploy with Databricks Apps

**Software Engineering (Java)**: Build a Medical Supply Inventory Service
- Scaffold a Spring Boot REST API with H2 database
- Teach Claude a proprietary SDK (SupplyTrackSDK — Java version) via bundled docs
- Write JUnit 5 tests with MockMvc and Mockito
- Run code review and security audit with subagents
- No cloud, no MCP, no tokens — just Java + Maven

---

## Project Structure

```
databricks-claude-code-hackathon/
├── README.md              # This file
├── CLAUDE.md              # Project context for Claude Code
├── SETUP.md               # Workshop setup guide (Mac + Windows)
├── claude_code_guide.md   # Claude Code features reference
├── workshop-permissions.md # Required Databricks permissions
└── demos/                 # Reference implementations
    ├── data-engineering/  # DABs + PySpark + Lakeflow Pipelines demo
    │   ├── CLAUDE.md      # Project-specific context
    │   ├── README.md      # Live demo script
    │   ├── .claude/       # Skills, agents, hooks
    │   └── src/           # Generated code (created live in demo)
    ├── data-science/      # MLflow + XGBoost demo
    │   ├── CLAUDE.md      # Project-specific context
    │   ├── README.md      # Live demo script
    │   ├── .claude/       # Skills, agents, hooks
    │   └── src/           # Generated code (created live in demo)
    ├── software-engineering/   # Databricks Apps + Lakebase demo
    │   ├── CLAUDE.md      # Project-specific context
    │   ├── README.md      # Live demo script
    │   ├── .claude/       # Skills, agents, hooks (+ SupplyTrackSDK docs)
    │   └── src/           # App code (generated live in demo)
    ├── software-engineering-java/  # Spring Boot + JUnit 5 demo (no cloud)
    │   ├── CLAUDE.md      # Project-specific context
    │   ├── README.md      # Live demo script
    │   ├── .claude/       # Skills, agents, hooks (+ SupplyTrackSDK docs)
    │   └── src/           # App code (generated live in demo)
    └── productivity/      # Email → deliverables demo (no infra)
        ├── CLAUDE.md      # Project-specific context
        ├── README.md      # Live demo script
        ├── .claude/       # Skills, hooks
        └── src/           # Sample email + generated output
```

---

## Prerequisites

Follow the **[Setup Guide](SETUP.md)** — installs Claude Code, Databricks CLI, and MCP in ~10 minutes.

**Quick check — you're ready when:**
```bash
claude --version        # Claude Code installed
databricks -v           # Databricks CLI installed
claude mcp list         # MCP servers connected
```

---

## Quick Start

### For Participants

```bash
# 1. Create your team folder and copy the demo template
mkdir -p participants/team-{name}
cp -r demos/data-engineering/* participants/team-{name}/
# OR
cp -r demos/data-science/* participants/team-{name}/
# OR
cp -r demos/software-engineering/* participants/team-{name}/
# OR
cp -r demos/software-engineering-java/* participants/team-{name}/

# 2. Navigate to your team folder
cd participants/team-{name}/

# 3. Update CLAUDE.md in YOUR TEAM FOLDER (not the repo root) with your team schema
# Replace {catalog} and {schema} with your assigned values

# 4. Start Claude Code
claude .

# 5. Setup demo data (if using DE, DS, or Node.js SE track)
# Say: "Setup demo data in {catalog}.{schema}"
```

### For Facilitators

```bash
# View demo scripts
cat demos/data-engineering/README.md
cat demos/data-science/README.md
cat demos/software-engineering/README.md
cat demos/software-engineering-java/README.md
cat demos/productivity/README.md

# Each demo README contains step-by-step presenter notes
```

---

## Demo Data

Data Engineering, Data Science, and Node.js Software Engineering tracks use the same dataset. Run once to create all tables:

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
| `aisles` | Product aisles | 100 |

**Key columns:**
- `orders`: order_id, user_id, order_dow (0-6), order_hour_of_day (0-23)
- `order_products`: order_id, product_id, add_to_cart_order, reordered (0/1)
- `products`: product_id, product_name, aisle_id, department_id

> **Note:** The Java SE demo and Productivity demo need no demo data — they run entirely locally.

---

## Expected Outcomes

By the end of this hackathon, participants will:

1. **Understand Vibe Coding** — Effectively prompt and collaborate with Claude Code
2. **Use MCP Integrations** — Connect Claude to Databricks and documentation tools
3. **Master Claude Code Features** — Skills, subagents, hooks, MCP, and CLAUDE.md
4. **Build Working Solutions** — Complete a data engineering or data science challenge
5. **Share Learnings** — Demo and discuss approaches (focus on learning, not competition)

---

## Claude Code Features Used

| Feature | Location | Description |
|---------|----------|-------------|
| **CLAUDE.md** | Project root | Auto-loaded project context and rules |
| **Skills** | `.claude/skills/` | User-invocable (`/deploy`, `/train`) and auto-triggered ("setup demo data") |
| **Agents** | `.claude/agents/` | Specialized subagents for complex tasks |
| **Hooks** | `.claude/settings.json` | Auto-run on events (e.g., format on save) |
| **MCP Servers** | External | Required: Databricks. Optional: confluence, context7, brave-search, memory, obsidian |

---

## Resources

### Demo References
- [Data Engineering Demo Script](demos/data-engineering/README.md) - Step-by-step walkthrough
- [Data Science Demo Script](demos/data-science/README.md) - Step-by-step walkthrough
- [Software Engineering Demo Script](demos/software-engineering/README.md) - Step-by-step walkthrough (Node.js)
- [Software Engineering Java Demo Script](demos/software-engineering-java/README.md) - Step-by-step walkthrough (Java)
- [Productivity Demo Script](demos/productivity/README.md) - Step-by-step walkthrough (no infra required)

### Documentation
- [Setup Guide](SETUP.md) - Install Claude Code, Databricks CLI, and MCP
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
| App deploy fails | Check `app.yaml` configuration and Databricks Apps enablement |
| Lakebase connection error | Verify Lakebase resource in app.yaml and env vars |
| Context too long | Use `/compact` to summarize conversation |

---

## Questions?

Contact the event organizers or check the Slack channel.
