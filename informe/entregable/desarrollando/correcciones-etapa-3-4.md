# Correcciones para cerrar §17.3 (Diseño Arquitectónico) y §17.4 (Implementación)

**Fecha:** 2026-08-19 · **Insumos:** `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v0.1.docx`,
`E-OVRT-VDP_Seccion_17.4_Implementacion_v0.1.docx`, `observaciones-etapa-3-4.txt` (41 comentarios, todos resueltos acá).
**Verificación:** todos los valores citados fueron contrastados contra los repos el 2026-08-19 (ver §D).
**Este archivo es fuente del project-kit** (etapas 3 y 4): al cambiar algo acá, regenerar el kit.
La sección §E da la renumeración de tablas y figuras que resulta de aplicar todo lo anterior.

---

## Decisiones firmadas (rigen todo el documento)

- **D1 — Término único:** el evento que publica el plano de medios se llama **"evento de percepción"**
  (denominación de diseño: *PerceptionEvent*). El nombre *DetectionEvent* se elimina del informe.
  El contrato que lo materializa se llama por su id: `media.detection.v1`.
- **D2 — Doctrina de reparto entre etapas:** §17.3 es **conceptual y paramétrico** — patrones de acople y
  tecnologías elegidas CON su justificación (son decisiones de diseño), pero **sin puertos numéricos, sin
  tablas de endpoints, sin tabla de correspondencia diseño→materialización y sin valores numéricos del
  patrón**. §17.4 es **concreto y efectivo** — puertos, endpoints, correspondencia, vista de procesos
  (FIG-A) y valores efectivos de configuración. Excepción coherente: la **máquina de estados (FIG-E) es
  diseño** → vive en §17.3.8.2; §17.4 la referencia sin repetirla.
- **D3 — Códigos de estrategia:** se agrega un mini-ajuste en **§17.1.5.4.2** que bautiza E-DIR / E-IND /
  E-HYB (ver §C-1). §17.3/§17.4/§17.5 los usan con un recordatorio breve al primer uso.
- **D4 — Justificación del núcleo-solo:** párrafo dedicado en **§17.4.10** + eco breve en las conclusiones.
  La justificación **nunca** es "falta de tiempo" (ver E4-17).
- **Regla de autocontención (GUIA §3.1):** el informe no referencia documentos locales, ADRs, fichas ni
  índices del repositorio. Todo texto sugerido acá ya cumple esa regla; no agregar citas internas.
- Los "textos guía" son orientativos: ChatGPT puede reformularlos manteniendo el contenido y el registro
  académico del informe (decimales con coma; milisegundos como "4.000 ms").

---

## A. Correcciones a §17.3 — Diseño Arquitectónico

### E3-01 · §17.3.3.1, Tabla 40 — justificación del núcleo-solo *(obs 2 / comentario C0)*
**Sin cambio en 17.3.** La justificación de por qué solo se implementó el núcleo validable se desarrolla
en §17.4.10 (ver E4-17). Opcional: no agregar nada acá; la Tabla 40 ya declara el tratamiento de cada
capacidad.

### E3-02 · §17.3.3.4, Tabla 43 — eliminar la columna "Estado" *(obs 3 / C1)*
Todas las filas dicen "Adoptada": la columna no discrimina nada.
1. Eliminar la columna **Estado**.
2. En DA-11, quitar la marca "(opcional)": el texto de la decisión ya dice "variante opt-in… deshabilitada
   por defecto".
3. Reescribir la Nota (hoy menciona "decisiones condicionadas" que ya no existen en la tabla).
   **Texto guía:** *"Nota. Las decisiones fijan reglas estructurales adoptadas para el diseño del prototipo
   experimental. Su materialización y verificación se documentan en la sección 17.4."*

### E3-03 · §17.3.5 — quitar "webconsole" y "runner" del diseño *(obs 4 / C2)*
En diseño, los nombres concretos quedan sin contexto. Reemplazar en el párrafo del comentario C2:
*"la webconsole y el runner no consumen directamente los buses"* →
**"la interfaz de inspección y el orquestador experimental gobiernan el ciclo de vida mediante las
interfaces de gobierno de cada módulo y no consumen directamente los buses"**.
Aplicar el mismo criterio en §17.3.10.2 (*"la webconsole y el runner lo gobiernan…"* → *"la interfaz de
inspección y el orquestador experimental lo gobiernan…"*). Los nombres concretos (webconsole, runner) se
introducen recién en §17.4.1 como materialización del soporte experimental.

### E3-04 · §17.3.5 — reescribir el párrafo de materialización: sin puertos y CON justificación de tecnologías *(obs 5 y 6 / C3)*
El párrafo actual ("La materialización de esta vista distingue dos patrones…") enumera puertos
(:8080/:8081/:8082/:5557/:5558) — eso migra a §17.4 (D2). En su lugar, el diseño debe **justificar** la
elección de cada tecnología. **Texto guía (reemplaza el párrafo completo):**

> *"La materialización de esta vista distingue dos patrones de acople complementarios. El gobierno de las
> corridas se realiza mediante interfaces HTTP gobernadas por configuración en los tres módulos
> ejecutables. Se adopta HTTP porque el ciclo de vida de una corrida —crear, consultar, cancelar, cerrar—
> tiene semántica de solicitud y respuesta, admite múltiples clientes sin acoplarlos entre sí y permite
> disponer los módulos en un mismo host o en hosts distintos sin modificar su lógica; el gobierno por
> configuración garantiza que cada corrida declare sus parámetros en lugar de heredarlos de constantes
> ocultas. El intercambio de datos en ejecución se realiza mediante un bus ZeroMQ con patrón
> publicador-suscriptor y serialización binaria msgpack: un canal de detecciones entre los planos y un
> canal de alertas hacia la distribución. Se adopta ZeroMQ porque ofrece transporte de baja latencia sin
> requerir un broker como dependencia adicional del prototipo, y el patrón publicador-suscriptor desacopla
> al productor de sus consumidores sin bloquear la ruta crítica; msgpack reduce el costo de serialización
> respecto de texto plano conservando estructuras autodescriptivas. La durabilidad no se le exige al canal:
> cada hecho se persiste en archivos JSONL de sólo adición antes de publicarse, de modo que la evidencia
> pueda releerse y reevaluarse sin depender de la mensajería. La persistencia JSONL cumple esa función de
> durabilidad y relectura —inspeccionable, de sólo adición y sin introducir una base de datos como
> dependencia del núcleo— y no constituye un tercer patrón de acople. HTTP gobierna configuración y ciclo
> de vida; el bus transporta hechos de ejecución."*

### E3-05 · Figura 4.2 (vista de procesos) — mover a §17.4.1 *(obs 6 / C4)*
La vista de procesos con puertos es concreción de implementación (D2) y §17.4.1 ya tiene el placeholder de
esa misma figura. Acciones:
1. Eliminar de §17.3.5 la Figura 4.2 con su nota (van a §17.4.1, ver E4-02).
2. §17.3 conserva solo la Figura 4.1 (vista conceptual).
3. Renumerar las figuras siguientes de §17.3 (mapa completo en §E).
4. Enmienda al plan de figuras: FIG-A tiene destino único §17.4.1 (ver §C-2).

### E3-06 · §17.3.6.2 — "ejecución experimental": ya resuelto *(obs 7 / C5)*
Sin cambio: el término quedó bien definido acá (unidad lógica identificada por `experiment_id`).
El rezago de "corrida paraguas" está en §17.4 (ver E4-15).

### E3-07 · §17.3.6.4 — recordatorio de las estrategias al primer uso *(obs 8 / C6)*
Depende del mini-ajuste en §17.1.5.4.2 (§C-1). En §17.3.6.4, donde dice *"…se mantienen en conjuntos
separados para E-DIR y E-HYB…"*, anteponer el recordatorio:
**"…para las estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica
(§17.1.5.4.2)…"**. La Tabla 39 y la Tabla 45 pueden seguir usando los códigos sin glosa (la prosa ya los
ancló). En §17.3.9.2 mantener la expansión que ya existe ("estrategia indirecta basada en evidencia
positiva con inferencia espacial de ausencia (E-IND)") — está bien como está.

### E3-08 · §17.3.8.2, Figura 4.5 — la máquina de estados queda ACÁ; limpiar el placeholder doble *(obs 9 / C7)*
Decisión D2: FIG-E es diseño → vive en §17.3.8.2. Acciones:
1. La figura tiene hoy DOS notas (la spec provisoria "La figura deberá representar…" y la nota final).
   Dejar **una sola figura con una sola nota** (conservar la nota final, que es la definitiva).
2. La figura se dibuja con los **cinco estados**: inactive → candidate → confirmed → sustained → resolved
   (verificado contra el motor; ver §D).
3. En §17.4.3 se elimina el placeholder duplicado y se referencia esta figura (ver E4-04).
4. Enmienda al plan de figuras: FIG-E destino §17.3.8.2 (ver §C-2).

### E3-09 · §17.3.8.3 y Tabla 46 — el motor se DISEÑA acá; los valores numéricos migran a §17.4.6 *(obs 10 y 11 / C8, C9)*
Respuesta a la duda de fondo: **§17.3.8.3 se queda** — desarrolla el motor como diseño (qué evalúa, con qué
reglas, con qué estados y granularidad), que es exactamente lo que corresponde a la etapa 3. Lo que NO
corresponde son los **valores numéricos efectivos**, que ya están duplicados en §17.4.6 (D2). Acciones
sobre la Tabla 46:
1. Fila "Criterio temporal": *"Confirmación: 4000 ms para PR-01 y 7000 ms para PR-02"* →
   **"Ventana de confirmación expresada en milisegundos, declarada por patrón."**
2. Fila "Histéresis y cierre": quitar los valores →
   **"Ventana de resolución expresada en milisegundos, declarada por patrón."**
3. Fila "Umbrales y precondiciones de evidencia": quitar los valores →
   **"Confianza mínima del sujeto y del EPP, y área mínima del sujeto, declaradas por patrón; umbrales de
   postproceso declarados en la configuración del plano de medios."**
4. Fila "Región de evaluación": quitar los porcentajes →
   **"Franja vertical y margen lateral relativos a la caja del sujeto, declarados por patrón (región
   cefálica para PR-01; torso para PR-02)."**
5. Fila "Severidad configurada": quitar high/medium →
   **"Severidad conceptual asignada por patrón desde el catálogo metodológico."**
6. Reescribir la Nota: **"Nota. La tabla define los componentes de una definición de patrón de riesgo. Los
   valores adoptados para el núcleo validable se documentan junto a la configuración efectiva en la
   sección 17.4.6. Los tiempos se expresan en milisegundos para conservar su significado ante distintas
   cadencias de procesamiento."**
7. Verificar que §17.4.6 conserve TODOS los valores desplazados (ya tiene ventanas y severidades; agregar
   los umbrales de evidencia del patrón y las regiones — ver E4-11).
8. Ajustar la frase que introduce la tabla en §17.3.8.2 (*"Los parámetros efectivos del núcleo, incluidos
   los criterios espaciales de CR-01 y CR-02, se sintetizan en la Tabla 46"*), que quedaría falsa sin los
   valores → **"Los componentes de una definición de patrón, incluidos los criterios espaciales de CR-01
   y CR-02, se sintetizan en la Tabla 46; los valores adoptados para el núcleo se documentan en la
   sección 17.4.6."**

### E3-10 · §17.3.10 — reescribir la apertura de la distribución para engancharla con la cadena *(obs 12 / C10)*
El problema es que §17.3.10.1 arranca en seco. **Texto guía para un párrafo puente inicial (antes del
contenido actual de 17.3.10.1):**

> *"La cadena descripta hasta aquí termina en un hecho interno: el plano de control registra una alerta
> cuando un patrón confirma un episodio. Falta el último tramo: hacer llegar esa alerta a un canal externo
> sin comprometer al motor que la produjo. De ese tramo se ocupa el módulo de distribución. El plano de
> control publica cada alerta confirmada en un bus de alertas dedicado; el módulo de distribución la
> consume desde allí, aplica la política de notificación y registra el resultado de cada intento de
> entrega. No forma parte del razonamiento del patrón ni constituye un tercer plano: es un módulo
> desacoplado que transforma una alerta ya confirmada en intentos de entrega observables."*

Además, por D2, en §17.3.10.2 quitar los puertos: *"El dato de distribución viaja por el bus de alertas
:5558. El módulo expone una interfaz HTTP config-driven en :8082…"* → **"El dato de distribución viaja por
el bus de alertas dedicado. El módulo expone su propia interfaz de gobierno para crear, consultar, cancelar
y cerrar corridas de entrega…"**. La Tabla 48 se conserva (es diseño: consumidores y salidas).

### E3-11 · §17.3.10.3 — aclarar qué es "el motor" *(obs 13 / C11)*
Reescribir: *"El motor posee una capacidad técnica de control de re-confirmación, pero no se utiliza como
política del núcleo"* → **"El motor de patrones del plano de control posee una capacidad técnica de
control de re-confirmación, pero la decisión de diseño adoptada no la utiliza en el núcleo: la supresión
de re-notificación —cooldown, agrupación o limitación de tasa— pertenece a la política del módulo de
distribución."** (Y eliminar la oración siguiente que quedaría redundante.)

### E3-12 · Tabla 50 — término único del evento *(obs 14 / C12)*
Fila "DetectionEvent" → **"PerceptionEvent"** (misma función y contenido; la columna de información mínima
sigue citando `media.detection.v1`). Con D1 no debe quedar ninguna aparición de "DetectionEvent" en §17.3.

### E3-13 · §17.3.11.3 — eliminar la Tabla 61 y la Tabla 62 de §17.3 *(obs 14 y 15 / C13, C14)*
Por D2, la correspondencia diseño→materialización (Tabla 61) y el inventario de interfaces con puertos
(Tabla 62) pertenecen a §17.4 (allí ya existen; ver E4-05/E4-06). Acciones:
1. Eliminar de §17.3.11.3 la Tabla 61 completa (con eso desaparece también el comentario C13).
2. Eliminar la Tabla 62 completa. Las dos filas de buses y las filas de distribución que solo estaban acá
   se incorporan a la Tabla 62 de §17.4 (ver E4-06).
3. Conservar el párrafo *"El evento central del sistema es media.detection.v1…"* (es diseño del contrato).
4. Conservar las invariantes de `clip_gt.v2` y los cinco hitos temporales (párrafos posteriores).
5. Renumerar las tablas del capítulo tras la eliminación (mapa completo en §E — ojo: hoy los números de
   las Tablas 61–64 de §17.3 COLISIONAN con los de §17.4).

### E3-14 · §17.3.12.1 — mover el árbol de directorios `runs/` a §17.4 *(obs 16 / C15)*
El listado del repositorio por ejecución es materialización (D2) y hoy aparece en seco. Acciones:
1. Eliminar el bloque `runs/<experiment_id>/ …` de §17.3.12.1; la prosa de principios (sólo adición, sin
   sobrescritura, agrupación por `experiment_id`) se conserva.
2. Incorporarlo en §17.4.7 como cuadro con introducción (ver E4-13).

### E3-15 · Tablas 52, 64 y 53 — VALIDADAS, sin cambios de fondo *(obs 17 / C16, C17, C18)*
Se verificó contra los repos: nombres de métricas y tramos, definiciones operacionales (G2A desde el
dequeue, capture_to_host solo con ancla temporal, SDR solo comparable a igual cadencia, re-alertas ≠ FP),
estados de aplicabilidad (computed / applicable_not_computed / not_applicable / not_interpretable) y los
esquemas `media.metric.v2` / `control.metric.v1`. Quitar los tres comentarios; no hay correcciones.

### E3-16 · §17.3.14 — abreviar el desarrollo DBE/EBE *(obs 18 / C19)*
La definición de los escenarios ya está en §17.1.3.3 y §17.1.4.4 (con las Tablas 19 y 20). Acciones:
1. Comprimir §17.3.14.1 y §17.3.14.2 a **un párrafo cada uno**, eliminando lo que repite la definición
   metodológica y conservando solo la lectura arquitectónica (DBE: fuente pulleable, prioridad de
   reproducibilidad; EBE: fuente viva, instrumentación de temporalidad). Abrir con una remisión:
   **"La definición metodológica de ambos escenarios corresponde a la sección 17.1.4.4; aquí se conservan
   únicamente sus consecuencias arquitectónicas."**
2. Conservar §17.3.14.3 (equivalencia arquitectónica) completo — es el aporte propio de esta etapa.
3. En la Tabla 54, eliminar las filas que no derivan una implicancia arquitectónica nueva ("Objetivo
   experimental" y "Riesgo principal" repiten metodología; conservar fuente, control temporal,
   instrumentación adicional, métricas prioritarias y condición de comparabilidad).
4. Conservar §17.3.14.5 y §17.3.14.6 (alcance arquitectónico y naturaleza temporal — son diseño).

### E3-17 · §17.3.14.5, Tablas 55 y 56 — eliminar el código "EN-2" *(obs 19 / C20, C21)*
El código EN-2 quedó huérfano: la tabla de modos del EN (EN-0/EN-1/EN-2) existía en la versión anterior de
la etapa 3 y desapareció en esta reescritura. Respuesta a "¿se utilizó?": la preselección está implementada
en el código (opt-in, deshabilitada por defecto, fail-open — verificado), pero quedó fuera de los
experimentos finales, así que no se reporta como resultado. Acciones:
1. §17.3.14.5: *"La variante EN-2 es opcional…"* → **"La variante de preselección liviana en el borde es
   opcional, deshabilitada por defecto y fail-open…"**
2. Tabla 55, fila "EN-2" → **"Preselección en el borde"** (mismo contenido).
3. Tabla 56, fila EN: *"La preselección EN-2 es opcional…"* → **"La preselección liviana es opcional…"**,
   y en la misma fila *"(modo base EN-1)"* → eliminar el código: **"EN (modo base de captura)"**.
4. Verificar que no quede ningún "EN-1"/"EN-2" en §17.3 ni en §17.4.

### E3-18 · Barrido final de puertos en §17.3 *(consecuencia de D2)*
Quitar todo puerto numérico restante:
- §17.3.8.1: *"por el canal de detecciones :5557"* → **"por el canal de detecciones del bus"**.
- §17.3.15 (prosa): *"gobernada por HTTP en :8082 y consumidora del bus de alertas :5558"* →
  **"gobernada por su propia interfaz HTTP y consumidora del bus de alertas"**.
- Tabla 56, fila Módulo de distribución: *"Servicio HTTP config-driven en :8082…"* →
  **"Servicio gobernado por configuración con interfaz HTTP propia, co-ubicable con el CPN o desplegable
  por separado"**; y en Responsabilidades: *"desde el bus :5558"* → **"desde el bus de alertas"**.
- Tabla 59, fila Tramo de distribución: *"Gobernar la corrida por HTTP en :8082, consumir control.alert.v1
  desde el bus :5558…"* → **"Gobernar la corrida por su interfaz HTTP, consumir control.alert.v1 desde el
  bus de alertas…"**.
- §17.3.18 (cierre) ya está sin puertos: no tocar.

---

## B. Correcciones a §17.4 — Implementación

### E4-01 · §17.4.1 — borrar las menciones a las CLI preliminares *(obs 23 / C0, C1)*
1. Eliminar: *"Sus utilidades históricas de línea de comandos se conservaron como herramientas auxiliares
   y dejaron de constituir la interfaz principal."*
2. Eliminar: *"la interfaz de línea de comandos se conservó para la relectura offline"* (la relectura DBE
   queda descripta por el modo replay del servicio; ver Tabla 62).

### E4-02 · §17.4.1 — la vista de procesos (FIG-A) se materializa ACÁ *(cierra E3-05)*
El placeholder ya existe. La figura incorpora los tres servicios con sus puertos (:8080, :8081, :8082),
el soporte experimental como cliente HTTP, el módulo de distribución **con línea continua** (es un servicio
más, no un apéndice), los dos buses (:5557 detecciones, :5558 alertas), el repositorio de corrida y el
orden de disparo. La nota que acompañaba a la Figura 4.2 de §17.3 se adapta como nota de esta figura.

### E4-03 · §17.4.1 — distribución como servicio HTTP *(obs 24 / C2)*
Reescribir el párrafo del módulo de distribución. **Texto guía:**

> *"El módulo de distribución de alertas constituye un cuarto componente funcional y no un tercer plano.
> Al igual que los dos planos, se ejecuta como un servicio gobernado por configuración con interfaz HTTP
> propia. Consume las alertas confirmadas desde el bus de alertas, aplica la política de notificación,
> controla idempotencia y supresión, entrega por MQTT con confirmación de calidad de servicio y conserva
> un registro de entregas de sólo adición (ledger). La vista de resultados de entrega y el lanzamiento
> desde la orquestación quedaron integrados."*

### E4-04 · §17.4.3 — eliminar el placeholder de la máquina de estados *(obs 9 / cierra E3-08)*
Eliminar el placeholder `[[FIGURA: máquina de estados…]]` y su marca. En el párrafo de
`control.pattern_state.v1`, referenciar: **"…las transiciones entre los estados inactive, candidate,
confirmed, sustained y resolved (figura de la sección 17.3.8.2)…"** — sin número hardcodeado: la figura
cambia de número con la renumeración de §E.

### E4-05 · Tabla 61 — reemplazar los "No aplica" por el mecanismo real de trazabilidad *(obs 25 y 26 / C3, C4, C5)*
No se inventan versiones nuevas en el código: el versionado de esos contratos existe por otros mecanismos y
la columna debe decir cuáles. Con la Tabla 61 de §17.3 eliminada (E3-13), esta pasa a ser la única.
1. Renombrar la columna **"Esquema o versión"** → **"Versionado y trazabilidad"**.
2. Reemplazos fila por fila:
   - SourceDefinition: "No aplica" → **"Esquema de configuración; congelado por el manifiesto"**
   - ModelProfile: → **"Catálogo versionado; un archivo por variante"**
   - PromptDefinition: → **"prompt_set_id registrado en cada corrida"**
   - FrameMetadata: → **"Contrato interno; viaja dentro del evento publicado"**
   - PatternDefinition: → **"Conjunto de patrones versionado (pattern set)"**
   - ErrorEvent: → **"Esquema por componente, registrado por corrida"**
   - Repositorio de eventos: → **"Esquemas de cada evento persistido"**
   - Reporte experimental: → **"Proyección regenerable de los artefactos primarios"**
3. Fila "PerceptionEvent / DetectionEvent" (D1): la denominación de diseño queda **"PerceptionEvent"**, la
   materialización **"Evento de percepción normalizado"**, versión `media.detection.v1`.
4. La Nota se simplifica: ya no hay "sin versión propia".

### E4-06 · Tabla 62 — única tabla de interfaces del informe *(obs 27 y 28 / C6, C7)*
1. **Eliminar la fila** "GET /healthz y GET /readyz" (acordado con tu colega).
2. **Agregar las filas de distribución (:8082):** `POST /api/runs` (inicia una corrida de entrega con
   fuente de alertas, política, canal e identificador de experimento); `GET /api/runs/{id}` (estado);
   `POST /api/runs/{id}/cancel` (cancela); `GET /api/config` (configuración efectiva).
3. **Agregar las dos filas de buses** (vienen de la Tabla 62 eliminada de §17.3):
   medios → control, ZeroMQ PUB/SUB + msgpack en :5557, transporta `media.detection.v1` y el ciclo de vida
   dentro de `bus.envelope.v1`; control → distribución, ídem en :5558, transporta `control.alert.v1`.
4. **Agregar la fila de clientes:** runner y webconsole como clientes HTTP de los tres servicios; gobiernan
   corridas y consolidan artefactos; no consumen los buses de datos.
5. Precisión verificada: NO existe `cancel` en el plano de medios (el verbo real es `stop`) ni en el plano
   de control. No listarlos; la Nota existente ("interfaces de administración y detención") los cubre.

### E4-07 · §17.4.5 y Tabla 63 — DOS patrones de acople, no tres *(obs 29 / C8)*
El acople BFF-subproceso fue reemplazado por la interfaz HTTP del módulo de distribución y ya no es un
patrón de la plataforma (queda solo como contingencia operativa interna, que el informe no necesita
mencionar). Acciones:
1. §17.4.5 primer párrafo: *"tres patrones técnicos de acople"* → **"dos patrones técnicos de acople"**.
2. Tabla 63: eliminar la fila "BFF-subproceso" y su Nota.
3. Fila "HTTP gobernado por configuración": Participantes → **"Soporte experimental, plano de medios,
   plano de control y módulo de distribución"**.
4. Nueva Nota. **Texto guía:** *"Nota. Los dos patrones separan gobierno y datos: HTTP gobierna
   configuración y ciclo de vida de los tres servicios; el bus transporta los hechos de ejecución."*

### E4-08 · §17.4.5 — borrar el párrafo de la parada cooperativa *(obs 30 / C9)*
Eliminar completo: *"La parada de fuentes de red se implementó de manera cooperativa…"*.

### E4-09 · §17.4.5 — dockerización: reproducibilidad, sin "dos nodos" *(obs 31 y 37 / C10)*
Reemplazar *"El despliegue EBE en dos nodos se contenedorizó y verificó con imágenes separadas por rol,
sin modificar los contratos de los planos."* por un desarrollo breve de la idea. **Texto guía:**

> *"La plataforma se contenedorizó con imágenes separadas por rol funcional. La finalidad no es la
> distribución física, sino la reproducibilidad del despliegue: cada imagen congela las dependencias, la
> versión de código y la configuración de arranque de su rol, de modo que el entorno de ejecución deje de
> ser una variable implícita de la corrida. El arranque ordenado de los servicios —control antes que
> medios, conforme al orden de suscripción del bus— se declara en la composición y no depende de pasos
> manuales. Los contratos entre módulos no distinguen si los servicios comparten host o no; la topología
> efectiva de cada corrida se registra en su configuración. En los experimentos del presente trabajo, los
> servicios se ejecutaron co-ubicados en un único host con GPU; la separación por roles se conserva como
> organización lógica del despliegue, no como topología exigida."*

(Nota interna, no va al informe: al cierre se consolida la infra dockerizada en los repositorios para que
el texto y el código coincidan.)

### E4-10 · §17.4.6 — borrar la oración de milisegundos *(obs 32 / C11)*
Eliminar: *"Los tiempos se expresan en milisegundos y no en cuadros, por lo que su significado se conserva
frente a cambios de cadencia."* — ya está dicho en §17.3.8.2 y en la nota de la Tabla 46.

### E4-11 · §17.4.6 — supresión como decisión de diseño + valores del patrón completos *(obs 33 / C12, y cierre de E3-09)*
1. Reescribir: *"El conjunto de patrones oficial opera con granularidad de escena y no configura supresión
   de re-alertas. El motor dispone de esa capacidad, pero la configuración adoptada la mantiene desactivada
   porque…"* → **Texto guía:** *"El conjunto de patrones oficial opera con granularidad de escena. En
   coherencia con la decisión de diseño que separa la alerta interna de su comunicación (DA-13), el motor
   registra cada confirmación sin supresión: el cooldown, la agrupación y la limitación de tasa pertenecen
   a la política del módulo de distribución."*
2. Completar los valores del patrón que migran desde la Tabla 46 (E3-09). Agregar tras las ventanas:
   **"Las precondiciones de evidencia exigen confianza mínima de 0,35 y área mínima de 400 píxeles
   cuadrados para el sujeto, y confianza mínima de 0,25 para el elemento de protección. La región de
   búsqueda se define de forma relativa a la caja del sujeto: para CR-01, la franja superior entre el 0 %
   y el 45 % de la altura con margen lateral del 12 %; para CR-02, la franja del torso entre el 25 % y el
   85 % con margen lateral del 8 %."** (Valores verificados contra el pattern set; ver §D.)

### E4-12 · §17.4.6 — catálogo de modelos y corrección del umbral *(obs 34 / C13 + discrepancia verificada)*
Reescribir el párrafo del perfil desplegado. Dos correcciones obligatorias: **box_threshold es 0,30, no
0,35** (verificado en el perfil del campeón y en los registros de las campañas oficiales), y
"confidence_threshold" no es un umbral del carril Grounding DINO. **Texto guía:**

> *"La estrategia perceptiva del núcleo utiliza evidencia positiva: person como entidad y helmet y vest
> como elementos de protección. La ausencia se infiere en el plano de control y no se consulta como una
> negación opaca al detector. El catálogo de perfiles de modelo materializa la sustituibilidad prevista en
> el diseño: incluye variantes de Grounding DINO (tiny y base, con resolución de entrada de 800 y de 560
> píxeles), de MM-Grounding DINO y de YOLOE, todas integradas mediante adaptadores sobre el mismo contrato
> de salida. El perfil desplegado para el núcleo es grounding-dino/gdino-tiny-560, seleccionado en la
> comparación de modelos que se presenta en la sección 17.5. Su configuración efectiva fija el umbral de
> caja en 0,30 y el umbral de texto en 0,25; el postproceso aplica confianza mínima de 0,25, supresión de
> solapamientos con IoU de 0,50 y área mínima de caja de 100 píxeles cuadrados; el control de ritmo opera
> con selección determinista de paso 1 y una cola máxima de ocho unidades. Estos valores quedan persistidos
> con cada corrida y no dependen de constantes ocultas en el código."*

### E4-13 · §17.4.7 — incorporar el árbol del repositorio de corrida *(cierra E3-14)*
El árbol que estaba en §17.3.12.1 no coincidía con el layout real: la consolidación del soporte
experimental **copia los artefactos livianos y referencia los pesados** (exactamente lo que ya dice la
Nota de la Tabla 64) — verificado contra los repositorios de ejecución reales el 2026-08-19. Después de
la Tabla 64, insertar con introducción. **Texto guía:**

> *"Cada plano conserva su repositorio completo por corrida (el plano de medios: detecciones, métricas,
> errores, resumen, configuración efectiva, manifiesto y procedencia; el plano de control: transiciones,
> alertas, métricas, errores, resumen y configuración efectiva). El soporte experimental consolida la
> ejecución experimental copiando los artefactos livianos y referenciando los pesados:"*

```
runs/<experiment_id>/                (repositorio del soporte experimental)
  manifest.effective.yaml
  media/      summary.json · metrics.jsonl · effective_config.yaml ·
              detections.ref.json   (referencia al detections.jsonl del plano de medios)
  control/    alerts.jsonl · pattern_events.jsonl · metrics.jsonl ·
              summary.json · effective_config.yaml
              (y la evaluación temporal, cuando la corrida la habilita)
  report/     report.json · report.md
```

Cuando el tramo de distribución está habilitado, su ledger y su reporte se consolidan del mismo modo.
En la Nota de la Tabla 64: *"…se referencian en la corrida paraguas…"* → **"…se referencian en la ejecución
experimental…"** *(rezago del término detectado)*.

### E4-14 · §17.4.8 — CVAT con nombre propio; podar los detalles de exportación *(obs 35 y 36 / C14, C15, C16)*
Reescribir la sección completa. **Texto guía:**

> *"La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante
> el esquema clip_gt.v2. Para la anotación de los videos se seleccionó CVAT, una herramienta de anotación
> de código abierto con soporte de interpolación temporal y exportación estructurada, que permite anotar
> episodios sobre video con esfuerzo humano acotado. Su salida se procesa mediante una cadena reproducible
> de separación, derivación de la referencia temporal, validación, promoción y agregación; la cadena valida
> la estructura de cada exportación antes de derivar, y las anotaciones promovidas quedan congeladas bajo
> control de versiones. La herramienta de anotación funciona así como instrumento de captura: la referencia
> experimental es la versión promovida en el repositorio."*

(Se eliminan: el párrafo del nivel de exportación proyecto/tarea con su error simétrico, y el párrafo de
correcciones firmadas — quedan cubiertos por "valida la estructura" y "congeladas bajo control de
versiones". El marcador `[[PENDIENTE: dirección de origen…]]` se conserva.)

### E4-15 · Tabla 65 — despliegue contenedorizado sin "dos nodos" *(obs 37 / C17 en su antecedente)*
Fila "Despliegue en dos nodos" → **"Despliegue contenedorizado por rol"**; evidencia →
**"Los servicios se construyeron como imágenes por rol y se ejercieron sin modificar los contratos entre
planos."** Estado: Verificada (eso sí ocurrió).

### E4-16 · Tabla 66 — eliminar las filas/celdas de lo que no se hizo *(obs 37 y 38 / C17, C18)*
1. **Eliminar la fila completa** "Latencia captura-resultado en topología de dos nodos" (los experimentos
   finales se ejecutaron en un solo nodo; la regla general de relojes queda en §17.3.13.2, que no afirma
   ejecución).
2. Fila "Paridad DBE/EBE sobre fuente equivalente": eliminar la celda-consecuencia actual (*"La
   sincronización explícita entre reloj de captura…"*) y reemplazar por **"La reevaluación offline de una
   corrida live produce artefactos equivalentes; la paridad de transporte y relectura queda verificada."**
3. **Actualizar la fila de la rama de ajuste fino** (quedó desactualizada): *"la corrida completa fue
   autorizada y encolada en el nodo de entrenamiento"* → **Texto guía:** *"Protocolo, procedencia, servicio
   de inferencia, evaluación y línea base quedaron congelados. El primer tramo ejecutado se evaluó contra
   el banco congelado y no superó los criterios de incorporación predefinidos; un tramo exploratorio
   adicional permanece en ejecución."* El marcador `[[PENDIENTE: …]]` se conserva hasta el veredicto final.
   (Regla de encuadre: la rama es condicionada por datos y protocolo, nunca "por falta de tiempo".)

### E4-17 · §17.4.10 — párrafo nuevo: por qué solo el núcleo validable *(obs 2 / C0 de §17.3)*
Insertar después del primer párrafo de §17.4.10 (antes de la Tabla 66). **Texto guía:**

> *"La concentración del prototipo en el núcleo validable no responde a una reducción tardía del alcance,
> sino a las condiciones de evaluabilidad de cada condición del catálogo. Las condiciones de Nivel 1
> cuentan con datasets públicos y bancos de evaluación con verdad de terreno para persona y elementos de
> protección personal, lo que permite medir percepción, estado temporal y alerta con denominadores
> declarados. Las condiciones de Nivel 2 y Nivel 3, en cambio, exigen insumos que el material disponible no
> provee: verdad de terreno de andamios, arneses, bordes desprotegidos o zonas restringidas; definiciones
> externas de zona y geometría de cámara controlada; y evaluadores relacionales o de trayectoria cuya
> validación requeriría bancos propios que no existen en el dominio. Incorporarlas sin esa base habría
> producido capacidades no medibles, contrarias al criterio metodológico de no convertir extensiones en
> dependencias del flujo base. El esfuerzo experimental se concentró, en cambio, en llevar el núcleo a
> capacidad medida: la misma decisión que limitó la cantidad de condiciones cubiertas es la que permite
> reportar cada resultado con su evidencia."*

(Eco breve en las conclusiones cuando se redacte esa etapa — no repetir el argumento, solo reafirmarlo.)

### E4-18 · Barrido general anti-redundancia con §17.3 *(obs 32, criterio general)*
Además de E4-10, revisar que §17.4 no re-explique reglas ya establecidas en el diseño; donde haga falta el
concepto, referenciar la sección de §17.3. Casos concretos detectados:
- §17.4.4 último párrafo y §17.4.5 tercer párrafo repiten el orden de suscripción ya diseñado en §17.3.8.4:
  conservarlo UNA vez en §17.4.5 (como condición de corrección verificada) y quitar la repetición de
  §17.4.4 (dejar solo *"En una corrida live, la respuesta afirmativa del plano de control implica que su
  consumidor ya está suscripto"*).
- §17.4.5: *"El patrón publicador-suscriptor no retiene mensajes emitidos antes de la suscripción"* puede
  abreviarse remitiendo al diseño (*"conforme a la restricción de suscripción previa establecida en la
  sección 17.3.8.4"*).

---

## C. Ajustes fuera de los dos documentos

### C-1 · Mini-ajuste en §17.1.5.4.2 (etapa 2) — bautizar las estrategias *(decisión D3)*
En el pasaje que distingue formulaciones directas de indirectas, insertar los códigos. **Texto guía:**

> *"En este trabajo, estas familias se identifican como estrategia directa (E-DIR), cuando el prompt
> intenta describir la condición de riesgo completa; estrategia indirecta (E-IND), cuando el detector
> identifica entidades visibles por separado y la condición se reconstruye mediante lógica externa al
> modelo; y estrategia híbrida (E-HYB), cuando se combinan consultas de ambos tipos bajo una regla de
> composición explícita. Estos códigos identifican las variantes en el diseño arquitectónico y en la
> evaluación experimental."*

Es un ajuste quirúrgico sobre una sección ya integrada en Google Docs (regla D-A: se corrige directo en el
maestro).

### C-2 · Enmienda al plan de figuras (manual 08 §6 / materiales 99)
- **FIG-E** (máquina de estados): destino **§17.3.8.2** (Figura 4.5), con los **cinco** estados
  (inactive → candidate → confirmed → sustained → resolved) — resuelve además la discrepancia del plan,
  que la rotulaba con tres estados. §17.4.3 la referencia sin figura propia.
- **FIG-A** (vista de procesos): destino **único §17.4.1** (ya no va también en §17.3.5). En §17.3 queda
  solo la Figura 4.1 conceptual.
- La puerta P4 de §17.4 pasa a exigir solo FIG-A.

### C-3 · Recordatorios de cierre (no van al informe)
- Al cerrar cada sección en el maestro: re-extraer el `.md` y fechar en `entregable/00-el-informe-hoy.md`
  (regla D-C).
- El eco del encuadre "núcleo-solo" queda anotado para el pase de conclusiones (etapa 5/6).
- Consolidar la infra dockerizada en los repositorios antes del cierre final, para que E4-09 quede
  respaldado 1:1 por el código.

---

## D. Hechos verificados (2026-08-19) — NO "corregir" estos valores

Verificados contra los repositorios; cualquier texto que los contradiga está mal, no ellos.

| Hecho | Valor verificado | Fuente |
|---|---|---|
| Ventanas CR-01 | confirmación 4.000 ms · resolución 2.000 ms · severidad high | `e-ovrt_control-plane/configs/patterns/cr01_cr02_v2.yaml` |
| Ventanas CR-02 | confirmación 7.000 ms · resolución 3.000 ms · severidad medium | ídem |
| Evidencia del patrón | sujeto ≥ 0,35 y ≥ 400 px² · EPP ≥ 0,25 (campo único para helmet/vest) | ídem |
| Regiones | CR-01: 0–45 % superior, margen 12 % · CR-02: 25–85 %, margen 8 % | ídem |
| Cooldown | NO configurado en el pattern set; el cooldown vive en distribución (default 30 s) | pattern set + `eovrt_distribution/policy.py` |
| Estados del motor | inactive, candidate, confirmed, sustained, resolved (los 5, exactos) | `pattern_engine.py` |
| Perfil campeón | `grounding-dino/gdino-tiny-560` · **box_threshold 0,30** (no 0,35) · text 0,25 · image_size 560 | `configs/models/grounding-dino/gdino-tiny-560.yaml` + `results/*/campaign.yaml` |
| Postproceso | min_confidence 0,25 · IoU 0,50 · área mínima 100 px² | `eovrt_media/config/schemas.py` |
| Control de ritmo | stride 1 (determinista) · cola máxima 8 | ídem |
| Catálogo de modelos | 11 perfiles: gdino tiny/base × 800/560 · mm-gdino tiny/base/large · yoloe 26s/m/l/x · mock · +ft-t1 | `e-ovrt_media-plane/configs/models/` |
| Endpoints medios (:8080) | healthz, readyz, /api/model, POST/GET /api/runs, GET detections, POST/GET evaluate, **stop (no cancel)**, dropped, artifacts, websockets | routers del servicio |
| Endpoints control (:8081) | POST/GET /api/runs, GET alerts, pattern-progress, pattern-events, received-units, /api/config, healthz/readyz · **sin cancel** | ídem |
| Endpoints distribución (:8082) | POST/GET /api/runs, **POST /api/runs/{id}/cancel**, /api/config, healthz/readyz | ídem |
| Esquemas | media.detection.v1 · control.pattern_state.v1 · control.alert.v1 · control.notification.v1 · control.delivery.v1 · bus.envelope.v1 · run.lifecycle.v1 · media.metric.v2 · control.metric.v1 — todos existen con ese nombre exacto | contracts de los 3 repos |
| Preselección en borde | implementada, `enabled: False` por defecto, fail-open estructural; fuera de los experimentos finales | `schemas.py` + `oak_d_source.py` |
| Pruebas | 2.203 aprobadas en cinco suites (relevamiento integral) | constancia operacional |
| Puertos | medios :8080 · control :8081 · distribución :8082 · bus detecciones :5557 · bus alertas :5558 | servicios + CLAUDE.md |
| Repo de ejecución consolidado | `manifest.effective.yaml` + `media/` (livianos + `detections.ref.json`) + `control/` (livianos) + `report/` — los pesados se referencian, no se copian | `experimental-setup/runs/exp_*` |

---

## E. Renumeración de tablas y figuras (consecuencia de aplicar §A y §B)

Hoy los números COLISIONAN: §17.3 tiene Tablas 61/62/63/64 intercaladas fuera de orden (entre la 50 y la
51) que repiten los números de las Tablas 61–67 de §17.4. Tras eliminar las Tablas 61 y 62 de §17.3
(E3-13), la renumeración queda así (la numeración definitiva la fija el maestro al integrar):

**Tablas de §17.3** — 39 a 50 sin cambio; luego, en orden de aparición en el documento:

| Número actual | Contenido | Número nuevo |
|---|---|---|
| Tabla 63 | Superficie de crecimiento del evento de percepción (§17.3.11.4) | **51** |
| Tabla 51 | Hechos persistibles mínimos (§17.3.12.2) | **52** |
| Tabla 52 | Métricas y evidencias por tramo (§17.3.13.1) | **53** |
| Tabla 64 | Diccionario de métricas (§17.3.13.2) | **54** |
| Tabla 53 | Señales observables (§17.3.13.3) | **55** |
| Tabla 54 | Comparación DBE/EBE (§17.3.14.4) | **56** |
| Tabla 55 | Condiciones observables para interpretar EBE (§17.3.14.5) | **57** |
| Tabla 56 | Roles funcionales y unidades desplegables (§17.3.15) | **58** |
| Tabla 57 | Riesgos arquitectónicos (§17.3.16) | **59** |
| Tabla 58 | Plan de materialización del núcleo (§17.3.17) | **60** |
| Tabla 59 | Capacidades complementarias (§17.3.17) | **61** |
| Tabla 60 | Criterios de cierre (§17.3.18) | **62** |

Referencias en prosa de §17.3 a actualizar: *"La Tabla 63 explicita…"* (§17.3.11.4) → **51**;
*"La Tabla 54 resume…"* (§17.3.14.4) → **56**. Las referencias a las Tablas 39–50 no cambian.

**Tablas de §17.4** — corren +2 para continuar desde la 62 final de §17.3: 61→**63** (correspondencia),
62→**64** (interfaces), 63→**65** (patrones de acople), 64→**66** (artefactos), 65→**67** (verificación),
66→**68** (brechas), 67→**69** (extensibilidad). Referencias en prosa: *"La Tabla 61 establece…"*
(§17.4.2) → **63**; *"La Tabla 66 evita…"* (§17.4.10) → **68**.

**Figuras de §17.3** — tras mover la Figura 4.2 a §17.4.1 (E3-05): 4.1 sin cambio; 4.3→**4.2** (flujo del
plano de medios), 4.4→**4.3** (flujo del plano de control), 4.5→**4.4** (máquina de estados, FIG-E),
4.6→**4.5** (cadena de traducción), 4.7→**4.6** (roles CPN/EN/TN). La prosa de §17.3 no referencia
figuras por número, así que solo cambian los rótulos.

**Figura de §17.4** — la vista de procesos (FIG-A, §17.4.1) toma el número consecutivo siguiente
(**4.7**), sujeto al esquema de numeración del maestro al integrar.
