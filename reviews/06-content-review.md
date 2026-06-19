## 06-prompting-techniques.md

### Formatting Issues
- [FORMAT] line 585, 594, etc. — Knowledge Check questions are not bolded (e.g., `1. Multiple Choice:` instead of `1. **Multiple Choice:**`).
- [FORMAT] line 615 — The `<summary>` tag content is not bolded (`<summary>Click to Reveal Answers</summary>` instead of `<summary><strong>Click to Reveal Answers</strong></summary>`).
- [FORMAT] line 617-621 — Knowledge Check answers do not use the exact `1. **Answer**:` prefix format. They omit the "Answer" word entirely.
- [FORMAT] line 441 — Diagram `diagrams/ch06-technique-ladder.svg` is embedded using an HTML `<img>` tag instead of standard Markdown `![alt](url)` syntax. Diagrams must use markdown image syntax.
- [FORMAT] line 520, 524 — Consecutive Admonitions. A `> [!NOTE]` block is immediately followed by a `> [!TIP]`.

### Structure Issues
- [STRUCT] Admonitions — Too many `[!TIP]` admonitions (4 instead of the maximum allowed 1-2). 
- [STRUCT] Admonitions — Invalid admonition type `[!PROMPT]` used at line 311.

### References
- [REF] No broken references found.

### Consistency
- [CONSIST] No terminology inconsistencies found.

### Verdict: 7 issues found
