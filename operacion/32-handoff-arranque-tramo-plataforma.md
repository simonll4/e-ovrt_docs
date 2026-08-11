# Handoff — arranque del tramo plataforma

> **SUPERADO (2026-07-10).** Todo lo que este doc mandaba ejecutar está hecho: Paso 0
> (doc 33) y G0 completo con verificación real (docs 34–35). **El punto de entrada
> vigente es [`operacion/36-handoff-plan2-bus-y-live.md`](36-handoff-plan2-bus-y-live.md).**
> Este doc queda como registro del arranque.

- **Fecha de congelamiento:** 2026-07-09
- **Para quién:** la sesión que empieza a **implementar** (hasta acá el trabajo fue
  documental: 11 ADRs + 6 specs). Este doc dice **dónde estamos, qué leer, qué
  ejecutar primero y hacia dónde va**.
- **Regla de oro:** las decisiones están cerradas. Si algo parece ambiguo, la
  respuesta está en un ADR o en un spec — no re-litigar, buscar. Si de verdad
  falta una decisión, se escribe un ADR nuevo, no se improvisa en el código.

## 1. Qué leer, en este orden (30 min)

| # | Documento | Por qué |
|---|---|---|
| 1 | `00-indice.md` | Mapa del set y estado del tablero. |
| 2 | `decisiones/README.md` | Las 11 decisiones, en una tabla. **Leer los ADRs 002, 008, 010, 011 completos** — son los que más afectan al código. |
| 3 | `specs/README.md` | La cola y el orden de ejecución. |
| 4 | `specs/40-plataforma-etapa4-integrador.md` | **Normativa transversal**: envelope del bus, `experiment_id`, criterio de relojes, diccionario de métricas (incl. §5.2, `t_capture→alert`). Todo lo demás lo cita. |
| 5 | `specs/41-control-plane.md` | El spec que se implementa primero. |
| 6 | `nucleo/historicos/01-relevamiento-control-plane.md` §12 | Qué hizo la rama `mati` (motor mejorado + labs). |

Lectura opcional según toque: `specs/42` (media-plane), `nucleo/05` (diseño del
bus), `nucleo/12` (prompts y fusión E-HYB, para cuando toque el evaluador D1).

## 2. Estado congelado de los repos

| Repo | Rama | Estado |
|---|---|---|
| `e-ovrt_control-plane` | **`feature/control-service`** (creada desde `mati`, base `443712b`) | Árbol limpio. `.venv` creado con `pip install -e ".[dev]"`. **Núcleo 18/18 verde**, incluido el gate de regresión temporal (F1 = 1.0). |
| `e-ovrt_media-plane` | `feature/inference-service` | Árbol limpio (commit `e12b56a`, visibilidad two-node). **440 tests verdes.** 3 commits sin pushear, 38 sin mergear a `main` — el usuario maneja git. |
| `e-ovrt_experimental-setup` | — | Webconsole funcionando como cliente del media-plane. Sin cambios de este tramo aún. |
| `docs` (este repo) | `main` | Repo git propio, **local, sin remote**. 19 archivos sin commitear (ADRs 010/011 + specs 40–45). |

**Falla conocida no bloqueante:** `tests/labs/test_perception_generator.py` falla
por `ModuleNotFoundError: numpy` — importa contratos del media-plane cross-repo y
`numpy` no está en el extra `dev`. No es regresión. Correr el núcleo con
`.venv/bin/python -m pytest -q --ignore=tests/labs`. Arreglarlo cuando se toque
`labs` (o marcar el test como `requires labs`).

## 3. Reglas del workspace (no negociables)

1. **Nunca commitear sin pedido explícito del usuario en ese turno.** Vale también
   para specs/planes escritos por skills.
2. **Nunca agregar `Co-Authored-By`.**
3. **No crear nada en GitHub.** Todo local. Si hace falta backup, copia a otro disco.
4. **Cuidado con Docker/WSL**: entender el blast radius antes de correr nada; la
   "Capa 3" del control de disco mata WSL.
5. Los dos repos son hermanos en disco y las rutas relativas de config lo asumen.

## 4. PASO 0 — Re-correr la Fase 0 con el motor de `mati` (primero, sin código)

> **EJECUTADO el 2026-07-09. Paso 0 CERRADO.** Resultados, hallazgos y correcciones a
> esta sección en [`operacion/33-fase0-rerun-motor-mati.md`](33-fase0-rerun-motor-mati.md).
> Dos avisos, si estás leyendo esto para ejecutarlo de nuevo: la predicción de §4.3 **falló
> y era la predicción la que estaba mal** (el BENCH no contiene EPP disputado entre personas,
> así que el matching 1:1 es un no-op y las alertas se mantienen en 137); y el criterio 3 de
> §4.4 **es inalcanzable con `cr01_cr02_v1`** — requiere una corrida diagnóstica aparte.

**Por qué:** la Fase 0 del 2026-07-06 corrió con el **motor viejo** (matching por
contención). El doc 01 §12.4.6 exige re-ejecutarla con el motor nuevo **antes de
calibrar nada**. No necesita una sola línea de código y entrega tres cosas:
valida que el contrato sigue alineado tras la migración de `timing` que hizo
`mati` (`read_ms`/`preprocess_ms` → `normalize_ms`); da los números baseline del
motor nuevo; y **hace visible el warning de `det_NNN`**, que es la evidencia
empírica de por qué G0 es el primer cambio.

### 4.1 Trampa: `configs/replay_dbe_cr01_cr02.yaml` está roto

Apunta a `../../e-ovrt_media-plane/runs/latest/detections.jsonl` y **`runs/latest`
no existe**. Hay que apuntar a una corrida concreta (o crear el symlink).

### 4.2 Diseño del experimento: variable única = el motor

Usar **exactamente el mismo input y el mismo pattern set** que la Fase 0 previa,
para que toda diferencia sea atribuible al motor:

- Input: `e-ovrt_media-plane/runs/run_20260704_205708_dbe_grounding_dino_96b2b0/detections.jsonl`
  (GDINO sobre BENCH, 82 unidades).
- Pattern set: `configs/patterns/cr01_cr02_v1.yaml` (confirm 1 frame).
  **No usar `field_v1`**: su `coverage_memory` está pensado para video, no para
  imágenes independientes, y contaminaría la comparación.

```bash
cd /home/simonll4/projects/e-ovrt_control-plane
# copiar el config de la fase0 previa y ajustar run.name; o editar el dbe config
.venv/bin/eovrt-control replay <config.yaml>
```

### 4.3 Baseline contra el que comparar (motor viejo, `fase0_dbe_gdino_bench_20260706`)

| Métrica | Motor viejo |
|---|---|
| `units_processed` | 82 |
| `units_failed` / `errors_count` | 0 / 0 |
| `pattern_events_count` | 137 |
| `alerts_count` | **137** |
| `avg_processing_ms` | 0.129 |

~~**Qué esperar del motor nuevo:** menos alertas de CR-02 (…). Si las alertas **no bajan**,
investigar antes de seguir.~~

**CORREGIDO (doc 33 §3).** Se esperaba menos alertas de CR-02 por el matching bipartito 1:1.
**No bajan, y es correcto que no bajen:** se midió el input y tiene **cero** items de EPP
disputados (ningún casco ni chaleco cae en la región de más de una persona), de modo que
sobre este corpus el matching 1:1 y el matching por contención son la misma función. El
BENCH de imágenes no sirve para demostrar el valor del matching 1:1; eso requiere material
con personas superpuestas (clip bench, spec 43). El resultado esperado es **137 = 137**.

### 4.4 Criterio de terminado del Paso 0

- [x] Corrida completa sin errores de contrato (`errors_count: 0`).
- [x] Tabla comparativa viejo-vs-nuevo (alertas por condición) escrita → doc 33 §2.
- [x] Warning de ids inestables (`det_NNN`) capturado como evidencia → doc 33 §4.
      **Ojo:** el warning está gateado por `confirm_after_frames > 1`, así que **no puede
      dispararse con `cr01_cr02_v1`**. Se capturó con una corrida diagnóstica aparte
      (`configs/fase0_dbe_gdino_bench_persistence_probe.yaml`), para no contaminar la
      comparación de motores, que exige variable única.

## 5. Hacia dónde vamos: el tramo plataforma

**Objetivo declarado por el usuario:** la plataforma experimental completa y
funcional = **media-plane y control-plane trabajando en conjunto, generando los
eventos correctos, con métricas desde la captura del frame hasta la generación del
evento**. El módulo de distribución de alertas (spec 45) queda **para el final**:
es simple y rápido.

**Criterio de cierre del tramo** (spec 40 §7 + spec 44 §7): una corrida EBE con
`t_capture→alert` y `t_compute-budget` computados y atribuidos por alerta (join por
`unit_id`), y una corrida DBE donde `t_capture→alert` figura
`not_interpretable/dbe_media_time` y el budget `computed`. Es decir: **la
instrumentación completa demostrada antes de que exista el dataset con GT.**

### 5.1 Orden de trabajo (spec 41 §10, con sus gates)

1. **G0 en el motor** (spec 41 §2) — clave de estado `(pattern_id, source_id)`,
   `granularity: scene|subject` por patrón, fixture regenerado a escena-condición.
   *Es el cambio que hace que los eventos sean correctos*: hoy el estado se acumula
   sobre `det_NNN`, que en video real aliasa personas distintas.
   **Gate:** F1 = 1.0 en ambas granularidades.
2. **`MediaEventSource`** (jsonl/memory) — **Gate:** replay actual intacto.
3. **Bus**: publisher en media-plane (spec 42 §2) + `BusSource` + runtime live
   (spec 41 §3–4). **Gate:** test de paridad replay↔stream.
4. **Servicio mínimo** del control-plane (spec 41 §5). **Gate:** smoke por API + 409.
5. **Instrumentación** de `t_capture→alert` (spec 40 §5.2.4: campos por `unit_id` en
   ambos planos) + pattern set `cr01_cr02_v2`. **Gate:** una alerta con su cadena
   de latencias atribuida frame→evento.
6. **experimental-setup** (spec 44): `experiment_id`, runner, reporte consolidado.
7. Evaluadores D1 + fusión E-HYB (spec 41 §6) — puede correr en paralelo desde (4).

Después: spec 43 (clip bench, su disparador es el cierre del 44) y spec 45.

## 6. Las decisiones que NO se re-litigan (resumen operativo)

- **E-IND es el núcleo** (ADR-001). E-DIR es variante; E-HYB-or/and se corre siempre
  en la Fase 2 del experimento D1. Vote excluida.
- **G0 (escena) es el núcleo; G1 (sujeto) es demostrativa** (ADR-002). El tracker de
  `eovrt_labs` se porta al media-plane como `track_id` **opcional aditivo** (sin bump
  de versión del contrato). Sin métricas MOT.
- **Bus ZeroMQ PUB/SUB**, broker excluido (ADR-003). El JSONL es la verdad; el bus
  transporta. Suscribirse **antes** de disparar el run; huecos de `seq` ⇒ corrida
  degradada declarada.
- **`experiment_id` paraguas** desde experimental-setup (ADR-004); el runner CLI
  orquesta por HTTP; **la webconsole no consume ZeroMQ** (usa las APIs).
- **Distribución: repo propio, canal MQTT** (ADR-005), al final.
- **El control-plane pasa a servicio mínimo** (ADR-008); la CLI se conserva.
- **Config experimental centralizada en experimental-setup** (ADR-009); la webconsole
  es la superficie de gestión de ambos planos.
- **Plataforma primero** (ADR-010); el clip bench se ejecuta al cerrar el spec 44.
- **El motor emite `AlertEvent` en CADA confirmación** (ADR-011). **El cooldown NO va
  en el motor** — es política de notificación del módulo de distribución. El pattern
  set `cr01_cr02_v2` va **sin cooldown**. El evaluador cuenta `re_alerts` por
  episodio como estabilidad, **no como falsos positivos**.

## 7. Trampas conocidas

- `runs/latest` no existe en el media-plane (§4.1).
- El `.venv` del control-plane hay que crearlo; sin él, `pytest` falla al recolectar.
- El WS del media-plane emite **resúmenes**, no `DetectionEvent` completos: no sirve
  como bus (por eso existe el `BusPublishingArtifactWriter`).
- El media-plane tiene trabajo valioso sin pushear ni mergear a `main`.
- `eovrt_labs` vive en el repo del control-plane pero **no es la percepción canónica**
  (esa es el media-plane). Es herramienta de calibración y generación de fixtures.
  No importarlo cruzado.
- Cambios de contrato: **siempre aditivos** (campos opcionales con default).

## 8. Pendiente de decisión del usuario (no avanzar solo)

1. **Integrar `mati` a `main`** en el control-plane (es fast-forward, 11 commits,
   cero divergencia) — es coordinación con el compañero de equipo.
2. Commits/push de `docs` y del media-plane.
3. Revisión y congelamiento de las formulaciones de `edir_v1` (doc 12 §2.2:
   requiere acta de revisión del usuario antes de correr el experimento D1).
