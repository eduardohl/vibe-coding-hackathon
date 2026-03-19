---
name: slide-creator
description: Create HTML slide decks from email content or meeting context. Use when the user mentions "create slides", "slide deck", "presentation", "create a deck", "make slides", or "powerpoint".
---

# Slide Creator Skill

Automatically triggered when the user wants to create a presentation.

## When to Activate

This skill activates when the user mentions:
- "create slides", "create a slide deck"
- "presentation", "make a presentation"
- "create a deck", "slide deck"
- "powerpoint", "make slides"

## Actions

### 1. Gather Content
- Read the source material (email, notes, conversation context)
- Identify the key points for each slide
- Extract data, metrics, and quotes

### 2. Structure the Deck
- Title slide with event name and date
- One slide per major topic
- Keep text minimal — bullet points, not paragraphs
- Include data and metrics where available

### 3. Generate HTML Presentation
Create a self-contained HTML file that can be opened in any browser.

The HTML should include:
- **Built-in slide navigation** (arrow keys or click)
- **Clean, professional styling** (dark or light theme)
- **Readable typography** (large fonts for presentation)
- **Data visualization** where appropriate (simple CSS charts or tables)
- **Slide numbers**

### 4. Save the File
Write to `src/generated-slides.html`

## Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <title>{Presentation Title}</title>
  <style>
    /* Professional slide styling */
    /* Navigation with arrow keys */
    /* Print-friendly */
  </style>
</head>
<body>
  <div class="slide" id="slide1">
    <h1>{Title}</h1>
    <p>{Subtitle / Date}</p>
  </div>

  <div class="slide" id="slide2">
    <h2>{Topic}</h2>
    <ul>
      <li>{Point 1}</li>
      <li>{Point 2}</li>
    </ul>
  </div>

  <!-- More slides... -->

  <script>
    // Arrow key navigation
    // Slide counter
  </script>
</body>
</html>
```

## Guidelines

- **5-7 slides maximum** — keep it focused
- **One idea per slide** — don't overcrowd
- **Use the data** — include actual numbers from the source
- **Make it presentable** — someone should be able to open this in a browser and present immediately
- **Include speaker notes** as HTML comments if helpful

## Example Slide Content

```
Slide 1: Q3 Distribution Ops Review (title + date)
Slide 2: Key Metrics (fulfillment rate, inventory accuracy, on-time delivery)
Slide 3: Capacity & Growth (new distribution centers, warehouse expansion)
Slide 4: Challenges (budget overrun, slipped client go-lives)
Slide 5: Q4 Priorities (client onboarding, shrinkage reduction, API integration)
```
