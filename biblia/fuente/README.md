# Tapas de Biblia (contraportada + lomo + portada)
Para cambiar las medidas con los datos de tu imprenta:
`./build_biblia.sh '{"tw":152.4,"th":228.6,"spine":30,"bleed":3}'`
- tw / th: ancho y alto de una tapa (corte final), en mm
- spine: ancho del lomo, en mm
- bleed: sangrado, en mm
Requiere Chromium y poppler (pdftoppm). Los PDF salen en `out/`.
