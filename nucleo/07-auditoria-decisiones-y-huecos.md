# Auditoría crítica: decisiones tomadas, contraargumentos y huecos detectados

- **Fecha:** 2026-07-06
- **Propósito:** segunda pasada adversarial sobre todo el set de documentos (01–06).
  Cada decisión se ataca con su contraargumento más fuerte, se identifica qué la
  invalidaría, y se registran los huecos que ningún documento cubría. Las correcciones
  marcadas ✎ ya fueron aplicadas a los documentos correspondientes.

## Parte I — Crítica de las decisiones explícitas (D1–D6)

### D1 — Protocolo E-IND vs E-DIR (doc 04)

**Lo decidido:** fork empírico pre-registrado; E-IND favorita a priori.

**Contraargumentos y debilidades encontradas:**

1. **El matching de Fase 1 estaba mal especificado para E-DIR-obs.** El protocolo
   decía "matchear detecciones de frase por IoU≥0.5 con personas GT". Eso funciona
   para frases persona-céntricas ("person without hard hat" → caja de persona), pero
   una detección `bare_head` es una caja de *cabeza*: su IoU contra la caja de la
   persona completa es estructuralmente bajo (~0.05–0.15) y el criterio la habría
   descartado siempre — **sesgando el experimento contra E-DIR-obs**, justo la
   variante que el prior ya castiga. ✎ Corregido en doc 04 §7 Fase 1: matching por
   variante (frase-persona: IoU≥0.5; frase-parte: centro de la detección dentro de
   la región superior del bbox de persona).
2. **Potencia estadística no considerada.** BENCH tiene 196 imágenes; lo que importa
   no es el total de personas sino cuántas están *sin* casco/chaleco (la clase
   positiva del estado). Si son pocas decenas, un ΔF1 de 0.05 (el umbral de "empate
   técnico" del §8) queda dentro del ruido. ✎ Agregado a doc 04: reportar conteos por
   clase de estado e intervalos por bootstrap; si n<30 por condición, el criterio de
   empate se ensancha y la Fase 2 (clips) pesa más en la decisión.
3. **Calibrar y evaluar sobre el mismo conjunto.** El doc decía "calibrar sobre
   partición de calibración (no BENCH)" pero los atributos `has_helmet/has_vest`
   **solo existen en BENCH** — no había con qué calibrar fuera de él. ✎ Corregido:
   partición estratificada de BENCH en mitades calibración/test, declarada en la
   configuración de corrida.
4. **Escenario no contemplado: que ninguna estrategia sirva para CR-02.** Si el
   recall de `vest` es bajo (E-IND genera FP de alerta) y las frases de chaleco
   fallan (E-DIR), el protocolo no decía qué hacer. ✎ Agregada contingencia: el
   núcleo mínimo defendible es CR-01 completo + CR-02 reportado con sus límites —
   eso también es un resultado, no un fracaso del experimento.
5. **Atajo disponible no aprovechado en el plan:** las corridas de Sprint 2 sobre
   BENCH probablemente siguen en disco (`runs/`) — la Fase 1 de E-IND puede
   puntuarse **sin re-inferir**, solo con scoring offline. Ahorra días.
6. **Sesgo del auditor:** el prior pro-E-IND lo escribió quien implementó E-IND (yo,
   sobre el código existente). Mitigación real: los criterios están fijados antes de
   correr y el gate le da a E-DIR una vía de supervivencia objetiva. Aún así,
   conviene que las formulaciones E-DIR del prompt set las revise el usuario antes
   de correr (que nadie pueda decir que se eligieron frases débiles a propósito).

**Veredicto:** la decisión de resolver D1 empíricamente sobrevive; el protocolo
tenía dos fallas reales (1 y 3) que habrían viciado el resultado. Corregidas.

### D2 — Granularidad G0 (escena) como núcleo

**Contraargumentos:**

1. **Pérdida semántica real:** "hay alguien sin casco" vs "este trabajador estuvo
   8 s sin casco". Para el caso asistivo es suficiente (la alerta orienta atención
   humana, no sanciona individuos — y de hecho refuerza la línea ético-legal del
   TFG: menos individualización = menos tensión con privacidad). Pero hay que
   decirlo de frente en el informe, no esconderlo.
2. **SDR y duración de episodio se contaminan** si distintas personas alternan la
   condición dentro del mismo episodio de escena (A sin casco sale, entra B sin
   casco → un solo episodio largo). Limitación declarable; G1 la resuelve.
3. **Costo de migración subestimado en el doc 03:** no es solo la clave del motor —
   el fixture temporal (`worker_a/b/c`), su ground truth y los tests están escritos
   a nivel sujeto. Hay que regenerar GT a nivel escena-condición y adaptar la eval.
   Sigue siendo chico (~1–2 días), pero no es "un cambio de clave".
4. **Alternativa no descartable:** tracker IoU-greedy son ~100 líneas; ¿por qué no
   G1 directo? Porque agrega una fuente de error nueva (ID switches) que habría que
   medir con GT de identidad que no existe, y el clip bench se encarecería (anotar
   identidades). G0 primero sigue siendo lo correcto con 12 semanas; G1 sobre 2–3
   clips si sobra agenda.

**Veredicto:** sostenida, con la limitación 2 declarada y el costo 3 presupuestado.

### D3 — Bus ZeroMQ PUB/SUB, broker diferido

**Contraargumentos:**

1. **PUB/SUB pierde mensajes por diseño** (slow joiner: lo publicado antes de que el
   suscriptor conecte se pierde; HWM: descarta bajo backpressure). Para el
   control-plane un evento perdido = un hit menos = una alerta potencialmente
   distinta entre live y replay. Mitigaciones concretas que faltaban por escrito:
   (a) orden de arranque — control-plane suscripto **antes** de iniciar el run;
   (b) contador de secuencia por `unit_id` para *detectar* pérdidas y reportarlas
   como métrica (encaja con la política de "corrida degradada" de Etapa 3);
   (c) el JSONL sigue siendo la verdad: toda corrida live es re-evaluable offline y
   la comparación live-vs-replay es en sí un resultado de robustez. ✎ Agregado al
   doc 03 (D3, inclinación posterior).
2. **Incoherencia aparente ZeroMQ + MQTT** ("¿por qué dos tecnologías de
   mensajería?"). Defensa preparada: son tramos con requisitos opuestos — media→
   control es interno, de alta tasa y sin broker como dependencia de la ruta
   crítica; alertas→consumidores es externo, de baja tasa, donde MQTT es el
   estándar de integración IoT. Un solo broker MQTT para ambos tramos sería
   técnicamente posible pero pondría un broker en la ruta crítica de video,
   contradiciendo DA-01/DA-02.
3. **¿Y si el tribunal pregunta por Kafka?** La respuesta ya está escrita (DA-03:
   el log es la durabilidad, el bus transporta; seam `BrokerSource` documentado).
   Riesgo residual bajo.

**Veredicto:** sostenida, con las mitigaciones de pérdida ahora explícitas.

### D4 — Manifiesto paraguas + experiment_id

**Contraargumentos:**

1. **¿Quién orquesta?** Propagar el id es trivial; lo no trivial es qué componente
   lanza las dos corridas con el mismo `experiment_id`. Riesgo de scope creep: que
   la webconsole mute en orquestador de plataforma. Contención: un **runner script**
   en experimental-setup (CLI, ~100 líneas: lee manifiesto → POST /api/runs →
   espera → dispara control-plane → escribe report) es suficiente para la tesis;
   la webconsole solo *lee*.
2. **Riesgo de sobre-diseño del manifiesto:** no inventar un schema nuevo grande;
   el manifiesto paraguas referencia los archivos de config existentes + ids.

**Veredicto:** sostenida con la contención de alcance explícita (runner CLI, no
servicio nuevo).

### D5 — MQTT como canal

**Contraargumentos:**

1. La justificación original ("por su velocidad") es débil académicamente — la
   latencia de cualquier canal es despreciable frente al tramo de percepción. Las
   razones defendibles son: peso mínimo (Mosquitto ~10 MB en el compose), estándar
   de integración IoT (Tabla 48 de Etapa 3 lo lista explícitamente), y medición
   limpia de `t-alert-notification` sin la variabilidad de una API externa. ✎ Así
   quedó redactado en el ADR del doc 03.
2. MQTT QoS 1 puede duplicar entregas → el ledger de idempotencia del diseño 06 deja
   de ser opcional incluso en la versión recortada. Costo ya presupuestado.
3. Con MQTT no hay "demo visual" del canal (a diferencia de Telegram). Mitigación:
   la webconsole muestra las alertas; para la defensa, un `mosquitto_sub` en vivo en
   una terminal es suficiente y hasta más "de ingeniería". Nota posterior: la
   consolidación metodológica del informe lista MQTT explícitamente como componente
   del tramo de notificación (doc 08 §1.5) — la decisión quedó, además, alineada con
   el protocolo.

**Veredicto:** sostenida.

### D6 — Reporte consolidado con estados de aplicabilidad

**Contraargumentos:** casi ninguno — es la decisión más barata y rentable del set.
Único riesgo: sobre-ingeniería. Contención: es **un script** que junta summaries +
evals y emite `report.json` + `report.md`; no un servicio, no una base de datos.

**Veredicto:** sostenida.

## Parte II — Crítica de las decisiones implícitas

### I1 — "Won't: fine-tuning/TN" (doc 02 §5)

El riesgo real no es el fine-tuning en sí: es que el tribunal pregunte **"¿cómo sabés
que un detector supervisado cerrado no haría esto mejor y más barato?"**. R1 compara
OVD-vs-OVD, no OVD-vs-supervisado. Mitigaciones sin romper el won't: (a) citar los
resultados supervisados publicados sobre los datasets fuente (CHV, etc.) como
referencia contextual; (b) el argumento arquitectónico — el vocabulario es
extensible por configuración sin reentrenar, que es la tesis de la plataforma;
(c) declararlo límite explícito. Si en la semana 9 sobrara tiempo (improbable), un
YOLO supervisado sobre train_v2 sería la extensión de mayor valor — pero no debe
prometerse.

### I2 — Plan de 12 semanas (doc 02 §7)

1. **La escritura está subpresupuestada:** 2 semanas finales para capítulos de
   Etapa 4/5 + resultados es optimista. Corrección de proceso: **escritura
   incremental desde la semana 5** — cada experimento cierra con su sección
   redactada (los docs de este set ya son borrador de Etapa 4); las semanas 11–12
   son de integración y pulido, no de redacción desde cero.
2. **No hay slack:** 12 semanas justas hasta ~fin de septiembre. El plan ya ordena
   por dependencia dura (clip bench primero); si algo se cae, lo primero
   sacrificable es G1, luego la segunda vuelta de calibración — nunca R3 ni R4.
3. El congelamiento de campaña en semana 10 debería tratarse como semana 9 si la
   escritura viene atrasada.

### I3 — El norte R1–R4 (doc 02 §6)

**R4 tiene una tensión de modelo no resuelta** (hueco H5 abajo): GDINO-tiny es el
mejor en calidad pero lento para "tiempo real" percibido; YOLOE-26l es rápido pero
no detecta vest (mata CR-02 y a E-IND parcialmente). Ninguna elección es mala si se
declara: Etapa 3 dice explícitamente que el objetivo no es maximizar FPS sino hacer
interpretable el comportamiento (§17.3.7.3). Pero hay que decidirlo, no descubrirlo
en la semana 7.

### I4 — "Un solo código, caminos como configuración"

Sigue siendo correcta. Único matiz: el evaluador `direct_evidence` y la fusión E-HYB
sí son código nuevo (chico). La frase precisa es "ramas como configuración **más
extensiones aditivas acotadas**" — nada se bifurca, todo se agrega.

### I5 — Organización documental (esta misma)

La numeración de lectura (00–07, 90) prioriza comprensión sobre cronología — las
fechas viven dentro de cada doc. Riesgo: números pegados si aparecen docs
intermedios; aceptado (hay huecos 08–89 disponibles). El índice 00 es el único punto
de entrada a mantener.

## Parte III — Huecos detectados (nadie los tenía escritos)

| # | Hueco | Corrección / decisión pendiente |
|---|---|---|
| H1 | Matching de Fase 1 sesgado contra `bare_head` (cajas de cabeza vs IoU con persona). | ✎ Corregido en doc 04 (matching por variante). |
| H2 | **Origen de los clips del clip bench sin resolver.** Los datasets del repo son de *imágenes*; no hay videos con episodios CR-01/CR-02. Descargar de internet mete licencias y privacidad. | Propuesta: **grabación propia escenificada** (persona con/sin casco y chaleco, guionada: N segundos sin EPP → se lo pone → sale de cuadro). Encaja literalmente con el EBE "captura en entorno controlado" de Etapa 3, resuelve licencia y consentimiento, y permite GT temporal exacto por diseño del guion. Complementar con 2–3 clips CC de obra real si aparecen con licencia clara. Registrar todo en `license_registry`. **Update 2026-07-09 (doc 01 §12.3):** parcialmente resuelto — el equipo ya usa videos reales de obra (`video1.avi` Intel … `video5`) en los experimentos HF de la rama `mati`; están en el entorno del compañero (git-ignorados). Falta: obtenerlos/coordinarlos, GT temporal de episodios, y registrar licencia del dataset Intel en el registry. La grabación escenificada sigue vigente para los casos guionados (V1–V3) y el GT exacto. |
| H3 | Calibración sin datos (atributos solo en BENCH). | ✎ Corregido en doc 04 (mitades calib/test de BENCH). |
| H4 | **Fuente viva para EBE sin definir** (OAK-D no disponible). | RTSP sintético: `mediamtx` + `ffmpeg -stream_loop` sirviendo los clips del clip bench como stream en vivo, y/o webcam USB. Tabla 55 de Etapa 3 admite explícitamente "archivo simulado como stream". Cero hardware nuevo; el mismo clip sirve para DBE (archivo) y EBE (stream) → comparación DBE-vs-EBE con fuente idéntica, que es un resultado extra gratis. |
| H5 | **Modelo para la demo EBE (R4) sin decidir**: GDINO (calidad, lento) vs YOLOE (rápido, sin vest). | Decisión propuesta: GDINO-tiny con rate-gate y FPS efectivo declarado (la narrativa de Etapa 3 lo respalda); medir en semana 7 y, si el FPS es indefendible (<1–2), demo CR-01-only con YOLOE como variante documentada. Registrar como mini-ADR en semana 7. |
| H6 | Pérdida de mensajes del bus (slow joiner, HWM) sin mitigación escrita. | ✎ Agregado al doc 03/D3: orden de arranque, contador de secuencia, drops como métrica, re-eval offline como red. |
| H7 | Contingencia "CR-02 no funciona con ninguna estrategia". | ✎ Agregada al doc 04 §8: núcleo mínimo defendible = CR-01 + CR-02 con límites declarados. |
| H8 | Consentimiento/licencias de evidencia visual del clip bench. | Cubierto por H2 (grabación propia + registry). Extender `license_registry.md` con la categoría "clips temporales". |
| H9 | Escritura del informe concentrada al final. | Corrección de proceso en I2: sección redactada al cierre de cada experimento desde semana 5. |
| H10 | **La documentación de `projects/docs/` no está versionada** (el workspace no es un repo según CLAUDE.md, aunque existe un `.git` vacío en la raíz — inconsistencia en sí misma). Riesgo de pérdida del set completo. | Decisión del usuario pendiente: (a) versionar `docs/` en un repo propio, o (b) moverla al repo del informe/TFG. Recomendado (a) ya mismo. Sin commit hasta que lo pidas — regla del workspace. |
| H11 | Las 3 preguntas abiertas del doc 06 (§20) quedaron sin dueño. | Cerradas por decisiones posteriores: Q1 plantilla de notificación → fija en código (recorte D5); Q2 alcance dashboard → absorbido por webconsole (D5); Q3 `t-alert-notification` en DBE → wall-clock etiquetado DBE o N/A (política D6). ✎ Reflejado aquí; el doc 06 se conserva como diseño original sin editar. |

## Parte IV — Qué queda genuinamente abierto después de esta auditoría

1. Formalizar los ADRs D2–D6 (recomendaciones listas; son ~1 hora de escritura).
2. Correr el experimento D1 (semanas 3–4) — con el protocolo ya corregido.
3. Mini-ADR H5 (modelo EBE) en semana 7 con datos de FPS.
4. Decisión H10 (dónde versionar esta documentación) — única decisión nueva que
   introduce esta auditoría y requiere al usuario.
