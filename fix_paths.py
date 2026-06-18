import os
import re

book_dir = "/Users/kangs/code/github/building-with-llms-book"
export_sh = os.path.join(book_dir, "scripts/export-excalidraw.sh")

with open(export_sh, "r") as f:
    content = f.read()

new_content = re.sub(r'DIAGRAMS_DIR="\$\(cd "\$\(dirname "\$0"\)/\.\./book/diagrams" && pwd\)"', 
                     r'DIAGRAMS_DIR="$(cd "$(dirname "$0")/../diagrams" && pwd)"', content)

if new_content != content:
    with open(export_sh, "w") as f:
        f.write(new_content)
    print("Fixed export-excalidraw.sh")
