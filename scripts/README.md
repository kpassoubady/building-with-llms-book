# Building with LLMs - Scripts Guide

This directory contains utility scripts to generate and build assets (diagrams and slides) for the book.

## Usage Guide

### 1. Building Mermaid Diagrams
**Script:** `build-diagrams.sh`

Builds Mermaid (`.mmd`) files into `.svg` or `.png` formats, with automatic support for white edge casing to ensure legibility on both light and dark backgrounds.

**Usage:**
```bash
./scripts/build-diagrams.sh [chapter_number|all] [--png|--svg|--both]
```

**Examples:**
- `./scripts/build-diagrams.sh all` (Builds all `.mmd` diagrams in the repo as SVG by default)
- `./scripts/build-diagrams.sh 01` (Builds all Chapter 1 diagrams as SVG)
- `./scripts/build-diagrams.sh 04 --both` (Builds Chapter 4 diagrams as both PNG and SVG)

**Dependencies:**
- `npx` (for `@mermaid-js/mermaid-cli`)
- `pdf2svg` (`brew install pdf2svg` on macOS or `apt install pdf2svg` on Linux)
- Python 3 (for the `add-edge-casing.py` helper script)

---

### 2. Exporting Excalidraw Diagrams
**Script:** `export-excalidraw.sh`

Exports all `.excalidraw` source diagrams in the `book/diagrams` folder to SVG (primary) and PNG formats. It uses `excalidraw-render` to produce clean vector lines instead of hand-drawn squiggles.

**Usage:**
```bash
./scripts/export-excalidraw.sh [--svg-only|--png-only]
```

**Examples:**
- `./scripts/export-excalidraw.sh` (Exports both SVG and PNG)
- `./scripts/export-excalidraw.sh --svg-only` (Exports SVG only)

**Dependencies:**
- `pip install excalidraw-render`

---

### 3. Building Slides
**Script:** `build-slides.sh`

Builds markdown (`.md`) Marp slide decks into PDF documents.

**Usage:**
```bash
./scripts/build-slides.sh [day1|day2|day3|day4|all]
```

**Examples:**
- `./scripts/build-slides.sh all` (Builds PDFs for all days)
- `./scripts/build-slides.sh day1` (Builds PDFs for day 1 only)

**Dependencies:**
- `marp` (`npm install -g @marp-team/marp-cli` or similar)
