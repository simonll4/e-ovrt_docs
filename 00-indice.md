# Índice de lectura — Documentación de la plataforma E-OVRT-VDP

- **Última actualización:** 2026-07-11
- **Propósito:** guía de lectura ordenada del set de documentos generados durante el
  relevamiento del control-plane, la revisión de Etapa 3 y la definición del norte
  hacia la defensa (~fines de septiembre 2026).

> ✅ **`docs/` es un repo git propio desde 2026-07-09** (hueco H10 resuelto, opción (a),
> a pedido explícito del usuario; baseline `571652c`). Sigue rigiendo la regla del
> workspace: **no commitear salvo pedido explícito en ese turno** (`CLAUDE.md`
> §"Git conventions"). **Sin remote por decisión del usuario (2026-07-09): todo
> local, no se crea nada en GitHub.** Si se quiere redundancia, copia manual del
> directorio a otro disco.
> El `.git/` cascarón de la raíz de `projects/` sigue existiendo; es inofensivo
> (el repo real de `docs/` tiene precedencia), pero no versiona nada del workspace.

## Cómo está organizado

El **número del documento es su identidad** y no cambia: en todo el set se referencian
entre sí como "doc 04", "doc 07", etc. Las carpetas agrupan por **rol**, no por tema:

| Carpeta | Qué contiene | Estabilidad |
|---|---|---|
| `informe/` | **El TFG en sí** (`.docx`) y su texto extraído (serie 90-). Es nuestro entregable, no una fuente externa. | Viva — se reescribe al final |
| `nucleo/` | 01–11. La narrativa principal, en orden de lectura. | Viva — se corrige y amplía |
| `decisiones/` | ADR-001…014. Las decisiones formalizadas (D1–D6 + 1:1, servicio, config/gestión, secuenciación, frontera de alertas, memoria G0, temporalidad de fuente, layout de artefactos por experimento). **Un ADR solo se revisa con causa registrada** (p. ej. el experimento D1). | Cerrada — se agrega, no se re-litiga |
| `specs/` | Serie 40-. Specs de Etapa 4 por módulo, escritos **sin alternativas** a partir de los ADRs. | **Serie completa escrita (2026-07-09)**; 43 diferido en ejecución (ADR-010) |
| `contingencia/` | Serie 20-. Trabajo **fuera del plan**, por si sobra tiempo. No reabre exclusiones. | Congelada salvo que se active |
| `operacion/` | Serie 30- (llena: 30–39; **continúa en la serie 50-**, porque la 40- pertenece a `specs/`). Runbooks, mediciones y handoffs sobre el host local. `operacion/datos/` guarda evidencia cruda (JSON, scripts). | Viva — se re-mide |
| `herramientas/` | Diseño y plan de utilidades del entorno de desarrollo. No es documentación de la plataforma. | Independiente |

**Cómo se relacionan `informe/` y `nucleo/`.** No hay una carpeta que sea "la verdad" y
otra que la comente. El informe **está en desarrollo** y el núcleo lo critica y lo corrige
a la luz de la implementación y los experimentos (doc 02 revisa Etapa 3; doc 08 se alinea
con §17.1 y lista las desalineaciones a arreglar **en ambos lados**). El propio doc 08 lo
dice: *el informe no es fuente de verdad cerrada, pero es el protocolo contra el que la
plataforma y nuestros documentos deben leerse.* El flujo es bidireccional:

```
   informe/  ──"protocolo, definiciones, metodología"──►  nucleo/
        ▲                                                    │
        └──"redlines, erratas, resultados, decisiones"───────┘
              (se aplican casi al final del proyecto)
```

Corolario práctico: **una crítica del núcleo no se pierde**, se agenda como redline sobre
el `.docx`. Y un cambio del informe puede invalidar un doc del núcleo. Ninguno manda solo.

> Recordatorio: **`docs/` es un repo git propio (local, sin remote) desde 2026-07-09** —
> ver el aviso al principio de este índice; el hueco H10 de
> `nucleo/07-auditoria-decisiones-y-huecos.md` quedó resuelto con eso.

## Orden de lectura recomendado

### `nucleo/` — la narrativa principal

| # | Documento | Qué responde | Tipo |
|---|---|---|---|
| 01 | `nucleo/01-relevamiento-control-plane.md` | ¿Qué es y cómo funciona el repo `e-ovrt_control-plane`? Arquitectura, contratos, motor de patrones, punto débil de identidad. **§12: actualización 2026-07-09 con la rama `mati`** (motor mejorado: matching 1:1, pose, cooldown; paquete `eovrt_labs` con generador + tracker IoU + backend supervisado yolo-ppe; **§12.3: toolchain de calibración y los dos experimentos reales ya corridos** — video Intel 06-26 y video5+gdino 07-07). | Relevamiento |
| 02 | `nucleo/02-revision-critica-etapa3-y-norte.md` | ¿Qué dice la Etapa 3 del TFG, qué está bien, qué falta decidir, y cuál es el norte? Estado real vs backlog, recorte must/won't, 4 resultados defendibles (R1–R4), plan de 12 semanas. | Crítica + plan |
| 03 | `nucleo/03-spec-plataforma-dos-caminos.md` | ¿En qué difiere exactamente "lo implementado" de "lo que plantea el doc" y cómo se decide cada punto? Las 6 dimensiones (D1–D6), tablero de decisiones vivo, secuencia de inclinación de la implementación. **Documento rector.** | Spec integrador |
| 04 | `nucleo/04-diseno-comparativo-estrategias-edir-eind.md` | ¿Cómo se decide D1 (la única dimensión empírica)? Desarrollo documental de E-IND, E-DIR (neg/obs) y E-HYB; protocolo pre-registrado en 2 fases con gates y criterios fijados antes de correr. | Pre-registro experimental |
| 05 | `nucleo/05-integracion-media-control-bus-eventos.md` | ¿Cómo se conectan los planos con un bus de eventos (D3)? Costuras en cada repo, envelope, ZeroMQ vs broker, fases A/B/C. | Diseño técnico |
| 06 | `nucleo/06-diseno-distribucion-alertas.md` | ¿Cómo se distribuyen las alertas confirmadas (D5)? Diseño completo del 2026-07-04 — **se implementa recortado** según D5 del doc 03 (canal MQTT + ledger; dashboard absorbido por la webconsole). | Diseño técnico (pre-existente, a recortar) |
| 07 | `nucleo/07-auditoria-decisiones-y-huecos.md` | ¿Qué puede estar mal en todo lo anterior? Crítica decisión por decisión (D1–D6 + decisiones implícitas), huecos detectados con su corrección, y contingencias. | Auditoría |
| 08 | `nucleo/08-alineacion-consolidacion-metodologica.md` | ¿Cómo se alinea todo el set con la Consolidación Metodológica del informe (§17.1)? Validaciones textuales (D1 mandado por el protocolo de prompts, G0, clip bench=EBE oficial), desalineaciones a corregir (severidades/ventanas PR-01/PR-02, nombres y umbrales de métricas, ejes de prompts faltantes) y acciones. | Alineación |
| 09 | `nucleo/09-justificacion-ovd-y-defensa.md` | ¿Por qué OVD si un modelo cerrado detecta cascos mejor? Reencuadre de la tesis, 5 argumentos de defensa, Q&A hostil, estructura del cierre del informe, y qué mostrar en la presentación (4 números, videos V1–V4, overlay renderer, gestión de riesgo de demo). | Defensa |
| 10 | `nucleo/10-registro-alcance-y-exclusiones.md` | Cierre formal del alcance: la lista cerrada de lo que SÍ se implementa (núcleo validable + EBE ya construido + distribución mínima) y el registro E-01…E-13 de todo lo excluido, cada uno con estado, regla del informe que lo ampara, rastro documental y frase de declaración. **Documento rector del alcance.** | Alcance |
| 11 | `nucleo/11-relevamiento-media-plane.md` | Relevamiento completo del media-plane (estado 2026-07-09): API, módulos, flujos single-host/two-node, historia de ramas, y las novedades sin commitear (visibilidad two-node en webconsole validada E2E). Hallazgo: `VideoAnnotationWriter` ya cubre media pieza del overlay renderer del doc 09. | Relevamiento |
| 12 | `nucleo/12-diseno-prompts-y-fusion-ehyb.md` | Bajada operativa de D1 (complementa el doc 04, se congela con él): prompt sets `eind_v1`/`edir_v1` desde Tabla C.1, reglas de comparabilidad (variable única, calib/test, aislado-vs-completo), **fusión E-HYB** (dual-run, gating por persona, or/and con factor de ventana), medición en 3 niveles contra Tabla D.4, protecciones del núcleo validable. | Diseño experimental |

**Lectura mínima si hay poco tiempo:** 02 (norte) → 03 (decisiones) → 07 (riesgos) → 08 (alineación con el informe) → 09 (defensa).

**¿Venís a implementar, no a leer?** Empezá por
[`operacion/32-handoff-arranque-tramo-plataforma.md`](operacion/32-handoff-arranque-tramo-plataforma.md):
estado de los repos, Paso 0 y orden de trabajo con gates.

### `decisiones/` — ADRs (2026-07-09)

Las 11 decisiones formalizadas: D1–D6 del tablero + semántica 1:1, control-plane
como servicio mínimo, config centralizada/webconsole, secuenciación
plataforma-primero y frontera de política de alertas. Tabla completa en
`decisiones/README.md`. Se leen después del doc 03 (que explica cada dimensión) y
antes de cualquier spec.

### `specs/` — Etapa 4 por módulo (serie 40, en construcción)

Cola y reglas en `specs/README.md`. Orden de ejecución (ADR-010, plataforma
primero): 40 plataforma → 41 control-plane → 42 media-plane → 44 experimental-setup
→ **43 clip bench** (escrito y congelado; su disparador es el cierre del 44 —
corridas/configs trazables + runner + reporte; el material crudo de videos ya se
arma en paralelo). El 45 (distribución) no bloquea al 43 y corre tras el 44.
Se escriben sin alternativas, citando los ADRs.

### `contingencia/` — fuera del plan

| # | Documento | Qué responde |
|---|---|---|
| 20 | `contingencia/20-investigacion-finetuning-condicionada-e04.md` | Investigación completa de fine-tuning de GDINO (MM-GDINO/ODVG) y YOLOE sobre nuestros datos, por si sobra tiempo: inventario de lo ya listo, presupuestos GPU, escalera T1–T3 con criterios go/no-go pre-registrados, y una corrección de cita del paper Abdalwhab para el informe. **No reabre E-04.** |

### `operacion/` — runbooks y mediciones del host local

| # | Documento | Qué responde |
|---|---|---|
| 30 | `operacion/30-runbook-local.md` | Cómo levantar media-plane + webconsole en local sin Docker, con hot-reload, para iterar rápido: comandos por terminal, refs de modelo, lanzar una corrida RTSP, y las trampas conocidas (`dist/` viejo servido en silencio, run "succeeded" con cámara caída). |
| 31 | `operacion/31-benchmark-modelos-host-local.md` | Benchmark de las 6 variantes GDINO/YOLOE: BENCH v2 val con GT (mAP@0.5, AP por clase, recall CR-01) + cámara RTSP en vivo (keep-up, latencia, VRAM). **Hallazgo clave: YOLOE es ciego a `bare_head` (recall CR-01 ≈ 0), y el mAP oculta que GDINO-base gana en CR-01 y `vest` pese a perder en mAP.** |
| 32 | `operacion/32-handoff-arranque-tramo-plataforma.md` | *(Reemplazado por el 36 → 50; registro histórico.)* Estado congelado de los repos al arranque del tramo, orden de lectura, reglas del workspace, el **Paso 0** (ya ejecutado, ver 33), el orden de trabajo con sus gates, las decisiones que no se re-litigan y lo pendiente del usuario. |
| 33 | `operacion/33-fase0-rerun-motor-mati.md` | **Paso 0, cerrado (2026-07-09).** Fase 0 re-ejecutada con el motor de `mati`. **Hallazgo clave: las alertas no cambian (137 = 137) y es correcto** — el BENCH tiene cero EPP disputado entre personas, así que el matching 1:1 es un no-op sobre imágenes; demostrarlo exige el clip bench. Captura el warning de `det_NNN` (evidencia de G0) con una corrida diagnóstica aparte, y corrige dos afirmaciones del doc 32. |
| 34 | `operacion/34-implementacion-g0-resultados-y-deuda.md` | **G0 implementado (2026-07-10), gate alcanzado** (F1=1.0 en ambas granularidades, verificado significativo). ADR-012 **confirmado** por par discriminante. El BENCH baja de 137 a 77 alertas por diseño (invariante Σ`subjects_in_evidence_max` = 137 exacto). **Corrobora empíricamente la limitación D2.2 del doc 07**: un riesgo transitorio adelanta el reloj del episodio de escena. Deuda: nadie produce `track_id` (⇒ modo `subject` inerte), el overlay pinta una caja por escena, y el motor no tiene purga de estado. |
| 35 | `operacion/35-verificacion-e2e-video-rtsp-real.md` | **Cierra la brecha del doc 34: inferencia real, no simulada.** Media-plane levantado con GDINO-tiny real en GPU sobre el video crudo (733 frames, 0 fallos) y sobre la cámara RTSP real (192.168.1.5, 3 frames, reloj de pared real) → encadenado al motor G0. Confirma en t=4000/7000ms exacto sobre video; aliasing de `det_NNN` medido de nuevo (1831px de recorrido) sobre esta corrida fresca. El camino EBE con bus en vivo sigue sin existir. |
| 36 | `operacion/36-handoff-plan2-bus-y-live.md` | *(Reemplazado por el 50 al ejecutarse el plan 2; registro histórico del arranque.)* Estado congelado post-G0: qué estaba hecho, qué leer, el plan 2 (MediaEventSource → bus ZeroMQ → runtime live, con sus gates), la deuda a absorber, trampas operativas y lo pendiente del usuario. Su §3 lleva el tablero tachado al día. |
| 37 | `operacion/37-plan2-bus-y-live-resultados.md` | **Plan 2 ejecutado (2026-07-10): ítems 2–3 del orden.** `MediaEventSource` + bus ZeroMQ (`bus.envelope.v1`, XPUB, `seq` monótono) + runtime live 1:1. Gate de paridad replay↔stream en verde y **verificado significativo por mutación** (bbox 1 px ⇒ falla; dropout 1 frame ⇒ lo absorbe la histéresis). E2E real: 40/40 unidades, 0 perdidas, cierre por `run_finished`, y el mismo run releído offline da **artefactos byte-idénticos** (ADR-003 demostrado). §6: los 9 defectos del plan que la revisión atrapó. §7.2: **corrección medida** — la purga de estado del motor NO bloquea el live (el estado crece con `source_id` distintos, no con el tiempo). |
| 38 | `operacion/38-servicio-minimo-control-plane.md` | **Ítem 4 ejecutado (2026-07-10).** El control-plane como servicio FastAPI :8081 (`eovrt-control serve`): 7 endpoints, un run activo (409), config por payload o referencia (ADR-009). Invariante central: **el 201 de `mode: live` implica `BusSource` ya suscripto** — el primer gate era vacuo (probado con mutación) y se reemplazó por uno estructural. Parada cooperativa (`request_stop()`) para no morir con el SIGABRT de libzmq. E2E con **los dos servicios hablándose**: 30/30 unidades, 0 perdidas, orden del spec 44 respetado. §6: 8 defectos corregidos (path traversal por `run.id`, run fantasma por `BaseException`, 500 por config inválida, reuso de `run.id`…). |
| 39 | `operacion/39-instrumentacion-g2a-media-plane.md` | **Ítem 5, mitad media-plane, ejecutado (2026-07-10).** Insumos de `t_capture→alert` (spec 40 §5.2.4): instante de captura estampado al leer la unidad (viaja por el canal y el wire two-node), `source_clock` por fuente, `g2a_ms` por `unit_id` en `metrics.jsonl`, bloque `g2a` en el summary (percentiles, warm-up declarado, presupuesto 50–250 ms). **En two-node `g2a_ms` es `null` y el bloque `not_interpretable / cross_node_monotonic_clock`** — los relojes monotónicos de dos hosts no se restan. Corrida real: P50 14.7 ms / P95 31.8 ms, dentro de presupuesto. |
| 50 | `operacion/50-reporte-estado-tramo-plataforma.md` | **PUNTO DE ENTRADA PARA IMPLEMENTAR (reemplaza al 36).** Reporte consolidado del tramo al 2026-07-10: tablero de ítems (1–5a hechos), qué se construyó con su evidencia, los gates verificados por mutación, los 22 defectos que atrapó la revisión adversarial, las reglas duras del dominio, el inventario de lo **no commiteado** (79 rutas en 3 repos), y lo que falta en orden: ítem 5b detallado (mitad control-plane + `cr01_cr02_v2` + publisher de alertas), specs 44/45/43, deuda técnica y pendientes del usuario. |
| 51 | `operacion/51-instrumentacion-5b-control-plane.md` | **Ítem 5b ejecutado (2026-07-11).** Mitad control-plane de `t_capture→alert` (spec 40 §5.2.4): `ts_receive_ms`, hitos `first_evidence_*`, `alert_registered_ms`, `experiment_id` en los tres eventos, percentiles + TTFA interna en el summary, y el `join` con estados de aplicabilidad (ADR-006). Pattern set oficial **`cr01_cr02_v2`** (CR-01 high 4000ms / CR-02 medium 7000ms, escena, sin cooldown/cobertura). Publisher de alertas `control.alert.v1` (espejo del media-plane, persiste-primero). **177 passed**, revisión final LISTO PARA MERGE. E2E real por bus: 300 unidades, 2 alertas, 0 perdidas, join `not_interpretable/dbe_media_time` (correcto para DBE video). §3: byte-paridad rota por `exclude_none` en el sketch del plan, gate sin cableado real, flicker vacuo — los tres corregidos. |
| 52 | `operacion/52-evaluate-alerts-v2.md` | **`evaluate-alerts` v2 ejecutado (2026-07-11).** Evaluador temporal del control-plane a v2 (spec 41 §8 item 7): matching alerta↔episodio por ventana en ms `[start_ms+persistencia_min, start_ms+t_alert_max]` (spec 43 §4.1, default Tabla D.4), `re_alerts` (ADR-011, no son FP), `sub_threshold_events`, estados de aplicabilidad (ADR-006); path v1 frame-based intacto. **192 passed**, LISTO CON RESERVAS. Defecto corregido: doble-conteo entre episodios de misma condición con ventanas solapadas (P8). Deuda alta: la asignación greedy puede DEFLACIONAR recall en P8 con ≥2 alertas (fix = matching bipartito). Los números REALES siguen diferidos (dataset de clips con GT, spec 43). |
| 53 | `operacion/53-experimental-setup-runner-y-reporte.md` | **Experimental-setup núcleo backend ejecutado (2026-07-11, spec 44 A1+A2).** El runner reproducible que orquesta los dos planos por HTTP en el orden correcto (control-first live con `SubscriptionNotConfirmed` obligatorio; media-first DBE-replay, no dispara control si media falla), + consolidación ADR-014 (`detections.jsonl` referenciado nunca copiado) + generador `report.json`/`report.md` con el diccionario spec 40 §5.1 y estados de aplicabilidad ADR-006 (video→`not_interpretable/dbe_media_time`, imágenes→`non_temporal_source`, GT→`not_applicable/no_ground_truth`). Repo `e-ovrt_experimental-setup`, 151→204 passed, LISTO PARA MERGE. Falta: webconsole (Plan B), frontend React (Plan C), spec 45. |
| 54 | `operacion/54-video-gt-lab-y-contrato-gt.md` | **video-gt-lab ejecutado (2026-07-11) — el tooling del spec 43, COMPLETO y PUSHEADO.** Pipeline semi-automático de GT temporal de video: `prepare_clip.sh` (CFR) → `preannotate_video` (GDINO-**base** anti-circularidad + ByteTrack + NMS + huecos de evidencia marcados) → CVAT (atributos `unknown/true/false` — la incertidumbre NUNCA fabrica infracción) → `derive_clip_gt.py` (+`provenance`) → `validate` + kappa → **`promote_clip.py`** al banco `processed/clip_bench/`. La auditoría reparó el contrato GT↔evaluador (**`source_id = clip_id`**, knob en media-plane) y la sesión E2E cerró TODOS los gaps de código: **SDR+TTFD** en evaluate-alerts (5 métricas del spec 43 §10), umbrales alineados **4000/7000** (Tabla D.4), hook `clip_id`/`ground_truth` en el runner. **Smoke §8.8 EJECUTADO real** con `cb_b01_p7` (GT **preliminar** por revisión visual, estado `gt_preliminary`): P=0.5 R=1.0 F1=0.67, t_alert=4000ms, TTFD=0ms, SDR=0.999 — el FP CR-02 es hallazgo del modelo. Suites 102/520/212/247; pusheado (datasets f8a2f3bc, media 5653978, control 853f690, exp-setup eda5736). Pendiente: pasada humana en CVAT (reemplaza el GT preliminar), grabación A+C, EBE-desde-clip. |
| 55 | `operacion/55-como-continuar.md` | **⬅️ EMPEZÁ ACÁ SI VOLVÉS DESPUÉS DE UN TIEMPO.** Guía paso a paso de continuación (2026-07-11): qué está hecho (plataforma completa y probada E2E: dos planos + evaluate-alerts con las 5 métricas + runner + laboratorio de GT de video), qué falta (pasada humana en CVAT, grabación del banco A+C + consentimientos, spec 45, D1 bloqueado por acta `edir_v1`, EBE-desde-clip) y **el orden concreto con los comandos reales**: PASO 1 probar CVAT con el clip que ya está (`cb_b01_p7`, valida la herramienta antes de grabar) → PASO 2 reemplazar el GT preliminar por el tuyo → PASO 3 benchmark con tu GT → PASO 4 grabar el banco (guiones spec 43 §3) → PASO 5 resultados. Incluye qué se me puede pedir mientras tanto y una tabla de referencias rápidas. |

Evidencia cruda, para que los números sean auditables y re-generables:

| Archivo | Qué es |
|---|---|
| `operacion/datos/31-benchmark-modelos-host-local.datos.json` | Salida cruda de las 12 corridas (6 modelos × 2 suites), con `run_id`, latencias y evaluación. |
| `operacion/datos/31-benchmark-modelos-host-local.driver.py` | Script que las reproduce: levanta y baja un servicio por modelo. |
| `operacion/datos/33-fase0-rerun-motor-mati.datos.json` | Los tres `summary.json` (motor viejo, motor nuevo, probe de persistencia) y el conteo de items disputados. |
| `operacion/datos/33-fase0-rerun-motor-mati.probe.py` | Script que reproduce el conteo de items EPP disputados (el que explica la igualdad). |
| `operacion/datos/37-2026-07-10-live-e2e-*.json` / `*-alerts.jsonl` | Doc 37 §4: summaries de la corrida live (media + control), del replay byte-idéntico, y sus alertas. |
| `operacion/datos/38-2026-07-10-dos-servicios-*.json` / `*-alerts.jsonl` | Doc 38 §4: summaries y alertas de la corrida E2E con los dos servicios HTTP. |
| `operacion/datos/39-2026-07-10-g2a-video-summary.json` | Doc 39 §3: summary de la corrida real de G2A sobre video (`source_clock: media`, percentiles). |

### `informe/` — el TFG, en desarrollo

Nuestro entregable. **No es fuente de verdad cerrada**: se lo critica desde `nucleo/` y se
lo reescribe al final, cuando estén tomadas las decisiones (D1–D6) y corridos los
experimentos. Los redlines pendientes viven en los docs 02 (§4.8, erratas) y 08 (§2,
desalineaciones).

| # | Documento | Qué es |
|---|---|---|
| — | `informe/E-OVRT-VDP_v1.1_05062026-sin-indice.docx` | El informe completo del TFG (Etapas 1–2 + consolidación metodológica §17.1 + Etapa 3 previa). Aporta el protocolo metodológico contra el que se leen los docs 01–11. |
| — | `informe/E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` | El capítulo 17.3 standalone (versión más reciente de Etapa 3). Insumo del doc 02, que lo revisa críticamente. |
| 90 | `informe/90-etapa3-texto-extraido.md` | Texto plano de Etapa 3, **solo para búsqueda y cita rápida**. Es una extracción derivada: al editar, se edita el `.docx`, no este archivo. |

### `herramientas/` — entorno de desarrollo

| Documento | Qué es |
|---|---|
| `herramientas/2026-07-05-docker-wsl-disk-control-design.md` | Diseño del mecanismo de 3 capas para que Docker/WSL2 no agote el disco `C:`. |
| `herramientas/2026-07-05-docker-wsl-disk-control.md` | Plan de implementación del mismo. Los scripts viven en `projects/scripts/`. |

## Estado del tablero de decisiones (espejo de 03 §9 — actualizar allí primero)

**2026-07-09 — TABLERO CERRADO.** Todas las decisiones formalizadas en
`decisiones/` (ver su [README](decisiones/README.md) para la tabla completa):

| # | Dimensión | Estado |
|---|---|---|
| D1 | Estrategia del núcleo | **ADR-001** — E-IND (encuadre); el experimento del doc 04 cuantifica y es lo único que puede revisarla |
| D2 | Granularidad del patrón | **ADR-002** — G0 núcleo + G1 demostrativa (tracker portado al media-plane, sin métricas MOT) |
| D3 | Bus media→control | **ADR-003** — ZeroMQ PUB/SUB; broker diferido |
| D4 | Config paraguas / experiment_id | **ADR-004** — manifiesto en experimental-setup; runner CLI orquesta por HTTP |
| D5 | Distribución + canal | **ADR-005** — recorte, MQTT, **repo propio** |
| D6 | Reporte consolidado + métricas | **ADR-006** — Camino B + diccionario de métricas + criterio de relojes |
| +  | Semántica de corrida EBE | **ADR-007** — 1:1 con el run del media-plane |
| +  | Forma de ejecución del control-plane | **ADR-008** — servicio mínimo; webconsole cliente de ambos planos (excepción registrada en doc 10) |
| +  | Config y gestión de la plataforma | **ADR-009** — config experimental centralizada en experimental-setup; webconsole superficie de gestión primaria (+mejora UX); runner CLI para campañas (doc 10 ítem 11) |
| +  | Orden de ejecución del proyecto | **ADR-010** — tramo plataforma primero (servicios, bus, trazabilidad, instrumentación); el clip bench (spec 43) se dispara al cierre del spec 44 (la distribución no lo bloquea); Fase 2 de D1 y R3 se mueven con él; material crudo de videos en armado paralelo |
| +  | Frontera de política de alertas | **ADR-011** — el motor emite en cada confirmación; cooldown y supresión de re-notificación pasan al módulo de distribución; el evaluador cuenta `re_alerts`, no los penaliza como FP |
| +  | Qué sostiene G0 sin identidad | **ADR-012** — la memoria de cobertura EPP es inaplicable bajo escena (se ignora con causa declarada; la histéresis la subsume) y sobrevive solo en G1; la expiración de sujetos sí se reinterpreta a escena. **Falsable por test** (gate F1=1.0 + test de parpadeo) |
| +  | Qué mide cada tipo de fuente | **ADR-013** — imágenes → percepción y asociación espacial; video → patrones con GT temporal; RTSP → patrones + métricas end-to-end. La plataforma detecta la temporalidad por `source_type` y declara `not_applicable / non_temporal_source` sola; sobre imágenes un patrón con persistencia **no puede alertar** (medido: doc 33 §4) |
| +  | Dónde caen los resultados de un run global | **ADR-014** — run global (con `experiment_id`) → resultados **consolidados** en `experimental-setup/runs/<experiment_id>/` (git-ignored) con **híbrido selectivo**: copia lo liviano (configs, summaries, metrics, alerts, report), referencia por `run_id` los `detections.jsonl` pesados (fuente de verdad = `runs/` del plano, DA-03). Run de test de un módulo → `runs/` local, sin consolidar; "sellado" opt-in materializa los crudos para archivado permanente |

**Insumo nuevo para D1:** el doc 31 muestra que YOLOE no puede sostener CR-01 tal como está
definida (`bare_head`). Si CR-01 sigue anclada a esa clase, YOLOE sale del espacio de
búsqueda antes de correr el experimento del doc 04.

## Trabajo común que no depende de ninguna decisión (arranca ya)

1. Corrida DBE end-to-end real (media-plane → control-plane sobre detecciones reales).
2. ~~Clip bench con GT temporal — mayor lead time~~ **✎ ADR-010:** diseño hecho
   (spec 43), ejecución al cierre del spec 44; en paralelo corren el armado del
   material crudo de videos (en proceso) y los trámites (Intel, consentimientos).
3. Calibración de umbrales/regiones con datos reales.
4. Erratas del .docx de Etapa 3 (doc 02 §4.8).
