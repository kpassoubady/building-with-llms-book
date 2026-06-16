# Building with LLMs: The Developer's Handbook

Book manuscript repository. Contains 14 chapters, 5 appendices, diagrams, illustrations, and build configuration for PDF/EPUB generation.

## Related repositories

| Repo | Path | Purpose |
| :--- | :--- | :--- |
| gen-ai | `../gen-ai` | Instructor-led 4-day course (slides, labs, demos, diagrams) |
| building-with-llms-companion | `../building-with-llms-companion` | Book companion exercises, solutions, capstone projects |
| gen-ai-setup | `../gen-ai-setup` | Pre-class setup, install guides, environment verification |

## Repository structure

```
building-with-llms-book/
  00-dedication.md              Dedication page
  00-front-matter.md            Preface (audience, prerequisites, conventions)
  00.5-how-to-use.md            Reading guide (4-part structure, reading paths)

  Part I: Foundations (Chapters 1-4)
  01-intro-genai-llms.md        Transformer architecture, tokenization, embeddings
  02-llm-landscape.md           Model comparison (GPT-4, Claude, Gemini, Llama)
  03-working-with-llm-apis.md   API setup, litellm, first calls
  04-capabilities-limitations.md  Strengths, failures, hallucinations

  Part II: Prompt Engineering (Chapters 5-8)
  05-prompt-fundamentals.md     4 building blocks, system vs user messages
  06-prompting-techniques.md    Zero-shot, few-shot, CoT, role prompting
  07-api-parameters.md          Temperature, top_p, max_tokens, streaming
  08-iteration-evaluation.md    Testing, golden datasets, LLM-as-judge

  Part III: Conversational AI & RAG (Chapters 9-11)
  09-conversation-design.md     Multi-turn chatbots, context management
  10-embeddings-vector-databases.md  Embeddings, FAISS, Chroma, Pinecone
  11-rag-architecture.md        RAG pipeline, chunking, retrieval

  Part IV: Production & Responsible AI (Chapters 12-14)
  12-security-guardrails.md     API key management, prompt injection, moderation
  13-cost-optimization.md       Token economics, caching, batch processing
  14-ethics-evaluation.md       Bias detection, fairness, human-in-the-loop

  appendix-a-labs.md            Links to companion repo exercises
  appendix-b-capstone.md        Capstone project guidelines
  appendix-c-setup.md           Environment setup instructions
  appendix-d-resources.md       Additional resources and references
  appendix-e-diagrams.md        High-resolution architecture diagrams

  diagrams/                     SVG diagrams (ch##-name.svg)
  images/                       Chapter illustrations (hero-ch##.png, fact-ch##.png)
  cover-info/                   Cover images and author bio

  builder/
    build.sh                    Build script for PDF/EPUB/DOCX
    book-order.json             Book configuration, styling, content processing
    pdf/                        Generated output files
```

## Build system

The book uses `bookbuilder` for PDF/EPUB generation.

```bash
cd builder
./build.sh pdf               # generate PDF
./build.sh epub              # generate EPUB
./build.sh pdf --order FILE  # use custom chapter order
```

Output lands in `builder/pdf/`.

## Chapter conventions

Each chapter follows a consistent structure:

1. Chapter title: `# N. Chapter Name`
2. Learning objectives callout: `> **Learning Objectives**`
3. Opening narrative (real-world story or problem)
4. Hero illustration: `<img src="images/hero-ch##.png" ... style="float:right; margin-left:20px; width:200px; border-radius:8px;" />`
5. Main content with H2/H3 sections
6. Try It Yourself section: `## Try It Yourself`
7. Chapter Summary: `## Chapter Summary`
8. Knowledge Check: `## Knowledge Check`

## Callout blocks

Use GitHub-style admonitions:

```markdown
> [!NOTE]
> **Did You Know?** Interesting facts.

> [!TIP]
> **Cross-Reference:** See [Chapter X](XX-file.md)

> [!IMPORTANT]
> Critical information.

> [!PROMPT]
> Example prompt to try.

> [!TRY IT]
> Hands-on exercise.

> [!KEY CONCEPT]
> Important definition.
```

## Writing style

- No em dash or en dash. Use comma, period, colon, parentheses, or plain hyphen.
- No antithesis patterns ("not just X, it's Y"). State what the thing IS.
- No hedging filler ("It's worth noting", "In essence", "At its core").
- No hype words ("powerful", "game-changing", "revolutionary").
- No LLM openers ("Let's dive in", "In today's world").
- Bold on first introduction of key terms. Not mid-paragraph for emphasis.
- Cross-references use relative paths: `[Chapter X](XX-file.md)`

## Diagrams and images

- Diagrams live in `diagrams/` as SVG files, named `ch##-name.svg`
- Referenced as: `![Description](diagrams/ch##-name.svg)`
- Chapter illustrations live in `images/` as PNG files
- Hero images: `hero-ch##.png` (chapter opening, floated right)
- Fact images: `fact-ch##.png` (concept illustration)

## Code examples

- Python is the primary language
- Use `from shared import get_completion` pattern (matching companion repo)
- Include expected output in comments where helpful
- Show both good and bad examples for teaching contrast

## File naming

- Chapters: `NN-chapter-name.md` (01 through 14)
- Appendices: `appendix-X-name.md` (A through E)
- Front matter: `00-dedication.md`, `00-front-matter.md`, `00.5-how-to-use.md`
- Diagrams: `ch##-name.svg`
- Images: `hero-ch##.png`, `fact-ch##.png`

## Common tasks

- Edit a chapter: modify the corresponding `NN-*.md` file at the repo root.
- Add a diagram: create SVG in `diagrams/` named `ch##-name.svg`, reference in chapter markdown.
- Add a chapter illustration: place PNG in `images/` following `hero-ch##.png` or `fact-ch##.png` naming.
- Rebuild the book: run `./builder/build.sh pdf` (or `epub`).
- Update build config: edit `builder/book-order.json` (page size, fonts, margins, admonition styles).
- Add a cross-reference: link as `[Chapter N](NN-file.md)` in a `[!TIP]` callout.

## Book metadata

- Title: Building with LLMs: The Developer's Handbook
- Author: Kangeyan Passoubady (Kangs)
- Page size: 6in x 9in
- Body font: Inter, 9pt, line-height 1.6
- Code font: SF Mono, 7pt
- Heading color: #1a1a2e
- Body color: #333333
