#!/bin/bash
# Render all Mermaid .mmd files to SVG (with white edge casing for night mode)
# Usage: ./scripts/build-diagrams.sh [01|02|...|all] [--png|--svg|--both]
#
# Dependencies:
#   - npx (for mermaid-cli)
#   - pdf2svg (macOS: brew install pdf2svg | Linux: apt install pdf2svg)

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MERMAID_CONFIG="$REPO_ROOT/scripts/mermaid-config.json"
EDGE_CSS="$REPO_ROOT/scripts/edge-casing.css"
CASING_SCRIPT="$REPO_ROOT/scripts/add-edge-casing.py"

if [ ! -f "$MERMAID_CONFIG" ]; then
  echo "Error: mermaid config not found at $MERMAID_CONFIG"
  exit 1
fi

build_chapter() {
  local chapter=$1
  local format=$2
  local diagram_dir="$REPO_ROOT/diagrams"

  if [ ! -d "$diagram_dir" ]; then
    echo "No diagrams directory — skipping"
    return
  fi

  local pattern="*.mmd"
  if [ "$chapter" != "all" ]; then
    pattern="ch${chapter}-*.mmd"
  fi

  local mmd_count
  mmd_count=$(find "$diagram_dir" -maxdepth 1 -name "$pattern" | wc -l | tr -d ' ')
  if [ "$mmd_count" -eq 0 ]; then
    echo "No .mmd files matching $pattern in $diagram_dir — skipping"
    return
  fi

  if [ "$chapter" = "all" ]; then
    echo "Building all diagrams ($format)..."
  else
    echo "Building chapter $chapter diagrams ($format)..."
  fi

  for mmd_file in "$diagram_dir"/$pattern; do
    [ -e "$mmd_file" ] || continue
    local filename outputs
    filename=$(basename "$mmd_file" .mmd)
    outputs=""

    if [ "$format" = "png" ] || [ "$format" = "both" ]; then
      outputs="$filename.png"
      # -C edge-casing.css adds a white halo around connectors/arrowheads so the
      # transparent PNG stays legible on both light (day) and dark (night) pages.
      npx -y -p @mermaid-js/mermaid-cli mmdc \
        -i "$mmd_file" \
        -o "$diagram_dir/$filename.png" \
        -c "$MERMAID_CONFIG" \
        -C "$EDGE_CSS" \
        -b transparent \
        --scale 3 >/dev/null
    fi

    if [ "$format" = "svg" ] || [ "$format" = "both" ]; then
      [ -n "$outputs" ] && outputs="$outputs + $filename.svg" || outputs="$filename.svg"
      tmp_dir=$(mktemp -d -t "mmd-XXXXXX")
      tmp_pdf="$tmp_dir/$filename.pdf"
      # Render via PDF so we get vector paths for connector lines.
      # --pdfFit makes the page size match the chart content.
      npx -y -p @mermaid-js/mermaid-cli mmdc \
        -i "$mmd_file" \
        -o "$tmp_pdf" \
        -c "$MERMAID_CONFIG" \
        -b transparent \
        --pdfFit >/dev/null
      # Convert PDF to SVG with vector outlines.
      pdf2svg "$tmp_pdf" "$diagram_dir/$filename.svg"
      # Add a white vector casing under connectors/arrowheads so edges stay
      # visible on both light (day) and dark (night) backgrounds.
      python3 "$CASING_SCRIPT" "$diagram_dir/$filename.svg" >/dev/null
      rm -rf "$tmp_dir"
    fi

    echo "  $filename.mmd → $outputs"
  done
}

target="all"
format="svg"
for arg in "$@"; do
  case "$arg" in
    --png) format="png" ;;
    --svg) format="svg" ;;
    --both) format="both" ;;
    *) target="$arg" ;;
  esac
done

if [ "$format" = "svg" ] || [ "$format" = "both" ]; then
  if ! command -v pdf2svg >/dev/null 2>&1; then
    echo "Error: pdf2svg not found. Install with:"
    echo "  macOS: brew install pdf2svg"
    echo "  Linux: apt install pdf2svg"
    exit 1
  fi
fi

if [ "$target" = "all" ]; then
  build_chapter "all" "$format"
else
  build_chapter "$target" "$format"
fi

echo "Done."
