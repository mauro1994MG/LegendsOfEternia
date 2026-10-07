#!/bin/bash
set -e
S=$(cd "$(dirname "$0")" && pwd)
CH=$(ls /opt/pw-browsers/chromium-1194/*/chrome | head -1)
pr() { "$CH" --headless=new --no-sandbox --disable-gpu --no-pdf-header-footer --virtual-time-budget=5000 --print-to-pdf="$2" "file://$1" 2>/dev/null; }
mkdir -p "$S/build/fonts"; cp "$S/fonts/anton.woff2" "$S/build/fonts/"
python3 -I "$S/gen2.py" "$S/build/book.html" > "$S/build/keys.json"
pr "$S/build/book.html" "$S/build/pass1.pdf"
PAGES=$(python3 -I - "$S/build/pass1.pdf" <<'PY'
import sys, json, re
from pypdf import PdfReader
r = PdfReader(sys.argv[1]); out = {}
for i, pg in enumerate(r.pages):
    if i < 5: continue
    T = (pg.extract_text() or '').upper()
    op = all(x in T for x in ['ANTES DE EMPEZAR', 'POSICIONAMIENTO', 'CONTENIDO', 'SISTEMA']) and 'RECORRIDO DEL LIBRO' in T
    if op and 'CAPÍTULO' in T:
        m = re.search(r'\n(\d{2})\n', T)
        if m: out.setdefault('c%d' % int(m.group(1)), i+1)
    if op and 'INTRODUCCIÓN' in T: out.setdefault('intro', i+1)
    if op and 'CONCLUSIÓN' in T: out.setdefault('concl', i+1)
    if 'TUS EJERCICIOS' in T and 'HERRAMIENTAS' in T: out.setdefault('wb', i+1)
    if 'PLAN DE ACCIÓN DE 30 DÍAS' in T and 'wb' in out: out.setdefault('plan', i+1)
    if i > 12 and '20 GANCHOS PARA EMPEZAR' in T: out.setdefault('bonus', i+1)
print(json.dumps(out))
PY
)
echo "$PAGES" >&2
python3 -I "$S/gen2.py" "$S/build/book.html" "$PAGES" > /dev/null
pr "$S/build/book.html" "$S/build/book.pdf"
