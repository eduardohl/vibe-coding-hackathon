# Claude Code Feature Guide

> **Comprehensive documentation for all 11 features — from slash commands to background tasks**

---

## Quick Reference Table

| Feature | Invocation | Persistence | Best For |
|---------|------------|-------------|----------|
| **Slash Commands** | Manual (`/cmd`) | Session only | Quick shortcuts |
| **Memory (CLAUDE.md)** | Auto-loaded | Cross-session | Long-term learning |
| **Skills** | Auto-invoked | Filesystem | Automated workflows |
| **Subagents** | Auto-delegated | Isolated context | Task distribution |
| **MCP Protocol** | Auto-queried | Real-time | Live data access |
| **Hooks** | Event-triggered | Configured | Automation & validation |
| **Plugins** | One command | All features | Complete solutions |
| **Checkpoints** | Manual/Auto | Session-based | Safe experimentation |
| **Planning Mode** | Manual/Auto | Plan phase | Complex implementations |
| **Background Tasks** | Manual | Task duration | Long-running operations |
| **CLI Reference** | Terminal commands | Session/Script | Automation & scripting |

---

## Use Case Matrix

| Use Case | Recommended Features |
|----------|---------------------|
| **Team Onboarding** | `Memory` `Slash Commands` `Plugins` |
| **Code Quality** | `Subagents` `Skills` `Memory` `Hooks` |
| **Documentation** | `Skills` `Subagents` `Plugins` |
| **DevOps** | `Plugins` `MCP` `Hooks` `Background Tasks` |
| **Security Review** | `Subagents` `Skills` `Hooks` |
| **API Integration** | `MCP` `Memory` |
| **Quick Tasks** | `Slash Commands` |
| **Complex Projects** | `All Features` `Planning Mode` |
| **Refactoring** | `Checkpoints` `Planning Mode` `Hooks` |
| **Learning/Experimentation** | `Checkpoints` `Extended Thinking` `Permission Mode` |
| **CI/CD Automation** | `CLI Reference` `Hooks` `Background Tasks` |
| **Performance Optimization** | `Planning Mode` `Checkpoints` `Background Tasks` |
| **Script Automation** | `CLI Reference` `Hooks` `MCP` |
| **Batch Processing** | `CLI Reference` `Background Tasks` |

---

## Detailed Features

<details>
<summary><strong>1. Slash Commands</strong> — Manual Invocation</summary>

### Overview
Pre-written prompts stored as .md files that you trigger on-demand. Perfect for repetitive tasks like commit generation, testing, or scaffolding.

| Property | Value |
|----------|-------|
| **Invocation** | `/command-name` |
| **Persistence** | Session only |
| **Token Cost** | 100–1,000 per use |

### Common Examples
```
/commit   – Generate commit messages
/test     – Run tests
/push     – Stage, commit, and push
/scaffold – Generate project structure
/deploy   – Deploy application
```

</details>

<details>
<summary><strong>2. Memory (CLAUDE.md)</strong> — Auto-loaded</summary>

### Overview
Hierarchical markdown files that persist across sessions, containing project conventions, team standards, and architectural patterns.

| Property | Value |
|----------|-------|
| **Invocation** | Automatic at startup |
| **Persistence** | Cross-session |
| **Search Pattern** | Hierarchical/Recursive |

### What to Store
- Coding standards
- Build/deploy instructions
- Architectural patterns
- Team preferences
- Project context

</details>

<details>
<summary><strong>3. Skills</strong> — Auto-invoked</summary>

### Overview
Domain-specific expertise packages that Claude discovers automatically when relevant. Progressive disclosure keeps context efficient.

| Property | Value |
|----------|-------|
| **Invocation** | Automatic (contextual) |
| **Persistence** | Filesystem |
| **Token Cost** | 30–50 (metadata only) |

> **Key Insight:** Skills activate only once per conversation when Claude detects relevance. They expand from 30–50 tokens of metadata to 500–5,000 tokens only when needed.

</details>

<details>
<summary><strong>4. Subagents</strong> — Auto-delegated</summary>

### Overview
Specialized Claude instances with dedicated context windows. Ideal for task distribution, code reviews, and parallel analysis.

| Property | Value |
|----------|-------|
| **Invocation** | Automatic (delegated) |
| **Context** | Isolated window |
| **Execution** | Parallel capable |

> **Best Pattern:** Subagents analyze (read-only) → Main Claude executes (write tools). This preserves control while enabling specialized expertise.

</details>

<details>
<summary><strong>5. MCP (Model Context Protocol)</strong> — Auto-queried</summary>

### Overview
External tool/service integrations connecting Claude to databases, APIs, browsers, and specialized systems. Tool Search enables lazy loading.

| Property | Value |
|----------|-------|
| **Invocation** | Automatic (data needed) |
| **Persistence** | Real-time |
| **Context Savings** | 85% reduction |

### Common MCP Servers
```
- Supabase/Postgres (database ops)
- GitHub (version control)
- Playwright/Puppeteer (browser automation)
- Context7 (documentation)
- Email systems, file system, web search
```

</details>

<details>
<summary><strong>6. Hooks</strong> — Event-triggered</summary>

### Overview
Automated shell commands at lifecycle events (PreToolUse, PostToolUse, Stop, etc.). Non-negotiable automation with exit-code control.

| Property | Value |
|----------|-------|
| **Invocation** | System events |
| **Persistence** | Always configured |
| **Control** | Exit codes |

> **Use Cases:** Auto-formatting, linting, logging, permission checks, security scanning, notifications. Exit code 0 = proceed, non-zero = block.

</details>

<details>
<summary><strong>7. Plugins</strong> — One-command Install</summary>

### Overview
Packaged bundles of commands, subagents, hooks, and MCP servers. Perfect for team standardization and shareable solutions.

| Property | Value |
|----------|-------|
| **Invocation** | Single install |
| **Bundling** | Commands + Agents + Hooks + MCP |
| **Distribution** | GitHub + Marketplace |

</details>

<details>
<summary><strong>8. Checkpoints</strong> — Manual/Auto Snapshots</summary>

### Overview
Automatic snapshots before edits, stored in local Git refs. Enables fearless experimentation with instant rollback via `Esc+Esc` or `/rewind`.

| Property | Value |
|----------|-------|
| **Invocation** | Manual or automatic |
| **Persistence** | Session-based |
| **Restore Modes** | Code only or full rollback |

> **Important:** Checkpoints only handle file changes. External operations (database writes, API calls, deployments) cannot be checkpointed.

</details>

<details>
<summary><strong>9. Planning Mode</strong> — Strategic Planning</summary>

### Overview
Two-phase execution: Claude creates detailed plan, you review/approve, then Claude executes. Perfect for complex refactors and uncertain requirements.

| Property | Value |
|----------|-------|
| **Invocation** | Manual for complex tasks |
| **Phases** | Plan → Approve → Execute |
| **Best For** | Architectural changes |

</details>

<details>
<summary><strong>10. Background Tasks</strong> — Async Operations</summary>

### Overview
Long-running operations (tests, builds, deployments) that execute while you continue working. Perfect for time-consuming tasks.

| Property | Value |
|----------|-------|
| **Invocation** | Manual |
| **Persistence** | Task duration |
| **Execution** | Asynchronous |

</details>

<details>
<summary><strong>11. CLI Reference (Headless Mode)</strong> — Terminal Automation</summary>

### Overview
Non-interactive Claude execution. Send prompt via terminal, get response to stdout. Perfect for CI/CD, automation, and scripting.

| Property | Value |
|----------|-------|
| **Invocation** | Terminal command |
| **Persistence** | Session/Script |
| **I/O** | Pipe-friendly |

### Usage
```bash
claude -p "Your prompt here"

# Examples
git diff | claude -p "Review for security"
npm audit | claude -p "Rank vulnerabilities"
```

</details>

---

## Feature Comparison

| Feature | Triggers | Persists | Context Cost | Best Scenario |
|---------|----------|----------|--------------|---------------|
| **Slash Commands** | You (`/cmd`) | Session | 100–1K tokens | Quick actions |
| **Memory** | Auto at start | Cross-session | Variable | Team standards |
| **Skills** | Claude (relevant) | Filesystem | 30–50 metadata | Domain expertise |
| **Subagents** | Claude (delegated) | Isolated | Separate window | Specialized tasks |
| **MCP** | Claude (data needed) | Real-time | ~5K with search | External systems |
| **Hooks** | System event | Always on | Minimal | Quality control |
| **Plugins** | One install | All included | Bundle sum | Complete solutions |
| **Checkpoints** | Manual/auto | Session | None | Safe experimentation |
| **Planning Mode** | You (complex) | Plan phase | Normal | Strategic projects |
| **Background Tasks** | You (long ops) | Task duration | Normal | Long operations |
| **CLI** | Terminal | Session/script | Normal | Automation |

---

## Skills vs Slash Commands

> **The Key Difference:**
> - `Skills` = Claude discovers and activates automatically based on context
> - `Slash Commands` = You manually trigger when needed

| Aspect | Skills | Slash Commands |
|--------|--------|----------------|
| Who decides? | Claude (model-driven) | You (user-driven) |
| Token cost | 30–50 (metadata) | 100–1,000 (full) |
| Predictability | Contextual | Explicit |
| Best use | Domain knowledge | Repeated actions |

---

## Hooks vs Subagents

> **The Key Difference:**
> - `Hooks` = "This action must ALWAYS happen" (deterministic)
> - `Subagents` = "Analyze this and advise me" (intelligent)

| Aspect | Hooks | Subagents |
|--------|-------|-----------|
| Type | Deterministic automation | AI-powered delegation |
| Reasoning | None (shell commands) | Full Claude reasoning |
| Best for | Linting, formatting, logging | Analysis, reviews, research |
| Control | Blocking (exit codes) | Advisory (can override) |

---

## Workflow Patterns

### Pattern 1: Team Onboarding
```
CLAUDE.md (project standards)
    ↓
Slash Commands (quick actions)
    ↓
Plugins (entire package)
    ↓
Hooks (enforce quality)
```

### Pattern 2: Code Quality Assurance
```
Memory (conventions)
    ↓
Skills (expertise)
    ↓
Subagents (parallel review)
    ↓
Hooks (auto-format/lint/test)
```

### Pattern 3: Complex Refactoring
```
Planning Mode (strategy)
    ↓
Checkpoints (safety net)
    ↓
Subagents (parallel work)
    ↓
Hooks (auto-test)
```

### Pattern 4: DevOps Automation
```
Plugins (toolchain)
    ↓
MCP (integration)
    ↓
Hooks (validation)
    ↓
Background Tasks (deployments)
    ↓
CLI (CI/CD)
```

### Pattern 5: Security Review
```
Skills (security patterns)
    ↓
Subagents (read-only analysis)
    ↓
Hooks (block dangerous ops)
    ↓
Memory (security policies)
```

---

## Decision Matrix

| Goal | Primary Feature | Supporting Features |
|------|-----------------|---------------------|
| Save time on repetitive tasks | Slash Commands | Memory, Hooks |
| Maintain consistency | Memory | Skills, Hooks |
| Delegate specialized tasks | Subagents | Skills, MCP |
| Connect external systems | MCP | Memory, Plugins |
| Enforce quality standards | Hooks | Subagents, Skills |
| Share workflows with team | Plugins | All features |
| Safe experimentation | Checkpoints | Planning Mode |
| Complex projects | Planning Mode | Checkpoints, Subagents |
| Automation & CI/CD | CLI + Hooks | Background Tasks, MCP |
| Real-time data access | MCP | Skills, Subagents |

---

## Quick Start: 3-Day Implementation

### Day 1: Foundation
- Create `.claude/CLAUDE.md` with team standards
- Write 3 frequently-used Slash Commands
- Set up basic Hooks for formatting/linting

### Day 2: Automation
- Create 1–2 Skills for domain expertise
- Configure MCP for essential external services
- Test command/skill/hook combinations

### Day 3: Scaling
- Create first Plugin bundling Day 1–2 features
- Document workflows for team
- Gather feedback and iterate

---

## Glossary

| Term | Definition |
|------|------------|
| **MCP** | Model Context Protocol; standard for external tool integration using JSON-RPC over stdio |
| **Subagent** | Specialized Claude instance with isolated context window; can run in parallel |
| **Checkpoint** | Snapshot of file state stored in local Git refs; enables safe rollback |
| **Hook** | Automated shell command triggered by lifecycle event (PreToolUse, PostToolUse, Stop, etc.) |
| **Skill** | Auto-invoked expertise package discovered by Claude when contextually relevant |
| **Plugin** | Bundled package containing commands, agents, hooks, and MCPs; shareable and versioned |
| **Planning Mode** | Two-phase execution: Claude creates plan → You approve → Claude executes |
| **Tool Search** | Lazy loading of tool definitions via regex; reduces context usage by 85% |
| **Headless Mode** | Non-interactive Claude execution via CLI; perfect for automation and scripting |
| **Background Task** | Long-running operation (tests, builds, deployments) that executes asynchronously |
| **Memory File** | CLAUDE.md file containing project context, conventions, and team preferences; loaded hierarchically |
| **Slash Command** | User-triggered shortcut stored as .md file; executes on manual invocation |

---

*Claude Code Feature Guide • Last Updated: January 2026*

For official documentation, visit [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code)
