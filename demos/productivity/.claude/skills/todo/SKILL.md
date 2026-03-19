---
name: todo
description: Parse the sample email into an organized task checklist. Use when the user says "todo", "task list", "extract tasks", "parse email into tasks", "what do I need to do", or wants to create a checklist from an email.
---

# Parse Email into Todo Checklist

Read the sample email and extract all action items into a structured, prioritized task list.

## Steps

1. **Read** the email at `src/sample-email.md`

2. **Extract** every action item, request, and follow-up
   - Identify who is responsible for each item
   - Note deadlines mentioned (explicit or implied)
   - Identify dependencies between tasks

3. **Categorize** tasks by type:
   - **Before the Review** — tasks needed to prepare
   - **During the Review** — things to present or discuss
   - **After the Review** — follow-up actions

4. **Prioritize** each task:
   - **HIGH** — Has a deadline or blocks other work
   - **MEDIUM** — Important but flexible timing
   - **LOW** — Nice to have, can wait

5. **Write** the checklist to `src/generated-todo.md` using this format:

```markdown
# Q3 Distribution Ops Review — Task Checklist

Generated from Jordan's email on {date}

## Before the Review (by Thursday 2 PM)

### HIGH Priority
- [ ] **{Task}** — Owner: {Name} — Deadline: {Date}
  - Details: {Specifics from email}

### MEDIUM Priority
- [ ] **{Task}** — Owner: {Name}
  - Details: {Specifics}

## After the Review

- [ ] **{Task}** — Owner: {Name}
  - Details: {Specifics}

---
Total tasks: X | High: X | Medium: X | Low: X
```

## Notes

- Include ALL action items — don't miss implicit tasks
- If an owner isn't clear, mark as "TBD"
- Flag any tasks that depend on other tasks completing first
