#!/bin/bash
set -e
S=$(cd "$(dirname "$0")" && pwd)
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
[ -x "$CH" ] || CH=$(ls /opt/pw-browsers/chromium-1194/*/chrome | head -1)
pr() { "$CH" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --virtual-time-budget=5000 --print-to-pdf="$2" "file://$1" 2>/dev/null; }
mkdir -p "$S/build/fonts"; cp "$S/cover.jpg" "$S/build/"; cp "$S/fonts/anton.woff2" "$S/build/fonts/"
python3 -I "$S/gen.py" "$S/build/ebook.html" > "$S/build/keys.json"
pr "$S/build/ebook.html" "$S/build/pass1.pdf"
PAGES=$(python3 -I - "$S/build/pass1.pdf" <<'PY'
import sys, json, re
from pypdf import PdfReader
r = PdfReader(sys.argv[1])
out = {}
for i, pg in enumerate(r.pages):
    if i < 5: continue
    T = (pg.extract_text() or '').upper()
    op = 'MÉTODO V.A.R.C.' in T and 'VISIBILIDAD' in T
    if op and 'CAPÍTULO' in T:
        m = re.search(r'\n(\d{2})\n', T)
        if m: out.setdefault('c%d' % int(m.group(1)), i+1)
    if op and 'INTRODUCCIÓN' in T: out.setdefault('intro', i+1)
    if op and 'CONCLUSIÓN' in T: out.setdefault('concl', i+1)
    if 'WORKBOOK PROFESIONAL' in T and 'HERRAMIENTAS' in T: out.setdefault('wb', i+1)
    if i > 12 and '15 HOOKS PARA EMPEZAR' in T: out.setdefault('bonus', i+1)
print(json.dumps(out))
PY
)
echo "$PAGES" >&2
python3 -I "$S/gen.py" "$S/build/ebook.html" "$PAGES" > /dev/null
pr "$S/build/ebook.html" "$S/build/ebook.pdf"
