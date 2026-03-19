---
name: draft-reply
description: Draft a professional reply to the sample email. Use when the user says "draft reply", "reply to email", "respond to email", "write a reply", "reply to Jordan", or wants to compose a response to the original email.
---

# Draft Reply to Email

Read the sample email and draft a comprehensive reply acknowledging all items and confirming your plan of action.

## Steps

1. **Read** the original email at `src/sample-email.md`

2. **Check** what work has already been done
   - Look for `generated-todo.md` (task checklist)
   - Look for `generated-budget.csv` (spreadsheet)
   - Look for `generated-slides.html` (presentation)
   - Look for any draft messages
   - Reference completed items in the reply

3. **Draft** the reply with this structure:
   - Professional greeting
   - Acknowledge the request and timeline
   - For each action item: confirm who's handling it and status
   - Flag any concerns or questions
   - Positive closing

4. **Write** to `src/generated-reply.md`

## Reply Format

```markdown
# Reply to Jordan — Q3 Distribution Ops Review

**To:** Jordan Mitchell
**Subject:** Re: Q3 Distribution Ops Review — Action Items

---

Hi Jordan,

Thanks for putting this together. Here's where we stand on each item:

**1. Budget Summary** — {Status}

**2. Presentation** — {Status}

**3. Metro Regional Health Technical Response** — {Status}

**4. Team Coordination** — {Status}

**5. Post-Review Follow-ups** — {Status}

{Any questions or concerns}

{Closing}
```

## Notes

- Reference specific work already completed (files generated)
- Be concrete about timelines
- Tone: professional, confident, collaborative
