# Guía de figuras del informe — sistema visual y especificación por figura

> **Para quién es.** Para quien tenga que **producir las figuras del informe desde cero**, con un
> solo estilo, sin haber participado del trabajo experimental. Define un sistema visual completo y
> después especifica, figura por figura, qué tiene que mostrar cada una, con qué rótulos exactos y
> con qué trampas.
>
> **Regla de oro sobre el formato de entrega.** **No generes las figuras como imagen de un modelo
> de imagen.** Los generadores de imagen deforman el texto: un diagrama técnico con quince rótulos
> vuelve con palabras inventadas, y eso en un informe académico es peor que no tener figura.
> **Entregá código vectorial**: SVG escrito a mano, o un script de Python con `matplotlib`, o
> Graphviz. El texto queda exacto, el resultado es reproducible y se puede corregir una etiqueta sin
> rehacer el dibujo. Si el entorno no permite ejecutar código, entregá **el SVG completo como
> texto**, listo para guardar y abrir.
>
> **Qué NO hay que inventar.** Todo dato, rótulo, estado, nombre de módulo y relación que aparece
> en las especificaciones de la sección 5 sale del texto vigente del informe o del código
> verificado. Si una figura parece necesitar un dato que no está acá, **no lo supongas: preguntá**.
> Una figura con un número inventado es indistinguible de una cita inventada.

---

## 1. Las seis figuras del informe

| Figura | Sección | Qué es | Tipo | Estado hoy |
|---|---|---|---|---|
| **4.1** | 17.3.3 | Vista conceptual de la arquitectura | diagrama de bloques | existe, rehacer |
| **4.2** | 17.3.5 | Flujo conceptual del pipeline de medios | diagrama de flujo | existe, rehacer |
| **4.3** | 17.3.6.1 | Máquina de estados del motor de patrones | diagrama de estados | existe, **con errores de fondo** |
| **4.4** | 17.3.6.4 | Cadena de traducción de condición a alerta | diagrama de cadena | existe, rehacer |
| **4.5** | 17.4.1 | Vista de procesos de la plataforma | diagrama de despliegue | existe, rehacer |
| **4.6** | 17.5.4 | Fotograma con alerta confirmada | captura anotada | existe, **no se redibuja** |

Hoy conviven **dos lenguajes visuales distintos**: las cuatro de la sección 17.3 son diagramas de
línea en azul marino con iconos, y la 4.5 salió de una biblioteca de graficación, con otra paleta,
otra tipografía y una nota de procedencia impresa dentro de la imagen. Esa mezcla se lee como
descuido de edición. **El objetivo de esta guía es que las seis se lean como una sola familia.**

La 4.6 es un fotograma real y no se redibuja: sólo se le normaliza el tratamiento, según la
sección 5.6.

---

## 2. El sistema visual

### 2.1 Superficie, tinta y color

La paleta de datos no se eligió a ojo: pasó un validador de seis chequeos (banda de luminosidad,
piso de croma, separación para daltonismo, piso de visión normal y contraste) en modo claro sobre
la superficie del informe. **No la cambies.** Lo que esta guía agrega es la tinta estructural para
los diagramas, derivada del mismo azul.

| Rol | Valor | Dónde se usa |
|---|---|---|
| Superficie de diagramas | `#FFFFFF` | fondo de las figuras 4.1 a 4.5 |
| Superficie de figuras de datos | `#FCFCFB` | fondo de cualquier gráfico con ejes |
| Tinta estructural | `#1A2E5A` | trazo de cajas, flechas de flujo, rótulos de nodo |
| Relleno de caja | `#FFFFFF` | interior de todos los nodos |
| Insignia de icono | `#E7EFFA` | círculo detrás del icono, dentro del nodo |
| Acento primario | `#2A78D6` | serie 1, resaltado, anotaciones de ventana temporal |
| Acento de atención | `#EB6834` | serie 2, el nodo terminal de una cadena, el hecho crítico |
| Tercer color | `#1BAF7A` | serie 3 **sólo con etiqueta directa visible** |
| Texto primario | `#0B0B0B` | rótulos de nodo |
| Texto secundario | `#52514E` | texto interior de nodo, etiquetas de flecha |
| Texto atenuado | `#8A8985` | leyendas y anotaciones de segundo orden |
| Grilla y ejes | `#E4E3DF` | sólo en figuras con ejes, siempre línea fina continua |

⚠ **El tercer color tiene contraste 2,74 sobre la superficie, por debajo de 3:1.** Por regla de
relieve, toda serie de ese color lleva **etiqueta directa visible** y nunca se identifica sólo por
color. No lo uses para trazos finos ni para texto.

**Un color, un significado, en las seis figuras.** El naranja es el hecho terminal o el elemento que
el lector tiene que encontrar primero; el azul de acento es temporalidad y resaltado; el azul marino
es estructura. Si en una figura el naranja marca el repositorio y en otra marca un error, el sistema
se rompe.

### 2.2 Tipografía

- **Una sola familia sans en las seis figuras**, humanista y de caja alta legible en cuerpo chico.
  Preferencia: Inter, Source Sans 3 o IBM Plex Sans. Alternativa segura si no hay tipografía
  instalable: DejaVu Sans.
- **Nunca dos familias en la misma figura**, ni serif dentro de un diagrama.
- Tamaños referidos al **ancho final de 16 cm**: rótulo de nodo **10 pt en semibold**; texto
  interior de nodo **8,5 pt regular**; etiqueta de flecha **8 pt**; leyenda **8,5 pt**; anotación
  atenuada **7,5 pt**.
- **Los valores del contrato van en monoespaciada**, porque son literales del sistema y no prosa:
  `inactive`, `candidate`, `confirmed`, `sustained`, `resolved`, `confirm_after_ms`,
  `media.detection.v1`. Todo lo demás, en la sans.
- **Minúscula rioplatense en los rótulos descriptivos.** «Plano de medios», no «Plano De Medios».
  Mayúscula sólo al principio y en nombre propio.
- Nunca versalitas, nunca subrayado, nunca texto en diagonal, nunca texto sobre un fondo de color
  saturado.

### 2.3 Geometría

- **Nodo**: rectángulo de esquinas redondeadas, radio equivalente a 8 px sobre un lienzo de 1.900 px
  de ancho. Trazo `#1A2E5A` de 2 px. Relleno blanco. Sin sombra, sin degradado, sin borde doble.
- **Aire interior** del nodo: al menos 12 px arriba y abajo, 16 px a los lados. Un nodo apretado se
  lee como error de exportación.
- **Iconos**: opcionales, y si van, van en **las seis o en ninguna**. Line-art de trazo 1,5 px, un
  solo color `#1A2E5A`, dentro de una insignia circular `#E7EFFA` de 40 px. Un icono por nodo, a la
  izquierda del rótulo, alineado a su eje vertical. **Sin iconos de relleno, sin emoji, sin
  pictogramas de banco de imágenes.**
- **Flechas**: trazo de 1,6 px, punta triangular cerrada de 9 px. Tres tipos y sólo tres:
  - **continua** para flujo de datos y eventos,
  - **punteada** para influencia de configuración y capacidades de soporte,
  - **continua fina en gris `#8A8985`** para lectura y consolidación, que no es ruta crítica.
- **Ortogonalidad**: las flechas van rectas u ortogonales con codo redondeado. **Prohibidas las
  curvas de Bézier que se cruzan**: en la 4.5 actual cuatro curvas se cruzan en el centro y el
  lector no puede seguir ninguna. Si dos flechas deben cruzarse, una hace un salto de puente.
- **Etiqueta de flecha**: sobre el trazo, con un recuadro blanco de fondo que corte la línea, nunca
  al costado suelta.
- **Cuadrícula de composición**: alineá todo a una grilla; los nodos de un mismo nivel comparten
  altura y ancho. La irregularidad de tamaño se lee como jerarquía y engaña.
- **Máximo siete nodos por figura**, sin contar los de contexto. Si hay más, la figura está haciendo
  dos trabajos.

### 2.4 Lo que nunca va dentro de la imagen

Tres reglas que corrigen defectos concretos del estado actual:

1. **Ningún título horneado.** El epígrafe `Figura 4.N` y su título los pone el procesador de texto.
   Duplicarlo dentro de la imagen se lee como descuido.
2. **Ninguna nota de procedencia impresa.** Hoy la 4.5 lleva cinco renglones de nota adentro del
   PNG. Eso tiene dos costos: el lienzo se expande hasta abarcar la línea de texto más larga, y al
   insertar a 16 cm **toda la figura se achica** hasta dejar los rótulos ilegibles. La nota va en el
   documento, como párrafo `Nota.` debajo del epígrafe.
3. **Ningún número de página, marca de agua, logo, borde exterior ni fondo de color.**

### 2.5 Tamaño y exportación

- **Ancho de diseño: 16 cm.** Diseñá a ese ancho y **no reescales al insertar**: los cuerpos de
  letra se eligieron para ese tamaño final.
- Alto libre, con un tope razonable de 12 cm para que la figura y su epígrafe entren en una página.
- **Entregá SVG y PNG.** El SVG es la fuente; el PNG a **300 dpi** es lo que se inserta.
- Márgenes de recorte ajustados, con 4 px de aire. Sin espacio muerto a los lados.
- Nombre de archivo en minúscula con guiones: `fig-4-3-maquina-de-estados.svg`.

### 2.6 Legibilidad: gris, daltonismo e impresión

- **La figura tiene que funcionar impresa en escala de grises.** Probalo: convertí a gris y mirá si
  se sigue distinguiendo todo.
- **Ninguna información codificada sólo por color.** Si dos flechas significan cosas distintas, se
  distinguen además por **patrón de trazo** y llevan leyenda o etiqueta directa.
- Contraste mínimo 4,5:1 para cualquier texto sobre su fondo.
- Sin dependencia del hover ni de la interacción: es papel.

---

## 3. Reglas de contenido, para las seis

1. **Autocontención.** La figura no cita documentos internos, ni decisiones de arquitectura por
   número, ni rutas de archivos del repositorio. Nombres de artefactos de salida del sistema, sí.
2. **Nada de lo dibujado puede contradecir el texto** de la sección donde va. Si al dibujar
   aparece una contradicción, no la resuelvas en el dibujo: reportala.
3. **Lo que no se ejecutó no se dibuja como si existiera.** Y lo que sí existe no se dibuja como
   pendiente: la distribución de alertas es un servicio más y va en línea continua, nunca punteada.
4. **Español rioplatense**, sin anglicismos evitables. «flujo de datos», no «data flow». Las
   excepciones son los valores del contrato, que son literales.
5. **Una figura, una idea.** Si el epígrafe necesita dos oraciones para decir qué muestra, sobra
   contenido.

---

## 4. Corrección obligatoria: la Figura 4.3 hoy es incorrecta

Antes de rehacerla hay que saber esto, porque **el dibujo actual y el texto que lo acompaña
afirman dos transiciones que el sistema no hace**. Verificado contra el motor de patrones del plano
de control, no contra la documentación.

**Lo que el dibujo actual muestra y está mal:**

| Lo dibujado hoy | Lo que hace el sistema |
|---|---|
| `candidate → inactive` con el rótulo «evidencia insuficiente / no persiste» | desde `candidate`, si la evidencia se despeja o expira, el patrón va a **`resolved`**, no a `inactive` |
| `resolved → inactive` con el rótulo «cierre del episodio» | **no existe ninguna transición hacia `inactive`**: es sólo el estado inicial, y nada vuelve a él |

**Lo que falta y hay que agregar:**

- **El salto directo a `confirmed`.** Si la primera evidencia ya satisface la ventana de
  confirmación, el patrón pasa de `inactive` o de `resolved` **directamente a `confirmed`**, sin
  pasar por `candidate`.
- **La reapertura.** Un episodio nuevo sobre el mismo sujeto arranca **desde `resolved`**, que es
  donde quedó el anterior. Esa reapertura es la que produce una **re-alerta**, que el informe
  contabiliza aparte de los falsos positivos.
- **Los dos caminos a `resolved`**, que hoy se ven como uno: **despeje sostenido** de la condición
  cumplida la histéresis, y **ausencia del sujeto** por encima del tiempo de expiración.

**El texto de 17.3.6.1 arrastra el mismo error** en dos oraciones: «el episodio pasa a resolved y
retorna a inactive» y «el patrón vuelve a inactive sin generar una alerta». La sección está cerrada,
así que **esto se reporta y lo decide el autor**; la figura no puede corregirse sola y dejar al
texto diciendo lo contrario. **Dibujá la versión correcta y avisá que el texto necesita el mismo
ajuste.**

---

## 5. Especificación por figura

### 5.1 Figura 4.1 — Vista conceptual de la arquitectura

**Va en** 17.3.3. **Qué tiene que mostrar:** la organización lógica de alto nivel, con la cadena
principal en una sola línea horizontal y dos entradas transversales.

**Cadena principal**, de izquierda a derecha, flechas continuas:

`Fuentes visuales` → `Plano de medios` → `Bus interno de eventos` → `Plano de control` →
`Distribución de alertas confirmadas` → `Consumidores desacoplados`

**Relaciones transversales**, flechas punteadas. ✎ **2026-09-08 — corregido: las dos barras NO
conectan lo mismo, y la versión anterior de esta guía decía «los cuatro módulos ejecutables» en las
dos, que está mal por partida doble.** Los módulos ejecutables son **tres**, y el bus no es uno de
ellos: es transporte. Los destinos exactos son estos.

- **Arriba, `Configuración experimental` → TRES destinos**, y el bus **no** es uno:
  `Plano de medios`, `Plano de control`, `Distribución de alertas confirmadas`.
- **Abajo, `Soporte experimental` ← CUATRO orígenes**, y el bus **sí** es uno:
  `Plano de medios`, `Bus interno de eventos`, `Plano de control`,
  `Distribución de alertas confirmadas`. Lleva el subtítulo «trazabilidad · observabilidad ·
  inspección y reporte».

**Por qué la asimetría, para que no se lea como un error de dibujo.** El bus **no tiene
configuración propia**: la tabla de elementos mínimos de la configuración experimental enumera
«las configuraciones efectivas del plano de medios, del plano de control y del módulo de
distribución», tres y no cuatro, y los parámetros del transporte se declaran dentro de la
configuración de los módulos que lo abren y lo consumen. Pero el bus **sí es origen de una señal
observable**: la tabla de señales observables del sistema atribuye los huecos de secuencia
directamente al bus, mientras que los eventos de percepción se atribuyen al plano de medios y las
transiciones de patrón al plano de control. De modo que el bus se observa aunque no se configure, y
la figura tiene que mostrar exactamente eso.

**Corrección concreta respecto del dibujo actual:** hoy la configuración baja a cuatro bloques.
**Sobra la flecha que va al bus.** Las cuatro del soporte están bien y se conservan.

**Composición:** **no dibujes flechas divergentes desde un punto**. Usá una barra horizontal de
distribución con bajadas ortogonales cortas, tres arriba y cuatro abajo. El abanico de curvas del
dibujo actual es su defecto de composición más visible.

**Nota para el documento**, no para la imagen, que evita que un lector cuente las flechas y crea
que falta una: «El bus interno de eventos recibe soporte experimental pero no configuración propia:
sus parámetros se declaran en la configuración de los módulos que lo abren y lo consumen».

**El nodo de consumidores** lleva dos ítems: «adaptadores de notificación» y «clientes de inspección
en vivo».

**Leyenda obligatoria**, abajo a la derecha: línea continua «flujo de datos y eventos», línea
punteada «configuración y soporte».

**Trampas:**
- El soporte experimental es **una capacidad transversal, no una etapa del flujo**: no puede quedar
  en la línea principal.
- La distribución va en la cadena principal, en continua.
- **«Módulos ejecutables» son tres**, y el texto nunca dice «cuatro módulos». El bus es un nodo de
  la cadena principal, pero no un módulo: no se lo cuenta entre ellos ni se le atribuye ciclo de
  vida propio. Si una figura o una oración necesita contarlos, son tres.
- El bus recibe y emite flechas continuas de la cadena, y **una sola** punteada, la del soporte.

---

### 5.2 Figura 4.2 — Flujo conceptual del pipeline de medios

**Va en** 17.3.5. **Qué tiene que mostrar:** la cadena de transformación interna del plano de
medios, con una frontera de entrada y una de salida.

**Las seis etapas internas**, en cadena, con estos rótulos exactos:

1. `Ingesta y decodificación`
2. `Control de ritmo y selección de unidades visuales`
3. `Normalización visual`
4. `Inferencia open-vocabulary`
5. `Postproceso y normalización de detecciones`
6. `Publicación de evidencia perceptiva`

**Composición:** las seis etapas dentro de **un recuadro contenedor** rotulado «Plano de medios».
Con seis nodos, la cadena en una sola fila queda ilegible a 16 cm: usá **dos filas de tres en
serpentina**, con el codo de retorno marcado, o una fila vertical de seis con la cadena a la
izquierda y el texto a la derecha.

**Fuera del recuadro, a la izquierda:** `Fuentes visuales`, con la nota de que son externas al
plano.

**Fuera del recuadro, a la derecha:** `Evento de percepción normalizado`, **deliberadamente
afuera**, para marcar la frontera de salida hacia el bus interno de eventos y el plano de control.
El texto lo dice explícitamente: esa posición es intencional y hay que respetarla.

**Entrada transversal punteada:** `Configuración de corrida`, que parametriza la ejecución sin
formar parte del procesamiento cuadro a cuadro.

**Trampa:** los dos escenarios experimentales no cambian la salida del plano, sólo la forma de
lectura. No dibujes dos ramas paralelas: es **un solo camino** con una anotación que diga que la
diferencia entre escenarios se resuelve en la ingesta.

---

### 5.3 Figura 4.3 — Máquina de estados del motor de patrones

**Va en** 17.3.6.1. **Leé antes la sección 4 de esta guía: la versión actual es incorrecta.**

**Cinco estados**, en monoespaciada: `inactive` · `candidate` · `confirmed` · `sustained` ·
`resolved`.

**Transiciones, todas y sólo estas:**

| Desde | Hacia | Etiqueta | Trazo |
|---|---|---|---|
| `inactive` | `candidate` | primera evidencia | continua |
| `inactive` | `confirmed` | primera evidencia que ya cumple la ventana | continua |
| `candidate` | `confirmed` | ventana de confirmación cumplida | continua, **resaltada** |
| `candidate` | `resolved` | despeje o ausencia, sin alerta | punteada |
| `confirmed` | `sustained` | la condición persiste | continua |
| `sustained` | `sustained` | evidencia continua, sin alerta nueva | auto-lazo continuo |
| `confirmed` o `sustained` | `resolved` | despeje sostenido cumplida la histéresis | continua |
| `confirmed` o `sustained` | `resolved` | ausencia por encima del tiempo de expiración | punteada |
| `resolved` | `candidate` | nueva evidencia sobre el mismo sujeto | continua |
| `resolved` | `confirmed` | nueva evidencia que ya cumple la ventana, **re-alerta** | continua |

**El elemento que la figura tiene que hacer imposible de pasar por alto:** la **alerta interna se
registra en la entrada a `confirmed`**, y sólo ahí. Marcá esa transición con el acento primario y
colgale un nodo lateral, en naranja de atención, rotulado «alerta interna registrada». Entre la
primera evidencia y la alerta media una condición temporal, y **eso es exactamente lo que separa
una detección de una alerta**: es la idea central del capítulo.

**Anotaciones de ventana temporal**, en acento primario, con llave sobre el tramo que abarcan:
«ventana de confirmación» sobre `candidate → confirmed`, y «ventana de resolución» sobre el tramo
que llega a `resolved`.

**Anotación al pie del estado sostenido:** «la evidencia que sigue llegando lo mantiene acá y no
produce una alerta nueva».

**Trampas:**
- No dibujes ninguna flecha hacia `inactive`.
- `sustained` no es un paso obligatorio hacia `resolved`: se puede resolver desde `confirmed`.
- Las ventanas se expresan en milisegundos, no en cuadros. Si anotás unidades, que sean ms.

---

### 5.4 Figura 4.4 — Cadena de traducción de condición a alerta

**Va en** 17.3.6.4. **Qué tiene que mostrar:** cómo una condición definida en el plano metodológico
se materializa en la arquitectura, atravesando los dos planos.

**La cadena**, cinco eslabones:

`Condición observable` → `Estrategia de detección` → `Evidencia perceptiva normalizada` →
`Patrón de riesgo` → `Alerta interna`

**Composición en dos carriles horizontales**, que es lo que hace legible la figura y hoy no está:

- carril **plano de medios**: contiene la evidencia perceptiva normalizada,
- carril **plano de control**: contiene el patrón y la alerta interna,
- los dos primeros eslabones quedan **arriba de los carriles**, en una banda rotulada «definición
  metodológica», porque no son componentes de ejecución.

**Bajo el eslabón de estrategia**, como cuatro opciones y no como cadena: «prompt directo»,
«combinación de consultas», «evidencia auxiliar», «reglas contextuales».

**El último eslabón, en naranja de atención**, con la anotación: «salida asistiva del sistema; no
es una notificación externa ni una certificación normativa». Esa salvedad es una posición del
trabajo y la figura no puede omitirla.

---

### 5.5 Figura 4.5 — Vista de procesos de la plataforma

**Va en** 17.4.1. **Qué tiene que mostrar:** la disposición efectiva de procesos, complementaria de
la vista lógica de la 4.1. Es la figura que más gana con el rehacé: la actual tiene cuatro curvas
cruzándose y una nota impresa adentro.

**Fila central, los tres servicios**, cada uno con sus responsabilidades como texto interior:

| Nodo | Texto interior |
|---|---|
| `Servicio de medios` | ingesta · control de ritmo · normalización · inferencia OVD · postproceso · publicación · modelo cargado al arranque |
| `Servicio de control` | consumo de eventos · motor de patrones · alertas internas · persistencia · métricas |
| `Módulo de distribución` | política de entrega · registro de idempotencia · publicación por el canal externo · registros |

Entre ellos, flechas continuas de flujo con etiqueta: `bus` de medios a control, `canal de alertas`
de control a distribución.

**Fila superior, dos clientes:** `Orquestador experimental` («manifiesto de experimento · dispara
los tres servicios · consolida artefactos y reporta») e `Interfaz de inspección` («cliente de las
interfaces de servicio de los planos de medios y de control»).

**Fila inferior, en naranja de atención:** `Repositorio de corrida` («archivos de sólo adición, uno
por plano»), que recibe de medios y de control con la etiqueta «persiste antes de publicar», y del
que sale una flecha gris fina de «lectura y consolidación» hacia los dos clientes de arriba.

**El orden de arranque**, con marcadores ①②③ sobre las flechas del orquestador a cada servicio:

> **① control → ② distribución → ③ medios.**

⚠ **Esta es la trampa más cara de todo el informe.** Una versión anterior decía que el orden era «el
inverso del flujo de datos», y es **falso**. El orden real, verificado contra el orquestador, es
control primero, distribución segunda porque necesita el identificador de la corrida de control, y
medios al final. Y la garantía de que no se pierda ninguna alerta **no la da el orden**: la da el
publicador, que espera a que el suscriptor esté conectado antes de emitir. La figura puede marcar el
orden, pero **no puede sugerir que el orden es la garantía**.

**Composición:** los tres servicios alineados y equiespaciados; las flechas del orquestador bajan
**ortogonales**, no en curva, y **no se cruzan entre sí**. Si el cruce es inevitable por la posición
de la interfaz de inspección, movela a la derecha y bajá sus flechas por fuera.

**Leyenda:** «flujo de datos» continua negra, «arranque de servicio» continua en acento primario,
«lectura y consolidación» fina gris.

**Lo que va afuera, como nota en el documento y no en la imagen:** que los tres módulos se ejecutan
como servicios independientes gobernados por configuración y pueden disponerse en un mismo host o en
hosts distintos sin cambiar su lógica; y que la ausencia de una flecha del bus a la interfaz de
inspección es una frontera de diseño, no una omisión del dibujo.

---

### 5.6 Figura 4.6 — Fotograma con alerta confirmada

**Va en** 17.5.4. **No se redibuja**: es un fotograma real de una corrida, y su valor está
justamente en que no es una ilustración. Lo que se normaliza es el tratamiento.

- **Recortar la banda de cabecera** del renderizador. La versión sin recortar queda como respaldo,
  no va al informe.
- **Sin rótulo horneado** del video ni línea de procedencia impresa: eso va en la nota del
  documento.
- Si se le superponen anotaciones, van en el mismo sistema: acento primario, misma tipografía, mismo
  cuerpo relativo.
- La línea de tiempo al pie del fotograma se conserva, marcando la primera evidencia y el instante
  de la alerta.

**Lo que la nota del documento tiene que decir**, porque sin eso la imagen se malinterpreta: el
estado del motor en el instante mostrado, el instante de la alerta, y que **el casco que aparece
detectado no está sobre el sujeto**, de modo que no suprime la condición: la condición es sobre la
persona, no sobre la escena.

---

## 6. Lista de verificación antes de dar una figura por buena

Marcá las doce. Si una falla, la figura vuelve.

1. ¿El ancho de diseño es 16 cm y el texto se lee sin ampliar?
2. ¿No hay título ni nota de procedencia impresos dentro de la imagen?
3. ¿Todos los rótulos coinciden **literalmente** con los de esta guía?
4. ¿Los valores del contrato están en monoespaciada y el resto en la sans?
5. ¿Una sola familia tipográfica?
6. ¿La paleta es la de la sección 2.1, sin colores agregados?
7. ¿Cada tipo de flecha tiene además un patrón de trazo distinto y hay leyenda?
8. ¿Sobrevive en escala de grises?
9. ¿No hay flechas curvas que se crucen?
10. ¿Los nodos del mismo nivel comparten tamaño y están alineados a una grilla?
11. ¿Se entregó SVG **y** PNG a 300 dpi?
12. ¿Nada de lo dibujado contradice el texto de su sección, y las contradicciones encontradas
    quedaron reportadas en vez de resueltas por cuenta propia?

---

## 7. Anti-patrones observados, que no hay que repetir

- **Nota de procedencia dentro del PNG.** Expandió el lienzo a más del doble del ancho de la figura;
  al insertar a 16 cm, los ejes quedaron ilegibles.
- **Curvas cruzadas en el centro del dibujo.** Cuatro trazos que se cruzan en el mismo punto hacen
  imposible seguir cualquiera de ellos.
- **Dos lenguajes visuales en el mismo capítulo.** Cuatro figuras con iconos y azul marino, y la
  quinta con otra paleta y otra tipografía.
- **Una figura que dibuja una transición que el sistema no hace.** Es el peor de todos, porque el
  lector confía en el dibujo más que en el párrafo.
- **Grilla o ejes punteados.** En figuras con ejes, la grilla va en línea fina continua, del color
  de la sección 2.1, y nunca compite con los datos.
- **Número impreso sobre cada punto de una serie.** Se etiqueta el extremo, no todos.
- **Doble eje vertical.** No se usa en ninguna figura del informe.
