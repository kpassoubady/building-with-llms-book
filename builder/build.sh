#!/usr/bin/env bash
# Build Building with LLMs: The Developer's Handbook ebook
# Usage: ./build.sh [pdf|epub|docx] [--order FILE]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
ORDER_FILE="$SCRIPT_DIR/book-order.json"
OUTPUT_DIR="$SCRIPT_DIR/pdf"
TEMP_DIR="$SCRIPT_DIR/temp"
FORMAT="pdf"

while [[ $# -gt 0 ]]; do
  case "$1" in
    -F|--format) FORMAT="$2"; shift 2 ;;
    -o|--order) ORDER_FILE="$2"; shift 2 ;;
    *) FORMAT="$1"; shift ;;
  esac
done

echo "Building GenAI Prompt Engineering Handbook ($FORMAT)..."
echo "  Root:   $ROOT_DIR"
echo "  Order:  $ORDER_FILE"
echo "  Output: $OUTPUT_DIR"
echo "  Temp:   $TEMP_DIR"
echo ""

bookbuilder build \
  --root "$ROOT_DIR" \
  --order "$ORDER_FILE" \
  --output-dir "$OUTPUT_DIR" \
  --temp "$TEMP_DIR" \
  --format "$FORMAT" \
  --force

echo ""
echo "Done. Output in: $OUTPUT_DIR"
