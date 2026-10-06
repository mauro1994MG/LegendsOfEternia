# Fuente del eBook "De Invisible a Referente"

- `gen.py` — contenido y estructura del libro (texto editable).
- `style.css` — diseño (naranja / negro / blanco, formato 6×9 in).
- `build.sh` — genera `build/ebook.pdf` con Chromium headless (dos pasadas para numerar el índice).

Para regenerar: `./build.sh` (requiere Chromium y `pypdf`).
