# 99 — Materiales de cierre del capítulo de resultados

- **Fecha:** 2026-08-05 · **✎ Actualizado 2026-08-10** — puesto al día al mundo
  **post-estrato-B**: §1 (banco 47 + filas nuevas del tramo de video T-82…T-84/FIG-F),
  §2 (freeze vigente + alcance real de los verificadores), §3.1/§4.1 (el lote ya tiene
  GT; L1/L4/L6 en su formulación vigente), §5 (mecanismos nuevos del video) y §6
  (puerta de redacción levantada). Cifras verificadas contra los índices de `results/`
  (verificadores 96 y 109 en verde ese día).
- **Ojo con el número:** existe también `operacion/99-relevamiento-datasets-imagenes.md`.
  Este es **`informe/99`**. Al citarlo, decir la carpeta.
- **Qué es esto:** los cinco materiales que se pudieron cerrar **sin depender del GT del
  lote de internet** (✎ el GT llegó — docs 102–111 — y el armado sobrevivió como estaba
  diseñado), armados y verificados contra artefacto. Es el andamio del capítulo:
  inventario de figuras/tablas, anexo de reproducibilidad, licencias y citas,
  limitaciones + ADRs, y el catálogo de mecanismos.
- **Qué NO es:** **no es redacción de §17.x.** Acá no hay prosa de capítulo; hay
  inventarios, tablas de procedencia y texto declarativo corto (licencias,
  limitaciones). ✎ 2026-08-10: la orden que difería la redacción quedó **levantada** —
  los runs del lote corrieron (docs 109–113) y la redacción está habilitada y es el
  carril principal (banner de `informe/97`).
- **Se lee junto a:** `informe/97` (reglas de redacción; ⚠️ su §5 de cifras quedó
  histórica el 08-10 — **cifras solo de los índices de `results/`**),
  `informe/98` (manifiesto del Project), `operacion/98` (conclusiones transversales) y
  los cuatro índices de `e-ovrt_experimental-setup/results/`.
- **§6 es lo importante si vas con poco tiempo:** los 6 hallazgos que este armado destapó.
  **Cuatro quedaron cerrados el mismo día** (procedencia del lote de internet ·
  consentimiento del rodaje · ADR-015 escrito, aceptado y aplicado · lista canónica de
  limitaciones L1–L8) **y el de las dos series de ADR se cerró el 2026-08-06**
  (convención bajada al glosario doc 13). **El de los catálogos de modelos se cerró el
  2026-08-10** — y la premisa era falsa: los 11 catálogos sí declaran licencia; lo que
  faltaba era el registro, ya escrito (§6, fila 3). **Sigue abierto solo el residual
  del hallazgo 1:** URL + fecha de acceso por video (C1 del doc 113 — del usuario).

---

## 1. Inventario de figuras y tablas, con su artefacto de origen

**Numeración.** El capítulo cierra en la **Tabla 60**; el doc 94 ya ocupa **61–67**. Las
de acá se proponen desde **68**, y el doc 93 advierte verificar colisiones al
transcribir. Los identificadores `T-nn`/`FIG-x` son **de trabajo**, no del informe.

**Columna «insumo»** — verificada contra disco el 2026-08-05 (✎ filas del tramo de
video T-82…T-84 y FIG-F agregadas y verificadas el 2026-08-10):
`✅ en disco` = el artefacto existe y la tabla se llena copiando · `⚙ generar` = hay que
correr un script sobre artefactos que existen · `📐 spec` = está especificada pero no
producida.

**Columna «redline» — tentativa.** Sale del *encabezado* de cada redline en el doc 93, no
de su cuerpo. Los marcados con `?` son inferencia mía y hay que confirmarlos leyendo el
"DEBE DECIR" antes de darlos por saldados. Los seguros son R-09 (que es literalmente una
especificación de figura, doc 94 §4), R-12 y R-13 (ambos "Sección nueva al cierre ·
EVIDENCIA") y R-26 (§17.3.17/18, extensibilidad).

| ID | Tabla / figura | Artefacto de origen | Redline | Insumo |
|---|---|---|---|---|
| T-68 | **Campañas de Nivel B sobre el banco del rodaje (Bloque A)** (T1, T2, G1, D1, H1, B1: R/P/F1, `t_alert`, TTFD, SDR, FP neg) — ✎ 08-10: el censo vigente de `clip_bench` es de **14 campañas** (estas 6 + R1–R6 de T-71 + I1/I2 de T-82) | `results/clip_bench/index.md` + `*/metrics.json` | R-12/R-13 | ✅ en disco |
| T-69 | Desglose **por escenario** P1–P9 | `results/clip_bench/index.md` §Detalle por escenario | R-12 | ✅ en disco |
| T-70 | Desglose **por condición** CR-01 / CR-02 | idem §Detalle por condición + `metrics.json → by_condition` | R-12 | ✅ en disco |
| T-71 | **Eje de densidad** R1–R6 (30 / 4,29 / 2,0 / 1,15 fps × escena/sujeto) | `results/clip_bench/index.md` §Eje de densidad + `operacion/96` | R-13 | ✅ en disco |
| T-72 | **Selección de modelos** sobre `bench_v3` (mAP50 por modelo × estrato) | `results/bench_imagenes/index.md` §2 + `operacion/64` | R-13? | ✅ en disco |
| T-73 | **AP por clase y por estrato** (la asimetría estructural) | idem §Por clase y por estrato + `operacion/66` | R-13? | ✅ en disco |
| T-74 | **Nivel A**: E-DIR vs E-IND por condición y estrato, con IC | `results/bench_nivel_a/d1_*/metrics.json` | R-12 | ✅ en disco |
| T-75 | **Latencia y tiempo real**: G2A single-host, G2A live por modelo, presupuesto | `results/realtime/index.md` §2/§3 + `operacion/39`, `71` | R-05?/R-14? | ✅ en disco |
| T-76 | **Integridad del acople EBE**: paridad, `bus_dropped_events`, 1:1 | `results/realtime/index.md` §1 + `operacion/37`, `65`, `91` | R-04? | ✅ en disco |
| T-77 | **A1 — costo de una clase nueva** (0 entrenamientos / 48 líneas / 9 min / AP 0,662) | `operacion/datos/94-piloto-clase-nueva/resultados.json` | R-26 | ✅ en disco |
| T-78 | **Composición del banco de clips** — ✎ 08-10: **47 clips en dos bloques** (A rodaje 34 · B lote de internet 13), **32 positivos / 15 negativos, 37 episodios**; evaluables **34/35 en el Bloque A** (1 censurado con causa) y **2/2 en el B** (post-revisión ciega); 1 clip soak (`v06_c01`, 6:09,6). *(Decía "34 clips, 35 episodios" — eso es el Bloque A, no el banco.)* | `datasets/processed/clip_bench/manifest.yaml` (sha `3f14f50a…`, freeze 2026-08-09) + `meta/*.clip.yaml` | R-12 | ✅ en disco |
| T-79 | **Composición de `bench_v3`** por estrato (6.477 / 55.165 / sha256) | `bench_v3_manifest.json` + `registry/bench_v3.md` | R-21 | ✅ en disco |
| T-80 | **Limitaciones declaradas** (§4 de este doc) | `operacion/98` §6 + `results/index.md` | R-13 | ✅ en disco |
| T-81 | **ADR → dónde se declara en el informe** (§4 de este doc) | `decisiones/` + `estado-de-implementacion-adrs.md` | — (R-18 es la Tabla 43 DA-01…DA-13, **no** esta) | ✅ en disco |
| T-82 | **Estrato B (obra real no guionada) — I1/I2** (✎ 08-10): F1 0,333 (`scene`) / 0,190 (`subject`) sobre **2 episodios evaluables — no rankear con ese n**; lo robusto es la **asimetría de FP: 26 vs 323 sobre 11 negativos (12×)** y el FAR del único soak, citado como **"3 y 190 FP en 6:09,6"** (tasas derivadas 29,2 / 1.850,8 FA/h, denominador 0,1027 h) | `results/clip_bench/{i1,i2}_gdinotiny560_*_internet/metrics.json` + índice | R-13 | ✅ en disco |
| T-83 | **Nivel A sobre video (NA1, 17 clips)** (✎ 08-10): CR-01 F1 0,031 / CR-02 0,018 contra 0,408/0,479 en imágenes (`bench_obra`) — el derrumbe es de **precision**, el recall se sostiene | `results/bench_nivel_a/na1_gdinotiny560_v2short_video/metrics.json` | R-13 | ✅ en disco |
| T-84 | **Revisión ciega del GT del lote como resultado de calidad de GT** (✎ 08-10): **5 de 7 declaraciones de episodio eran errores de anotación (~71%)**, todas sobre-declarando donde el estado no era observable — el mismo modo de falla que el motor | constancia en `operacion/113` §B + correcciones firmadas en los `clip.yaml` | R-13 | ✅ en disco |
| T-85 | **Latencia de notificación (distribución): p95 64,534 ms (n=460) + régimen sostenido** | `results/realtime/t_alert_notification/metrics.json` + `operacion/118` | §17.3.10 | ✅ en disco |
| FIG-A | **Arquitectura de los dos planos** (DBE / EBE, corte tras normalización) (✎ 08-19: destino único **§17.4.1** — §17.3 quedó sin vista de procesos por la doctrina del pase de cierre) | especificación en **doc 94 §4** | R-09 | 📐 spec |
| FIG-B | **Curva calidad vs densidad** (F1 escena y sujeto contra fps) | `results/clip_bench/r{1..6}_*/metrics.json` | R-13 | ⚙ generar |
| FIG-C | **Frame con overlay de alerta confirmada** | renderer en `experimental-setup/defensa/` + `runs/*/previews/` | R-12 | ⚙ generar |
| FIG-D | **Montaje lado a lado escena \| sujeto** (el mecanismo de F-89.1 en una imagen) | `experimental-setup/defensa/` (VG1 lado a lado, ya renderizado) | R-26 | ✅ en disco |
| FIG-E | **Máquina de estados del motor** (`inactive → candidate → confirmed → sustained → resolved`, con `confirm_after_ms`) (✎ 08-19: destino **§17.3.8.2** y CINCO estados — el rótulo de tres estados era una simplificación incorrecta) | contrato `pattern_events` del control-plane | R-06/R-07 | ⚙ generar |
| FIG-F | **Frontera de juzgabilidad de 3 ejes** (escala × iluminación × oclusión) — dónde el material deja de ser evaluable (✎ 08-10) | mediciones en `operacion/103` §7 y `operacion/105` (F-105.3) | R-13 | ⚙ generar |

> ✎ **2026-08-21 — LAS CINCO FIGURAS PENDIENTES ESTÁN PRODUCIDAS.** `FIG-A`, `FIG-B`,
> `FIG-C`, `FIG-E` y `FIG-F` dejaron de ser `📐 spec` / `⚙ generar`: viven en
> [`informe/figuras/`](../../figuras/README.md) en PNG 300 dpi + SVG, con generadores
> reproducibles y notas al pie redactadas. **El inventario de materiales del informe
> queda completo** — 17 tablas + 6 figuras, todas con artefacto de origen. Tres
> advertencias de cita, en el README de esa carpeta: el módulo de distribución va en
> línea **continua** (la nota al pie de `94` §4 quedó falsa y está reemplazada allí), el
> **orden de arranque es el inverso del flujo de datos**, y la máquina de estados tiene
> **cinco** estados con la reapertura hacia `candidate`, no hacia `inactive`.

**Regla al llenarlas:** ninguna tabla se transcribe desde este inventario ni desde el
§5 del doc 97 — se transcribe **desde el artefacto**, y el inventario solo dice cuál es.
Toda tabla de resultados lleva, en su nota al pie, el `campaign_id` o el sha256 del
banco: es lo que la hace verificable por un tercero.

**Las tres reglas de lectura que ninguna tabla puede violar** (F-EV1, L5, F-96.6):
los clips negativos (✎ 08-10: hoy son **15** — 4 del Bloque A + 11 del estrato B) **no**
entran a P/R/F1, su métrica son los FP · se reporta **por estrato y por escenario**,
nunca solo el agregado · el **SDR no se compara entre cadencias**.

---

## 2. Anexo de reproducibilidad

### 2.1 Huellas de los artefactos congelados (verificadas el 2026-08-05; ✎ re-verificadas el 2026-08-10 — cambió solo el manifest del banco de clips)

| Artefacto | sha256 | Verificación |
|---|---|---|
| `bench_v3.json` (banco de imágenes) | `4557024ecc4ee497…a4462` | `sha256sum` **coincide** con `bench_v3_manifest.json → bench_v3_sha256` |
| estrato `bench_obra_test` | `e82eed03469665a3…af61a` | coincide con `source_sha256` |
| estrato `bench_obra_val` | `b2326724b71e7776…4c58c` | coincide con `source_sha256` |
| estrato `chv` | `6d15ff9b46407511…39a7` | coincide con `source_sha256` |
| estrato `shel5k` | `bf35f63bcf726c1c…d1e0f` | coincide con `source_sha256` |
| `manifest.yaml` (banco de clips, **47 — vigente desde 2026-08-09**) | `3f14f50a53c0d6c57b429378544dcfb6ed87fc942640db302c53ba1470001a75` | `sha256sum` directo == `clip_bench_manifest.json`; freeze `clip_bench.sha256` **189/189 OK** (verificador 109) |
| `manifest.yaml` (freeze histórico del sub-banco del rodaje, 34) | `cef5082e1eb1981c…260e8` | commit `f7a27fe6` — es el freeze que citan T1/T2/D1/H1/G1/B1/R1–R6 |
| prompt set `cr01_cr02_v2_short` | `df81fd48b6daf892…b309a` | `frozen_sha256` en el YAML, acta doc 76 |
| prompt set `eind_v1` | `7a0126f45eb1362a…ed770` | idem |
| prompt set `edir_v1` | `a1278d0c34cd13be…43703` | idem |

> **Queda saldado un riesgo de la auditoría del doc 75**: decía que el sha256 de
> `bench_v3` **no era verificable con `sha256sum`**. Sí lo es — se verificó hoy, y los
> cuatro sha256 por estrato también. El manifest guarda exactamente el digest del
> archivo, sin canonicalización de por medio.

### 2.2 El verificador mecánico de cifras

```bash
cd docs && python3 operacion/datos/96-verificar-indices.py
```

✎ 2026-08-14 — **el alcance volvió a crecer** (docs 113 y 118). Corrido hoy:
**`✅ Todo verificado`** — **25 cifras** contra `metrics.json` (14 F1 de `clip_bench`,
5 de `bench_nivel_a` y 6 valores de `realtime/t_alert_notification`), **guard de
cobertura 17/17 campañas** (falla si aparece una campaña sin fila de verificación),
3 deltas de bootstrap con su IC, 1.447 enlaces y **35 docs de procedencia** (ninguno
faltante). *(Decía: 8 F1, 31 docs, "solo cubre T1, G1 y R1–R6" — ese hueco quedó
cerrado por el guard.)*

**Lo que sigue sin cubrir, y se chequea a mano:** `bench_imagenes/`; el descarte se
contrasta contra el doc 64. `realtime/t_alert_notification` ya tiene `metrics.json`,
prueba negativa obligatoria y cobertura mecánica.

**Segundo verificador** (✎ 08-10):
`python3 docs/operacion/datos/109-verificar-organizacion.py` — las 6 reglas de
organización del material de video: estratos en su lugar (34+13+4 retirados), campaña
citable vs evidencia exploratoria, anotaciones del repo como fuente de verdad
(correcciones firmadas con guard `--check`), integridad lab↔banco por sha256,
exclusiones firmadas (`v08_c01`), banco reportable con freeze 189/189.

### 2.3 Cadena de comandos por material

Los cuatro repos son hermanos en disco y las rutas relativas lo asumen.

**Banco de imágenes (`bench_v3`) y percepción**
```bash
# reconstruir el banco (idempotente, lee las 4 fuentes curadas)
python3 datasets/scripts/curate/build_bench_v3.py
# evaluar una corrida del media-plane contra el banco
cd e-ovrt_media-plane && .venv/bin/python -m eovrt_media.tools.evaluate \
    --run runs/<run_id> \
    --bench-coco ../e-ovrt_datasets/datasets/processed/coco/bench/curated/bench_v3.json
```

**Servicio del media-plane y disparo de una corrida**
```bash
cd e-ovrt_media-plane && EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve  # :8080
curl -s localhost:8080/healthz localhost:8080/readyz          # = make smoke
# POST /api/runs con el run config (una corrida activa a la vez)
```

**Camino offline (DBE) y camino en vivo (EBE)**
```bash
cd e-ovrt_control-plane
.venv/bin/eovrt-control serve --port 8081                       # servicio
.venv/bin/eovrt-control replay   --config <cfg>                 # DBE: relee detections.jsonl
.venv/bin/eovrt-control live     --config <cfg>                 # EBE: consume el bus
.venv/bin/eovrt-control evaluate-alerts ...                     # 5 métricas contra GT temporal
```
> **EBE, orden no negociable:** primero `POST :8081/api/runs` con `mode: live` (su 201
> implica suscripción hecha), después `POST :8080/api/runs` con `bus.enabled: true`.
> PUB/SUB pierde todo lo publicado antes de la suscripción.

**Cadena de GT de video** (✎ 08-10: las anotaciones llegaron — docs 102–111 — y la
cadena quedó ejercitada de punta a punta sobre 13 clips)
```bash
# ¡verificar meta/task vs meta/project ANTES de decidir el primer paso! Un export a
# nivel PROYECTO exige el split (sin él el GT sale negativo EN SILENCIO); el lote llegó
# a nivel TASK y aplicárselo habría sido el error simétrico (doc 102).
python3 <video-gt-lab>/split_cvat_project.py ...
python3 <video-gt-lab>/derive_clip_gt.py ...
python3 <video-gt-lab>/validate_clip_gt.py ...
python3 <video-gt-lab>/promote_clip.py ...        # suma el clip al banco
python3 <video-gt-lab>/aggregate_clip_campaign.py ...   # métricas de campaña
# guard de correcciones firmadas (✎ 08-10): apply_attribute_corrections.py --check
# sale 1 si una corrección firmada del repo falta en el GT (doc 111)
```

**Piloto de clase nueva (A1)** — un solo archivo de config de 48 líneas, 0 entrenamientos;
procedencia de las 5 corridas en `operacion/datos/94-piloto-clase-nueva/resultados.json`.

### 2.4 Trazabilidad corrida→resultado

Cada campaña de `results/` trae su procedencia en disco, y es lo que hay que citar:

| Archivo | Qué garantiza |
|---|---|
| `campaign.yaml` | la definición de la campaña (modelo, prompt set, granularidad, pattern set) |
| `provenance.json` / `provenance_runs.json` | los `run_id` exactos del media-plane y del control-plane |
| `evals/eval_<clip>.json` | la evaluación por clip, uno por clip del banco |
| `metrics.json` | el agregado (`positives`, `negatives`, `by_condition`, `by_scenario`, `by_clip`) |

**Entorno:** media-plane Python 3.12 (`pip install -e ".[gpu,dev]"`), control-plane y BFF
Python 3.11, `datasets` sin paquete (scripts sueltos, requiere `Pillow`). Puertos 8080
(media) y 8081 (control). El JSONL es la verdad en los dos caminos: **toda corrida live
es re-evaluable offline y produce artefactos idénticos** (paridad verificada por mutación).

---

## 3. Licencias, consentimientos y citas obligatorias

### 3.1 Lo que efectivamente sostiene un resultado reportado

Solo estas fuentes aparecen en los números del capítulo. El resto del
`license_registry.md` (SH17, GDUT-HWD, SHWD, SODA, Pictor-PPE, Construction-PPE,
`construction_safety_hardhat`) **no se cita**: o quedó descartado o nunca entró.

| Fuente | Dónde entra | Licencia | Obligación en el informe |
|---|---|---|---|
| `construction_site_safety` (Roboflow) | estratos `bench_obra` (147 imgs) + split TRAIN | **CC BY 4.0** | atribución |
| `chv` (GitHub `ZijianWang-ZW/PPE_detection`) | estrato `chv`, **1.330 imgs = 20,5% de `bench_v3`** | **sin licencia formal** (SPDX: none); grant informal de los autores: *"open for free use"* | **cita obligatoria `wang2021ppe`** + declarar *"dataset académico de terceros usado para evaluación bajo el grant de uso libre de sus autores, con cita; imágenes no redistribuidas"*. Se cumple por construcción: raw gitignorado, solo se versionan anotaciones derivadas |
| **SHEL5K** (Mendeley) | estrato `shel5k`, **5.000 imgs (77% del agregado)** | **CC BY 4.0**, DOI `10.17632/9rcv8mm682.4` | atribución + DOI |
| `ppe_siabar` (Roboflow) | split TRAIN | CC BY 4.0 | atribución (**y declarar el estado del entrenamiento a la entrega**: el TRAIN se construyó y la jornada de fine-tuning está **comprometida — ADR-017**; si a la entrega no se entrenó, se dice con causa técnica, nunca "quedó fuera") |
| **MOCS** (copia Roboflow `mocs-bowib`) | piloto A1 (evidencia cualitativa + ancla `person`↔`Worker`) | CC BY 4.0 **declarada por el uploader de la copia**; el original de `anlab340` nunca se descargó ni se verificó | **citar el paper original de MOCS** + declarar que se usó una copia de terceros, sin redistribución |
| **Rodaje propio 2026-07-25** | **el banco de 34 clips = el resultado principal** | material propio | consentimientos de los participantes (ver §3.3) |
| **Lote de internet (14 clips — ✎ 08-10: 13 con GT humano, `v08_c01` excluido con causa firmada)** | estrato B del banco de clips (Bloque B); **precisa L4, no la levanta** (D-113.1) | ✎ **2026-08-05: origen registrado** — canal de YouTube **`@HospitalConstruction`** (https://www.youtube.com/@HospitalConstruction). **Es *Standard YouTube License*, no Creative Commons** ⇒ base de uso: **académico/evaluativo con cita y sin redistribución** (postura `chv`), **nunca presentado como licencia de libre uso** | **citar el canal como fuente de las escenas** + los caveats de §3.3 (no es cámara-nativo · caras difuminadas en figuras · velocidad real verificada) |

### 3.2 Licencias de los modelos: hueco abierto

Los catálogos de `e-ovrt_media-plane/configs/models/` (`grounding-dino/`,
`mm-grounding-dino/`, `yoloe/`) **no traen campo de licencia**. El informe cita tres
familias de pesos y hoy no hay registro de bajo qué términos se usan. **Hay que
verificarlo y registrarlo antes de citarlas** — mirar el `LICENSE` del repo de origen de
cada familia de pesos y anotarlo junto al catálogo. No lo doy por sabido acá: es
exactamente el tipo de dato que no se declara de memoria.

### 3.3 El lote de internet: origen registrado el 2026-08-05, con dos salvedades

> ✅ **RESUELTO en lo esencial el mismo día.** El usuario aportó la procedencia: las 14
> escenas salen del **canal público de YouTube `@HospitalConstruction`**
> (https://www.youtube.com/@HospitalConstruction), cuyas descripciones declaran que los
> videos son públicos. **Decisión: se cita el canal como fuente de las escenas.** Quedó
> registrado en `e-ovrt_datasets/datasets/registry/license_registry.md`, sección
> **"Material de VIDEO"** — que hasta hoy no existía —, junto con la entrada del rodaje
> propio. La base de uso declarada es la misma que ya se usa para `chv`: **uso
> académico/evaluativo con cita, sin redistribución** (los `.mp4` están gitignorados; solo
> se versionan anotaciones derivadas, previews y nombres de archivo).
>
> **Salvedad 1 — RESUELTA, y define cómo se redacta: es *Standard YouTube License*.** Se
> revisó la descripción: **no hay marcador de Creative Commons**, así que rige la licencia
> por defecto, que no concede reproducción ni obra derivada. La descripción sí declara que
> lo grabado son vistas y escenas visibles al público — pero eso dice **qué se filmó**, no
> otorga reuso. ⇒ El informe declara **uso académico/evaluativo con cita y sin
> redistribución** (postura `chv`), y **nunca** "licencia CC" ni "material de libre uso".
>
> **Salvedad 2 — personas identificables de terceros**, consentimiento no obtenible. La
> declaración del autor ayuda **acá**: respalda que no hay expectativa razonable de
> privacidad sobre lo filmado. Mitigaciones igual: no se redistribuye, sin datos personales
> en el repo (DA-08/09), E-11 intacta. **Regla: si un frame del lote se publica como
> figura, se difuminan las caras.**
>
> **Dos caveats metodológicos del estrato, que van declarados con él:**
> **(1) velocidad real verificada por dos vías ⇒ las métricas temporales aplican** — el
> canal publica sobre todo time-lapse, y un clip time-lapse volvería inservibles TTFD /
> `confirm_after_ms` / SDR; el autor declara velocidad original y además se **midió** sobre
> las pre-anotaciones de los 14 clips: **0,4–2,8 px/frame de mediana** (máx ~23), propio de
> 30 fps continuos. Los 14 masters son 1920×1080 @ 30 fps.
> **(2) el material no es cámara-nativo** — el autor declara corrección de color,
> estabilización y recortes. Preproceso ajeno que no controlamos: se declara. El rodaje sí
> es cámara-nativo, así que los dos estratos se leen por separado (L5).
>
> **Falta**: URL y fecha de acceso por video (hoy: el canal + un video de referencia,
> subido 2015-04-05, grabado 2015-03-28).
>
> Lo que sigue abajo es el diagnóstico original. **Se conserva solo como rastro**: explica
> por qué registrar la procedencia no era opcional y qué se verificó antes de tenerla. Los
> dos puntos que abría —licencia del lote y consentimiento del rodaje— están cerrados
> (este banner y §3.3 arriba, más el registry).

Verificado el 2026-08-05 (antes de que se aportara el origen), tres cosas independientes:

1. Los **14 `clip.yaml` del lote de internet no tienen cláusula de licencia** (a
   diferencia de `cb_b01_p7`, que sí llevaba la condición escrita). ✎ 08-06: los 3
   promovidos (`v04_c01`/`v06_c01`/`v10_c01`) **ya la llevan** (bloque `license:` con
   `video_url: TODO` — la URL por video sigue pendiente, hallazgo 2 de §6).
2. El `license_registry.md` **no tiene ninguna entrada de video** — ni rodaje, ni banco
   de clips, ni lote de internet.
3. **No hay URL de origen registrada** para los 14 masters (`raw/1.1.mp4` … `10.1.mp4`).

Y la regla que lo vuelve vinculante ya estaba escrita: **spec 43 §7, "Marco legal
(bloqueante de la grabación, no del diseño)"**, que exige dos cosas distintas:

- *"**Consentimiento libre, expreso e informado por escrito** de cada persona grabada
  (**Ley 25.326, Disposición 10/2015** — doc 08 §1.3), archivado y **referenciado en
  `license_registry.md`** (sin datos personales en el repo)"*.
- *"**Bloque B: registrar la licencia** del dataset antes de usar los videos **en
  resultados reportables**"*.

Su ítem de checklist **`[ ] Consentimientos y licencias en license_registry.md; sha256 en
manifest` sigue sin marcar** (spec 43 §9). Y es el motivo #1 por el que `cb_b01_p7` se
retiró, que cita esa misma sección: *"licencia/consentimiento sin registrar — motivo
vinculante… no se resuelve con una pasada de CVAT"*.

**La consecuencia práctica:** cuando lleguen las anotaciones, el lote **queda
igualmente inelegible para resultados reportables** hasta que su procedencia esté
registrada. Anotarlo no lo desbloquea. Es decidible **hoy**, en paralelo al CVAT, y solo
lo puede hacer quien sepa de dónde salieron los videos.

**Dos casos, severidades distintas — no confundirlos:**

- **Rodaje (34 clips, el resultado principal): ✅ resuelto por declaración (2026-08-05).**
  Las personas que aparecen son **los propios integrantes del proyecto**, actuando según el
  guion del doc 69, **sin terceros en cuadro**: son a la vez los sujetos y los responsables
  del material, y las situaciones son actuadas — no documentan conducta laboral real de
  nadie. Eso es lo que se declara en el informe, y es una posición más fuerte que un
  formulario. Lo administrativo lo maneja el equipo por su cuenta; la identificación del
  responsable va en el informe, no en el registry. Queda disponible
  `registry/plantilla-consentimiento-audiovisual.md` por si la facultad pide el formulario.
- **Lote de internet (14 clips):** obra real de terceros, con personas identificables y
  **procedencia desconocida en el repo**. Riesgo alto: si no se puede acreditar el origen
  y sus términos, el material no entra al capítulo — exactamente como `cb_b01_p7`.

**Lo que se puede hacer sin esperar a nadie** (✎ 2026-08-06: la entrada de video **ya
se creó** ese mismo día — §3.3; lo que sigue faltando del bloque es solo **URL + fecha
de acceso por master**): completar en `license_registry.md` §Material de VIDEO la URL
de origen y términos por master, y el sha256 en el manifest. Si el lote no acredita, el capítulo **se sostiene
igual** con L4 declarada — es la regla del doc 57 §7.6: *el cierre lo decide la cobertura
del material; lo no cubierto se declara con causa, nunca se fabrica*.

---

## 4. Limitaciones y ADRs

### 4.1 Lista canónica de limitaciones: L1–L8 (cerrada 2026-08-05)

**Resuelto.** `results/index.md` definía **L1–L5** y `operacion/98` §6 listaba **7**
limitaciones con solo **4 etiquetadas** (L4, L1, L5, L2) — L3 no aparecía y tres iban
sueltas. Ahora las ocho tienen código en los dos lugares, con `results/index.md`
§Limitaciones declaradas como versión de referencia.

> **Colisión de etiquetas que hay que respetar al redactar:** la **Fase L** del doc 62 usa
> `L0`/`L1` para sus hitos (`L0` = ensayo pre-rodaje, `L1` = el rodaje). Se decidió
> **mantener el prefijo `L` para las limitaciones** (ya estaban citadas en varios docs) y
> desambiguar en prosa: escribir **"limitación L1"**, nunca `L1` a secas.

| ID | Limitación | Estado | Fuente |
|---|---|---|---|
| **L4** | **Un solo bloque guionado, sin obra real en video.** La más citable: mismos actores, misma locación, escenarios guionados | declarada; ✎ 08-06: licencia registrada y GT humano en marcha; **✎ 08-10 — formulación VIGENTE (D-113.1, firmada): "L4 se precisó, no se levantó** — existe medición en obra real no guionada (I1/I2, 13 clips, revisión ciega incluida) y esa medición **caracteriza por mecanismo dónde el sistema deja de ser evaluable; no lo valida sobre obra real**". No se crea L9: la frontera de juzgabilidad es el contenido nuevo de L4. Versión de referencia: `results/index.md` | `operacion/98` §6 + D-113.1 |
| **L1** | **FAR/hora no sostiene una cota.** Harían falta ~3 h de cumplimiento anotado; el control de negativos discrimina (T1/T2/G1: 0 FP de 4; D1/H1/B1: 2–3) | declarada con causa cuantificada (D-90.1) — **✎ 08-10: precisada**: desde el 08-07 hay un clip soak (`v06_c01`, 0,1027 h) y la tasa **es computable**; se cita como **"3 y 190 FP en 6:09,6 del único soak"** con la tasa horaria como derivada (29,2 / 1.850,8 FA/h). Sigue sin sostener una cota. Versión de referencia: `results/index.md` | `operacion/98` §6 |
| **L5** | **Escenarios desbalanceados** ⇒ obliga a reportar siempre por escenario y por estrato | declarada; es regla de lectura, no solo limitación | `results/index.md` |
| **L2** | **Sin doble anotación ni kappa** — decisión declarada, no omisión | declarada | `results/index.md` |
| **L3** | **Seis bordes adjudicados** en el GT del rodaje (oclusión, no cambio de estado), con firma en `clip.yaml` | declarada; trazable en `apply_adjudications.py` | `results/index.md` |
| **L6** | **El tracker no está medido en obra real con multitud** — G1 se verificó en vivo con pocos sujetos; el `track_id` es post-hoc/decorador | declarada y **etiquetada 2026-08-05** — **✎ 08-10: parcialmente levantada**: en `v06_c01` (127 personas reales) el tracker produjo **182 identidades con FP** — fragmenta en denso y el costo de G1 escala con la escena (F-103.2). Versión de referencia: `results/index.md` | `operacion/98` §6 |
| **L7** | **Licencia de `chv` parcial** (20,5% del bench de imágenes): uso permitido con cita, sin redistribución | declarada y **etiquetada 2026-08-05** | `operacion/98` §6 + §3.1 |
| **L8** | **CR-02 a Nivel A no cerrada** — un solo estrato, IC solapados | declarada y **etiquetada 2026-08-05** | `operacion/98` §6 |

**Y una que este armado agrega:** la latencia G2A **no es** vidrio→alerta (F-101.8). No
es una limitación del sistema sino del **instrumento**, y ya tiene su advertencia
obligatoria en el doc 97 §5.4. Decidir si entra a la lista con etiqueta propia o queda
solo como caveat de la tabla de latencia.

### 4.2 ADRs: dos series que se confunden

**Trampa de numeración, va al informe:** hay **dos** series de ADR y se confunden a
simple vista.

- `docs/decisiones/` → **ADR-001…ADR-019** (3 dígitos): las decisiones **del proyecto**
  (✎ 2026-08-06: *decía "…014"*; el 015 es el cierre de alcance. ✎ 2026-08-10: el 016 es
  la reapertura acotada de la distribución. ✎ 2026-08-18: *decía "…016"* — el 017 es la
  jornada de fine-tuning, el 018 el acople BFF-subproceso —**derogado el mismo 08-18 por
  el 020**—, el 019 el servicio HTTP del distribuidor y el **020** el cierre: HTTP es el
  acople, el subproceso baja a fallback ⇒ **dos** patrones de acople, no tres).
- `e-ovrt_control-plane/docs/decisions/` → **ADR-0001…ADR-0013** (4 dígitos, falta 0005):
  las decisiones **internas del control-plane**.

Se solapan en tema y difieren en número (p. ej. aplicabilidad de métricas es ADR-006 del
proyecto y ADR-0006 del control-plane). **Al citar, decir siempre la serie.**
✎ 2026-08-06: **la convención quedó fijada en el glosario (doc 13 §3, entrada
"ADR-NNN (dos series)")** y las citas sin serie de `nucleo/01` y `nucleo/10` fueron
aclaradas en el lugar.

> Queda saldado otro ítem del doc 75: reclamaba **8 ADRs inexistentes**
> (`ADR-0006..0013` del control-plane). **Existen los 8**, verificado hoy.

**Los del proyecto** (ADR-015 va en prosa aparte, §5/§6), con dónde aterrizan:

| ADR | Decisión | Dónde se declara |
|---|---|---|
| 001 | Estrategia del núcleo: **E-IND** (encuadre) | §17.3 estrategia + veredicto del eje (T-68) |
| 002 | Granularidad: G0 núcleo + G1 demostrativa | **Revisar el texto**: G1 dejó de ser demostrativa — es el mejor resultado del banco (F1 0,930) |
| 003 | Bus media→control: **ZeroMQ PUB/SUB**, broker diferido | arquitectura EBE (FIG-A, T-76) |
| 004 | Corrida paraguas y `experiment_id` | reproducibilidad (§2.4) |
| 005 | Distribución de alertas: recorte, canal MQTT, repo propio | ✎ **2026-08-12: funcionalmente implementada y verificada** — seis criterios de spec 45 cerrados, incluidos DBE/EBE, reporte y MQTT real. Quedan la vista de webconsole, la orquestación integral y el primer commit; E-06 sigue excluida. **✎ 2026-08-14: los tres pendientes del 08-12 quedaron cerrados el 2026-08-13** — vista de webconsole (`13c801e`, "feat(webconsole): mostrar outcomes de distribución") y orquestación integral (`42529e2`, "feat(experiments): orquestar distribución de alertas") en `e-ovrt_experimental-setup`; el repo `e-ovrt_alert-distribution` ya tiene historia propia (`c9903cc`, `1e6d8fa`). E-06 sigue excluida |
| **016** | **Reapertura acotada de la distribución** para cerrar la arquitectura | deroga ADR-015 §2b/§2c/§6; ratifica §2a/§3/§4/§5. E-06 sigue excluida |
| 006 | Reporte consolidado y **aplicabilidad de métricas** | lenguaje de estados: `not_applicable` / `non_temporal_source` |
| 007 | Semántica de corrida en EBE: **1:1** | T-76 |
| 008 | Control-plane como servicio mínimo | arquitectura |
| 009 | Config centralizada + webconsole como superficie de gestión | arquitectura + método |
| 010 | Secuenciación: plataforma primero, GT al final | método y cronología |
| 011 | Frontera de la política: el motor emite siempre; la supresión es de distribución | **`re_alerts` no son FP** |
| 012 | Sin memoria de cobertura bajo G0; la histéresis la subsume | mecanismo (F-81.1 / F-85.3) |
| 013 | Aplicabilidad por temporalidad de la fuente | estados de aplicabilidad |
| 014 | Layout y consolidación de artefactos por experimento | §2.4 |
| **017** *(✎ fila agregada 2026-08-18)* | El fine-tuning (E-04) se ejerce como jornada, nunca "falta de tiempo" | rama comparativa del §17.5 — **jornada T1 ejercida y cerrada con veredicto pre-registrado** (doc 123); T2 exploratorio en curso (D-FT-14/15) |
| ~~**018**~~ | ~~Tercer patrón de acople: BFF-subproceso~~ ⛔ **DEROGADA por 020** | **no va al informe** — registro histórico |
| **019** *(✎ fila agregada 2026-08-18)* | El distribuidor también como **servicio HTTP** (`:8082`) | §17.4 despliegue: los tres módulos son servicios HTTP config-driven; containerización diferida con causa (doc 124) |
| **020** *(✎ fila agregada 2026-08-18)* | **HTTP es el acople de la distribución**; el subproceso baja a fallback operativo y deja de ser patrón | §17.4/§17.3: **DOS patrones de acople** — (a) HTTP config-driven en los tres módulos, (b) bus ZeroMQ. El fallback **no se describe**: es operación, no arquitectura |

**ADR-015 — ✅ escrito y ACEPTADO el 2026-08-05.**
[`decisiones/adr-015-cierre-de-alcance.md`](../../../decisiones/adr-015-cierre-de-alcance.md).
El doc 95 §5.1 lo pedía como *"recorte final de alcance"* porque los docs 91/94 declaraban
tracker/G1 como no implementado; **su premisa se invirtió** (G1 es el mejor resultado del
banco), así que no es un recorte: es el **registro de que el alcance creció, con
evidencia, y de qué sigue excluido**. Qué hace:

- **Registra los cuatro movimientos**: E-03 (G1 de demostrativa a capacidad operativa
  medida en 34/34), E-07 (parcial: OAK-D + EN-2 con 87% de descarte), E-13 (E-HYB-or
  ejecutada y refutada; `hyb_and` no ejecutada con causa), E-04 (no ejercida, pero por
  secuenciación — ✎ 2026-08-11: fila **superada por ADR-017**, E-04 es jornada
  experimental comprometida y la causa temporal está derogada). **E-10 y las otras
  ocho exclusiones no cambian.**
- **Cierra la puerta** (§2b): ninguna capacidad nueva de acá a la defensa — es la parte
  que *restringe*, y es el riesgo que el doc 95 realmente quería cubrir.
- **Registró un estado transitorio del condicional de ADR-005.** ADR-016 lo sustituyó:
  el condicional quedó resuelto en **sí** y el recorte mínimo fue implementado y
  verificado. §2b/§2c/§6 de ADR-015 quedaron derogados; §2a, §3, §4 y §5 —incluida
  **la lista de límites L1–L8**— siguen vigentes.
- **Desbloquea R-13** con una lista auditada ítem por ítem: **de los 8 límites de julio,
  5 estaban resueltos** (`track_id`, evaluadores de D1, GT preliminar, matching greedy,
  inventario de datasets) y sobreviven 3, uno de ellos agravado por F-101.8.
- **Desbloquea R-21 corrigiendo un punto falso**: su tabla dice *"MOT ✗ tracker no
  implementado"*; lo excluido son las **métricas** MOT (E-10), no la capacidad.

Integrado en `decisiones/README.md`, `estado-de-implementacion-adrs.md` (§0 y §1) y
anotaciones en R-13 y R-21 del doc 93. **Y aplicado al doc 10 el mismo día**: el ítem 10 de
la lista de alcance quedó reescrito (G1 = capacidad operativa medida en 34 clips, ya no
"demostrativa en 2–3") y las filas **E-03/E-04/E-07/E-13** de la tabla de exclusiones
llevan su estado real con evidencia. **Registro de alcance y resultados ya dicen lo mismo.**

*De yapa, en la misma pasada:* la fila del ADR-001 en `estado-de-implementacion-adrs.md`
§3 decía *"sigue abierto (acta `edir_v1` pendiente)"* — **el acta se firmó el 2026-07-29
(doc 76) y D1 corrió en los dos niveles**. Corregida.

---

## 5. Catálogo de mecanismos: lo que el CVAT no movió — y lo que agregó

Esta es la parte del capítulo que da credibilidad. La premisa original ("es inmune al
lote de internet: el GT nuevo puede mover un agregado, no un mecanismo medido") **quedó
verificada por los hechos** (✎ 2026-08-10): el CVAT llegó (docs 102–113), hubo
re-derivaciones y hasta una revisión ciega del GT, y el catálogo del Bloque A de abajo
sobrevivió intacto. El tramo de video **agregó mecanismos propios** — bloque nuevo al
final de esta sección. Texto fuente: los índices de `results/` (verificados
mecánicamente) — de ahí se transcribe, no de acá.

**Cómo la plataforma agrega sobre la detección cruda**
- **F-81.1** — la **histéresis rescata percepción intermitente**: CR-02 se detecta en ~1
  de cada 6 frames del episodio (F-G2.1) y el motor igual confirma.
- **F-85.3** — y es **palanca de doble filo, medida en los dos sentidos**: rescata lo
  intermitente-correcto y también sostiene lo intermitente-equivocado.
- **F-87.2** — **la unión de evidencia NO es monótona en un motor temporal**: sumar un
  brazo (`hyb_or`) no sube el recall, lo derrumba (0,824 → 0,353). Predicción
  pre-registrada **refutada**.
- **F-89.1 / F-89.2** — **el margen no estaba en el modelo ni en los prompts, sino en la
  identidad**: F1 0,789 → 0,930 con las detecciones **bit a bit las mismas** (SDR y TTFD
  idénticos). Es el hallazgo central del capítulo.
- **F-81.3** — TTFD ~5 frames: la latencia de la plataforma **es la política**, no el modelo.

**Cómo se expresa la condición en lenguaje (y su modo de falla propio)**
- **F-88.3** — **la etiqueta corta gana a la frase negada**, y eso ordena el eje.
- **F-88.1** — **el caption tiene costo medido**: 0,082 de F1 por una palabra.
- **F-88.2** — `bare_head` como evidencia directa **tampoco alcanza** (0,480 vs 0,582 de
  la ausencia espacial, **sobre las mismas detecciones**).
- **F-83.6** — **E-DIR no es un detector, es un recuperador**: recupera 18,5% de lo que
  E-IND no ve.
- **F-85.4** — **el ranking de Nivel A no transfiere a Nivel B**: la brecha se agranda
  con la plataforma.
- **F-85.5** — P9 es la única victoria de E-DIR, y está donde E-IND es más débil.
- **F-94.1** — **la palabra tiene que alinear con la taxonomía del despliegue**:
  `vehicle` junto a `machinery` da **0 detecciones**; aislada, AP 0,026 porque el 67% cae
  sobre lo que ese GT llama `machinery`. Segundo caso independiente el 2026-08-05
  (`gloves`: 252 detecciones, ninguna sobre un guante). **Va junto al número de A1, no
  después.**

**Qué sobrevive al tiempo real**
- **F-RT3** — el techo de fps es **contención de GIL**, no térmico ni la rama de texto.
- **F-RT5** — palanca aplicada y significativa: 3,75 → 4,42 fps, −14,4% latencia, p = 0,0195.
- **F-RT2** — la ventana temporal **exige estabilidad perceptual**: YOLOE entra en
  presupuesto y es inservible para la condición.
- **F-96.1** — a ~4 fps el agregado **no se degrada de forma detectable**, pero un
  agregado plano **escondía una redistribución completa**.
- **F-96.2** — **lo primero que se rompe bajo tiempo real es el rescate de F-81.1**:
  CR-02/P2 cae 1,00 → 0,60 → 0,20. Límite de cadencia declarado.
- **F-96.4** — **la ganancia de la identidad excluye el cero en las 4 densidades**
  (bootstrap pareado por clip). Formulación segura: doc 101 §3.
- **F-101.8** — **el G2A se mide desde el dequeue, no desde el fotón**: vidrio→alerta =
  `capture_to_host` (202–217 ms en el rodaje, 1.600 ms en tomas degradadas) **+ G2A**.

**Trampas de instrumento — se declaran o el número engaña**
- **F-EV1** — los clips negativos **no entran** a P/R/F1; su métrica son los FP.
- **F-96.6** — el **SDR no se compara entre cadencias**: sube al bajar la densidad, ~100%
  artefacto, verificado por decimación de las mismas detecciones.
- **F-96.5** — el **`t_alert` agregado no se compara entre densidades** sin control de
  supervivencia (corregido en revisión adversarial).
- **F-96.7** — 0 FP en negativos (✎ 08-10: acotado a las campañas del **Bloque A**): con
  4 clips es **control, no tasa**. El estrato B sí produce FP sobre sus 11 negativos —
  y ahí el conteo ES la métrica (ver el bloque del tramo de video).
- **F-RT1** — la sobre-marca de `vest` suprime CR-02 (dependiente de la vestimenta).
- **F-RT4** — deriva del host ±150 ms ⇒ las palancas <20% exigen ~10 pares **pareados
  intra-campaña** (protocolo doc 74).

**Qué agregó el tramo de video (estrato B) — ✎ 2026-08-10**
- **F-103.2** — bajo `subject` la identidad recupera el recall también en denso, **pero
  el tracker multiplica el ruido por la multitud**: en `v06_c01`, 182 identidades con FP
  contra 127 personas reales — el precio escala con la escena, no con el modelo.
- **F-105.2** — **la caída del estrato B queda confirmada a nivel PERSONA con el scorer
  oficial**: el mismo E-IND pasa de F1 0,41–0,55 en imágenes a ~0,15/0,01 sobre video
  real; **el recall se sostiene (~0,33), lo que se derrumba es la precision**.
- **F-105.3** — **la juzgabilidad NO se reduce a la escala**: `video02_clip07` tiene los
  sujetos más grandes del conjunto (370 px) y rinde F1 0,084 por oclusión mutua (58,5%
  de personas solapadas) — los ejes son **escala × iluminación × oclusión**.
- **F-105.4** — **el `unknown` del anotador mide la juzgabilidad HUMANA, no la del
  modelo**: el humano usa continuidad temporal (siguió a cada persona 6 minutos y
  determinó el 94%), el modelo decide frame a frame sin memoria — la vía de mejora
  señalada es **agregación temporal de evidencia para DETERMINAR estado**, no solo para
  confirmar.
- **F-108.1** — **la variable no era la granularidad: era la densidad** — `subject` solo
  hace falta cuando los sujetos se relevan; no existe "la mejor granularidad" del banco,
  existe la correcta para un régimen de densidad.
- **F-111.1 (enmendado — citar la versión enmendada)** — en obra real densa **la ventaja
  de la identidad que G1 mostró en el rodaje no se reproduce, y `subject` paga un orden
  de magnitud más FP** (asimetría 12× en negativos); el ranking por F1 **no se afirma**
  (n = 2 evaluables). La enmienda misma es citable como método.
- **F-113.1** — hallazgo de REPRODUCIBILIDAD: **re-evaluar sin re-agregar congela la
  procedencia** (el agregador copia `campaign.yaml` dentro de `metrics.json` — los
  `metrics.json` de I1/I2 declaraban el freeze pre-corrección); detectado y corregido
  **sin mover ninguna cifra**.
- **D-113.1** — decisión firmada: **se precisa L4, no se crea L9** — la frontera de
  juzgabilidad es el contenido nuevo de L4 (formulación de cita en §4.1).
- **D-113.2** — decisión firmada: la persona `unknown` **sale del denominador** del
  scorer de Nivel A, **pero una violación predicha sobre ella cuenta como FP** — "la
  alerta sobre una persona no juzgable suena igual"; la regla simétrica se evaluó y se
  descartó (medido: 48% de los FP de CR-01 en los pilotos caen sobre `unknown`).

**Resto del catálogo** (F-83.3/4/5/7, F-84.1/5/6, F-81.2, F-96.x restantes,
F-101.1/3/5/6/7/9, F-EV2/3, F-DR*, F-GT1): están en los índices de `results/` y en sus
docs de origen. **No los transcribo acá para no crear una segunda fuente**: el catálogo
vive en los índices verificados y este documento solo señala los que sostienen una
afirmación del capítulo.

---

## 6. Lo que este armado encontró, y qué hay que decidir

| # | Hallazgo | Quién decide |
|---|---|---|
| 1 | ✅ **RESUELTO 2026-08-05.** El origen del lote de internet es el canal público `@HospitalConstruction` y se cita como fuente; registrado en `license_registry.md` §Material de VIDEO. **Queda UNA salvedad chica** (✎ 2026-08-06: la otra —¿CC BY o *Standard*?— ya estaba resuelta en §3.3: es *Standard YouTube License*, **nunca** presentarlo como CC): anotar **URL + fecha de acceso por video** (evidencia perecedera — mejor ahora que después; ✎ 08-10: son **18 `clip.yaml`** + re-promover las 13 copias `meta/`, paso a paso en doc 113 §C1) | vos (chequeo barato) |
| 2 | ✅ **CERRADO 2026-08-05 por declaración**: en los 34 clips del rodaje aparecen **los propios integrantes del proyecto**, actuando según guion y sin terceros en cuadro — sujetos y responsables son los mismos. Lo administrativo lo maneja el equipo; la identificación del responsable va en el informe. Entrada de video creada en el registry; plantilla de consentimiento disponible por si la facultad la pide | — |
| 3 | ⚠ **Parcialmente cerrado — ✎ 2026-08-14, ver la enmienda al pie de esta tabla** (residuales abiertos: la posición sobre el checkpoint derivado T1 y el asset `mobileclip2_b.ts`, ambos pendientes de firma del usuario). ✎ **2026-08-15: las dos posiciones quedaron FIRMADAS** (ver la enmienda 2026-08-15 al pie); el único residual del hallazgo es ahora el archivo `LICENSE` por repo. Traza del cierre original, que se mantiene: ~~**Los catálogos de modelos no registran licencia.**~~ ✅ **CERRADO 2026-08-10 — y la premisa era FALSA.** Los **11 catálogos** de `configs/models/**/*.yaml` (todos menos `mock`, que no tiene pesos) **sí** declaran `license:` y `source:`; el hallazgo se había escrito sin auditar los subdirectorios por familia. Lo que faltaba de verdad era el registro y la implicancia, ya escritos: **nueva sección "PESOS DE MODELO" en `datasets/registry/license_registry.md`** — Grounding DINO **Apache-2.0** (verificado contra el frontmatter del model card descargado), MM-Grounding-DINO **Apache-2.0** (ídem), YOLOE **AGPL-3.0** (verificado contra la cadena embebida en el propio `.pt` y contra el paquete `ultralytics` 8.4.86). Las 3 declaraciones del catálogo **coinciden** con la evidencia independiente. La implicancia AGPL queda declarada: YOLOE se usó como **contraste medido y descartado con causa**, no se redistribuyen pesos (`models/**` gitignorado), y el alcance AGPL es el adaptador, no el proyecto. **Residual, y es decisión del usuario, no bloqueo de defensa:** los repos no tienen archivo `LICENSE` propio — hay que elegirlo antes de publicar | ⚠ parcialmente cerrado — ver enmienda 2026-08-14 |
| 4 | ✅ **CERRADO 2026-08-05**: ADR-015 escrito, **aceptado** y **aplicado al doc 10** (ítem 10 + filas E-03/E-04/E-07/E-13). Registra que el alcance creció, cierra la puerta a capacidad nueva, declara MQTT no implementada y **desbloquea R-13 y R-21** — R-13 con los 8 límites auditados (5 estaban resueltos) y R-21 con la corrección de "MOT ✗ tracker no implementado", falso al cierre | — |
| 5 | ✅ **CERRADO 2026-08-05**: lista canónica **L1–L8**, con las tres que faltaban etiquetadas (L6/L7/L8) y L3 agregada. Aplicada en `results/index.md` (referencia) y `operacion/98` §6. Se mantiene el prefijo `L` y se desambigua en prosa (**"limitación L1"**), porque la Fase L usa `L0`/`L1` para sus hitos | — |
| 6 | ✅ **CERRADO 2026-08-06.** **Dos series de ADR** (`ADR-001…016` del proyecto vs `ADR-0001…0013` del control-plane): la convención de cita ("decir siempre la serie") quedó **escrita en el glosario doc 13 §3** —el doc que el manifiesto manda usar como vocabulario— y las citas sin serie de `nucleo/01` y `nucleo/10` se aclararon en el lugar | — |

> **Enmienda 2026-08-14 al hallazgo 3 — parcialmente cerrado.** El registry de
> datasets ya registra los catálogos de modelos con SPDX, la posición propuesta sobre
> el checkpoint derivado T1 y el caso `mobileclip2_b.ts` con fuentes. Quedan la decisión
> de archivo `LICENSE` por repo y la firma del usuario sobre la posición del checkpoint
> y el asset MobileCLIP2.
>
> **✎ Enmienda 2026-08-15 — las dos firmas llegaron; queda UN residual.** El usuario firmó
> las dos posiciones que esta enmienda dejaba abiertas: **(a)** el **checkpoint derivado T1**
> hereda AGPL-3.0 en lectura conservadora — uso local y académico, no se redistribuye, no se
> commitea, no se publica con la tesis, y si la defensa exigiera publicarlo sale bajo
> AGPL-3.0; **(b)** `mobileclip2_b.ts` **se mantiene `NOASSERTION` por decisión expresa** —
> afirmar que conserva el estatuto de Apple sería una atribución que el release de Ultralytics
> no sostiene. Se agregó además algo que no estaba registrado: la subida del asset (253 MB) a
> Mendieta el 2026-08-13 quedó **ratificada como excepción acotada y retroactiva** a la
> política *"al clúster sólo material CC BY 4.0"* del doc 100 §6.3 — que **sigue vigente sin
> cambios para datos**. Al citarla: excepción ratificada *después* del hecho, nunca
> autorización previa. **Residual único del hallazgo 3:** los repos no tienen archivo
> `LICENSE` propio; es decisión del usuario y no bloquea la defensa.

**Saldados en este pasada** (eran ítems abiertos de la auditoría del doc 75): el sha256 de
`bench_v3` **sí** es verificable con `sha256sum` (§2.1) y los **8 ADRs del control-plane
existen** (§4.2).

**✎ 2026-08-10 — la orden que difería estos dos frentes quedó cumplida y levantada:**
los runs del lote de internet corrieron y cerraron (docs 109–113), la redacción de
§17.x está **habilitada y es el carril principal** (banner de `informe/97`), y el
`informe-project-kit/` **se regeneró el 2026-08-10** según el manifiesto de
`informe/98`. Sigue fuera de este documento solo la prosa del capítulo.
