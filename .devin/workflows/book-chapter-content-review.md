---
description: Review book chapters to remove AI-generated formatting tells, enforce consistent style, and validate chapter structure
---

# Book Chapter Content Review

Review chapter markdown so the workflow matches the current manuscript patterns. This workflow inherits `natural-prose-formatting` and adds book-specific checks for structure, admonitions, references, diagrams, and quiz formatting.

Primary scope:
- `01-*.md` through `14-*.md` (core chapter rules)
- `appendix-*.md`, `00-front-matter.md`, `00.5-how-to-use.md`, `cover-info/*.md` (lightweight structure and prose checks only)

---

## Core Rules

All `natural-prose-formatting` rules apply:
- no em dash or en dash
- no antithesis patterns (for example, "not just X, it is Y")
- no hedging filler ("It is worth noting", "In essence", "At its core")
- no random bold/italic emphasis
- no list abuse in prose

---

## Book Chapter Structure Rules

### 1. Required chapter sections

For chapters `01` to `14`, validate this order:
- `# N. Chapter Title`
- Learning objectives block at top:
  - `> **🎯 Learning Objectives**`
  - exactly 3 objective bullets
- Opening narrative section as first `##` section, usually story-driven title (do not force a specific 3 to 5 word count)
- Main chapter content sections (`##` and `###`)
- `## 🧪 Try It Yourself` with practical exercises
- `## 📋 Chapter Summary` containing:
  - `> **💡 Key Takeaways**` bullets
  - `> [!PITFALLS]` with 3 pitfall bullets
- `## 🧠 Knowledge Check` with 5 questions and answer reveal block

### 2. Admonitions

Current chapters use these admonition types:

| Type | When to Use | Frequency |
|:-----|:------------|:----------|
| `[!NOTE]` | Facts, clarification, context | common |
| `[!TIP]` | Practical guidance, cross-links, best practices | common |
| `[!WARNING]` | Common mistakes and failure modes | common |
| `[!IMPORTANT]` | Must-know operational detail | occasional |
| `[!CAUTION]` | Higher-risk action or decision point | occasional |
| `[!PROMPT]` | Prompt examples in some chapters | occasional |
| `[!PITFALLS]` | Summary pitfall block in each chapter | required |

Review guidance:
- target roughly 4 to 8 admonitions per chapter including `[!PITFALLS]`
- do not enforce a fixed mix per chapter
- labels such as `**Did You Know?**` are encouraged but not mandatory for every admonition type
- avoid back-to-back identical admonitions without clear need

### 3. Code blocks

Code blocks in chapters should:
- include language tags (`python`, `bash`, `text`, `json`, etc.)
- be syntactically valid and complete (no truncated statements)
- use the book's helper pattern where relevant (`from shared import get_completion`)
- include expected output where it improves learning
- keep examples concise unless explicitly marked as full exercise handoff

```python
# Avoid deep visual alignment that wraps badly in 6x9 page layout
{"role": "system", "content": "You are a senior Python developer. "
                               "Explain in 3-4 sentences."}

# Prefer a simple wrapped layout
{"role": "system",
 "content": (
    "You are a senior Python developer. "
    "Explain in 3-4 sentences."
 )}
```

### 4. Tables

Tables must:
- be valid markdown tables
- use alignment row (for example `|:---|:---|`)
- keep cell content concise
- use consistent column ordering within the same chapter

### 5. Cross-chapter references

Cross-references can be inline prose or inside admonitions.

Required checks:
- chapter references must be clickable markdown links, for example `[Chapter 7](07-api-parameters.md)`
- target file must exist
- do not link a chapter to itself unless there is a strong reason
- referenced topic should match the destination chapter content

### 6. Diagram references

Current manuscript uses both:
- SVG diagrams: `![...](diagrams/chNN-name.svg)`
- sketch PNG diagrams: `![...](./diagrams/chNN-name-sketch.png)` (with or without `./`)

Checks:
- every local diagram/image path must resolve to an existing file
- high-resolution companion links should be valid GitHub URLs when present
- alt text should describe the figure clearly

---

## Book-Specific Formatting Rules

### 7. Horizontal rules

Do not insert `---` as visual separators inside chapter prose. Keep flow with headings and paragraphs.

### 8. Bold usage in chapters

Bold is allowed in:
- Headings (handled by `#` syntax)
- Table headers and first-column labels
- Definition-style list items (the defined term)
- Admonition labels (e.g., "**Did You Know?**")
- First introduction of key terms when pedagogically useful

Not allowed: bolding random words for emphasis within a sentence or paragraph.

### 9. List discipline

Use lists when items are parallel and scannable. Prefer prose for short non-parallel points.

### 10. Paragraph structure

- One idea per paragraph
- Short paragraphs (3-5 sentences max)
- Split overly long paragraphs when readability drops

### 11. Comparison tables

Use comparison tables when comparing approaches, models, or trade-offs. A common pattern:

```markdown
| Approach | Pros | Cons | When to Use |
|:---------|:-----|:-----|:------------|
```

### 12. Knowledge Check format

Section header must be `## 🧠 Knowledge Check`.

Each chapter should include:
- 5 questions total
- mix of:
  - Multiple Choice
  - True or False
  - Fill in the Blank
  - Scenario
- answer reveal in `<details>` block with `<summary><strong>Click to Reveal Answers</strong></summary>`

Canonical layout:

```markdown
## 🧠 Knowledge Check

1. **Multiple Choice:** Question text?

    ::: {.mcq-2col}
    - [ ] Option A
    - [ ] Option B
    - [ ] Option C
    - [ ] Option D
    :::

2. **True or False:** Statement here?

    ::: {.tf-inline}
    - [ ] True
    - [ ] False
    :::

3. **Fill in the Blank:** The ______ is the answer.

4. **Multiple Choice:** Another question?

    ::: {.mcq-2col}
    - [ ] Option A
    - [ ] Option B
    - [ ] Option C
    - [ ] Option D
    :::

5. **Scenario:** A scenario question here?

<details>
<summary><strong>Click to Reveal Answers</strong></summary>

1. **Answer**: Explanation.
2. **Answer**: Explanation.
3. **Answer**: Explanation.
4. **Answer**: Explanation.
5. **Answer**: Explanation.

</details>
```

Critical rules:
- Nested lists need an empty line before them and 4-space indentation so PDF numbering does not break
- The `:::` containers are required for multiple choice and true/false questions.
- Answer lines use `**Answer**:` (colon after bold)
- The `<details>` block must have a blank line before `</details>`

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
| Excessive visual separators (`---`) | formatting drift | Remove and use headings instead |
| Missing required section | structure gap | Add the missing section |
| Standalone `## Common Pitfalls` section | structure error | Move to `[!PITFALLS]` block under Chapter Summary |
| Cross-reference without markdown link | reference error | Convert to `[Chapter N](NN-filename.md)` clickable link |
| Invalid cross-reference | reference error | Fix or remove the reference |
| Code continuation aligned under opening quote | code style | Break after comma, 4-space indent continuation |
| Paragraph > 5 sentences | paragraph length | Split into shorter paragraphs |

---

## Part 2: Reference Integrity

### 2.1 File Existence

For every file path mentioned in chapters, verify the file exists:
- Diagram/image files (`diagrams/*`, `images/*`)
- Cross-referenced chapters (`XX-chapter-title.md`)

### 2.2 Cross-Chapter References

When a chapter references content from another chapter, verify:
- The referenced chapter exists
- The chapter number is correct
- The description matches what the referenced chapter actually contains

### 2.3 Diagram References

- Every local diagram link must point to an existing file
- Figure references should match chapter context
- Companion GitHub links should be reachable and correctly named

### Flag Format

```
[REF] file:line — "referenced path" → missing or mismatched
```

---

## Part 3: Content Consistency

### 3.1 Opening Story Validation

- Opening section should connect to chapter theme with a concrete scenario
- Story should transition naturally into "In this chapter..." scope statement
- Keep prose specific and practical

### 3.2 Terminology Consistency

Verify that the same concept uses the same term throughout all chapters:
- "context window" vs "context length"
- "prompt injection" vs "prompt hijacking"
- API parameter names should be consistent across all chapters

### 3.3 Learning Progression

Check that concepts are introduced before they are used:
- No chapter should reference a technique that hasn't been explained in an earlier chapter
- Cross-references should point backward (to earlier chapters) or forward (to later chapters) appropriately

---

## Output Format

### Per-File Report

For each reviewed file, produce:

```
## file-path

### Formatting Issues
- [FORMAT] line N — pattern description

### Structure Issues
- [STRUCT] section description

### References
- [REF] line N — ...

### Consistency
- [CONSIST] term inconsistency

### Verdict: clean / N issues found
```

---

## How to Run This Review

1. Specify which chapters or files to review (e.g., `05-prompt-fundamentals.md` or `*`)
2. For each file, list every violation with line number, category, and the offending text
3. Provide the corrected version for each violation
4. After listing violations, apply fixes if the user approves

---

## Scope

This workflow applies to:

- Core chapter rules: `[0-9][0-9]-*.md` (01 to 14)
- Lightweight prose checks: `00-front-matter.md`, `00.5-how-to-use.md`, `appendix-*.md`, `cover-info/*.md`
