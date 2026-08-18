# Guía para redactar el informe — para quien NO participó del trabajo experimental

**Vos sos el lector previsto de este documento.** Todo el resto del set `docs/` está
escrito como memoria de trabajo de quienes hicieron los experimentos: usa voseo, da por
sabido el contexto y cita códigos sin definirlos. Este archivo es la única puerta de
entrada pensada para alguien que llega de cero y tiene que escribir el capítulo de
resultados.

- **Fecha:** 2026-08-10 · ✎ **act. 2026-08-13** · **Estado:** tramo experimental **cerrado y
  verificado**, con **una excepción declarada**: la **jornada de fine-tuning (E-04) está en
  curso** y corre en paralelo. Por ADR-017 §2f **no bloquea la redacción**; su subsección de
  resultados queda reservada (`informe/ajustes/05` → `AJ-5.13`). Todo lo demás está congelado.
- **Qué NO vas a encontrar acá:** cifras. Las cifras tienen una sola fuente y está más
  abajo. Si un número aparece en este documento es como ejemplo de cómo citarlo, no como
  fuente.

---

## 1. El proyecto en cinco minutos

Se construyó una **plataforma de detección de riesgos de seguridad en obra** que usa
modelos de **detección open-vocabulary** (OVD): modelos a los que se les describe en
**lenguaje natural** qué buscar, en vez de entrenarlos con ejemplos etiquetados.

Se detectan dos condiciones de riesgo:

- **CR-01** — una persona **sin casco**.
- **CR-02** — una persona **sin chaleco** reflectivo.

**La tesis NO es "OVD detecta mejor que un modelo entrenado".** Eso sería perder: un
modelo entrenado para cascos detecta cascos mejor. La tesis es:

> *¿Qué rendimiento se obtiene **hoy**, en construcción civil, expresando las condiciones
> de riesgo **en lenguaje** y **sin entrenar el modelo**, y qué aporta la **plataforma**
> construida alrededor del modelo?*

Esa distinción gobierna todo el capítulo. **Cada número es el rendimiento medido de una
combinación concreta, no una nota de aprobación.** Un recall de 0,40 en multitud no es un
fracaso del proyecto: es el dato. **El contraste entre filas ES el experimento.**

### Las tres piezas de software

| Pieza | Qué hace |
|---|---|
| **media-plane** | Recibe video (archivo o cámara), corre el modelo OVD y emite **detecciones** |
| **control-plane** | Consume detecciones y decide si hay que **alertar**, aplicando una ventana temporal (no alerta con un solo frame: exige que la condición persista) |
| **experimental-setup** | La consola web y el runner de experimentos; también guarda los **resultados** |

> **Hay un cuarto repo, y no es un tercer plano.** `e-ovrt_alert-distribution` consume
> alertas ya confirmadas, aplica cooldown e idempotencia, entrega por MQTT y registra cada
> resultado. ✎ **Estado verificado 2026-08-11:** está **funcionalmente implementado** y
> cumple los seis criterios de spec 45: replay DBE idempotente, camino EBE desde el
> publisher real, MQTT QoS 1 contra broker real y reporte consolidado. Su suite cerró con
> 39 tests unitarios más la integración MQTT.
>
> **Qué falta, y no hay que ocultarlo:** E-06 (canales adicionales y dashboard propio)
> permanece excluida. ✎ **2026-08-14:** los tres pendientes que este párrafo listaba —vista
> de outcomes en la webconsole, orquestación integral del distribuidor y versionar el
> repo— se cerraron el 2026-08-13 (commits `13c801e` y `42529e2` en
> `e-ovrt_experimental-setup`; el repo `e-ovrt_alert-distribution` ya tiene historia propia,
> `c9903cc` y `1e6d8fa`). El diseño y los contratos
> se redactan desde `informe/92b`; el estado ejecutado y sus salvedades, desde
> `operacion/114`. Las latencias de loopback usadas para verificar el canal no se convierten
> en una cifra de desempeño de la tesis.

La cifra citable del tramo de distribución es **`t_alert-notification` p95 =
64,534 ms (n = 460 entregas live)** (`results/realtime/t_alert_notification/metrics.json`;
protocolo y contención en `operacion/118`). Mide **bus de alertas → PUBACK MQTT**, no
captura, inferencia ni evaluación del patrón. Para operación continua citar también el
régimen sostenido: entregas 2.ª+ **p95 = 102,025 ms (n = 104)**; las primeras entregas
dan 49,869 ms (n = 356). El smoke de loopback no es desempeño; la campaña del doc 118 sí.

### Dos escenarios de despliegue

- **DBE** — todo en un host, sobre archivos de video. Es el modo con el que se midió casi
  todo, porque es **reproducible**: la misma entrada da la misma salida.
- **EBE** — en vivo, con cámara, y los dos planos comunicándose por un bus. Es el modo que
  demuestra que funciona en tiempo real.

### Tres niveles de medición — **no los confundas, es el error más caro**

| Nivel | Qué mide | Unidad | Dónde |
|---|---|---|---|
| **Percepción (imágenes)** | ¿El modelo ve las cosas? AP por clase | una imagen | `bench_imagenes/` |
| **Nivel A** | ¿Determina bien el **estado de cada persona** (con/sin casco)? Sin tiempo | una persona | `bench_nivel_a/` |
| **Nivel B** | ¿La **plataforma entera** emite la alerta correcta? Con motor temporal | un episodio de video | `clip_bench/` |

Nivel B es **el resultado principal de la tesis**, porque es el único que mide la
plataforma y no solo el modelo.

---

## 2. Orden de lectura — cinco pasos, en este orden

1. **Este documento**, hasta el final. Incluye las trampas; saltearlas cuesta caro.
2. **`docs/sintesis/fundamentos-teoricos.md`** — la teoría, sin cifras. Es lo más
   pedagógico del set y explica por qué el diseño experimental es el que es.
3. **`docs/13-glosario-y-convenciones-de-lectura.md`** — siglas, las reglas de oro de
   lectura y (en §4.1–4.3) los códigos, los IDs de campaña y las colisiones de símbolos.
4. **`docs/sintesis/resultados-y-conclusiones.md`** — la narrativa completa con cifras.
   **Es el documento central para escribir el capítulo.** Su §8 trae la escala
   **AF-1…AF-11**: qué se afirma y **con qué fuerza**.
5. **`e-ovrt_experimental-setup/results/index.md`** y sus cuatro índices — **la única
   fuente de cifras**. Cada tabla de ahí tiene su artefacto en disco.

Cuando ya entendiste el trabajo y vas a **escribir**, el sexto paso es
**`docs/informe/ajustes/00-mapa-de-ajustes.md`**: te dice, etapa por etapa (1 → 6), qué hay
que corregir del texto que ya existe y qué hay que escribir desde cero. **Tres secciones del
informe están vacías —§17.4 Implementación, §17.5 Evaluación y §17.6 Cierre—**, y ese mapa
es el que dice qué va en cada una y de dónde sale.

> **Las etapas son seis, y son la guía de desarrollo del proyecto** (Gantt del §14.3 =
> §14.2): 1 investigación bibliográfica · 2 análisis metodológico · 3 diseño arquitectónico ·
> 4 implementación MVP · 5 evaluación y validación · 6 documentación y defensa. **El informe
> está ordenado por sección, no por etapa**, así que la correspondencia etapa → sección la
> tenés en el §0 del mapa. Ojo con un detalle: **el Gantt numera las tareas 0–5 y el §14.2
> numera las etapas 1–6** — misma secuencia, corrida en uno.
>
> **Y la regla que gobierna el tiempo narrativo (no-anacronismo, mapa regla 5): una etapa
> temprana no menciona resultados de etapas posteriores.** §15/§16 dejan la brecha con
> literatura; §17.1 deja decisiones y criterios; **todo número propio vive en §17.5/§18**.
> Si al corregir §15 te ves escribiendo una cifra medida por el proyecto, estás en la
> sección equivocada.

Recién después, y solo si necesitás el detalle de un experimento puntual, vas al documento
de `docs/operacion/NN` que la síntesis te indique.

### Qué **no** abrir

| No abras | Por qué |
|---|---|
| `docs/GUIA-CIERRE.md` y `docs/operacion/113` | Son el checklist operativo **del equipo experimental**, no material de redacción |
| `docs/informe/92` y `docs/operacion/56` y `92` | **Derogados como fuente de cifras** |
| `docs/operacion/32`, `36`, `50` | Estado de plataforma superado por `operacion/97` |
| `../informe-project-kit/` | Kit aplanado externo **eliminado**. Para ChatGPT usar `docs/informe/project-kit/README.md`: cuatro archivos de knowledge — dos `.md` generados por etapa + dos DOCX del entregable (✎ 2026-08-16) |
| Cualquier doc de `operacion/` con banner ⚠️ | Los banners dicen qué quedó superado. **Leé el banner antes que el cuerpo, siempre** |

**Regla general del set:** un documento con banner de corrección **manda por el banner, no
por el cuerpo**. Los cuerpos se conservan a propósito, para trazabilidad.

---

## 3. Cómo citar una cifra — ejemplos pareados

Estas fórmulas no son estilo: son **precisión**. Cada una existe porque la versión de la
izquierda ya se escribió mal alguna vez.

| ❌ Así NO | ✅ Así SÍ | Por qué |
|---|---|---|
| "El sistema alcanza F1 0,930" | "La mejor combinación medida (**G1**: identidad por sujeto) alcanza **F1 0,930** sobre el banco del rodaje, contra 0,789 de la línea de base" | Un número sin su combinación y su banco no significa nada |
| "El banco tiene 34 clips" | "El banco tiene **47 clips** (32 positivos / 15 negativos, **37 episodios**), en dos bloques: **A**, el rodaje guionado (34), y **B**, el lote de obra real (13)" | 34 es el **Bloque A**, no el banco |
| "34 episodios evaluables sobre 35" *(como denominador del banco)* | "34 evaluables sobre 35 **en el bloque del rodaje**" | Es el denominador de un bloque, no del banco |
| "El FAR es de 29,2 falsas alarmas por hora" | "**3 falsos positivos en 6:09,6** del único clip de soak; la tasa horaria derivada es 29,2 FA/h, sobre un denominador de 0,1027 h" | La tasa desnuda sugiere una hora observada que **no existe** |
| "El sistema cumple ≤1 FA/hora" | *(no se puede afirmar)* — "para sostener una cota harían falta ~3 h de cumplimiento anotado; el banco llega a 0,1027 h" | **Limitación L1** |
| "A nivel de escena (0,333) el sistema supera al de sujeto (0,190)" | "En el estrato B, con **solo 2 episodios evaluables**, la diferencia de F1 **no es interpretable**. Lo robusto es la **asimetría de falsos positivos**: 26 contra 323 sobre 11 clips negativos (**12×**)" | Con n=2 eso es ruido |
| "El lote de internet valida el sistema en obra real" | "El lote aporta medición en obra real **acotada**, y su aporte principal es **caracterizar dónde el sistema deja de ser evaluable**" | **Limitación L4, precisada** |
| "mAP50 0,551" | "mAP50 **0,551** sobre `bench_v3` (6.477 imágenes de **3 fuentes independientes**), con el desglose por estrato" | **Nunca solo el agregado** (limitación L5) |
| "Los clips negativos bajan el F1" | "Los clips negativos **no entran** a precision/recall/F1: su métrica son los falsos positivos" | Promediarlos cuenta aciertos como catástrofes |
| "El sistema emitió 12 falsos positivos" *(contando re-alertas)* | "…sin contar `re_alerts`, que son re-confirmaciones con la infracción **todavía activa**" | Una re-alerta no es un error |
| "La latencia de vidrio a alerta es de 14,7 ms" | "El tramo medido G2A es de 14,7 ms **desde el dequeue**; de vidrio a alerta hay que sumarle la captura (202–217 ms en el rodaje)" | Se mide desde el dequeue, no desde el fotón |
| "El SDR mejora al bajar la densidad" | *(no se compara)* — "el SDR **solo es comparable dentro de una misma cadencia**" | Es artefacto del instrumento |

**Regla que resume todas:** un número va siempre con **(a)** qué combinación lo produjo,
**(b)** sobre qué material, y **(c)** con qué `n`.

### 3.1 ✎ Qué NO se referencia jamás en el texto del informe (regla del usuario, 2026-08-16)

**El informe es autocontenido.** Toda esta documentación —los docs de `operacion/`, los
ADRs (de cualquier serie), las specs, las fichas `AJ-`/`R-`/`PODA-`, los IDs internos
(`F-xx.x`, `D-xx.x`, `T-FT-xxx`), las rutas del repo y los índices de `results/`— es
**andamiaje local para guiar el desarrollo**, y el informe **no la menciona nunca**: ni
como cita, ni como paréntesis de procedencia, ni como nota al pie. En el texto del
informe una afirmación se sostiene por el propio informe (§), por la bibliografía, o por
la combinación experimental declarada (la regla (a)(b)(c) de arriba) — sin decir de qué
archivo interno salió el número. La procedencia interna vive en los borradores como
notas al integrador (bloques `> ✎`, que no se pegan) y en el tablero del manual `08`.
Sí se usan los identificadores que el informe define para sí: condiciones CR-01/CR-02,
contratos (`media.detection.v1`), limitaciones L1–L8, nombres de configuración.

---

## 4. Las siete trampas que más caro salen

> **Trampa del banco de clips:** 47 = 34 rodaje + 13 internet (bloques A/B del
> manifest) y, por otra partición, 32 positivos + 15 negativos. Nunca mezclar ambas
> descomposiciones en una misma frase.

**1. Escribir el capítulo sobre el banco de 34 clips.** Es el error más probable, porque
varios documentos del kit fueron escritos cuando ese era el banco. **Vigente: 47 clips,
37 episodios.** Si un documento dice 34 sin aclarar "bloque A", está desactualizado.

**2. Decir que no se midieron falsas alarmas** (porque un doc viejo dice que FAR/hora "no
es una métrica de este trabajo"). **Se mide y se reporta**, pero no sostiene una cota. Ver
la tabla de arriba.

**3. Rankear granularidades en el estrato B.** Con 2 episodios evaluables no sale ningún
ranking. Lo publicable de ese estrato es la asimetría de falsos positivos y la frontera de
juzgabilidad.

**4. Decir que el lote de internet "levanta" la limitación L4.** La decisión firmada dice
**precisada, no levantada**. Varios documentos viejos usan "levanta".

**5. Citar el "BENCH de 196 imágenes" o el clip `cb_b01_p7`.** Los dos están **retirados**:
el primero por estar 20–25 % fuera de dominio, el segundo por licencia sin registrar y GT
generado por IA. Si los ves citados en un doc, ese doc es viejo.

**6. Encuadrar el fine-tuning como "descartado por falta de tiempo"** (o "por
presupuesto de tiempo", o "por secuenciación" — la enmienda intermedia). Documentos
viejos del kit lo dicen; **esa causa está prohibida (ADR-017)**. Vigente: el
fine-tuning (E-04) es una **rama experimental condicionada por datos y protocolo desde
el planteo** (Tabla 37: baseline primero; F-100.1 ya resuelta; gates vigentes de freeze,
serving/evaluación y procedencia) — el cómputo nunca fue la causa de descarte (Mendieta
disponible y envelope T1 acotado) — y está
**comprometida como jornada completa**, que se documenta con sus resultados,
limitaciones y estado a la entrega, con causa técnica.

> ✎ **2026-08-13 — estado operativo:** `1166583` cerró freeze/smoke técnico en A30 con
> 12 tensores/3.096 parámetros y optimizer 12/12; dual gate y serving real están verdes.
> T1 full sigue en NO-GO por contrato de serving (D-FT-08/T-FT-005), evaluación
> (T-FT-031) y baseline YOLOE-26s (T-FT-032). La procedencia (T-FT-023) quedó
> **CERRADA** el 2026-08-13 (snapshot tar `639e60df…`).
> ✎ **2026-08-15 — el contrato de serving quedó CERRADO, y la misma jornada cerraron
> T-FT-031 y T-FT-032.** El usuario firmó D-FT-08 (T-FT-005 `done`), D-FT-12 y D-FT-13,
> y después se ejecutó todo lo técnico: comando de evaluación congelado, enforcement
> canónico v2 y **baseline YOLOE-26s one-shot sobre `bench_v3`** (doc 120: `bare_head`
> AP50 0,000; recall CR-01 agregado 0,0002; retención a proteger person 0,7843 /
> helmet 0,6286 / vest 0,2642 — cifras de la RAMA, tablas propias, por estrato).
> **El NO-GO de T1 full quedó en su último eslabón**: emitir `full-authorization.json` y
> el `RUN` manual (T-FT-043). Al redactar: no listar decisiones NI gates técnicas
> pendientes en E-04; ~~**no hay cifra del checkpoint ajustado** (no existe)~~ **← SUPERADO
> el 2026-08-17, ver la adenda al final de este bloque: la cifra existe** y la baseline
> no se compara con la tabla histórica del doc 64 (doc 120 §2.5). **D-FT-12 se firmó
> antes de la baseline**: pre-registración estricta. La negativa sin auth dejó cero
> full. La proyección Slurm 2026-08-18 no es
> promesa. No hay cifra científica citable ni job full enviado.
>
> ✎ **2026-08-15 (noche) — T-FT-043 CERRADA: el job full se envió.** La autorización se
> emitió y verificó en el clúster con sus 7 gates, el ensayo `--test-only` pasó y el
> `RUN` quedó **encolado (job `1167640`)**. Lo de arriba —"último eslabón", "cero jobs
> full", "ni job full enviado"— queda **superado**: ya no hay ninguna tarea previa
> pendiente. **Lo que sigue abierto es otra cosa: la corrida en sí y su evaluación.**
> Enviar no es medir: **sigue sin existir cifra del modelo ajustado**, así que en el
> informe esa subsección va reservada con `[[PENDIENTE: …]]`, nunca con un valor
> estimado ni con una redacción que sugiera que la comparación ya se hizo.
>
> ✎ **2026-08-17 — LA JORNADA CERRÓ Y LA CIFRA YA EXISTE: veredicto D-FT-12 = NO-GO**
> ([`operacion/123`](operacion/123-cierre-jornada-t1-no-go.md)). **La subsección deja de ir
> reservada: se redacta con estos números** — `bare_head` AP50 **0,0000 → 0,0455** y recall
> CR-01 **0,0002 → 0,2089** (de 1 violador detectado en todo el banco a 1.109), `vest`
> 0,2642 → **0,3292**, contra `person` 0,7843 → 0,6932 y mAP50 0,4193 → 0,4171. **NO-GO**
> porque el gain gate pedía +0,05 (faltaron **0,0045**) o recall >0,5, y la retención de
> `person` cayó **−11,62 %** sobre un tope de 10 %.
>
> **Cómo redactarlo, sin margen:** es un **negativo pre-registrado** — los márgenes se
> firmaron el 15/08 antes de existir baseline y checkpoint — así que **es un resultado, no un
> fracaso**, y **jamás** se atribuye a falta de tiempo (criterio de invalidación 1 de
> ADR-017). Reportar **siempre por estrato además del agregado**: en `bench_obra_val` el
> ajuste **mejora** (mAP50 +0,0828, `bare_head` 0,000 → 0,2614) y son `chv`/`shel5k` los que
> bajan, por `helmet`. Estas cifras son de la **rama comparativa**: no se funden con el
> núcleo zero-shot, no van a `results/` y **no se comparan con la tabla del doc 64**
> (protocolo distinto). El gate de latencia **no se midió** y eso se dice explícito (F-123.1),
> no se omite.
>
> **T2 (si su jornada corre antes del cierre del informe) se redacta con esta secuencia
> exacta, sin suavizarla:** tras el NO-GO de T1 la escalera cerró la rama; una **enmienda
> explícita (D-FT-14, 2026-08-17)** reabrió T2 como tier **exploratorio** para descartar que
> el fallo fuera artefacto de capacidad, **con márgenes propios firmados antes de cualquier
> resultado T2** (D-FT-15) y expectativa pre-registrada (NO-GO probable). Nunca presentarlo
> como reintento de T1 ni omitir que la enmienda fue posterior al veredicto — la transparencia
> de la secuencia ES el argumento. **T3 no corre**: trabajo futuro con causa técnica (sin
> baseline MM-GDINO geométricamente sana), jamás "falta de tiempo".

**7. Describir la plataforma con DOS patrones de acople.** Son **tres**, y el tercero está
registrado en **[ADR-018](decisiones/adr-018-acople-bff-subproceso-distribucion.md)** desde
el 2026-08-15: **(a)** HTTP config-driven — la webconsole y el runner son clientes de los
dos planos (ADR-008/009); **(b)** bus ZeroMQ PUB/SUB + msgpack, media→control (ADR-003);
**(c)** **BFF-subproceso** — el runner de la webconsole lanza `eovrt-distribute` como
proceso hijo local, porque el repo de distribución es una CLI y **no** un servicio HTTP.
Dos precisiones que se pierden fácil: el *dato* de distribución igual viaja por el bus
(`:5558`), así que lo propio del tercer patrón es el **control del ciclo de vida**, no el
transporte; y el requisito `EOVRT_DISTRIBUTION_EXECUTABLE` de la consola dockerizada es
parte de la decisión, no una nota de operación. Documentos anteriores al 08-15 describen
sólo dos acoples: están viejos.

> ⛔ **✎ 2026-08-18 — TODA LA TRAMPA 7 DE ARRIBA QUEDÓ SUPERADA. ADR-020 derogó a ADR-018
> y los patrones de acople volvieron a ser DOS.** El párrafo original (y su primera
> corrección del mismo día, que hablaba de tres) se conservan como cuerpo histórico, pero
> **no describen el sistema entregado**.
>
> **Lo vigente, y lo único que va al informe:**
> **(a) HTTP config-driven en los TRES módulos** — medios `:8080`, control `:8081` y
> **distribución `:8082`**; la webconsole y el runner son clientes de los tres y **ninguno
> consume el bus**. **(b) bus ZeroMQ PUB/SUB + msgpack** para el dato: detecciones
> `:5557` (medios→control) y alertas `:5558` (control→distribución).
>
> **Qué NO escribir:** "BFF-subproceso", "tres patrones de acople", "el repo de
> distribución es una CLI y no un servicio". El camino por subproceso **sigue existiendo
> en el código** como **fallback operativo** detrás de una variable de entorno, pero eso
> es un detalle de operación, **no arquitectura**: no se cuenta como patrón ni se
> describe en el capítulo. Y ojo con el matiz simétrico: el distribuidor **conserva su
> CLI** para el camino offline, igual que el control-plane — decir "es solo un servicio"
> tampoco es exacto.
>
> **La trampa, reformulada:** el número de patrones cambió tres veces en cuatro días
> (dos → tres con ADR-018 → tres con ADR-019 → **dos** con ADR-020). Cualquier documento
> que no lleve enmienda del 2026-08-18 está describiendo un estado intermedio.
>
> **Sobre la containerización, que es una pregunta aparte y tiene respuesta propia
> (✎ 2026-08-18):** está **diferida con causa** y **sí se puede mencionar en el informe**.
> Se va a hacer **después** de cerrar la redacción; su razón de ser es la
> **reproducibilidad** (que un tercero levante la plataforma en otra máquina), no cerrar
> el capítulo; y su **documentación operativa vive en los repositorios**, no en la tesis.
> Escribila como **compromiso declarado con su fundamento**, en el cierre (§17.6/§18) y en
> el anexo de reproducibilidad (§19). **Nunca en presente, nunca como capacidad existente,
> nunca como instructivo de despliegue.** Regla corta: *describir el compromiso es
> correcto; describir un despliegue que no corrió es falso.*

> ⏳ **✎ 2026-08-12 — y la jornada ARRANCÓ.** Corre en paralelo a la redacción y **no la
> bloquea** (ADR-017 §2f). Para vos significa tres cosas concretas: **(1)** el §17.5 tiene
> una subsección **reservada** para esa rama (`informe/ajustes/05` → `AJ-5.13`) — no la
> borres ni la escribas como exclusión; **(2)** mientras no haya un artefacto en `results/`,
> **no hay cifra citable** de esa rama; **(3)** sus resultados, cuando existan, van
> **rotulados como rama comparativa y en tablas propias** — nunca fundidos con los del
> núcleo zero-shot, porque la pregunta de la tesis es justamente cuánto rinde el stack
> **sin entrenar**. Un desenlace negativo es un resultado documentable, no una omisión.

---

## 5. Cómo se decide qué se puede afirmar

No lo decidís vos ni lo decide el número: está pre-registrado en la escala
**AF-1…AF-11** (síntesis §8), que clasifica cada conclusión por **fuerza de evidencia**:

- **Establecida** — se afirma sin hedging.
- **Establecida direccionalmente** — se afirma el sentido, no la magnitud.
- **Tendencia con mecanismo** — se describe el mecanismo, se declara que no es efecto
  establecido.
- **No cerrada** — se declara como limitación, no se afirma.

**Consultá esa tabla antes de escribir cualquier afirmación.** Y las **limitaciones
L1–L8** (versión vigente en `results/index.md`) se declaran, no se esconden: en este
trabajo lo que no se pudo medir es parte del resultado.

Un principio que atraviesa el capítulo: **varias de las cosas más valiosas del trabajo son
refutaciones de predicciones propias** — hipótesis escritas *antes* de medir y que la
medición tumbó. Eso se cuenta como fortaleza metodológica, no se disimula.

---

## 6. Dónde vive cada cosa

| Necesitás | Está en |
|---|---|
| **Cifras de cualquier tipo** | `e-ovrt_experimental-setup/results/index.md` + sus 4 índices |
| La narrativa completa con contexto | `docs/sintesis/resultados-y-conclusiones.md` |
| Teoría, definiciones, por qué el diseño es así | `docs/sintesis/fundamentos-teoricos.md` |
| Qué calcula cada métrica | `docs/sintesis/inventario-de-metricas.md` |
| Cómo está implementada la plataforma (concreción técnica) | `docs/operacion/97-relevamiento-plataforma-2026-08-05.md` — la foto verificada contra código (2.203 tests verdes) |
| El módulo de **distribución de alertas** (§17.3.10) | `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md` — diseño y contratos · **`operacion/114`** — implementación verificada, pruebas y brechas · **`nucleo/19`** — ciclo de vida y fronteras · **`operacion/124`** — servicio HTTP (ADR-019). Estado: funcional e integrado — ~~pendientes webconsole, orquestación y commits~~ ✎ cerrados el 2026-08-13; desde el 2026-08-18 corre además como servicio HTTP (`:8082`, subproceso sigue default) |
| El kit para trabajar en **ChatGPT Web** | `docs/informe/project-kit/README.md` — instrucciones + cuatro archivos de knowledge: contexto base, etapa activa y los dos DOCX del entregable (informe sin §17.3 + Etapa 3 vigente; ✎ 2026-08-16) |
| Siglas, códigos, colisiones de símbolos | `docs/13-glosario-y-convenciones-de-lectura.md` §3 y §4 |
| Reglas de estilo y honestidad al redactar | `docs/informe/97` §1–§3 (⚠️ **su §5 está superada**) |
| Qué figura/tabla va en cada sección | `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md` §1 (✎ al día al 2026-08-10 — incluye el tramo de video, T-82…T-84/FIG-F) |
| **Qué hay que cambiarle al informe, etapa por etapa** | ✎ **`docs/informe/ajustes/00-mapa-de-ajustes.md`** — el mapa de Etapa 1 a Etapa 6, con un documento por etapa (`01`…`06`). **Empezá por acá y no por el 93**: el 93 cubre solo la Etapa 3 |
| **Cómo se aplica todo eso: dónde escribís, en qué orden, qué te toca** | ✎ **`docs/informe/ajustes/08-manual-de-aplicacion.md`** — **es el documento del día 1.** Trae el reparto de trabajo, el orden con su dependencia dura (la vara del §15 antes que el §17.5), el loop repetible por sección, las cuatro puertas de cierre y el tablero de las 109 unidades. **Leelo después de esta guía y antes de tocar nada** |
| Qué hay que corregir del **§17.3** (Etapa 3) | `docs/informe/93` — los **26 redlines** (R-01…R-26). Enrutados desde `informe/ajustes/03-etapa-3-diseno-arquitectonico.md` |
| Las secciones que hay que **escribir desde cero** | **§17.4, §17.5 y §17.6 están vacías** en el informe. Qué tiene que decir cada una: `informe/ajustes/04-etapa-4-implementacion.md`, `05-etapa-5-evaluacion-y-validacion.md` y `06-etapa-6-documentacion-y-cierre.md` |
| Qué **recortar** del informe (está muy extenso) | ✎ `docs/informe/ajustes/07-critica-extension-y-poda.md` — 18 podas medidas (`PODA-nn`, ~27% del texto), con guardrails de qué NO tocar. Se aplica junto con los `AJ-`/`R-` de cada sección |
| Texto ya redactado para adaptar | `docs/informe/94` (§1–§9: cubre 9 de los 26 redlines, y es el modelo de estilo) |
| Por qué se decidió algo | Los **ADR** (`docs/decisiones/`) + `docs/nucleo/10` (alcance y exclusiones) |
| El detalle de un experimento puntual | `docs/operacion/NN` — entrá por la síntesis, que te dice cuál |

---

## 7. Si algo no cierra

**El set es grande y tiene tres semanas de correcciones encima.** Si encontrás dos
documentos que se contradicen, la jerarquía es:

1. `results/index.md` y sus índices — para **cifras**, siempre gana.
2. `docs/sintesis/resultados-y-conclusiones.md` — para **interpretación**.
3. El banner ⚠️ o ✎ de un documento — gana sobre el cuerpo de ese documento.
4. La fecha — más nuevo gana, y las fechas están en la cabecera de cada doc.

**Y si aun así no cierra, preguntá antes de escribir.** Una contradicción que sobrevive a
esa jerarquía probablemente sea un error real que conviene arreglar en el repo, no algo
que haya que resolver escribiendo con ambigüedad.

**Verificación mecánica disponible:** `python3 docs/operacion/datos/96-verificar-indices.py`
comprueba que las cifras citadas en los índices coincidan con los artefactos en disco (19
cifras sobre las 16 campañas). Si dudás de un número, corrélo.
