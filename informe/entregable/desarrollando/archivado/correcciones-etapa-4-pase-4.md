# Correcciones — pase 4 sobre §17.4 Implementación (v1.6 → v1.7)

> **Estatuto.** Acta del pase de consolidación de la Etapa 4, aplicado el 2026-09-04 sobre
> `desarrollando/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.6.docx` y entregado como
> `…_v1.7 (sugerencias sin aceptar).docx`, con control de cambios y autoría propia.
>
> **Origen:** diagnóstico [`analisis-17-4-17-5-etapas-4-5.md`](analisis-17-4-17-5-etapas-4-5.md),
> con las quince decisiones D-A…D-O firmadas por el usuario el 2026-09-04. Aplicador
> `herramientas/aplicar_v17_17_4.py`, compuerta `herramientas/verificar_pase_17_4_17_5.py`
> (**verde, 0 fallas**). El aplicador parte siempre de la v1.6, así que volver a correrlo
> reproduce la entrega byte a byte.
>
> ⚠ **La numeración de subsecciones cambió.** Toda unidad `E4-01…E4-31`, las fichas `AJ-4.x` de
> `ajustes/04` y la extracción `90b` citan números que ya no existen: se leen con
> [`mapa-secciones-17-4-v1-7.md`](mapa-secciones-17-4-v1-7.md).

---

## 0. Resultado, medido con el mismo instrumento antes y después

| Marcador | v1.6 | v1.7 |
|---|---:|---:|
| Prosa | 5.088 w | **4.642 w** |
| Tablas | 1.287 w | **851 w** |
| Prosa y tablas | 6.375 w | **5.493 w (−13,8 %)** |
| Títulos | 16 | **9** |
| Títulos de nivel 4 | 4 | **0** |
| Tablas | 6 | **5**, renumeradas 56–60 |
| Dos puntos en prosa | 55 | **1** |
| Punto y coma en prosa | 29 | **0** |
| Rayas | 28 | **0** |
| Párrafos de más de 150 palabras | 9 | **0** |
| Oraciones de más de 45 palabras | 27 | **0** |
| Palabras por oración | 26,5 | **21,6** |

La poda es mayor que el saldo, porque el pase **suma** unas 230 palabras de contenido que
faltaba (H2-01, H2-02 y E4-31) y convierte una tabla de 472 palabras en prosa.

---

## A. Estructura — D-A, Opción A

Once secciones de nivel 3 pasan a ocho, sin títulos de nivel 4. Tres fusiones y cuatro títulos
que desaparecen. El detalle de la traducción está en el mapa de secciones.

### E4-32 · Entrada del capítulo — dos párrafos a uno
Los párrafos de propósito y de frontera con §17.5 decían lo mismo con distinto foco. Quedan en un
párrafo de 68 palabras, sin «La presente sección». La regla de frontera se enuncia **una vez**, y
las ocho remisiones a §17.5 repartidas por el capítulo dejan de re-justificarla.

### E4-35 · §17.4.2 + §17.4.3 → **17.4.2 Correspondencia y contratos materializados**
El título de la vieja §17.4.3 desaparece. La correspondencia y los cinco contratos que la
materializan son el mismo movimiento argumental, y separarlos obligaba a repetir la introducción.
El comentario 0 del usuario, sobre los objetos de transferencia, se re-ancla al párrafo que
presenta los cinco contratos.

### E4-41 · §17.4.4 + §17.4.5 → **17.4.3 Servicios, gobierno por configuración y acople**
El título de la vieja §17.4.5 desaparece. Los dos caminos experimentales son la contraparte de los
servicios que los ejecutan, y su sección propia repetía lo que §17.3.3 y §17.3.10.1 ya fijan.

### E4-48 · §17.4.8 → **17.4.6**, sin títulos de nivel 4 (D-B)
Los cuatro títulos de nivel 4 encabezaban un párrafo cada uno. Pasan a entradillas en negrita
—adquisición, segmentación, preanotación y revisión, derivación y congelamiento— y los párrafos
de 207, 314, 168 y 158 palabras se parten en siete. El contenido verificado para E4-19 no cambia.

### E4-50 · §17.4.9 + §17.4.10 → **17.4.7 Verificación, alcance efectivo y brechas**
El título de la vieja §17.4.10 desaparece. Verificar y declarar el alcance efectivo son el mismo
cierre, y la verificación ocupaba 149 palabras más una tabla.

---

## B. Los tres handoffs que este pase aterriza

### E4-42 · **H2-01 — el orden de arranque real, y una sola vez**
🔴 El defecto más grave del capítulo. La v1.6 afirmaba tres cosas distintas e incompatibles:

| Dónde | Qué decía | Estado |
|---|---|---|
| §17.4.4 párr. 4 | «primero la distribución, después el control, por último el plano de medios» | **falso** |
| §17.4.5 párr. 3 | «primero se inicia el plano de control… después el plano de medios», citando la **sección 17.3.8.4, que ya no existe** | incompleto y con remisión rota |
| Nota de la Figura 4.7 | «el orden live inicia el control, confirma la suscripción y recién entonces habilita los medios» | incompleto |

El orden real, verificado contra el orquestador, es **control → distribución → medios**. El control
va primero porque debe quedar suscripto al canal de detecciones antes de que los medios publiquen,
y la distribución va segunda porque su corrida se declara contra la corrida de control ya creada.
**La no pérdida en el canal de alertas no depende del orden sino del publicador**, que espera a que
haya un suscriptor antes de emitir. El pase lo enuncia una sola vez, en 17.4.3, y §17.3.6.3 —que
remite a §17.4 para el orden efectivo— queda correctamente servida.

### E4-43 · La remisión rota desaparece
El párrafo que citaba §17.3.8.4 se elimina entero, porque su otra mitad (el número de secuencia y
los huecos) ya está en el párrafo del envoltorio del bus.

### E4-47 · **E4-31 — el detalle operativo del ledger aterriza**
§17.3 v1.6 dice que «el detalle operativo del ledger, incluida la unidad de conteo del tramo, se
documenta en la sección 17.4», y §17.4 v1.6 no lo decía. Entra en 17.4.5 un párrafo con las tres
piezas que salieron del diseño: la unidad de conteo del tramo es **la notificación y no la fila**,
una notificación no entregada deja **una fila por intento más la del descarte definitivo**, y al
reutilizar un directorio de salida **la generación anterior se archiva íntegra** y la deduplicación
considera todas las generaciones.

### E4-53 · **H2-02 — las 2.946 imágenes de ajuste y su causa**
§17.1 fija un rango orientativo de 500 a 2.000 imágenes y exige justificar cualquier desviación.
§17.5 ya reportaba las 2.946 sin decir que exceden el rango ni por qué, de modo que el protocolo
parecía violado. No lo fue: **la desviación es consecuencia de cumplir la regla de partición**. Se
tomó el total de los linajes elegibles tras excluir íntegramente la fuente que el banco comparte y
deduplicar de forma perceptual contra él, sin submuestrear al techo del rango. El párrafo declara
además los controles de solapamiento en cero y la semilla registrada. La causa es de
implementación y por eso vive acá; §17.5 no se toca.

---

## C. Consolidación contra §17.1 y §17.3

### E4-33 · §17.4.1 deja de describir los servicios
«Gobernado por configuración», «carga el modelo una vez» y «una corrida por vez» aparecían en
17.4.1, en la nota de la figura, tres veces en 17.4.4, una en 17.4.6 y una en la Tabla 59. Quedan
**una sola vez**, en la entrada de 17.4.3. La sección de componentes dice qué hace cada uno.

### E4-34 · La nota de la figura
Repetía en 112 palabras lo que la Tabla 57 declara fila por fila, y cerraba con el orden de
arranque incompleto. Queda en 82 palabras, con los dos patrones de acople, los puertos de los dos
buses —que la tabla no trae— y sin ninguna afirmación sobre el orden.

### E4-36 · «contratos preliminares» → «contratos mínimos»
§17.3.8.1 los llama contratos mínimos y versionados desde el pase 2 (D-P2-5). La expresión
«preliminares» sobrevivía en la entrada de la correspondencia y contradecía a su propia tabla.

### E4-37 · Los nombres de clase salen de la prosa (D-P2-6)
`DetectionEvent`, `PatternStateChanged` y `AlertEvent` funcionaban como aposiciones en prosa. La
regla vigente es que un identificador se declara una vez, en la tabla de correspondencia, y la
prosa habla en castellano. Además el primero **contradecía a la Tabla 56**, que declara el contrato
como evento de percepción. Los tres desaparecen del cuerpo y siguen en la tabla.

### E4-45 · §17.4.6 → **17.4.4**, sin lo que §17.3 ya fija
El párrafo del cooldown (72 w) queda en una oración con su decisión de diseño, porque §17.3.7 lo
desarrolla en dos párrafos. El de evidencia positiva (38 w) queda en la lista del vocabulario
activo, que es el dato concreto, porque el mecanismo de inferencia de la ausencia es §17.3.4.3.
Los párrafos 4 y 5 decían dos veces que hay un servicio por perfil y se funden. **Los valores
efectivos del núcleo y los literales del perfil operativo no se tocan**: son exactamente lo que
§17.3 remite a este capítulo.

### E4-46 · §17.4.7 → **17.4.5**, con los comentarios 2 y 3
El párrafo que repetía en prosa las dos primeras filas de la Tabla 58 se elimina, y con él se
resuelve el comentario 2 («falta el módulo de distribución»): la tabla ya trae las cuatro filas.
La oración de la modularidad se elimina por el comentario 3. Los estados de aplicabilidad quedan en
una cláusula, porque §17.3.9 y §17.1.7.6 los fundamentan.

### E4-40 · D-D · La evolución aditiva migra a extensibilidad
El campo de identidad entre fotogramas, sus tres mecanismos y el catálogo de campos previstos se
contaban en la sección de contratos (250 w más un bloque de código), en la Tabla 60 y otra vez en
extensibilidad. Quedan **sólo en 17.4.8**, en dos párrafos, y la sección de contratos deja una
oración con la remisión. El bloque de código cae, porque los campos ya se ven en el ejemplo del
evento persistido.

### E4-51 · D-E · La cifra de pruebas se fecha, no se actualiza
«2.203 pruebas aprobadas, sin fallos, en cinco suites» es la foto de una verificación integral que
ya no describe el estado del repositorio. Actualizarla sería peor, porque los conteos disponibles
hoy son de pruebas **recolectadas** y no ejecutadas en verde. La celda ahora dice que el conteo
corresponde a esa verificación.

---

## D. Los seis comentarios del usuario, y dónde quedaron

Ninguno se marca resuelto (D-M). Los seis cuyo párrafo desaparece se re-anclan al texto que los
absorbe, con su rango intacto.

| # | Texto | Ancla en la v1.6 | Ancla en la v1.7 | Cómo lo atiende el pase |
|---|---|---|---|---|
| 0 | «agregar los DTO fue algo que nos marco mariano» | título §17.4.3 | párrafo que presenta los cinco contratos (17.4.2) | La sección sobrevive entera como segundo movimiento de 17.4.2, con su ejemplo de evento persistido |
| 1 | «referenciar a la seccion donde se hablo de la pc como recurso» | «co-ubicados en un único host con GPU» | mismo párrafo, reescrito | Remisión explícita a **§17.1.4.1**, que define el nodo central de procesamiento y su equipo |
| 2 | «falta el modulo de distribucion» | párrafo que repetía la Tabla 58 | párrafo nuevo del ledger (17.4.5) | El párrafo se elimina, y el módulo gana el detalle operativo que le faltaba (E4-31) |
| 3 | «este dato es como que esta de mas» | oración de la modularidad | mismo párrafo, sin esa oración | La oración se elimina |
| 4 | «agregar hs de anotacion» | título §17.4.8.2 | bloque de preanotación y revisión (17.4.6) | **El dato no existe en ninguna fuente del repositorio** (D-G). El pase afirma el esfuerzo por lo que la revisión hizo, sin inventar una cifra. Si el usuario la aporta, entra acá |
| 5 | «da como a entender que no fue una actividad de mucho esfuerzo» | cierre del bloque de CVAT | párrafo nuevo de la revisión humana | La oración defensiva se reemplaza por lo que la pasada humana efectivamente hizo, con sus denominadores |
| 6 | «pasar a desarrollo esta tabla, es mucho texto asi en las columnas» | título de la Tabla 60 | primer párrafo de la prosa que la reemplaza | E4-52 |

---

## E. E4-52 · D-C · La Tabla 60 pasa a prosa por estatuto

La tabla tenía 472 palabras en ocho filas, con **cuatro celdas de 40 a 70 palabras**. Se reemplaza
por cinco párrafos ordenados por estatuto, que es lo que su propia nota prometía y la forma de
tabla impedía leer:

1. **Ejercido y medido** — identidad por sujeto, las tres estrategias, distribución por MQTT y
   paridad entre caminos, con los valores remitidos a §17.5.
2. **Implementado y caracterizado fuera del régimen evaluativo** — la preselección en el borde, con
   la causa de su exclusión y la cifra remitida a §17.5.7.
3. **Especificado y no implementado** — las condiciones de Nivel 2 y Nivel 3.
4. **Rama comparativa de ajuste fino** — lo que la implementación ejerció, sin las cifras de la
   curva, que son de §17.5.6.
5. **La desviación del rango de entrenamiento** — E4-53.

El reparto con §17.5 sigue las restricciones 3 y 4 del pase 3: el 87 % de la preselección y las
cifras de la curva de ajuste fino **se citan con denominador en §17.5**, y §17.4 declara el
estatuto.

---

## F. Estilo y notación

### E4-55 · Celdas
- Tabla 57: «modo replay o live» → «modo diferido o en vivo» · «Runner y webconsole» →
  «Orquestador y consola» · dos celdas pierden su punto y coma.
- Tabla 59: tres celdas pierden su punto y coma, y «una corrida live puede reevaluarse offline» →
  «una corrida en vivo puede reevaluarse por el camino diferido».
- Tabla 61 (hoy 60): dos celdas pierden sus dos puntos y su punto y coma.

### E4-56 · Renumeración
- **Tablas:** 56, 57, 58 y 59 conservan su número; la 60 pasa a prosa; la **61 se vuelve 60**.
  Cada una se cita ahora exactamente una vez en prosa; en la v1.6, cuatro no se citaban.
- **Figura:** 4.7 → **4.5**, contigua con las cuatro de §17.3 v1.6, y **citada en prosa**, que en la
  v1.6 no lo estaba.

### Puntuación y voz
Los 55 dos puntos de prosa quedan en 1 —la nota de la tabla de extensión, donde introduce una
disyuntiva— y los 29 punto y coma en 0. Las 28 rayas desaparecen. Los anglicismos que §17.3 ya
había normalizado (`open-vocabulary`, `live`, `offline`, `replay`, `runner`, `webconsole`,
`backend`, `endpoint`) salen del capítulo.

---

## G. Lo que NO se tocó

- **Las Tablas 56, 57 y 58** conservan todas sus filas. La 59 sólo acorta cinco celdas.
- **Los dos bloques que el usuario pidió** (el evento persistido y el árbol del repositorio de
  corrida) se conservan íntegros.
- **Los valores efectivos del núcleo** —4.000/2.000 y 7.000/3.000 ms, 0,35, 400 px², 0,25, las dos
  franjas con sus márgenes— y **los literales del perfil operativo** —560 px, caja 0,30, texto
  0,25, confianza 0,25, IoU 0,50, área 100 px², paso 1, cola 8—.
- **El fundamento del recorte ex ante de los clips**, verificado para E4-19.
- **El marcador `[[PENDIENTE]]`** de procedencia del lote, que depende de C1.
- **La imagen embebida de la figura**, que el usuario reemplaza por la producida (D-F). La nota ya
  describe el orden correcto, de modo que al pegarla todo coincide.

---

## H. E4-57 · El efecto colateral sobre §17.3, cerrado

§17.3 v1.6 cita **«la sección 17.4.6»** para los valores efectivos del núcleo, y tras la
renumeración esa sección es **17.4.4**.

El cambio se entregó primero como control de cambios y, **por indicación del usuario, se aplicó en
limpio** sobre el documento que él mismo había pasado sin marcas. El resultado es
`…_17.3_…_v1.7.docx`, sin cambios controlados y sin necesidad de otra ronda de aceptación.
Verificado contra la v1.6: **el texto tiene la misma longitud y es idéntico salvo el token**, cero
inserciones y cero borrados, los cuatro comentarios en su lugar, los 21 `sectPr` y las 4 figuras
intactos, y el mismo inventario de archivos en el paquete. `verificar_entregable.py` sin problemas
duros, y `90-etapa3-texto-extraido.md` re-extraído de la v1.7 (regla D-C). La v1.6 y la entrega con
sugerencias quedaron en `archivado/`.

---

## I. Verificación

`herramientas/verificar_pase_17_4_17_5.py` — **verde, 0 fallas**. Comprueba, sobre la vista
aceptada y la rechazada:

1. **Rechazar todos los cambios devuelve exactamente la v1.6.** Es la propiedad que hace segura la
   entrega.
2. Nueve títulos y cero de nivel 4 o más.
3. Dos puntos y punto y coma de prosa dentro del objetivo, cero párrafos de más de 150 palabras y
   cero oraciones de más de 45.
4. Greps prohibidos en cero: la remisión a 17.3.8.4, el orden falso, el metadiscurso, los
   anglicismos, «contratos preliminares» y la numeración anterior a la fusión.
5. Greps exigidos presentes: el orden real, la garantía del publicador, el ledger, las 2.946
   imágenes, la remisión a §17.1.4.1 y la figura renumerada.
6. Cada tabla con un rótulo y una cita.
7. Los siete comentarios, la figura y el `sectPr` del cuerpo sobreviven, y la entrega trae cambios
   controlados.

---

## J. Lo que queda

**Del usuario:**
1. Aceptar los cambios de `…_17.4_…_v1.7 (sugerencias sin aceptar).docx` y guardar como
   `…_v1.7.docx`, y lo mismo con `…_17.3_…_v1.7`.
2. **Reemplazar la imagen de la Figura 4.5** por `informe/figuras/fig-a-vista-de-procesos.png`,
   a 16 cm de ancho y sin reescalar.
3. Decidir si aporta las horas de anotación (comentario 4).
4. Cerrar los comentarios cuando quiera.
5. Git.

**Al aceptar:** re-extraer `90b-etapa4-texto-extraido.md` (regla D-C) y regenerar el kit.

**Para la integración:** la numeración global de tablas queda con el hueco 53–55 que dejó §17.3 y
con §17.4 cerrando en la 60; la figura de este capítulo es la 4.5 en el esquema del capítulo y la
numeración global la fija la integración.
