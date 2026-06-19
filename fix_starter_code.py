import glob
import re
import os

for filename in glob.glob("*.md"):
    with open(filename, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    new_lines = []
    i = 0
    in_starter_code_block = False
    
    while i < len(lines):
        line = lines[i]
        
        # Check for blockquoted Starter Code TIP
        if line == "> [!TIP]" and i+1 < len(lines) and "> **Starter Code:**" in lines[i+1]:
            # Found blockquoted Starter Code TIP
            p_text = lines[i+1].replace("> **Starter Code:**", "").strip()
            # Ensure it ends with a colon
            if p_text.endswith("."): p_text = p_text[:-1] + ":"
            elif not p_text.endswith(":"): p_text += ":"
            new_lines.append(p_text)
            new_lines.append("") # Blank line
            in_starter_code_block = True
            i += 2
            continue
            
        # Check for non-blockquoted Starter Code
        if line.startswith("**Starter Code:**") or line.startswith("> **Starter Code:**"):
            p_text = line.replace("> **Starter Code:**", "").replace("**Starter Code:**", "").strip()
            if p_text.endswith("."): p_text = p_text[:-1] + ":"
            elif not p_text.endswith(":"): p_text += ":"
            new_lines.append(p_text)
            new_lines.append("") # Blank line
            in_starter_code_block = True
            i += 1
            continue
            
        if in_starter_code_block:
            if line.startswith("> - "):
                new_lines.append(line.replace("> - ", "- "))
            elif line.startswith("- "):
                new_lines.append(line)
            elif line.strip() == "" or line.strip() == ">":
                # Skip empty lines immediately after the starter code paragraph because we already added one
                pass
            else:
                # We reached the end of the starter code section
                in_starter_code_block = False
                new_lines.append("") # Ensure blank line before next section (usually ## Chapter Summary)
                new_lines.append(line)
        else:
            new_lines.append(line)
            
        i += 1
        
    # Write back
    new_content = '\n'.join(new_lines)
    # clean up multiple blank lines just in case
    new_content = re.sub(r'\n{3,}', '\n\n', new_content)
    
    if new_content != content:
        with open(filename, 'w') as f:
            f.write(new_content)
        print(f"Updated {filename}")
