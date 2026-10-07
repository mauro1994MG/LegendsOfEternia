# Fuente del eBook "Toda la Verdad sobre Marca Personal"
- `content1.py`, `content1b.py`, `content2a.py`, `content2b.py`: texto de la introducción y los 17 capítulos (editable).
- `content3.py`: workbook, plan de 30 días, bonus y contraportada.
- `gen2.py`: portada, páginas iniciales y armado del libro. `style.css` y `extra.css`: diseño.
- `build.sh`: genera `build/book.pdf` con Chromium (dos pasadas para numerar el índice). Requiere Chromium y `pypdf`.
