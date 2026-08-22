# 127 — Cierre del tier T2: promoción, evaluaciones únicas y veredicto **NO-GO** — la curva de capacidad completa (2026-08-21)

- **Contexto:** el full T2 v2 (job `1167982`, enmienda D-FT-16: SGD lr0=0,01 explícito desde
  el peso base, techo 60 épocas / patience 15) encoló el 18/08 y **corrió el 20/08** en Mendieta
  (`COMPLETED` exit 0, 26m10s en una A30, nodo ivb14). Este doc cierra T-FT-065 (promoción),
  T-FT-066 (evaluaciones únicas de los dos brazos + go/no-go D-FT-15) y con ellas **la escalera
  completa de la jornada** que autorizó [ADR-017](../decisiones/adr-017-fine-tuning-jornada-experimental.md):
  T1 NO-GO ([`123`](123-cierre-jornada-t1-no-go.md)) · T2 NO-GO (este doc) · T3 cerrado con causa
  técnica (doc `117` §2).
- **Antecedentes directos:** [`123`](123-cierre-jornada-t1-no-go.md) (cierre T1) y doc `117` §3
  (diseño D-FT-14/15/16). El job intermedio `1167864` (`optimizer=auto`, submuestreado por el LR
  ciego al conteo de parámetros — verificado en `BaseTrainer.build_optimizer` de ultralytics
  8.4.86) quedó como **evidencia del hallazgo del LR, no candidato**; sus 10 épocas se citan como
  segundo régimen de la curva, nunca como brazo evaluado.
- **Regla heredada del doc 119:** ninguna fila de evidencia sin haber corrido el comando.
  Todo lo de abajo fue ejecutado y observado el 2026-08-21.

> **Veredicto: NO-GO.** El gate de ganancia **PASA** (`bare_head` 0,0000 → **0,0909**, umbral
> +0,05 — el doble de lo que logró T1) pero las **dos retenciones fallan de forma catastrófica**:
> in-domain −40,6 % a −65,6 % en las tres clases protegidas (tope 10 %) y open-vocabulary
> **−71,3 %** (mAP50 COCO 0,4347 → 0,1247, umbral 0,3912). Las tres expectativas pre-registradas
> en el protocolo (§`preregistered_expectation`, firmado 17/08 con cero cifras tuned) **se
> confirmaron una por una**. Un negativo así es resultado, no fracaso (ADR-017), y este cierra
> la pregunta que T2 existía para responder.

---

## 1. El entrenamiento colapsó, y eso es parte del dato

`EarlyStopping` cortó en la época **16/60** con `best_epoch = 1`: el mejor checkpoint es el
**menos entrenado** (una época a LR de warmup ≈0,0033, un tercio del lr0). En cuanto el LR llegó
a 0,01 pleno (épocas 2–6) la validación interna se derrumbó (mAP50-95 0,084 → 0,018) y la
recuperación que siguió al decay lineal se estancó en ~0,03, sin pendiente de retorno — el corte
por patience no robó nada. `train/cls` casi no bajó (7,06 → 5,53): la cabeza de clasificación
por embeddings de YOLOE apenas aprendió antes de romper el alineamiento visual-texto.

Con esto, los dos regímenes de full FT quedan **acotados por ambos lados**:

| Régimen | Job | Trayectoria interna (mAP50-95) |
|---|---|---|
| AdamW auto (lr=0,00125, ciego a los 10,35M params) | `1167864` | sube monótono pero lentísimo: 0,031 a las 10 épocas |
| SGD estándar (lr0=0,01, punto de diseño de batch efectivo 64) | `1167982` | destruye desde la época 2; meseta ~0,03 |

Ambos convergen al mismo lugar, **~6× peor que el linear probing de T1 (0,190)** sobre los
mismos datos. El contrato estructural se cumplió exacto en las dos corridas (390 tensores /
10.350.308 params entrenados; `reprta`/`savpe` congelados, 42/3.426.528) y el run declaró
`open_vocabulary_preserved` — el diseño funciona; lo que no alcanza son los datos: 2.946
imágenes de train para 10,35M de parámetros.

## 2. T-FT-065 — promoción del checkpoint (cerrada)

Regla 7 de `finetuning/README.md` (integridad, binding, serving smoke), ejecutada antes de
copiar nada. Constancia: `finetuning/manifests/t2_promotion_1167982.json`.

| Requisito | Cómo se verificó | Resultado |
|---|---|---|
| Integridad | backup por tar vía SSH (sha256 del tar idéntico en ambos extremos, `73a9a822…`); `best.pt`/`last.pt`/`results.csv` contra `eovrt_run_manifest.json` del postcheck remoto | coincide byte a byte |
| Binding de clases | `torch.load` del checkpoint | `{0: person, 1: helmet, 2: vest, 3: bare head}`; `train_args` confirma SGD lr0=0,01; interfaz OV en el state_dict (68 tensores savpe, 4 reprta) |
| Serving smoke | run offline DBE de 2 imágenes vía `run_pipeline` (mismo camino que los brazos) | 4 detecciones, 0 errores, cuda, `set_classes` con el prompt set congelado |

- Backup local: `finetuning/weights/finetuned/full-1167982/` (27 archivos, `MANIFEST.sha256`
  verificado limpio — generado **sin** carrera de auto-listado, lección del doc del 18/08).
- Destino: `e-ovrt_media-plane/models/yoloe/finetuned/t2/best.pt`
  (sha256 preservado `a3c482ac…`).
- Catálogo nuevo: `configs/models/yoloe/yoloe-26s-ft-t2.yaml` — **sin `fixed_vocabulary`**:
  el checkpoint T2 NO hereda D-FT-08 y se sirve open-vocabulary vía `set_classes`, como el
  brazo baseline (protocolo §`serving`).
- Driver reproducible: `finetuning/scripts/run_offline_media_plane.py` (el camino in-process
  `load_run_config` → `run_pipeline` con que se produjeron todos los brazos, ahora como comando).

## 3. T-FT-066 — corridas únicas de los dos brazos (cerradas)

Regla one-shot respetada: **una** corrida y **una** evaluación por brazo; `last.pt` jamás fue
segundo candidato. Este fue **el último brazo contra `bench_v3`** de la rama FT.

| Brazo | Run | Cobertura | Evaluación congelada |
|---|---|---|---|
| in-domain `bench_v3` | `finetuning/runs/t2_yoloe26s_tuned_bench_v3` | 6.477/6.477, 0 drops, 0 errores, 41.729 det, 197 s | `evaluate_t1_bench_v3.py --arm tuned` (insumos sha256 OK) |
| retención OV COCO | `finetuning/runs/t2_coco_retention_tuned` | 5.000/5.000, 80/80 clases, 0 errores, 20.511 det, 117 s | `evaluate_t2_coco_retention.py --arm tuned` (GT+prompts sha256 OK) |

Las configs de ambos runs son espejos exactos de sus brazos de referencia (T1-tuned y
retención-base): la única variable es `model.ref: yoloe/yoloe-26s-ft-t2`.

### 3.1 Percepción — agregado (mAP50 0,4193 → **0,2374**)

| Clase | baseline | T1 | **T2** | Δ T2 vs baseline |
|---|---|---|---|---|
| person | 0,7843 | 0,6932 | **0,3943** | −49,7 % |
| helmet | 0,6286 | 0,6004 | **0,3734** | −40,6 % |
| vest | 0,2642 | 0,3292 | **0,0909** | −65,6 % |
| `bare_head` | 0,0000 | 0,0455 | **0,0909** | **+0,0909** |
| mAP50 | 0,4193 | 0,4171 | **0,2374** | −43,4 % |

### 3.2 Percepción — por estrato (nunca sólo el agregado)

| Estrato | mAP50 | `bare_head` |
|---|---|---|
| bench_obra_test | 0,2196 | **0,0** |
| bench_obra_val | 0,1312 | **0,0** |
| chv | 0,3725 | n/a |
| shel5k | 0,2826 | **0,0909** |

⚠ **La ganancia agregada de `bare_head` proviene íntegramente de `shel5k`** (99 detecciones
sobre 6.181 GT); en los dos estratos de obra quedó en cero. Reportarla siempre así.

### 3.3 CR-01 — recall por fuente (nunca el combinado histórico)

| Fuente | baseline | T1 | **T2** |
|---|---|---|---|
| bench_obra | 0,0167 | 0,1667 | **0/60 = n/d** |
| shel5k | 0,0000 | 0,2094 | **0,0055** (29/5.248) |
| ponderado | 0,0002 | 0,2089 | **0,0055** |

### 3.4 Retención open-vocabulary (la medición central del tier)

**mAP50 COCO val2017: 0,4347 (base congelada) → 0,1247 — erosión del 71,3 %**, siete veces el
tope del 10 % (umbral NO-GO 0,3912). Una sola época de full FT a LR de warmup ya destruyó el
71 % de la capacidad open-vocabulary. Vara **interna**: jamás compararla con benchmarks COCO
publicados.

## 4. El gate D-FT-15, aplicado

| Gate | Regla | Resultado |
|---|---|---|
| Ganancia (either) | ΔAP50 `bare_head` ≥ +0,05 **o** rescate recall <0,1→>0,5 | **PASA** por el delta (+0,0909); el rescate falla (0,0055) |
| Retención in-domain | regresión relativa ≤10 % en person/helmet/vest/mAP50 | **FALLA ×4** (−49,7 / −40,6 / −65,6 / −43,4 %) |
| Retención OV | mAP50 COCO ≥ 0,3912 | **FALLA** (0,1247, −71,3 %) |
| Latencia | ≤5 % pareada | **No se midió** — dos gates ya fallan y no puede revertir el veredicto (mismo criterio que F-123.1); queda medible a pedido como dato descriptivo (sesión pareada de 3 brazos, con corriente) |

**Veredicto: NO-GO.** El checkpoint **no se adopta**; catálogo y peso se conservan sólo para
reproducir. El modelo de servicio sigue siendo el campeón zero-shot (`gdino-tiny-560`).

## 5. F-127.1 — la respuesta a la pregunta pre-registrada: es estructural

La pregunta de D-FT-14 era si el NO-GO de T1 es **artefacto de capacidad** del linear probing
o un **trade-off estructural**. La curva de tres puntos —el valor declarado del tier— responde:

| Brazo | Params entrenados | `bare_head` AP50 | mAP50 bench | mAP50 OV COCO | recall CR-01 | person |
|---|---|---|---|---|---|---|
| baseline | 0 | 0,0000 | 0,4193 | 0,4347 | 0,0002 | 0,7843 |
| T1 (linear probing) | 3.096 | 0,0455 | 0,4171 | n/m (head fusionado) | 0,2089 | −11,6 % |
| T2 (full FT, best=ep1) | 10.350.308 | 0,0909 | 0,2374 | 0,1247 | 0,0055 | −49,7 % |

**Más capacidad compra más `bare_head` pagando destrucción in-domain y OV creciente.** Con
×3.343 de capacidad y dos regímenes de optimizador probados (ambos con elecciones con
principios, pre-registradas: el default del framework y el default documentado de SGD en su
punto de diseño), el full FT empeora todo salvo la clase objetivo. El límite no era el head de
T1: es el **volumen de datos** (2.946 imágenes de train). Flanco honesto para el informe: un LR
intermedio no se exploró — quedó fuera del presupuesto pre-registrado, y aun un full FT bien
entrenado tendría que superar gates que el brazo mejor comportado (T1) ya falló.

Nota fina para la redacción: T1 y T2 **no ganan por la misma vía** — T1 rescata recall CR-01
(0,2089) con poca AP; T2 logra AP (0,0909, sólo shel5k) con recall casi nulo (0,0055). La curva
es de trade-offs, no de una métrica única.

## 5-bis. F-127.2 — la erosión OV es global, no selectiva (análisis post-cierre de artefactos ya producidos)

Análisis por clase de las dos evaluaciones de retención **ya corridas** (base vs tuned, 80
clases; cero corridas nuevas — sólo lectura de `eval_retention.aggregate.json` de ambos
brazos, 2026-08-21). El patrón descarta la hipótesis del "trade selectivo" (sacrificar
clases lejanas para comprar las cercanas al dominio):

- De las **79 clases con base > 0,05**, sólo **1** retiene ≥90 % de su AP50 (`toaster`,
  0,27→0,25 — ruido); **69 pierden más de la mitad**. Seis caen a exactamente 0.
- Las que más pierden en absoluto son las que mejor andaban: `cat` 0,793→0,045,
  `bear` 0,628→0,000, `giraffe` 0,787→0,179, `dog` 0,670→0,091.
- **Hasta `person` — clase DE entrenamiento — se erosiona en COCO**: AP50 0,647→0,356,
  recall 0,705→0,412. Coherente con su caída in-domain en bench (−49,7 %): una época de
  full FT a LR de warmup ya produce **deriva global del alineamiento visual-texto**, no un
  reacomodo hacia el dominio objetivo.
- Cierra también la intención de la sonda D-FT-13 (`machinery`): la pregunta "¿sigue
  detectando clases nuevas?" quedó medida por el instrumento más fuerte disponible (80
  clases COCO con AP50); la respuesta es "apenas" (mAP50 0,1247). El
  `open_vocabulary_check` del run (6 clases, interfaz) verificó que el **mecanismo**
  `set_classes` sobrevive; esta medición muestra que la **capacidad** detrás casi no.

Lectura para el informe: refuerza F-127.1 — el full FT en este volumen de datos no
intercambia capacidad, la **destruye en todas direcciones**, incluidas las clases que está
viendo en el train set.

## 6. Integridad del protocolo one-shot

- Márgenes D-FT-15 firmados 17/08; enmienda D-FT-16 firmada 18/08 **pre-resultado** (con
  `1167979`/`1167980` cancelados en PD sin gastar GPU); primera cifra tuned observada: 21/08.
- Los dos one-shot quedaron **consumidos**; prohibiciones post-observación vigentes (no
  re-correr, no cambiar umbrales, no elegir otro checkpoint, no renegociar márgenes).
- Insumos verificados por sha256 en ambas evaluaciones (evaluador, bench COCO, estratos,
  GT CR-01, GT COCO, prompt sets congelados `98f6e463…` y `07455877…`).
- La secuencia completa **se declara** en el informe: NO-GO T1 → D-FT-14 → D-FT-15 →
  submuestreo `1167864` → D-FT-16 → RUN `1167982` → NO-GO. Nunca presentar T2 como reintento.

## 7. Evidencia (sha256)

| Artefacto | Ubicación | Hash |
|---|---|---|
| `best.pt` (T2) | `finetuning/weights/finetuned/full-1167982/weights/` y `media-plane/models/yoloe/finetuned/t2/` | `a3c482acdca1ad5f6ce03978b0e4737e307f47b3a42f3ac3b8271ac4d9c16eea` |
| `last.pt` (auditoría, jamás evaluado) | `finetuning/weights/finetuned/full-1167982/weights/` | `2b70ba8ba00d06bbff19119e3d996e63315b41f5ce487ae63aa9fd7bc0f9b3d1` |
| Manifiesto del run remoto | `full-1167982/eovrt_run_manifest.json` | `status=succeeded`, `early_stopped=true`, `best_epoch=1` |
| Promoción | `finetuning/manifests/t2_promotion_1167982.json` | — |
| Go/no-go | `finetuning/manifests/t2_go_no_go_1167982.json` | — |
| Eval bench | `finetuning/runs/t2_yoloe26s_tuned_bench_v3/eval/artifact.sha256` | hashes de los 4 artefactos + detections |
| Eval retención | `finetuning/runs/t2_coco_retention_tuned/eval/artifact.sha256` | ídem |
| Catálogo T2 | `media-plane/configs/models/yoloe/yoloe-26s-ft-t2.yaml` | `e66ba1bc9da82de941facf5f6b45dd430d85795beb0c88a5a7da350c2a6bf23f` |

## 8. Qué queda

- **La jornada E-04 está COMPLETA**: T1 NO-GO (123) · T2 NO-GO (este doc) · T3 cerrado con
  causa técnica. No hay más brazos contra `bench_v3`.
- Latencia pareada de los 3 brazos: **opcional**, sólo si el informe la quiere como dato
  descriptivo (requiere sesión con corriente; no cambia ningún veredicto).
- Propagación pendiente de redacción: doc `117` (tablero de decisiones, estado D-FT-15/16),
  ficha E-04 de `nucleo/10`, estado de ADR-017, síntesis y GUIA-REDACTORES (la curva de 3
  puntos reemplaza al "T2 en curso").
- Los resultados van al informe como **rama comparativa** con tablas propias, por estrato,
  nunca fundidos con el núcleo zero-shot ni comparados con el doc 64.
