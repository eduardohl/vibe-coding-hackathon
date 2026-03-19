# Productivity Demo Project

## Overview

This project demonstrates how Claude Code can accelerate everyday productivity tasks — no infrastructure, no databases, no deployment. Just you, Claude, and a messy email from your boss.

**Scenario:** Your VP of Distribution Operations sends an email about an upcoming Q3 Operations Review. You use Claude Code to turn it into organized action: a todo checklist, draft messages, a slide deck, a spreadsheet, and a quick script to answer a technical question.

**This demo showcases Claude Code features including:**
- Auto-triggered skills (email parsing, message drafting, slides, spreadsheets)
- Custom skills (`/todo`, `/draft-reply`)
- Code generation for practical tasks
- Hooks for automatic code formatting
- Checkpoints for safe experimentation

## Rules

- **ONLY use local skills** from this project's `.claude/skills/` directory — do NOT use external plugin skills. This demo must be self-contained.
- ALWAYS check `.claude/skills/` directory before implementing any task manually
- Read the skill file and follow its instructions exactly before writing any code
- **IMPORTANT:** When creating new files, use the `generated-` prefix (e.g., `generated-todo.md`, `generated-slides.html`) to distinguish demo-created files from template files
- **NO MCP servers required** — this demo runs entirely offline with local files

## Environment

- No Databricks, no cloud services, no MCP servers
- Just Claude Code + local files
- Python 3.x for any scripts (optional)
- All output files are created in `src/`

## The Email

The input email is at `src/sample-email.md`. It contains:

| Section | What It Needs |
|---------|---------------|
| Budget Summary | Spreadsheet with Q3 spend vs. budget by department |
| Presentation | 5-slide deck for executive leadership |
| Technical Question | Research + draft response about real-time inventory API |
| Team Coordination | Messages to Sarah, Mike, and Lisa |
| Post-Review Follow-ups | Summary email + scheduling tasks |

## Claude Code Features

### Skills

Skills in `.claude/skills/` can be invoked directly (e.g., `/todo`) or activate automatically based on context:

| Skill | Invocation / Triggers |
|-------|----------------------|
| `todo` | `/todo` - Parse the sample email into an organized task checklist |
| `draft-reply` | `/draft-reply` - Draft a professional reply to the email |
| `email-parser` | "parse email", "analyze email", "extract action items" |
| `message-drafter` | "draft message", "write to", "send to" |
| `slide-creator` | "create slides", "slide deck", "presentation" |
| `spreadsheet-creator` | "create spreadsheet", "budget spreadsheet", "csv" |

### Hooks (Automation)

| Hook | Trigger | Action |
|------|---------|--------|
| PostToolUse:Write | After writing .py files | Auto-format with Ruff |

## File Structure

```
├── CLAUDE.md                    # This file
├── README.md                    # Demo script
├── .gitignore                   # Ignores generated files
├── .claude/
│   ├── skills/                  # Skills (user-invocable and auto-triggered)
│   │   ├── todo/SKILL.md
│   │   ├── draft-reply/SKILL.md
│   │   ├── email-parser/SKILL.md
│   │   ├── message-drafter/SKILL.md
│   │   ├── slide-creator/SKILL.md
│   │   └── spreadsheet-creator/SKILL.md
│   └── settings.json            # Hooks and permissions
└── src/
    ├── sample-email.md          # The input email (read this first!)
    └── generated-*/             # Created during demo by Claude
```

> **Note:** Files with `generated-` prefix are created live during the demo.

## Coding Standards

### Generated Files

- All output goes in `src/` with `generated-` prefix
- Markdown for text documents (todo lists, messages)
- HTML for slide decks (self-contained, viewable in browser)
- CSV for spreadsheets (openable in Excel/Sheets)
- Python for any scripts (auto-formatted by hooks)

### Messages

- Professional but warm tone
- Include specific details from the email (dates, numbers, names)
- Clear call-to-action in each message
