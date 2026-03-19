---
name: email-parser
description: Parse emails into structured task checklists with priorities and owners. Use when the user mentions "parse email", "extract action items", or "analyze email".
---

# Email Parser Skill

Automatically triggered when the user wants to parse and analyze an email.

## When to Activate

This skill activates when the user mentions:
- "parse email", "parse this email", "analyze email"
- "extract action items", "extract tasks from the email"
- "what are the action items in the email"

## Actions

### 1. Find the Email
- Look for `src/sample-email.md` or ask the user which email to parse
- Read the full email content

### 2. Extract Action Items
- Identify every explicit request ("I need...", "Can someone...", "Please...")
- Identify implicit tasks (deadlines imply preparation work)
- Identify coordination tasks (reaching out to people)
- Identify follow-up tasks (things to do after an event)

### 3. Organize Tasks
For each task, determine:
- **What**: Clear description of the deliverable
- **Who**: Person responsible (from email context or mark as "You")
- **When**: Deadline (explicit date or inferred)
- **Priority**: HIGH (has deadline / blocks others), MEDIUM (important), LOW (nice to have)
- **Dependencies**: Other tasks that must complete first

### 4. Generate Checklist
Write to `src/generated-todo.md` with:
- Tasks grouped by timeline (Before / During / After the event)
- Priority labels on each task
- Checkbox format for easy tracking
- Summary count at the bottom

## Example Output

```markdown
# Task Checklist

## HIGH Priority
- [ ] **Create budget spreadsheet** — Owner: You — Deadline: Wednesday
  - Q3 spend vs. budget by department with variance calculations
- [ ] **Prepare slide deck** — Owner: You — Deadline: Wednesday
  - 5 slides covering Q3 highlights, metrics, team, challenges, Q4

## MEDIUM Priority
- [ ] **Coordinate with Sarah** — Deadline: Tuesday
  - Ask her to finalize cycle count variance report

---
Total: 12 tasks | HIGH: 4 | MEDIUM: 5 | LOW: 3
```
