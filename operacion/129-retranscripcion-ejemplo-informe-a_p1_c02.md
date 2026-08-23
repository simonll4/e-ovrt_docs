# 129 — Re-transcripción del ejemplo canónico del informe sobre clip vigente (`a_p1_c02`) (2026-08-22)

- **Contexto:** la revisión de cierre (`informe/ajustes/09` §3.2) marcó que el ejemplo de
  evento de percepción y de alerta que los materiales del informe muestran "listo para
  pegar" salía de **`cb_b01_p7`**, clip **retirado del banco** el 2026-08-03 (licencia sin
  registrar + GT por IA). El propio material (`informe/ajustes/material-etapa-3/94` §1.3)
  dejaba dos salidas honestas y recomendaba la **(a): re-transcribir desde un replay sobre
  un clip del banco vigente**, sin editar identificadores a mano (la garantía de
  transcripción literal viene de la auditoría del 2026-07-12, doc `95` §2).
- **Este doc es la constancia de esa re-transcripción**, ejecutada el 2026-08-22. Regla
  heredada del doc 119: ninguna fila sin haber corrido el comando — todo lo de abajo fue
  ejecutado y observado ese día.

## 1. La cadena elegida (todo artefactos reales, cero fabricación)

| Eslabón | Valor |
|---|---|
| Clip | **`a_p1_c02`** — banco vigente (rodaje, Bloque A), escenario P1, condición CR-01, 1 episodio esperado |
| Corrida de medios | `run_20260803_211225_dbe_grounding_dino_1e06f3` (GDINO-tiny-560, set `cr01_cr02_v2_short` por catálogo) — la corrida REAL de la campaña T1 del banco de clips (`results/clip_bench/t1_gdinotiny560_v2short_scene/evals/eval_a_p1_c02.json` apunta su `detections_path` a este run) |
| Unidad transcripta | `frame_000229` (7.633,33 ms de video) — **la unidad en la que CR-01 confirma**; contiene 3 detecciones y se muestran las 3 (sin recorte) |
| Replay de control | `bench_a_p1_c02_gdino_20260822_20260822T225536Z` — `eovrt-control replay` sobre el `detections.jsonl` de ese run, pattern set `cr01_cr02_v2`, 1.123 unidades, 2 alertas (confirmación + re-alerta en `frame_000764`) |

**Verificación de la cadena temporal:** primera evidencia en `frame_000109` (3.633,33 ms)
→ confirmación en `frame_000229` (7.633,33 ms) = **4.000 ms exactos**, la ventana de
CR-01. Contra el GT del banco, `t_alert_system_ms = 4.600,33` y `TTFD = 600,33`
(`metrics.json` de la campaña, fila `a_p1_c02`): la descomposición TTFD + ventana =
t_alert cierra al milisegundo. El replay del 08-22 reproduce la misma confirmación que el
replay independiente del 08-05 (`defensa_a_p1_c02_scene_20260805T180039Z`): mismos
`unit_id`, `timestamp_ms`, evidencia y `rationale`.

**Bonus pedagógico que el ejemplo viejo no tenía:** la unidad contiene un `helmet` (0,456)
**fuera** de la región cefálica del sujeto (cae a su derecha, más allá del margen lateral
del 12 %), y `vest` positivo (0,8755) del mismo sujeto. CR-01 confirma igual y CR-02 no
abre episodio: es la inferencia espacial de ausencia (E-IND) por sujeto y por región,
visible en un solo artefacto.

## 2. Artefactos archivados (capa evidencia)

```
docs/operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-alerts.jsonl
docs/operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-summary.json
```

## 3. Dónde quedó aplicado

- `informe/ajustes/material-etapa-3/92` §2.2 (DTO literal), §2.3 (envoltorio), §4.3
  (superficie de crecimiento), §5.1 (comentario `subject_key`), §5.2 (alerta) y el
  hallazgo G2A (§7): todos re-transcriptos sobre esta cadena. El G2A del run vigente:
  `p50 1.473,1 ms · p95 4.953,9 ms · p95_within_budget: false` (n = 1.123).
- `informe/ajustes/material-etapa-3/94` §1.3 (evento) y §1.4 (alerta): ídem; la
  advertencia "RESOLVER ANTES DE PEGAR" pasó a "RESUELTO".
- `informe/ajustes/09` §3.2: marcado ✅ RESUELTO.
- Los artefactos históricos del ejemplo anterior (`operacion/datos/95-2026-07-12-…`)
  **no se tocan**: son la evidencia de la auditoría del 07-12 y quedan como historia.

## 4. Cómo re-verificar

```bash
# la unidad transcripta, literal
grep '"unit_id": "frame_000229"' \
  e-ovrt_media-plane/runs/run_20260803_211225_dbe_grounding_dino_1e06f3/detections.jsonl
# la alerta archivada
head -1 docs/operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-alerts.jsonl | python3 -m json.tool
```
