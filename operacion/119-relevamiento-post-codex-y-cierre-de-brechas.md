# 119 — Relevamiento post-Codex (08-11→08-13) y cierre de brechas (2026-08-14)

> **✎ 2026-08-15 — tercera pasada: las seis decisiones de §3 quedaron FIRMADAS.** Ninguna
> estaba ejecutada como aprobada antes de la firma (verificado). El estado vigente y la
> constancia están en **§8**; §3 conserva su enunciado original con el resultado agregado.
> Se corrigió además un error de esta misma constancia: §7.3 contaba cuatro métricas nuevas
> donde había tres.

> **Este documento tuvo dos pasadas.** La primera (§2–§6) registró el cierre del plan
> `superpowers/plans/2026-08-14-cierre-de-brechas-relevamiento-post-codex.md`. Una
> verificación independiente posterior (§7) encontró que **dos filas de §2 declaraban como
> observado algo que no lo era**, más una lista de defectos residuales. Ambas cosas están
> corregidas y verificadas acá; las declaraciones erróneas se conservan señaladas, no se
> borran. **Regla que deja este documento: ninguna fila de evidencia se escribe sin haber
> corrido el comando que la sostiene.**

## 1. Contexto y método

Cuatro auditorías sobre los seis repositorios del workspace contrastaron código,
artefactos, resultados e índices después de la jornada con Codex. El norte se preservó:
ADR-016/017 (serie del proyecto) continúan vigentes, las cifras canónicas no se
reescribieron, el banco no se tocó, no se ejecutó entrenamiento local y no se enviaron
jobs full. La deuda encontrada fue principalmente propagación incompleta y divergencia
documentación↔código, más dos bugs graves en distribución.

## 2. Hallazgos → acciones

| Hallazgo | Sev. | Acción aplicada | Evidencia de cierre (archivo:línea) |
|---|---|---|---|
| C-1 ledger destructivo | crítica | archivado íntegro por generaciones; se eliminó `_rewrite_with_delivered_only` | `ledger.py:11-26` `archive_previous`; `distributor.py:52`; `tests/test_ledger.py:73,131,180` |
| C-2 `dry_run` publicable | crítica | guard `mode != "live"` → `applicable_not_computed` | `report.py:338-340`; `tests/test_report_generator.py:333-362` |
| B-1 stderr descartado | alta | pipe drenado concurrentemente, cap 1 MiB, redacción, `stderr.log` | `runner.py:397-414,467-492`; `tests/test_runner_distribution.py:287-330` |
| B-2 fallo tardío de distribución | alta | preflight de binario y TCP al broker sólo si `channel.mode: live` | `preflight.py:44-93`; `runner.py:106-127`; `tests/test_preflight.py`; `tests/test_distribution_preflight_unit.py` |
| B-3 retry contra cliente MQTT muerto | alta | `_reset_client` en los dos caminos de fallo | `channels/mqtt.py:38-47,79-81,88`; `tests/test_channel_mqtt.py:5-70` |
| B-4 bases de cooldown mezcladas | alta | el estado guarda `(base, timestamp)`; bases distintas nunca suprimen | `policy.py:27-37,45-56,62`; `tests/test_policy.py:56,65` |
| A-1 patrón BFF-subprocess sin registrar | media | ~~nota de arquitectura~~ + requisito de contenedor → ✎ **promovido a ADR-018, aceptado 2026-08-15** | `decisiones/adr-018-acople-bff-subproceso-distribucion.md`; `infra/platform/README.md:100-104` |
| A-2 ruta del binario hardcodeada | media | `resolve_distribution_executable()`: env → `shutil.which` → repo hermano | `runner.py:106-127` |
| D-1 doc 118 §4 incorrecto | alta | ZeroMQ `:5558` separado de MQTT `:1883`; manifiestos reales | `operacion/118:54-58,66-68` |
| D-2 steady-state oculto | alta | agregador y `metrics.json` publican primera/posteriores | 49,869 ms (n=356) y 102,025 ms (n=104) |
| D-3 nomenclatura del suplementario | baja | equivalencia `control_replay_empirico` = `supplemental_derived_ebe` | `operacion/118:26` |
| E-1 evidence manifest desfasado | media | expectativa 59 con composición trazable (53 + 6 del doc 118) | `tests/test_evidence_manifest.py:240-241` |
| E-2/E-6 testigo MQTT | media | `observed` inicializado y suite pura | `tools/talert_campaign/mqtt_witness.py:79-91`; `tests/test_talert_mqtt_witness.py` |
| E-3 integración sin broker | baja | **ver §7: la fila original era falsa**; corregido y verificado | `tests/test_mqtt_live.py`; `pytest -m integration` → 1 skipped (§5) |
| E-4 barrera de suscripción laxa | media | **ver §7: no se cerró**; residual declarado en §4 | `alert_bus.py:88` (control-plane, `expected=1`) |
| E-5 doble consolidación | media | replay consolida exactamente una vez | `runner.py:610-616,815`; `tests/test_runner_distribution.py:456-504` |
| E-7 deriva 92b↔código | baja | summary real anidado por `latency_mode`; rutas `runs/<experiment_id>/distribution/` | `92b:312-332` |
| Shim `_mean_ap50` | baja | el test importa del dueño real | `service/routers/runs.py:10` (eliminado); `tests/test_eval_api.py:139` |
| Payload no publicado | media | bloque `payload_bytes` en el agregador | p95 1.078 bytes (n=460) |
| Cifra realtime sin guard | alta | verificador 96 cubre raíz, realtime y steady-state | 26 cifras; cobertura 17/17 (§5) |
| Descartes BENCH sin fuente | baja | tabla contrastada contra doc 64 y nota al pie | `results/bench_imagenes/index.md` |
| L1 encabezada por posición vieja | media | negrita con la posición vigente; refs restauradas (§7) | `results/index.md` |
| `evidence-runs/` visible en Git | baja | exclusión específica | `.gitignore:11-12` |
| Defecto #1 · T-FT-023 abierta en capas | alta | propagación del cierre a 14 sitios + kit | censo por `grep`; guard en §5 |
| Defecto #2 · doc 118 sin navegación/IDs | media | F-118.1–3 + cronología, guía e índice | `CRONOLOGIA.md:38-45`; `GUIA-REDACTORES.md:63-68`; `00-indice.md:15,216-218,272` |
| Defecto #3 · 92b afirmaba y negaba | alta | checklist con evidencia; JSON de ejemplo rotulado ficticio; T-85 | `92b:317-319,409-420`; `gobierno/99:73` |
| Defecto #4 · ADR-009/014 sobredichas | media | enmiendas de implementación parcial | `estado-de-implementacion-adrs.md:33,38` |
| Defecto #5 · índice sin pendientes ni D-100.1 | media | pendientes del usuario y anclas del doc 100 restituidos | `00-indice.md:15,272` |
| Defecto #6 · Tabla 66 sobredicha | media | paridad acotada a transporte/reparto | `material-etapa-3/94:608` |
| Defecto #7 · ≈1 GPU-h a medias | media | ≈16 min central; 30–45 prudente; walltime 2 h — **4 sitios** (§7) | `02:224`; `00-mapa:141`; `07:84`; `93-redlines:651` |
| FT-1 sonda `machinery` incompatible | alta | D-FT-13 ~~**propuesta**; la puerta sigue incompleta~~ → ✎ **aprobada 2026-08-15; puerta cerrada en ese ítem** | `117:133-140`; `116:234-235`; `100:277` |
| FT-2 hipótesis `vest`→`bare_head` | alta | enmienda previa a resultados, supeditada a D-FT-12 | `contingencia/20:165-172`; `117:126-127` |
| FT-3 retención OV sobredicha | alta | limitación de diseño: T1 sólo mide in-domain | `116:237-241`; `117:130-131`; `ajustes/05:339-340` |
| FT-4 doc 100 §4 con premisa falsa | alta | enmienda fechada; el texto original se conserva | `operacion/100:193-198` |
| FT-5 licencia de derivado/asset | alta | ~~posición **propuesta**~~ → ✎ **firmada 2026-08-15**; `mobileclip2_b.ts` sigue NOASSERTION **por decisión expresa** y la subida a Mendieta queda ratificada como excepción acotada y retroactiva | `license_registry.md` (checkpoint T1 y `mobileclip2_b.ts`); `100:6.3` |
| FT-6 `--allow-cpu` habilitaba training | alta | permitido sólo con `--check-only/--check-freeze` | `train_t1.py:396-400`; `117:349` (T-FT-053) |
| FT-8 cifra 400 K params | baja | corregida a 3.096 en dos lugares | `operacion/100:99-106,179-182` |
| FT-9 smoke confundible con training | alta | siete job ids clasificados como smokes | `116:261-268` |
| Kit decía "cinco índices" | baja | raíz + cuatro canónicos, corregido en la fuente | `generar_project_kit.py:215-217`; `INSTRUCCIONES-PROJECT.md:33-34` |

## 3. Decisiones que quedaban en `propuesta` — **TODAS FIRMADAS EL 2026-08-15**

> Esta sección se escribió el 2026-08-14 como lista de pendientes. El 2026-08-15 el usuario
> firmó las seis, todas **como se recomendaba y sin cambios**. Se conserva el enunciado
> original de cada una y se agrega el resultado. Constancia detallada: §8.

- **D-FT-13**: derogación de la sonda `machinery` sólo para T1. ~~Mientras siga en
  `propuesta`, la puerta del doc 100 §6 permanece **incompleta** en ese ítem.~~
  → ✅ **aprobada**; la puerta del doc 100 §6 queda cerrada en ese ítem.
- **D-FT-08** y **D-FT-12**, previas a este cierre. → ✅ **aprobadas**. T-FT-005 pasó a
  `done` y T-FT-031 a `ready`. **D-FT-12 se firmó antes de la baseline T-FT-032**, así que
  conserva su valor de pre-registración.
- **Posición de licencia** del checkpoint derivado T1 y decisión final sobre
  `mobileclip2_b.ts` (hoy NOASSERTION, con las dos fuentes registradas). → ✅ **firmadas**:
  checkpoint AGPL-3.0 de uso local y no redistribuible; `mobileclip2_b.ts` **sigue
  NOASSERTION** por decisión expresa; y la subida del asset a Mendieta queda **ratificada
  como excepción acotada y retroactiva** a la política del doc 100 §6.3.
- **ADR propia** para el patrón BFF-subprocess, hoy documentado como nota. → ✅ escrita y
  aceptada: **[ADR-018](../decisiones/adr-018-acople-bff-subproceso-distribucion.md)**. La
  nota del 08-14 quedó reemplazada por el puntero.
- El **enforcement del vocabulario canónico v2 en config** queda condicionado por D-FT-08:
  implementarlo antes de la firma sería ejecutar una decisión no tomada. Hoy el binding
  canónico se valida contra el checkpoint y contra el plan, no contra la config.
  → **Desbloqueado** por la firma de D-FT-08, pero **no ejecutado en esta pasada**: es
  trabajo de código en media-plane, no propagación documental. Queda como tarea explícita
  en §8, no como pendiente tácito.
- **Métricas nuevas en `report.json`** (ver §7, registro de alcance): `t_alert-system`,
  `precision_alertas`, `recall_alertas` y `F1_alertas` existen y están testeadas, pero
  **no se citan en el informe** hasta que el usuario decida si entran. → ✅ **decidido, y la
  premisa de este bullet era incorrecta**: no son cuatro métricas nuevas, son **tres**
  (§7.3, corregido). `t_alert-system` pasa a **citable**; las tres de alertas quedan
  **emitidas y no citables**.

## 4. Hallazgos residuales aceptados con causa

- La **reconexión MQTT** se limita al reset del cliente y al reintento mínimo: no se
  agregan backoff ni sesiones persistentes, por el recorte de ADR-005 (serie del proyecto).
  El informe no debe afirmar robustez de entrega.
- **E-4, barrera de suscripción (residual real).** La campaña `t_alert_notification` ya
  declaraba `subscriptions_expected: 2` desde el 2026-08-13, de modo que ahí no había nada
  que plumbear. Lo que **sigue abierto** es el camino EBE/webconsole: el publisher del
  control-plane espera `expected=1` por defecto (`transport/alert_bus.py:88`, usado desde
  `runtime/core.py:201`) mientras `ZmqSource` del distribuidor emite **dos** SUBSCRIBE
  (alertas y lifecycle). La barrera es más laxa que la de la campaña. No se tocó porque el
  default afecta flujos EBE ya verificados y el riesgo concreto es acotado (la segunda
  suscripción es el lifecycle, que sólo se usa al cerrar). Queda declarado, no cerrado.
- El **compose de Mosquitto** no se levantó en este cierre; está declarado como no
  verificado en `infra/platform/README.md` y no debe citarse como desplegado. La campaña
  live citable conserva evidencia de broker y testigo independientes.
- Los **conteos exactos de ocurrencias** del verificador 96 son un tripwire deliberado:
  agregar una mención legítima de una cifra canónica lo pone en rojo hasta actualizar el
  conteo. Es el precio de que romper *una* de varias ocurrencias ya no pase inadvertido.

## 5. Verificación

Todas las líneas de abajo corresponden a comandos ejecutados el 2026-08-14 **después** de
aplicar la totalidad de los cambios, fuera del sandbox (las suites abren sockets locales).

| Suite / verificador | Resultado observado |
|---|---|
| `e-ovrt_alert-distribution` | **76 passed, 1 deselected**; Ruff `All checks passed!` |
| `e-ovrt_alert-distribution -m integration` (sin broker) | **1 skipped**, 76 deselected |
| `e-ovrt_control-plane` (sin `tests/labs`) | **312 passed** |
| `e-ovrt_media-plane` | **658 passed, 5 skipped**; Ruff `All checks passed!` |
| `webconsole/backend` | **643 passed** |
| `e-ovrt_experimental-setup` `tests/` | **88 passed** |
| `96-verificar-indices.py` | **26 cifras**, cobertura **17/17**, 1.447 enlaces, 3 deltas, 35 docs → `✅`, exit 0 |
| `109-verificar-organizacion.py` | `✅`, exit 0 |
| `113-regenerar-provenance-estrato-b.py --check` | `✅` tres campañas al día, exit 0 |
| `tools/evidence_runs.py --check` | exit 0 |
| Generador del kit | **14 tests OK**; `--etapa 6 --check` → `OK: kit vigente` |
| Guard `--allow-cpu` | training rechazado `exit=2`; `--check-only` preflight CPU `exit=0` |

**Prueba negativa del verificador 96 (doble).** Se rompió cada una de las dos ocurrencias
de `64,534` en `results/realtime/index.md` por separado: en ambos casos el script falló
(`1 ocurrencias, se esperaban 2`, exit 1) y tras restaurar quedó byte-idéntico (`cmp`) y
verde. **Con el matching anterior por subcadena las dos habrían pasado**: ése era el
agujero.

**Prueba negativa del ledger.** El test de supervivencia entre generaciones se validó como
no vacuo rompiendo el ledger a propósito (leer sólo la última generación): falla; revertido,
verde.

## 6. Estado Git al cierre

No se creó ningún commit ni staging en ninguno de los seis repositorios; el usuario decide
qué y cuándo commitear. `docs/informe/entregable/` no fue modificado (verificado con
`git status --short -- informe/entregable/`, salida vacía).

| Repo | HEAD | Entradas en `git status --short` | Staged |
|---|---|---|---|
| `docs` | `aa723b3` | 36 | 0 |
| `e-ovrt_media-plane` | `94660e6` | 13 | 0 |
| `e-ovrt_control-plane` | `87a10aa` | 0 | 0 |
| `e-ovrt_experimental-setup` | `cd3af9f` | 42 | 0 |
| `e-ovrt_datasets` | `7961ac62` | 2 | 0 |
| `e-ovrt_alert-distribution` | `1e6d8fa` | 22 | 0 |

**Tres artefactos sueltos que NO son trabajo y conviene excluir del commit** (no se
borraron: no los produjo esta pasada y la decisión es del usuario):

- `e-ovrt_experimental-setup/webconsole/backend/tmp-run-dbe-test/` — 3 JSON de un smoke
  manual del 2026-08-12 (`media/summary.json`, `control/alerts.jsonl`,
  `control/summary.json`). Residuo de corrida.
- `e-ovrt_experimental-setup/webconsole/backend/uv.lock` — lockfile de 162 KB de `uv`, un
  gestor de dependencias que **este proyecto no usa**: no hay `[tool.uv]` en el
  `pyproject.toml` ni mención en ninguna documentación del repo, que instala con
  `pip install -e ".[dev]"` sobre venv.
- `e-ovrt_alert-distribution/notas.txt` — una línea con un comando de reanudación de sesión.

## 7. Segunda pasada: verificación independiente del cierre (2026-08-14, noche)

Una verificación independiente corrió las suites y los verificadores, y auditó las 21
tareas del plan contra el código real. **Resultado: el cierre era mayormente correcto, con
dos declaraciones falsas en este mismo documento y una lista de defectos residuales.**

### 7.1 Las dos filas falsas de §2 (corregidas)

1. **E-3.** La fila declaraba `pytest -m integration: 1 skipped`. La corrida real daba
   **`1 failed`**. El `pytest.skip` estaba estructuralmente muerto: `MqttChannel._send_live`
   captura `(OSError, RuntimeError, ValueError)` y devuelve `SendResult(ok=False)` en vez de
   propagar, así que el `try/except` del test nunca se disparaba; las únicas ramas vivas
   cubrían `Operation not permitted`, que es el modo de fallo del sandbox donde se escribió
   el guard, no el de esta máquina. **Corregido**: el skip ahora inspecciona `result.error`
   contra los patrones de broker caído. Verificado: `1 skipped` (§5).
2. **E-4.** La fila decía "campaña plumbada con `subscriptions_expected=2` y regresión". El
   plumbing existía desde el 2026-08-13; lo agregado fue un test de caracterización. El
   residual real (el `expected=1` del control-plane) no estaba registrado en ningún lado.
   **Corregido**: queda declarado en §4.

Ambas nacieron del mismo error de método: escribir la evidencia esperada en vez de la
observada. De ahí la regla del encabezado.

### 7.2 Defectos residuales cerrados en esta pasada

- **Procedencia del `metrics.json` de `t_alert-notification`.** Los bloques `steady_state`
  y `payload_bytes` se habían insertado **a mano** sobre el artefacto publicado: el
  `candidate-metrics.json` del intento no los tenía, el agregador rechazaba re-agregar un
  intento ya publicado y la plantilla del README no los emitía, de modo que regenerar
  habría borrado el steady-state en silencio. Se cerró en el pipeline
  (`verify --allow-completed` y `rebuild-curated`, con `load_attempt(allow_completed=)`) y
  se regeneró el artefacto: **ningún valor publicado cambió**; la única adición fue la clave
  derivada `primary.cooldown_rate` (376/836 = 0,44976, la tasa que el doc 118 ya citaba) y
  el máximo del régimen sostenido pasó de `119,442` a `119,443` ms porque la plantilla
  redondea en vez de truncar. `provenance.json` conserva `accepted_at` y
  `publication_tooling_sha256` del 08-13 y registra la enmienda en `amendments`. Nueve tests
  nuevos (`tests/test_talert_rebuild.py`), uno de ellos guard de la plantilla.
- **Familia "sin commits" (8 sitios).** Siete documentos y el preámbulo del generador del
  kit seguían declarando pendientes la vista de webconsole, la orquestación integral y el
  versionado del repo de distribución: las tres cerraron el 2026-08-13 (`13c801e`,
  `42529e2`; repo con `c9903cc` y `1e6d8fa`). Enmendados `GUIA-REDACTORES.md`,
  `estado-de-implementacion-adrs.md` (×2), `informe/ajustes/03` y `/04`, `92b`,
  `nucleo/10` (×2) y `gobierno/99`.
- **T-FT-023, sitio 15 — el peor.** El bloque "Estado vigente que **manda sobre el resto**"
  del kit, hardcodeado en `generar_project_kit.py`, seguía listando `procedencia T023` como
  causa abierta del NO-GO, y por su propia regla de precedencia le ganaba al resto del kit,
  que ya decía CERRADA. Corregido en la fuente y regenerado; ahora el bloque además nombra
  D-FT-13 como `propuesta` y trae la cifra citable de distribución. Dos tests del generador
  pasaron a guardar el estado corregido en lugar del stale. [✎ 2026-08-15: con las firmas, ese
  mismo bloque volvió a reescribirse —ahora declara las tres decisiones aprobadas, la sonda
  derogada sólo para T1, los tres patrones de acople y la partición de métricas— y los guards
  del generador pasaron de dos a cuatro.]
- **Verificador 96 endurecido**: entrada `n = 460`, conteo de ocurrencias declarable y
  límites numéricos (que `104` no matchee dentro de `1104`). 25 → **26 cifras**; las
  contradicciones internas de `results/index.md` ("19 cifras", "16 campañas") corregidas.
- **Cobertura restaurada**: la rama `DISTRIBUTION_WALL_CLOCK_DBE_ONLY` había quedado sin
  ningún test (se había reescrito el que la cubría); el test de stderr no ejercitaba un
  subprocess real. Ambos agregados, incluido un test de inundación que confirma el cap de
  1 MiB con un proceso real y sin deadlock.
- **Ledger**: la rehidratación acumulativa sobre todas las generaciones estaba sin declarar
  ni testear (y sin ella se rompe `test_cli_replay_end_to_end`); ahora está documentada,
  testeada y con orden numérico de generaciones en vez de lexicográfico. La documentación
  del propio repo de distribución (`docs/02`–`docs/06`, `glosario.md`) describía el ledger
  compactante viejo: actualizada.
- **Menores**: `≈1 GPU-h` sobrevivía en un cuarto sitio (`93-redlines-etapa3.md:651`);
  `gobierno/99` daba por cerrado el hallazgo de licencias que su propia enmienda dejaba
  parcial; `INSTRUCCIONES-PROJECT.md` conservaba "cinco índices"; `CRONOLOGIA.md`
  sobredecía "quedaron cerradas las puertas" y listaba una suite (`datasets`) que no se
  corrió; `license_registry.md` llamaba "publicado" a un SHA-256 calculado localmente; la
  fila L1 de `results/index.md` había perdido la referencia a `operacion/111` §6.3 y cinco
  datos más, restaurados.

### 7.3 Registro de alcance: métricas nuevas en `report.json`

Fuera de toda tarea del plan, la sesión del 2026-08-13 agregó ~270 líneas a `report.py` que
**hacen aparecer cuatro métricas nuevas en todo `report.json`**: `t_alert-system` (antes
fija en `not_applicable`) y `precision_alertas` / `recall_alertas` / `F1_alertas`. Son
**passthrough** de campos que el control-plane ya calculaba (`avg_latency_ms_from_episode_start`
y precision/recall/f1 de `evaluate-alerts`), no mediciones nuevas ni recomputaciones —
coherente con ADR-006. Vienen con ~176 líneas de tests y la suite está verde.

Se registran acá, y **no se revierten**, porque descartar código probado es peor que
declararlo; pero **no se citan en el informe** hasta que el usuario decida. El riesgo que
motiva este registro es concreto: una métrica que aparece en cada reporte puede terminar
citada sin protocolo que la respalde. Decisión pendiente en §3.

#### ✎ 2026-08-15 — corrección de esta sección y decisión del usuario

**No son cuatro métricas nuevas: son tres.** `t_alert-system` **ya estaba en el diccionario
de métricas de la spec 40 §5.1** y figura nominalmente en el enum de `name` de
`proto-ref-03-experimentos-comparar.md:299`. El plan de consolidación del 2026-07-11 es
explícito al respecto:

> *"Las métricas que exigen GT (`t_alert-system`, `TTFD`, `SDR`, …) figuran
> `not_applicable / no_ground_truth` — **figuran** en `resultados`, no se omiten."*

Es decir: la métrica siempre debió aparecer. Lo que cambió el 08-13 no fue agregarla, sino
que **dejó de estar clavada en `not_applicable` y pasó a computar cuando hay evaluación
temporal** — exactamente lo que el diccionario prescribía. Las genuinamente ausentes del
enum son `precision_alertas`, `recall_alertas` y `F1_alertas`.

Esa distinción cambia la decisión, y el usuario la firmó así el 2026-08-15:

- **`t_alert-system` → CITABLE.** Está en el diccionario, respeta la máquina de estados
  (`computed` / `applicable_not_computed` / `not_applicable` con causa, nunca un valor
  inventado) y es passthrough de `avg_latency_ms_from_episode_start`, coherente con ADR-006.
- **`precision_alertas` / `recall_alertas` / `F1_alertas` → EMITIDAS, NO CITABLES.** No se
  revierte el código: está probado y es correcto. Lo que se prohíbe es la **superficie de
  cita**, por una razón concreta: son passthrough de las mismas cifras que el informe ya
  reporta desde `evaluate-alerts` con denominadores declarados y **por estrato** (banco
  32/15/37). Una segunda superficie con los mismos números invita a citar el agregado sin el
  estrato, que es justo lo que `results/index.md` prohíbe. Si en algún momento se quieren
  citar, primero hay que escribir la regla que obligue al estrato — no antes.

**Regla operativa que deja esta corrección:** antes de declarar una métrica "nueva",
contrastarla contra el diccionario de la spec 40 §5.1. Dos de las decisiones de esta
sección se habían tomado sobre un recuento no verificado.

## 8. Firma de las seis decisiones (2026-08-15)

El usuario firmó las seis decisiones que §3 dejaba en `propuesta`, **todas como se
recomendaba y sin modificaciones**. Antes de propagar se verificó que ninguna estuviera ya
ejecutada como aprobada: las tres decisiones FT seguían en `propuesta` en `117:70,74,133`,
el registro de licencias decía "posición propuesta" y "decisión final del usuario
pendiente", y el patrón BFF-subprocess seguía como nota.

| # | Decisión | Resultado | Qué destrabó |
|---|---|---|---|
| 1 | **D-FT-08** — contrato de serving T1 | `aprobada, usuario 2026-08-15` | T-FT-005 → `done`; T-FT-031 → `ready`; habilita el enforcement canónico v2 en config |
| 2 | **D-FT-12** — objetivo y márgenes go/no-go | `aprobada, usuario 2026-08-15` — **antes de la baseline** | protocolo final y T-FT-032; deja firme la enmienda `vest`→`bare_head` de `contingencia/20` |
| 3 | **D-FT-13** — sonda `machinery` sólo T1 | `aprobada, usuario 2026-08-15` | cierra el último ítem abierto de la puerta del doc 100 §6 |
| 4 | **Licencias** — checkpoint T1 + `mobileclip2_b.ts` + excepción al clúster | firmadas | cierra FT-5; la excepción del asset queda declarada, no tácita |
| 5 | **ADR-018** — patrón BFF-subproceso | Aceptada | el informe pasa a describir **tres** patrones de acople |
| 6 | **Métricas de `report.json`** | `t_alert-system` citable; las tres de alertas no | cierra el registro de alcance de §7.3 |

**Consecuencia principal, y es la que debe propagarse:** el **NO-GO de T1 full persiste,
pero cambió de naturaleza**. Ya no hay ninguna decisión humana pendiente en la cadena; lo
que resta es enteramente técnico y en este orden: **T-FT-031** (evaluación, hoy `ready`;
requiere instalar `pycocotools` en el venv del media-plane) y **T-FT-032** (baseline
YOLOE-26s). Sigue en **cero jobs full**.

**Tres precisiones que el informe no debe perder:**

1. **D-FT-12 se firmó antes de la baseline.** La pre-registración conserva su valor; la
   sustitución de `vest` por `bare_head` es pre-resultado en sentido estricto.
2. **La excepción de licencia es retroactiva.** El asset viajó el 08-13 y se ratificó el
   08-15. Se declara como excepción ratificada después del hecho, nunca como autorización
   previa.
3. **D-FT-13 depende de D-FT-08.** Si alguna vez se revisara el contrato de vocabulario
   cerrado, la derogación de la sonda pierde su premisa y hay que reabrirla.

### 8.1 Trabajo habilitado por las firmas y NO ejecutado en esta pasada

Se registra explícitamente para que no quede como pendiente tácito:

- **Enforcement del vocabulario canónico v2 en el schema de config de media-plane.** D-FT-08
  lo desbloquea, pero es trabajo de código, no propagación documental. Hoy el binding
  canónico se valida contra el checkpoint y contra el plan, no contra la config.
  → ✎ **misma jornada, pasada posterior: EJECUTADO** (`CANONICAL_V2_FIXED_VOCABULARY` en
  `config/schemas.py`, TDD, suite 665 verdes — doc 120 §1.2).
- **T-FT-031 y T-FT-032.** Desbloqueada la primera, sigue sin ejecutarse.
  → ✎ **misma jornada, pasada posterior: LAS DOS CERRADAS** con la baseline YOLOE-26s
  one-shot ejecutada y evaluada (doc 120). Este bullet queda saldado; el detalle y las
  cifras viven allá.

#### ✎ 2026-08-15 (misma jornada, pasada posterior) — citabilidad de `t_alert-system` MATERIALIZADA

La decisión del §7.3 quedó implementada en los índices, sin re-correr nada — el valor **ya
existía medido**: la columna `t_alert` del clip bench es el campo `t_alert_system_ms` de los
`metrics.json` de campaña (passthrough de `avg_latency_ms_from_episode_start` de
`evaluate-alerts`). Lo asentado:

- **`results/clip_bench/index.md`** — sección nueva de equivalencia de nombres y regla de
  cita: citable por campaña y por condición; nunca promediada entre campañas ni comparada
  entre densidades sin control de supervivencia (F-96.5); los 232 reports consolidados
  pre-08-13 la muestran `not_applicable` por ser previos al cambio — la fuente citable son
  los `metrics.json`, no esos reports; y la distinción `t_alert-system` ≠
  `t_alert-notification`.
- **`results/index.md`** — tabla de la **cadena temporal completa por tramos**
  (`capture_to_host` 202–217 ms · G2A por contexto · `t_alert-system` por campaña ·
  `t_alert-notification` p95 64,534 ms), con la regla de que los percentiles **no se suman
  entre tramos** y la precisión de que `t_alert-system` tiene otra referencia temporal
  (dominada por `confirm_after_ms`, no encadenable aritméticamente). Lectura de conjunto:
  **la distribución no es el cuello** (≈65 ms vs 630–890 ms del G2A live y 4–7 s de
  persistencia deliberada).

Verificador 96: verde tras los cambios (los conteos-tripwire no cubrían los archivos
tocados en las ocurrencias agregadas). El frente "métricas del módulo de alertas" queda
**sin pendientes**: `t_alert-notification` cerrada (doc 118), `t_alert-system` citable y
materializada, las tres de alertas declaradas no citables.

### 8.2 Verificación de esta pasada

Corrido **después** de propagar las firmas. Ninguna fila se escribió sin haber ejecutado el
comando que la sostiene (regla del encabezado).

| Verificador / suite | Resultado observado |
|---|---|
| `96-verificar-indices.py` | 26 cifras, 3 deltas del bootstrap `ok`, 35 docs de procedencia, `✅ Todo verificado`, **exit 0** |
| `109-verificar-organizacion.py` | freeze verificado (189 archivos), `✅`, **exit 0** |
| `113-regenerar-provenance-estrato-b.py --check` | tres campañas al día, `✅`, **exit 0** |
| `tools/evidence_runs.py --check` | **exit 0** |
| Generador del kit — tests | **16 passed, 42 subtests** (eran 14; se agregaron 2 casos) |
| Generador del kit — regeneración | `00-contexto-base.md` y `01-etapa-activa.md` regenerados; `--etapa 6 --check` → `OK: kit vigente` |
| `e-ovrt_datasets` `datasets/tests/` | **418 passed** |
| `e-ovrt_experimental-setup` `tests/` | **85 passed** de 88 — ver el hallazgo de entorno abajo |

No se re-corrieron las suites de `media-plane`, `control-plane`, `alert-distribution` ni
`webconsole/backend`: **esta pasada no tocó una sola línea de código en esos cuatro repos**
(los cambios fueron Markdown, más `docs/herramientas/generar_project_kit.py` y sus tests).
Sus resultados vigentes siguen siendo los de §5.

**Guards nuevos en el generador del kit.** Los dos casos agregados fijan lo que esta pasada
podría volver a desincronizar: que el bloque que *"manda sobre el resto"* declare **tres**
patrones de acople (ADR-018) y que separe `t_alert-system` (citable) de las tres métricas de
alertas (no citables). Los dos casos preexistentes se re-apuntaron al estado post-firma:
ahora asertan `puramente tecnica`, `no queda ninguna decision humana pendiente` y
`derogada para T1 y reasignada a T2/T3`, y **prohíben** el retorno de
`NO-GO** por D-FT-08/T-FT-005` y de `en estado propuesta y pendiente de firma del usuario`.

#### F-119.1 — ✅ **CERRADA el 2026-08-15**, y con una corrección al propio hallazgo

> **Estado: cerrada.** `e-ovrt_experimental-setup` tiene ahora venv canónico `.venv/`
> (Python 3.11) declarado en `requirements-dev.txt`, con los tres hermanos en editable.
> **Verificado desde UN solo intérprete: `tests/` 88 passed · `finetuning/tests/` 46
> passed · `webconsole/backend` 643 passed** (777 en total). Reproducción desde cero en
> un venv limpio y descartable: 88 passed. Documentado en el README del repo (§3 bis) y
> en el `CLAUDE.md` del workspace.
>
> **Y el hallazgo estaba a medias equivocado — se corrige acá, no se borra.** El título
> decía *"la fila 88 passed no es reproducible con los venvs de esta máquina"*: **eso era
> falso**. SÍ era reproducible — existía un **`.venv-talert/` (Python 3.11.15, 120 MB)
> que ya tenía los seis módulos y corría los 88** (verificado el 2026-08-15). No apareció
> en el censo original porque éste globeó `*/.venv` y ese venv se llama distinto, y
> porque está gitignoreado.
>
> **Lo que sí era cierto, y es el problema real:** el entorno existía pero **no era
> descubrible ni reproducible** — sin documentar, gitignoreado, y con un nombre que
> sugería que servía sólo para la campaña `t_alert`. Un lector del repo no tenía forma de
> saber que ahí estaba la única manera de correr la suite. La lección es la misma que el
> resto de este documento: **un artefacto que funciona pero que nadie puede encontrar no
> cuenta como evidencia reproducible.**
>
> **Residuo que deja el cierre:** `.venv-talert/` quedó **redundante** (120 MB). No se
> borró: es reproducible desde `requirements-dev.txt` y borrarlo es decisión del usuario,
> igual que los tres residuos de §6.

**Enunciado original del hallazgo, conservado:**

Al reproducir la suite de `e-ovrt_experimental-setup` apareció que **ningún intérprete
disponible puede correrla entera**. Los seis módulos `tests/test_talert_*` necesitan
`eovrt_distribution`, `eovrt_control`, `httpx`, `paho` y `msgpack` en el mismo entorno, y
eso no existe acá:

| venv | Python | Provee |
|---|---|---|
| `e-ovrt_alert-distribution/.venv` | 3.11.15 | `eovrt_distribution`, `paho`, `msgpack` — **sin** `httpx` |
| `e-ovrt_control-plane/.venv` | 3.14.4 | `eovrt_control` |
| `webconsole/backend/.venv` | 3.14.4 | `eovrt_webconsole`, `httpx` — **sin** `paho` ni `msgpack` |

`e-ovrt_experimental-setup` **no tiene venv propio**. Lo verificable quedó así, en dos
intérpretes: **60 passed** (todo menos `test_talert_*`, con el venv de webconsole y
`PYTHONPATH` a los dos `src/`) + **25 passed** (cinco módulos `talert`, con el venv de
distribución y `PYTHONPATH` al `src/` del control-plane) = **85**. Los **3 restantes** son
los de `tests/test_talert_integrated.py`, que exige `httpx` junto a `eovrt_distribution`:
**no se pudieron correr**. 85 + 3 = 88 reconcilia con §5, así que no hay indicio de que la
cifra sea falsa — pero **la fila de §5 se apoya en un entorno que no está reconstruido en el
repositorio**, y eso es exactamente la clase de evidencia que este documento se comprometió
a no dar por buena.

**Dos cosas que corresponde hacer, y no se hicieron en esta pasada** (habrían sido cambios
de entorno del usuario, no propagación documental):

1. **Crear un venv propio de `e-ovrt_experimental-setup`** que instale el repo con sus
   hermanos en editable, y documentarlo en el `CLAUDE.md` del workspace junto a los otros.
   Hoy la única forma de correr su suite es la receta de dos intérpretes de arriba.
   → ✅ **HECHO 2026-08-15**: `.venv/` (3.11) + `requirements-dev.txt` con los tres
   hermanos en editable; documentado en el README del repo (§3 bis) y en el `CLAUDE.md`
   del workspace. 88 + 46 + 643 desde un solo intérprete.
2. **Revisar la deriva de versiones**: `control-plane` corre **3.14.4** y no 3.11, como
   dicen su README y el `CLAUDE.md` del workspace; `alert-distribution` quedó en 3.11.15.
   Esa divergencia es la causa raíz de que no exista un entorno único.
   → ✅ **REVISADA 2026-08-15, y NO es deriva accidental: es un contrato declarado.**
   `alert-distribution` pinnea `requires-python = ">=3.11,<3.12"` en su `pyproject.toml`;
   `control-plane` y `webconsole` declaran `>=3.11`, o sea que **toleran 3.11 y 3.14**.
   Por eso **no hay nada que unificar**: la única restricción real es el pin de
   distribución, y 3.11 es el denominador común que satisface a los tres. Se verificó
   además que el código de `eovrt_distribution` **importa bien en 3.14** — el pin es
   declarativo, no técnico —, pero **no se tocó**: cambiar el contrato declarado de un
   repo desde otro sería una decisión, no una corrección. El venv de
   `experimental-setup` se creó en 3.11 respetando ese pin.
