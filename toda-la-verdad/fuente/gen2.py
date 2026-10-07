# Generador del eBook "Toda la Verdad sobre Marca Personal" -> HTML para imprimir a PDF con Chromium.
import json, sys, os, random

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
TOC_PAGES = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}

H = []
def add(s): H.append(s)

# ---------- bloques ----------
def p(t): return f'<p>{t}</p>'
def lead(t): return f'<p class="lead">{t}</p>'
def h3(t): return f'<h3>{t}</h3>'
def quote(t): return f'<blockquote class="pull"><span class="qm">“</span>{t}</blockquote>'
def formula(steps, label=None, sep='→'):
    lab = f'<div class="flabel">{label}</div>' if label else ''
    items = f'<span class="arr">{sep}</span>'.join(f'<span class="fstep">{s}</span>' for s in steps)
    return f'<div class="formula">{lab}<div class="fsteps">{items}</div></div>'
def deflist(rows, cls=''):
    r = ''.join(f'<div class="drow"><div class="dterm">{a}</div><div class="ddef">{b}</div></div>' for a, b in rows)
    return f'<div class="deflist {cls}">{r}</div>'
def ul(items): return '<ul class="bul">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def ol(items): return '<ol class="num">' + ''.join(f'<li><span class="n">{k+1:02d}</span><span>{i}</span></li>' for k, i in enumerate(items)) + '</ol>'
def checks(items): return '<ul class="checks">' + ''.join(f'<li><span class="box"></span><span>{i}</span></li>' for i in items) + '</ul>'
def case(title, *blocks): return f'<div class="case"><div class="ctag">Ejemplo ilustrativo</div><div class="ctitle">{title}</div>{"".join(blocks)}</div>'
def exercise(title, *blocks, tag='Ejercicio'): return f'<div class="exer"><div class="etag">✎ {tag}</div><div class="etitle">{title}</div>{"".join(blocks)}</div>'
def note(t): return f'<div class="note"><b>Nota:</b> {t}</div>'
def keybox(title, *blocks): return f'<div class="keybox"><div class="ktitle">{title}</div>{"".join(blocks)}</div>'
def learn(t): return f'<div class="learn">{t}</div>'
def lines(n=2): return '<div class="wlines">' + '<div class="wl"></div>' * n + '</div>'
def wq(q, n=2): return f'<div class="wq"><div class="wqt">{q}</div>{lines(n)}</div>'
def chips(items): return '<div class="chips">' + ''.join(f'<span>{i}</span>' for i in items) + '</div>'
def compare(a_title, a_items, b_title, b_items):
    la = ''.join(f'<li>{i}</li>' for i in a_items); lb = ''.join(f'<li>{i}</li>' for i in b_items)
    return (f'<div class="cmp"><div class="cmpa"><div class="cmph">{a_title}</div><ul>{la}</ul></div>'
            f'<div class="cmpb"><div class="cmph">{b_title}</div><ul>{lb}</ul></div></div>')
def table2(h1, h2, rows):
    r = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in rows)
    return f'<table class="mtable"><tr><th>{h1}</th><th>{h2}</th></tr>{r}</table>'

OACT = ('<div class="oact"><div class="oai">24h</div><div><div class="oat">Aplicación práctica</div>'
        '<div class="oax">Mientras leés este capítulo, buscá <b>una decisión concreta</b> que puedas implementar durante las próximas 24 horas.</div></div></div>')
PARTS = ['Antes de empezar', 'Posicionamiento', 'Contenido', 'Sistema']

def tracker(active):
    cells = ''
    for i, nme in enumerate(PARTS):
        on = ' on' if i in active else ''
        cells += f'<div class="tcell{on}"><div class="tl">{i+1}</div><div class="tn">{nme}</div></div>'
    return f'<div class="tracker">{cells}</div>'

TOC = []
def opener(label, num, title, sub, active, key, act=True):
    numhtml = f'<div class="onum">{num}</div>' if num else ''
    add(f'''<section class="opener" id="{key}">
  <div class="oglow"></div>
  <div class="otop"><span class="olabel">{label}</span><span class="obrand">Toda la verdad sobre marca personal</span></div>
  {numhtml}
  <h1 class="otitle">{title}</h1>
  <div class="obar"></div>
  <p class="osub">{sub}</p>
  {OACT if act else ''}
  <div class="obottom"><div class="ometh">Recorrido del libro</div>{tracker(active)}</div>
</section>''')

def body(*blocks):
    add('<section class="body">' + ''.join(blocks) + '</section>')

def chapter(key, label, num, title, sub, active, *blocks, toc_title=None, with_action=True):
    TOC.append((key, num or '', toc_title or title.replace('<br>', ' '), label))
    opener(label, num, title, sub, active, key, with_action)
    body(*blocks)

# ---------- PORTADA (vectorial, sin imágenes) ----------
random.seed(7)
cols, rows_, dx, dy = 13, 11, 31, 31
orange_cells = {(2, 3), (5, 1), (8, 4), (10, 2), (4, 6), (7, 8), (1, 8), (11, 9), (6, 5)}
dots = ''
for r in range(rows_):
    for c in range(cols):
        cx, cy = 22 + c * dx, 22 + r * dy
        if (c, r) in orange_cells:
            dots += f'<circle cx="{cx}" cy="{cy}" r="9.5" fill="#FF6B00"/><circle cx="{cx}" cy="{cy}" r="15" fill="none" stroke="#FF6B00" stroke-opacity=".35" stroke-width="1.3"/>'
        else:
            dots += f'<circle cx="{cx}" cy="{cy}" r="5.5" fill="#3a3632"/>'
add(f'''<section class="cover2">
  <div class="cv-glow"></div>
  <div class="cv-top"><span></span>GUÍA PRÁCTICA 2026<span></span></div>
  <div class="cv-title"><div class="t1">TODA LA</div><div class="t2">VERDAD</div><div class="t3">SOBRE MARCA<br>PERSONAL</div></div>
  <div class="cv-swoosh"></div>
  <p class="cv-sub">Cómo construir una marca que atraiga <b>clientes</b>, no solo seguidores.</p>
  <svg class="cv-dots" viewBox="0 0 {22*2 + (cols-1)*dx} {22*2 + (rows_-1)*dy}" preserveAspectRatio="xMidYMid meet">{dots}</svg>
  <div class="cv-legend"><span class="lg1"></span>Seguidores<span class="lg2"></span>Clientes</div>
  <div class="cv-badge">INCLUYE<b>WORKBOOK</b>Plan de 30 días</div>
  <div class="cv-author"><b>EMANUEL GALVÁN</b><span>Experto en Marketing Digital</span></div>
</section>''')

# ---------- PÁGINA DE TÍTULO ----------
add('''<section class="titlepage">
  <div class="oglow big"></div>
  <div class="tp-kicker">Guía práctica · Edición 2026</div>
  <div class="tp-title">TODA LA <span>VERDAD</span><br>SOBRE MARCA<br>PERSONAL</div>
  <div class="tp-swoosh"></div>
  <p class="tp-sub">Cómo construir una marca que atraiga <b>clientes</b>, no solo seguidores.</p>
  <div class="tp-pill">Emanuel Galván</div>
  <div class="tp-by">Experto en Marketing Digital</div>
  <div class="tp-includes">Incluye: Workbook · Plan de 30 días · 20 ganchos · Checklists</div>
</section>''')

# ---------- LEGAL ----------
add('''<section class="body legal">
  <div class="legal-inner">
  <div class="lg-title">TODA LA VERDAD SOBRE MARCA PERSONAL</div>
  <div class="lg-sub">Emanuel Galván · Edición 2026</div>
  <p>© 2026 Emanuel Galván. Todos los derechos reservados.</p>
  <p>Ninguna parte de esta publicación puede ser reproducida, distribuida, revendida ni transmitida por ningún medio sin autorización previa y por escrito del titular de los derechos. La compra de este eBook otorga una licencia de uso personal e intransferible.</p>
  <p><b>Aviso sobre resultados.</b> Los ejemplos de este libro son ilustrativos: los uso para explicar ideas y no representan a personas ni resultados reales. Nada de lo que leas aquí es promesa ni garantía de ingresos o de crecimiento. Tus resultados dependen de tu mercado, tu oferta, tu dedicación y otros factores.</p>
  <p><b>Aviso general.</b> El contenido tiene fines educativos. No sustituye asesoramiento legal, fiscal, sanitario ni financiero profesional. Las marcas y empresas que menciono como ilustración pertenecen a sus propietarios y no tienen relación con esta obra.</p>
  </div>
</section>''')

# ---------- CÓMO USAR ESTE LIBRO ----------
add('''<section class="body howto">
  <div class="kicker">Antes de empezar</div>
  <h2 class="ptitle">Cómo usar este libro</h2>
  <p class="lead">Escribí este libro para que lo apliques, no solo para que lo leas. Cada idea viene con un ejemplo, un ejercicio y una decisión para tomar en las próximas 24 horas.</p>
  <div class="howgrid">
    <div class="hg"><div class="hgi">01</div><div><b>Leé un capítulo.</b> Cada uno desarrolla una pieza del sistema con ideas y ejemplos.</div></div>
    <div class="hg"><div class="hgi">02</div><div><b>Hacé el ejercicio.</b> Los recuadros naranjas convierten la teoría en decisiones.</div></div>
    <div class="hg"><div class="hgi">03</div><div><b>Decidí en 24 horas.</b> Cada capítulo abre con un desafío concreto.</div></div>
    <div class="hg"><div class="hgi">04</div><div><b>Completá el workbook.</b> Al final tenés las plantillas para diseñar tu marca.</div></div>
  </div>
  <div class="kicker" style="margin-top:6mm">El mapa del recorrido</div>
  <h2 class="ptitle sm">Cuatro partes</h2>
  <div class="varc">
    <div class="vc"><div class="vl">1</div><div class="vn">Antes de empezar</div><div class="vd">Definir qué querés lograr y desde qué lugar.</div></div>
    <div class="vc"><div class="vl">2</div><div class="vn">Posicionamiento</div><div class="vd">Elegir por qué querés ser recordado.</div></div>
    <div class="vc"><div class="vl">3</div><div class="vn">Contenido</div><div class="vd">Crear piezas que construyan confianza.</div></div>
    <div class="vc"><div class="vl">4</div><div class="vn">Sistema</div><div class="vd">Sostenerlo en el tiempo sin quemarte.</div></div>
  </div>
  <p class="small muted">Los ejemplos con personas o negocios son ilustrativos; no constituyen garantía de resultados.</p>
</section>''')

add('%%TOC%%')

for f in ['content1.py', 'content1b.py', 'content2a.py', 'content2b.py', 'content3.py']:
    exec(open(os.path.join(HERE, f)).read())

# ---------- ÍNDICE ----------
rows = ''
for key, num, title, label in TOC:
    pg = TOC_PAGES.get(key, '')
    numcell = num if num else {'Introducción': '—', 'Conclusión': '—', 'Herramientas': 'WB', 'Bonus': '★'}.get(label, '')
    cls = ' special' if not num else ''
    rows += f'<a class="trow{cls}" href="#{key}"><span class="tn">{numcell}</span><span class="tt">{title}</span><span class="dots"></span><span class="tp">{pg}</span></a>'
toc_html = f'<section class="body toc"><div class="kicker">Contenido</div><h2 class="ptitle">Índice</h2><div class="toclist">{rows}</div></section>'

html = ''.join(H).replace('%%TOC%%', toc_html)
css = open(os.path.join(HERE, 'style.css')).read() + open(os.path.join(HERE, 'extra.css')).read()
open(OUT, 'w').write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Toda la Verdad sobre Marca Personal</title><style>{css}</style></head><body>{html}</body></html>')
print(json.dumps([k for k, *_ in TOC]))
