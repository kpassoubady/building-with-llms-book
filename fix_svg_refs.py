import glob
import re

files_to_fix = [
    "13-cost-optimization.md",
    "08-iteration-evaluation.md",
    "11-rag-architecture.md",
    "06-prompting-techniques.md",
    "04-capabilities-limitations.md",
]

for filename in files_to_fix:
    with open(filename, 'r') as f:
        content = f.read()
    
    new_content = re.sub(
        r'diagrams/(ch04-preprocessing|ch04-strengths-weaknesses|ch04-where-llms-excel|ch06-technique-matrix|ch08-eval-pipeline|ch11-rag-5-steps|ch13-token-cost)\.svg',
        r'diagrams/\1-sketch.svg',
        content
    )
    
    if new_content != content:
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Fixed {filename}")
