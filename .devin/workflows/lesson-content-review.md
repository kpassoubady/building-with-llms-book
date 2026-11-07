---
description: Validate course lesson content for technical accuracy, reference integrity, outline alignment, and code correctness. Use after formatting is clean (run /course-content-review first).
---

# Lesson Content Review

Validate substance, not style. This workflow checks whether course content is technically accurate, internally consistent, and aligned with the master outline. Run this after `/course-content-review` has already cleaned up formatting.

This workflow does not re-check prose formatting. That is handled by `natural-prose-formatting` (during writing) and `/course-content-review` (during formatting review).

---

## Reference Files

These files are the source of truth for validation:

- **Master outline:** `catalog/Generative-AI-4Day-Detailed-Outline.md`
- **LLM client interface:** `shared/llm_client.py`
- **Setup guide:** `install/install.md`
- **Dependencies:** `requirements.txt`

---

## Part 1: Technical Fact-Checking

### 1.1 API and Parameter Accuracy

Verify every API parameter, function name, and technical claim against the actual codebase and provider documentation:

- Parameter names (`temperature`, `top_p`, `max_tokens`, `seed`, `stop`, `frequency_penalty`, `presence_penalty`) must match real API parameters.
- Function references to `shared/llm_client.py` must match the actual interface: `get_completion()`, `get_completion_full()`, `get_model()`, `show_config()`.
- Provider and model names must match `PROVIDER_MODELS` in `shared/llm_client.py`.
- Library names (`litellm`, `tiktoken`, `faiss-cpu`, `chromadb`) must match `requirements.txt`.

### 1.2 Model and Capability Claims

- Model names (GPT-4o, Claude Sonnet, Gemini Flash, etc.) must be current and correctly attributed to their providers.
- Claims about model capabilities (context window sizes, knowledge cutoffs, supported features) must be verifiable.
- Comparisons between models must be fair and factually grounded.

### 1.3 Conceptual Accuracy

- Technical explanations (tokenization, embeddings, attention, RAG pipeline, vector similarity) must be correct.
- Definitions must be precise. Flag vague or misleading simplifications that could confuse learners.
- Security guidance (API key management, prompt injection defenses, PII handling) must reflect current best practices.

### Flag Format

For each issue found:

```
[FACT] file:line — "quoted claim" → correction or concern
```

---

## Part 2: Code Validation

### 2.1 Code Examples in Slides

- Every code snippet shown on a slide must be syntactically valid Python.
- Imports must reference real packages from `requirements.txt`.
- Calls to `get_completion()` or `get_completion_full()` must use the correct signature.
- If a slide references a file (e.g., "see `shared/llm_client.py`"), that file must exist.

### 2.2 Lab Files

- Each lab file referenced in slides or the outline must exist under `day*/labs/`.
- Lab files must be runnable (correct imports, no undefined variables in the template).
- Lab numbering must be sequential within each day and match the outline.

### 2.3 Demo Files

- Each demo referenced in slides must exist under `day*/demos/`.
- Demo scripts must import from the correct paths.

### Flag Format

```
[CODE] file:line — description of the issue
```

---

## Part 3: Reference Integrity

### 3.1 File Existence

For every file path mentioned in slides, concept docs, or the outline, verify the file exists:

- `shared/llm_client.py`
- `install/install.md`
- `requirements.txt`
- Lab files (`day*/labs/lab*`)
- Demo files (`day*/demos/demo*`)
- Diagram files (`day*/diagrams/*.svg`)
- Concept docs (`day*/concepts/*.md`)

### 3.2 Cross-Day References

When a lesson references content from another day (e.g., "the chatbot from Lab 3.2" in Day 4), verify:

- The referenced lab/demo exists.
- The lab number is correct.
- The description matches what the referenced lab actually does.

### 3.3 Diagram References

- Every `<img>` tag or markdown image link in slides must point to an existing file.
- Every `.mmd` source in `day*/diagrams/` should have a corresponding `.svg`.

### Flag Format

```
[REF] file:line — "referenced path" → missing or mismatched
```

---

## Part 4: Outline Alignment

Compare each day's actual content against `catalog/Generative-AI-4Day-Detailed-Outline.md`.

### 4.1 Session Coverage

For each session listed in the outline, check:

- A corresponding slide deck exists (e.g., Session 1 of Day 1 maps to `day1/slides/01-*.md`).
- The topics listed in the outline appear in the slide content.
- Labs and demos mentioned in the outline have matching files.

### 4.2 Lab and Demo Inventory

Build a comparison table:

| Outline Reference | Expected File | Exists? | Content Matches? |
|:------------------|:--------------|:--------|:-----------------|
| Lab 1.1: Hello LLM | `day1/labs/lab1_1_hello_llm.py` | yes/no | yes/no/partial |

### 4.3 Missing Content

Flag any topic, lab, or demo listed in the outline that has no corresponding file or slide coverage.

### Flag Format

```
[ALIGN] outline-section — description of gap
```

---

## Part 5: Content Completeness

### 5.1 Learning Progression

Check that concepts are introduced before they are used:

- No slide should reference a term or technique that hasn't been explained in the same session or an earlier one.
- Day 2 content should not assume Day 3 knowledge, and so on.

### 5.2 Consistent Terminology

Verify that the same concept uses the same term throughout all days:

- If Day 1 calls it "context window," Day 3 should not call it "context length" without explanation.
- API parameter names should be consistent across all slides and labs.

---

## Output Format

### Per-File Report

For each reviewed file, produce:

```
## file-path

### Fact-Check
- [FACT] line N — ...

### Code
- [CODE] line N — ...

### References
- [REF] line N — ...

### Alignment
- [ALIGN] ...

### Verdict: clean / N issues found
```

### Summary Table

After all files, produce:

| Day | Session | Slides | Labs | Demos | Concepts | Issues |
|:----|:--------|:-------|:-----|:------|:---------|:-------|
| 1 | 1 | clean | clean | clean | clean | 0 |
| 1 | 2 | 2 issues | clean | n/a | 1 issue | 3 |

---

## How to Run This Review

1. Specify which day or files to review (e.g., `day2/` or `day4/slides/02-cost-latency-error-handling.md`).
2. Read the master outline to understand what the session should cover.
3. Read each target file and validate against Parts 1-5.
4. Produce the per-file report and summary table.
5. Apply fixes only if the user approves.

---

## Scope

This workflow applies to all files under:

- `day*/slides/*.md`
- `day*/concepts/*.md`
- `day*/labs/*.py`
- `day*/demos/*.py`
- `catalog/*.md`
- `shared/*.py`
- `install/*.md`
