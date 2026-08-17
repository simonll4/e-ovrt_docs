# 123 — Cierre de la jornada T1: promoción, evaluación única y veredicto **NO-GO** (2026-08-17)

- **Contexto:** el full T1 (job `1167640`) quedó encolado el 15/08 y **corrió el 16/08**
  (`COMPLETED` exit 0, 10/10 épocas, 13m08s en una A30). Este doc cierra T-FT-050 (promoción),
  T-FT-051 (evaluación única del brazo tuned) y T-FT-052 (go/no-go), y con ellas la jornada
  de fine-tuning que autorizó [ADR-017](../decisiones/adr-017-fine-tuning-jornada-experimental.md).
- **Antecedente directo:** [`120`](120-cierre-t031-t032-baseline-26s.md) — comando de evaluación
  congelado, enforcement canónico v2 y **baseline YOLOE-26s one-shot** sobre `bench_v3`.
- **Regla heredada del doc 119:** ninguna fila de evidencia sin haber corrido el comando.
  Todo lo de abajo fue ejecutado y observado el 2026-08-17.

> **Veredicto: NO-GO.** El ajuste rescata `bare_head` del cero absoluto y multiplica el recall
> CR-01 por ~1.000, pero **se queda a 0,0045 del umbral de ganancia** y **rompe la retención de
> `person` (−11,62 %, tope 10 %)**. Los márgenes estaban firmados desde el 15/08, **antes** de
> existir la baseline y el checkpoint: esto es pre-registración estricta y un negativo así
> **es resultado, no fracaso** (ADR-017).

---

## 1. T-FT-050 — promoción del checkpoint (cerrada)

La regla 7 de `finetuning/README.md` prohíbe promover sin **integridad, binding de clases y
serving smoke**. Las tres se ejecutaron antes de copiar nada:

| Requisito | Cómo se verificó | Resultado |
|---|---|---|
| Integridad | sha256 y tamaño de `best.pt` contra `full-ready-1167640.json` (auditoría del finalize remoto), tras bajarlo | coincide byte a byte |
| Binding de clases | `torch.load` del checkpoint | `{0: person, 1: helmet, 2: vest, 3: bare head}` — exacto y en orden |
| Serving smoke | `verify_t1_media_plane.py --mode service --device cuda` | `fixed_vocabulary_serving_passed`, 5 detecciones, `set_classes` prohibido, caché de prompts intacta |

Recién entonces `best.pt` se copió a `e-ovrt_media-plane/models/yoloe/finetuned/t1/best.pt`
**conservando el sha256** (`5714f833…efbe`), y el catálogo `yoloe-26s-ft-t1.yaml` verificó contra
el hash que el protocolo tenía congelado (`97129219…cc9f`). Constancia:
`finetuning/manifests/t1_promotion_1167640.json`.

**Copia local de resguardo:** `finetuning/weights/finetuned/full-1167640/` (234 MB: los 12
checkpoints, la auditoría remota, metadatos y logs del job, `MANIFEST.sha256` 22/22 OK). Los
originales siguen en Mendieta. `last.pt` se conserva **sólo para auditoría** y nunca se evaluó
como segundo candidato.

## 2. T-FT-051 — corrida única del brazo tuned (cerrada)

`run_20260817_015315_dbe_yoloe_deterministic` → `finetuning/runs/t1_yoloe26s_tuned_bench_v3/`.
**6.477/6.477 unidades, 0 fallos, 0 drops, 40.696 detecciones**, 256,7 s de pared,
`errors.jsonl` vacío. Cobertura verificada por el comando congelado.

La config del brazo (`finetuning/configs/t1_tuned_bench_v3.yaml`) se validó **en seco contra la
baseline antes de correr**: los **15 campos que el protocolo congela** coinciden uno a uno
(`image_size 640`, `conf 0.25`, `iou 0.5`, `device cuda`, `half_precision true`, `warmup true`,
postproceso, `stride 1`, `seed 42`, adapter). La única variable es el modelo:
`yoloe/yoloe-26s` → `yoloe/yoloe-26s-ft-t1`.

### 2.1 Percepción — agregado (mAP50 0,4193 → **0,4171**)

| Clase | AP50 baseline | AP50 tuned | Δ | n_det base → tuned |
|---|---|---|---|---|
| person | 0,7843 | 0,6932 | **−0,0911** | 23.596 → 20.309 |
| helmet | 0,6286 | 0,6004 | −0,0282 | 16.758 → 16.144 |
| vest | 0,2642 | **0,3292** | +0,0650 | 1.297 → 2.979 |
| **bare_head** | **0,0000** | **0,0455** | **+0,0455** | **10 → 1.264** |
| **mAP50** | 0,4193 | 0,4171 | −0,0022 | |

### 2.2 Percepción — por estrato (nunca sólo el agregado)

| Estrato | imgs | mAP50 base → tuned | person | helmet | vest | bare_head |
|---|---|---|---|---|---|---|
| bench_obra_test | 62 | 0,3564 → **0,3778** | −0,0951 | −0,1069 | **+0,2576** | +0,0303 |
| bench_obra_val | 85 | 0,3780 → **0,4608** | −0,0867 | −0,0105 | **+0,1669** | **+0,2614** |
| chv | 1.330 | 0,6423 → 0,6258 | −0,0195 | −0,1232 | +0,0932 | — (sin GT) |
| shel5k | 5.000 | 0,4451 → 0,4214 | −0,0133 | −0,1034 | — (sin GT) | +0,0455 |

**El agregado esconde la historia.** Donde el ajuste hace lo que se le pidió es en **obra**:
`bench_obra_val` sube el mAP50 (+0,0828) y `bare_head` pasa de 0,000 a **0,2614**. Los dos
estratos grandes (`chv`, `shel5k`) bajan, y bajan por **`helmet`** (−0,12 y −0,10), que es lo
que arrastra el agregado hacia abajo.

### 2.3 CR-01 — recall por fuente (nunca el combinado histórico)

| Fuente | violators | detectados base → tuned | recall base → tuned |
|---|---|---|---|
| bench_obra (test+val) | 60 | 1 → **10** | 0,0167 → **0,1667** |
| shel5k | 5.248 | 0 → **1.099** | 0,0000 → **0,2094** |
| **ponderado por conteo** | 5.308 | 1 → **1.109** | 0,0002 → **0,2089** |

Es la mejora cualitativa más grande de la jornada: de detectar **un** violador en todo el banco
a detectar **1.109**. No alcanza el umbral, pero el mecanismo quedó demostrado.

## 3. T-FT-052 — el gate D-FT-12, aplicado (cerrada)

Márgenes firmados por el usuario el **2026-08-15**, `signed_before_baseline: true` y
`signed_before_any_tuned_result: true`.

**Gain gate (regla «either») — NO PASA por las dos vías:**

| Vía | Exigencia | Observado | |
|---|---|---|---|
| A | ΔAP50 absoluto de `bare_head` ≥ **0,05** | **+0,0455** | falta **0,0045** |
| B | `cr01_recall` de <0,1 a **>0,5** | 0,0002 → **0,2089** | parte bien, no llega |

**Retention gate (in-domain, regresión relativa máx. 10 %) — NO PASA por una clase:**

| | baseline → tuned | regresión relativa | |
|---|---|---|---|
| **person** | 0,7843 → 0,6932 | **+11,62 %** | **excede** |
| helmet | 0,6286 → 0,6004 | +4,49 % | ok |
| vest | 0,2642 → 0,3292 | −24,60 % (mejora) | ok |
| mAP50 | 0,4193 → 0,4171 | +0,52 % | ok |

**Veredicto: NO-GO.** El checkpoint **no se adopta** como modelo de servicio. El catálogo y el
peso promovido se conservan únicamente para reproducir esta evaluación; no se declaran modelo
de producción.

## 4. F-123.1 — el gate de latencia no se midió, y por qué no cambia nada

`D-FT-12` incluye un gate de latencia (rechazar degradación > 5 % relativo, mismo host, post-warmup).
**No se midió**, por dos razones que conviene separar:

1. **No es decisión-relevante.** Gain y retención ya fallan; ningún resultado de latencia puede
   revertir un NO-GO.
2. **La pareja no existe.** [F-120.1](120-cierre-t031-t032-baseline-26s.md#3-f-1201--nota-de-instrumento-cambio-de-energía-durante-la-corrida)
   dejó las latencias del brazo baseline **no citables** (el host pasó de batería a corriente con
   la corrida en curso). Un gate pareado exige ambos brazos en la misma condición.

Como **dato descriptivo del run** —no como evidencia de gate— el brazo tuned fue más rápido en
todos los percentiles (p50 35,55 ms, p95 52,52 ms, 25,31 fps ef.) que el brazo baseline
(p50 57,47 ms, p95 72,09 ms, 17,29 fps ef.). Hay un mecanismo plausible —el vocabulario fijo
evita el `set_classes` dinámico— pero **la comparación no es citable** por lo dicho arriba, y la
dirección favorable sólo refuerza que la latencia no era el problema. Si el informe la necesita,
se mide aparte, pareada, y se reporta como medición propia.

## 5. Cómo se cuenta este resultado

- **Es un negativo pre-registrado, no un fracaso.** Los márgenes se firmaron antes de que
  existieran la baseline y el checkpoint. Presentarlo como fracaso, o peor, moverlo de umbral
  después de ver el número, invalidaría el diseño entero.
- **La causa nunca es temporal** (criterio de invalidación 1 de ADR-017): el cómputo estuvo
  disponible, la corrida tardó 13 minutos y la jornada se ejerció completa.
- **Lo que el resultado sí demuestra:** con 3.096 parámetros entrenables (12 tensores, sólo la
  proyección de clase fusionada) el ajuste **saca `bare_head` del cero absoluto** y **mejora
  `vest` un 24,6 %** — dos de las tres debilidades que el zero-shot arrastraba. Lo que **no**
  logra es hacerlo sin costo: `person` paga 11,6 %.
- **Estas cifras son de la RAMA comparativa.** No se funden con el núcleo zero-shot ni se
  promueven a `results/`, y **no se comparan con la tabla histórica del doc 64** (protocolo
  distinto — misma advertencia que el doc 120 §2.5).

## 6. Integridad del protocolo one-shot

Dos hechos que quedan registrados porque callarlos sería peor que contarlos:

- **Un primer intento de lanzamiento abortó** al cargar el modelo (la ruta de pesos del catálogo
  es relativa al CWD y se invocó desde el workspace en vez de la raíz del media-plane). Falló
  **antes de cualquier inferencia**: se verificó que el directorio de salida no existía y que no
  se escribió ningún artefacto. **No cuenta como observación del brazo**; el tuned se evaluó
  exactamente una vez.
- **Asimetría de registro entre brazos:** la baseline declaró el prompt *inline* y en esa copia
  se perdió el campo `strategy` de cada clase; el brazo tuned lee el `.yaml` congelado que el
  protocolo fija por sha256 (verificado, `98f6e463…bad5`) y sí lo trae. **No entra al
  `PromptPlan`**: ids, textos y orden son idénticos en ambos brazos, y `_validate_fixed_plan`
  del adapter lo aceptó contra el head del checkpoint. En rigor el tuned quedó *más* apegado al
  protocolo que la baseline.

También verificado por construcción: con `fixed_vocabulary` presente, `_ensure_classes` del
adapter valida y retorna — **`set_classes` no se invoca nunca** sobre el checkpoint T1. El
contrato D-FT-08 está garantizado por estructura, no por convención.

## 7. Evidencia (sha256)

| Artefacto | sha256 |
|---|---|
| `finetuning/manifests/t1_promotion_1167640.json` | `795639f8be9f712f493d987081da72be79bd4932b0389a96215ce2aaa5ac9d99` |
| `finetuning/manifests/t1_go_no_go_1167640.json` | `e1902b0c6e445ca845ab03e9adac811a5833b018c888421cf1c85ffbf0c106b0` |
| `finetuning/manifests/t1_full_1167640_media_plane.json` | `41f79681cc27b939bf4041b29533b9891c805ec4080584d1f95554233e82c022` |
| `finetuning/configs/t1_tuned_bench_v3.yaml` | `38f594dabdc363440a7066edfd0ff343340bd2f1037930fb28f150bf526b10ce` |
| `runs/t1_yoloe26s_tuned_bench_v3/eval/artifact.sha256` | `26c6750409d027d493340a4c01dae7dcb031d36d298b6f5651268cad45c43a91` |
| checkpoint promovido `best.pt` | `5714f8339dfcf68469b27c127857d801afb5d6d556e0db0c96ce28c74bc5efbe` |
| `last.pt` (auditoría, nunca evaluado) | `2c71f82ef4140d93491d5159205204bf7c914d0134e50338dbddffdf926412e7` |

Los cuatro artefactos del protocolo (`eval_perception.aggregate/by_stratum`, `eval_cr01.by_source`,
`protocol_snapshot`) más `detections.jsonl` están hasheados dentro del `artifact.sha256` de cada
brazo. Los pesos, runs y payloads siguen git-ignored: se citan por hash, no se versionan.

## 8. Qué queda

1. **Decidir si se ejerce T2/T3.** Esta corrida es la **entrada** de la escalera
   pre-registrada, no su cierre; los go/no-go siguen gobernados por `contingencia/20` §6.
   El dato nuevo para esa decisión: el mecanismo funciona (`bare_head` deja de ser cero) pero
   con esta capacidad —linear probing, 3.096 parámetros— no alcanza y cuesta `person`.
2. **Integrar al informe** como rama comparativa: cierra `AJ-5.13` y el `[ACTUALIZAR A LA ENTREGA]`
   del borrador de §17.4 que el [doc 122](122-dia-1-pase-de-redaccion.md) §6 dejó esperando este
   resultado.
3. **Si el informe quiere latencia**, medirla pareada y aparte (F-123.1).
