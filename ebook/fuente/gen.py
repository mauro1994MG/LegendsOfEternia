# Generador del eBook "De Invisible a Referente" -> HTML listo para imprimir a PDF con Chromium.
import json, sys, os

OUT = sys.argv[1]
TOC_PAGES = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}

H = []
def add(s): H.append(s)

# ---------- helpers de bloques ----------
def p(t): return f'<p>{t}</p>'
def lead(t): return f'<p class="lead">{t}</p>'
def h3(t): return f'<h3>{t}</h3>'
def quote(t): return f'<blockquote class="pull"><span class="qm">“</span>{t}</blockquote>'
def formula(steps, label=None):
    lab = f'<div class="flabel">{label}</div>' if label else ''
    items = '<span class="arr">→</span>'.join(f'<span class="fstep">{s}</span>' for s in steps)
    return f'<div class="formula">{lab}<div class="fsteps">{items}</div></div>'
def deflist(rows, cls=''):
    r = ''.join(f'<div class="drow"><div class="dterm">{a}</div><div class="ddef">{b}</div></div>' for a, b in rows)
    return f'<div class="deflist {cls}">{r}</div>'
def ul(items): return '<ul class="bul">' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'
def ol(items): return '<ol class="num">' + ''.join(f'<li><span class="n">{k+1:02d}</span><span>{i}</span></li>' for k, i in enumerate(items)) + '</ol>'
def checks(items): return '<ul class="checks">' + ''.join(f'<li><span class="box"></span><span>{i}</span></li>' for i in items) + '</ul>'
def case(title, *blocks): return f'<div class="case"><div class="ctag">Caso práctico</div><div class="ctitle">{title}</div>{"".join(blocks)}</div>'
def exercise(title, *blocks, tag='Ejercicio'): return f'<div class="exer"><div class="etag">✎ {tag}</div><div class="etitle">{title}</div>{"".join(blocks)}</div>'
def note(t): return f'<div class="note"><b>Nota:</b> {t}</div>'
def keybox(title, *blocks): return f'<div class="keybox"><div class="ktitle">{title}</div>{"".join(blocks)}</div>'
def action(): return ('<div class="action"><div class="aicon">24h</div><div><div class="atag">Aplicación práctica</div>'
                      '<div class="atext">Antes de pasar al próximo capítulo, elegí <b>una decisión concreta</b> que puedas implementar durante las próximas 24 horas.</div>'
                      '<div class="aline"></div></div></div>')
def lines(n=2): return '<div class="wlines">' + '<div class="wl"></div>' * n + '</div>'
def wq(q, n=2): return f'<div class="wq"><div class="wqt">{q}</div>{lines(n)}</div>'

OACT = ('<div class="oact"><div class="oai">24h</div><div><div class="oat">Aplicación práctica</div>'
        '<div class="oax">Mientras leés este capítulo, buscá <b>una decisión concreta</b> que puedas implementar durante las próximas 24 horas.</div></div></div>')
VARC = ['V', 'A', 'R', 'C']
VARC_NAMES = ['Visibilidad', 'Autoridad', 'Relación', 'Conversión']

def tracker(active):
    cells = ''
    for i, (l, nme) in enumerate(zip(VARC, VARC_NAMES)):
        on = ' on' if l in active else ''
        cells += f'<div class="tcell{on}"><div class="tl">{l}</div><div class="tn">{nme}</div></div>'
    return f'<div class="tracker">{cells}</div>'

def opener(label, num, title, sub, active, key, act=True):
    numhtml = f'<div class="onum">{num}</div>' if num else ''
    add(f'''<section class="opener" id="{key}">
  <div class="oglow"></div>
  <div class="otop"><span class="olabel">{label}</span><span class="obrand">De Invisible a Referente</span></div>
  {numhtml}
  <h1 class="otitle">{title}</h1>
  <div class="obar"></div>
  <p class="osub">{sub}</p>
  {OACT if act else ''}
  <div class="obottom"><div class="ometh">Método V.A.R.C.</div>{tracker(active)}</div>
</section>''')

def body(*blocks):
    add('<section class="body">' + ''.join(blocks) + '</section>')

TOC = []
def chapter(key, label, num, title, sub, active, *blocks, toc_title=None, with_action=True):
    TOC.append((key, num or '', toc_title or title.replace('<br>', ' '), label))
    opener(label, num, title, sub, active, key, with_action)
    body(*blocks)

# ---------- PORTADA ----------
add('<section class="cover"><img src="cover.jpg" alt="Portada"></section>')

# ---------- PÁGINA DE TÍTULO ----------
add('''<section class="titlepage">
  <div class="oglow big"></div>
  <div class="tp-kicker">Guía práctica · Edición 2026</div>
  <div class="tp-title">DE <span>INVISIBLE</span><br>A REFERENTE</div>
  <div class="tp-swoosh"></div>
  <p class="tp-sub">El método práctico para construir una <b>marca personal</b>, crear contenido que atraiga atención y convertir confianza en <b>oportunidades comerciales</b>.</p>
  <div class="tp-pill">Método V.A.R.C. en 4 pasos</div>
  <div class="tp-includes">Incluye: Workbook profesional · Plan de 30 días · 15 hooks · Checklists</div>
</section>''')

# ---------- LEGAL ----------
add('''<section class="body legal">
  <div class="legal-inner">
  <div class="lg-title">DE INVISIBLE A REFERENTE</div>
  <div class="lg-sub">Edición Premium · 2026</div>
  <p>© 2026. Todos los derechos reservados.</p>
  <p>Ninguna parte de esta publicación puede ser reproducida, distribuida, revendida ni transmitida por ningún medio sin autorización previa y por escrito del titular de los derechos. La compra de este eBook otorga una licencia de uso personal e intransferible.</p>
  <p><b>Aviso sobre resultados.</b> Los casos y cifras que aparecen en este libro son ejemplos ilustrativos que uso para explicar una lógica estratégica. No constituyen promesa ni garantía de resultados. Los resultados de cada persona dependen de su mercado, su oferta, su dedicación y otros factores.</p>
  <p><b>Aviso general.</b> El contenido tiene fines educativos. No sustituye asesoramiento legal, fiscal, sanitario ni financiero profesional. Cualquier afirmación técnica o de salud que quieras publicar en tus redes debe ser verificada antes por un profesional.</p>
  </div>
</section>''')

# ---------- CÓMO USAR ESTE LIBRO ----------
add('''<section class="body howto">
  <div class="kicker">Antes de empezar</div>
  <h2 class="ptitle">Cómo usar este libro</h2>
  <p class="lead">Escribí este libro para que cada idea venga acompañada de casos, ejemplos, ejercicios y aplicaciones. No es un libro para leer de corrido y olvidar: es un sistema para implementar.</p>
  <div class="howgrid">
    <div class="hg"><div class="hgi">01</div><div><b>Leé un capítulo.</b> Cada uno desarrolla una pieza del sistema con ideas, casos y ejemplos.</div></div>
    <div class="hg"><div class="hgi">02</div><div><b>Hacé el ejercicio.</b> Los recuadros naranjas convierten la teoría en decisiones.</div></div>
    <div class="hg"><div class="hgi">03</div><div><b>Aplicá en 24 horas.</b> Cada capítulo abre con un desafío: una decisión concreta para implementar ya.</div></div>
    <div class="hg"><div class="hgi">04</div><div><b>Completá el workbook.</b> Al final tenés las plantillas para diseñar tu marca.</div></div>
  </div>
  <div class="kicker" style="margin-top:6mm">El mapa del recorrido</div>
  <h2 class="ptitle sm">Método V.A.R.C.</h2>
  <div class="varc">
    <div class="vc"><div class="vl">V</div><div class="vn">Visibilidad</div><div class="vd">Hacer que las personas correctas te descubran.</div></div>
    <div class="vc"><div class="vl">A</div><div class="vn">Autoridad</div><div class="vd">Demostrar que sabés resolver problemas.</div></div>
    <div class="vc"><div class="vl">R</div><div class="vn">Relación</div><div class="vd">Construir confianza y conversación.</div></div>
    <div class="vc"><div class="vl">C</div><div class="vn">Conversión</div><div class="vd">Crear un siguiente paso comercial natural.</div></div>
  </div>
  <p class="small muted">Los casos con cifras son ejemplos ilustrativos; no constituyen garantía de resultados.</p>
</section>''')

# ---------- ÍNDICE (placeholder, se rellena al final) ----------
add('%%TOC%%')

# ---------- INTRODUCCIÓN ----------
chapter('intro', 'Introducción', None, 'No te falta valor:<br>te falta visibilidad',
        'Podés tener una profesión excelente. Pero si el mercado no sabe que existís, todo lo demás se bloquea.', 'VARC',
        lead('Podés tener una profesión excelente, un producto competitivo o una experiencia que realmente ayude a otras personas. Pero existe un problema que puede bloquear todo lo demás: <b>que el mercado no sepa que existís.</b>'),
        p('Mi tesis es directa: las redes sociales se han convertido en un lugar donde las personas descubren profesionales, negocios, productos, ideas y referentes. Por eso, construir una marca personal ya no debería entenderse como una actividad reservada a influencers. Puede ser una <b>infraestructura de marketing</b> para un negocio.'),
        p('Ahora bien, en este libro no te propongo perseguir fama. Te propongo construir una asociación mental: que una persona concreta te recuerde cuando aparece un problema, un deseo o una oportunidad relacionada con lo que sabés hacer.'),
        p('Pensá el proceso como una escalera. Primero necesitás visibilidad. Después necesitás demostrar autoridad. Luego necesitás construir relación y confianza. Finalmente, necesitás una forma natural de convertir esa confianza en una conversación comercial. Ese recorrido es el Método V.A.R.C.:'),
        formula(['Visibilidad', 'Autoridad', 'Relación', 'Conversión'], 'Método V.A.R.C.'),
        p('A lo largo del libro vas a ver esta lógica una y otra vez: diseñar la marca, conocer al cliente, crear contenido útil y reflexivo, y después abrir conversaciones mediante un recurso de valor. Mi objetivo es convertir esas ideas en un sistema concreto, con ejemplos, ejercicios, decisiones y casos.'),
        note('los casos y cifras que aparecen en los recuadros de este libro son ejemplos ilustrativos. Los incluyo para mostrar la lógica estratégica, no como promesas de resultados.'),
        quote('Mi meta no es que copies una fórmula. Es que puedas entender por qué cada pieza existe y adaptar el sistema a tu negocio.'),
)

# ---------- CAPÍTULO 1 ----------
chapter('c1', 'Capítulo', '01', 'El nuevo activo:<br>ser reconocible',
        'La visibilidad es el puente entre lo que ofrecés y las personas que podrían necesitarlo.', 'V',
        lead('Abrir un negocio no garantiza que el mercado lo encuentre. Tener una cuenta en Instagram tampoco. La visibilidad es el puente entre lo que ofrecés y las personas que podrían necesitarlo.'),
        p('Me gusta usar una imagen: un negocio desconocido puede parecerse a una <b>tienda instalada en medio del desierto</b>. Puede tener excelentes productos, pero si nadie pasa por delante, el problema no es la calidad del producto: es la ausencia de tráfico y reconocimiento.'),
        p('La marca personal interviene precisamente ahí. Hace visible a la persona que está detrás de la propuesta. Esto es especialmente relevante cuando la compra implica confianza: servicios profesionales, asesorías, formación, coaching, salud, creatividad, consultoría, negocios locales o productos donde la recomendación y la experiencia personal pesan.'),
        keybox('Una marca personal fuerte permite que el mercado responda tres preguntas con menos fricción',
               ol(['¿Quién es esta persona?', '¿Qué problema sabe resolver?', '¿Por qué debería prestarle atención a ella?'])),
        quote('No necesitás ser conocido por todos. Necesitás ser reconocible por un grupo suficientemente relevante.'),
        case('Floristería local',
             p('Pensá en una floristería de barrio. El punto interesante no es la cifra de seguidores, sino la lógica: incluso un negocio extremadamente local puede usar las redes sociales para captar clientes y, además, abrir una segunda línea de negocio, por ejemplo, formación para otras floristas.'),
             p('Supongamos que con una audiencia de unos <b>1.900 seguidores</b> vende dos formaciones presenciales de <b>1.500 € cada una</b>, además de conseguir clientes para la propia floristería. No hace falta una audiencia enorme para que los números cierren.'),
             '<div class="learn"><b>¿Qué aprendemos?</b> La audiencia no tiene que ser masiva. Tiene que contener personas relevantes. Y una marca puede descubrir nuevas oportunidades de monetización que no eran evidentes al principio.</div>'),
        exercise('Test de reconocimiento',
                 p('Completá la frase:'),
                 '<div class="fill">“Quiero que cuando alguien piense en <span class="blank"></span>, mi nombre aparezca como una opción porque <span class="blank"></span>.”</div>',
                 p('Después preguntale a tres personas que conozcan tu actividad: <i>“¿Qué creés que hago y para quién?”</i>. No les expliques la respuesta antes. Compará lo que querés comunicar con lo que realmente perciben.'),
                 p('<b>Si existe una diferencia grande, tenés un problema de posicionamiento, no necesariamente de contenido.</b>')),
)

# ---------- CAPÍTULO 2 ----------
chapter('c2', 'Capítulo', '02', 'Marca personal no es<br>ser influencer',
        'Una marca personal es un sistema de percepción y confianza. Puede existir con 500 seguidores o con 500.000.', 'V',
        lead('Una confusión frecuente consiste en pensar que marca personal equivale a fama. No.'),
        p('Una marca personal es un <b>sistema de percepción y confianza</b> alrededor de una persona. Puede existir con 500 seguidores, 5.000 o 500.000. La cantidad de atención cambia; el principio permanece.'),
        p('Hay una distinción que siempre repito: <b>crecer en redes y vender son habilidades diferentes.</b> Una cuenta puede acumular visualizaciones y no producir negocio. También puede ocurrir lo contrario: una comunidad relativamente pequeña puede generar oportunidades comerciales si existe una buena oferta y una conversación bien planteada.'),
        h3('Por eso conviene separar seis activos'),
        deflist([('Identidad', 'Cómo te presentás.'), ('Posicionamiento', 'Por qué tema querés ser recordado.'),
                 ('Prueba', 'Qué demuestra que sabés.'), ('Contenido', 'Cómo entregás valor.'),
                 ('Relación', 'Cómo generás confianza.'), ('Oferta', 'Qué puede comprar alguien que necesita avanzar.')], 'grid2'),
        p('La autenticidad no significa publicar absolutamente todo. Lo pienso así: una marca puede estar diseñada de manera intencional y seguir siendo auténtica. Elegir qué mostrar no convierte automáticamente la comunicación en falsa. Significa seleccionar lo que es coherente con el posicionamiento.'),
        case('El profesional técnico',
             p('Imaginá un contador que quiere captar pequeñas empresas. Puede publicar exclusivamente consejos tributarios complejos. Eso demuestra conocimiento, pero quizá no genere identificación. Puede sumar contenido sobre errores que cometen los dueños al manejar caja, decisiones que debería tomar un emprendedor antes de contratar personal y situaciones reales de gestión.'),
             '<div class="learn">No dejó de ser contador. Simplemente <b>tradujo su conocimiento al mundo mental del cliente.</b></div>'),
        exercise('Mapa de identidad',
                 p('Escribí:'),
                 ul(['Tres temas por los que querés ser conocido.', 'Tres valores que querés transmitir.',
                     'Tres cosas que nunca querés que se asocien a tu marca.', 'Tres pruebas de experiencia que podés mostrar.',
                     'Una oferta que tenga sentido dentro de ese territorio.']),
                 p('<b>La marca se vuelve más fuerte cuando estas cinco respuestas apuntan en la misma dirección.</b>')),
)

# ---------- CAPÍTULO 3 ----------
chapter('c3', 'Capítulo', '03', 'Tu territorio de<br>posicionamiento',
        '¿Por qué tema debería recordarte una persona? La especificidad hace que el cliente se reconozca.', 'V',
        lead('El posicionamiento responde una pregunta sencilla: <b>¿por qué tema debería recordarte una persona?</b>'),
        p('El error más habitual es hablar de todo. El segundo error es elegir un nicho tan estrecho que no existe suficiente mercado. La solución es encontrar un <b>territorio</b>: un espacio donde confluyen tu experiencia, tus intereses, los problemas del mercado y una posibilidad comercial.'),
        formula(['Lo que sé', 'Lo que me interesa', 'Lo que el cliente necesita', 'Lo que puedo monetizar'], 'La fórmula del territorio').replace('<span class="arr">→</span>', '<span class="arr">+</span>'),
        h3('De lo amplio a lo específico'),
        '<div class="ladder"><div class="lad l1"><span>Amplio</span>“Marketing”</div><div class="lad l2"><span>Más claro</span>“Marketing para restaurantes”</div><div class="lad l3"><span>Específico</span>“Contenido para restaurantes que quieren aumentar reservas sin depender únicamente de descuentos”</div></div>',
        quote('La especificidad ayuda porque hace que el cliente se reconozca.'),
        case('Escuela de drift',
             p('Imaginá a un piloto que dirige una escuela de drift. El ejemplo es interesante porque el posicionamiento no depende únicamente de decir “tengo una escuela”. El universo visual del drift, los colores de marca, el traje y la forma de presentar la experiencia forman parte del territorio.'),
             '<div class="learn"><b>La lección es aplicable:</b> tu posicionamiento no vive solamente en el texto de tu bio. También aparece en tu estética, tus escenarios, tus ejemplos, tu vocabulario y el tipo de historias que contás.</div>'),
        exercise('Matriz de territorio',
                 '<div class="matrix"><div><b>A</b>10 cosas que sabés hacer.</div><div><b>B</b>10 cosas sobre las que podrías hablar durante un año.</div><div><b>C</b>10 problemas o deseos que tiene tu cliente.</div><div><b>D</b>5 cosas por las que alguien estaría dispuesto a pagarte.</div></div>',
                 p('<b>Buscá intersecciones.</b> Ahí aparecen territorios potenciales.')),
)

# ---------- CAPÍTULO 4 ----------
chapter('c4', 'Capítulo', '04', 'Diseñá cómo querés<br>ser percibido',
        'Una publicación no define una marca; cientos de señales consistentes sí.', 'V',
        lead('La percepción se construye por acumulación. Una publicación no define una marca; cientos de señales consistentes sí.'),
        p('Una marca personal sólida está diseñada deliberadamente: imagen, colores, mensajes, temas y aquello que se decide mostrar o no mostrar. La idea estratégica es poderosa: <b>la autenticidad y la intención no son opuestos.</b>'),
        p('Tu marca debería producir una sensación reconocible. Podés querer transmitir, por ejemplo:'),
        '<div class="chips"><span>Autoridad y precisión</span><span>Cercanía y practicidad</span><span>Innovación y velocidad</span><span>Elegancia y exclusividad</span><span>Energía y entretenimiento</span><span>Calma y profundidad</span></div>',
        p('No hace falta que elijas una sola palabra. Pero sí necesitás una dirección.'),
        case('Consultor B2B',
             p('Supongamos que sos consultor de ventas para empresas. Si tu posicionamiento es “ventas B2B con procesos”, una comunicación basada únicamente en memes puede atraer atención, pero quizás no genere la percepción que necesitás. Podés usar humor, pero debería convivir con casos, frameworks, análisis y demostraciones.')),
        quote('La pregunta no es “¿esto puede hacerse viral?”. La pregunta es “¿esto contribuye a la percepción que necesito construir?”.'),
        exercise('Antes de publicar, preguntate',
                 checks(['¿Esto parece venir de la misma persona?', '¿Refuerza mi territorio?', '¿Habla el lenguaje de mi cliente?',
                         '¿Demuestra algo?', '¿Genera una emoción compatible con mi marca?', '¿Me acerca o me aleja de la oferta que quiero vender?']),
                 p('<b>La coherencia reduce fricción.</b>'), tag='Checklist de percepción'),
)

# ---------- CAPÍTULO 5 ----------
chapter('c5', 'Capítulo', '05', 'Conocé al cliente antes<br>de crear contenido',
        'Las personas prestan atención a aquello que perciben como útil, divertido o inspirador.', 'A',
        lead('Hay una idea que conviene convertir en regla: las personas prestan atención a aquello que perciben como <b>útil, divertido o inspirador.</b>'),
        p('Pero “útil” no significa únicamente enseñar un tutorial. Puede significar ayudar a tomar una decisión, evitar un error, imaginar un futuro o sentirse comprendido.'),
        h3('Para crear contenido relevante, investigá seis dimensiones'),
        deflist([('Problemas', '¿Qué está intentando resolver?'), ('Frustraciones', '¿Qué probó y no funcionó?'),
                 ('Deseos', '¿Qué quiere conseguir?'), ('Miedos', '¿Qué teme perder?'),
                 ('Aspiraciones', '¿Cómo quiere sentirse o verse?'), ('Situaciones', '¿Cuándo aparece el problema?')], 'grid2'),
        case('Terapeuta que trabaja con estrés',
             p('Te propongo explorar los problemas derivados del estrés: dificultades para dormir, molestias digestivas, dolores de cabeza, irritabilidad o conflictos de pareja. Y también investigar los deseos: disponer de más tiempo, descansar, disfrutar vacaciones y sentirse mejor.'),
             p('Fijate en lo que acaba de pasar. “Estrés” dejó de ser un tema abstracto. Se convirtió en decenas de situaciones concretas. De ahí pueden salir contenidos:'),
             ul(['“Tres señales de que tu estrés está afectando tu descanso.”', '“Por qué llegar de vacaciones agotado no resuelve el problema.”',
                 '“Qué hábitos de tu jornada pueden estar alimentando la sensación de estar siempre acelerado.”']),
             '<div class="learn">El contenido empieza a sentirse personal porque <b>utiliza el mundo del cliente.</b></div>'),
        exercise('Banco de 30 problemas',
                 p('Escribí <b>10 problemas funcionales, 10 problemas emocionales y 10 deseos.</b> No busques frases elegantes. Usá las palabras que usaría tu cliente al hablar con un amigo.'),
                 p('Ese documento será una fuente de contenido durante semanas.')),
)

# ---------- CAPÍTULO 6 ----------
chapter('c6', 'Capítulo', '06', 'Convertí problemas y deseos<br>en ideas infinitas',
        'Cuando alguien dice “no sé qué publicar”, normalmente no necesita creatividad: necesita preguntas mejores.', 'A',
        lead('Cuando alguien dice “no sé qué publicar”, normalmente no necesita creatividad: <b>necesita preguntas mejores.</b>'),
        p('Por cada problema podés crear al menos diez ángulos. Ejemplo con el problema <b>“mi negocio no consigue clientes”</b>:'),
        '<table class="angles">' + ''.join(f'<tr><td class="an">{i+1:02d}</td><td class="ak">{k}</td><td>{v}</td></tr>' for i, (k, v) in enumerate([
            ('Explicación', '“Las tres razones por las que un negocio puede tener visitas pero no consultas.”'),
            ('Error', '“El error de publicar precios sin contexto.”'),
            ('Paso a paso', '“Cómo convertir una consulta en una conversación.”'),
            ('Historia', '“Lo que aprendí después de perder un cliente por no hacer esta pregunta.”'),
            ('Comparación', '“Perfil que informa vs. perfil que convierte.”'),
            ('Opinión', '“No creo que publicar todos los días sea el problema.”'),
            ('Caso', '“Qué cambiaría en este perfil.”'),
            ('Advertencia', '“Antes de invertir en publicidad revisá estas cuatro variables.”'),
            ('Checklist', '“¿Tu perfil responde estas cinco preguntas?”'),
            ('Experimento', '“Probé dos llamadas a la acción durante una semana.”')])) + '</table>',
        quote('El objetivo no es fabricar contenido por fabricar. Cada pieza debería reforzar tu posición.'),
        exercise('Matriz 10×10',
                 p('Elegí <b>10 problemas</b> y aplicales los <b>10 ángulos</b>. Tenés un banco potencial de <b>100 piezas</b> sin inventar temas arbitrarios.')),
)

# ---------- CAPÍTULO 7 ----------
chapter('c7', 'Capítulo', '07', 'El contenido que detiene<br>el desplazamiento',
        'Saber qué decir no es suficiente. También importa cómo se presenta.', 'A',
        lead('Saber qué decir no es suficiente. También importa <b>cómo se presenta.</b>'),
        p('Pensá en el contraste entre un video genérico sobre el insomnio y una versión estructurada alrededor de una apertura fuerte, una explicación y un consejo accionable. La estructura que podemos extraer es:'),
        formula(['Hook', 'Contexto', 'Tensión', 'Valor', 'Cierre'], 'Estructura de una pieza'),
        deflist([('Hook', 'Una frase que haga relevante la siguiente frase.'), ('Contexto', 'Por qué el tema importa.'),
                 ('Tensión', 'Qué problema, error o contradicción debe resolver el espectador.'),
                 ('Valor', 'La idea, método o acción.'), ('Cierre', 'Una conclusión o siguiente paso.')]),
        quote('Un hook no necesita gritar. Necesita prometer relevancia.'),
        h3('Ejemplos de hooks'),
        '<div class="hooks">' + ''.join(f'<div class="hk">{h}</div>' for h in [
            '“Si tu perfil recibe visitas pero nadie te escribe, mirá esto.”',
            '“La mayoría intenta solucionar este problema demasiado tarde.”',
            '“Antes de gastar dinero en publicidad, revisá estas tres cosas.”',
            '“Si empezara mi marca personal desde cero, no empezaría por el logo.”']) + '</div>',
        case('El video de estrés',
             p('Compará una introducción débil con una apertura más específica sobre dificultades de sueño y un consejo práctico. El punto metodológico es que el segundo formato genera <b>una razón inmediata para seguir escuchando.</b>')),
        note('cualquier afirmación médica incluida en un ejemplo debe verificarse antes de publicarse. Nunca conviertas una afirmación de salud en un hecho científico sin revisión profesional.'),
        exercise('5 versiones del mismo tema',
                 p('Elegí un tema y escribí cinco hooks:'),
                 ul(['Uno basado en <b>error</b>.', 'Uno basado en <b>curiosidad</b>.', 'Uno basado en <b>resultado</b>.', 'Uno basado en <b>contraste</b>.', 'Uno basado en <b>opinión</b>.']),
                 p('Después elegí el que mejor conecte con tu cliente, no necesariamente el que suene más espectacular.')),
)

# ---------- CAPÍTULO 8 ----------
chapter('c8', 'Capítulo', '08', 'Autoridad + conexión:<br>los dos motores',
        'El contenido práctico demuestra competencia. El reflexivo demuestra perspectiva.', 'A',
        lead('Siempre distingo dos tipos de contenido que conviene mantener juntos.'),
        '<div class="engines"><div class="eng dark"><div class="engk">Contenido práctico</div><div class="engv">Demuestra <b>competencia</b></div><div class="engq">“¿Esta persona sabe?”</div></div>'
        '<div class="eng plus">+</div>'
        '<div class="eng or"><div class="engk">Contenido reflexivo</div><div class="engv">Demuestra <b>perspectiva</b></div><div class="engq">“¿Esta persona piensa como yo?”</div></div></div>',
        p('Si solamente enseñás, podés ser útil pero fácilmente reemplazable. Si solamente opinás, podés generar conversación pero sin suficiente autoridad.'),
        case('Estrés y opinión',
             p('Volvamos al ejemplo de una persona que trabaja con estrés. El contenido práctico podría explicar cómo identificar situaciones que aumentan la tensión. El contenido reflexivo podría cuestionar la frase <i>“no te estreses, tomá una tila”</i> y explicar por qué minimizar el problema no ayuda.'),
             '<div class="learn">El segundo contenido no agrega necesariamente una técnica nueva. <b>Agrega identidad.</b></div>'),
        quote('Cuando alguien comenta “yo pienso igual”, acaba de aparecer una señal de conexión.'),
        exercise('10 + 10',
                 ul(['Creá <b>10 ideas prácticas</b> que enseñen algo.', 'Creá <b>10 ideas reflexivas</b> que expresen una postura relacionada con tu sector.']),
                 p('Después buscá parejas. Cada tema importante de tu negocio debería poder generar al menos una pieza de autoridad y una de conexión.')),
)

# ---------- CAPÍTULO 9 ----------
chapter('c9', 'Capítulo', '09', 'Convertir atención<br>en relación',
        'Un seguidor es atención. Una relación requiere interacción.', 'R',
        lead('Un seguidor es atención. <b>Una relación requiere interacción.</b>'),
        p('El sistema que propongo utiliza un recurso gratuito como puente:'),
        formula(['Contenido de valor', 'Invitación a pedir un regalo', 'Conversación privada', 'Diagnóstico', 'Eventual oferta'], 'El puente'),
        p('La lógica es importante porque evita dos extremos:'),
        '<div class="extremes"><div><span>Extremo A</span>“Comprame” en cada publicación.</div><div><span>Extremo B</span>Publicar durante meses sin ofrecer ningún siguiente paso.</div></div>',
        h3('Un recurso útil puede ser'),
        '<div class="chips"><span>Checklist</span><span>Plantilla</span><span>Guía</span><span>Clase</span><span>Diagnóstico</span><span>Calculadora</span><span>Biblioteca</span><span>Mini entrenamiento</span></div>',
        case('Educador y clase gratuita',
             p('Imaginá a dos educadores que ofrecen una clase gratuita. La persona la solicita, ellos reciben el contacto por mensaje privado y continúan la conversación.'),
             '<div class="learn">La lección no es “regalá una clase”. La lección es <b>construir un puente entre una necesidad y una conversación.</b></div>'),
        keybox('Regla de conversación: escuchá más de lo que hablás',
               p('Preguntas útiles:'),
               '<div class="qs"><div>“¿Qué estás intentando conseguir?”</div><div>“¿Qué te está frenando?”</div><div>“¿Qué probaste?”</div><div>“¿Qué sería un buen resultado para vos?”</div></div>',
               p('No conviertas el chat en un interrogatorio. La conversación debe ser humana y útil.')),
        quote('Una marca fuerte no obliga a comprar. Facilita que la persona correcta encuentre el siguiente paso correcto.'),
)

# ---------- CAPÍTULO 10 ----------
chapter('c10', 'Capítulo', '10', 'De la conversación<br>a la venta',
        'La venta aparece cuando existe encaje entre problema, solución y capacidad de ejecución.', 'C',
        lead('La venta aparece cuando existe <b>encaje entre problema, solución y capacidad de ejecución.</b>'),
        p('Una conversación comercial puede organizarse así:'),
        formula(['Contexto', 'Problema', 'Impacto', 'Objetivo', 'Opciones', 'Siguiente paso'], 'Conversación comercial'),
        p('Primero entendés la situación. Después profundizás en el problema. Luego explorás qué impacto tiene y qué resultado quiere conseguir la persona. Recién entonces tiene sentido explicar cómo podrías ayudar.'),
        case('Asesorías individuales',
             p('Hagamos números con una consultora que empieza desde cero con el método de conversaciones y ofrece asesorías individuales de 1,5 horas a 500 €. Con <b>20 clientes</b> en dos semanas, factura <b>10.000 €</b>.'),
             p('No es una promesa: es un ejemplo para entender la lógica: una audiencia pequeña puede contener compradores suficientes cuando la oferta tiene valor y la conversación identifica necesidades reales.'),
             p('Otro ejemplo: una estilista que forma a otras en peinados de novia. Con cinco alumnas a 2.500 €, son <b>12.500 €</b> con una sola formación.')),
        p('El patrón común no es el número de seguidores. Es la combinación de:'),
        formula(['Audiencia relevante', 'Oferta específica', 'Conversación'], 'La combinación que vende').replace('<span class="arr">→</span>', '<span class="arr">+</span>'),
        exercise('Diagnóstico comercial',
                 p('Escribí:'),
                 ul(['¿Qué problema resuelvo?', '¿Qué resultado vendo?', '¿Qué prueba tengo?', '¿Qué persona está más preparada para comprar?',
                     '¿Qué objeción aparece antes de comprar?', '¿Cuál sería un siguiente paso pequeño y razonable?']),
                 p('<b>La conversación no reemplaza una buena oferta. La hace visible.</b>')),
)

# ---------- CAPÍTULO 11 ----------
def stage(n, name, desc, prob, case_txt, app):
    c = f'<div class="stcase"><b>Caso:</b> {case_txt}</div>' if case_txt else ''
    pr = f'<div class="stprob"><span>Prioridad</span>{prob}</div>' if prob else ''
    return (f'<div class="stage"><div class="stn"><small>Etapa</small>{n}</div><div class="stb"><div class="stname">{name}</div>'
            f'<p>{desc}</p>{pr}{c}<div class="stapp"><b>Aplicación:</b> {app}</div></div></div>')

chapter('c11', 'Capítulo', '11', 'Las cinco etapas<br>del emprendedor',
        'La estrategia correcta depende de la etapa. No a todos les sirve lo mismo.', 'VARC',
        lead('Esta clasificación es especialmente útil porque <b>evita aplicar la misma estrategia a todo el mundo.</b>'),
        stage(1, 'Todavía no empezaste', 'Puede que tengas trabajo, ambición y ganas, pero no sepas exactamente qué vender.',
              'Explorar y construir visibilidad sin poner toda la presión financiera sobre la marca.',
              'muchas personas empiezan a trabajar su marca personal mientras tienen otro trabajo y antes de saber exactamente qué vender.',
              'hablá de lo que sabés, de lo que te apasiona y observá qué preguntas aparecen.'),
        stage(2, 'Profesional invisible', 'Tenés oferta, pero casi nadie te conoce.', 'Visibilidad.',
              'pensá en un coach que empieza desde cero y tarda más que la media en crecer. No necesitás esperar resultados instantáneos.',
              'aumentar exposición, contenido y presencia en espacios donde están tus clientes.'),
        stage(3, 'Creador atascado', 'Publicás, pero no conseguís suficiente atención.', 'Capacidad de captar interés y estructurar contenido.',
              'un profesional con 12.000 seguidores puede multiplicar su alcance cuando mejora hooks y guiones. El crecimiento depende de la ejecución, no hay garantías.',
              'mejorar ideas, hooks, guiones, presentación y aprendizaje a partir de métricas.'),
        stage(4, 'Audiencia sin monetización', 'Tenés atención, pero no negocio. Recordá: crecer y vender son habilidades diferentes.', 'Conversión.', None,
              'oferta, recurso, conversación y seguimiento.'),
        stage(5, 'Referente', 'La demanda empieza a llegar con menos esfuerzo directo. El problema cambia: capacidad operativa, saturación y dependencia del tiempo.', None, None,
              'delegar, subir precios cuando exista valor y capacidad, sistematizar y evolucionar el modelo de negocio.'),
        keybox('Diagnóstico',
               p('No preguntes “¿qué debería hacer en redes?”. Preguntá primero: <b>“¿cuál es mi cuello de botella actual?”</b>'),
               p('La estrategia correcta depende de la etapa.')),
)

# ---------- CAPÍTULO 12 ----------
chapter('c12', 'Capítulo', '12', 'Producción de contenido<br>sin vivir para publicar',
        'No es sostenible depender de grabar un video completamente distinto cada día. La alternativa: trabajar por lotes.', 'VARC',
        lead('Hay una idea operacional muy importante: no es sostenible depender de grabar un video completamente distinto cada día. <b>La alternativa es trabajar por lotes.</b>'),
        h3('El sistema'),
        '<div class="steps9">' + ''.join(f'<div><span>{i+1}</span>{s}</div>' for i, s in enumerate(
            ['Investigación', 'Banco de ideas', 'Selección', 'Guiones', 'Grabación', 'Edición', 'Publicación', 'Análisis', 'Repetición mejorada'])) + '</div>',
        p('Con experiencia y práctica, hay creadores que graban entre 40 y 50 videos en un día. Si estás empezando, te recomiendo cantidades mucho menores y un proceso progresivo.'),
        quote('No copies el volumen. Copiá el principio: agrupá tareas.'),
        '<div class="keep">' + h3('Sistema semanal mínimo') +
        '<div class="week">' + ''.join(f'<div><b>{d}</b>{t}</div>' for d, t in [('Lun', 'Investigar'), ('Mar', 'Guionar'), ('Mié', 'Grabar'), ('Jue', 'Editar / programar'), ('Vie', 'Conversar y analizar')]) + '</div>',
        case('Profesional con empleo',
             p('Imaginá una nutricionista que trabaja de lunes a viernes. En vez de intentar grabar todos los días, puede dedicar dos horas el sábado a preparar 10 guiones y dos horas el domingo a grabar cinco piezas. Luego puede editar o delegar.'),
             '<div class="learn">La marca deja de competir con toda la agenda.</div>'),
        p('<i>No es una ley. Es una estructura para reducir fricción.</i>') + '</div>',
)

# ---------- CAPÍTULO 13 ----------
chapter('c13', 'Capítulo', '13', 'Métricas: no confundas<br>atención con negocio',
        'Una publicación puede tener alcance enorme y cero ventas. Otra puede tener menos alcance y generar un cliente excelente.', 'VARC',
        lead('Una marca personal necesita métricas, pero <b>no todas responden la misma pregunta.</b>'),
        '<div class="funnel">' + ''.join(f'<div class="fr" style="width:{w}%"><b>{k}</b><span>{v}</span></div>' for k, v, w in [
            ('Alcance', '¿Cuántas personas tuvieron oportunidad de descubrirme?', 100), ('Retención', '¿El contenido consiguió mantener atención?', 94),
            ('Interacción', '¿Generó participación?', 88), ('Visitas al perfil', '¿Despertó curiosidad?', 82),
            ('Conversaciones', '¿Movió a la persona a una acción directa?', 76), ('Leads', '¿Generó oportunidades?', 70), ('Ventas', '¿Produjo ingresos?', 64)]) + '</div>',
        case('Dos videos, dos resultados',
             p('Un abogado publica un video que consigue <b>200.000 reproducciones</b> y 40 consultas irrelevantes. Otro video alcanza <b>12.000 reproducciones</b> y genera cinco consultas de empresas que encajan con su servicio.'),
             p('Si mirás únicamente reproducciones, declararías ganador al primero. Si mirás negocio, la respuesta puede ser diferente.'),
             '<div class="learn">La métrica debe corresponder al objetivo.</div>'),
        h3('Objetivo → métrica principal'),
        '<table class="mtable"><tr><th>Objetivo</th><th>Métrica principal</th></tr>'
        '<tr><td>Descubrimiento</td><td>Alcance y retención</td></tr><tr><td>Autoridad</td><td>Guardados, comentarios cualificados, visitas al perfil</td></tr>'
        '<tr><td>Relación</td><td>Respuestas y conversaciones</td></tr><tr><td>Conversión</td><td>Leads, reuniones y ventas</td></tr></table>',
        quote('No optimices una métrica aislada. Optimizá el sistema.'),
)

# ---------- CAPÍTULO 14 ----------
errs = [('Esperar perfección', 'Publicar versiones suficientemente buenas y mejorar.'),
        ('Copiar al referente', 'Estudiar estructuras, pero construir una voz propia.'),
        ('Hablar de todo', 'Territorio y pilares.'),
        ('Obsesionarse con seguidores', 'Medir relevancia y oportunidades.'),
        ('Vender en cada publicación', 'Alternar autoridad, conexión y conversión.'),
        ('No vender nunca', 'Ofrecer un siguiente paso cuando exista encaje.'),
        ('Esperar resultados inmediatos', 'Tratar el contenido como un sistema de aprendizaje.'),
        ('Abandonar después de pocas semanas', 'Analizar suficientes piezas para encontrar patrones.'),
        ('Crear contenido desconectado del negocio', 'Cada pilar debe tener relación con el problema, deseo o identidad del cliente.'),
        ('Depender de una sola plataforma', 'Construir una audiencia y activos que puedan trasladarse a distintos canales.')]
chapter('c14', 'Capítulo', '14', 'Los errores<br>que más frenan',
        'Diez trampas frecuentes y cómo salir de cada una.', 'VARC',
        '<div class="errors">' + ''.join(f'<div class="err"><div class="errn">{i+1:02d}</div><div><div class="errt">{e}</div><div class="errs"><span>Solución</span>{s}</div></div></div>' for i, (e, s) in enumerate(errs)) + '</div>',
        case('El creador que solo publica tendencias',
             p('Un profesional de arquitectura empieza a copiar audios virales. Las visualizaciones suben, pero sus seguidores no entienden qué hace ni por qué contratarlo.'),
             '<div class="learn">No necesita menos contenido. Necesita más coherencia.</div>'),
        quote('Una tendencia puede ser el formato. El tema debe seguir siendo tuyo.'),
)

# ---------- CAPÍTULO 15 ----------
plan = [('1–3', 'Posicionamiento', 'Definí territorio, cliente y promesa.'),
        ('4–7', 'Investigación', 'Creá un banco de 30 problemas, 30 deseos y 20 objeciones.'),
        ('8–10', 'Perfil', 'Revisá foto, nombre, bio, propuesta de valor y contenido fijado.'),
        ('11–15', 'Contenido', 'Creá 10 hooks, 5 guiones prácticos y 5 reflexivos.'),
        ('16–18', 'Producción', 'Grabá por lotes.'),
        ('19–23', 'Distribución', 'Publicá, respondé comentarios y registrá preguntas recurrentes.'),
        ('24–26', 'Recurso', 'Creá una pieza gratuita relacionada directamente con tu oferta.'),
        ('27–29', 'Conversaciones', 'Invitá a personas interesadas a solicitar el recurso. Conversá, preguntá y escuchá.')]
chapter('c15', 'Capítulo', '15', 'Plan de acción<br>de 30 días',
        'El objetivo no es “hacerse viral”. Es salir con un sistema de aprendizaje y una primera evidencia de qué funciona.', 'VARC',
        '<div class="timeline">' + ''.join(f'<div class="tli"><div class="tld"><small>Días</small>{d}</div><div class="tlb"><div class="tlt">{t}</div><div>{x}</div><span class="box"></span></div></div>' for d, t, x in plan) +
        '<div class="tli last"><div class="tld"><small>Día</small>30</div><div class="tlb"><div class="tlt">Revisión</div><div>Respondé:</div>' +
        ul(['¿Qué contenido retuvo más?', '¿Qué tema generó más conversación?', '¿Qué preguntas se repitieron?', '¿Qué personas demostraron intención?',
            '¿Qué oferta podría resolver su problema?', '¿Qué debo cambiar el próximo mes?']) + '</div></div></div>',
        quote('El objetivo de los 30 días no es “hacerse viral”. Es salir con un sistema de aprendizaje y una primera evidencia de qué funciona.'),
)

# ---------- CAPÍTULO 16 ----------
def icase(letter, title, rows, story, lesson):
    r = ''.join(f'<div class="ir"><span>{k}</span>{v}</div>' for k, v in rows)
    s = f'<p class="istory">{story}</p>' if story else ''
    return f'<div class="icase"><div class="ihead"><span class="il">{letter}</span>{title}</div><div class="ibody">{r}{s}<div class="ilesson"><b>Lección:</b> {lesson}</div></div></div>'

chapter('c16', 'Capítulo', '16', 'Casos integrados:<br>cómo aplicar el sistema',
        'Cinco negocios distintos, una misma lógica.', 'VARC',
        icase('A', 'Floristería', [('Situación', 'Negocio local con necesidad de clientes.'), ('Territorio', 'Flores, decoración, eventos y formación.'),
                                   ('Contenido práctico', 'Cuidado de flores, elección de arreglos, errores frecuentes en eventos.'),
                                   ('Contenido de conexión', 'Historias de bodas, criterio estético, opinión sobre tendencias.'),
                                   ('Conversión', 'Recurso para organizar un evento o clase para floristas.')],
              'Ejemplo: con unos 1.900 seguidores, vende dos formaciones presenciales de 1.500 € cada una, además de captar clientes para la floristería.',
              'una audiencia pequeña puede tener valor si está alineada.'),
        icase('B', 'Escuela de drift', [('Situación', 'Negocio experiencial.'), ('Territorio', 'Drift, conducción, adrenalina y experiencia.'),
                                        ('Identidad', 'Estética visual fuerte y coherente.'), ('Contenido', 'Demostraciones, experiencias, errores, técnica, historias.'),
                                        ('Conversión', 'Reserva de experiencia.')],
              'Es una marca que integra identidad visual y experiencia: lo que se ve en el contenido es lo que se vive en la pista.',
              'no todos los negocios venden “resolver un dolor”. Algunos venden deseo, identidad y experiencia.'),
        icase('C', 'Tatuador', [('Situación', 'Profesional creativo.'), ('Contenido', 'Proceso, decisiones de diseño, errores, historias de clientes, opinión estética.')],
              'Mostrar el proceso de un tatuaje de principio a fin es un formato que puede alcanzar cientos de miles de visualizaciones.',
              'la experiencia profesional puede convertirse en entretenimiento y educación.'),
        icase('D', 'Coach / servicio premium', [('Situación', 'Pocos clientes, ticket alto.'), ('Contenido', 'Problemas específicos del cliente, casos y perspectiva.'),
                                                ('Conversión', 'Recurso + conversación + diagnóstico.')],
              'Ejemplo: 20 asesorías individuales de 500 € en dos semanas suman 10.000 €.',
              'la cantidad de seguidores no determina por sí sola el potencial económico.'),
        icase('E', 'Formadora de peinados', [('Situación', 'Audiencia existente pero necesidad de monetización.'), ('Oferta', 'Formación específica.')],
              'Ejemplo: cinco alumnas a 2.500 € suman 12.500 € con una sola formación.',
              'cuando existe una transformación concreta y una oferta clara, la audiencia puede convertirse en compradores.'),
)

# ---------- CAPÍTULO 17 ----------
chapter('c17', 'Capítulo', '17', 'El sistema operativo<br>de tu marca',
        'Una marca personal madura no depende de inspiración. Depende de un sistema.', 'VARC',
        lead('Una marca personal madura no depende de inspiración. <b>Depende de un sistema.</b> Cada semana deberían existir cinco movimientos:'),
        '<div class="moves">' + ''.join(f'<div class="mv"><div class="mvn">{i+1}</div><div class="mvt">{t}</div><div class="mvd">{d}</div></div>' for i, (t, d) in enumerate([
            ('Escuchar', 'Revisá comentarios, mensajes, preguntas y objeciones.'), ('Crear', 'Convertí esas señales en contenido.'),
            ('Publicar', 'Distribuí de manera consistente.'), ('Conversar', 'Profundizá con las personas que muestran interés.'),
            ('Aprender', 'Medí qué ocurrió y ajustá.')])) + '</div>',
        p('Esto crea un ciclo:'),
        formula(['Mercado', 'Contenido', 'Atención', 'Conversación', 'Aprendizaje', 'Nuevo contenido'], 'El ciclo'),
        p('El ciclo se vuelve más potente con el tiempo porque cada semana tenés más información sobre tu audiencia.'),
        quote('La marca deja de ser “lo que publicás” y pasa a ser un sistema de inteligencia comercial.'),
        exercise('Podés responder claramente…',
                 checks(['¿Qué problema resuelvo?', '¿Para quién?', '¿Por qué deberían recordarme?', '¿Qué contenido demuestra mi capacidad?',
                         '¿Qué contenido demuestra mi perspectiva?', '¿Qué recurso puedo ofrecer?', '¿Qué conversación quiero generar?',
                         '¿Qué oferta existe después de la conversación?', '¿Qué métricas indican progreso?']),
                 p('<b>Si no podés responder alguna, ahí está tu siguiente proyecto.</b>'), tag='Checklist de madurez'),
)

# ---------- CONCLUSIÓN ----------
chapter('concl', 'Conclusión', None, 'Dejá de esperar<br>permiso',
        'No necesitás ser famoso. Necesitás ser relevante.', 'VARC',
        lead('No necesitás ser famoso. <b>Necesitás ser relevante.</b>'),
        p('No necesitás una audiencia gigantesca. Necesitás que las personas correctas entiendan qué hacés, confíen en tu criterio y sepan cómo avanzar con vos. El recorrido es simple de describir, aunque requiere trabajo:'),
        formula(['Visibilidad', 'Autoridad', 'Relación', 'Conversión']),
        deflist([('Visibilidad', 'Hace que te descubran.'), ('Autoridad', 'Demuestra que sabés.'), ('Relación', 'Hace que confíen.'),
                 ('Conversión', 'Transforma esa confianza en una oportunidad.')]),
        p('No hay magia. Hay método, repetición, aprendizaje y adaptación. Tu marca personal tampoco es un personaje. Es una selección intencional de las señales que querés que el mercado asocie con vos.'),
        '<div class="manifesto"><div class="mcol"><div class="mh">Empezá con lo que tenés</div><div>Un teléfono.</div><div>Una experiencia.</div><div>Un problema que sabés resolver.</div><div>Una persona a la que podés ayudar.</div></div>'
        '<div class="mcol"><div class="mh">Después</div><div>Publicá.</div><div>Escuchá.</div><div>Ajustá.</div><div>Volvé a publicar.</div></div></div>',
        quote('La reputación se construye por acumulación.'),
        p('Tu objetivo no es que todo el mundo te conozca. Es que, cuando aparezca el problema correcto frente a la persona correcta, <b>tu nombre sea una de las opciones que recuerde.</b>'),
        with_action=False,
)

# ---------- WORKBOOK ----------
TOC.append(('wb', '', 'Workbook profesional', 'Workbook'))
add('''<section class="opener wbopen" id="wb">
  <div class="oglow"></div>
  <div class="otop"><span class="olabel">Herramientas</span><span class="obrand">De Invisible a Referente</span></div>
  <div class="onum wbword">WORK<br>BOOK</div>
  <h1 class="otitle">Workbook profesional</h1>
  <div class="obar"></div>
  <p class="osub">No leas estas páginas como teoría. Completalas. La función del workbook es convertir el contenido en decisiones.</p>
  <div class="obottom"><div class="wbsec">8 secciones · Bonus 15 hooks · Checklist de publicación</div></div>
</section>''')

def wsec(n, title, *blocks):
    return f'<div class="wsec"><div class="wsh"><span>{n:02d}</span>{title}</div>{"".join(blocks)}</div>'

def stage_pick():
    st = ['Etapa 1 — Exploración', 'Etapa 2 — Profesional invisible', 'Etapa 3 — Creador atascado', 'Etapa 4 — Audiencia sin monetización', 'Etapa 5 — Referente']
    return '<div class="picks">' + ''.join(f'<div><span class="box"></span>{s}</div>' for s in st) + '</div>'

body(
    wsec(1, 'Diagnóstico de etapa', '<div class="wqt">Marcá una:</div>', stage_pick(),
         wq('¿Cuál es tu cuello de botella actual?'), wq('¿Qué evidencia tenés de que ese es el problema?'),
         wq('¿Qué acción concreta podría mover esa variable durante los próximos 7 días?')),
    wsec(2, 'Posicionamiento', wq('Quiero ser reconocido por:'), wq('Mi cliente principal es:'), wq('El problema que resuelvo es:'),
         wq('El resultado que ayudo a conseguir es:'), wq('Mi perspectiva diferencial es:'), wq('Pruebas de experiencia que puedo mostrar:')),
    wsec(3, 'Mapa de cliente', wq('10 problemas funcionales:', 3), wq('10 frustraciones:', 3), wq('10 deseos:', 3), wq('5 miedos:', 2),
         wq('5 aspiraciones:', 2), wq('10 situaciones cotidianas en las que aparece el problema:', 3), wq('5 objeciones antes de comprar:', 2)),
    wsec(4, 'Banco de contenido', wq('10 preguntas frecuentes:', 3), wq('10 errores frecuentes:', 3), wq('10 opiniones que defiendo:', 3),
         wq('10 historias que puedo contar:', 3), wq('10 casos que puedo analizar:', 3), wq('10 comparaciones útiles:', 3)),
    wsec(5, 'Plantilla de guion', wq('Hook:'), wq('Contexto:'), wq('Tensión:'), wq('Valor:'), wq('Cierre:'), wq('CTA:'), wq('¿Qué métrica voy a observar?')),
    wsec(6, 'Recurso gratuito', wq('Problema específico que resolverá:'),
         '<div class="wqt">Formato:</div><div class="picks inline">' + ''.join(f'<div><span class="box"></span>{s}</div>' for s in ['PDF', 'Checklist', 'Clase', 'Plantilla', 'Diagnóstico', 'Otro: ________']) + '</div>',
         wq('Promesa:'), wq('CTA para solicitarlo:'), wq('Preguntas que haré después de entregarlo:')),
    wsec(7, 'Conversación comercial', wq('¿Qué está intentando conseguir la persona?'), wq('¿Qué la está frenando?'), wq('¿Qué probó?'),
         wq('¿Qué impacto tiene el problema?'), wq('¿Qué resultado considera valioso?'), wq('¿Existe encaje con mi oferta?'), wq('¿Cuál es el siguiente paso adecuado?')),
    wsec(8, 'Revisión mensual', wq('Contenido con mejor retención:'), wq('Contenido con mejores conversaciones:'), wq('Contenido que generó leads:'),
         wq('Oferta que más interés recibió:'), wq('Objeción repetida:'), wq('Aprendizaje principal:'), wq('Experimento del próximo mes:')),
)

# ---------- BONUS ----------
TOC.append(('bonus', '', 'Bonus: 15 hooks + checklist de publicación', 'Bonus'))
hooks = ['Si estás intentando ______, probablemente estés cometiendo este error.', 'La mayoría de ______ intenta resolverlo de esta manera. Yo lo haría distinto.',
         'Antes de invertir en ______, revisá estas tres cosas.', 'Si empezara de cero en ______, estas serían mis primeras decisiones.',
         'Tu problema no es ______. El problema está en ______.', 'Una señal de que ______ no está funcionando.', 'Lo que nadie te explica sobre ______.',
         '3 errores que veo constantemente en ______.', 'Si tenés poco presupuesto para ______, empezá por esto.',
         'Esto parece una buena idea, pero puede estar perjudicando ______.', 'Una pregunta que deberías hacerte antes de ______.',
         'Te muestro cómo abordaría ______ paso a paso.', 'El consejo que me hubiera gustado recibir cuando empecé en ______.',
         'Hay una diferencia enorme entre ______ y ______.', 'Si tus resultados están estancados, mirá primero ______.']
add('<section class="body" id="bonus"><div class="bonusbadge">Bonus</div><h2 class="ptitle">15 hooks para empezar</h2>'
    '<p class="lead">Completá los espacios con tu tema, tu cliente o tu sector. Cada plantilla puede generar decenas de piezas.</p>'
    '<div class="hooklist">' + ''.join(f'<div class="hl"><span>{i+1:02d}</span><div>{h.replace("______", "<i class=bl></i>")}</div></div>' for i, h in enumerate(hooks)) + '</div>'
    '<div class="newpage"></div><div class="bonusbadge">Bonus</div><h2 class="ptitle">Checklist de publicación</h2>'
    + checks(['La pieza habla a una persona concreta.', 'El inicio hace evidente por qué debería prestar atención.',
              'El contenido entrega una idea, aprendizaje o perspectiva.', 'La pieza refuerza mi territorio.', 'No hago afirmaciones que no pueda respaldar.',
              'El CTA tiene sentido para el objetivo.', 'Sé qué métrica quiero observar.', 'La pieza puede convertirse en otra pieza o formato.']).replace('class="checks"', 'class="checks big"')
    + '</section>')

# ---------- CONTRAPORTADA ----------
add('''<section class="backpage">
  <div class="oglow big"></div>
  <div class="bp-q">“Tu objetivo no es que todo el mundo te conozca. Es que, cuando aparezca el problema correcto frente a la persona correcta, <span>tu nombre sea una de las opciones que recuerde.</span>”</div>
  <div class="bp-bar"></div>
  <div class="bp-title">DE <span>INVISIBLE</span> A REFERENTE</div>
  <div class="bp-varc"><span>Visibilidad</span>→<span>Autoridad</span>→<span>Relación</span>→<span>Conversión</span></div>
  <div class="bp-ed">Edición Premium · 2026</div>
</section>''')

# ---------- ÍNDICE ----------
rows = ''
for key, num, title, label in TOC:
    pg = TOC_PAGES.get(key, '')
    numcell = num if num else {'Introducción': '—', 'Conclusión': '—', 'Workbook': 'WB', 'Bonus': '★'}.get(label, '')
    cls = ' special' if not num else ''
    rows += f'<a class="trow{cls}" href="#{key}"><span class="tn">{numcell}</span><span class="tt">{title}</span><span class="dots"></span><span class="tp">{pg}</span></a>'
toc_html = f'<section class="body toc"><div class="kicker">Contenido</div><h2 class="ptitle">Índice</h2><div class="toclist">{rows}</div></section>'

html = ''.join(H).replace('%%TOC%%', toc_html)
css = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'style.css')).read()
doc = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>De Invisible a Referente</title>
<style>{css}</style></head><body>{html}</body></html>'''
open(OUT, 'w').write(doc)
print(json.dumps([k for k, *_ in TOC]))
