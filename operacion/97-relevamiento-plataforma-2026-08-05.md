# 97 — Relevamiento integral de la plataforma (2026-08-05)

- **Fecha:** 2026-08-05.
- **Tipo:** relevamiento consolidado / memoria de implementación.
- **Reemplaza como punto de entrada a:** **doc 56** (foto del 2026-07-18), que pasa a
  ser artefacto histórico. **Este documento es la foto completa y verificada de la
  plataforma al 2026-08-05** — insumo directo para el capítulo de concreción técnica
  del informe.
- **Método:** relevamiento contra **git y código**, no contra memoria: `git log` desde
  el 2026-07-18 en los 4 repos (85 commits), verificación por lectura de los módulos
  citados, y ejecución real de las 5 suites. Ninguna afirmación de acá sale de un
  mensaje de commit sin haber mirado el código.

---

## 0. Resumen ejecutivo

Desde el doc 56 la plataforma **no cambió de arquitectura**: sigue siendo dos servicios
HTTP config-driven (media-plane `:8080`, control-plane `:8081`) con dos caminos de
acople (DBE por archivo, EBE por bus ZeroMQ), más la webconsole como superficie de
gestión primaria (ADR-009). Lo que cambió es que **dejó de ser una plataforma probada
en laboratorio y pasó a ser una plataforma que produjo el tramo experimental completo**:
13 campañas sobre GT humano, un rodaje con hardware real y una jornada de operación en
vivo.

Seis bloques de capacidad que el doc 56 no cubre:

1. **Identidad por sujeto como capacidad de plataforma** (control-plane `b0ba763`):
   `sources/tracking.py` produce `track_id` como **decorador de fuente**, en DBE y en
   EBE/live por igual, activable con `input.track_persons`. Es la palanca que dio el
   mejor resultado del banco.
2. **Estrategias de evidencia por patrón** (`5327080`): el motor despacha entre
   `eind` (ausencia espacial), `edir` (evidencia directa gateada por persona),
   `hyb_or` y `hyb_and` — este último **rechazado en validación** hasta el tramo de
   fusiones, para que no falle en silencio comportándose como `eind`.
3. **Evaluador temporal maduro**: `evaluate-alerts` v2 (censura por dimensionamiento,
   FAR/hora con base declarada, matching bipartito) más los **3 fixes F-EV1/2/3** que
   subestimaban la plataforma.
4. **Grabación y recorte de clips desde la consola** con hardware real (F-DR2..F-DR10),
   y el **video-gt-lab** cerrando GT temporal humano de 34 clips.
5. **Modelos con `image_size`** y los catálogos `gdino-tiny-560` / `gdino-base-560`,
   más `prepare_run` (pre-flight por corrida que resolvió el misterio de latencia 20×).
6. **Consola rediseñada de raíz** (tokens, primitivas, 11 pantallas) como evidencia de
   tesis, con preflight de plataforma y lanzamiento gateado.

**Estado de suites: las 5 verdes, 2.203 tests** (medidas hoy, no supuestas).

## 1. Suites, medidas hoy

| Repo / módulo | Comando | Resultado |
|---|---|---|
| media-plane | `.venv/bin/python -m pytest -q` | **641 passed**, 5 skipped |
| control-plane | `pytest tests/ -q --ignore=tests/labs` | **312 passed** |
| datasets | `python3 -m pytest datasets/tests/ -q` | **283 passed** |
| webconsole backend | `.venv/bin/python -m pytest -q` | **586 passed** |
| webconsole frontend | `npm test` (vitest) | **381 passed** (55 archivos) |
| **Total** | | **2.203 tests, 0 fallos** |

## 2. Qué se sumó desde el doc 56, por repo

### 2.1 control-plane (9 commits)

| Commit | Fecha | Qué |
|---|---|---|
| `b0ba763` | 08-05 | **Identidad por sujeto como capacidad de plataforma** + endurecimiento del camino live |
| `5327080` | 08-04 | **Evaluador `direct_evidence` + estrategias de evidencia por patrón** (spec 41 §6) |
| `c1cbb56` | 08-03 | **3 artefactos de medición** que subestimaban la plataforma (F-EV1/2/3) |
| `03ee8b0` | 07-29 | Deprecación del pattern set v1 (migrar `replay_dbe` a v2), ADRs 0006–0013 materializados |
| `5fcea11` | 07-26 | Patrones activos expuestos por HTTP en vivo y en la traza |
| `ef001ff` | 07-23 | La corrida live usa v2, no v1 (**F-DR9**) |
| `b3c6cc8` | 07-19 | `evaluate-alerts` v2: censura por dimensionamiento, FAR/hora, matching bipartito |
| `a53e95e` | 07-18 | `DELETE /api/runs/{id}` |

**Verificado en código:**

- `sources/tracking.py` — `TrackingSource` es un **proxy transparente**: delega
  `close()`, `request_stop()` y `dropped_events` al inner source explícitamente, y el
  resto por `__getattr__`. El docstring registra por qué: *"un decorador en live
  silenciaría `bus_dropped_events` (violación de ADR-003)"*. `maybe_track(source,
  enabled, ...)` es el punto de entrada config-driven.
- `engine/evaluators/` — `spatial_absence.py` y `direct_evidence.py`, con despacho por
  `evidence.strategy`. El motor no conoce evaluadores concretos.
- `configs/patterns/` — 7 pattern sets. Oficial vigente: **`cr01_cr02_v2`**; la
  variante de granularidad es `cr01_cr02_v2_subject`; `cr01_cr02_v1` **deprecado**.

> **Trampa vigente (F-DR9):** `cr01_cr02_v1` produce falsos `missed` por umbrales
> incompatibles con `derive_clip_gt`. **Nunca usar v1.**

### 2.2 media-plane (12 commits)

| Commit | Fecha | Qué |
|---|---|---|
| `d4f9ef4` | 07-24 | Nombre opcional de run (`RunSummary.name`) expuesto en vivo y terminado |
| `c78bd16` | 07-23 | `evaluate` restringe el `person_gt` al run por default |
| `da44756` | 07-23 | **`image_size` en GDINO + catálogos `gdino-tiny-560` / `gdino-base-560`** |
| `b37d550` | 07-23 | **`prepare_run`**: pre-flight por corrida antes de abrir la fuente |
| `9ef144c` | 07-23 | Corrida con cero unidades termina `failed` con motivo explícito (**F-DR10**) |
| `eddeb89`, `cee8832`, `71bf0ac` | 07-18 | **Sesión de preview en vivo** para posicionar cámaras y probar prompts (sin backlog, con deletterbox) |
| `d9f21fa` | 07-18 | Warm-up de lente (descarte de frames iniciales) en fuentes vivas |

**Verificado en código:** `models/base.py::prepare_run`, `image_size` en el adaptador
de GDINO y en la fábrica de modelos, `service/preview_manager.py`.

**El hallazgo detrás de `prepare_run`** (doc 61): el binding lazy del modelo hacía que
el costo de warm-up cayera sobre los primeros frames de la corrida, produciendo una
latencia aparente 20× mayor. El pre-flight lo mueve fuera de la ventana de medición.

> **Nota de estado:** la palanca **F-RT5** (+18% fps, −14,4% latencia, p=0,0195) está
> commiteada en la rama **`perf/producer-pil-roundtrip`** (`3deb64c`) y **el merge es
> decisión del usuario** — no está en la línea principal. La salida es byte a byte
> idéntica, así que no requiere re-validar mAP.

### 2.3 experimental-setup (50 commits)

El repo que más se movió. Cuatro bloques:

- **Grabación de rodaje** (07-21 → 07-23): script standalone OAK-D, motor de
  grabación, API REST, panel en la ventana Cámaras, y los fixes del dry-run con
  hardware real (**F-DR2..F-DR8**).
- **Generación y recorte de clips desde la consola** (07-23 → 07-26): UI de clips,
  contrato `marks: list[float]`, `compute_window_multi` para P6/P8, piso de censura
  universal y cola por escenario.
- **Rediseño completo de la consola** (07-28): capa base (tokens, primitivas,
  glosario, gráficos), 4 pantallas de la defensa reconstruidas y las 7 restantes
  migradas al armazón compartido. **11 pantallas** en `frontend/src/pages/`.
- **Catálogos y resultados** (07-29 → 08-05): congelamiento de `edir_v1`/`eind_v1`
  (acta doc 76), estructura de campañas, y las **13 campañas** hoy en `results/`.

**Verificado:** las 11 pantallas existen; `results/` tiene los 4 índices por material
con punto de entrada en `results/index.md`.

### 2.4 datasets (14 commits)

- **`bench_v3` ensamblado y congelado** (6.477 imgs, 3 fuentes, sha256 por fuente) tras
  incorporar SHEL5K y curar `bench_obra` de forma reproducible **dejando el original
  intacto**.
- **GT temporal del rodaje**: fichas `.clip.yaml` de los 34 clips + GT derivado +
  banco reportable.
- **Agregador de campañas normalizado** (`aggregate_clip_campaign.py`) — la pieza que
  hace que comparar dos combinaciones sea leer dos archivos con la misma forma.
- **Scoring de estado por persona** para Fase D + GT de CR-02 desde negativos
  explícitos, y **fusión dual-run** para E-HYB.

## 3. La plataforma hoy, por capacidad

| Capacidad | Estado | Dónde vive |
|---|---|---|
| Servicio de inferencia OVD config-driven | ✅ | media-plane `:8080`, modelo por proceso (`EOVRT_MODEL_REF`) |
| Fuentes: archivo, carpeta, RTSP, OAK-D | ✅ | `sources/{video_file,image_folder,rtsp,oak_d}_source.py` |
| Prefilter EN-2 on-device | ✅ (opcional, fail-open) | solo `oak_d`; 87% drop medido |
| Preview en vivo para encuadre y prompts | ✅ | `service/preview_manager.py` |
| Motor de patrones temporal CR-01/CR-02 | ✅ | control-plane `:8081`, pattern set `cr01_cr02_v2` |
| Estrategias de evidencia (eind/edir/hyb_or) | ✅ | `engine/evaluators/`, despacho por `evidence.strategy` |
| `hyb_and` | ⚫ **rechazado en validación** con causa | declarado, no silencioso |
| Granularidad escena (G0) / sujeto (G1) | ✅ | `granularity` del patrón + `input.track_persons` |
| Acople DBE (archivo) | ✅ | `eovrt-control replay` |
| Acople EBE (bus ZeroMQ + msgpack) | ✅ | `bus.envelope.v1`, `bus_dropped_events=0` en todas las corridas |
| Evaluación temporal de alertas (5 métricas) | ✅ | `evaluate-alerts` v2 + SDR/TTFD |
| Laboratorio de GT temporal de video | ✅ | video-gt-lab, contrato `clip_gt.v2` |
| Banco de imágenes estratificado | ✅ | `bench_v3`, 6.477 imgs |
| Consola web (gestión + evidencia) | ✅ | 11 pantallas, preflight y lanzamiento gateado |
| Runner de experimentos reproducible | ✅ | manifiestos en `experiments/` |
| Distribución de alertas (MQTT, spec 45) | 🔴 **no implementada** | decisión: es lo último (ADR-005) |

## 4. Lo que NO está implementado (registro honesto)

- **Distribución de alertas por MQTT** (spec 45): especificada, no construida. Por
  decisión de orden (ADR-010: plataforma primero), no por bloqueo.
- **`track_id` producido por el pipeline online del media-plane** (spec 42 §3): hoy la
  identidad la produce el control-plane como decorador de fuente. **Funciona en DBE y
  en live** (verificado, doc 91), pero el productor de identidad no está en el plano
  de medios. Decisión de ADR-002 pendiente si se quisiera llevar a producción.
- **`hyb_and`**: rechazado en validación con causa escrita (doc 87 §5).
- **Ancla de sincronización para EBE-desde-clip**: impide hoy alimentar el banco por el
  bus con correspondencia exacta al GT temporal.
- **F-RT5 sin mergear** a la línea principal (§2.2).
- **Doble anotación / kappa** en el GT de video: decisión declarada (L2), no omisión.

## 5. Trampas operativas vigentes

Consolidadas del doc 68 §6 más las de esta jornada. Las que muerden en silencio:

1. **Levantar cada servicio desde la raíz de SU repo** — las rutas relativas de los
   configs resuelven contra el CWD.
2. **Orden EBE no negociable**: control-plane primero (confirmar `subscribed: true`),
   media-plane después. PUB/SUB pierde lo publicado antes de la suscripción.
3. **Nunca cerrar un socket ZeroMQ desde otro hilo** mientras uno está en
   `recv_multipart` — `SIGABRT`. Para eso existe `request_stop()`.
4. **Nunca usar el pattern set v1** (F-DR9).
5. **El `ping` a una cámara link-local desde WSL en modo NAT miente** — responde el
   gateway de Windows (`ttl=63`). Verificar con `ip route get` (sin `via`) y `ttl=64`.
   Requiere `networkingMode=mirrored` en `.wslconfig`.
6. **`ingest.config` de la OAK-D usa `url`, no `ip`** (con `ip` da 422).
7. **`outputs.base_dir` del control-plane resuelve relativo al archivo de config**, no
   al CWD del script que lo invoca.
8. **El modelo es del proceso, no del run** (`EOVRT_MODEL_REF` al arrancar).
9. **El summary de `/api/runs/{id}` viene anidado bajo `summary`** — leer el nivel de
   arriba devuelve `None` en silencio (mordió al runner del doc 81).
10. **Descubrir el run del control por diferencia de directorios, no por mtime** — el
    mtime cruza las alertas de un clip con el GT de otro sin avisar.
11. **El export de CVAT a nivel PROYECTO numera frames en espacio global** — sin
    `split_cvat_project.py` el GT sale negativo en silencio.
12. **`cameras/` está gitignorado** (credenciales RTSP en claro).

## 6. Estado de git

| Repo | Rama | Último commit | Sin commitear |
|---|---|---|---|
| media-plane | `feature/inference-service` | `94660e6` (08-04) | — |
| control-plane | `feature/*` | `b0ba763` (08-05) | — |
| datasets | `feature/*` | `6577d7b5` (08-05) | — |
| experimental-setup | `feature/*` | `ab2d809` (08-05) | los 4 índices de `results/`, las 6 campañas R1–R6, `prompts/clase_nueva_v1.yaml` |
| docs | local (sin remote por decisión) | `a256250` (08-04) | docs 93–97 + `datos/94-*`, `96-*` |

**Deuda declarada:** `main` desactualizado en los 4 repos con remote (el trabajo vive
en ramas `feature/*`); backup de `docs` a otro disco pendiente (no tiene remote por
decisión del proyecto).

## 7. Qué cambia respecto del doc 56

| Afirmación del doc 56 | Estado hoy |
|---|---|
| "Plataforma completa, integrada y probada E2E" | **Sigue vigente, y además produjo el tramo experimental completo** |
| GT de video `gt_preliminary` | **Superado: `gt_ready`** con adjudicación humana (doc 80) |
| Benchmark de imágenes = BENCH v2 (196 imgs) | **Superado: `bench_v3`** (6.477 imgs, 3 fuentes) |
| Métrica estrella = `cb_b01_p7` (1 clip) | **Superado: 34 clips, 13 campañas** |
| Granularidad: solo escena (G0) | **G1 por sujeto disponible y verificada en vivo** |
| Estrategia de evidencia: solo ausencia espacial | **4 estrategias, 3 implementadas** |

> **Para el informe:** las cifras del doc 56 §9 y de la tabla del brief de redacción
> (`informe/97` §5) están **superadas en su totalidad**. La fuente de cifras vigente es
> `e-ovrt_experimental-setup/results/index.md` y sus cuatro índices.
