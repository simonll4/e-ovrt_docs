# Alineación con la Consolidación Metodológica del informe (§17.1)

> ⚠️ **2026-08-10 — DOCUMENTO HISTÓRICO.** Alineación previa al tramo experimental (última
> actualización 2026-07-09). Para redactar §17.1 hoy, la fuente es
> `../../informe/ajustes/02-etapa-2-consolidacion-metodologica.md`. Ver el `README.md` de
> esta carpeta.

- **Fecha:** 2026-07-07
- **Fuente:** `docs/informe/entregable/E-OVRT-VDP_v1.1_05062026-sin-indice.docx` — leído completo el
  §17.1 (Consolidación Metodológica), estructura de §15–16 (estado del arte y marco
  teórico) y §17.3 (versión previa de Etapa 3). El informe **no es fuente de verdad
  cerrada** (está en desarrollo), pero es el protocolo contra el que la plataforma y
  nuestros documentos 01–07 deben leerse.
- **Resultado neto:** la metodología del informe **valida las decisiones centrales del
  set 01–07** (en varios casos textualmente) y aporta definiciones operativas que nos
  faltaban (severidades, ventanas, umbrales, nombres de métricas, protocolo de
  prompts). Hay ~8 ajustes concretos a aplicar y una autocorrección de la auditoría.

> **✎ Adenda 2026-07-19 — dimensionamiento del banco y frontera de métricas
> (`operacion/57`).** El doc 57 completa esta alineación por el lado del **dataset
> de video**: duraciones de clips derivadas de las ventanas/targets de este doc
> (bimodal 15 / 25–30 s), validación externa contra i-LIDS/TRECVID (la estructura
> episodio+ventana+`re_alerts` resulta ser la versión *corregida* del estándar), y
> la **frontera de atribución de métricas** (§7: Nivel A = rendimiento OVD
> [AP/TTFD/SDR/G2A], Nivel B = alertado de la plataforma [P/R/F1, t_alert,
> FAR/hora]; `t_alert-system` **no** compara modelos — D1 se decide en Nivel A).
> Su §7.5 lista las **cinco declaraciones** que Etapa 4 debe hacer (FAR/hora como
> derivada propia; mediana+rango por-episodio amparado en la cláusula "n efectivo
> + IC" de §17.1.5.4.2; `metric_censored`; P9+soak como extensión de C.2; la
> advertencia sobre t_alert) y aclara que el **piso de ~200 instancias** aplica a
> lo espacial/prompts (instancias/imágenes), no a episodios. Sin contradicciones
> con este doc: llena el hueco de duraciones/composición que el informe no fijó.
> Su §7.6 fija el **principio rector del cierre** (decisión del equipo
> 2026-07-19): el núcleo validable se cierra con las métricas que el material
> efectivamente cubra — cobertura decide el set reportado; lo no cubierto se
> declara con estado y causa (ADR-006), nunca bloquea ni se fabrica.

## 1. Lo que el informe valida (y refuerza)

1. **El experimento D1 ya estaba mandado por la metodología.** §17.1.5.4.2 (eje
   "estrategia de detección") y §17.1.5.4.5 exigen comparar empíricamente
   formulaciones **directas vs indirectas** "para todas las condiciones en que sean
   aplicables, **sin presuponer la superioridad de ninguna**". Nuestro doc 04 es la
   ejecución de ese protocolo. Consecuencia fuerte: la adopción de la estrategia
   directa como núcleo en Etapa 3 §17.3.9.2 no solo contradice la implementación —
   **contradice la propia consolidación metodológica del informe**. La crítica del
   doc 02 §4.1 queda cerrada a favor de "comparar primero".
2. **G0 (granularidad escena) validada textualmente.** §17.1.10.2: "CR-01 y CR-02 se
   evalúan mediante persistencia temporal simple **sin requerir MOT obligatorio**,
   siempre que la evaluación se mantenga **a nivel de patrón y no exija identidad
   individual persistente**". La recomendación D2 (G0 núcleo, G1 condicionada) es
   exactamente esto.
3. **El clip bench escenificado es el diseño oficial del EBE.** Tabla 20: "espacio de
   obra simulado; personas reales portando EPP; configuración de escenas **con y sin
   infracción deliberada**". La propuesta H2 (grabación propia guionada) no es un
   atajo: es el Escenario B del informe. Requisito que trae aparejado: consentimiento
   libre, expreso e informado + minimización (Ley 25.326, Disposición 10/2015) —
   documentarlo al grabar.
4. **La política de aplicabilidad de métricas (D6) es núcleo metodológico.**
   §17.1.7.3.3 fija cinco condiciones de factibilidad y §17.1.7.8.2 enumera los casos
   de no-aplicación. Nuestro `report.json` con estados debe implementar esa taxonomía
   tal cual (calculada / no ejecutada con causa / no aplicable).
5. **MQTT (D5) aparece explícitamente** en la Tabla 33 como componente del tramo de
   notificación (`MQTT/HTTP/WebSocket`). Alineado.
6. **El "won't" de fine-tuning (I1) tiene marco formal.** §17.1.9 Tabla 37: "la regla
   **no prescribe que el fine-tuning deba ejecutarse**; define cuándo vale la pena".
   Matiz honesto a incorporar: el TN existe y está disponible (clúster Mendieta,
   CCAD-UNC, GPUs A30) — el won't se declara por **presupuesto de tiempo del
   proyecto**, no por falta de recursos, citando la regla de decisión de la Tabla 37
   (ganancia exigible / costo operativo / prioridad del núcleo). (✎ 2026-08-11:
   encuadre **superado por ADR-017** — la causa "presupuesto de tiempo" queda
   derogada; E-04 se ejerce como jornada comprometida y el ajuste vigente es
   AJ-2.11 reescrito.)
7. **Si G1/tracker entra, la métrica correcta ya está definida:** ΔFP_tracker
   (§17.1.7.4.2) — diferencia de falsos positivos entre corridas con y sin tracker,
   **sin necesidad de GT de identidades**. Mucho más barata que HOTA/IDF1; la Tabla 38
   la fija como primer paso obligatorio antes de exigir métricas MOT completas.
8. **CPN = laptop RTX 4060 8GB, Windows 11 + WSL2** — el entorno actual es el
   previsto; el presupuesto G2A declarado es **50–250 ms** (restricción de la
   Tabla 21, estimación 35–250 ms en §17.1.7.7.5). El H5 (¿GDINO lento para EBE?)
   tiene ahora una vara concreta: GDINO-tiny debe caer dentro de esa banda para ser
   defendible como configuración EBE.

## 2. Desalineaciones a corregir en lo nuestro

### 2.1 Severidades y ventanas de persistencia (la más importante — toca código/config)

El catálogo de patrones (Tabla 24) fija:

| Patrón | Severidad | Persistencia | Nuestro control-plane hoy |
|---|---|---|---|
| PR-01 (CR-01, sin casco) | **Alto** | **3–5 s** | severity `medium`, `confirm_after_frames: 1` |
| PR-02 (CR-02, sin chaleco) | **Medio** | **5–10 s** | severity `medium`, `confirm_after_frames: 1` |

Además §17.1.5.3.3 exige parametrizar la persistencia **en segundos, no en frames**
(la conversión depende del throughput) — el motor ya soporta `confirm_after_ms`, así
que el ajuste es de configuración: crear un pattern set `cr01_cr02_v2` alineado
(PR-01: alto, confirm ~4000 ms; PR-02: medio, confirm ~7000 ms; valores iniciales
declarados dentro de los rangos, calibrables en validación). El set actual con
confirm=1 frame queda como configuración de diagnóstico DBE-imágenes, documentada
como tal. La histéresis activación≠desactivación (§17.1.5.3.3) ya está soportada
(`resolve_after_*`).

### 2.2 Nomenclatura y definiciones de métricas (cierra el diccionario de D6)

Adoptar los nombres y definiciones del informe, textuales:

- **G2A** (Glass-to-Algorithm): captura/lectura del frame → resultado algorítmico.
  Componentes: t_capture + t_transport + t_preprocess + t_inference. Presupuesto
  50–250 ms.
- **t_alert-system** (métrica operativa principal): **inicio anotado del evento** →
  alerta confirmada y registrada. Integra G2A + t_track + t_reasoning + T_persistencia.
- **t_alert-notification** (complementaria, solo con trayecto instrumentado).
- **TTFD**: inicio anotado → primera detección positiva válida (criterio declarado).
- **SDR**: proporción del intervalo anotado con detecciones positivas sostenidas.
- **ΔFP_tracker**: delta de FP con/sin tracker, unidad de conteo declarada.
- Reporte temporal mínimo: **P50/P95/P99 + promedio**, con warm-up previo declarado y
  timestamps monotónicos de fuente explícita.

**Adenda 2026-07-09 — dos métricas derivadas propias (no del informe).** El spec 40
§5.2 introduce `t_capture→alert` (captura del frame de primera evidencia → alerta
registrada) y `t_compute-budget` (= t_capture→alert − T_persistencia_efectiva).
**No sustituyen a `t_alert-system`: la descomponen**, y se introducen porque son
las únicas métricas end-to-end computables **sin GT**, lo que permite validar el
tramo plataforma antes de que exista el clip bench (ADR-010). Vale la identidad
`t_alert-system = TTFD + t_capture→alert` **si y solo si** el `t1` de TTFD se
define en el **instante de captura** del frame de primera evidencia — así queda
declarado en el spec 40 §5.2.2. `t_compute-budget` es, literalmente, el
"presupuesto computacional" por el que la Tabla D.4 dice que `t_alert` excede a la
persistencia. Al escribir Etapa 4 deben presentarse como aporte instrumental
propio, con esta justificación, no como reemplazo de la métrica oficial.

**Umbrales orientativos por severidad (Tabla 35) — son los targets de R3:**

| Severidad | t_alert-system | TTFD | SDR mínima |
|---|---|---|---|
| Alta (PR-01) | 5–10 s | < 3 s | ≥ 0.60 |
| Media (PR-02) | 10–20 s | < 10 s | ≥ 0.70 |

El evaluador temporal del control-plane (`evaluate-alerts`) debe leer sus resultados
contra estos umbrales y el clip bench debe anotar inicio/fin de episodio (t0 de
TTFD/t_alert-system = **inicio anotado**, no primera detección).

### 2.3 Protocolo de prompts: ejes que a D1 le faltaban (actualizar doc 04)

El protocolo (§17.1.5.4.2/.5, 5 fases) agrega requisitos que el doc 04 no tenía:

1. **Contexto de vocabulario como variable**: cada prompt se evalúa **en aislamiento
   y en vocabulario completo** (hipótesis: prompts semánticamente próximos compiten).
   Incorporar al menos para las formulaciones finalistas de D1.
2. **Variantes con template** ("a photo of a [CLASS]") como eje de estructura
   sintáctica — sumar 1–2 variantes template al prompt set `edir_v1`.
3. **Hiperparámetros congelados** (confianza/NMS constantes entre variantes de
   prompt) — explicitarlo en la config de las corridas D1.
4. **Piso muestral: ~200 instancias positivas por condición** o reportar tamaño
   efectivo + intervalos de confianza — nuestra corrección de bootstrap (doc 07/H1)
   ya cumple la segunda vía; reportar el n contra este piso.
5. **Anotación complementaria con doble anotador**: ≥20% doblemente anotado, kappa de
   Cohen para etiquetas, IoU para cajas — aplica al **clip bench** y a cualquier
   anotación nueva de estado EPP.
6. **Confianza media de los TP** como indicador de estabilidad por formulación.
7. Para la estrategia indirecta, **métricas por entidad componente** (person, helmet,
   vest por separado) para atribuir la degradación — el BENCH ya las produce.
8. El catálogo de formulaciones candidatas vive en el **Anexo C (Tabla C.1)** del
   informe — `edir_v1` debe construirse desde ahí (además de la Tabla 45 de Etapa 3),
   citándolo.

### 2.4 El plan de 12 semanas debe mapear a las fases del protocolo integrado (Tabla 36)

| Fase del informe | Nuestro plan | Estado |
|---|---|---|
| Preparación (congelar entorno, checkpoints, test set, bitácora) | Semana 1–2 (Fase 0 + ADRs) | BENCH v2 ya congelado; falta declarar el congelamiento formal (versiones, checkpoints) |
| Baseline DBE zero-shot | Ya ejecutada (Sprint 2) | Redactar como resultado R1 |
| Sensibilidad de prompts | Semanas 3–4 (experimento D1) | Protocolo doc 04 + ajustes §2.3 |
| Pipeline y tracking (G2A, FPS, ΔFP_tracker) | Semanas 5–6 | G2A explícito vs presupuesto 50–250 ms |
| Fine-tuning condicionado | Won't (rama no ejercida, Tabla 37) (✎ 2026-08-11: hoy **jornada comprometida**, ADR-017) | Declarar con la regla del informe |
| EBE complementario | Semanas 7–8 (R4) | Escenificado + consentimientos |
| Reporte | Semanas 9–12 (D6) | `report.json` + estados de aplicabilidad |

Usar los nombres de fase del informe en specs y en la escritura de Etapa 4/5 — la
correspondencia 1:1 es un argumento de coherencia metodológica gratis en la defensa.
*(✎ 2026-07-09, ADR-010: las semanas de la columna "Nuestro plan" dejan de leerse
literalmente — vale la correspondencia de fases y sus dependencias; "Sensibilidad
de prompts" se parte en Fase 1 temprana / Fases 2–3 con el clip bench al final.)*

### 2.5 Instrumentación pendiente detectada por §17.1.7.8

- Hitos obligatorios por alerta: timestamp de **primera evidencia positiva**, patrón
  candidato, confirmado, alerta registrada, notificación. El control-plane persiste
  candidate/confirmed/alert (✓ en `pattern_events.jsonl`); falta explicitar la
  primera evidencia (derivable del primer hit — dejarlo como campo del episodio).
- Percentiles P50/P95/P99 en métricas del control-plane (hoy solo promedio).
- Warm-up declarado por corrida (media-plane: verificar; control-plane: N/A en replay).
- Bitácora mínima por corrida (§17.1.7.8.4) ≈ nuestro `report.json` consolidado + 
  `effective_config` — ya cubierto por D4/D6 al implementarse.

### 2.6 Matiz para H4 (fuente EBE)

El informe define el EN candidato (OAK-D Pro PoE — **disponible e integrado desde
2026-07-13** como fuente `oak_d` del media-plane) **con plan de contingencia
oficial: cámara IP convencional** (§17.1.4.2.4), que se ejerció primero. Para la corrida EBE de
la defensa, una cámara IP/webcam real es más fiel al diseño que el RTSP sintético;
mediamtx+ffmpeg queda como (a) herramienta de desarrollo y (b) vía de
reproducibilidad DBE↔EBE con fuente idéntica. Actualiza la prioridad de H4:
contingencia oficial primero, sintético como complemento.

## 3. Autocorrección de la auditoría (erratas de Etapa 3)

Los "nombres de métrica vacíos" que reporté en doc 02 §4.8 y doc 07 como errata del
docx de Etapa 3 aparecen con el mismo patrón en toda la extracción del informe
(§17.1.5.3.2, §17.1.7, Tabla 33...). Eso indica que **son objetos de ecuación de Word
(t_alert-system, t_alert-notification, G2A, T_persistencia, ΔFP_tracker) que mi
extracción XML no captura**, no campos rotos del documento. En el Word original casi
seguro se ven bien. Corrección aplicada en docs 02 y 07: queda como "verificar
visualmente en Word", no como errata confirmada. Las demás erratas (Figuras x,
títulos de tabla pegados, oración duplicada en §17.3.15) siguen vigentes.

## 4. Acciones concretas (en orden)

1. **Pattern set `cr01_cr02_v2`** en control-plane: PR-01 alto/~4000 ms, PR-02
   medio/~7000 ms, resolve por histéresis; el v1 queda como config de diagnóstico. (§2.1)
   *Nota 2026-07-09:* la rama `mati` agregó `cr01_cr02_field_v1` (perfil de campo con
   expiración/cooldown/memoria de cobertura) — la v2 alineada al informe debe partir
   de ese perfil, cambiando severidades (PR-01→alto, PR-02→medio) y ventanas
   (3–5 s / 5–10 s; hoy usa 1000 ms), **y desactivando el cooldown: por ADR-011
   la supresión de re-notificación es política del tramo de distribución, no del
   motor** (spec 41 §7).
2. **Diccionario de métricas (D6)** con los nombres/definiciones/umbrales del §2.2 —
   ya no hay que inventarlo: es transcribir §17.1.7 + Tabla 35.
3. **Actualizar doc 04**: ejes de §2.3 (vocabulario aislado/completo, templates,
   hiperparámetros congelados, kappa, n≥200 o IC, confianza media TP, Anexo C como
   fuente del prompt set).
4. **Clip bench**: protocolo de anotación con doble anotador 20% + kappa; GT con
   inicio/fin de episodio; consentimientos escritos (§1.3).
5. **Specs por módulo**: usar nombres de fases de Tabla 36 y métricas de §2.2.
6. **Reformular I1** (won't fine-tuning) citando Tabla 37 y aclarando que el TN
   (Mendieta) existe — la exclusión es por presupuesto de tiempo. (✎ 2026-08-11:
   superado por **ADR-017** — la causa temporal queda prohibida; ver AJ-2.11
   reescrito en `informe/ajustes/02`.)
7. G2A explícito en el reporte del media-plane contra el presupuesto 50–250 ms; H5 se
   decide contra esa banda.
8. ~~Leer Anexos C y D~~ — **hecho** (2026-07-07); hallazgos en §5.

## 5. Adenda: Anexos C y D (leídos 2026-07-07)

### 5.1 Anexo C — el prompt set tiene fuente exacta

- **Tabla C.1 es la fuente literal de `edir_v1`**: para CR-01 define 5 formulaciones
  por eje (sintáctica "person without hard hat", especificidad "construction worker
  without safety helmet", estado observable "person with bare head on construction
  site", template "a photo of a hard hat", **indirecta "hard hat ; person"**) y para
  CR-02 el set análogo. Dato clave: **la estrategia indirecta (E-IND) figura como una
  fila más de la matriz de prompts del informe** — el experimento D1 es literalmente
  "correr la Tabla C.1 completa". Los templates son de *presencia* (diagnóstico), no
  de ausencia.
- **Tabla C.2 (variables de sensibilidad EBE) debe moldear el guion del clip bench**:
  iluminación (controlada/mixta/natural), resolución base 1280×720 (1080p como
  variante), distancia cámara-sujeto 5–10 m y 10–20 m, oclusión baja/media (severa no
  exigible), tracker on/off, matriz de prompts y composición de vocabulario. Al
  grabar los clips escenificados, variar estas dimensiones según C.2 convierte la
  grabación en la campaña EBE del informe, no en un extra.
- **Tabla C.3 (cobertura)**: CR-01 sólida (7 fuentes), CR-02 adecuada (4), CR-03/04
  BRECHA (0 directas), CR-05/06 parcial — respalda cuantitativamente el recorte del
  núcleo. **Drift a conciliar en Etapa 4**: el inventario del informe (SH17, SHEL5K,
  CHV, Pictor-PPE, Construction-PPE, GDUT-HWD, SHWD, SODA, MOCS) es anterior a la
  selección v2 real del repo datasets (construction_site_safety, chv, ppe_siabar);
  el informe final debe declarar qué candidatos se retuvieron efectivamente y por qué
  (el registry del repo ya lo documenta).

### 5.2 Anexo D — el diccionario de métricas ya está escrito

- **Tabla D.4 completa** (agrega a la Tabla 35 la persistencia y la prioridad de
  error): Crítica t_alert 3–5 s / TTFD <1 s / SDR ≥0.50 / persistencia 2–4 s /
  minimizar FN; Alta 5–10 s / <3 s / ≥0.60 / 3–5 s / balance; Media 10–20 s / <10 s /
  ≥0.70 / 5–10 s / minimizar FP. El t_alert máximo **excede necesariamente** a la
  persistencia (incluye el presupuesto computacional) — cuidar esa lectura en el
  evaluador.
- **Tabla D.5 (insumos por familia de métricas)** es el checklist de instrumentación
  del `report.json`: la familia "alerta y patrón" exige logs con primera evidencia
  positiva, candidato, confirmado, alerta registrada y notificación — coincide con
  §2.5.
- **Tabla D.6 (bitácora)** es el schema de campos del reporte consolidado (D4/D6):
  identificación, modelo/checkpoint/variante, entrada, parámetros (incluye tracker
  on/off, ventana, histéresis), hardware, entorno, temporalidad/logs, eventos de
  patrón y alerta, resultados, observaciones. El spec del reporte debe mapear campo a
  campo contra esta tabla.
- ΔFP_tracker (Tabla D.2): "obligatorio (*) si hay tracker y unidad de FP comparable";
  sin unidad declarable, solo análisis exploratorio — regla a copiar en el spec de G1.
