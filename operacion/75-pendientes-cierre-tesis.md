# 75 — Qué falta para cerrar la tesis con resultados defendibles (relevamiento integral)

- **Última actualización:** 2026-07-29 (documento VIVO: cada ítem cerrado queda
  tachado con fecha; el tablero restante consolidado está en §7)
- **Propósito:** foto única de TODO lo pendiente para cerrar la implementación con
  resultados correctos y defendibles ante el tribunal (~fines de septiembre 2026).
  Reemplaza la lista "lo único que falta" del doc 62 §9, que quedó del 2026-07-23.
- **Método:** relevamiento simultáneo de los 5 repos el 2026-07-28 (git, docs,
  registries, tests, configs); cierres del 29/07 verificados con revisión
  adversarial (2 revisores + 2 correctores) y suites frescas.

## 0. Estado en una línea

**La plataforma está terminada y verificada**, los **6 riesgos de correctitud del §2
están cerrados**, la **maquinaria de Fases T/P/D está lista sin deuda de código**, y
la **documentación de defendibilidad (§3.3) está al día**. Lo único que convierte
corridas en resultados es la **pasada humana de GT en CVAT — EN CURSO (usuario,
desde 2026-07-29)**. Suites al cierre del 29/07: datasets **188** / control-plane
**251** / BFF **586** / frontend **381** — todo verde, verificado en fresco.

## 1. Ruta crítica de resultados (sin esto no hay Fase T → P → D → reporte)

| # | Pendiente | Desbloquea | Ref |
|---|---|---|---|
| 1 | **Pasada humana CVAT** — 🔄 **EN CURSO (usuario, desde 2026-07-29)** sobre el lote de 48 clips pre-anotados (34 rodaje + 14 internet, GDINO-base + ByteTrack, 0 fallidos). Al terminar cada clip: export XML → `derive_clip_gt` → `promote_clip` → `build_clip_bench` (secuencia exacta en el docstring de `build_clip_bench.py`) | Fase T completa | doc 60 §5, GUIA-CIERRE §1 |
| 2 | ~~Ficha de eventos → recorte~~ **superado por los hechos**: el recorte ya ocurrió (48 clips cortados, con `.clip.yaml`, subidos a CVAT). Si alguna marca de ficha quedó incompleta, ya no bloquea nada | — | doc 72 §5.1 (histórico) |
| 3 | **GT CVAT del material del rodaje** — dentro del mismo lote en curso del ítem 1; la doble anotación parcial para medir acuerdo (equipo de 3) sigue siendo el protocolo | Fase T con material propio | doc 58 §B.3 |
| 4 | ~~**Acta de congelamiento `edir_v1` + `eind_v1`**~~ **CERRADO 2026-07-29 (doc 76)**: ambos `frozen` con sha256; Fase D desbloqueada | Fase D (D1 E-DIR vs E-IND) | doc 76 |
| 5 | ~~**Promoción laboratorio→banco**~~ **CERRADO 2026-07-29**: `build_clip_bench.py` ensambla el banco (manifest agregado análogo a bench_v3: composición P1–P9, soak/FAR, gate `gt_ready` con `--allow-preliminary` no-reportable, cruce `xml_sha256`, freeze verificable con `sha256sum -c`); 17 tests; secuencia del día del GT en el docstring | Fase T (estructura del banco) | doc 54 §5.4 |
| 6 | ~~**Cablear `far_per_hour`/`censored_episodes` al reporte**~~ **CERRADO 2026-07-29**: `report.py` del BFF propaga `far_per_hour`, `observed_duration_ms` y censurados (conteo + detalle) con semántica ADR-006 (`evaluation_without_v2_fields` para evaluaciones viejas Y para el path v1 vigente, que emite defaults de Pydantic — gate `_censura_evaluada` por `observed_duration_ms`, rojo-verde verificado); BFF 586 passed | Fase P sin re-corridas | docs 51/58 |
| 7 | **1–2 clips soak de 5–10 min (`negative: true`)** para FAR/hora con denominador serio (hoy n≈12 clips de 30 s → estimador de FP sesgado). Costo de anotación ≈ 0 | G1 metodológico de Fase T | doc 57 |

**El único cuello real es el GT humano (ítems 1/3, EN CURSO): todo lo demás de esta
tabla quedó cerrado el 29/07.** Fases S, L0 y L1 están CERRADAS (docs 64/66/65/67/71;
el doc 62 §9 ya lleva banner de "superado, ver doc 75").

## 2. Correctitud — riesgos que INVALIDAN números si no se corrigen

Hallazgos del relevamiento que ningún registry declaraba completos:

1. ~~**`person_gt.json` del núcleo desincronizado con la curación**~~ **CERRADO
   2026-07-29**: generado `curated/person_gt_bench_obra.json` sobre los 147 curados —
   **262 personas, 60 violadores CR-01** (no 65: la curación también removió
   `bare_head` sub-pixel que era la única evidencia de 5 violadores; subconjunto
   estricto verificado y pinneado en `test_person_gt_bench_obra.py`). `bench_v3.md`
   ahora instruye el archivo nuevo y marca `person_gt.json` como HISTÓRICO prohibido.
   **OJO: todo número CR-01 del núcleo citado antes con denominador 111 debe releerse
   contra 60.**
2. ~~**`cr01_cr02_v1` activo sin marca de deprecado**~~ **CERRADO 2026-07-29** (lado
   config): banner de deprecación en el YAML v1 (también en su `description`),
   `replay_dbe_cr01_cr02.yaml` migrado a v2, cero configs activas apuntando a v1
   (tests de mecánica por frames y `_archive` quedan legítimamente); suite 251 passed.
   **Sigue pendiente** re-generar un informe de resultados con v2 (§3.2).
3. ~~**El test espejo de prompts rojo enmascara la verificación de hashes**~~
   **CERRADO 2026-07-29 (doc 76 §5):** `safety_vest` normalizado a `exploratory`,
   espejo amplía `track` con `comparative`, `edir_v1`/`eind_v1` congelados.
   `test_prompt_store.py` 15/15 — la aserción de integridad `frozen_sha256` vuelve
   a ejecutarse para todos los sets. Backend BFF 578 passed.
4. ~~**sha256 de `bench_v3` no verificable**~~ **CERRADO 2026-07-29**:
   `build_bench_v3.py` ahora escribe la misma serialización que hashea
   (`freeze_payload`, sort_keys); artefacto regenerado (solo orden de claves,
   conteos intactos, manifest **byte-idéntico** — `bench_v3_sha256` no cambió);
   `sha256sum bench_v3.json` coincide; test de pin nuevo
   (`test_bench_v3_freeze.py`) y procedimiento documentado en `bench_v3.md`.
5. ~~**Bug de denominador gemelo** en `evaluate_bench.py`~~ **CERRADO 2026-07-29**:
   `evaluate_cr01()` restringe con doble criterio (imagen en el bench evaluado Y
   cubierta por el run — mismo espíritu que `restrict_gt_to_detections`), expone
   `n_violators_gt_total` y reporta violadoras fuera del denominador; 4 tests.
6. **Task 4.3 del bench sin ejecutar** — checkpoint humano, sigue en manos del
   usuario, pero el **kit está listo (2026-07-29)**:
   `datasets/processed/audit_task43/` (24 PNGs con GT dibujado, muestra determinista
   seed 43: 12 con violador + 12 conformes, 55 personas) y la tabla §4 de
   `bench_gt_audit.md` pre-cargada; solo falta marcar ✓/✗, resumen §5 y firma §6.
   La muestra sale de las 147 curadas y audita `person_gt_bench_obra.json`
   (decisión registrada en §3 del registry). ~15 min.

## 3. Defendibilidad — git, evidencia y documentación

### 3.1 Git: `main` no tiene el sistema que se defiende (los 4 repos con remote)

| Repo | Situación |
|---|---|
| media-plane | `feature/inference-service` **59 commits adelante de `main`**; `main` además tiene 17 commits locales SIN pushear; **`perf/producer-pil-roundtrip` (`3deb64c`, +18% fps, salida byte-idéntica) sin mergear** — única decisión técnica abierta del repo (doc 73 §10.4) |
| control-plane | `feature/control-service` **22 commits adelante de `main`** (bus, servicio :8081, evaluate-alerts v2, TTFD/SDR); rama `mati` 100% integrada, pendiente de borrar |
| datasets | `feature/datasets-v2-setup` **19 commits adelante de `main`** (todo bench_v3 + video-gt-lab) |
| experimental-setup | `feature/webconsole-consola-tesis` **59 commits adelante de `main`** (main = solo docs); **`feature/webconsole-rediseno-fundacion` (88 commits) existe SOLO local, sin respaldo remoto** — pushear o descartar conscientemente; worktree residual con 11 untracked |

Si el tribunal clona `origin/main` de cualquier repo, **no obtiene el sistema descrito
en la tesis**. Decisión: mergear a `main` (o declarar explícitamente la rama de
trabajo como la canónica). El repo `docs` está limpio y al día (backup a otro disco
sigue pendiente — es la única copia).

**➡️ La receta completa, comando por comando, está en el doc 77** (2026-07-29):
commits del trabajo del 29/07, push PRIMERO de la rama huérfana, merges a `main`
×4, borrar `mati`, merge recomendado de `perf`, bundle de `docs` a otro disco.

### 3.2 Evidencia sin consolidar

- **Ningún resultado versionado en control-plane**: `runs/*` gitignorado entero, 36
  corridas en disco, cero evidencia reproducible commiteada con pattern set v2.
  **Decisión 2026-07-29: el informe v2 se genera EN FASE T con el GT humano de CVAT**
  — generarlo hoy versionaría números `gt_preliminary` destinados a ser superados
  en días; la maquinaria ya está lista (§1.5/§1.6) y el camino queda sin deuda de
  código.
- **Los 10 manifiestos `experiment.manifest.v1`** (ebe_*, yoloe_p*, rt-01,
  diag_riesgo_activo, video16_clip10_gt) tienen `report: {}` y `frozen: {}` vacíos:
  son ejecutables, no evidencia cerrada. Congelarlos/reportarlos o marcarlos
  exploratorios fuera del alcance.
- **Los 6 experimentos de la comparación GDINO/YOLOE no tienen consolidado ni
  `report.json`** (stop manual → `stopped` → `ok: false`; doc 71 §5). Decisión
  pendiente: ¿`stopped` limpio consolida?
- **Parity live↔offline no re-verificada** con las corridas nuevas (doc 71 §5).
- ~~Informe suelto en la raíz del control-plane~~ **reubicado 2026-07-29** a
  `docs/reportes/2026-07-25-patterns-live-endpoint.md` (se commitea con el resto).
  Quedan los residuos `.superpowers/*experiment-id*` en media-plane (gitignorados,
  limpieza cosmética).
- Verificación visual de la Task 12 del rediseño de consola (4 capturas vs prototipo,
  clasificando diferencias deliberadas vs deuda) sin rastro: 90 checkboxes, 0 tildados.

### 3.3 Documentación desincronizada (lo que un tribunal detecta primero)

- ~~**control-plane: 8 ADRs citados en código que NO existen**~~ **CERRADO 2026-07-29**:
  hallazgo estructural — el código cita la serie de ADRs DEL PROYECTO (repo docs,
  `decisiones/`, completa), no una serie local perdida; lo que faltaba era su
  materialización en el repo para auditoría standalone. Materializados
  `docs/decisions/ADR-0006..0013` (8 archivos, formato de los existentes, todos con
  fuente primaria fechada 2026-07-09 — nada reconstruido de memoria; ADR-0011/0012 =
  por qué cooldown y memoria de cobertura quedan fuera del motor bajo `scene`).
  `docs/progress.md` actualizado con sección 2026-07-29 anclada a commits; el
  "Pendiente inmediato" viejo quedó marcado histórico. El informe suelto se reubicó
  a `docs/reportes/2026-07-25-patterns-live-endpoint.md`.
- ~~**media-plane: `docs/implementation-status.md`** desactualizado~~ **CERRADO
  2026-07-29**: fecha, 380→**646 tests** (verificado con collect-only), features de
  julio documentadas y verificadas contra código una por una, `debug_run` quitado,
  tools vigentes confirmadas (`evaluate`, `inspect_runs`, `preannotate_video`,
  `run_node`, `videogt`). `CLAUDE.md` alineado a Python 3.12 (también el del
  workspace).
- ~~**experimental-setup**: README y `docs/prompt-sets.md` desactualizados~~
  **CERRADO 2026-07-29**: README §5 con el catálogo real (5 sets, 3 frozen con acta
  76) y `docs/prompt-sets.md` §4 re-escrito veraz con los 5 sets y fecha.
  `docs/experiments.md` sigue sin cubrir los 10 manifiestos v1 — pendiente menor,
  ligado a la decisión §5 sobre su destino.
- **datasets: licencia de CHV en estado `Parcial`** (sin LICENSE en el ZIP) y aporta
  **1.330/6.477 imgs (20,5%) del bench congelado**; `bench_v3.md` no refleja ese
  estado. Además el vocabulario de `license_registry.md` está roto: define
  `Pendiente/Aprobado/Bloqueado` pero ninguna fila dice `Aprobado`. Resolver la
  verificación o declarar el estrato "uso interno, no redistribuible" en la tesis.
- Menores, estado al 29/07: banner de `00-indice.md` ✅; `CLAUDE.md` Python 3.12 ✅
  (repo y workspace); doc 62 §9 ✅ (banner agregado apuntando a este doc como
  tablero vigente).

## 4. Material de defensa (videos V1–V3, docs 09/50/55/69)

1. **Nadie produce `track_id`** → `granularity: subject` solo vive en fixtures →
   overlays por persona imposibles. Bloquea V1–V3 tal como están concebidos.
2. **El overlay pinta una caja por escena** (deuda de G0, doc 34) → hace falta un
   renderer que consuma `supporting` o modo `subject` (depende del anterior), o
   re-encuadrar V1–V3 a overlay de escena.
3. **V1 sin tildar** en el checklist del doc 69 (línea 678): la toma vistosa de la
   cadena infracción → alerta. Re-toma de una P2 live limpia es opcional (doc 71 §7.2).

## 5. Decisiones abiertas (elegir y documentar, no necesariamente implementar)

| Decisión | Opciones | Ref |
|---|---|---|
| Merge de `perf/producer-pil-roundtrip` | mergear (evidencia p=0,0195, byte-idéntica) / no | doc 73 §10.4 |
| F-RT3 (techo de fps = GIL) | citar diagnóstico / medir two-node en un host / split single-host | doc 73 §6 |
| Fase 2c two-node | no existe compose de dos nodos; ¿entra o se defiende single-host (validado 07-05)? | experiments.md:105 |
| `stopped` limpio ¿consolida? | afecta a los 6 experimentos GDINO/YOLOE | doc 71 §5 |
| Destino de los manifiestos exploratorios | limpiar `rt-01`, `diag_riesgo_activo`, `realt-time-safety_vest` (typo) | doc 71 §5 |
| `replay_dbe_cr01_cr02.yaml` quedó casi duplicada de `replay_cr01_cr02_v2.yaml` tras la migración | ¿archivar una? (revisión adversarial 07-29) | — |
| Banner de deprecación de v1 invisible por API (solo en el YAML; `effective_config` excluye el pattern set) | ¿exponer `description` en summary? Barato, no urgente | — |

## 6. Limitaciones que se DECLARAN, no se arreglan

- **A6 no realizable** con el material actual (videos fuente ya cortados a 12 s) — doc 58.
- **CR-02 sin GT en el bench de imágenes** (`has_vest` no anotado en shel5k; chv sin
  negativos) → el bench de imágenes solo sostiene CR-01; CR-02 se sostiene en video/EBE.
- Caveats por estrato de `bench_v3` (ya escritos y honestos en `bench_v3.md:32-38`):
  bench_obra con pasada visual muestral 36/147; chv dominio mixto + watermark; shel5k
  416×416 + mirror-padding 2–10%. `bare_head` limpio del núcleo: **n=61, no 110**.
  CR-01 violadoras 111 < 150 del mínimo de spec (limitación del dataset, no del pipeline).
- **F-RT4** (biestabilidad 2,6×) sin causa aislada; remedio operativo verificado (doc 74).
  Brecha 187→306 ms sin repartir entre inquilinos (doc 73 §0.6). El camino DBE es inmune.
- GT del banco de video: declarar el protocolo de acuerdo inter-anotador (doc 58 §B.3)
  cuando exista la pasada humana; hasta entonces TODO resultado temporal es preliminar.

## 7. TABLERO RESTANTE (2026-07-29, tras el cierre de §1.4–1.6, §2 completo y §3.3)

**Del usuario:**

| Tarea | Esfuerzo | Nota |
|---|---|---|
| 🔄 Pasada CVAT (en curso) | días | única latencia real; secuencia post-CVAT lista (§1.1) |
| Task 4.3 con el kit (§2.6) | ~15 min | `processed/audit_task43/` + tabla pre-cargada |
| Receta git del **doc 77** | ~30 min | commits + merges a `main` + push rama huérfana + `mati` + bundle docs |
| Licencia CHV (§3.3) | ~30 min | verificar o declarar "uso interno, no redistribuible" |
| Decisiones del §5 | minutos c/u | perf (recomendado mergear), F-RT3, two-node, stopped-consolida, manifiestos, config duplicada, banner v1 por API |

**De Claude (ejecutable ya):**

| Tarea | Nota |
|---|---|
| Clips soak (§1.7) | **coordinar con el usuario** — no tocar `datasets-videos/` mientras el lote CVAT esté abierto |
| `track_id` + overlay (§4) | el único bloque de implementación restante; arranca con brainstorming de alcance |
| `docs/experiments.md` (manifiestos v1) | tras la decisión §5 sobre su destino |

**Con GT humano (el tramo final):** Fase T → P → D → análisis de errores → reporte
de cierre (doc 62 §1–8), consolidando evidencia versionada (§3.2) — **sin escribir
código nuevo**: la maquinaria completa quedó lista y verificada el 29/07.

**Observación menor a vigilar:** la suite frontend mostró 1 archivo rojo en 1 de 4
corridas del 29/07 (no reprodujo; 381/381 verdes en las re-corridas) — flake de
entorno jsdom, sin archivo identificado aún.

Recordatorios operativos al retomar corridas: volver `EOVRT_MODEL_REF` a
`grounding-dino/gdino-tiny-560` (quedó en `yoloe/yoloe-26x`), y el manifiesto que
referencia `a_p1_c01.mp4` apunta a un clip inexistente (la serie arranca en `c02`).
