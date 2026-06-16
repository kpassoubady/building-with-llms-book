# Appendix E: Architecture & Matrices

Throughout the book, we discuss complex technical architectures, processing pipelines, and comparison matrices. For readability, the full-page Excalidraw diagrams for these concepts are collected here and hosted in the [building-with-llms-companion](https://github.com/kpassoubady/building-with-llms-companion/tree/main/diagrams) repository.

You can view the high-resolution `.png` exports or download the editable `.excalidraw` source files to modify them for your own presentations and design docs.

## Diagram Inventory

### [Chapter 1](01-intro-genai-llms.md#how-transformers-work-simplified): The Transformer Architecture
**File:** [`ch01-transformer-full.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch01-transformer-full.png)
A complete visual breakdown of the Transformer architecture, including input embeddings, positional encoding, multi-head attention (Q/K/V), feed-forward layers, and output probabilities.

### [Chapter 4](04-capabilities-limitations.md#where-llms-excel): Model Capability Matrix
**File:** [`ch04-capability-matrix.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch04-capability-matrix.png)
A full capability matrix mapping 10 common generative AI tasks against their reliability rating, the best-in-class model for that task, and the associated cost tier.

### [Chapter 6](06-prompting-techniques.md#summary-of-techniques): Prompting Technique Matrix
**File:** [`ch06-technique-matrix.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch06-technique-matrix.png)
A detailed comparison of 6 advanced prompting techniques (e.g., Zero-Shot, Few-Shot, Chain-of-Thought, ReAct), detailing when to use them, pros, cons, and an example task.

### [Chapter 8](08-iteration-evaluation.md#evaluation-methods): Evaluation Pipeline
**File:** [`ch08-eval-pipeline.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch08-eval-pipeline.png)
A visualization of the complete evaluation pipeline: taking a Golden Dataset, passing it through a Prompt Runner, scoring it with an LLM-as-Judge, and finally generating a metrics report.

### [Chapter 10](10-embeddings-vector-databases.md#chunking-strategies): Chunking and Indexing Pipeline
**File:** [`ch10-chunking-indexing.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch10-chunking-indexing.png)
A structural flow of the document ingestion process, tracing the path from raw documents (PDF/Text) to Document Loaders, Text Splitters, Embedding Models, and ultimately the Vector Database.

### [Chapter 11](11-rag-architecture.md#the-two-pipelines): RAG Architecture (Full)
**File:** [`ch11-rag-full.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch11-rag-full.png)
The complete Retrieval-Augmented Generation (RAG) architecture, bridging the offline ingestion pipeline with the real-time query pipeline and the evaluation feedback loops.

### [Chapter 13](13-cost-optimization.md#cost-optimization-strategies): Cost Optimization Decision Tree
**File:** [`ch13-cost-decision-tree.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch13-cost-decision-tree.png)
A practical decision tree for cost optimization, branching through prompt shortening, caching implementation, and model tier switching, with estimated savings percentages at each leaf.

### [Chapter 14](14-ethics-evaluation.md#detecting-bias): Production Evaluation Harness
**File:** [`ch14-eval-harness.png`](https://github.com/kpassoubady/building-with-llms-companion/blob/main/diagrams/ch14-eval-harness.png)
A robust production evaluation harness architecture, flowing from Golden Datasets to Multi-Scorers, Drift Monitors, and alerting systems (PagerDuty/Slack).
