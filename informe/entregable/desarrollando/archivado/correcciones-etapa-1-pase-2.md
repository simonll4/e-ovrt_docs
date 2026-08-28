# Correcciones a la Etapa 1 — pase 2: revisión de la iteración de GPT sobre §15

- **Fecha:** 2026-08-27 · **Sobre:** `desarrollando/Etapa 1 — copia ajustada E1 2026-08-27.docx`
  (10.870 palabras; sin control de cambios ni comentarios).
- **Contra qué se revisa:** el texto base `90d` (22.266 palabras) y el pase 1
  (`correcciones-etapa-1.md`: E1-01…E1-12, AJ- abiertos, podas con dos enmiendas, guardrails).
- **Tres preguntas que ordenan la revisión:** (1) ¿cumplió lo pedido? (2) ¿la reducción a la
  mitad está justificada por aporte, o hubo poda por poda? (3) ¿sigue siendo un estado del
  arte de tesis, o quedó un texto acomodado a nuestro diseño?
- **IDs:** los comentarios nuevos continúan la serie: **E1-13…E1-23**. Las decisiones nuevas:
  **D-E1-7, D-E1-8**. Nada de esto está aplicado.

---

## 0. Veredicto en cuatro líneas

1. **Cumplimiento: alto.** 11 de los 12 `E1-` están aplicados; el que falta (E1-06) es el de
   menor peso. Los `AJ-` abiertos quedaron resueltos (dos de ellos por eliminación). Cero
   fugas de andamiaje, cero resultados propios: la regla de no-anacronismo se respetó.
2. **Extensión: justificada en el agregado.** 22.266 → 10.870 palabras (−51 %). La poda
   pre-autorizada (`ajustes/07`, PODA-01…04 con las enmiendas del pase 1) proyectaba
   ~10.300. GPT cortó **lo que se le dijo que cortara y conservó lo que se le dijo que
   conservara** (§15.2.5 brechas 0 % · §15.4.3 brechas 0 % · RTSP/RTP · Tabla 8 · las 7
   tablas). No hay poda por poda **en el qué**; hay daño colateral **en el cómo**.
3. **Daño colateral: seis puntos concretos**, todos de una misma clase — *la prosa se
   comprimió más rápido que lo que dependía de ella*: tablas que quedaron con filas que el
   texto ya no explica, una brecha que cita un análisis borrado, numeración con huecos, un
   paradigma sin ficha, citas huérfanas en notas, y la síntesis de licencias perdida.
4. **Registro de tesis: se sostiene, con dos correcciones.** Dos pasajes nuevos afirman en
   voz normativa —y sin fuente— criterios que son *nuestros* (los tres niveles de evaluación
   del proyecto; los criterios de selección del tracker). Un jurado los leería como "el
   autor decide y lo disfraza de literatura". Se corrigen convirtiéndolos en brecha con cita.

---

## 1. Cumplimiento del pase 1

| Unidad | Estado | Dónde / observación |
|---|---|---|
| E1-01 Swin-B sin vara | ✅ | §15.2.1.1.3, párrafo nuevo: pesos públicos, sin cifra zero-shot comparable porque COCO está en su entrenamiento. **Pero** se asentó como hecho lo que el pase 1 marcó **[R] a verificar**, y cita "(IDEA-Research, 2024)" **sin letra**, colisionando con 2024a/b/c → E1-21 |
| E1-02 YOLOE-v8 vs YOLOE-26 | ✅ | §15.2.1.2.2: "los resultados publicados para YOLOE-v8 no deben utilizarse como si fueran una medición de las variantes YOLOE-26" (Ultralytics, 2026) |
| E1-03 Tabla 4 fila YOLOE | ✅ | Fila reescrita: "No evaluada por los autores · la receta estándar produce vocabulario fijo; la retención requiere reinyectar y evaluar vocabulario abierto". La prosa (§15.2.4 ¶4) lo acompaña |
| E1-04 equilibrar fine-tuning | ✅ parcial | Se sumó la vara tamaño-de-datos/parámetros (Kumar et al., 2022; Lee et al., 2022) y YOLOE ganó peso. El costo: la Tabla 4 quedó sin sostén → E1-14 |
| E1-05 Bloque D mal rotulado | ✅ | Renombrado "Modelos guiados por prompts generalistas: generativos e híbridos"; fila de Tabla 2 corregida. El costo: el bloque quedó **sin ninguna ficha** → E1-13 |
| E1-06 duplicación intro/fichas | ❌ | Los párrafos 2–8 de §15.2.1 están **idénticos** al base: siguen dando 52,5 AP, 35,9 AP @102,5 FPS, etc., que las fichas repiten → E1-19 |
| E1-07 cierre de §15.3.2.1 | ✅ | Reescrito en criterios, "no una elección anticipada de un tracker particular". FairMOT y la referencia colgada desaparecieron. **Pero** el párrafo quedó **sin una sola cita** → E1-16 |
| E1-08 métricas MOT comprimir | ✅ | 126 palabras, una oración por métrica + el argumento del valor operativo. Ecuación fuera |
| E1-09 Tabla 7 | ✅ | Fila inter-cámara eliminada; fila de datasets conservada |
| E1-10 PODA-04 con excepción | ✅ | RTSP/RTP íntegro en lo esencial (200–800 ms, play-out buffer, Axis 2015, ONVIF); **§15.4.3 intacta (0 %)**; Tabla 8 completa |
| E1-11a ingesta por SDK | ✅ | §15.4.2 ¶2 (Luxonis, s. f.), sin equipararla a inferencia en el borde |
| E1-11b MQTT / pub-sub | ✅ | §15.4.2 ¶4 (OASIS, 2019): QoS 1, PUBACK, reentregas, idempotencia |
| E1-12 texto de plantilla | ✅ | Desapareció con el párrafo de RTMP |
| Erratas: Ahmad 2005 · ".." · FairMOT · Tabla 8 push/pull · split del 63,0 | ✅ | Ahmad 2005 ahora sostiene *transcodificación* (uso correcto); Tabla 8: "RTSP controla la sesión; RTP transporta el flujo"; "62,6 AP en COCO val y 63,0 AP en test-dev" |
| AJ-1.04 / AJ-1.05 (OmDet-Turbo) | ✅ por eliminación | Ficha y filas de Tabla 3 eliminadas. Queda una cita huérfana en la Fuente de Tabla 3 → E1-20 |
| AJ-1.09 Tabla A.1 · AJ-1.16 §16 | — | Fuera de este `.docx`. Ver D-E1-7 |

---

## 2. La extensión: qué se cortó y si estaba justificado

| Bloque | Base | GPT | Δ | Qué salió | Juicio |
|---|---:|---:|---:|---|---|
| §15.1 alcance | 181 | 181 | 0 % | — | ✅ |
| §15.2.1 paradigmas y fichas | 4.641 | 2.070 | −55 % | Fichas de GLIP/GLIPv2, OV-DETR, OV-DINO, OmDet-Turbo, Detic, DetCLIP; las 4 del Bloque D colapsadas a un párrafo; **Bloque E completo** (Grounded SAM, OVTrack, Roboflow Rapid) | ✅ es exactamente PODA-01 (quedan los modelos con rol + techo de API cerrada). Tres pérdidas a reparar: numeración (E1-13), paradigma 4 sin ficha (E1-13), genealogía GLIP (E1-18) |
| §15.2.2 composición | 665 | 128 | −81 % | La descripción larga de Grounded SAM/SAM 2 | ✅ la idea (desacoplar etapas, costo del pipeline completo) sobrevive y es la que la plataforma necesita; no hay segmentación en la tesis |
| §15.2.3 síntesis + Tabla 2/3 | 1.129 | 1.088 | −4 % | Filas de OmDet en Tabla 3 | ✅ |
| ex-§15.2.4 ventajas/limitaciones (.1–.4) | ~1.000 | 0 | −100 % | Eficiencia (duplicaba 15.2.3) · generalización · **licencias y riesgo de adopción** · segmentación (duplicaba 15.2.2) | ⚠ tres de las cuatro eran duplicación (PODA-02). **La de licencias no**: es criterio de selección declarado y se perdió su síntesis → E1-17 |
| §15.2.4 fine-tuning (ex-.5) | 2.688 | 885 | −67 % | Las recetas de MM-GDINO en detalle, LoRA médico (Rasaee), el hallazgo del text encoder frágil de YOLO-World, OWL-ST/n-gramas, Florence-2 LoRA (Ucar/Skalski), *catastrophic forgetting* (Kirkpatrick) | ⚠ la compresión es defendible, pero **la Tabla 4 conserva 11 filas que nombran esas recetas** y la prosa ya no las presenta → E1-14 |
| **§15.2.5 brechas + Tabla 5** | 1.737 | 1.737 | **0 %** | — | ✅ **el núcleo, intacto** |
| §15.2.6 cierre | 161 | 161 | 0 % | — | ✅ |
| §15.3.1 métodos MOT | 806 | 277 | −66 % | Fichas de DeepSORT/ByteTrack/OC-SORT/BoT-SORT → un párrafo de contraste | ✅ PODA-03; Tabla 6 conserva la comparativa completa |
| §15.3.2 síntesis + Tabla 6 | 554 | 436 | −21 % | — | ✅ (ver E1-16 por las citas) |
| §15.3.3 métricas | 373 | 126 | −66 % | Tres subsecciones y la ecuación | ✅ E1-08 (ver E1-16 por el cierre) |
| §15.3.4 brechas + Tabla 7 | 633 | 567 | −10 % | Fila inter-cámara | ✅ |
| §15.4.1 protocolos | 4.025 | 1.039 | −74 % | RTMP, HLS/DASH/CMAF, WebRTC, SRT, RIST en prosa (→ un párrafo en 15.4.2) | ✅ PODA-04 con la excepción cumplida: criterios de clasificación + RTSP/RTP íntegros |
| §15.4.2 servidores → "alternativas complementarias" | 2.544 | 322 | −87 % | Roles del servidor en detalle, observabilidad, edge/cloud/híbrido, Janus/Kurento/MediaMTX/OME/SRS | ✅ nada de eso sostiene una decisión; el reemplazo trae lo que faltaba (SDK, MQTT). Una consecuencia sin reparar → E1-15 |
| **§15.4.3 brechas** | 737 | 737 | **0 %** | — | ✅ **intacta, como se pidió** |
| §15.4.4 síntesis + Tabla 8 | 589 | 594 | +1 % | — | ✅ |
| **Total** | **22.266** | **10.870** | **−51 %** | | **Dentro del 5 % de lo pre-autorizado (~10.300)** |

**Lectura:** la mitad que se fue es la mitad que el `07` había identificado hace dos
semanas como *survey de tecnologías no usadas* (16 % del informe entre §15.4 y §15.3) y
*catálogo sin uso posterior* (25 modelos para 3 familias evaluadas). Lo que sostiene un
argumento de defensa —las brechas, las varas, las tablas de síntesis— está **palabra por
palabra**. La reducción de páginas está justificada. Lo que hay que arreglar es el
**acabado**: seis lugares donde el texto comprimido dejó colgando algo que dependía de él.

---

## 3. Lo que no cumplió o hay que mejorar

### 3.1 Consecuencias de la compresión (acabado)

**E1-13 · 🟠 · Numeración con huecos y un paradigma sin ficha.** Al borrar fichas se
conservaron los números viejos: el Bloque A pasa de su título a **15.2.1.1.3** (Grounding
DINO) y **15.2.1.1.5** (DINO-X) — faltan .1, .2 y .4, y se ve en el índice. Renumerar
(.1 y .2). Además, el **Bloque D quedó sin ninguna ficha** mientras A, B y C conservan el
formato *Arquitectura · Mecanismo · Resultados · Licencia*: el paradigma 4 de la
introducción (generativo, Florence-2) es el único de los cuatro **sin desarrollo propio**.
Restituir una ficha breve de Florence-2 (~120 palabras: seq2seq, DaViT, FLD-5B, 37,5 mAP
COCO zero-shot, MIT) — es el representante declarado del paradigma y aparece en Tabla 2,
Tabla 4 y §15.2.5.2.

**E1-14 · 🟠 · Tabla 4 quedó sin sostén en la prosa.** De sus 11 filas, **7 nombran recetas
que el texto ya no presenta**: "MixedGroundingDataset", "MultiModalDataset",
"Reparametrización eficiente (sin RepVL-PAN)", "Adaptación LoRA", "Self-training (OWL-ST)
con pseudo-anotaciones / n-gramas", "Florence-2 fine-tuning con LoRA". Su Fuente cita a
Rasaee (2025) y Ucar (2025), que no aparecen en ningún párrafo. Una tabla con términos que
el lector no encontró antes es indefendible. Dos salidas, elegir una: (a) restituir **una
oración por familia** que nombre la receta (≈150 palabras en total), o (b) reducir la
Tabla 4 a las filas que la prosa sostiene (GDINO closed/open-set, YOLO-World con/sin
encoder, YOLOE transferring, OWL-ST). Recomendación: (a) — la tabla es el resumen que
§17.5 va a citar. Errata en el mismo bloque: dos oraciones seguidas anuncian la tabla
("La Tabla 4 resume…" / "La Tabla 4 sintetiza…"); dejar una.

**E1-15 · 🟠 · §15.4.3.3 cita un análisis que fue borrado.** Dice: *"Si bien se estableció
un mapa de roles potenciales por familia de protocolos y se analizaron las capacidades de
interoperabilidad de servidores de medios de código abierto…"*. Ese análisis (ex-§15.4.2.5)
ya no existe. Reescribir el arranque: *"Aun cuando la literatura describe los roles del
servidor de medios (§15.4.2), no ofrece evidencia consolidada sobre el overhead real…"*.

**E1-17 · 🟡 · Se perdió la síntesis de licencias.** La ex-§15.2.4.3 ("Licencias y riesgo
de adopción") no era duplicación: reunía GPL-3.0 (YOLO-World) / AGPL-3.0 (YOLOE) /
CC BY-NC-SA (OV-DETR) frente a Apache-2.0 (GDINO, OmDet, LLMDet) y la API cerrada de
1.5/DINO-X, y cerraba con *"el régimen de disponibilidad se mantiene como criterio técnico
de evaluación"* — que es un criterio de selección que §17.1 usa. Hoy la información quedó
dispersa en las líneas "Licencia" de cada ficha y la Tabla A.1. Restituir **un párrafo**
(~100 palabras) en §15.2.3, después de la Tabla 2.

**E1-18 · 🟡 · Genealogía y vocabulario estándar.** Con GLIP eliminado, Grounding DINO
aparece sin su antecedente directo (el preentrenamiento por *grounding* región–palabra que
GDINO hereda). Una oración en §15.2.1.1.3 basta: *"Grounding DINO extiende la formulación
de detección como phrase grounding introducida por GLIP (Li et al., 2021)…"*. Del mismo
modo, el término *catastrophic forgetting* (Kirkpatrick et al., 2017) —el nombre estándar
del fenómeno que §15.2.4 describe— desapareció; conviene una mención, porque es el
vocabulario con el que el jurado va a preguntar.

**E1-19 · 🟡 · E1-06 sigue sin aplicar.** Los párrafos 2–8 de §15.2.1 son idénticos al
texto base y repiten las cifras de las fichas (52,5 AP Swin-L; 35,9 AP @102,5 FPS; OWL-ST
"más de mil millones"). Dos opciones: dejar la introducción **sin cifras** (solo el
mecanismo de cada paradigma) y que las cifras vivan en las fichas; o al revés. Recomendación:
la primera — la introducción explica *qué* es cada paradigma, las fichas *cuánto* rinden.

**E1-20 · 🟡 · Citas huérfanas en notas de tabla.** Tabla 3: la Fuente cita "T. Zhao et al.
(2024)" (OmDet-Turbo) y ya no hay fila de OmDet. Tabla 5: la Fuente cita "Zhou et al.
(2022a" (Detic, eliminado); las filas solo usan 2022b. Corregir las dos Fuentes. La Fuente
de la Tabla 8 cita ~12 obras que ya no aparecen en prosa (Pantos, DASH-IF, Roy, Sonono,
VSF, W3C…): APA lo admite —una tabla es una cita válida— pero hay que **decidirlo
conscientemente** (D-E1-8), porque esas entradas van a sobrevivir en la lista de
referencias sostenidas solo por una nota.

### 3.2 Registro de tesis (la pregunta 3)

Verificado: **no hay ningún resultado propio, ningún nombre de configuración, ningún
identificador de la plataforma** en el texto (`bench_v3`, E-IND, 560 px, ZeroMQ,
histéresis, umbrales: cero apariciones). Las brechas se cierran con *"la respuesta
experimental corresponde a las secciones posteriores"*. En eso el texto es un estado del
arte y no una justificación del diseño. Pero hay **dos pasajes nuevos** donde nuestro
marco se cuela en voz normativa y sin fuente:

**E1-16 · 🟠 · Dos párrafos prescriben criterios nuestros como si fueran literatura.**
(a) §15.3.3 cierra: *"la evaluación del seguimiento debe distinguirse de la evaluación del
**estado por persona** y de la **alerta temporal producida por la plataforma**"*. Esos son
los tres niveles de evaluación del proyecto (§17.1), enunciados aquí como conclusión del
estado del arte, sin cita. (b) §15.3.2.1 enumera como criterios *"independencia respecto
del detector, determinismo y reproducibilidad, ausencia de entrenamiento adicional y
transparencia de las reglas de asociación"* — que son exactamente las propiedades de
nuestro tracker — y el párrafo **no tiene una sola cita** (el original citaba a Adžemović,
2025, para la compatibilidad de los métodos geométricos con OVD). Un jurado lee: *"el
autor eligió y lo disfrazó de literatura"*. Corrección para (a): formularlo como **brecha**
—*"estas métricas caracterizan al tracker pero no miden el valor temporal de una alerta;
la evaluación de un sistema asistivo exige niveles adicionales, cuya definición
corresponde al protocolo experimental"*— sin los términos propios. Para (b): restituir la
cita de Adžemović (2025) y anclar los criterios en el hecho publicado (los métodos sin
apariencia no dependen de un dominio de entrenamiento), no en su deseabilidad.

**El resto del texto nuevo pasa la prueba.** El párrafo de MQTT (OASIS, 2019) describe
QoS 1 y la idempotencia como propiedades del estándar, no como nuestra política. El de SDK
(Luxonis, s. f.) evita explícitamente equipararlo a inferencia en el borde. El de Swin-B se
limita al régimen de la cifra. Los de Kumar/Lee traen literatura general de fine-tuning
que no conocía el texto y que es la vara correcta para lo que §17.5 va a decir.

### 3.3 Referencias y trazabilidad

**E1-21 · 🟠 · Seis referencias nuevas sin entrada verificable, y una colisión.** El pase
introdujo: *IDEA-Research (2024)* —**sin letra**, en un informe que ya tiene 2024a/b/c—,
*Ultralytics (2026)*, *Kumar et al. (2022)*, *Lee et al. (2022)*, *Luxonis (s. f.)*,
*OASIS (2019)*. Ninguna está en el `96e` actual. Pedir el **delta de referencias** (altas
completas en APA 7 con DOI/URL, y las bajas que PODA-18 arrastra: GLIP, OV-DETR, OV-DINO,
OmDet, Detic, DetCLIP, APE, T-Rex2, Grounded SAM, Roboflow, servidores de medios, RTMP/
HLS/SRT/RIST en prosa…). Dos verificaciones puntuales antes de que queden: (1) la
afirmación sobre GroundingDINO-B (COCO en su entrenamiento) se asentó **como hecho** y el
pase 1 la marcó **[R]**: confirmar contra el README oficial y citar esa entrada concreta;
(2) *Lee et al.* ("Surgical fine-tuning") es arXiv 2022 pero **ICLR 2023** — fijar el año
según la versión que se cite.

**E1-22 · 🟡 · El cuerpo ahora depende de la Tabla A.1.** §15.2.3 remite a *"la Tabla A.1
del Anexo A… matriz ampliada… modelos representativos según familia, mecanismo, métricas,
rendimiento y licenciamiento"* — y con las fichas podadas, **esa tabla es el único lugar
donde el estado del arte conserva su amplitud** (los ~25 modelos). PODA-17 proponía
eliminar el Anexo A. Ya no se puede: hay que **invertir PODA-17** — la Tabla A.1 se
conserva, se corrige (AJ-1.09, licencias de 1.5/DINO-X) y se le agregan las filas de los
modelos que salieron del cuerpo si no las tiene. → D-E1-7.

**E1-23 · proceso · El `.docx` llegó sin control de cambios ni bloque de trazabilidad.**
No hay forma de auditar qué se movió sin la extracción y el diff que hizo esta revisión.
Para la próxima iteración pedir **una de dos**: cambios controlados de Word, o el bloque
*diagnóstico · texto propuesto · trazabilidad* por unidad que INSTRUCCIONES exige.

---

## 4. Decisiones del equipo

| ID | Decisión | Recomendación | ✔ |
|---|---|---|---|
| D-E1-7 | PODA-17 (eliminar Anexo A) queda **invertida**: la Tabla A.1 se conserva y corrige, porque el cuerpo podado depende de ella para la amplitud del catálogo. Actualizar `ajustes/07` y la D-E1-4 del pase 1. | Sí. Es la forma de podar el cuerpo sin achicar el estado del arte. | [ ] |
| D-E1-8 | Referencias sostenidas solo por notas de tabla (Tabla 8: ~12 obras). ¿Se aceptan o se poda la Tabla 8 a las filas con prosa? | Aceptar: la Tabla 8 es la síntesis que §15.4.4 comenta, y APA admite la cita en tabla. Dejarlo declarado. | [ ] |

---

## 5. Instrucciones para la próxima iteración de GPT (en orden)

1. **Acabado de la poda** (sin cambiar el alcance de lo cortado): E1-13 renumerar y ficha
   breve de Florence-2 · E1-14 una oración por receta de la Tabla 4 y borrar la oración
   duplicada · E1-15 reescribir el arranque de §15.4.3.3 · E1-20 corregir las Fuentes de
   Tablas 3 y 5.
2. **Registro de tesis:** E1-16 (a) y (b) — brecha con cita, sin términos propios.
3. **Restituciones cortas:** E1-17 párrafo de licencias en §15.2.3 · E1-18 una oración de
   genealogía (GLIP) y una mención de *catastrophic forgetting*.
4. **E1-19** (E1-06 pendiente): introducción de §15.2.1 sin cifras.
5. **E1-21** delta de referencias completo + las dos verificaciones.
6. **Entregar con cambios controlados** (E1-23).

**Lo que NO hay que hacer:** volver a alargar. Ninguna de estas correcciones supera las
~600 palabras en total; el texto debe quedar en el orden de las 11.500. Y no volver a
aplicar E1-01…E1-12 ni los AJ- ya resueltos: están hechos.

---

## 6. ✎ Verificación de la nueva versión (2026-08-27, segunda iteración de GPT)

Se re-extrajo `Etapa 1 — copia ajustada E1 2026-08-27.docx` (segunda versión, 05:01) y se
hizo diff contra la primera. **10.870 → 10.725 palabras (−145): no volvió a alargar**, y
las restituciones pedidas se pagaron con la compresión de la introducción (E1-19).

| Unidad | Estado | Verificación |
|---|---|---|
| E1-13 numeración · ficha Florence-2 | ✅ | Bloque A renumerado **.1/.2**; Bloque D gana **15.2.1.4.1 Florence-2** (DaViT, seq2seq, FLD-5B 126 M imgs / 5,4 mil M anotaciones, 37,5 mAP COCO zero-shot, MIT — cifras correctas) |
| E1-14 Tabla 4 sin sostén | ✅ 10/11 | La prosa ya nombra MixedGroundingDataset, MultiModalDataset, reparametrización sin RepVL-PAN, LoRA (Rasaee), OWL-ST/n-gramas, Florence-2 LoRA (Ucar). Oración duplicada eliminada. **Residual R1** abajo |
| E1-15 §15.4.3.3 | ✅ | Arranca "Aun cuando la literatura describe los roles del servidor de medios… (§15.4.2)" |
| E1-16 registro de tesis | ✅ | (a) §15.3.3 cierra "la evaluación de un sistema asistivo exige niveles adicionales, cuya definición corresponde al protocolo experimental" — sin "estado por persona" ni "alerta temporal producida por la plataforma". (b) §15.3.2.1 cita Adžemović (2025) y Wojke et al. (2017), ya no enumera nuestros criterios, y cierra "por sí sola, no determina la elección de un tracker" |
| E1-17 licencias | ✅ | Párrafo nuevo en §15.2.3: GPL/AGPL vs Apache vs API cerrada; "distinguir entre licencia del código, licencia de los pesos y condiciones del servicio" — con 6 citas |
| E1-18 genealogía · término | ✅ | "Grounding DINO extiende la formulación de detección como phrase grounding introducida por GLIP (Li et al., 2021)"; "olvido catastrófico (catastrophic forgetting)… (Kirkpatrick et al., 2017)" |
| E1-19 (ex E1-06) intro sin cifras | ✅ | Los cuatro párrafos de paradigmas reescritos **sin ninguna cifra**; las cifras viven solo en las fichas |
| E1-20 Fuentes de Tablas 3 y 5 | ✅ | T. Zhao fuera de Tabla 3; Zhou 2022a fuera de Tabla 5 |
| E1-21 citas nuevas | ✅ parcial | IDEA-Research pasa a **2024c** — correcto: por orden APA de títulos, 2024a = DINO-X-API, 2024b = Grounded-SAM-2, 2024c = GroundingDINO. Lee → **2023** ✓. **La afirmación sobre Swin-B se verificó contra el README oficial** (`IDEA-Research/GroundingDINO`, tabla de checkpoints): fila GroundingDINO-B → Data `COCO,O365,GoldG,Cap4M,OpenImage,ODinW-35,RefCOCO`, box AP `56.7`; la T → `O365,GoldG,Cap4M`, `48.4 (zero-shot)`. **Exacto: deja de ser [R], es [P].** El delta de referencias sigue pendiente → R3 |
| E1-23 cambios controlados | ❌ | De nuevo cero `w:ins`/`w:del`, cero comentarios |
| No-anacronismo / fugas | ✅ | Cero identificadores de plataforma, cero andamiaje |

### Residuales (lo único que queda sobre el texto)

- **R1 · 🟡 · Tabla 4, fila "OWL-ViT/OWLv2 · Fine-tuning end-to-end con regularización · Parcial".** Es la única fila que la prosa ya no sostiene: "regularización" aparece solo en la tabla. Una oración en el párrafo de dual-encoders (*"el ajuste sobre datasets cerrados exige regularizar para no colapsar el espacio de embeddings compartido, Minderer et al., 2022"*) o eliminar la fila.
- **R2 · 🟡 · Formato de la ficha nueva.** Florence-2 lleva el rótulo "Arquitectura, entrenamiento y disponibilidad." **sin negrita**; las demás fichas usan rótulos en negrita. Y el punto quedó inconsistente entre fichas ("**Arquitectura base.**" vs "**Arquitectura base**."). Unificar al aplicar al maestro.
- **R3 · 🟠 · Delta de referencias, todavía no entregado.** Verificado contra `96e`: **existen** AILab-CVC 2024, Google 2022/2023, Kirkpatrick 2017, Li L. H. 2021 (GLIP), Microsoft 2024, THU-MIG 2025, IDEA-Research 2024a/c, Adžemović, Rasaee, Ucar. **No existen** y hay que darlas de alta en APA 7: *Kumar et al. (2022)* · *Lee et al. (2023)* · *OASIS (2019)* · *Ultralytics (2026)*. **Corregir** *Luxonis (s. f.)* → la entrada de `96e` es **"Luxonis. (s. f.-b). OAK-D Pro PoE"** — lleva letra. Y las **bajas** de PODA-18 (todo lo que dejó de citarse: OV-DETR, OV-DINO, OmDet, Detic, DetCLIP, Grounded SAM/SAM 2, OVTrack, Roboflow, Janus/Kurento/OME/SRS, RTMP/HLS/SRT/RIST en prosa, MEC…) — cuidando que lo citado solo en la nota de la Tabla 8 **se conserva** (D-E1-8).
- **R4 · proceso ·** tercera entrega sin cambios controlados. Si la próxima vuelve sin ellos, el equipo audita por extracción y diff como hasta ahora — funciona, pero cuesta una pasada.

**Estado del §15 al 2026-08-27 (noche): pase 1 y pase 2 APLICADOS Y VERIFICADOS**, salvo
R1–R3. El texto base del kit se re-extrajo de esta versión (`90d`). Lo que sigue de la Etapa
1 es **§16 y el Anexo A** (D-E1-2, D-E1-7).

---

## 7. Fuentes de esta revisión

Extracción de ambos `.docx` con `herramientas/extraer_informe.py` (2026-08-27); conteo de
palabras por encabezado numerado; diff textual por sección; búsqueda de identificadores de
plataforma y de andamiaje (cero hallazgos); verificación de citas nuevas contra los títulos
publicados. Pase 1: `correcciones-etapa-1.md`. Crítica de extensión: `ajustes/07`.
