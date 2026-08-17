# 115 — Soporte experimental transversal: métricas, reportes y consola

- **Fecha del relevamiento:** 2026-08-13
- **Estado:** **GATE DE INSTRUMENTACIÓN CERRADO; gestión histórica y consola diferidas**
- **Propósito:** separar el soporte mínimo obligatorio para producir resultados del
  informe de las capacidades operativas que pueden implementarse más adelante.
- **D-115.1 — Decisión vigente:** no crear un repositorio ni un servicio independiente de
  métricas y reportes. La instrumentación productor → artefacto → consolidación →
  reporte sí es condición previa para iniciar el informe; el histórico durable, la
  consulta de campañas y su visualización ampliada no lo son.

---

## 1. Aclaración arquitectónica

En la Etapa 3, los bloques del diseño son **responsabilidades lógicas**, no una
correspondencia obligatoria de un bloque con un proceso o repositorio. Con esa lectura:

1. `e-ovrt_experimental-setup` es el dueño de la **configuración experimental**,
   los manifiestos, la orquestación, la consolidación y la webconsole. Esta asignación
   coincide con ADR-009.
2. El **soporte experimental** —trazabilidad, observabilidad, métricas, reportes e
   inspección— es una capacidad transversal. Cada repositorio instrumenta y persiste
   las métricas que conoce; `e-ovrt_experimental-setup` reúne las salidas de una corrida,
   las proyecta en reportes y las presenta en la consola.
3. Por lo tanto, **no falta un “repo de métricas”**. Falta completar un subsistema
   transversal que ya existe parcialmente.

La regla de responsabilidad futura queda así:

```text
media-plane ───────────────┐
control-plane ─────────────┼─> artefactos por módulo
alert-distribution ────────┤
datasets/evaluadores ──────┘
                                  │
                                  v
experimental-setup: consolidar -> indexar -> reportar -> comparar -> mostrar
```

Esta distribución conserva la autonomía de los repositorios: el coordinador no debe
recalcular métricas de dominio que pertenecen a otro módulo ni convertir a los planos
en dependientes de la webconsole.

## 2. Estado verificado al 2026-08-13

### 2.1 Lo que ya existe

| Componente | Producción o consumo actual | Estado |
|---|---|---|
| `e-ovrt_media-plane` | `metrics.jsonl`, `summary.json`, G2A, FPS, latencias, descartes, recursos y `eval_perception.json` | Implementado localmente |
| `e-ovrt_control-plane` | `metrics.jsonl`, `summary.json`, estados y eventos de patrón, alertas y evaluación temporal | Implementado localmente |
| `e-ovrt_alert-distribution` | `notifications.jsonl`, `distribution_summary.json`, outcomes y latencia de notificación por modo de reloj | Implementado localmente |
| `e-ovrt_datasets` | evaluadores, reportes de benchmark y verificadores de resultados | Implementado para las campañas actuales |
| `e-ovrt_experimental-setup` | manifiestos, runner, consolidación en `runs/<experiment_id>`, `report.json`/`report.md`, resultados curados en `results/` y webconsole | Flujo de métricas implementado; gestión histórica parcial |

Los avances recientes de distribución deben considerarse parte del estado actual: el
runner puede lanzarla de forma opcional, el reporte incorpora su summary y la vista de
detalle muestra outcomes. No corresponde volver a registrar esas piezas como ausentes.

La separación física vigente también es correcta:

- `runs/<experiment_id>/`: artefactos automáticos por ejecución, no versionados;
- `results/`: campañas seleccionadas, promovidas, versionadas y citables;
- repositorios de cada módulo: fuente de verdad de sus artefactos locales;
- webconsole: superficie de inspección, no fuente primaria de medición.

En el snapshot relevado, `experimental-setup/runs/` contiene 197 directorios con
reporte, pero solo 8 contienen el par de summaries de media y control, 3 incorporan
evaluación temporal, y ninguno contiene todavía una evaluación de percepción o un
summary de distribución consolidado. `results/` conserva 16 directorios de campaña y
sus índices por material; ese conjunto sí es la fuente citable usada para el informe.

Esas cantidades describen artefactos históricos y no se modifican retroactivamente por
el cierre del gate en código. Las corridas nuevas sí transportan los contratos corregidos.

### 2.2 Configuración experimental

La asignación de responsabilidad es correcta, pero ADR-009 está cumplida de forma
incompleta:

- los 9 manifiestos paraguas y sus configs de media/control viven en
  `e-ovrt_experimental-setup/experiments/`;
- las configs de control todavía referencian mediante path absoluto el pattern set
  `e-ovrt_control-plane/configs/patterns/cr01_cr02_v2.yaml`;
- ningún manifiesto versionado declara aún el bloque opcional `distribution`;
- los catálogos de modelos y datasets permanecen deliberadamente en el media-plane,
  como permite ADR-009; eso no es una brecha.

## 3. Gate obligatorio de instrumentación para el informe

**Estado al 2026-08-13: CERRADO en código y pruebas.** El criterio aplicado no fue
solo “existe un JSON”, sino la cadena completa: definición de la métrica, productor,
artefacto persistido, transporte o referencia, proyección al reporte y estado de
aplicabilidad.

Los cierres realizados son:

1. el evaluador del media-plane calcula y persiste `mAP50` junto con
   `per_class[].AP50` y `cr01_detection_recall`, tanto por CLI como por API;
2. el consolidador incluye `media/eval_perception.json` entre los artefactos livianos;
3. el reporte consume el contrato canónico del media-plane y mantiene lectura tolerante
   del contrato legado. Un artefacto histórico sin agregado no se presenta como
   `computed` con valor nulo: queda `applicable_not_computed` con causa explícita;
4. `t_alert-system`, precisión, recall, F1 y `re_alerts` se proyectan desde
   `control/temporal_evaluation.json`, respetando los estados de aplicabilidad del
   evaluador para clips negativos, censurados o sin matches;
5. la instrumentación de distribución conserva outcomes y separa la latencia `live`
   de `wall_clock_dbe`; el reporte nunca presenta una medición DBE como latencia
   operativa real.

| Familia que necesita el informe | Productor y artefacto | Consumo consolidado | Estado |
|---|---|---|---|
| Percepción: mAP50, AP por clase, recall CR-01 | media-plane, `eval_perception.json` | `mAP`, `AP <clase>`, `recall CR-01` | Cerrado |
| Rendimiento: G2A, latencias, FPS, drops, recursos | media-plane, `metrics.jsonl` + `summary.json` | métricas directas y sub-etapas | Cerrado |
| Alertas: P/R/F1, `t_alert-system`, TTFD, SDR, FAR, censura, re-alertas | control-plane, `temporal_evaluation.json` | métricas temporales con aplicabilidad | Cerrado |
| Cadena frame → alerta | media `metrics.jsonl` + control `alerts.jsonl` | `t_capture→alert` y `t_compute-budget` | Cerrado |
| Entrega de alertas | alert-distribution, `notifications.jsonl` + `distribution_summary.json` | outcomes y `t_alert-notification` por modo de reloj | Cerrado en instrumentación |
| Benchmarks y campañas | datasets/evaluadores + `results/` | tablas e índices citables | Cerrado para resultados actuales |

Este cierre habilita el inicio de la redacción. No implica que todas las cifras finales
ya existan: para completar el resultado de distribución todavía debe ejecutarse una
corrida representativa `live` y promoverse su evidencia citable. Eso es una tarea de
campaña, no una brecha de instrumentación.

Este cierre levanta el gate TÉCNICO; la orden de arrancar la redacción sigue siendo del
usuario (regla vigente desde el 08-05).

### 3.1 Evidencia de verificación del cierre

Ejecución fresca del 2026-08-13:

- media-plane: `.venv/bin/pytest -q` → **641 passed, 5 skipped**;
- control-plane: `.venv/bin/pytest -q --ignore=tests/labs` → **312 passed**;
- alert-distribution: `.venv/bin/pytest -q` → **69 passed, 1 deselected**;
- datasets: `python3 -m pytest datasets/tests -q` → **418 passed**;
- experimental-setup, cadena de instrumentación: consolidación, reporte, wiring
  post-run, evaluación temporal, distribución y gate A2 → **71 passed**;
- Ruff en media-plane y en el backend experimental → **All checks passed**;
- `git diff --check` en los repos modificados → sin errores.

La suite de rutas de alertas/reporte de la webconsole no se usó como evidencia de este
gate: en el entorno actual su `TestClient` se bloquea durante el startup del propio
harness, antes de ejecutar la aplicación. El runner async, la consolidación y el reporte
sí quedaron cubiertos. Reparar esa prueba corresponde al frente de UI diferido.

## 4. Brechas que quedan diferidas

**D-115.2 — Decisión vigente:** se difieren con causa los frentes A–F de esta sección;
no bloquean las cifras curadas ni autorizan por sí mismos el inicio de la redacción.

### A. Contrato general versionado de artefactos

El contrato mínimo requerido por el informe está cubierto. Sigue siendo conveniente,
pero no bloqueante, formalizar un catálogo versionado que distinga para todos los
módulos artefactos livianos, pesados referenciados, evaluaciones derivadas, errores,
descartes, provenance y versión de esquema.

### B. Trazabilidad anti-drift

El reporte sabe comparar `sent_config` con la `effective_config` persistida, pero el
runner no guarda `sent_config` en el manifiesto efectivo. En la práctica, el chequeo
queda normalmente como “no verificable”.

### C. Historial durable de corridas en la webconsole

`ExperimentRunManager` conserva los estados en memoria. Después de reiniciar el backend:

- el endpoint genérico de detalle ya no encuentra la corrida;
- el endpoint de reporte puede resolver el archivo por convención, pero la página de
  detalle necesita primero el estado del experimento;
- alertas y referencias a los runs de los planos dependen del estado volátil o del
  servicio remoto.

La pantalla “Experimentos” lista principalmente manifiestos, mientras “Corridas” y
“Comparar” están centradas en runs del media-plane. Todavía no existe un índice durable
de experimentos consolidados reconstruido desde disco.

### D. Resultados curados y promoción

La webconsole no consume los índices de `results/` ni ofrece una vista de campañas
citables. Tampoco hay un flujo explícito y verificable para promover una corrida de
`runs/` a `results/` conservando selección, provenance y referencias a artefactos.

### E. Distribución ejercitada desde la configuración real

El código de orquestación, reporte y visualización ya admite distribución, pero falta
al menos un manifiesto versionado que active el módulo y una prueba E2E representativa
que deje sus artefactos dentro del layout global. Esta brecha es de adopción e
integración, no de creación de otro módulo.

### F. Documentación de estado

Al retomar este frente debe reconciliarse `decisiones/estado-de-implementacion-adrs.md`
con el código vigente. Algunas descripciones de ADR-009, ADR-014 y distribución quedaron
por detrás de los avances recientes o expresan como cerrado un alcance más amplio que el
realmente verificado.

## 5. Resultado objetivo del frente ampliado

El gate del informe ya cubre producción, persistencia, consolidación y reporte de las
métricas necesarias. El soporte experimental ampliado se considerará completo cuando:

1. todos los contratos de artefactos tengan esquema y versión explícitos;
2. `sent_config` y `effective_config` permitan verificar drift por plano;
3. la webconsole reconstruya el historial desde `runs/` después de un reinicio;
4. la consola permita inspeccionar y comparar tanto corridas automáticas como campañas
   curadas de `results/`, sin confundir sus estatutos;
5. exista una promoción explícita y trazable de `runs/` a `results/`;
6. al menos un manifiesto real ejercite media + control + distribución de punta a punta;
7. las pruebas restantes cubran persistencia histórica y UI.

No se requiere un nuevo servicio central de métricas, una base de observabilidad
operacional ni un dashboard de producción para cumplir este objetivo.

## 6. Prioridad y relación con el informe

**Decisión del 2026-08-13:** la instrumentación es un gate obligatorio y quedó cerrado.
Por lo tanto, el desarrollo del informe puede comenzar usando los artefactos e índices
curados existentes. Quedan diferidas, sin bloquear esa redacción, la gestión histórica,
la promoción asistida y la visualización ampliada en la webconsole.

Este cierre levanta el gate TÉCNICO; la orden de arrancar la redacción sigue siendo del
usuario (regla vigente desde el 08-05).

Al describir la plataforma debe distinguirse:

- **diseño:** soporte experimental transversal y consolidación central;
- **implementación actual:** instrumentación distribuida y proyección de las métricas
  necesarias al reporte consolidado;
- **campaña pendiente:** evidencia `live` citable del tramo de distribución;
- **limitación diferida:** historial durable, promoción asistida y consulta de campañas
  desde la webconsole.

Esta limitación no invalida los resultados citables, porque estos se sostienen en los
artefactos versionados y verificados de `results/`, no en la persistencia de estado de la
webconsole.

## 7. Cuándo reabrir el frente diferido

Retomar después del primer tramo sustantivo de redacción, o antes solo si aparece una
necesidad concreta de demo o auditoría que requiera historial durable en la consola. El
orden recomendado al reabrir es:

1. persistencia de `sent_config` y cierre anti-drift;
2. índice durable de `runs/` y recuperación después de reinicio;
3. lectura de `results/` y promoción trazable;
4. manifiesto con distribución y corrida `live` citable;
5. contrato general versionado de artefactos;
6. actualización del estado de ADRs.

## 8. Fuentes de este registro

- Etapa 3: `informe/entregable/90-etapa3-texto-extraido.md`, en especial el bloque
  transversal de soporte experimental y las secciones de configuración, métricas y
  reportes.
- ADR-006: reporte consolidado y estados de aplicabilidad.
- ADR-009: configuración centralizada en `experimental-setup` y webconsole como
  superficie de gestión.
- ADR-014: layout híbrido de artefactos por `experiment_id`.
- ADR-016 y `operacion/114`: incorporación acotada de distribución.
- Código relevado en los cinco repositorios hermanos y artefactos actuales de
  `e-ovrt_experimental-setup/runs/` y `results/`.
