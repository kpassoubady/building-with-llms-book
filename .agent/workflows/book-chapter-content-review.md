---
description: Review book chapters to remove AI-generated formatting tells, enforce consistent style, and validate chapter structure
---

# Book Chapter Content Review

Strip LLM-style formatting patterns from book chapters (`book/*.md`, `book/cover-info/*.md`, `book/appendix-*.md`). Inherits rules from `natural-prose-formatting` (no em/en dashes, no antithesis, no hedging, no bold/list abuse in prose).

## 1. Structure
Every chapter must include:
- Learning objectives (blockquote, 3 items, action verbs)
- Opening story (2-3 paragraphs, **scene-specific 3-5 word headline**)
- Content sections (separated by `---` only if inside code blocks; `---` in prose is forbidden)
- Try It Yourself (`## Try It Yourself`, 2-3 mini exercises)
- Chapter Summary (bulleted list `> **💡 Key Takeaways**`, then `[!PITFALLS]` block with exactly 3 bullets)
- Knowledge Check (`## 🧠 Knowledge Check`, 5 questions)

## 2. Admonitions
Use 3-5 per chapter (`[!NOTE]`, `[!TIP]`, `[!WARNING]`, `[!IMPORTANT]`, `[!CAUTION]`).
- Concise (1-3 sentences), bold label (e.g., "**Did You Know?**").
- **Consecutive TIPs:** Two `> [!TIP]` blocks must NEVER appear consecutively. Either combine them, replace one, or introduce a bridging prose line between them.
- Cross-references: `**Cross-Reference:** For a deeper dive into X, see [Chapter Y](YY-filename.md): Title.`

## 3. Code Blocks
- Syntactically valid, concise (5-20 lines), comments included.
- Must show code AND output.
- **No deep string alignment:** Break after comma, 4-space indent for continuation strings.
- Point to companion repo for >20 lines: `> Full exercise: [repo/path](url)`

## 4. Tables & Lists
- Left-aligned headers (`:---`), no trailing pipes.
- Bullet lists for 3+ items. For 2 items, use prose ("and"/"or").
- Nested bullets need empty line before them and exactly 4-space indent.
- Comparison tables (`Approach | Pros | Cons | When to Use`) only when appropriate to the chapter flow.

## 5. Cross-references & Diagrams
- Chapter links: Must be clickable markdown links to target (e.g., `[Chapter 7](07-api-parameters.md)`).
- Diagrams inline (SVG or ≤6 element Excalidraw PNG). >6 elements go to companion repo.

## 6. Prose Style
- Bold: Headings, table headers, term definitions, admonition labels. No random bolding.
- Paragraphs: One idea, 3-5 sentences max. Split if longer.

## 7. Knowledge Check Format
```markdown
## 🧠 Knowledge Check

1. **Multiple Choice:** Question?
    ::: {.mcq-2col}
    - [ ] Option A
    - [ ] Option B
    :::

2. **True or False:** Statement?
    ::: {.tf-inline}
    - [ ] True
    - [ ] False
    :::

3. **Fill in the Blank:** The ______ is answer.

<details>
<summary><strong>Click to Reveal Answers</strong></summary>

1. **Answer**: Explanation.
2. **True/False**: Explanation.
3. **Answer**: Explanation.

</details>
```
*Note: Nested bullets need empty line before them. `<details>` block needs empty line before `</details>`.*

## LLM-Tell Detection Checklist
Flag: `—`, `–`, "not just X, it's Y", "It's worth noting", "In essence", "Furthermore", random bolding, hyperbole ("powerful"), "Let's dive in", "In today's world", `---` outside code blocks, standalone `Common Pitfalls` (must be `[!PITFALLS]` with exactly 3 bullets), missing links.

## Reference Integrity
- Verify file existence for diagrams, code, and cross-references.
- Validate `shared/llm_client.py` signatures and `requirements.txt`.
- Opening story must scope the chapter ("In this chapter, you will learn...").

## Output
Produce report per file:
```
## file-path
### Formatting Issues
- [FORMAT] line N — ...
### Structure Issues
- [STRUCT] section ...
### References
- [REF] line N — ...
### Consistency
- [CONSIST] term ...
### Verdict: clean / N issues found
```
