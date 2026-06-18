---
description: Guide and workflow for creating or converting book coding exercises into the standard companion repo pattern (start/ and solution/).
---

# Book Companion Exercise Guide & Workflow

This document serves as both a **workflow** for converting existing flat book exercises into the companion format, and a **style guide** for creating future coding exercises for the *Building with LLMs* book.

By following this pattern, we ensure all coding exercises provide a consistent, high-quality developer experience for readers, with clear boilerplate, guided instructions, and reference solutions, without "spoilers" directly in the code file.

---

## The Book Companion Pattern

Instead of creating flat lab files (e.g., `exercises/ch03/hello_llm.py`), every coding exercise should be structured as follows within the companion repository:

```text
exercises/
└── chXX/
    └── exercise_name/
        ├── README.md       <-- Exercise instructions, setup, and expected output
        ├── start/          <-- Boilerplate code with TODO markers for readers
        │   └── code.py
        └── solution/       <-- Fully completed, working reference code
            └── code.py
```

### 1. The `solution/` Directory
This directory contains the final, working version of the code. 
- The code must be fully tested and operational.
- It serves as the reference implementation if a reader gets stuck.

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
Each exercise folder must have a `README.md` that adheres to this standard structure:

- **Title**: e.g., `# Exercise: Building a QA Bot`
- **Goal**: A brief description of what the reader will accomplish.
- **Setup**: Provide a brief note reminding readers to activate their virtual environment, and link to the central root [Setup Instructions](../../../README.md) if necessary.
- **Instructions**: Step-by-step guidance.
  - Direct the reader to the `start/` directory.
  - Explain what file to open and what `TODO`s to look for.
  - Provide the exact terminal command to run the script (e.g., `python start/qa_bot.py`).
- **Getting Stuck?**: A brief section reminding the reader to check the `solution/` directory if they need help.

---

## Workflow: Converting Existing Book Exercises

When instructed to convert existing book exercises (e.g., "Refactor Chapter 3 exercises"), follow these steps autonomously:

### Step 1: Analyze
1. Review the existing flat `.py` file in the source `exercises/chXX/` directory.
2. Read the docstring to understand the instructions, inputs, and expected output.

### Step 2: Create the Structure
1. Create a new directory named after the exercise (e.g., `exercises/chXX/hello_llm/`).
2. Create `start/` and `solution/` subdirectories within it.

### Step 3: Populate `solution/`
1. Copy the original `.py` file into the `solution/` directory.
2. If the original file contains `# Hint:` blocks that represent the solution, uncomment them to make the code fully operational, and remove the `TODO` lines from the solution file.

### Step 4: Generate `start/` Code
1. Copy the original `.py` file into the `start/` directory.
2. Strip out the operational solution logic (or keep it commented out / deleted). 
3. Ensure explicit `TODO` markers remain.
4. Remove the giant multi-line docstring containing instructions from the top of the file, as it will be moved to the README.

### Step 5: Write the `README.md`
1. Extract the instructions, goals, and expected output from the original file's docstring.
2. Create the `README.md` in the exercise root directory using the standard structure, moving the documentation there.

### Step 6: Cleanup
1. Delete the original flat `.py` file from the `chXX/` directory.
2. Verify that the book chapters linking to this exercise are updated to point to the new directory via `/tree/main/...` instead of the raw `.py` file.
