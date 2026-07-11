# Spec 44 — experimental-setup (config centralizada, runner, reporte, webconsole)

- **Fecha:** 2026-07-09
- **Estado:** Escrito
- **Repo dueño:** `e-ovrt_experimental-setup` (contiene `prompts/`, `experiments/`,
  `webconsole/` — BFF FastAPI + frontend React, ya cliente del media-plane)
- **Decisiones que implementa:** ADR-004 (manifiesto + `experiment_id` + runner),
  ADR-006 (reporte consolidado), ADR-009 (config centralizada + webconsole como
  superficie de gestión + UX), ADR-001/doc 12 (prompt sets). Normativa: spec 40.

## 1. Config experimental centralizada (ADR-009)

### 1.1 Estructura

```
e-ovrt_experimental-setup/
├── prompts/                      # ya existe (prompt sets versionados)
│   ├── eind_v1.yaml
│   └── edir_v1.yaml              # nuevo — construcción según doc 12 §2 (Tabla C.1)
├── experiments/                  # ya existe (manifiestos)
│   └── <exp-slug>/
│       ├── manifest.yaml         # el paraguas (§2)
│       ├── media_run.yaml        # config de corrida del media-plane
│       └── control_run.yaml      # config de corrida del control-plane
├── patterns/                     # NUEVO: pattern sets del control-plane
│   ├── cr01_cr02_v2.yaml         # el alineado al informe (spec 41 §7)
│   └── diagnostico/              # v1, field_v1 (perfiles de diagnóstico)
├── tuning/                       # NUEVO: tuning sets (si la corrida usa labs)
└── runs/                         # NUEVO: resultados CONSOLIDADos por experimento (git-ignored)
    └── <experiment_id>/          # una instancia (ADR-014): copia lo liviano,
        ├── manifest.effective.yaml   #   referencia los detections.jsonl pesados
        ├── media/ control/ report/
```

> **`experiments/` vs `runs/` (ADR-014).** `experiments/` es la **declaración**
> (manifiestos plantilla, versionados en git: "qué se estudia"). `runs/` son los
> **resultados** de cada instancia (git-ignored: "qué salió"), consolidados por
> `experiment_id`. Config versionada y datos git-ignored no se mezclan (ADR-009 §2). El
> layout de `runs/<experiment_id>/` y el criterio híbrido (copiar lo liviano, referenciar
> los `detections.jsonl` pesados que quedan en el `runs/` del plano como fuente de verdad,
> DA-03) están en **ADR-014**.

- **Frontera (ADR-009 §2):** acá vive lo que **varía entre corridas/experimentos**.
  Lo operacional (puertos, env, `EOVRT_MODEL_REF`, compose) queda en cada repo de
  servicio. Los catálogos por id del media-plane no se duplican: las configs los
  **referencian**.
- Los servicios reciben estas configs **por payload** al disparar (specs 41 §5 /
  42 §4); su `effective_config` persistida en `runs/` sigue siendo el registro de
  qué corrió efectivamente. Regla anti-drift: el reporte (§4) compara el hash de
  lo enviado vs lo efectivo y marca discrepancias.
- El two-root loader del media-plane sobre `prompts/` se conserva intacto
  (restricción histórica del repo: `prompts/` y `experiments/` en la raíz).

### 1.2 Prompt sets (doc 12 §2)

- `eind_v1`: clases canónicas person/helmet/vest.
- `edir_v1`: formulaciones de la **Tabla C.1** por eje (negación, especificidad,
  estado observable, template de presencia), un `prompt_id` por formulación,
  **revisadas por el usuario antes de congelar** (checklist en el manifiesto del
  experimento D1). Congelados = no se editan; una variante nueva es un set nuevo.

## 2. Manifiesto paraguas (`experiment.manifest.v1`)

```yaml
schema_version: experiment.manifest.v1
experiment_id: exp_20260712T140000Z_d1-fase1     # generado al instanciar (§2.1)
slug: d1-fase1
description: ...
runs:
  media:   { service: "http://localhost:8080", config: ./media_run.yaml,
             mode: run }                          # POST /api/runs
  control: { service: "http://localhost:8081", config: ./control_run.yaml,
             mode: live | replay }                # POST /api/runs (spec 41 §5)
sequencing: control_first                         # suscripción previa (spec 40 §3.2)
# Los resultados NO caen junto al manifiesto plantilla (versionado): el runner los
# consolida en runs/<experiment_id>/ (git-ignored, ADR-014). `output` es relativo a
# ese dir de instancia; el runner lo deriva del experiment_id.
report: { output: report/ }
frozen: { prompt_set: eind_v1, pattern_set: cr01_cr02_v2,
          model_ref: gdino-tiny, notes: "hiperparámetros congelados doc 12 §3" }
```

- **No es un schema monolítico** (contención doc 07 D4.2): referencia archivos y
  declara secuencia; los schemas de cada config son de su plano.
- **§2.1 Generación de `experiment_id`:** `exp_<UTC>Z_<slug>` (spec 40 §2), la
  genera el runner o la webconsole al **instanciar** el manifiesto (una plantilla
  de experimento puede instanciarse N veces → N `experiment_id`).

## 3. Runner CLI (ADR-004; el camino reproducible)

`experimental-setup/runner/` (~100–200 líneas, sin estado propio):

1. Lee el manifiesto, genera/toma `experiment_id`.
2. `POST /api/runs` al **control-plane** primero (`mode: live` — queda suscripto;
   spec 41 §5) — orden `control_first` obligatorio con bus.
3. `POST /api/runs` al **media-plane** (config por payload + `experiment_id`).
4. Espera por polling de estado (`GET /api/runs/{id}` en ambos); timeout
   configurable; propaga fallas con exit code.
5. Invoca el generador de reporte (§4) y deja `report.json`/`report.md` junto al
   manifiesto instanciado.

Modo DBE-replay (sin bus): dispara solo media-plane, espera, dispara control-plane
en `mode: replay` apuntando al `detections.jsonl` del run. Las **campañas**
(R1–R4, D1) son listas de manifiestos ejecutadas por el runner — nunca a mano por
UI (ADR-009 §4).

## 4. Consolidación de artefactos y generador de reporte (ADR-014, ADR-006; spec 40 §6)

Dos operaciones distintas del runner, en este orden, **que no deben confundirse**:

**(a) Consolidación de artefactos (ADR-014) — colección, no cómputo.** Tras el fin de
ambas corridas, el runner arma `runs/<experiment_id>/` copiando los artefactos **livianos**
de cada plano (`effective_config`, `summary.json`, `metrics.jsonl`, `alerts.jsonl`,
`pattern_events.jsonl`) y el `manifest.effective.yaml`, y **referenciando** por `run_id`
los `detections.jsonl` pesados (`media/detections.ref.json`), que quedan en el `runs/` del
plano como fuente de verdad (DA-03). Es una **vista/snapshot** para leer/auditar/archivar,
no una segunda fuente de verdad. El "sellado" opt-in (ADR-014 §4) materializa también los
crudos para archivado permanente.

**(b) Generador de reporte (ADR-006) — agrega, no recalcula.**
`experimental-setup/report/` — script, no servicio:

- Entrada: `experiment_id` → el dir consolidado `runs/<experiment_id>/` (o, si no se
  consolidó, los `runs/` de ambos planos por los ids registrados).
- Salida: `report.json` con el schema mapeado a la **Tabla D.6** (spec 40 §6) —
  identificación, modelo/variante, entrada, parámetros, hardware/entorno,
  temporalidad y criterio de relojes, hitos por alerta, resultados con el
  **diccionario completo del spec 40 §5** (cada métrica con
  `status` + `cause`) — y `report.md` legible.
- Regla: **no recalcula** — agrega lo persistido; insumo faltante ⇒
  `applicable_not_computed` con causa, y el reporte sale igual. En el tramo
  plataforma (ADR-010), las métricas de GT salen `not_applicable/no_ground_truth`.
- **Única excepción a "no recalcula": el join de `t_capture→alert`** (spec 40
  §5.2.4). Por cada alerta, el generador une `first_evidence_unit_id` con la fila
  de `metrics.jsonl` del media-plane que tiene ese `unit_id`, y computa
  `t_capture→alert` y `t_compute-budget` con su descomposición (G2A / bus /
  persistencia / reasoning). Es aritmética sobre hitos ya persistidos, no
  re-evaluación. Decide el estado de aplicabilidad leyendo `source_clock` del
  summary del media-plane (spec 42 §5.1) y el criterio de relojes (spec 40 §4):
  `media` ⇒ `not_interpretable/dbe_media_time`; two-node sin sincronización
  declarada ⇒ `not_interpretable/clock_skew`; resto ⇒ `computed`.
  Si falta `first_evidence_unit_id` en una alerta ⇒ `applicable_not_computed /
  missing_join_key` para esa alerta (no aborta el reporte).

## 4.1 Aplicabilidad por temporalidad de la fuente (ADR-013)

El reporte lee `pattern_evaluation.state` del `summary.json` del control-plane y
`source_clock` del summary del media-plane. Cuando la fuente es no temporal
(`source_clock: none` / `source_type: "image"`), el reporte **omite y explica** —nunca
reporta en cero— las métricas de naturaleza temporal:

| Métrica | Sobre dataset de imágenes |
|---|---|
| `t_capture→alert` | `not_applicable / non_temporal_source` |
| `t_compute-budget` | **`computed`** (monotónico, independiente de la fuente) |
| TTFA interna, latencias de confirmación | `not_applicable / non_temporal_source` |
| `re_alerts` por episodio, estabilidad | `not_applicable / non_temporal_source` |
| G2A, mAP, AP por clase, recall por persona | `computed` — son métricas de percepción |

La corrida se rotula en el reporte como **diagnóstico espacial / smoke de contrato**, no
como evaluación de patrones.

## 5. Webconsole: superficie de gestión de la plataforma (ADR-009)

### 5.1 Alcance funcional nuevo

| Capacidad | Detalle |
|---|---|
| Cliente del **control-plane** | Segundo `RunBackend` en el BFF apuntando a :8081 (mismo patrón cliente-HTTP que ya usa con el media-plane; el BFF sigue siendo el único origen para el navegador). |
| **CRUD de configs de experimento** | Crear/editar/instanciar manifiestos y configs de §1.1 (archivos del repo — el BFF escribe en el árbol versionado; git sigue siendo manual, regla del workspace). |
| **Disparo orquestado** | Botón "ejecutar experimento" = la misma secuencia del runner (§3), implementada llamando a las mismas APIs; para campañas largas la UI recomienda el runner. |
| **Vista de alertas** | Lee `GET /api/runs/{id}/alerts` del control-plane (spec 41 §5) — polling; sin ZeroMQ en la consola (spec 40 §3.3). Tabla: condición, severidad, estado, timestamps de hitos, subject/escena. |
| **Agrupación por experimento** | `experiment_id` como eje: un experimento muestra sus dos corridas (+ distribución cuando exista), su manifiesto, su reporte. **Origen único de la vista: el dir consolidado `runs/<experiment_id>/` (ADR-014)** — manifiesto + configs + summaries + alertas + reporte; cae al `runs/` del plano solo para el `detections.jsonl` bajo demanda. |
| **Detección de fuente no temporal** (ADR-013) | Al seleccionar un data source, la consola **detecta el tipo** (`type: image_folder` en la config; re-confirmado por `source_type` en el primer evento) y lo comunica **antes de correr**: rotula la corrida como diagnóstico espacial / smoke, deshabilita los controles de umbrales temporales (inertes sobre imágenes), oculta las vistas de métricas temporales, y **advierte** si el pattern set elegido configura persistencia — esa corrida no podrá alertar. La detección es automática: no hay un toggle que el operador pueda contradecir. |

### 5.2 Rediseño UX (la parte declarada sacrificable — doc 10 ítem 11)

- **Navegación por experimento, no por servicio:** home = lista de experimentos
  (estado agregado de sus corridas); detalle = timeline manifiesto → corridas →
  alertas → reporte. Las vistas actuales por-run del media-plane pasan a ser el
  drill-down.
- Composición actual (formulario de corrida) se conserva como "corrida suelta"
  (sin experimento) — útil para diagnóstico; queda visualmente separada.
- Criterio de recorte: si la agenda aprieta, se sacrifica **solo** el rediseño de
  navegación (11-UX); el cliente del control-plane, el CRUD mínimo y la vista de
  alertas son estructurales (los usa la demo de R4).

## 6. Orden de implementación sugerido

1. Estructura §1.1 + `edir_v1` (con revisión del usuario) + pattern set v2
   movido/creado acá. *(gate: media-plane y control-plane corren con configs
   servidas desde este repo por payload)*
2. Manifiesto + runner modo DBE-replay + **consolidación de artefactos (ADR-014)**.
   *(gate: Fase 0 real —media→control sobre detecciones reales— ejecutada por el runner
   con `experiment_id` end-to-end, y `runs/<experiment_id>/` armado con lo liviano copiado
   y los `detections.jsonl` referenciados)*
3. Generador de reporte. *(gate: `report.json` de esa Fase 0 con diccionario
   completo y estados, leído desde el dir consolidado)*
4. Runner modo live (cuando specs 41/42 entreguen el bus). *(gate: corrida EBE 1:1)*
5. Webconsole: backend (cliente control-plane + endpoints de configs) → vista de
   alertas → agrupación por experimento → rediseño UX. *(gates por PR con la
   deuda Fase 2 existente de la consola priorizada detrás de esto)*

## 7. Criterios de terminado (evidencia)

- [ ] Un experimento completo (manifiesto → dos corridas → reporte) ejecutado por
      el runner **y** el mismo flujo disparado desde la webconsole, con el mismo
      `experiment_id` visible en todos los artefactos.
- [ ] `report.json` validando contra el schema del spec 40 §6, con hash
      enviado-vs-efectivo verificado (§1.1).
- [ ] `t_capture→alert` + `t_compute-budget` computados por alerta con su
      descomposición y su estado de aplicabilidad correcto en dos corridas: una
      DBE-archivo (`not_interpretable/dbe_media_time` + budget `computed`) y una
      EBE-RTSP (`computed`). **Es el criterio que cierra el tramo plataforma.**
- [ ] Vista de alertas mostrando una corrida live real (aunque sea con mock/RTSP
      de prueba — tramo plataforma, sin GT).
- [ ] `edir_v1` congelado con acta de revisión del usuario (fecha + versión).
- [ ] Prompts/patterns/tuning consumidos SOLO desde este repo en las corridas de
      experimento (nada hardcodeado en los servicios).

## 8. Interfaces

- **Specs 41/42:** APIs de disparo/estado/alertas; config por payload.
- **Spec 45:** el reporte incorpora `delivery` cuando el repo de distribución
  exista; la vista de alertas puede mostrar el outcome de entrega (fase 2).
- **Spec 43 (diferido):** las campañas de evaluación son manifiestos que iteran
  el manifest del clip bench; nada nuevo aquí.
