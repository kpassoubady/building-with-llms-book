#!/bin/bash
# Build all Marp slide decks to PDF
# Usage: ./scripts/build-slides.sh [day1|day2|day3|day4|all]

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
THEME="$REPO_ROOT/assets/theme.css"

build_day() {
  local day=$1
  local slide_dir="$REPO_ROOT/$day/slides"
  local pdf_dir="$slide_dir/pdf"

  if [ ! -d "$slide_dir" ]; then
    echo "No slides directory for $day — skipping"
    return
  fi

  local md_count
  md_count=$(find "$slide_dir" -maxdepth 1 -name '*.md' | wc -l | tr -d ' ')
  if [ "$md_count" -eq 0 ]; then
    echo "No .md files in $slide_dir — skipping"
    return
  fi

  mkdir -p "$pdf_dir"
  echo "Building $day slides → $pdf_dir/"

  for md_file in "$slide_dir"/*.md; do
    local filename
    filename=$(basename "$md_file" .md)
    echo "  $filename.md → $filename.pdf"
    marp --pdf --theme "$THEME" --allow-local-files "$md_file" -o "$pdf_dir/$filename.pdf"
  done
}

target="${1:-all}"

if [ "$target" = "all" ]; then
  for day in day1 day2 day3 day4; do
    build_day "$day"
  done
else
  build_day "$target"
fi

echo "Done."
