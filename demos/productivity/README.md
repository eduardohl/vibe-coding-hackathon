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
| 2 | `/todo` | [Skills](https://code.claude.com/docs/en/skills) |
| 3 | `Draft a message to Sarah Chen asking her to finalize the cycle count variance report by Tuesday` | [Skills](https://code.claude.com/docs/en/skills) (auto-triggered) |
| 4 | `Create a slide deck for the Q3 Distribution Ops Review based on the email` | [Skills](https://code.claude.com/docs/en/skills) (auto-triggered) |
| 5 | `Create a CSV spreadsheet with the budget breakdown including variance calculations` | [Skills](https://code.claude.com/docs/en/skills) (auto-triggered) |
| 6 | `Write a Python script that calculates fulfillment rate improvements...` | Code generation + [Hooks](https://code.claude.com/docs/en/hooks) |
| 7 | `Draft a technical response to Metro Regional Health about real-time inventory API integration` | [Skills](https://code.claude.com/docs/en/skills) (auto-triggered) |
| 8 | `/draft-reply` | [Skills](https://code.claude.com/docs/en/skills) |
| 9 | *Paste a UI screenshot* + `Recreate this as HTML` | Image understanding |
| 10 | *Press `Esc` twice* | [Checkpoints](https://code.claude.com/docs/en/overview) |

---

## Prerequisites

> **First time?** Follow [Step 1 of the Setup Guide](../../SETUP.md) to install Claude Code. That's the only requirement.

1. Terminal open in `demos/productivity/`
2. Claude Code installed — no MCP, no cloud, no tokens
3. Fresh session: start `claude`, then type `/clear`

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

> **Observe:** Claude reads the file and summarizes it — understanding people, deadlines, numbers, and action items from unstructured text. This email from Jordan (VP of Distribution Ops) is the starting point for everything that follows.

---

### Step 2: Extract a Todo Checklist

Jordan's email has at least a dozen action items buried across budget requests, presentation prep, team coordination, and follow-ups. Let's extract them all at once.

```
/todo
```

> **Observe:** `/todo` is a [Skill](https://code.claude.com/docs/en/skills) — a pre-written set of instructions at `.claude/skills/todo/SKILL.md`. Claude reads Jordan's email, identifies every explicit and implicit task, assigns owners and deadlines, and organizes them by priority. You typed two words instead of writing a detailed prompt.

**Expected output:** `src/generated-todo.md` — open it and check: did Claude catch the budget spreadsheet, the slide deck, the messages to Sarah/Mike/Lisa, and the post-review follow-ups?

---

### Step 3: Draft a Message

Jordan asked us to coordinate with three people. Let's start with Sarah.

```
Draft a message to Sarah Chen asking her to finalize the cycle count variance report by Tuesday EOD
```

> **Observe:** You didn't type `/` anything — Claude matched your intent to the [message-drafter skill](https://code.claude.com/docs/en/skills) automatically. Notice the tone, the specific details pulled from the email, and the clear ask.

**Try another from the email:**

```
Draft a message to Mike Rodriguez about preparing the warehouse throughput metrics from the WMS export
```

> **Observe:** Same skill, different context. Claude adapts the tone and details for each recipient.

---

### Step 4: Create a Slide Deck

Jordan needs a 5-slide deck for the executive leadership review next Thursday.

```
Create a slide deck for the Q3 Distribution Ops Review based on the email
```

> **Observe:** The [slide-creator skill](https://code.claude.com/docs/en/skills) activates and generates a complete HTML presentation using the metrics, team highlights, and challenges from Jordan's email. Open `src/generated-slides.html` in a browser — you have a real deck. How long would this take manually?

**Discuss:** What would you change? Ask Claude to add a slide or change the styling.

---

### Step 5: Create a Spreadsheet

Jordan included a budget table in the email — Warehouse Ops, Transportation, Procurement, Inventory Management. Let's turn it into a proper spreadsheet.

```
Create a CSV spreadsheet with the budget breakdown from the email, including variance calculations and percentage over/under
```

> **Observe:** The [spreadsheet-creator skill](https://code.claude.com/docs/en/skills) generates a CSV with the four departments from Jordan's email, plus calculated variances and percentages. Open `src/generated-budget.csv` in Excel or Google Sheets.

---

### Step 6: Write a Quick Script

Jordan's email mentions specific Q3 improvements — fulfillment rate, shrinkage, on-time delivery. Let's compute the exact percentage changes.

```
Write a Python script that takes our Q3 numbers (fulfillment rate 98.2% from 96.8%, shrinkage 0.8% from 1.3%, on-time delivery 97.4%) and calculates the exact improvements and percentage changes. Save it as src/generated-metrics.py
```

> **Observe:** (1) Claude writes a working Python script, and (2) it gets auto-formatted — that's the [PostToolUse hook](https://code.claude.com/docs/en/hooks) firing Ruff.

**Then:** `Run it`

> **Observe:** Claude executes the script and shows the results. You now have exact numbers for the slide deck and Jordan's reply.

---

### Step 7: Draft a Technical Response

Jordan's email mentions a client question from Metro Regional Health about real-time inventory API integration.

```
Draft a technical response to Metro Regional Health about whether our platform supports real-time inventory API integration across multiple warehouse locations. Make it sound knowledgeable but honest — we can do it with some caveats.
```

> **Observe:** Claude generates a professional technical response. Notice the structure: capability confirmation, architecture explanation, caveats, and next steps. This would take 30+ minutes to write from scratch.

---

### Step 8: Draft a Reply to Jordan

We've done everything Jordan asked for. Let's tie it all together.

```
/draft-reply
```

> **Observe:** Another [Skill](https://code.claude.com/docs/en/skills) — Claude reads the original email and drafts a comprehensive reply addressing every point, referencing the deliverables you've already created.

---

### Step 9: Image Understanding

Switching gears — Claude can also understand images. Take a screenshot of any app interface you use daily — a dashboard, an internal tool, a settings page — and paste it into Claude Code.

```
Recreate this interface as a self-contained HTML file. Make it look as close to the original as possible. Save it as src/generated-mockup.html
```

> **Observe:** Claude **reads the screenshot**, understands the layout, colors, and components, then generates a working HTML mockup. Open `src/generated-mockup.html` in a browser — a functional visual replica, built in seconds.

---

### Step 10: Safe Experimentation with Checkpoints

```
Actually, make the slide deck more visual with charts and a dark theme
```

After Claude makes changes, press **`Esc` twice** to open the checkpoint menu.

> **Observe:** [Checkpoints](https://code.claude.com/docs/en/overview) snapshot before every edit. Don't like the dark theme? Roll back instantly.

**Bonus:** `/compact` to summarize a long conversation.

---

> **Reflect with the group:** You just turned one email into a todo list, three draft messages, a slide deck, a spreadsheet, a Python script, a technical response, and a UI mockup — in about 20 minutes. What repetitive tasks in your daily work could benefit from this approach?

---

## Features Cheat Sheet

| Feature | What It Does | Where It Lives | Docs |
|---------|--------------|----------------|------|
| [CLAUDE.md](https://code.claude.com/docs/en/memory) | Project context, auto-loaded | `CLAUDE.md` | [Memory](https://code.claude.com/docs/en/memory) |
| [Skills](https://code.claude.com/docs/en/skills) | `/todo`, `/draft-reply`, email parsing, drafting, slides, spreadsheets | `.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| Image understanding | Paste a UI screenshot — Claude recreates it as HTML | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
| [Hooks](https://code.claude.com/docs/en/hooks) | Auto-format Python with Ruff | `.claude/settings.json` | [Hooks](https://code.claude.com/docs/en/hooks) |
| [Checkpoints](https://code.claude.com/docs/en/overview) | `Esc+Esc` to rewind changes | Built-in | [Overview](https://code.claude.com/docs/en/overview) |
