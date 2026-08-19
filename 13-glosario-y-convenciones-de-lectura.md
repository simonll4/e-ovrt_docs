# 13 — Glosario y convenciones de lectura del set documental

- **Fecha:** 2026-07-18 · **✎ Actualizado 2026-08-06** (relevamiento integral: se
  corrigieron las reglas 1/3/5/6/7 y las entradas G1, D1 y ADR-NNN que habían quedado
  pre-ADR-015, y se agregaron las convenciones **AF-x**, **limitación L1–L8 vs hito
  L0/L1** y **las dos series de ADR**)
- **Propósito:** definir en un solo lugar toda la sigla y jerga del proyecto, y las
  reglas para leer este set **sin contexto previo** (pensado para humanos que se suman
  y para LLMs que reciben los documentos fragmentados, p. ej. en un Project de
  claude.ai). Si un término aparece en cualquier doc sin definición, se define acá.

---

## 1. Convenciones de lectura (las reglas de oro)

1. **El número del documento es su identidad** ("doc 04", "doc 56"). Las carpetas
   agrupan por rol: `nucleo/` narrativa, `decisiones/` ADRs, `specs/` serie 40,
   `operacion/` series 30 y 50–101, `informe/` serie 90, `contingencia/` serie 20.
   **✎ 2026-08-10 — `nucleo/` está partida por vigencia:** en la raíz lo actualizado a
   lo implementado (`10` + la serie de relevamientos por servicio **`14`–`19`**); en
   **`nucleo/historicos/`** los docs `01`–`09`, `11` y `12` (ninguno posterior al
   2026-07-13), **con su número intacto** — una cita "nucleo/04" sigue siendo válida,
   solo que el archivo vive un nivel más abajo.
   **✎ 2026-08-06 — excepción que muerde:** desde el 90 las series de `operacion/` y
   de `informe/` **colisionan** (existen `operacion/93` ≠ `informe/93`,
   `operacion/95` ≠ `informe/95`, `operacion/92` ≠ `informe/92`…). Al citar un doc
   ≥90, **decir siempre la serie**: "operacion/95" o "informe/95", nunca "doc 95" a
   secas.
2. **El banner ✎ manda sobre el cuerpo.** Muchos docs son la foto de su fecha y llevan
   arriba banners de actualización posteriores. Si un fragmento del cuerpo contradice
   un banner (o un doc más nuevo), **vale el banner / el doc más nuevo**. Nunca citar
   el cuerpo de un doc histórico como estado actual sin verificar su banner.
3. **Jerarquía de verdad para el estado actual de la plataforma** (✎ actualizada
   2026-08-06; *decía doc 56 > … > doc 92*): **`operacion/97`** (foto integral
   2026-08-05, reemplaza al 56) > banners ✎ > **los 4 índices de
   `e-ovrt_experimental-setup/results/`** (cifras verificadas mecánicamente con
   `operacion/datos/96-verificar-indices.py`) > cuerpo de docs de operación > specs
   (lo *pedido*, no necesariamente lo *construido*). `informe/92` y `operacion/56`
   quedaron **derogados como fuente de números** (2026-08-05).
4. **Docs de registro histórico** (no describen el presente): 32, 36, 50 (reemplazados
   en cadena por el 56), los cuerpos de 33–39 (sus resultados siguen válidos como
   evidencia de esa fecha), y **todo `nucleo/historicos/`** (✎ 2026-08-10; su
   `README.md` dice qué conserva vigencia de cada uno — dos casos especiales: `04` y
   `12` valen **por** no haberse actualizado, son el pre-registro de D1).
5. **Los ADRs no se re-litigan.** Una decisión formalizada (ADR-001…**016**) solo se
   revisa con causa registrada. Si un texto propone reabrir una, es un error.
   **✎ 2026-08-10 — el ejemplo de cómo se hace bien:** ADR-016 reabrió la distribución
   derogando **puntualmente** ADR-015 §2b/§2c/§6 con causa firmada y ratificando el
   resto — sucesión explícita, nunca enmienda tácita.
   ADR-015 además **cierra la puerta**: ninguna capacidad nueva hasta la defensa.
6. **Ninguna cifra sin artefacto.** Todo número citable tiene su `metrics.json` (o
   artefacto equivalente) referenciado desde los 4 índices de
   `e-ovrt_experimental-setup/results/`, o su archivo en `operacion/datos/`. Un
   número sin artefacto no va al informe. (✎ 2026-08-06: *decía "o su ruta en el doc
   92"* — derogado como fuente de números.)
7. **El estatuto del GT depende del material** (✎ actualizado 2026-08-06; *decía "el
   GT de video es preliminar"*): el GT del **banco del rodaje** (34 clips, 35
   episodios) es **humano y `gt_ready` desde 2026-08-03** — sus métricas se reportan
   como **RESULTADO** de la tesis. La regla vieja ("solo verificación de mecánica")
   aplica únicamente a material cuyo GT siga `gt_preliminary` — ~~hoy, el lote de
   internet (14 clips, en anotación CVAT)~~.
   > ✎ **2026-08-10 — ya NO queda material en `gt_preliminary`: la regla vieja no aplica a
   > nada.** El lote de internet terminó su pasada humana (**13 de 14 con GT**, `v08_c01`
   > excluido con causa firmada), así que **sus métricas también se reportan como
   > RESULTADO**. Banco total: **47 clips / 37 episodios**.
   > **Y trajo un resultado propio que hay que contar, no esconder:** la **revisión ciega**
   > del GT (doc 113 §B) encontró que **5 de las 7 declaraciones de episodio del lote eran
   > errores de anotación**, todas sobre-declarando donde el estado **no era observable**.
   > ⇒ **la calidad del GT es un resultado en sí**, el estrato B quedó con **2 episodios
   > evaluables**, y de un n así **no sale ningún ranking** (ver regla 9 y síntesis §5.1).
8. **Registro:** los docs de operación usan voseo informal a propósito (son memoria de
   trabajo). El informe se redacta en registro formal impersonal — el modelo de estilo
   es el doc 94.
9. **El informe vive en `.docx`/Google Docs.** Los `9x-*-texto-extraido*` son
   extracciones derivadas solo para búsqueda y cita; nunca se editan. La Etapa 3
   vigente es el doc 90 (la embebida en el docx v1.1 está desactualizada).

## 2. El proyecto en tres frases

**E-OVRT-VDP** (Experimental Open-Vocabulary Real-Time Video Detection Platform) es el
proyecto integrador (TFG, defensa ~fines de septiembre 2026) de una **plataforma
experimental** que detecta condiciones de riesgo en obras de construcción usando
**detección open-vocabulary (OVD)**: las condiciones se expresan en lenguaje natural
(prompts) en vez de entrenar un modelo cerrado. La tesis **no** es "OVD detecta
mejor": es que una plataforma con condiciones en lenguaje permite **medir qué se logra
sin entrenar** y extender el sistema a condiciones nuevas sin re-entrenamiento
(argumentos A1–A5, doc 09). La plataforma son dos servicios HTTP config-driven
(media-plane :8080, control-plane :8081) orquestados por un runner y una consola web.
✎ 2026-08-18 (ADR-019 + **ADR-020**): **tres** servicios HTTP config-driven — el módulo de
distribución de alertas también expone el suyo (`:8082`) y **el runner le habla por HTTP
por default**. ADR-020 derogó a ADR-018: el subproceso quedó como fallback operativo y
dejó de ser patrón de acople ⇒ la plataforma tiene **dos** patrones (HTTP config-driven en
los tres módulos, y bus ZeroMQ), no tres.

## 3. Siglas y términos del dominio

| Término | Definición |
|---|---|
| **OVD** | Open-Vocabulary Detection: detección de objetos guiada por texto (prompts), sin conjunto de clases fijo. |
| **CR-01 / CR-02** | Las dos **condiciones de riesgo** del núcleo validable: persona sin casco (CR-01, severidad alta) y persona sin chaleco (CR-02, severidad media). "CR" = condición de riesgo del catálogo de la §17.1.5. |
| **PR-01 / PR-02** | Los **patrones de riesgo** que operacionalizan CR-01/CR-02 con persistencia temporal. Umbrales oficiales de plataforma (Tabla D.4 / pattern set `cr01_cr02_v2`): confirmación a los **4000 ms** (CR-01) y **7000 ms** (CR-02); resolución 2000/3000 ms. |
| **DBE** | Dataset-Based Evaluation: escenario offline; el media-plane escribe `detections.jsonl` y el control-plane lo relee (replay). El archivo es la fuente de verdad. |
| **EBE** | Environment-Based Evaluation: escenario live; acople por bus ZeroMQ PUB/SUB (`bus.envelope.v1`, msgpack), corrida 1:1 (ADR-007), cierre por `run_finished`. Toda corrida live es re-evaluable offline con artefactos byte-idénticos. |
| **media-plane** | El plano de medios/inferencia: servicio FastAPI :8080, carga un modelo OVD al arranque (`EOVRT_MODEL_REF`), ingiere fuentes visuales y emite `media.detection.v1`. Repo `e-ovrt_media-plane`. |
| **control-plane** | El plano de control: servicio FastAPI :8081, motor de patrones con histéresis (`inactive→candidate→confirmed→resolved`) que consume detecciones y emite alertas. Repo `e-ovrt_control-plane`. |
| **alert-distribution** | El módulo de distribución: consume las alertas confirmadas del bus (`:5558`) y las entrega por MQTT QoS 1 con ledger de idempotencia. Desde ADR-019 es también servicio FastAPI **:8082** (`eovrt-distribute serve`); desde **ADR-020** (2026-08-18) ese es el acople predeterminado — el subproceso queda como fallback operativo. Conserva su CLI (`replay`/`live`) para el camino offline. Repo `e-ovrt_alert-distribution`. |
| **experimental-setup** | Repo `e-ovrt_experimental-setup`: config experimental centralizada (ADR-009), runner reproducible que orquesta por HTTP los dos planos **y el módulo de distribución** (ADR-004; ADR-020 desde 2026-08-18), consolidación de artefactos (ADR-014), reporte, y la **webconsole**. |
| **webconsole / BFF** | Consola web de gestión: frontend React (Vite :5173) + backend FastAPI :8090 que actúa de Backend-For-Frontend proxy HTTP de los servicios de medios, control **y distribución** (`:8082`, ADR-020). Superficie de gestión primaria (ADR-009). |
| **runner** | CLI del experimental-setup que gobierna las corridas de los dos planos en el orden correcto —live ⇒ control primero (su 201 garantiza suscripción al bus), replay ⇒ media primero— y, cuando corresponde, la distribución posterior (por HTTP desde ADR-020; el subproceso queda como fallback). |
| **G0 / G1 / (G2)** | Granularidades del patrón (ADR-002): **G0 = escena** (sin identidad de personas; el núcleo validable), **G1 = sujeto** (con tracker IoU como decorador en el control-plane). ✎ 2026-08-06: G1 es **capacidad operativa medida** — F1 0,930 sobre los 34 clips **del Bloque A** (el rodaje; ✎ 08-12: decía "del banco", y el banco es de 47 — 34 es el bloque), el mejor resultado, con detecciones bit a bit idénticas a G0 (adenda ADR-002 + ADR-015 E-03; *decía "solo demostrativa"*). Siguen excluidas las métricas MOT (E-10). |
| **G2A** | "Glass-to-algorithm": latencia captura→resultado algorítmico en el media-plane (`g2a_ms` por unidad; presupuesto 50–250 ms). Parte de la métrica `t_capture→alert` (spec 40 §5.2.4). |
| **t_alert** | Latencia de alerta del sistema: desde que la condición se sostiene hasta que el patrón confirma. Con umbral 4000 ms, el valor ideal medido fue 4000,0 ms exactos. |
| **TTFD** | Time To First Detection: ms desde el inicio del episodio GT hasta la primera detección de la evidencia correspondiente. |
| **SDR** | Sustained Detection Rate: fracción del episodio GT cubierta por detecciones (clamp 0–1). |
| **re_alerts** | Alertas repetidas de un mismo episodio (el motor emite en cada confirmación, ADR-011); el evaluador las cuenta aparte y **no** las penaliza como falsos positivos. |
| **Estados de aplicabilidad** | ADR-006/013: cuando una métrica no corresponde, se declara con causa en vez de omitirse: `not_applicable/non_temporal_source` (imágenes), `not_interpretable/dbe_media_time` (video DBE), `not_interpretable/cross_node_monotonic_clock` (two-node), `not_applicable/no_ground_truth`, etc. |
| **D1…D6** | Las seis dimensiones de decisión del doc 03 (estrategia de detección, granularidad, bus, config paraguas, distribución, reporte), formalizadas en ADR-001…006. |
| **E-IND / E-DIR / E-HYB** | Estrategias de detección de D1: **E-IND** = indirecta (detectar persona + EPP y razonar la ausencia — la adoptada como encuadre, ADR-001), **E-DIR** = directa (prompt que describe la infracción, variantes negación/observable), **E-HYB** = fusión de ambas (dual-run con gating por persona). El experimento del doc 04/12 las comparó. ✎ 2026-08-06: **D1 corrió en los dos niveles** (acta firmada 2026-07-29, doc 76; *decía "bloqueada por el acta `edir_v1`"*): E-IND queda como núcleo (F1 0,789), E-DIR **vetada por precisión** (0,146 < 0,5) y E-HYB-or refutada (F-87.2); `hyb_and` no ejecutada con causa (D-90.4). |
| **E-01…E-13** | El registro de **exclusiones** de alcance del doc 10 (qué NO se implementa y bajo qué regla del informe). E-07 es el nodo de borde: OAK-D quedó integrada y EN-2 implementada opcional. |
| **EN / CPN / TN** | Nodos del entorno experimental (§17.1.4): Edge Node (captura; OAK-D Pro PoE), Central Processing Node (GPU de inferencia), Training Node (fine-tuning — clúster Mendieta; **jornada experimental comprometida, ADR-017**, siempre aparte del núcleo zero-shot medido). |
| **EN-2** | Variante de borde con **inferencia parcial en el dispositivo**: prefilter de personas corriendo EN la OAK-D (blob `person-detection-retail-0013`), fail-open, default off. Medido: 87 % de drop on-device en A/B real. |
| **R1…R4** | Los cuatro resultados defendibles del plan (doc 02): plataforma E2E, números DBE, números EBE/latencia, extensibilidad. |
| **A1…A5** | Los cinco argumentos de defensa de OVD del doc 09 (con videos V1–V4). **No confundir con AF-x** (fila siguiente). |
| **AF-1…AF-11** | Las once **afirmaciones** de la escala de conclusiones transversales (`operacion/98` §2), cada una con su fuerza declarada (establecida / direccional / tendencia / no cerrada / limitación). Prefijo **AF** justamente para no colisionar con los argumentos A1–A5 del doc 09. |
| **L1…L8 (limitaciones)** | La lista canónica de **limitaciones declaradas** del trabajo, cerrada el 2026-08-05; la referencia es `e-ovrt_experimental-setup/results/index.md` §Limitaciones. **Colisión a evitar:** la **Fase L** del plan maestro (doc 62) usa `L0`/`L1` para sus *hitos* (L0 = ensayo pre-rodaje, L1 = el rodaje). Al citar, escribir **"limitación L1"** para la lista y **"hito L1" / "el rodaje"** para la fase — nunca `L1` a secas. |
| **ADR-NNN (dos series)** | Architecture Decision Record. Hay **dos series que se confunden**: **`ADR-001…018`** del proyecto (3 dígitos, en `docs/decisiones/`; los ADRs existentes **no se reescriben** —sólo se anotan con ✎ y fecha— pero la serie **sí crece**: 016, 017 y 018 se agregaron después del "cierre" del 2026-07-18 — ver README de la carpeta y su companion `estado-de-implementacion-adrs.md`) y **`ADR-0001…0013`** internos del control-plane (4 dígitos, en `e-ovrt_control-plane/docs/decisions/`; el 0005 no existe). Se solapan en tema con número distinto (p. ej. aplicabilidad = ADR-006 del proyecto vs ADR-0006 del control-plane). **Al citar, decir siempre la serie** ("ADR-0003 del control-plane"). |
| **DA-01…DA-13** | Las **decisiones arquitectónicas iniciales** del capítulo de diseño del informe (§17.3.3.4, tabla completa en el doc 90). Las que más citan los ADRs: **DA-01** separar plano de medios y plano de control; **DA-02** publicar la evidencia perceptiva como eventos normalizados; **DA-03** diferenciar el canal de eventos del repositorio persistente (⇒ el JSONL del plano es la fuente de verdad); **DA-10** priorizar DBE antes de EBE; **DA-13** registrar la alerta interna antes de cualquier notificación externa. |
| **specs serie 40** | Los specs de Etapa 4 por módulo: 40 plataforma (normativa transversal), 41 control-plane, 42 media-plane, 43 clip bench/GT temporal, 44 experimental-setup, 45 distribución MQTT (para lo último). Escritos sin alternativas a partir de los ADRs. |
| **superpowers** | Metodología de trabajo con specs/planes/revisiones que usó Claude para implementar; sus artefactos viven en `docs/superpowers/` o `docs/_archive/superpowers/` de cada repo de código. No confundir con este repo `docs/`. |

## 4. Identificadores y contratos (trazabilidad)

| Término | Definición |
|---|---|
| **`unit_id`** | Identidad de una unidad visual (frame) dentro de un run. **La clave canónica de correlación** entre planos (la vista correlacionada de la consola une detecciones, descartes, progreso y alertas por `unit_id`; keyear por `frame_index` colapsa con `image_folder`). |
| **`run_id`** | Corrida de un plano (`runs/<run_id>/` en cada repo). La corrida EBE es 1:1: un run de control por run de media (ADR-007). |
| **`experiment_id`** | Corrida paraguas del experimental-setup (ADR-004): agrupa los runs de ambos planos y consolida artefactos en `runs/<experiment_id>/` (ADR-014: lo liviano se copia, `detections.jsonl` se referencia). |
| **`source_id` / `clip_id`** | Identidad de la fuente. Convención del clip bench: **`source_id = clip_id`** — así el matching de escena del evaluador une alerta↔episodio GT. |
| **`track_id`** | Identidad de sujeto (opcional en `Detection` desde 07-13). ✎ **2026-08-10 — corregido: decía "nadie lo produce aún, el modo `subject` está inerte". FALSO desde el 2026-08-04.** El modo `subject` **funciona y es el mejor resultado del banco**: la campaña **G1** llega a F1 **0,930** contra 0,789 de escena **con las mismas detecciones bit a bit** (la ganancia es 100% del motor). El `track_id` se produce **post-hoc** con `SimpleIoUTracker`, y el camino config-driven (`input.track_persons`) lo reproduce exacto. Lo que sigue sin existir son **métricas MOT** (E-10, excluida por ADR-015) y el port al pipeline online (decisión abierta, doc 89 §7). |
| **`media.detection.v1`** | Evento de detección del media-plane (JSONL y bus). Evolución **aditiva** (se agregan campos opcionales, no se rompen — regla pedida por el tutor, doc 92). |
| **`bus.envelope.v1`** | Envelope ZeroMQ (topic + `seq` monótono + payload msgpack). Huecos de `seq` = `bus_dropped_events` (degradan, nunca se silencian). |
| **`control.alert.v1`** | Alerta confirmada publicada por el control-plane (persiste-primero). |
| **`control.pattern_progress.v1`** | Progreso parcial 0–1 de un patrón en estado `candidate` (observabilidad; no toca la máquina de estados). |
| **`media.dropped_unit.v1`** | Ledger por-frame de descartes del media-plane (`rate_gate`, `queue_full`, `staleness_timeout`, `channel_closed`). |
| **`clip_gt.v2`** | Contrato de ground truth temporal de un clip: episodios por condición con ventanas en ms, flag `negative`, `sub_threshold_events`, `provenance`. |

### 4.1 Códigos que se citan en todo el set (✎ agregado 2026-08-10)

Estos prefijos aparecen cientos de veces y **hasta hoy no estaban definidos en ninguna
parte**. Sin esta tabla, un lector que no estuvo no puede resolver "F-113.1" ni "D-90.4".

| Código | Qué es | Cómo se lee |
|---|---|---|
| **`F-NN.N`** | **Hallazgo** (*finding*) con mecanismo explicado | El número antes del punto es **el documento de `operacion/` donde nació**; el de después, el hallazgo dentro de ese doc. `F-87.2` = segundo hallazgo del doc 87. Excepciones históricas con letras: `F-EV1/2/3` (fixes del evaluador), `F-RT1/2` (realtime), `F-GT1` (ground truth), `F-G2.1` (ensayo G2) |
| **`D-NNN.N`** | **Decisión firmada**, con causa y fecha | Misma convención: `D-90.4` = cuarta decisión del doc 90; `D-113.1` = primera del doc 113. **No se re-litigan al redactar: se declaran con su justificación** |
| **`AF-1…AF-11`** | La **escala de conclusiones**: qué se afirma y **con qué fuerza** (establecida / direccional / tendencia / no cerrada) | Vive en síntesis §8 y `operacion/98`. **Es la tabla que hay que consultar antes de afirmar cualquier cosa en el informe** |
| **`L1…L8`** | Las **limitaciones canónicas**, lista cerrada | Referencia vigente: **`results/index.md` §Limitaciones** (la de `informe/99` §4.1 y la de la síntesis §9 pueden estar atrás). ⚠️ **Colisión: la Fase L del plan maestro usa `L0`/`L1` para sus hitos.** Escribir **"limitación L1"** vs **"hito L1"** |
| **`E-01…E-13`** | **Exclusiones de alcance** declaradas (`nucleo/10`) | Cada una con su justificación; ADR-015 las cerró |
| **`DA-01…DA-13`** | **Decisiones de arquitectura** del set (distintas de los ADR) | — |
| **`R-01…R-26`** | Los **redlines** del informe: "dice hoy / debe decir / evidencia" (`informe/93`) | ⚠️ **Colisión triple, la peor del set** — ver abajo |

**⚠️ Las tres colisiones de símbolos. Un externo las pisa sí o sí si no se las avisan:**

| Símbolo | Significado 1 | Significado 2 | Significado 3 |
|---|---|---|---|
| **`R…`** | **`R1–R4`** = los cuatro **resultados defendibles** (`nucleo/02`) | **`R1–R6`** = las seis **campañas de densidad** del clip bench | **`R-01…R-26`** = los **redlines** del informe (`informe/93`) |
| **`D1`** | **Dimensión de decisión 1** del tablero | **Campaña de Nivel A** `d1_gdinotiny560_edir_vs_eind` | **Campaña de Nivel B** con `edir_v1` |
| **`A1`** | **Primer argumento de defensa** (`nucleo/09`) | El **piloto de clase nueva** (`machinery`, doc 94) | El **gate A1** de censura de episodios cortos |

**Al redactar: nunca usar estos símbolos desnudos.** Escribir "la campaña R1", "el redline
R-13", "el argumento A1", "el piloto A1 de clase nueva".

### 4.2 IDs de campaña (✎ agregado 2026-08-10)

Las tablas de resultados usan estos IDs como filas, sin leyenda. Son **16 campañas con
artefacto**; cada una es **una combinación concreta**, y el contraste entre filas *es* el
experimento.

| ID | Qué varía respecto de la línea de base | Nivel |
|---|---|---|
| **T1** | Nada — es la **línea de base** (`gdino-tiny-560` + `v2_short` + escena) | B |
| **T2** | El **modelo** (`gdino-base-560`) | B |
| **D1** | Los **prompts** (`edir_v1`, evidencia directa de ausencia) | B (y hay un **D1 de Nivel A**, otro experimento) |
| **H1** | La **fusión** de estrategias (`hyb_or`) | B |
| **G1** | La **granularidad** (por sujeto en vez de por escena) — **la mejor del banco** | B |
| **B1** | El **vocabulario** (`bare_head` directo) | B |
| **R1–R6** | La **densidad de evidencia** (`stride` 7/15/26 × escena/sujeto) | B |
| **I1 / I2** | El **material**: estrato B (obra real no guionada), escena y sujeto | B |
| **NA1** | Nivel A **sobre video** (17 clips) | A |

### 4.3 Estrato A / estrato B — y el otro "estrato" (✎ agregado 2026-08-10)

- **Estrato A (Bloque A)** = los **34 clips del rodaje guionado** del 2026-07-25. Es donde
  vive el resultado principal.
- **Estrato B (Bloque B)** = los **13 clips del lote de internet**, obra real **no
  guionada**. Se reporta **como fila aparte, nunca fusionado al agregado del rodaje**
  (D-90.6).
- ⚠️ **No confundir con "estrato" del bench de IMÁGENES**, que son los tres estratos de
  `bench_v3` (`bench_obra` / `chv` / `shel5k`). Misma palabra, materiales distintos.

### 4.4 `estrato` ≠ `fuente` en el bench de imágenes (✎ agregado 2026-08-18)

Colisión que induce un error de atribución en el informe: **los nombres de los tres
estratos de `bench_v3` no son los nombres de las tres fuentes**.

| Fuente (dataset externo) | Licencia | Estrato que aporta | Imágenes |
|---|---|---|---|
| **`construction_site_safety`** (Roboflow Universe) | CC BY 4.0 | **`bench_obra`** | 147 |
| **`chv`** (académico, GitHub ZijianWang) | sin licencia formal, cita obligatoria | `chv` | 1.330 |
| **`shel5k`** (Mendeley 9rcv8mm682 v4) | CC BY 4.0 | `shel5k` | 5.000 |

Dos de los tres estratos se llaman igual que su fuente; **el primero no**.
**`bench_obra` no es un dataset externo ni una cuarta fuente**: es el **subconjunto
curado internamente** de los splits `valid` + `test` de `construction_site_safety`
v27. Su cadena de procedencia completa: 114 val + 82 test = **196** (el "BENCH
histórico") → auditoría de dominio del **2026-07-23** → se excluyen **49 imágenes**
ajenas al dominio de obra (selfies con barbijo, PASCAL VOC, aeropuerto, casino,
librería, karting) y **4 cajas `bare_head` de menos de 9 px²** → **147 imágenes**
(85 val + 62 test). Reglas codificadas en
`e-ovrt_datasets/datasets/scripts/curate/build_bench_obra.py`; justificación y
conteos en `datasets/registry/curation_bench_obra.md`.

Dentro de `bench_v3`, `bench_obra_val` y `bench_obra_test` cuentan como **un solo
estrato de 147**, no como dos.

**Al redactar:** "tres fuentes independientes" son **`construction_site_safety`, CHV
y SHEL5K**. Si el texto enumera `bench_obra` entre las fuentes, está nombrando un
estrato derivado como si fuera un dataset — y el lector queda creyendo que hubo
cuatro datasets. Frase apta para el informe: *"`bench_obra` es el núcleo interno
curado del BENCH de Construction Site Safety v27: conserva 147 de las 196 imágenes
originales de validación y prueba, tras excluir contaminación fuera del dominio de
obra y anotaciones subpíxel."*

## 5. Datos, modelos y bancos

| Término | Definición |
|---|---|
| **canonical_v2** | Vocabulario canónico de clases compartido entre repos: `person`, `helmet`, `vest`, `bare_head` (+ atributos `has_helmet`/`has_vest` solo en BENCH). Las vistas `*_cr01_cr02` están **eliminadas**. |
| **TRAIN / BENCH / DEMO** | Splits v2 de imágenes: 5540 / 196 / 1064. El BENCH de imágenes mide percepción (AP por clase, recall CR-01). ⚠️ ✎ **2026-08-10 — el "BENCH de 196" NO es el banco vigente y no se cita**: se auditó como **20–25% fuera de dominio** (selfies de COVID, PASCAL VOC, aeropuerto — doc 63) y se conserva solo como artefacto histórico. **El banco de imágenes vigente es `bench_v3`: 6.477 imágenes**, congelado el 2026-07-23, estratificado sobre **3 fuentes independientes** — `construction_site_safety` (Roboflow Universe, CC BY 4.0), `chv` y `shel5k`. Sus **estratos** son `bench_obra` (147) · `chv` (1.330) · `shel5k` (5.000). ⚠️ **`bench_obra` NO es una cuarta fuente ni un dataset externo**: es el nombre del **estrato curado internamente a partir de `construction_site_safety`** — ver `estrato ≠ fuente` en §3. **Reportar siempre por estrato Y agregado, nunca solo el agregado** (el agregado está dominado por `shel5k`, 77%). |
| **clip bench** | El banco de **video** con GT temporal (`processed/clip_bench/`, spec 43). ✎ **2026-08-10 — corregido: decía "1 clip promovido (`cb_b01_p7`) en `gt_preliminary`". Doblemente falso**: ese clip fue **RETIRADO** el 2026-08-03 (licencia sin registrar + GT generado por IA) y **no debe citarse**. **Hoy el banco tiene 47 clips con GT HUMANO** = 32 positivos / 15 negativos / **37 episodios**, manifest `3f14f50a…`, en dos bloques: **A** = rodaje guionado (34) y **B** = lote de internet (13). Es el escenario EBE oficial del informe. |
| **video-gt-lab** | El pipeline semiautomático de GT temporal: `prepare_clip` → preanotación (GDINO-**base** anti-circularidad + ByteTrack) → CVAT (humano) → `derive_clip_gt` → `validate` → `promote_clip`. |
| **`gt_preliminary`** | Estado de un GT sin pasada humana (anotador `claude-vision-preliminary`). Ver regla de oro #7. |
| **GDINO / MM-GDINO / YOLOE** | Las tres familias de modelos OVD evaluadas. ✎ **2026-08-10 — cifra actualizada: el campeón es `gdino-tiny-560` con mAP50 0,551 sobre `bench_v3` (6.477 imgs)**, no el 0,441 del BENCH viejo. Licencias: GDINO y MM-GDINO **Apache-2.0**, YOLOE **AGPL-3.0** (registro en `license_registry.md` §PESOS DE MODELO). Hallazgos clave: **YOLOE es ciego a `bare_head`** (recall CR-01 ≈ 0); MM-GDINO-tiny descartado (bboxes rotas). Pista doble del núcleo (doc 12 §3): GDINO-tiny primaria + YOLOE-26s réplica. |
| **OAK-D Pro PoE** | Cámara edge con NPU (DepthAI). Fuente viva `oak_d` del media-plane; trae IP estática de fábrica 169.254.1.222. |
| **prompt set** | Conjunto versionado de prompts con ciclo de vida (`exploratory` → `frozen`, con `frozen_sha256`). ✎ **2026-08-10 — corregido: `eind_v1` y `edir_v1` están `frozen` con sha256 desde el 2026-07-29 (acta del usuario, doc 76). Ya no esperan nada.** Texto anterior: `eind_v1` está `frozen_pending_review` (espera el **acta** del usuario que desbloquea D1). |
| **pattern set** | Conjunto versionado de patrones del control-plane. El oficial es **`cr01_cr02_v2`** (escena, 4000/7000 ms, sin cooldown ni memoria de cobertura). |

## 6. Nombres de repos y puertos

| Cosa | Valor |
|---|---|
| Repos de código | `e-ovrt_media-plane`, `e-ovrt_control-plane`, `e-ovrt_experimental-setup`, `e-ovrt_datasets` (hermanos en disco; el acople cross-repo asume esa disposición) |
| Este repo | `docs/` — git propio, con remote (`e-ovrt_docs`) desde 2026-08-10, cuando el equipo empezó a necesitar acceso ✎ *(decía "local sin remote": esa fue la decisión inicial del 2026-07-09, superada al sumar redactores externos)* |
| Puertos | media :8080 · control :8081 · **distribución :8082** · BFF webconsole :8090 · frontend dev :5173 |
| Entry points | `uvicorn --factory eovrt_media.service.app:create_app` · `eovrt-control serve` · `eovrt-distribute serve` |
