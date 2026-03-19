---
name: message-drafter
description: Draft professional messages to colleagues based on email context. Use when the user mentions "draft message", "write message", "send to", "write to", "message to", "reach out to", or "draft a note".
---

# Message Drafter Skill

Automatically triggered when the user wants to draft a message to someone.

## When to Activate

This skill activates when the user mentions:
- "draft message to...", "write message to..."
- "send to...", "write to..."
- "reach out to...", "message to..."
- "draft a note to..."

## Actions

### 1. Identify the Recipient
- Parse the recipient's name from the user's request
- Look up context about this person from the sample email

### 2. Determine the Purpose
- What action is being requested of the recipient?
- What deadline applies?
- What context do they need?

### 3. Draft the Message
Write in a **professional but warm tone** — friendly, clear, and action-oriented:

```markdown
# Message to {Recipient Name}

**Subject:** {Clear, specific subject line}

---

Hi {First Name},

{Opening — brief context about why you're reaching out}

{The specific ask — what you need and by when}

{Any helpful context or resources they might need}

{Offer to help — "Let me know if you need anything from my side"}

Thanks,
{Sender}
```

### 4. Save the Message
Write to `src/generated-message-{recipient-first-name}.md`

## Guidelines

- **Be specific** — include dates, numbers, and details from the original email
- **Be warm but professional** — friendly colleague tone, not corporate-speak
- **Stay concise** — respect their time, get to the point
- **Be helpful** — provide context so they can act without asking follow-up questions
- **Include a clear CTA** — what exactly you need and by when

## Example

```markdown
# Message to Sarah Chen

**Subject:** Cycle Count Variance Report Needed by Tuesday EOD

---

Hi Sarah,

Jordan is pulling together materials for the Q3 Distribution Ops Review next Thursday, and the cycle count variance data is one of the key pieces.

Could you finalize the regional comparison by Tuesday end of day? I know you already have the raw data from all three distribution centers — we just need the breakdown by region.

The headline numbers look great (accuracy up to 99.1%) — definitely a story worth highlighting for leadership. Let me know if you need any help pulling the comparisons together.

Thanks,
{Sender}
```
