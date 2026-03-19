# Demo: Productivity with Claude Code

> **30 min** | No infrastructure required — just Claude Code | [Full Claude Code Docs](https://code.claude.com/docs/en/overview)
>
> **Best as the first demo** — zero setup, shows the power of Claude Code before diving into Databricks-specific tracks.

---

## Quick Reference — Prompts to Type

| Step | Prompt | Feature Shown |
|------|--------|---------------|
| 0 | *Start Claude Code in `demos/productivity/`* | Setup |
| 1 | `Read the email in src/sample-email.md and give me a quick summary` | File reading |
| 2 | *Paste a screenshot* + `What does this show?` | Image understanding |
| 3 | `/todo` | [Skills](https://code.claude.com/docs/en/skills) |
| 4 | `Draft a message to Sarah Chen asking her to finalize the cycle count variance report by Tuesday` | [Skills](https://code.claude.com/docs/en/skills) (message-drafter) |
| 5 | `Create a slide deck for the Q3 Distribution Ops Review based on the email` | [Skills](https://code.claude.com/docs/en/skills) (slide-creator) |
| 6 | `Create a CSV spreadsheet with the budget breakdown including variance calculations` | [Skills](https://code.claude.com/docs/en/skills) (spreadsheet-creator) |
| 7 | `Write a Python script that calculates fulfillment rate improvements and budget variance percentages` | Code generation + [Hooks](https://code.claude.com/docs/en/hooks) |
| 8 | `Draft a technical response to Metro Regional Health about real-time inventory API integration` | [Skills](https://code.claude.com/docs/en/skills) (message-drafter) |
| 9 | `/draft-reply` | [Skills](https://code.claude.com/docs/en/skills) |
| 10 | *Press `Esc` twice* | [Checkpoints](https://code.claude.com/docs/en/overview) |

---

## Prerequisites

1. Terminal open in `demos/productivity/`
2. Claude Code installed
3. That's it. No MCP, no cloud, no tokens.

---

## Walkthrough

### Step 0: Start Claude Code

```bash
cd demos/productivity
claude .
```

> **Observe:** Claude automatically reads the `CLAUDE.md` — it already knows the context, the skills available, and the scenario. That's [CLAUDE.md](https://code.claude.com/docs/en/memory) in action.

---

### Step 1: Read the Email

```
Read the email in src/sample-email.md and give me a quick summary
```

> **Observe:** Claude reads the file and summarizes it — understanding people, deadlines, numbers, and action items from unstructured text. This is the starting point for everything that follows.

---

### Step 2: Image Understanding

Take a screenshot of something relevant — a dashboard, a chart, an error message, a whiteboard photo, or even a table from a PDF — and paste it directly into Claude Code.

```
What does this show? Summarize the key takeaways.
```

> **Observe:** Claude can **read and understand images**. Paste a screenshot and ask it to summarize, extract data, explain an error, or turn a whiteboard sketch into structured notes. This works with dashboards, charts, spreadsheets, architecture diagrams — anything you can screenshot.

**Try it:** Take a screenshot of a chart or table from any tool you use daily. Paste it and ask Claude to extract the data into a CSV, or explain what it shows.

---

### Step 3: Extract a Todo Checklist

```
/todo
```

> **Observe:** This is a [Skill](https://code.claude.com/docs/en/skills) — you typed `/todo` and Claude followed the instructions in the skill to create a structured, prioritized task list. Check the generated file — are the priorities right? Would you reorder anything?

**Expected output:** `src/generated-todo.md` with categorized tasks, owners, deadlines, and priorities.

---

### Step 4: Draft a Message

```
Draft a message to Sarah Chen asking her to finalize the cycle count variance report by Tuesday EOD
```

> **Observe:** You didn't point to any file — Claude matched your intent to the [message-drafter skill](https://code.claude.com/docs/en/skills) automatically. Notice the tone, the specific details pulled from the email, and the clear ask. Would you change anything?

**Try another:**

```
Draft a message to Mike Rodriguez about preparing the warehouse throughput metrics from the WMS export
```

> **Observe:** Same skill, different context. Claude adapts the tone and details for each recipient.

---

### Step 5: Create a Slide Deck

```
Create a slide deck for the Q3 Distribution Ops Review based on the email
```

> **Observe:** The [slide-creator skill](https://code.claude.com/docs/en/skills) activates and generates a complete HTML presentation. Open `src/generated-slides.html` in a browser — you have a real deck with data, structure, and formatting. How long would this take manually?

**Discuss:** What would you change? What's missing? Ask Claude to add a slide or change the styling.

---

### Step 6: Create a Spreadsheet

```
Create a CSV spreadsheet with the budget breakdown from the email, including variance calculations and percentage over/under
```

> **Observe:** The [spreadsheet-creator skill](https://code.claude.com/docs/en/skills) generates a CSV with formulas-ready data. Open `src/generated-budget.csv` in Excel or Google Sheets. Notice it calculated the variances and percentages automatically from the email data.

---

### Step 7: Write a Quick Script

```
Write a Python script that takes our Q3 numbers (fulfillment rate 98.2% from 96.8%, shrinkage 0.8% from 1.3%, on-time delivery 97.4%) and calculates the exact improvements and percentage changes. Save it as src/generated-metrics.py
```

> **Observe:** (1) Claude writes a working Python script, and (2) it gets auto-formatted — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) firing Ruff. Run the script to see the output.

**Then:**

```
Run it
```

> **Observe:** Claude executes the script and shows the results. You now have exact numbers to reference in your response.

---

### Step 8: Draft a Technical Response

```
Draft a technical response to Metro Regional Health about whether our platform supports real-time inventory API integration across multiple warehouse locations. Make it sound knowledgeable but honest — we can do it with some caveats.
```

> **Observe:** Claude generates a professional technical response. Notice how it structures the answer: capability confirmation, architecture explanation, caveats, and next steps. This would take 30+ minutes to write from scratch.

---

### Step 9: Draft a Reply to Jordan

```
/draft-reply
```

> **Observe:** Another [Skill](https://code.claude.com/docs/en/skills) — Claude reads the original email and drafts a comprehensive reply addressing every point, referencing the work you've already done. It ties everything together.

---

### Step 10: Safe Experimentation with Checkpoints

```
Actually, make the slide deck more visual with charts and a dark theme
```

After Claude makes changes, press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot before every edit. Don't like the dark theme? Roll back instantly.

**Bonus — compact a long conversation:**

```
/compact
```

---

> **Reflect with the group:** You just turned one email into a todo list, three draft messages, a slide deck, a spreadsheet, a Python script, and a technical response — in about 20 minutes. What repetitive tasks in your daily work could benefit from this approach?

---

## Features Cheat Sheet

| Feature | What It Does | Where It Lives | Docs |
|---------|--------------|----------------|------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) | Project context, auto-loaded | `CLAUDE.md` | [Memory](https://code.claude.com/docs/en/memory) |
| [Skills](https://code.claude.com/docs/en/skills) | `/todo`, `/draft-reply`, email parsing, drafting, slides, spreadsheets | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| Image understanding | Paste screenshots — Claude reads and extracts data | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
| [Hooks](https://code.claude.com/docs/en/hooks) | Auto-format Python with Ruff | `.claude/settings.json` | [Hooks](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](https://code.claude.com/docs/en/overview) | `Esc+Esc` to rewind changes | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
