# Etapa 6 · v1.2 — lectura de los 14 hilos de comentarios (2026-09-12)

> ✎ **2026-09-12, más tarde — EJECUTADO.** El usuario respondió las siete preguntas y el pase
> `herramientas/pase_etapa6_v13.py` produjo la **v1.3 (sugerencias sin aceptar)**; acta:
> `pase-etapa-6-v1.3-2026-09-12.md`. Este análisis queda como constancia de la lectura.
>
> **Qué es esto.** Lectura uno por uno de los comentarios que trae
> `E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.2.docx`, con lo que entiendo de cada uno,
> los hechos verificados contra las secciones cerradas y los índices de resultados, la
> corrección que propongo y —donde hace falta— la pregunta que necesito responder antes de
> escribir la v1.3. **No se tocó el documento.**
>
> Guía de contraste: `E-OVRT-VDP_Secciones_Iniciales_hasta_14_v1.1 (sugerencias aceptadas).docx`
> (hipótesis §12.3, objetivos §13, etapas §14).

---

## 0. Estado del documento recibido

| Dato | Valor |
|---|---|
| Identidad (`sha256` de `word/document.xml`) | `45157574c1b1…386a` |
| `Copia de …_v1.1.docx` (misma carpeta, misma hora) | **byte a byte idéntica a la v1.2** — es el mismo archivo bajado dos veces |
| Sugerencias pendientes (`w:ins`/`w:del`) | **0** — todas las de la v1.1 quedaron aceptadas |
| Comentarios | **15 (14 hilos)**, todos de Simon, todos del 12-09; ninguno de los 13 míos de la v1.1 sobrevivió (resueltos en Google Docs, esperado) |
| Diferencias contra la vista aceptada de la v1.1 | **3**: (1) se quitó la sección Referencias (a propósito, 300 líneas); (2) «Canal @HospitalConstruction» → «Canal YouTube @HospitalConstruction» (bien); (3) §18.5 «Estos veredictos … **No implican**» → «**No implica**» — esta es una regresión gramatical (sujeto plural); la repongo en la v1.3 |
| Defectos del viaje por Google Docs | ninguno: no hay bloques de código, 19 títulos `Heading1–3` intactos, 18 tablas |

---

## 1. Mapa de los 14 hilos

| # | Dónde | Comentario (resumen) | Lo entiendo | Necesita decisión tuya |
|---|---|---|---|---|
| H01 | 17.6.1 | ¿citar los repos? son públicos | ✅ | **sí** (una: paraguas solo, o los cinco) |
| H02 | 17.6.3 ¶3 | «no entiendo esto, ¿qué suma?» | ✅ | **sí** (reescribir concreto o borrar) |
| H03 | 17.6.3 ¶4 | «tampoco, ¿qué suma?» | ✅ | idem H02 (van juntos) |
| H04 | 17.6.4 | decir que está todo dockerizado; verificación antes de la presentación final | ✅ | no (propuesta cerrada) |
| H05 | 17.6.4 + respuesta | resolver las referencias a archivos/configs/datos de forma sencilla; videos e imágenes a un Drive autorizado | ✅ | **sí** (la forma del punto de entrada único) |
| H06 | 18.1 ¶1 | la hipótesis hablaba de «persona sin casco / sin chaleco»: referenciarlo | ✅ | no |
| H07 | 18.1 ¶2 | ¿por qué F1 y no AP? | ✅ | menor (si además citamos el mAP50) |
| H08 | 18.2 | ¿qué es `machinery`? | ✅ | no |
| H09 | 18.3 ¶5 | «acá me perdí» (17 clips, F1 0,031) | ✅ | no |
| H10 | 18.4 ¶1 | no queda claro lo del presupuesto excedido | ✅ | no |
| H11 | 18.4 ¶3 | ¿30 FPS en tiempo real? | ✅ | no |
| H12 | 18.5 entero | «difícil de entender» | ✅ | **sí** (cómo nombrar los tres tramos) |
| H13 | 18.6 ¶4 | plantear caminos de continuidad para quien siga; «dejamos las bases listas» | ✅ | **sí** (confirmar la lista de caminos) |
| H14 | Anexo E entero | apunta a archivos de los repos con identificadores que pierden al lector | ✅ | **sí** (junto con H05: qué queda de la Tabla E.2) |

No hay ningún comentario que no entienda. Hay **cinco decisiones** (H01, H02/H03, H05/H14,
H12, H13) donde dos lecturas razonables dan textos distintos; el resto lo resuelvo con la
propuesta que va abajo.

---

## 2. Hilo por hilo

### H01 · 17.6.1 — «¿hace falta citar los repositorios acá? son repositorios públicos en GitHub»

**Lo que entiendo.** Querés que el informe diga dónde está el código, con la URL, ahora que
todo es público.

**Hechos verificados hoy (`gh repo view`).** Los **siete** repos son `PUBLIC`: los cinco de
código, `e-ovrt_docs` y el paraguas `e-ovrt-vdp`. El informe, en ninguna de sus secciones
cerradas ni en esta, cita todavía ninguna URL propia. El paraguas
`https://github.com/simonll4/e-ovrt-vdp` ya tiene la tabla de los cinco repos con qué es
cada uno, los índices de resultados enlazados, las figuras y `CITATION.cff`: fue diseñado
justamente para ser **la única referencia externa que cita el informe**.

**Propuesta.** Sí, citar, y citar **una sola vez y una sola cosa**: el paraguas, al final del
primer párrafo de 17.6.1 («El conjunto se publica en un repositorio de documentación que
reúne los cinco repositorios de código, los resultados con sus artefactos y las figuras
(Carrizo, Guillaumet y Llamosas, 2026)»), con su entrada en la lista de referencias. Los
cinco repos de código no se citan uno por uno: el paraguas los lista y así el informe no
carga cinco URLs que pueden cambiar de rama o de dueño.

**Pregunta 1.** ¿Paraguas solo (mi recomendación) o también las cinco URLs de código en el
texto?

**⚠ Bloqueo fuera del documento (tuyo).** La rama por defecto de
`e-ovrt_experimental-setup` en GitHub es `control-plane-configs` (último commit 2026-07-01)
y **no tiene `results/`**: todos los enlaces del paraguas a cifras (`blob/HEAD/results/…`)
dan 404 hoy. Si el informe apunta al paraguas, esa rama por defecto tiene que cambiar (o
mergear) antes de la entrega.

---

### H02 + H03 · 17.6.3 ¶3 y ¶4 — «no entiendo esto, ¿qué suma al informe?»

**Lo que entiendo.** Los dos párrafos están escritos en abstracto («la primera contrastó
las cifras declaradas con los artefactos… la segunda verificó la organización del material
de video…», «las verificaciones de relectura respaldaron el determinismo…») y no se ve qué
afirman.

**Por qué están.** El kit de la etapa pide nombrar «los dos verificadores mecánicos y qué
cubre cada uno» y la reproducción del banco. Como el informe no puede nombrar scripts ni
rutas, el redactor los describió en genérico y quedó ilegible.

**Lo que dicen, en concreto.** (1) Hay un verificador que **recalcula las cifras de los
índices de resultados a partir de los artefactos de cada corrida** y falla si una cifra
declarada no coincide: hoy 26 cifras sobre 17 campañas, cero rotas. (2) Hay otro que revisa
la **organización del material de video** (estratos, exclusiones, correspondencia de
anotaciones, huellas de los archivos congelados). (3) El banco de imágenes se **reconstruye
desde las fuentes y da el mismo archivo byte a byte**. (4) Releer los mismos eventos con la
misma configuración da los mismos resultados (determinismo del motor). Lo que **no**
cubren: repetir la inferencia en otra máquina.

**Propuesta (recomendada).** Fundir ¶3 y ¶4 en **un** párrafo de ~90 palabras que diga eso
tal cual, con la cifra «26 cifras sobre 17 campañas» como única cifra:

> Además de las pruebas de los módulos, dos comprobaciones automáticas cuidan el material
> experimental. La primera recalcula las cifras reportadas a partir de los artefactos de
> cada corrida y falla si alguna no coincide; al cierre cubría 26 cifras sobre 17
> campañas. La segunda revisa la organización del material de video: estratos,
> exclusiones, correspondencia de las anotaciones e integridad de los archivos congelados.
> Se comprobó, además, que el banco de imágenes se reconstruye desde sus fuentes y produce
> el mismo archivo byte a byte, y que releer los mismos eventos con la misma configuración
> produce las mismas alertas. Ninguna de estas comprobaciones sustituye repetir la
> inferencia en otro equipo.

**Pregunta 2.** ¿Reescribir así (recomendado: es la evidencia de que las cifras del informe
son verificables, y al tribunal le sirve) o borrar los dos párrafos?

---

### H04 · 17.6.4 — «cambiar esto: tenemos que decir que ya está todo listo y dockerizado; queda pendiente y lo trataremos después de la primera entrega; antes de la presentación final lo resolvemos»

**Lo que entiendo.** El texto actual («el despliegue no fue verificado… no se presenta
como evidencia de portabilidad») suena a que no se va a hacer. Querés que diga que el
empaquetado está hecho y que la verificación es un pendiente con fecha.

**Hechos verificados hoy.** `docker compose config` valida los **13 servicios** (consola,
control, distribución, `mosquitto` y nueve variantes del plano de medios); los tres
Dockerfiles existen en sus repos; **ninguna imagen está construida** y el smoke integral no
corrió. O sea: definido y validado por configuración, sí; construido y arrancado, no.

**Propuesta (sin pregunta).** Reescribir el párrafo en positivo y con el compromiso
explícito, sin afirmar un arranque que no ocurrió:

> La plataforma quedó empaquetada en contenedores: cada servicio cuenta con su
> especificación de construcción y una única composición levanta los trece servicios
> —consola, control, distribución, el broker MQTT y las variantes del plano de medios— con
> la misma disposición de rutas del entorno experimental. La composición fue validada. La
> construcción de las imágenes y la prueba integral de arranque quedaron previstas para
> antes de la presentación final del trabajo; hasta entonces, el empaquetado se reporta
> como estado de entrega y no como portabilidad verificada. Su documentación operativa
> acompaña al software.

Arrastra dos frases espejo que hay que alinear: §18.6 ¶5 («…comprobar una portabilidad que
esta entrega no verificó») y el último párrafo del Anexo E («el empaquetado definido no
acredita un despliegue ejecutado»). Las paso a «comprobación integral prevista antes de la
presentación».

---

### H05 · 17.6.4 (+ respuesta) — «resolver las referencias a archivos, configs, sets de datos que están en los repos o guardamos en disco (videos e imágenes van a un Drive con acceso autorizado) … de manera sencilla»

**Lo que entiendo.** Hoy el informe nombra artefactos (`bench_v3.json`, `clip_gt.v2`,
`build_bench_v3.py`, `eovrt-control replay --config`, huellas abreviadas) sin decir dónde
están ni cómo llegar, y el lector no puede seguirlos. Querés **un** mecanismo simple, no
uno por artefacto.

**Propuesta: un solo punto de entrada.**

1. **El informe cita una sola cosa externa: el repositorio público paraguas** (H01). Todo
   lo que es código, configuración, manifiestos, anotaciones derivadas, índices de
   resultados con sus artefactos y figuras se alcanza desde ahí (ya está armado así).
2. **El material audiovisual** (los 34 clips del rodaje, los recortes del lote de
   internet, las imágenes originales de los datasets que no se redistribuyen) va a la
   **carpeta de Drive con acceso autorizado**, y **el enlace a esa carpeta vive en el
   paraguas** (una sección «Material audiovisual: acceso autorizado» en su README y en
   `evidencia/material-de-video.md`, que hoy ya dice «no se publica ningún video»). El
   informe no pone la URL del Drive: dice que «el material audiovisual se conserva con
   acceso autorizado y se solicita a los autores a través del repositorio de
   documentación». Una URL de Drive en una tesis impresa envejece; la del repo no.
3. **En el texto del informe dejan de aparecer nombres de archivo y comandos** (que además
   violan la autocontención): «la herramienta de construcción del banco» en vez de
   `build_bench_v3.py`, «la evaluación de una corrida contra el banco» en vez de
   `python -m … --run --bench-coco`, etc. Se conservan sólo los nombres que el informe
   define para sí (`bench_v3`, `cr01_cr02_v2_short`, CR-01/CR-02, `media.detection.v1`).
4. **Las huellas SHA-256** quedan reducidas a las dos que un tercero puede verificar de
   punta a punta (ver H14).

Esto toca 17.6.1 (una oración), 17.6.4 (una oración), Anexo E (el grueso) y Anexo F (una
oración sobre el acceso al material).

**Pregunta 3.** ¿De acuerdo con que el Drive se enlace **desde el repo** y no desde el
informe? Y la carpeta: ¿la creás vos con la estructura sugerida en el plan de respaldo
(`01-evidencia/…`), o querés que te deje escrita la sección del README del paraguas para
cuando exista?

---

### H06 · 18.1 ¶1 — «como hipótesis se planteó resolver consultas como "persona sin casco" o "persona sin chaleco reflectivo" … deberíamos hacer referencia a eso, o a lo que se pudo concluir»

**Lo que entiendo.** El párrafo responde «afirmativa y condicionada» en abstracto; falta
cerrar el círculo con la formulación literal de §12.3.

**Hecho.** §12.3 dice: «una plataforma experimental podría recibir consultas o patrones
como "persona sin casco" o "persona sin chaleco reflectivo" y transformarlos en alertas
evaluables dentro de un flujo de video». Lo que se midió responde exactamente a eso, con
tres matices que son la conclusión: (a) las dos consultas se convirtieron en alertas
evaluables; (b) **no** funcionó formularlas literalmente como negación al detector: la
estrategia directa quedó descartada por precisión 0,146, y la que funciona reconstruye la
ausencia desde la evidencia positiva (persona detectada, sin casco detectado sobre ella);
(c) «sin casco» quedó sostenida en los dos niveles y «sin chaleco» sólo en el nivel de
alerta por episodio, con su clasificación por persona abierta (F1 0,479).

**Propuesta (sin pregunta).** Insertar, entre la oración de la hipótesis y la de la cadena
funcional:

> Las dos consultas que la hipótesis tomó como ejemplo, «persona sin casco» y «persona sin
> chaleco reflectivo», se transformaron en alertas evaluables sobre video, con dos
> precisiones que son parte de la respuesta: la condición no pudo formularse al detector
> como una negación literal —esa formulación quedó descartada por su precisión— sino como
> ausencia del elemento sobre una persona detectada; y la primera condición se sostuvo en
> los tres niveles de evidencia, mientras que la segunda alcanzó la alerta por episodio con
> su clasificación por persona todavía abierta.

---

### H07 · 18.1 ¶2 — «¿por qué hablamos de F1? en los papers y experimentos vi que siempre se muestra AP»

**Lo que entiendo.** Sospecha de que se eligió la métrica incorrecta o que quedó fuera la
que la literatura usa.

**Respuesta.** Las dos métricas están, cada una en su nivel, y no son intercambiables:

- **AP** mide un **detector sobre imágenes**: ordena las cajas por confianza y resume
  precisión y recall a lo largo de todos los umbrales. Es lo que reportan los papers
  porque evalúan detectores. En el informe está en el **nivel de percepción** (§17.5.2):
  mAP50 0,551 de `gdino-tiny-560` sobre el banco de 6.477 imágenes, con su desglose por
  estrato y por clase (`machinery` AP50 0,662, `vehicle` 0,026, etc.).
- **F1 de alertas** mide **decisiones binarias por episodio en video**: para cada episodio
  anotado, la plataforma emitió o no emitió una alerta dentro de la ventana; no hay
  ranking ni barrido de umbrales que promediar, así que AP no está definido. Lo que
  corresponde es precisión, recall y su F1 sobre episodios, que es lo que §17.1.7 fijó de
  antemano para el nivel de alerta. Y es el resultado principal porque la tesis no es «el
  detector detecta bien» sino «la plataforma alrededor del detector convierte eso en
  alertas»: 0,789 → 0,930 con **las mismas detecciones**, un efecto que el AP no puede
  ver porque las detecciones no cambiaron.

**Propuesta.** Agregar una oración al final del párrafo (o al comienzo del ¶4, que ya habla
de «los valores de AP publicados»):

> El AP, que la literatura reporta para comparar detectores sobre imágenes, se informa en
> el nivel de percepción de la sección 17.5.2; la alerta por episodio es una decisión
> binaria sobre una ventana temporal y se mide con precisión, recall y F1, que es la
> métrica que el protocolo fijó para ese nivel.

**Pregunta 4 (menor).** ¿Querés que §18.2 cite además el número del nivel de percepción
(mAP50 0,551 sobre 6.477 imágenes de tres fuentes, remitiendo a §17.5.2 para el desglose por
estrato)? Hoy dice «encabezó el mAP50» sin cifra.

---

### H08 · 18.2 — «¿qué es `machinery`? ¿una nueva clase que agregamos?»

**Sí.** Es el **piloto de extensibilidad**: para probar que se puede sumar una clase por
configuración sin entrenar, se agregó al vocabulario la palabra `machinery` (maquinaria),
ajena al núcleo CR-01/CR-02, y se la evaluó contra 99 cajas de referencia del material del
piloto (la copia de MOCS que lista el Anexo F). Dio AP50 0,662 sin ninguna corrida de
entrenamiento. La segunda parte del párrafo cuenta el límite: probaron también `vehicle`
y el modelo la resolvió sobre la misma maquinaria (0 detecciones acompañando a
`machinery`; aislada, 118 cajas con AP 0,026): la palabra no significaba lo que el equipo
quería que significara. Por eso «el costo de entrenamiento pudo evitarse, pero el costo de
validación permaneció».

**Propuesta (sin pregunta).** Reescribir las dos primeras oraciones:

> La extensibilidad sin entrenamiento sí fue ejercida: se añadió por configuración una
> clase ajena al núcleo, maquinaria de obra (prompt `machinery`), y sin ninguna corrida de
> entrenamiento alcanzó AP50 de 0,662 sobre 99 cajas de referencia del piloto de
> extensibilidad (sección 17.5.2).

---

### H09 · 18.3 ¶5 — «acá como que me perdí»

**Por qué se pierde.** El párrafo anterior habla de **episodios** (2 evaluables, 26 vs 323
falsos positivos) y este salta, sin avisar, a **otro nivel de evaluación** (estado por
persona, cuadro a cuadro, sin motor temporal) sobre **otro conjunto** (17 clips: los 13
del lote de internet más 4 de un piloto anterior), con jerga («evaluación intermedia»,
«conservar esa frontera», «condición anotable») que no se definió acá.

**Lo que dice, en claro.** Cuando se evaluó cuadro a cuadro si el detector acertaba el
estado de cada persona (¿tiene casco? ¿tiene chaleco?) sobre 17 clips de obra real, a
2 cuadros por segundo y sin el motor temporal, el F1 se derrumbó a 0,031 (CR-01) y 0,018
(CR-02) sobre más de diez mil cuadros con persona. La culpa fue de la precisión (< 0,02):
el detector emitía «sin casco» sobre personas cuyo estado **ni el anotador humano podía
determinar** (lejanas, de espaldas, ocluidas); el evaluador excluyó esos cuadros del
denominador y contó como falso positivo cualquier predicción sobre ellos. Conclusión: en
obra real, la brecha grande no es «formular la condición en lenguaje» sino que la escena
permita observarla.

**Propuesta (sin pregunta).** Reescribir:

> En el nivel de estado por persona, medido cuadro a cuadro y sin motor temporal sobre 17
> clips de obra real —los 13 del lote de internet y cuatro de un piloto anterior—, el F1
> cayó a 0,031 para CR-01 y 0,018 para CR-02, sobre más de diez mil cuadros con persona en
> cada condición (sección 17.5.3). La caída provino de la precisión, inferior a 0,02: el
> detector emitió la condición sobre personas cuyo estado el anotador humano no podía
> determinar, y cada una de esas predicciones contó como falso positivo. En obra real, la
> distancia mayor no está entre formular la condición en lenguaje y detectarla, sino entre
> detectarla y que la escena permita observarla.

---

### H10 · 18.4 ¶1 — «no deja bien en claro lo del presupuesto excedido»

**Por qué no queda claro.** Dice «excedieron el presupuesto de referencia» sin decir cuál
era el presupuesto ni por cuánto.

**Hechos.** §17.1.7.5 fija para el tramo previo a la acumulación temporal (desde que el
cuadro sale de la cola hasta el fin de la inferencia) una estimación de **hasta 250 ms por
unidad procesada**. Medido en vivo con `gdino-tiny-560` sobre la OAK-D: p95 entre 630 y
890 ms en tres corridas, es decir **entre 2,5 y 3,6 veces** el presupuesto. Dos contrastes
que dan sentido al número y hoy no están en el párrafo: la plataforma **sin** el detector
(inferencia simulada) cuesta 31,8 ms p95, o sea que el exceso es del modelo, no de la
cadena; y el modelo que sí entra en presupuesto (YOLOE, 225–249 ms) es el que no sirve
para la condición (recall de cabeza descubierta 0,000). Esa tensión calidad–latencia es un
hallazgo de primera línea y el §18.4 la deja implícita.

**Propuesta (sin pregunta).**

> El funcionamiento en vivo quedó demostrado, pero no dentro del presupuesto de latencia.
> La sección 17.1.7 había estimado hasta 250 ms por unidad procesada para el tramo entre
> la salida del cuadro de la cola y el fin de la inferencia; con gdino-tiny-560 sobre la
> OAK-D, el p95 de ese tramo se ubicó entre 630 y 890 ms en tres corridas, entre 2,5 y 3,6
> veces el presupuesto. El exceso es del detector y no de la cadena: la misma plataforma
> con inferencia simulada resolvió el tramo en 31,8 ms p95, y el único perfil que entró en
> presupuesto en vivo, YOLOE, fue el que no reconoce la condición. Ninguna de estas cifras
> mide desde el sensor: la captura hasta la cola se instrumentó por separado para OAK-D y
> no se midió para RTSP.

---

### H11 · 18.4 ¶3 — «¿es correcto a 30 fps en tiempo real?»

**Respuesta: no es tiempo real, y el texto lo insinúa mal.** Los 30 fps son la **cadencia
completa del material grabado**, evaluado en diferido: es el punto de partida de la
comparación. El camino en vivo entregó **entre 1,16 y 4,42 fps** (§17.5.5). Por eso los 34
clips se remuestrearon a 4,29 / 2 / 1,15 fps: para cubrir con el mismo material y las
mismas anotaciones la franja en la que efectivamente corre el vivo. La serie responde
«cuánto del resultado sobrevive cuando el sistema ve una fracción de los cuadros».

**Propuesta (sin pregunta).** Cambiar el arranque de la serie y una oración de contexto:

> El remuestreo regular permitió examinar el efecto de disponer de menos evidencia
> temporal sin cambiar las detecciones. El banco se evaluó en diferido a su cadencia
> completa de 30 fps, mientras que el camino en vivo entregó entre 1,16 y 4,42 fps; para
> cubrir esa franja, los 34 episodios se remuestrearon de manera pareada. El F1 por escena
> fue 0,789 a 30 fps, 0,794 a 4,29, 0,738 a 2 y 0,646 a 1,15 fps. […]

---

### H12 · 18.5 — «se me hizo como medio difícil de entender»

**Diagnóstico.** Seis párrafos con tres problemas: (1) arranca por la literatura en vez de
por qué se hizo; (2) los tres tramos se nombran con perífrasis largas («el ajuste de la
proyección de clases», «el de mayor capacidad», «el tercer tramo», «la variante tiny») que
obligan a recordar cuál es cuál —en la v1.1 sacamos las etiquetas T1/T2/T3 porque §17.4 y
§17.5 no las usan, pero la cura salió peor que la enfermedad—; (3) mezcla en cada párrafo
resultado, salvedad y diagnóstico.

**Propuesta: cuatro párrafos, en este orden.**

1. **Qué fue la rama** (3 oraciones): comparación separada del núcleo, sobre YOLOE-26s, con
   línea base y criterios de ganancia y retención fijados antes de medir; **una escalera de
   tres tramos, que acá se numeran para poder nombrarlos**: el **primer tramo** entrenó
   sólo la capa de proyección de clases, el **segundo** liberó más capacidad (10,35
   millones de parámetros), el **tercero** iba a aplicar lo aprendido a una variante
   ajustable de Grounding DINO.
2. **Qué pasó** (cifras mínimas): el primero no alcanzó la ganancia exigida y perdió
   retención de `person`; el segundo ganó en cabeza descubierta pero perdió retención en
   el dominio y **el 71,3 % de su capacidad de vocabulario abierto** (COCO: 0,4347 →
   0,1247), con un entrenamiento detenido en la época 16 de 60 cuyo mejor punto fue la
   primera; el tercero no se ejecutó porque la variante ajustable no preservaba el linaje
   del perfil desplegado y su checkpoint publicado reproducía una anomalía geométrica
   ajena al proyecto. **Ningún checkpoint se adoptó.**
3. **Qué significa**: con 2.946 imágenes de entrenamiento, subir la capacidad no resolvió
   nada, así que el límite es de **datos y retención, no de parámetros**; la literatura
   anticipaba el mecanismo (Kumar et al., 2022; Lee et al., 2023) pero no el resultado.
   No demuestra que toda adaptación falle: no se probaron métodos eficientes en parámetros
   ni un corpus independiente del banco.
4. **Cierre**: la rama no cambió la conclusión sobre el núcleo sin entrenamiento; dejó una
   decisión de no adopción auditable, no una promesa.

Esto baja de ~560 a ~380 palabras y saca la latencia no medida (ya está en 17.5.7).

**Pregunta 5.** ¿Va bien **numerar los tramos («primer/segundo/tercer tramo») definiéndolos
una vez** al inicio de 18.5? Es lo que hace legible el resto sin reintroducir T1/T2/T3.

---

### H13 · 18.6 ¶4 — «lo plantearía de otra forma: es probable que no continuemos nosotros, pero está bueno plantear qué caminos se pueden tomar para extender las capacidades y cubrir toda la tesis; a modo de cierre de que dejamos las bases listas»

**Lo que entiendo.** Hoy ¶4 y ¶5 son «continuidades justificadas» escritas como
condiciones que alguien debería cumplir antes de afirmar algo más. Querés que se lean
como **caminos abiertos para quien siga**, cada uno apoyado en algo que ya quedó
construido, y que cierre con la idea de que las bases están.

**Restricción que respeto.** El kit de la etapa dice que el trabajo futuro «sale de las
exclusiones ejercidas», sin prometer capacidades nuevas ni comprometer al equipo. Tu
planteo es compatible: los caminos son las exclusiones, contadas como puertas abiertas.

**Propuesta: fundir ¶4 y ¶5 en un párrafo de entrada + lista de seis caminos + una
oración de cierre.** Cada camino nombra **qué base queda lista** y **qué falta**:

| Camino | Base que queda lista | Qué falta |
|---|---|---|
| **Más condiciones de riesgo** (del catálogo de §17.1: zona restringida, proximidad a maquinaria…) | el motor de patrones y el vocabulario se extienden por configuración; la extensión de vocabulario se ejercitó con `machinery` | anotaciones y evaluadores para condiciones con relaciones espaciales |
| **Validación en obra real** | el protocolo de banco temporal, el evaluador y el control de negativos | horas de obra no guionada con anotación independiente y acceso resuelto; ~3 h anotadas para fijar una cota de falsas alarmas (L1) |
| **Evaluación del seguimiento** | el tracker está implementado y su aporte medido por su efecto en las alertas | anotaciones y métricas MOT (fue exclusión explícita) |
| **Adaptación del modelo** | el protocolo pre-registrado de ganancia y retención, y el resultado negativo | métodos eficientes en parámetros y un corpus que no comparta fuentes con el banco |
| **Distribución y consumo** | el servicio MQTT con idempotencia, medido | otros canales y la evaluación del consumo humano de las alertas |
| **Portabilidad** | el empaquetado de los trece servicios | la construcción de imágenes y el arranque integral, previstos antes de la presentación (H04) |

Cierre: «Ninguno de estos caminos exige rehacer lo construido: el código es público, los
bancos y sus referencias humanas están congelados e identificados, el protocolo distingue
lo pre-registrado de lo posterior y cada cifra remite a su artefacto. Quien continúe parte
de esas bases; este trabajo no compromete su ejecución.»

**Pregunta 6.** ¿Confirmás los seis caminos? ¿Va como lista (más legible; el §18 hoy no
tiene ninguna) o como prosa (más homogéneo con el resto)?

---

### H14 · Anexo E — «realmente es muy difícil entender a lo que se hace referencia: apuntamos a archivos de los repos, con identificadores que hacen perder al lector»

**De acuerdo, y es el mismo problema que H05 visto desde el anexo.** El Anexo E tiene tres
capas: la Tabla E.1 (qué se conserva y cómo se comprueba: **está bien y se queda**), la
Tabla E.2 (nueve huellas, siete abreviadas que —según su propia nota— «no sirven para una
verificación criptográfica»: **es la que pierde al lector**) y ocho párrafos de prosa que
mezclan comandos (`build_bench_v3.py`, `--run`, `--bench-coco`, `eovrt-control replay
--config`), reglas de lectura ya escritas en §17.5 y advertencias operativas.

**Propuesta.**

1. **Tabla E.1**: se queda tal cual, más una oración antes: «Todos los elementos de la
   tabla se alcanzan desde el repositorio de documentación del proyecto; el material
   audiovisual, con acceso autorizado, se solicita a los autores por esa misma vía.»
2. **Tabla E.2 → un párrafo con las dos huellas completas** que un tercero sí puede
   comprobar, ambas verificadas hoy contra disco: banco de imágenes
   `4557024ecc4ee497ab1fad01d6819206395c10fd794010ed8c1d9198b19a4462`; manifiesto del
   banco temporal de 47 clips
   `3f14f50a53c0d6c57b429378544dcfb6ed87fc942640db302c53ba1470001a75`. Las demás
   huellas (estratos, conjuntos de prompts, manifiesto histórico del rodaje) «acompañan a
   cada artefacto en el repositorio» y no se transcriben.
3. **La prosa** pasa de ocho párrafos a **cuatro pasos numerados, por material y sin
   comandos**: (a) banco de imágenes: reconstruir desde las fuentes → verificar la huella →
   evaluar las predicciones conservadas por estrato; (b) banco temporal: convertir y
   validar la anotación humana → comprobar episodios y exclusiones → releer los eventos
   conservados con la misma configuración → evaluar contra la referencia; (c) en vivo:
   preparar servicios, suscribir antes de publicar, orden control → distribución → medios,
   calentamiento fuera de la medición; (d) agregación: misma unidad estadística, mismas
   exclusiones, sin sumar percentiles entre tramos. Se conserva la advertencia del nivel de
   exportación de la anotación (tarea vs proyecto) porque es la trampa real, y la
   definición de G2A desde la salida de la cola.

Baja de ~840 a ~450 palabras y elimina todos los nombres de archivo.

**Pregunta 7.** ¿Tabla E.2 reducida a las dos huellas completas (recomendado) o eliminada
del todo?

---

## 3. Cambios de arrastre que haré junto con lo anterior

- Reponer «No implic**an**» en §18.5 (regresión de la bajada).
- Alinear las dos frases espejo del empaquetado (§18.6 ¶5 y Anexo E último párrafo) con H04.
- Alta en la lista de referencias del paraguas: «Carrizo, M. L., Guillaumet, G. A., y
  Llamosas, S. (2026). *E-OVRT-VDP: Plataforma experimental de detección open-vocabulary
  en video en tiempo real* [Repositorio de documentación]. GitHub.
  https://github.com/simonll4/e-ovrt-vdp» — la lista no está en esta v1.2 (la sacaste a
  propósito), así que la entrada va en el acta para la integración.
- Una oración en el Anexo F sobre el acceso autorizado al material audiovisual (H05).

## 4. Fuera del documento, pero condicionan lo que promete

| Pendiente | Dueño | Por qué importa acá |
|---|---|---|
| Rama por defecto de `e-ovrt_experimental-setup` sin `results/` → enlaces del paraguas a cifras en 404 | usuario (git) | H01/H05: el informe va a apuntar al paraguas |
| Carpeta de Drive con acceso autorizado, todavía no creada; enlace en el paraguas | usuario | H05 |
| C1: URL + fecha de acceso de los 13 videos del lote de internet (`[[PENDIENTE]]` del Anexo F) | equipo | Anexo F sigue con el marcador |
| `docker compose build` + smoke integral | equipo, antes de la presentación | H04 lo declara como previsto |

## 5. Cómo sigue

Con las siete respuestas escribo el **pase incremental v1.2 → v1.3** con el mismo circuito
de siempre: guion `herramientas/pase_etapa6_v13.py` con `--origen` = tu v1.2, todo como
**sugerencias + comentarios** (rechazar todo devuelve la v1.2 exacta), compuertas OPC y
`verificar_entregable.py`, acta en esta carpeta. Los cambios «sin pregunta» (H04, H06–H11) los
dejo ya redactados en el guion mientras esperás.
