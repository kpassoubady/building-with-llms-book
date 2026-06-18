import os
import glob
import re

book_dir = "/Users/kangs/code/github/building-with-llms-book"
script_file = os.path.join(book_dir, "scripts/generate-excalidraw-diagrams.py")

with open(script_file, "r") as f:
    content = f.read()

new_content = re.sub(r's\.save\("(.+?)\.excalidraw"\)', r's.save("\1-sketch.excalidraw")', content)
if new_content != content:
    with open(script_file, "w") as f:
        f.write(new_content)
    print("Updated python script to append -sketch")

for f in glob.glob(os.path.join(book_dir, '*.md')):
    with open(f, 'r') as file:
        content = file.read()
    
    new_content = re.sub(r'(\./diagrams/[a-zA-Z0-9-_\.]+?)(?<!-sketch)\.png', r'\1-sketch.png', content)
    
    if new_content != content:
        with open(f, 'w') as file:
            file.write(new_content)
        print(f"Updated markdown links in {os.path.basename(f)}")
