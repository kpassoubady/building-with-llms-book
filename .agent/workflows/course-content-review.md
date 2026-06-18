---
description: Review course slides and concept docs to remove AI-generated formatting tells and enforce consistent style
---

# Course Content Formatting Review

Strip LLM-style formatting patterns from course materials. Applies to both Marp slide decks and concept/reference markdown files across all days.

This skill inherits the core rules from `natural-prose-formatting` and adds course-specific constraints.

---

## Core Rules

All rules from the `natural-prose-formatting` skill apply without exception: no em/en dashes, no antithesis patterns, no hedging filler, no sentence-internal dash asides, no bold/italic abuse, no list abuse in prose. Those rules are not repeated here.

---

## Slide-Specific Rules (Marp markdown)

### 1. Bold in slides: allowed only in specific places

Slides permit bold for:
- Table column headers
- List item labels (the lead word/phrase, e.g., `- **Temperature:** controls randomness`)
- Slide titles (already handled by `#` headings)

Do not bold random words mid-sentence on slides.

### 2. One idea per slide

If a slide has more than one `###` subheading or more than ~12 content lines (excluding code blocks), split it into two slides with a `---` separator.

### 3. Code blocks: keep short

Code blocks on slides should be 12 lines or fewer. If longer, either:
- Trim to the essential lines with `# ...` placeholder comments
- Split across two slides (Part 1 / Part 2)
- Move the full version to a concept doc or lab file and show only the key excerpt on the slide

### 4. No orphan content after the last `---`

Every slide deck must end with a slide (title after `---`), not trailing content without a separator.

### 5. Diagram image sizing

All `<img>` tags for diagrams must include `max-height`. Default: `max-height:420px`. Increase to `500px` only if the diagram needs it and there is no other content on the slide.

### 6. Logo on lead and divider slides only

Every `<!-- _class: lead -->` and `<!-- _class: divider -->` slide must include:
```html
<img class="logo" src="../../assets/logo-white.svg" />
```
Regular content slides must NOT have the logo tag.

---

## Concept Doc Rules (long-form markdown)

### 7. No bold mid-paragraph in concept docs

Bold is allowed in:
- Headings
- Table headers and first-column labels
- Definition-style list items (the defined term)

Not allowed: bolding random words for emphasis within a sentence or paragraph.

### 8. List discipline in concept docs

Use bulleted lists for 3+ parallel items. For 2 items, write them as a sentence with "and" or "or". Do not use a list to present a single argument broken across bullets.

### 9. Consistent table style

Tables must use left-aligned headers with `:---` syntax. No trailing pipes after the last column. Keep cell content short (one line).

---

## LLM-Tell Detection Checklist

When reviewing, scan for these patterns and flag each:

| Pattern | Category | Fix |
|:--------|:---------|:----|
| `—` anywhere | em dash | Replace with comma, period, or parentheses |
| `–` anywhere | en dash | Replace with hyphen or "to" |
| "not just X, it's Y" | antithesis | Rewrite directly |
| "It's worth noting" | hedging | Delete the filler, keep the point |
| "In essence" / "At its core" | hedging | Delete |
| "Furthermore" / "Moreover" | hedging | Delete or replace with a real transition |
| Random **bold** mid-sentence | bold abuse | Remove bold, rewrite if needed |
| "powerful", "game-changing", "revolutionary" | hyperbole | Use specific language instead |
| "Let's dive in" / "Let's explore" | LLM opener | Delete or replace with the actual topic |
| "In today's world" / "In the ever-evolving" | cliche opener | Delete, start with the subject |
| Emoji overuse (3+ per slide) | emoji abuse | Max 1 emoji per slide title, 0 in body text |

---

## How to Run This Review

1. Specify which files or directories to review (e.g., `day1/slides/`, `day2/concepts/`)
2. For each file, list every violation with line number, category, and the offending text
3. Provide the corrected version for each violation
4. After listing violations, apply fixes if the user approves

---

## Scope

This skill applies to all files under:
- `day*/slides/*.md`
- `day*/concepts/*.md`
- `instructor/*.md`
- `install/*.md`
