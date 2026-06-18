---
description: Guide and workflow for creating or converting coding exercises into the standard companion repo pattern (start/ and solution/).
---

# Companion Exercise Guide & Workflow

This document serves as both a **workflow** for converting existing raw labs into the companion format, and a **style guide** for creating future coding exercises for any course.

By following this pattern, we ensure all coding exercises provide a consistent, high-quality developer experience for students, with clear boilerplate, guided instructions, and reference solutions.

---

## The Companion Pattern

Instead of creating flat lab files, every coding exercise should be structured as follows within the companion repository:

```text
dayX/
└── session-name-or-topic/
    ├── README.md       <-- Session guide, setup, and instructions
    ├── start/          <-- Boilerplate code with TODO markers for students
    │   └── lab_code.py
    └── solution/       <-- Fully completed, working reference code
        └── lab_code.py
```

### 1. The `solution/` Directory
This directory contains the final, working version of the code. 
- The code must be fully tested and operational.
- It serves as the reference implementation if a student gets stuck.

### 2. The `start/` Directory
This directory contains the exact same files as the `solution/` directory, but with the core implementation details removed.
- Leave imports, boilerplate, and function signatures intact.
- Remove the "meat" of the exercise (e.g., the LLM API call, the specific prompt string, the data parsing logic).
- Replace the removed code with explicit `TODO` comments explaining what needs to be implemented.
- **Example:**
  ```python
  # TODO: Construct the messages array with a SYSTEM message and the user's prompt
  # TODO: Call the get_completion function and return the result
  ```

### 3. The `README.md`
Each session folder must have a `README.md` that adheres to this standard structure:

- **Title**: e.g., `# Morning Session: Building a QA Bot`
- **Objective**: A numbered list of the parts/goals of the exercise.
- **Setup**: Provide a brief note reminding students to activate their virtual environment, and link to the central root [Setup Instructions](../../../README.md).
- **Instructions**: Step-by-step guidance.
  - Direct the student to the `start/` directory.
  - Explain what file to open and what `TODO`s to look for.
  - Provide the exact terminal command to run the script (e.g., `python 01_hello_llm.py`).
- **Getting Stuck?**: A brief section reminding the student to check the `solution/` directory if they need help.

---

## Workflow: Converting Existing Labs

When instructed to convert existing labs (e.g., "Convert `/Users/kangs/code/github/gen-ai/day2/labs` to the companion format"), follow these steps autonomously:

### Step 1: Analyze and Group
1. Review the existing files in the source `labs/` directory.
2. Group the labs logically into sessions (e.g., `morning-topic` and `afternoon-topic`) based on their numbering and content.

### Step 2: Create the Structure
1. Create the corresponding session directories in the companion repository (e.g., `/Users/kangs/code/github/gen-ai-companion/day2/morning-topic/`).
2. Create `start/` and `solution/` subdirectories within each session directory.

### Step 3: Populate `solution/`
1. Copy the original, working lab files directly into the `solution/` directories.

### Step 4: Generate `start/` Code
1. Copy the lab files into the `start/` directories.
2. Carefully strip out the learning objective logic and replace it with instructional `TODO` comments as outlined in the pattern above.

### Step 5: Write the `README.md` files
1. Generate the session `README.md` using the standard structure, tailored to the specific files in that session, linking to the root setup instructions.
2. Inside the `start/` and `solution/` folders, create a small `README.md` that links to the root setup guide. For example:
   ```markdown
   # Start / Boilerplate Code
   
   Before running these scripts, ensure your Python environment is activated. See the [Setup Instructions](../../../README.md).
   ```

### Step 6: Cleanup
1. Once the conversion is fully implemented and verified in the companion repository, **delete the original `labs/` directory** from the main course repository.
