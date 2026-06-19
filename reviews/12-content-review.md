## 12-security-guardrails.md

### Formatting Issues
- [FORMAT] line 27, 168, 390 — antithesis pattern ("not just..."). Fix: Rephrase to remove "not just".
- [FORMAT] line 139 — Consecutive Admonitions. A `> [!TIP]` (line 136) is followed immediately by a `> [!NOTE]` (line 139).
- [FORMAT] line 122 — Invalid admonition type `> [!PROMPT]`. Admonitions must be NOTE, TIP, IMPORTANT, WARNING, or CAUTION.
- [FORMAT] line 427-435 — Knowledge Check answers inside `<details>` do not follow the exact `1. **Answer**:` format. Currently they use `1. **(b) ...` and `2. **Partially true.**` etc.

### Structure Issues
- [STRUCT] Admonitions — Too many `[!TIP]` admonitions (3 instead of the maximum allowed 1-2). 
- [STRUCT] Admonitions — Invalid admonition types `[!PROMPT]` used.

### References
- [REF] line 203 — `![Defense-in-depth security rings](diagrams/ch12-defense-rings.svg)` has an invalid adjacent `<img>` tag copying an illustration alt text. Diagrams must use standard markdown formatting and not `<img>` tags.

### Consistency
- [CONSIST] No terminology inconsistencies found.

### Verdict: 6 issues found
