# Tapas completas de Biblia (contraportada + lomo + portada) en varios diseños, listas para imprimir.
# Medidas en milímetros. Cambiá TW/TH/SPINE/BLEED según tu imprenta y volvé a correr build.sh.
import sys, os, json

HERE = os.path.dirname(os.path.abspath(__file__))
P = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
TW = P.get('tw', 152.4)       # ancho de la tapa (corte final)
TH = P.get('th', 228.6)       # alto de la tapa (corte final)
SP = P.get('spine', 30.0)     # ancho del lomo
BL = P.get('bleed', 3.0)      # sangrado
GUIDES = P.get('guides', False)
OUTDIR = P.get('outdir', os.path.join(HERE, 'out'))
os.makedirs(OUTDIR, exist_ok=True)
W = 2 * TW + SP + 2 * BL
H = TH + 2 * BL

VERSE = 'Porque de tal manera amó Dios al mundo, que ha dado á su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.'
VREF = 'Juan 3:16'
BLURB = 'La Palabra de Dios en un solo volumen, Antiguo y Nuevo Testamento, para guiarte, consolarte y fortalecerte cada día, en tu casa, en tu iglesia y en tu camino.'

def cross(color, w, stroke=None, thin=False):
    t = 7 if thin else 16
    vx = 50 - t / 2
    hy = 40 - t / 2
    return (f'<svg viewBox="0 0 100 150" width="{w}mm" height="{w*1.5}mm" xmlns="http://www.w3.org/2000/svg">'
            f'<rect x="{vx}" y="0" width="{t}" height="150" fill="{color}"/><rect x="8" y="{hy}" width="84" height="{t}" fill="{color}"/></svg>')

def orn(color, w=60):
    return (f'<svg viewBox="0 0 120 12" width="{w}mm" height="{w/10}mm" xmlns="http://www.w3.org/2000/svg">'
            f'<rect x="0" y="5.5" width="48" height="1" fill="{color}"/><rect x="72" y="5.5" width="48" height="1" fill="{color}"/>'
            f'<rect x="54" y="0" width="12" height="12" transform="rotate(45 60 6)" fill="{color}"/></svg>')

BASE_CSS = '''
@page { size: __W__mm __H__mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { width: __W__mm; height: __H__mm; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.cov { position: relative; width: __W__mm; height: __H__mm; overflow: hidden; }
.bg { position: absolute; inset: 0; }
.panel { position: absolute; top: __BL__mm; height: __TH__mm; overflow: hidden; }
.back { left: __BL__mm; width: __TW__mm; }
.spine { left: calc(__BL__mm + __TW__mm); width: __SP__mm; }
.front { left: calc(__BL__mm + __TW__mm + __SP__mm); width: __TW__mm; }
.abs { position: absolute; }
.c { left: 0; right: 0; text-align: center; }
.spt { position: absolute; left: 0; right: 0; top: 0; bottom: 0; display: flex; align-items: center; justify-content: center; }
.spt span { writing-mode: vertical-rl; white-space: nowrap; }
.bar { position: absolute; right: 14mm; bottom: 14mm; width: 50mm; height: 30mm; background: #fff; display: flex; align-items: center; justify-content: center; font: 500 6.5pt Arial, sans-serif; color: #777; text-align: center; letter-spacing: .5pt; }
.g { position: absolute; pointer-events: none; }
'''

def page(css, inner, name):
    c = (BASE_CSS + css)
    for k, v in {'__W__': W, '__H__': H, '__BL__': BL, '__TW__': TW, '__TH__': TH, '__SP__': SP}.items():
        c = c.replace(k, str(v))
    guides = ''
    if GUIDES:
        guides = (f'<div class="g" style="left:{BL}mm;top:{BL}mm;width:{2*TW+SP}mm;height:{TH}mm;border:.3mm dashed #ff2d2d"></div>'
                  f'<div class="g" style="left:{BL+TW}mm;top:0;width:.3mm;height:{H}mm;background:#ff00ff"></div>'
                  f'<div class="g" style="left:{BL+TW+SP}mm;top:0;width:.3mm;height:{H}mm;background:#ff00ff"></div>'
                  f'<div class="g" style="left:{BL+10}mm;top:{BL+10}mm;width:{TW-20}mm;height:{TH-20}mm;border:.25mm dashed #00b7ff"></div>'
                  f'<div class="g" style="left:{BL+TW+SP+10}mm;top:{BL+10}mm;width:{TW-20}mm;height:{TH-20}mm;border:.25mm dashed #00b7ff"></div>'
                  f'<div class="g" style="left:{BL+TW+2}mm;top:{BL+4}mm;width:{SP-4}mm;height:{TH-8}mm;border:.25mm dashed #00c853"></div>')
    html = (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{name}</title><style>'
            f'{open(os.path.join(HERE, "fonts.css")).read()}{c}</style></head><body><div class="cov">{inner}{guides}</div></body></html>')
    open(os.path.join(OUTDIR, name + '.html'), 'w').write(html)

verse_html = lambda col, sub: (f'<div class="abs c" style="top:62mm;padding:0 20mm;font:italic 500 15pt/1.45 \'Cormorant Garamond\',serif;color:{col}">“{VERSE}”</div>'
                               f'<div class="abs c" style="top:112mm;font:600 9pt Cinzel,serif;letter-spacing:4pt;color:{sub}">{VREF.upper()}</div>')
blurb_html = lambda col: f'<div class="abs c" style="top:128mm;padding:0 22mm;font:500 11pt/1.55 \'Cormorant Garamond\',serif;color:{col}">{BLURB}</div>'

# ---------- 1. Clásica negro y oro ----------
GOLD = '#CDA64F'
css1 = f'''
.bg {{ background: radial-gradient(ellipse at 50% 38%, #221d15 0%, #0e0c0a 70%); }}
.fr {{ position:absolute; inset: 9mm; border: .6mm solid {GOLD}; }}
.fr2 {{ position:absolute; inset: 11.4mm; border: .25mm solid {GOLD}; }}
.sq {{ position:absolute; width:3.2mm; height:3.2mm; background:{GOLD}; }}
'''
corners = lambda: ''.join(f'<div class="sq" style="{p}"></div>' for p in ['left:7.4mm;top:7.4mm', 'right:7.4mm;top:7.4mm', 'left:7.4mm;bottom:7.4mm', 'right:7.4mm;bottom:7.4mm'])
in1 = f'''<div class="bg"></div>
<div class="panel back"><div class="fr"></div><div class="fr2"></div>{corners()}
 <div class="abs c" style="top:24mm">{cross(GOLD, 11)}</div>
 {verse_html('#EADFC4', GOLD)}
 <div class="abs c" style="top:118mm">{orn(GOLD, 50)}</div>
 {blurb_html('#D9CDB0').replace('top:128mm', 'top:132mm')}
 <div class="bar">CÓDIGO DE BARRAS / ISBN</div></div>
<div class="panel spine">
 <div class="abs c" style="top:16mm">{cross(GOLD, 8)}</div>
 <div class="spt"><span style="font:700 24pt Cinzel,serif;letter-spacing:7pt;color:{GOLD}">SANTA BIBLIA</span></div>
 <div class="abs c" style="bottom:16mm">{orn(GOLD, 20)}</div></div>
<div class="panel front"><div class="fr"></div><div class="fr2"></div>{corners()}
 <div class="abs c" style="top:30mm">{cross(GOLD, 26)}</div>
 <div class="abs c" style="top:103mm;font:600 22pt Cinzel,serif;letter-spacing:14pt;padding-left:14pt;color:{GOLD}">SANTA</div>
 <div class="abs c" style="top:117mm;font:700 70pt/1 Cinzel,serif;letter-spacing:3pt;color:{GOLD}">BIBLIA</div>
 <div class="abs c" style="top:150mm">{orn(GOLD, 70)}</div>
 <div class="abs c" style="top:164mm;font:400 11pt Cinzel,serif;letter-spacing:5pt;padding-left:5pt;color:#EADFC4">ANTIGUO Y NUEVO TESTAMENTO</div></div>'''
page(css1, in1, '1_Clasica_negro_y_oro')

# ---------- 2. Azul noche y plata ----------
SIL = '#DCE1EC'
css2 = f'''
.bg {{ background: linear-gradient(180deg, #0b1535 0%, #12285a 55%, #0a1230 100%); }}
.rays {{ position:absolute; inset:0; background: repeating-conic-gradient(from 0deg at 50% 36%, rgba(255,255,255,.085) 0deg 3.2deg, rgba(255,255,255,0) 3.2deg 11deg); }}
.fade {{ position:absolute; inset:0; background: radial-gradient(ellipse 62% 68% at 50% 36%, rgba(11,21,53,0) 22%, rgba(11,21,53,.97) 96%); }}
.halo {{ position:absolute; left:50%; top:36%; width:120mm; height:120mm; margin:-60mm 0 0 -60mm; border-radius:50%; background: radial-gradient(circle, rgba(220,230,255,.42) 0%, rgba(160,185,255,.14) 40%, rgba(160,185,255,0) 68%); }}
.ring {{ position:absolute; left:50%; top:36%; width:52mm; height:52mm; margin:-26mm 0 0 -26mm; border-radius:50%; border:.5mm solid {SIL}; }}
'''
in2 = f'''<div class="bg"></div>
<div class="panel back">
 <div class="abs c" style="top:24mm">{cross(SIL, 10)}</div>
 {verse_html('#E8ECF5', '#9FB4E8')}
 <div class="abs c" style="top:118mm">{orn(SIL, 46)}</div>
 {blurb_html('#C9D2E8').replace('top:128mm', 'top:132mm')}
 <div class="bar">CÓDIGO DE BARRAS / ISBN</div></div>
<div class="panel spine">
 <div class="abs c" style="top:16mm">{cross(SIL, 8)}</div>
 <div class="spt"><span style="font:700 24pt Cinzel,serif;letter-spacing:7pt;color:{SIL}">SANTA BIBLIA</span></div>
 <div class="abs c" style="bottom:16mm">{orn(SIL, 20)}</div></div>
<div class="panel front"><div class="rays"></div><div class="fade"></div><div class="halo"></div><div class="ring"></div>
 <div class="abs c" style="top:63.5mm">{cross(SIL, 24)}</div>
 <div class="abs c" style="top:122mm;font:600 20pt Cinzel,serif;letter-spacing:14pt;padding-left:14pt;color:#9FB4E8">SANTA</div>
 <div class="abs c" style="top:135mm;font:700 68pt/1 Cinzel,serif;letter-spacing:3pt;color:{SIL}">BIBLIA</div>
 <div class="abs c" style="top:168mm">{orn(SIL, 60)}</div>
 <div class="abs c" style="top:182mm;font:400 10.5pt Cinzel,serif;letter-spacing:5pt;padding-left:5pt;color:{SIL}">ANTIGUO Y NUEVO TESTAMENTO</div></div>'''
page(css2, in2, '2_Azul_noche_y_plata')

# ---------- 3. Marfil minimalista ----------
INK = '#1d1a16'; ACC = '#A8832F'
css3 = f'''
.bg {{ background: #F3EEE3; }}
.ln {{ position:absolute; background:{INK}; }}
'''
in3 = f'''<div class="bg"></div>
<div class="panel back">
 <div class="abs c" style="top:30mm">{cross(INK, 8, thin=True)}</div>
 {verse_html(INK, ACC).replace("top:62mm", "top:66mm").replace("top:112mm", "top:116mm")}
 <div class="abs c" style="top:132mm"><div style="width:14mm;height:.5mm;background:{ACC};margin:0 auto"></div></div>
 {blurb_html('#4a443b').replace('top:128mm', 'top:140mm')}
 <div class="bar" style="border:.2mm solid #cfc8b8">CÓDIGO DE BARRAS / ISBN</div></div>
<div class="panel spine">
 <div class="abs c" style="top:16mm">{cross(INK, 7, thin=True)}</div>
 <div class="spt"><span style="font:700 25pt 'Cormorant Garamond',serif;letter-spacing:5pt;color:{INK}">Santa Biblia</span></div>
 <div class="abs c" style="bottom:16mm"><div style="width:.5mm;height:12mm;background:{ACC};margin:0 auto"></div></div></div>
<div class="panel front">
 <div class="abs c" style="top:34mm">{cross(INK, 28, thin=True)}</div>
 <div class="abs c" style="top:122mm;font:700 54pt/1 'Cormorant Garamond',serif;color:{INK}">Santa Biblia</div>
 <div class="abs c" style="top:150mm"><div style="width:20mm;height:.6mm;background:{ACC};margin:0 auto"></div></div>
 <div class="abs c" style="top:158mm;font:500 11pt Cinzel,serif;letter-spacing:5pt;padding-left:5pt;color:#4a443b">ANTIGUO Y NUEVO TESTAMENTO</div></div>'''
page(css3, in3, '3_Marfil_minimalista')

# ---------- 4. Bordó y dorado ----------
G4 = '#D8B25E'
css4 = f'''
.bg {{ background: radial-gradient(ellipse at 50% 35%, #7a1829 0%, #4d0b17 70%, #36060f 100%); }}
.fr {{ position:absolute; inset: 9mm; border: .5mm solid {G4}; }}
.br {{ position:absolute; width:16mm; height:16mm; border: 1mm solid {G4}; }}
.circ {{ position:absolute; left:50%; top:34%; width:58mm; height:58mm; margin:-29mm 0 0 -29mm; border-radius:50%; border:.8mm solid {G4}; }}
.circ2 {{ position:absolute; left:50%; top:34%; width:52mm; height:52mm; margin:-26mm 0 0 -26mm; border-radius:50%; border:.25mm solid {G4}; }}
'''
brs = lambda: ''.join(f'<div class="br" style="{p}"></div>' for p in ['left:6mm;top:6mm;border-right:0;border-bottom:0', 'right:6mm;top:6mm;border-left:0;border-bottom:0', 'left:6mm;bottom:6mm;border-right:0;border-top:0', 'right:6mm;bottom:6mm;border-left:0;border-top:0'])
in4 = f'''<div class="bg"></div>
<div class="panel back"><div class="fr"></div>{brs()}
 <div class="abs c" style="top:24mm">{cross(G4, 11)}</div>
 {verse_html('#F3E4C1', G4)}
 <div class="abs c" style="top:118mm">{orn(G4, 50)}</div>
 {blurb_html('#E9D6AE').replace('top:128mm', 'top:132mm')}
 <div class="bar">CÓDIGO DE BARRAS / ISBN</div></div>
<div class="panel spine">
 <div class="abs c" style="top:16mm">{cross(G4, 8)}</div>
 <div class="spt"><span style="font:700 24pt Cinzel,serif;letter-spacing:7pt;color:{G4}">LA SANTA BIBLIA</span></div>
 <div class="abs c" style="bottom:16mm">{orn(G4, 20)}</div></div>
<div class="panel front"><div class="fr"></div>{brs()}<div class="circ"></div><div class="circ2"></div>
 <div class="abs c" style="top:61mm">{cross(G4, 22)}</div>
 <div class="abs c" style="top:118mm;font:600 14pt Cinzel,serif;letter-spacing:10pt;padding-left:10pt;color:{G4}">LA</div>
 <div class="abs c" style="top:128mm;font:600 24pt Cinzel,serif;letter-spacing:12pt;padding-left:12pt;color:#F3E4C1">SANTA</div>
 <div class="abs c" style="top:142mm;font:700 66pt/1 Cinzel,serif;letter-spacing:3pt;color:{G4}">BIBLIA</div>
 <div class="abs c" style="top:175mm">{orn(G4, 64)}</div>
 <div class="abs c" style="top:187mm;font:400 10.5pt Cinzel,serif;letter-spacing:5pt;padding-left:5pt;color:#F3E4C1">ANTIGUO Y NUEVO TESTAMENTO</div></div>'''
page(css4, in4, '4_Bordo_y_dorado')

# ---------- 5. Moderno naranja y negro ----------
OR = '#FF6B00'
css5 = f'''
.bg {{ background: radial-gradient(circle 120mm at 12% 22%, rgba(255,107,0,.34) 0%, rgba(255,107,0,0) 100%), radial-gradient(circle 120mm at 90% 14%, rgba(255,107,0,.34) 0%, rgba(255,107,0,0) 100%), #0D0D0D; }}
.ospine {{ position:absolute; top:0; bottom:0; left:{BL+TW}mm; width:{SP}mm; background:{OR}; }}
.oblock {{ position:absolute; left:{BL+TW}mm; right:0; bottom:0; height:{BL+118}mm; background:{OR}; }}
'''
in5 = f'''<div class="bg"></div><div class="ospine"></div><div class="oblock"></div>
<div class="panel back">
 <div class="abs" style="left:16mm;right:16mm;top:28mm">{cross(OR, 9)}</div>
 <div class="abs" style="left:16mm;right:16mm;top:62mm;font:italic 500 15pt/1.45 'Cormorant Garamond',serif;color:#fff">“{VERSE}”</div>
 <div class="abs" style="left:16mm;top:112mm;font:600 9pt Cinzel,serif;letter-spacing:4pt;color:{OR}">{VREF.upper()}</div>
 <div class="abs" style="left:16mm;right:22mm;top:128mm;font:500 11pt/1.55 'Cormorant Garamond',serif;color:#d8d8d8">{BLURB}</div>
 <div class="bar">CÓDIGO DE BARRAS / ISBN</div></div>
<div class="panel spine">
 <div class="abs c" style="top:16mm">{cross('#0D0D0D', 8)}</div>
 <div class="spt"><span style="font:400 30pt Anton,Impact,sans-serif;letter-spacing:5pt;color:#0D0D0D">BIBLIA</span></div></div>
<div class="panel front">
 <div class="abs" style="left:16mm;top:24mm;font:700 9pt Cinzel,serif;letter-spacing:6pt;color:#e8e8e8">LA PALABRA DE DIOS</div>
 <div class="abs" style="left:16mm;top:34mm">{cross(OR, 20)}</div>
 <div class="abs" style="left:16mm;right:10mm;top:66mm;font:400 112pt/1 Anton,Impact,sans-serif;color:#fff;letter-spacing:1pt">BIBLIA</div>
 <div class="abs" style="left:16mm;right:12mm;top:126mm;font:600 12pt Cinzel,serif;letter-spacing:6pt;color:#0D0D0D">ANTIGUO Y NUEVO<br>TESTAMENTO</div>
 <div class="abs" style="left:16mm;right:12mm;bottom:20mm;font:500 12pt/1.4 'Cormorant Garamond',serif;color:#0D0D0D">Una Biblia para leer, entender y vivir cada día.</div></div>'''
page(css5, in5, '5_Moderno_naranja_y_negro')

print(json.dumps({'W': W, 'H': H, 'files': sorted(f for f in os.listdir(OUTDIR) if f.endswith('.html'))}))
