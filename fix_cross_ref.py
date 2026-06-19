import os
import re
import glob

book_dir = "/Users/kangs/code/github/building-with-llms-book"
md_files = glob.glob(os.path.join(book_dir, "*.md"))

patterns = [
    (re.compile(r'^\s*>\s*\[!TIP\]\n\s*>\s*\*\*Cross-Reference:\*\*\s*(.*)$', re.MULTILINE), r'\1'), # Fix TIPs that still have Cross-Reference
    (re.compile(r'^\s*>\s*\*\*Cross-Reference:\*\*\s*', re.MULTILINE), r''), # Remove > **Cross-Reference:**
    (re.compile(r'\*\*Cross-Reference:\*\*\s*', re.MULTILINE), r''), # Remove **Cross-Reference:**
    (re.compile(r'\bCross-reference\s+\[Chapter', re.MULTILINE | re.IGNORECASE), r'See [Chapter'), # Fix 'Cross-reference [Chapter'
    (re.compile(r'^\s*Cross-Reference:\s*', re.MULTILINE), r''), # Remove Cross-Reference: without bold
]

for filepath in md_files:
    if "CLAUDE.md" in filepath or "book-order.json" in filepath:
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for pattern, replacement in patterns:
        content = pattern.sub(replacement, content)
        
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

# In 09-conversation-design.md we have two cross-references next to each other
content_09 = open(os.path.join(book_dir, "09-conversation-design.md")).read()
content_09 = content_09.replace(
    "For a deeper dive into message roles (system, user, assistant) and how to structure system messages, see [Chapter 3](03-working-with-llm-apis.md): Working with LLM APIs and [Chapter 5](05-prompt-fundamentals.md): Prompt Engineering Fundamentals.\n\nIf your chatbot needs to answer questions from a large knowledge base that exceeds the context window, see [Chapter 11](11-rag-architecture.md): Retrieval-Augmented Generation (RAG) for a more scalable approach than message history alone.",
    "For a deeper dive into message roles (system, user, assistant) and how to structure system messages, see [Chapter 3](03-working-with-llm-apis.md): Working with LLM APIs and [Chapter 5](05-prompt-fundamentals.md): Prompt Engineering Fundamentals. If your chatbot needs to answer questions from a large knowledge base that exceeds the context window, see [Chapter 11](11-rag-architecture.md): Retrieval-Augmented Generation (RAG) for a more scalable approach than message history alone."
)
with open(os.path.join(book_dir, "09-conversation-design.md"), 'w') as f:
    f.write(content_09)

print("Done")
