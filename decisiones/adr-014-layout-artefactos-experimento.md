# ADR-014 — Layout y consolidación de artefactos por experimento

- **Fecha:** 2026-07-10
- **Estado:** Aceptada
- **Decisión que atiende:** nueva (decisión del usuario). Precisa ADR-004/006/009 sobre
  **dónde caen los resultados de un run global** y cómo se centralizan.
- **Decisor:** usuario, 2026-07-10

## Decisión

### 1. Dos clases de corrida, dos destinos

- **Run global (experimento):** lanzado por el runner o la webconsole con un
  **`experiment_id`** y un manifiesto paraguas (ADR-004); involucra ≥ 2 planos
  (media + control, y a futuro distribución). Sus resultados se **consolidan** en
  `e-ovrt_experimental-setup/runs/<experiment_id>/` (git-ignored).
- **Run de test de un módulo (corrida suelta):** sobre un solo plano, sin
  `experiment_id`. Queda en el `runs/` **local de ese plano** y **no se consolida** —
  es diagnóstico/smoke, se configura y se lee en su propio repo (spec 44 §5.2). Un
  operador que prueba solo el media-plane o solo el control-plane no paga ninguna
  ceremonia de experimento.

### 2. Consolidación híbrida selectiva (el run global)

El directorio del experimento **copia físicamente** los artefactos **livianos y
decisivos** de cada plano y **referencia por `run_id`** (puntero, no copia) los
`detections.jsonl` **pesados**, que permanecen en el `runs/` del plano:

```
e-ovrt_experimental-setup/runs/<experiment_id>/     (git-ignored)
├── manifest.effective.yaml         # el manifiesto instanciado (provenance + hash)
├── media/
│   ├── effective_config.yaml        # qué corrió realmente en el media-plane
│   ├── summary.json                 # (incluye source_clock, g2a)
│   ├── metrics.jsonl                # capture_*, g2a_ms por unit_id
│   └── detections.ref.json          # { run_id, path } -> media-plane/runs/<id>/detections.jsonl
├── control/
│   ├── effective_config.yaml
│   ├── summary.json                 # (media_run_id, bus_dropped_events, pattern_evaluation)
│   ├── alerts.jsonl
│   ├── pattern_events.jsonl
│   └── metrics.jsonl                # ts_receive_ms, processing_ms por unit_id
└── report/
    ├── report.json                  # consolidado por experiment_id (Tabla D.6)
    └── report.md
```

El `detections.jsonl` es el artefacto dominante en disco (una línea por frame; un video
de cientos de frames son MB–GB). Todo lo demás es chico. **Copiar lo chico y referenciar
lo grande es el punto óptimo**: da la centralización real (leer/auditar/archivar un
experimento desde un solo lugar) sin duplicar los crudos ni violar DA-03.

### 3. Fuente de verdad y divergencia (no se rompe DA-03)

- La copia liviana en `runs/<experiment_id>/` es una **vista/snapshot** para leer,
  auditar y archivar el experimento. **No** es una segunda fuente de verdad. Ante
  cualquier divergencia, gana el `runs/` del plano (DA-03, ADR-003).
- El `report.json` se sigue generando por **agregación sin recálculo** (ADR-006 intacto).
  La consolidación de artefactos es una operación de **colección**, separada del cómputo
  del reporte. El único recálculo permitido sigue siendo el join `t_capture→alert`
  (spec 44 §4, excepción ya declarada).
- **Layout, resumido:** `experiments/<slug>/` (versionado en git) = la **declaración**
  (manifiesto plantilla, "qué se estudia"); `runs/<experiment_id>/` (git-ignored) = los
  **resultados** de una **instancia** ("qué salió"). Una plantilla se instancia N veces
  → N `experiment_id` → N directorios de resultados. Config versionada y datos
  git-ignored no se mezclan (coherente con ADR-009 §2).

### 4. Archivado permanente (sellado) — opt-in

La re-evaluabilidad offline (ADR-003: "toda corrida live es re-evaluable con artefactos
idénticos") requiere el `detections.jsonl`, que en el híbrido queda **referenciado**: se
preserva **mientras el `runs/` del plano viva**. Para un experimento que deba conservarse
más allá de la poda del plano (campañas congeladas R1–R4, D1), una acción explícita de
**"sellar experimento"** materializa (copia) también los `detections.jsonl` referenciados,
volviéndolo autocontenido y re-evaluable de forma permanente. El sellado es opt-in, no el
comportamiento por default: el default no duplica GB.

## Alternativas consideradas

- **Copia total por default:** autocontenido siempre, pero duplica los crudos pesados en
  cada corrida y crea dos fuentes de verdad (tensión directa con DA-03). Se conserva solo
  como el **sellado explícito** (§4), no como default.
- **Solo referencia (spec 44 original):** cero duplicación, pero no entrega "todo en un
  lugar" —hay que resolver referencias en 2–3 repos— y un `runs/` podado deja el reporte
  apuntando a la nada. La consolidación híbrida lo supera preservando localmente lo
  liviano (summaries/alerts/metrics/configs), que es lo que hace re-legible un experimento.

## Fundamento

- Da la centralización que el operador pidió (config + resultados de la plataforma en un
  lugar ordenado por `experiment_id`) sin pagar la duplicación de los crudos ni violar la
  regla de que el repositorio del plano es la fuente de verdad.
- El costo dominante en disco son los `detections.jsonl`; copiarlos por default sería caro
  y redundante. El híbrido optimiza exactamente ese eje.
- Los planos no cambian: siguen escribiendo su `runs/` local. La consolidación es **aguas
  arriba** —la hace el runner tras el fin de ambas corridas, leyendo por las mismas APIs y
  artefactos que ya expone— así que no acopla los planos entre sí ni al experimental-setup.

## Impacto

- **spec 44** (ajustado en esta misma edición): nuevo paso de **consolidación** en el
  runner (§4), layout `runs/<experiment_id>/` (§1.1), `report.output` apuntando al dir de
  la instancia (§2).
- **experimental-setup:** `.gitignore` de `runs/`; el consolidador como paso del runner
  (~después del polling de fin de ambas corridas); la acción de "sellar" opcional.
- **webconsole:** al agrupar por `experiment_id`, lee el dir consolidado como origen único
  de la vista del experimento (manifiesto + configs + summaries + alertas + reporte), y
  cae al `runs/` del plano solo para el `detections.jsonl` bajo demanda.
- **Ningún cambio en los planos.** Es trabajo del ítem 6 (spec 44); se implementa cuando
  ese ítem se tome. Registrado en `operacion/50` §8.2.

## Referencias

ADR-003 (DA-03: el repositorio del plano es la fuente de verdad), ADR-004 (paraguas +
`experiment_id`), ADR-006 (reporte agrega, no recalcula), ADR-009 (config centralizada;
frontera config/datos). Spec 44 §1.1/§2/§4/§5.2. Doc 50 §8.2.
