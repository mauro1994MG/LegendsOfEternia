# ---------- WORKBOOK ----------
TOC.append(('wb', '', 'Workbook: tus ejercicios', 'Herramientas'))
add('''<section class="opener wbopen" id="wb">
  <div class="oglow"></div>
  <div class="otop"><span class="olabel">Herramientas</span><span class="obrand">Toda la verdad sobre marca personal</span></div>
  <div class="onum wbword">WORK<br>BOOK</div>
  <h1 class="otitle">Tus ejercicios</h1>
  <div class="obar"></div>
  <p class="osub">No leas estas páginas como teoría. Completalas. Su función es convertir lo que leíste en decisiones.</p>
  <div class="obottom"><div class="wbsec">10 secciones · Plan de 30 días · Bonus</div></div>
</section>''')

def wsec(n, title, *blocks):
    return f'<div class="wsec"><div class="wsh"><span>{n:02d}</span>{title}</div>{"".join(blocks)}</div>'

body(
    wsec(1, 'Mapa inverso', wq('1. ¿Cuál es el resultado que quiero lograr?', 3), wq('2. Para lograrlo, ¿por qué tendría que ser conocido?', 3),
         wq('3. ¿Qué acciones concretas tengo que repetir día tras día?', 3), wq('4. ¿Qué necesito aprender para hacerlas bien?', 3),
         wq('Crear contenido público, ¿me acerca o me aleja de este resultado?', 2)),
    wsec(2, 'Punto de partida', '<div class="wqt">Hoy soy:</div><div class="picks inline"><div><span class="box"></span>Estudiante</div><div><span class="box"></span>Experto</div></div>',
         wq('10 cosas que aprendo y pruebo (o 10 cosas que logré y resolví):', 5), wq('2 intereses personales que podría mencionar con naturalidad:', 2),
         wq('Si en 5 años mirara mi contenido, ¿me sentiría orgulloso? ¿Por qué?', 2)),
    wsec(3, 'Mi cliente y sus problemas', wq('Mi cliente ideal es:', 2), wq('10 a 15 problemas dolorosos que tiene:', 6), wq('Mi solución distinta para los 3 más importantes:', 4),
         wq('Credibilidad contextual que podría mencionar para cada uno:', 3)),
    wsec(4, 'Tabla de desacuerdos', table2('Lo que dicen o hacen en mi sector', 'Lo que yo pienso o haría', [('<br><br>', ''), ('<br><br>', ''), ('<br><br>', ''), ('<br><br>', ''), ('<br><br>', ''), ('<br><br>', '')]),
         wq('Mi postura distinta elegida:', 2), wq('Señales de que resuena (citas, mensajes, menciones):', 2)),
    wsec(5, 'Asociaciones y frase ancla', wq('2 asociaciones por las que quiero ser conocido:', 2), wq('2 asociaciones contra las que quiero ser conocido:', 2),
         wq('Acciones que repetiré cada semana para lograrlas:', 2), wq('Frase ancla: Para ______ que quiere ______, creo que deberían ______ y no ______.', 3),
         wq('Versión final de mi frase ancla:', 2)),
    wsec(6, 'Mi contenido', wq('Cómo es mi apertura en cuatro pasos (para quién, por qué yo, hacia dónde, primer aprendizaje):', 4),
         wq('Mi estructura base de una pieza:', 3), wq('Mis tres capas: ¿qué contenido profundo, amplio y personal publicaré este mes?', 4), wq('¿Qué métrica voy a mirar?', 2)),
    wsec(7, 'Mi capacidad', wq('Horas por semana que puedo dedicar de verdad:', 1), wq('Qué partes del proceso me dan energía y cuáles me la quitan:', 3),
         wq('Mejor momento del día para crear:', 1), '<div class="wqt">Mi medio:</div><div class="picks inline"><div><span class="box"></span>Video</div><div><span class="box"></span>Audio</div><div><span class="box"></span>Texto</div><div><span class="box"></span>Gráficos</div></div>',
         wq('Mi plataforma principal y mi secundaria:', 2), wq('Mi ritmo inicial de publicación y cuándo lo revisaré:', 2)),
    wsec(8, 'Biblioteca de empaques', wq('10 títulos o ganchos que me llamaron la atención (y de qué plataforma):', 6), wq('3 que podría adaptar a mi tema:', 3)),
    wsec(9, 'Mis tres primeros contenidos', wq('Presentación: 3 a 5 momentos y la lección de cada uno:', 5), wq('Clase profunda: de 3 a 5 ideas grandes:', 4), wq('Experimento: formato y qué quiero descubrir:', 3)),
    wsec(10, 'Revisión mensual', wq('Contenido con mejor respuesta:', 2), wq('Contenido que generó conversaciones:', 2), wq('Lo que más me gustó hacer:', 2),
         wq('Lo que cambiaría el próximo mes:', 2), wq('Experimento del próximo mes:', 2)),
)

# ---------- PLAN DE 30 DÍAS ----------
TOC.append(('plan', '', 'Plan de acción de 30 días', 'Herramientas'))
plan = [('1–3', 'Mapa inverso', 'Respondé las cuatro preguntas y decidí si el contenido público te conviene.'),
        ('4–6', 'Punto de partida', 'Definí si sos estudiante o experto y armá tu bitácora o tu banco de pruebas.'),
        ('7–9', 'Tu cliente', 'Escribí 10 a 15 problemas dolorosos y tu solución distinta para cada uno.'),
        ('10–12', 'Tu postura', 'Completá la tabla de desacuerdos y elegí tres posturas para probar.'),
        ('13–15', 'Frase ancla', 'Escribí tres versiones de tu frase y elegí una.'),
        ('16–18', 'Sistema', 'Definí tu capacidad, tu medio, tus plataformas y tu ritmo inicial.'),
        ('19–23', 'Primer contenido', 'Preparalo, grabalo y publicalo. Empezá por tu presentación.'),
        ('24–27', 'Escuchar y ajustar', 'Revisá respuestas, mensajes y comentarios. Anotá qué resonó.'),
        ('28–29', 'Cascada', 'Convertí tu mejor momento en tres piezas nativas.')]
add('<section class="body" id="plan"><div class="kicker">Herramientas</div><h2 class="ptitle">Plan de acción de 30 días</h2>'
    '<p class="lead">Un recorrido simple para pasar de la lectura a la acción. El objetivo no es hacerte viral: es que termines con un sistema y una primera evidencia de qué funciona.</p><div class="timeline">' +
    ''.join(f'<div class="tli"><div class="tld"><small>Días</small>{d}</div><div class="tlb"><div class="tlt">{t}</div><div>{x}</div><span class="box"></span></div></div>' for d, t, x in plan) +
    '<div class="tli last"><div class="tld"><small>Día</small>30</div><div class="tlb"><div class="tlt">Revisión</div><div>Respondé:</div>' +
    ul(['¿Qué contenido tuvo mejor respuesta?', '¿Qué postura resonó más?', '¿Qué preguntas se repitieron?', '¿Qué cambio por el próximo mes?']) + '</div></div></div>'
    '</section>')

# ---------- BONUS ----------
TOC.append(('bonus', '', 'Bonus: 20 ganchos + checklist de publicación', 'Bonus'))
hooks = ['Si estás intentando ______, probablemente estés cometiendo este error.', 'La mayoría de ______ intenta resolverlo así. Yo lo haría distinto.',
         'Antes de invertir en ______, revisá estas tres cosas.', 'Si empezara de cero en ______, estas serían mis primeras decisiones.',
         'Tu problema no es ______. El problema está en ______.', 'Una señal de que ______ no está funcionando.', 'Lo que nadie te explica sobre ______.',
         '3 errores que veo siempre en ______.', 'Si tenés poco presupuesto para ______, empezá por esto.',
         'Esto parece una buena idea, pero puede estar perjudicando ______.', 'Una pregunta que deberías hacerte antes de ______.',
         'Te muestro cómo abordaría ______ paso a paso.', 'El consejo que me hubiera gustado recibir cuando empecé en ______.',
         'Hay una gran diferencia entre ______ y ______.', 'Si tus resultados en ______ están estancados, mirá primero esto.',
         'No creo que el problema de ______ sea lo que te dijeron.', 'Esto es lo que dejaría de hacer en ______ si quisiera clientes.',
         'Todos recomiendan ______, pero a mí me funcionó lo contrario.', 'La razón por la que ______ no te da clientes.', 'Si solo pudieras hacer una cosa en ______, haría esta.']
add('<section class="body" id="bonus"><div class="bonusbadge">Bonus</div><h2 class="ptitle">20 ganchos para empezar</h2>'
    '<p class="lead">Completá los espacios con tu tema, tu cliente o tu sector. Cada plantilla puede generar decenas de piezas.</p>'
    '<div class="hooklist">' + ''.join(f'<div class="hl"><span>{i+1:02d}</span><div>{h.replace("______", "<i class=bl></i>")}</div></div>' for i, h in enumerate(hooks)) + '</div></section>')
add('<section class="body"><div class="bonusbadge">Bonus</div><h2 class="ptitle">Checklist de publicación</h2>'
    + checks(['La pieza le habla a una persona concreta.', 'El inicio deja claro por qué debería prestar atención.', 'Entrega una idea, un aprendizaje o una perspectiva.',
              'Refuerza mi postura distinta.', 'Tiene una credibilidad contextual clara.', 'El empaque invita a abrir.', 'No hago afirmaciones que no pueda respaldar.',
              'Sé qué métrica quiero observar.', 'Puede convertirse en otras piezas.']).replace('class="checks"', 'class="checks big"') + '</section>')

# ---------- CONTRAPORTADA ----------
add('''<section class="backpage">
  <div class="oglow big"></div>
  <div class="bp-q">“Los seguidores aplauden. <span>Los clientes confían, y por eso compran.</span>”</div>
  <div class="bp-bar"></div>
  <div class="bp-title">TODA LA <span>VERDAD</span><br>SOBRE MARCA PERSONAL</div>
  <div class="bp-varc">Emanuel Galván · Experto en Marketing Digital</div>
  <div class="bp-ed">Edición 2026</div>
</section>''')
