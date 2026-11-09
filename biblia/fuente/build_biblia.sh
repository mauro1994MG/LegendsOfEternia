#!/bin/bash
# Uso: ./build_biblia.sh '{"tw":152.4,"th":228.6,"spine":30,"bleed":3}'  -> genera PDFs en out/ y vista previa en prev/
set -e
S=$(cd "$(dirname "$0")" && pwd)
CH=$(ls /opt/pw-browsers/chromium-*/chrome-linux*/chrome 2>/dev/null | head -1); [ -x "$CH" ] || CH=$(which google-chrome)
ARGS=${1:-'{}'}
rm -rf "$S/out" "$S/prev"; mkdir -p "$S/out" "$S/prev"
python3 -I "$S/gen_biblia.py" "$ARGS" > "$S/out/info.json"
for f in "$S"/out/*.html; do
  n=$(basename "$f" .html)
  "$CH" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --virtual-time-budget=4000 --print-to-pdf="$S/out/$n.pdf" "file://$f" 2>/dev/null
  pdftoppm -r 110 -png -singlefile "$S/out/$n.pdf" "$S/prev/$n" 2>/dev/null
done
cat "$S/out/info.json"; ls "$S/out"/*.pdf
