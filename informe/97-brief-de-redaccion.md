# 97 — Brief de redacción del informe final

> # ⚠️ LEER ESTO ANTES QUE CUALQUIER OTRA COSA DE ESTE DOCUMENTO (2026-08-10)
>
> **Este brief quedó atrás del cierre experimental, y su §5 se autodeclara "cifras
> canónicas relevadas contra disco". Lo era el 2026-08-05; hoy NO.** Entre el 08-06 y el
> 08-09 entró todo el tramo de video (el lote de internet) y hubo una **revisión ciega del
> GT** que cambió cifras publicadas. Si escribís el capítulo con las cifras de §5 tal como
> están, escribís **la versión de hace tres jornadas con etiqueta de verificada**.
>
> **LA FUENTE DE CIFRAS ES `e-ovrt_experimental-setup/results/index.md` Y SUS 4 ÍNDICES.
> SIEMPRE. Este §5 pasa a ser referencia histórica.**
>
> Lo que cambió, concretamente:
>
> | Este doc dice | Vigente |
> |---|---|
> | Banco de **34 clips**, 35 episodios, manifest `cef5082e…` (§5.1) | Banco de **47 clips** = 32 positivos / 15 negativos / **37 episodios**, manifest `3f14f50a…` |
> | *"Al citar el denominador, decir **34 episodios evaluables sobre 35**"* (§5.1) | Esa regla vale **solo para el sub-banco del rodaje**. El banco completo son 47 clips; al citar hay que decir de qué bloque se habla (**A** = rodaje, **B** = lote de internet) |
> | **12 campañas** | **16 campañas** con artefacto (14 en `clip_bench` + 2 en `bench_nivel_a`) |
> | *"los 14 clips del lote de internet están cortados pero **sin GT**"* (§3, §5.7) | **13 de 14 tienen GT humano** desde el 08-09 (`v08_c01` excluido con causa firmada). §5.7 ya no describe un futuro: **ya pasó** |
> | *"FAR/hora **NO es una métrica de este trabajo**"* (§5.6) | **Se computa y se reporta** (29,2 escena / 1.850,8 sujeto), pero **no sostiene una cota**. Fórmula de cita obligatoria: **"3 y 190 FP en 6:09,6 del único clip soak"**, con la tasa horaria como derivada (limitación **L1 precisada**, no derogada) |
> | *"D1/H1/T2/B1 son las únicas que el verificador NO chequea"* (cabecera) | Desde el 08-09 el verificador cubre **19 cifras sobre las 16 campañas**, con un guard que falla si aparece una campaña sin verificar |
> | §4: *"la redacción NO arranca todavía"* | ✎ **LEVANTADO el 2026-08-10**: la redacción **está habilitada** y es el carril principal |
>
> **Lo que este brief SÍ conserva vigente y hay que respetar:** §1 (registro y estilo),
> §2 (jerarquía de fuentes), §3 (reglas de honestidad experimental) y §5.5 (el número de
> A1). Son las partes que no dependen de qué se midió.

- **Fecha:** 2026-07-18 · **§5 reescrita el 2026-08-05 y relevada contra disco el mismo
  día** (ver el banner de esa sección: la tabla anterior citaba un clip retirado del
  banco). El relevamiento cotejó una por una las 4 filas de §5.1, las 3 de §5.2, §5.3,
  los tres sha256 y el número de A1 contra el `metrics.json`/`manifest` correspondiente:
  **coinciden todas**. Las cifras de §5.1 de D1/H1/T2/B1 son las únicas que
  `96-verificar-indices.py` **no** chequea (solo cubre T1, G1 y R1–R6), así que se
  verificaron a mano.
- **Propósito:** las reglas de redacción para escribir/reescribir el informe (el
  `.docx`/Google Docs) a partir de este set documental. Pensado como instrucción
  operativa para el asistente (LLM) que ayude a redactar en el Project de claude.ai.
- **Complementa:** doc 13 (glosario y jerarquía de verdad), doc 93 (los redlines a
  resolver), doc 94 (el texto modelo), y **para cifras los cuatro índices de
  `results/`** (ver §2 y §5).

---

## 1. Registro y estilo

- **Registro formal impersonal**, tiempo presente para el diseño ("el plano de control
  evalúa…") y pretérito para lo ejecutado ("la corrida produjo…"). Sin voseo, sin
  primera persona singular. Primera persona plural solo donde el resto del informe ya
  la usa.
- **El modelo de estilo es el doc 94** (`94-secciones-nuevas-etapa3.md`): así se
  escribe una sección nueva. El doc 90/96 muestran el estilo del documento existente
  al que hay que integrarse.
- Terminología: usar **exactamente** los términos del glosario (doc 13) y de la §17.1.
  No introducir sinónimos nuevos para conceptos ya nombrados (p. ej. no alternar
  "plano de medios" / "media-plane" dentro de una misma sección: seguir la convención
  de la sección del informe donde se escribe; el informe usa los nombres en español
  con el nombre técnico entre paréntesis en la primera mención).
- Los nombres de artefactos, campos y contratos van en `monoespaciado` y **no se
  traducen** (`detections.jsonl`, `confirm_after_ms`, `media.detection.v1`).
- No usar viñetas donde el informe usa prosa; el capítulo 17 es mayormente prosa con
  tablas numeradas.

## 2. Jerarquía de fuentes al redactar

1. **Cifras y contratos** (✎ actualizado 2026-08-05): de los **cuatro índices de
   `e-ovrt_experimental-setup/results/`** — que son los que se verifican
   mecánicamente contra los `metrics.json` en disco
   (`operacion/datos/96-verificar-indices.py`) — con la §5 de este doc como atajo, y
   `operacion/98` para las conclusiones transversales. Si un número no está ahí,
   **no existe** para el informe (regla del doc 95: ninguna cifra estrella sin
   artefacto). *El doc 92 de `informe/` y el 56 de `operacion/` quedaron superados
   como fuente de cifras: 92 es la extracción del texto de Etapa 3 y el 56 fue
   reemplazado por `operacion/97`.*
2. **Estado de la plataforma:** **`operacion/97`** (reemplaza al 56). Nunca del cuerpo
   de docs 32/36/50 ni de fragmentos sin banner.
3. **Decisiones y sus porqués:** ADR-001…**015** + doc 10 (alcance/exclusiones). (✎
   2026-08-06: *decía "…014"* — faltaba el **ADR-015**, cierre de alcance del
   2026-08-05: el alcance CRECIÓ en E-03/E-07/E-13, MQTT declarada NO implementada,
   puerta cerrada hasta la defensa.) Las decisiones **no se re-litigan** en el
   informe: se declaran con su justificación.
4. **Protocolo y definiciones metodológicas:** §17.1 (doc 96b). El informe nuevo debe
   ser consistente con ella; si la implementación se desvió del protocolo, la
   desviación **se declara** (los casos conocidos ya están relevados en docs 91/93).
5. **Qué escribir:** el doc 93 es el tablero — **26** redlines (**R-01…R-26**) con "dice
   hoy / debe decir / evidencia". El doc 94 ya trae texto redactado listo para adaptar.
   *(✎ corregido 2026-08-05: acá decía "24 (R-01…R-24)". R-25 y R-26 se agregaron
   después, y el propio doc 93 marca a **R-26 como "la más valiosa"** (§17.3.17/18, texto
   en doc 94 §9) — con el número viejo se saltaban los dos mejores sin enterarse.)*
6. **Figuras, tablas, reproducibilidad, licencias, limitaciones y mecanismos:**
   `informe/99-materiales-de-cierre.md` (2026-08-05). Trae el inventario de figuras y
   tablas con su artefacto de origen, el anexo de reproducibilidad con los sha256
   verificados, las citas obligatorias por dataset, las limitaciones L1–L8 y el catálogo
   de mecanismos. **Su §6 lista 6 hallazgos: 4 CERRADOS el 2026-08-05** (incluida la
   procedencia del lote de internet, que era la bloqueante) **y 2 abiertos** —
   licencias de los catálogos de modelos, y la convención de cita de las dos series de
   ADR (✎ esta última bajada al glosario doc 13 el 2026-08-06). *(✎ corregido
   2026-08-06: decía "6 decisiones abiertas, una bloqueante".)*

## 3. Reglas de honestidad experimental (no negociables)

- **GT del banco: ✎ ya NO es preliminar (actualizado 2026-08-05).** Los **34 clips del
  rodaje están `gt_ready`** en el manifest, con pasada humana de CVAT y seis bordes
  adjudicados con firma (docs 80/81; `clip_gt.v2` con `provenance.xml_sha256`). O sea
  que **sus métricas SE REPORTAN COMO RESULTADO**, no como verificación de la mecánica.
  La regla anterior —presentarlas como "verificación" mientras el GT fuera
  `gt_preliminary`— **ya no aplica al banco y no debe usarse**: aplicarla hoy
  subestimaría el resultado principal del trabajo. ~~Sí sigue vigente para material sin
  pasada humana: los 14 clips del lote de internet están cortados pero sin GT (esperando
  CVAT), y cualquier cifra sobre ellos es provisoria hasta que se integren.~~
  > ✎ **2026-08-10 — esa salvedad ya no aplica: EL LOTE TIENE GT HUMANO.** 13 de 14 clips
  > (`v08_c01` excluido con causa firmada), banco **47**. **Sus métricas también se
  > reportan como RESULTADO**, no como provisorias. Y trajeron un resultado propio que hay
  > que contar: la **revisión ciega del GT** (doc 113 §B) encontró que **5 de las 7
  > declaraciones de episodio del lote eran errores de anotación**, todas sobre-declarando
  > donde el estado no era observable ⇒ **la calidad del GT es un resultado en sí**, y el
  > estrato quedó con **2 episodios evaluables**. Consecuencia de redacción, no negociable:
  > **con n=2 no se rankean granularidades** (`scene` 0,333 vs `subject` 0,190 **no** es
  > "escena gana": es ruido, F-111.1 enmendado). Lo robusto es la **asimetría de FP**:
  > 26 vs 323 sobre 11 negativos (12×). Ver síntesis §5.1.
- **Lo no hecho se registra, no se esconde** (✎ lista actualizada 2026-08-05):
  distribución MQTT (spec 45) no implementada · **campaña EBE de punta a punta por el
  bus contra GT** no ejecutada (falta el ancla wallclock↔media **como ingeniería de
  campaña**, doc 101 §3; el ancla *puntual* sí quedó cerrada con reloj externo en el
  humo anclado del doc 101 §5.4 —las 4 patas, ancla física +1.066 ms—, que es una toma,
  no un banco: **no confundir las dos cosas al redactar**; el eje se cubre por proxy de
  densidad + humos verdes) · `hyb_and` **no ejecutada con causa** (no medible
  contra este banco sin romper la comparabilidad, D-90.4) · **CR-02 a Nivel A no
  cerrado** (un estrato, IC solapados) · tracker **no medido en obra real con
  multitud** (L4) · FAR/hora **limitación declarada**, no métrica (D-90.1). *Quedaron
  obsoletos en esta lista: "tracker sin productor de `track_id`" (G1 es capacidad
  operativa config-driven, verificada en DBE 34/34 y en vivo, doc 91), "D1 sin correr"
  (corrió: veto de precisión, doc 85) y "pasada humana CVAT pendiente" (hecha para el
  rodaje).* El registro honesto se redacta desde `operacion/98` §6 y los índices de
  `results/`, no desde el doc 91 §7, que es anterior al tramo experimental.
- **Estados de aplicabilidad:** cuando una métrica no aplica, el informe usa el
  lenguaje del ADR-006/013 ("se declara `not_applicable/non_temporal_source`"), no
  frases vagas ("no se pudo medir").
- **La tesis no es "OVD detecta mejor"** (doc 09). Toda comparación con modelos
  cerrados se encuadra en extensibilidad y costo de adaptación, no en supremacía de
  detección. Ante números flojos de detección: el argumento es la *plataforma que los
  mide y los mejora sin re-entrenar*.
- **`re_alerts` no son falsos positivos**; el doc 52 fija la semántica.

## 4. Mecánica de trabajo en el Project

> ✅ **PUERTA ABIERTA — 2026-08-10.** ~~*Puerta de secuencia (orden del usuario,
> 2026-08-05 — `informe/99` §7): la redacción de §17.x NO arranca todavía. Primero (1) el
> CVAT del lote de internet con sus runs/evals (estrato B), después (2) los videos V1–V3,
> y recién ahí la redacción.*~~
>
> **Los dos precedentes se cumplieron o dejaron de bloquear:** (1) el CVAT del lote
> **está hecho** —13 de 14 clips con GT, campañas corridas y re-evaluadas tras la revisión
> ciega (`operacion/113` §B)—; (2) los videos V1–V3 y las URLs de los clips pasaron a
> **carril paralelo** por decisión del usuario del 08-10, porque no bloquean escribir.
> **La redacción es hoy el carril principal**, y la escriben **dos integrantes del equipo
> que no participaron del tramo experimental** — de ahí que este brief haya necesitado el
> banner de cabecera.

- El `.docx` **no se edita desde el repo**: los redlines se resuelven en Google Docs.
  El chat produce texto listo para pegar + la casilla del redline que salda.
- Al redactar una sección: (1) identificar el redline del doc 93 que la cubre, (2)
  levantar la evidencia **de los cuatro índices de `results/` + `operacion/97`** (✎
  corregido 2026-08-05: **no** del doc 92/56, que §2.1 ya derogó como fuente de cifras;
  este paso decía "doc 92/56" y contradecía la jerarquía), (3) partir del texto del
  doc 94 si existe, (4) devolver el texto final + qué redline queda saldado.
- Trabajar por bloques del plan del doc 91 §8: A contradicciones → B concreción →
  C evidencia → D erratas. Del doc 95 sigue vigente **§5.5 (el orden de sacrificio)
  — salvo su ítem 1, derogado por los hechos: G1 se implementó y es el mejor
  resultado del banco (ADR-015 E-03)**;
  su cronograma (§5.1 y §5.4, con "GRABAR EL BANCO" en la semana 2–3) es **histórico
  pre-rodaje** y no debe leerse como pendiente.
- Si el asistente detecta una contradicción entre docs, **no la resuelve en silencio**:
  la señala, propone la resolución según la jerarquía del doc 13 §1, y la registra
  como pendiente si no puede decidirse con lo disponible.

## 5. Números canónicos de referencia rápida

> ✎ **ACTUALIZADA 2026-08-05 · RELEVADA CONTRA DISCO EL MISMO DÍA.** La versión anterior de esta tabla (fechada
> 2026-07-18) quedó superada por el tramo experimental completo y **encabezaba con un
> número inválido**: el benchmark del clip `cb_b01_p7`, que fue **retirado del banco el
> 2026-08-03** (licencia/consentimiento sin registrar + GT generado por IA; ver
> `datasets/processed/clip_bench/_retired/cb_b01_p7/MOTIVO.md`). Citar de ahí habría
> reintroducido exactamente la falla que el doc 95 §2.1 denunció ("el número estrella
> del TFG no tenía respaldo en el repo"). También estaban superados el mAP del BENCH v2
> y el split `BENCH 196` (auditado 20-25% fuera de dominio, doc 63).
>
> **Fuente de verdad actualizada:** los cuatro índices de
> `e-ovrt_experimental-setup/results/` (`bench_imagenes/`, `bench_nivel_a/`,
> `clip_bench/`, `realtime/`) + doc 98 (conclusiones transversales) y doc 97 de
> `operacion/` (estado de plataforma, reemplaza al 56). **Los índices se verifican
> mecánicamente** con `operacion/datos/96-verificar-indices.py` (chequea que cada cifra
> citada coincida con el `metrics.json` en disco): correrlo antes de volcar cifras.
> Esta tabla sigue siendo **solo un índice**: verificar en el artefacto antes de citar.

### 5.1 Alertas sobre video — Nivel B, el resultado principal (banco de 34 clips)

> ⚠️ **Esta sub-tabla describe SOLO el Bloque A (el rodaje guionado), y sigue siendo
> correcta para él.** Lo que falta acá es el **Bloque B (lote de internet, 13 clips)**,
> que entró después. **Banco completo hoy: 47 clips / 37 episodios.** Las cifras del
> estrato B y su lectura obligada están en `results/clip_bench/index.md` y en la
> **síntesis §5.1**. Al citar, decir **de qué bloque** se habla: "34 evaluables sobre 35"
> es el denominador del **rodaje**, no del banco.

Banco: 34 clips del rodaje 2026-07-25, 35 episodios (CR-01 28 / CR-02 7), GT humano,
`manifest.yaml` sha256 `cef5082e…`. Micro por episodio; los 4 clips negativos quedan
fuera de P/R/F1 y se reportan como control de FP (F-EV1).

> **Al citar el denominador, decir "34 episodios evaluables sobre 35".** Las 12
> campañas traen `episodes_censored: 1` / `episodes_evaluable: 34`: hay un episodio
> censurado que no entra al micro (mecanismo `metric_censored`, enmienda A2 del doc 58).
> Escribir "35 episodios evaluados" es incorrecto.

| Campaña | Combinación | Recall | Prec. | **F1** | t_alert | TTFD | FP neg |
|---|---|---|---|---|---|---|---|
| **T1** | tiny-560 + `v2_short` + escena (**núcleo**) | 0,824 | 0,757 | **0,789** | 5.327 ms | 168 ms | 0/4 |
| **G1** | ídem + granularidad por sujeto (**mejor del banco**) | 0,971 | 0,892 | **0,930** | 5.236 ms | 168 ms | 0/4 |
| D1 | `edir_v1` (E-DIR) | 0,176 | 0,146 | 0,160 | 6.611 ms | 847 ms | 2/4 |
| H1 | fusión `hyb_or` | 0,353 | 0,255 | 0,296 | 6.956 ms | 113 ms | 2/4 |

**La cifra de la histéresis (F-81.1), que esta tabla no muestra:** en T1, **CR-02
confirma 7/7 = recall 1,000 con SDR 0,281** — la evidencia de chaleco aparece en ~1 de
cada 6 frames y el patrón temporal la acumula igual, pagando `t_alert` (8.572 vs
4.314 ms de CR-01). SDR por campaña: T1/G1 0,698 · T2 0,819 · D1 0,210 · H1 0,738 ·
B1 0,940.

Artefacto: `results/clip_bench/<campaign_id>/metrics.json` (+ `evals/`, `campaign.yaml`,
`provenance.json`). Tabla completa con T2/B1 y desglose por escenario/condición:
`results/clip_bench/index.md`.

**Veredicto del eje (criterios pre-registrados en `nucleo/04` §8):** E-IND **0,789**
núcleo · E-DIR **0,160** descartada por **veto de precisión** (0,146 < 0,5) · E-HYB-or
**0,296** no supera a la mejor individual. `hyb_and` **no ejecutada con causa**
(D-90.4). **La ganancia de G1 es 100% del motor**: SDR y TTFD idénticos a T1 porque las
detecciones son bit a bit las mismas.

### 5.2 Percepción sobre imágenes — banco `bench_v3`

Banco congelado 2026-07-23: **6.477 imágenes**, 3 fuentes independientes
(`bench_obra` 147 = 85 val + 62 test · `chv` 1.330 · `shel5k` 5.000), 55.165
anotaciones, sha256 `4557024e…`. **Reportar siempre por estrato y agregado, nunca solo
el agregado** (L5: el agregado está dominado por `shel5k`, 77%).

| Modelo | mAP50 `bench_v3` | mAP50 `bench_obra` | recall CR-01 (n=5.313) |
|---|---|---|---|
| **`gdino-tiny-560`** (campeón) | **0,551** | 0,503 | 0,308 |
| `gdino-base-560` (especialista en `bare_head` —evidencia de CR-01— y en `vest`/CR-02; ✎ 2026-08-06, *la etiqueta "CR-02/`bare_head`" mezclaba los ejes*) | 0,525 | 0,474 | **0,599** |
| `yoloe-26x` | 0,442 | 0,405 | **0,000** |

Artefacto: doc 64 (selección S1/S2 + confirmación B5) y doc 66; índice:
`results/bench_imagenes/index.md`.

### 5.3 Estado por persona — Nivel A

CR-01 E-IND: F1 **0,546** (`shel5k`, n=2.487 violadores, IC no solapados) / **0,408**
(`bench_obra`, n=28). CR-02 E-IND: F1 **0,479** (`bench_obra`, n=82) — **CR-02 NO está
cerrado a Nivel A**: un solo estrato con IC solapados, se declara. Umbrales calibrados
en mitad A, métricas sobre mitad B. Artefacto: doc 83/84 + `results/bench_nivel_a/`.

### 5.4 Tiempo real y latencia

| Resultado | Valor | Artefacto |
|---|---|---|
| G2A single-host (video) | p50 **14,7 ms** / p95 **31,8 ms** (presupuesto 50–250 ms) | `operacion/datos/39-*` |
| G2A live GDINO sobre OAK-D | p95 **630–890 ms** → **fuera** de presupuesto | doc 71 §2.1 |
| G2A live YOLOE sobre OAK-D | p95 **225–249 ms** → dentro, pero **inservible para la condición** (F-RT2) | doc 71 §2.1/2.3 |
| Techo de fps y su causa | contención de **GIL** (F-RT3); palanca F-RT5 aplicada: **3,75 → 4,42 fps**, −14,4% latencia, p = 0,0195 | docs 73/74 |
| **Calidad bajo densidad del live** | escena: 0,794 @4,29 fps → 0,646 @1,15 · sujeto: 0,866 → 0,742. **F-96.4: la ganancia de la identidad excluye el cero en las 4 densidades** | doc 96 + `results/clip_bench/` §densidad |
| Verificación temporal en vivo (claqueta) | política **4.142 ms** vs `confirm_after_ms` 4.000 · relojes de los dos procesos con **4 ms** de residuo · ancla física tono→fotón **+1.066 ms** | doc 101 §5.4 |
| Prefilter EN-2 (A/B real con GDINO) | **87% drop** on-device (solo `source.type: oak_d`) | doc 10 E-07 |
| Paridad replay↔stream | **byte-idéntica** (verificada por mutación); `bus_dropped_events = 0` en las 6 corridas del rodaje, L0 y regresión | docs 37/65/71/91 |

> ⚠ **F-101.8 — advertencia obligatoria al citar G2A** (doc 101 §5.5): `G2A` se mide
> desde el **dequeue en el host**, no desde la captura del fotón. La latencia
> vidrio→alerta suma `capture_to_host_ms`, que varía un orden de magnitud con el estado
> de la fuente: **202–217 ms** (medianas de las 6 corridas del rodaje) y **1.600 ms** en
> las tomas del 08-05. Está instrumentado por frame, así que **es declarable**; no
> presentar G2A como latencia vidrio→alerta sin este término.

### 5.5 Extensibilidad — el número de A1

**0 entrenamientos · 1 archivo de 48 líneas · 9 minutos · 0 GT nuevo anotado**, y
`machinery` **AP@0.5 0,662** zero-shot (n=99 cajas) sobre clases que la plataforma
jamás configuró — **supera el mAP50 agregado del campeón con sus clases configuradas**.
Artefacto: doc 94 + `datos/94-piloto-clase-nueva/`.

> **F-94.1, el contrapeso que va junto al número:** la palabra debe alinear con la
> taxonomía del despliegue (`vehicle` junto a `machinery` da 0 detecciones; aislada, AP
> 0,026 porque el 67% cae sobre lo que ese GT llama `machinery`). Versión fuerte de A1:
> agregar la clase cuesta minutos **y validar la palabra también**. Segundo caso
> independiente medido el 2026-08-05 (`gloves` sobre el material del rodaje: 252
> detecciones, **ninguna sobre un guante** — caían sobre el casco amarillo;
> `experimental-setup/defensa/README.md` §V2).

### 5.6 Configuración y datos de referencia

| Ítem | Valor | Artefacto |
|---|---|---|
| Umbrales oficiales | CR-01 `confirm_after_ms` 4000 / `resolve_after_ms` 2000 · CR-02 7000 / 3000 | `cr01_cr02_v2.yaml` (**nunca `v1`**) |
| Pattern set vigente | `cr01_cr02_v2` (escena) / `cr01_cr02_v2_subject` (sujeto) | control-plane `configs/patterns/` |
| Prompt set congelado | `cr01_cr02_v2_short`, `frozen_sha256 df81fd48…` | `experimental-setup/prompts/` + acta doc 76 |
| Splits de imágenes v2 | TRAIN **5.540** / DEMO **1.064** (el viejo "BENCH 196" está **descartado**: 20–25% fuera de dominio, doc 63 — el banco de evaluación es `bench_v3`) | registry `datasets` |
| FAR/hora | ⚠️ **FILA SUPERSEDIDA (✎ 2026-08-10).** Decía *"NO es una métrica de este trabajo"*. **D-90.1 quedó PRECISADA, no derogada** (limitación **L1**): con el clip soak del estrato B (0,1027 h) la métrica **se computa y se reporta** — **29,2** (escena) y **1.850,8** (sujeto) FA/hora — pero **no sostiene ninguna cota**, porque harían falta 3 h de cumplimiento anotado. **Fórmula de cita obligatoria: "3 y 190 FP en 6:09,6 del único clip soak", con la tasa horaria como derivada.** Nunca escribir "≤N FA/hora" ni la tasa desnuda. La evidencia principal sigue siendo el **control de negativos** | `results/index.md` §L1 |

### 5.7 ~~Lo que puede cambiar cuando llegue el GT del lote de internet~~ → **YA LLEGÓ: qué cambió de hecho**

> ✎ **2026-08-10 — esta sección describía un futuro que ya ocurrió.** Se conserva la
> predicción original abajo porque **acertó**, y eso es citable: lo que se dijo que se
> movería se movió, y lo que se dijo que no, no.

**Predicción original (2026-08-05):** *"Pendiente externo (14 clips ya cortados, sin GT).
Al integrarse **como estrato B con desglose obligatorio** (recomendación D-90.6) puede
moverse: el **agregado** del clip bench, el texto de **L4** (la limitación más citable —
un solo bloque guionado), y el contexto de soak. **No se mueven**: los mecanismos (F-81.x,
F-85.x, F-87.2, F-88.x, F-89.x, F-96.x, F-101.x), el veredicto del eje ni las cifras por
estrato ya publicadas."*

**Lo que efectivamente pasó:**

- **Se movió lo previsto.** El banco pasó a **47 clips**; **L4 quedó precisada** (D-113.1:
  hay obra real medida, pero acotada, y su contenido nuevo es la **frontera de
  juzgabilidad** — escala × iluminación × oclusión); y el soak apareció (`v06_c01`,
  0,1027 h), lo que movió **L1** de "no reportable" a "se reporta sin sostener cota".
  Bonus no previsto: **L6** también se movió (el tracker quedó medido en multitud real).
- **No se movió nada de lo que se dijo que no.** Los mecanismos, el veredicto del eje y
  las cifras por estrato del rodaje están intactos.
- **Lo que la predicción NO anticipó, y es el hallazgo mayor del tramo:** que la **calidad
  del GT sería un resultado**. La revisión ciega encontró **5 de 7 declaraciones de
  episodio erróneas**, todas sobre-declarando donde el estado no era observable. El
  estrato quedó con **2 episodios evaluables** ⇒ **de ahí no sale ningún ranking**.

**Fuente vigente de todo esto:** `results/clip_bench/index.md` §Estrato B y **síntesis
§5.1**; el registro operativo, en `operacion/111`, `112` y `113` §B.
