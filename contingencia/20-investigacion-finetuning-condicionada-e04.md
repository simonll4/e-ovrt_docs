# Investigación condicionada E-04: fine-tuning de GDINO y YOLOE sobre el dominio EPP

- **Fecha:** 2026-07-09
- **Estado:** ✎ **2026-08-11 — PLAN DE LA JORNADA COMPROMETIDA
  ([ADR-017](../decisiones/adr-017-fine-tuning-jornada-experimental.md)).** Este doc
  nació como contingencia; ADR-017 reabrió E-04 como **jornada experimental completa
  comprometida**, así que sus recetas, presupuestos y criterios go/no-go pasan de
  contingencia a **plan pre-registrado de ejecución**. Las condiciones de entrada
  "por semanas libres" (§1/§6) quedan derogadas: la entrada es **T1 tras cerrar las
  puertas del doc 100 §6** (decisión F-100.1 incluida), y el escalamiento T2/T3 lo
  siguen gobernando los go/no-go. *Decía "FUERA DEL PLAN ACTUAL — contingencia
  armada… para que, si sobra tiempo, la rama se ejecute sin investigación previa"*.
- **Método:** análisis de activos propios (repos + informe Anexo B) + investigación
  web multi-fuente (harness de deep research: 5 ángulos, fuentes oficiales de
  OpenMMLab/MMDetection, Ultralytics, THU-MIG/yoloe y papers arXiv, con citas
  textuales). Nota de confianza: 3 afirmaciones pasaron verificación adversarial
  completa; el resto proviene de documentación oficial citada pero la ronda de
  verificación se cortó por límite de sesión — se marcan (✓) las verificadas.

## 1. Resumen ejecutivo (go/no-go en tres líneas)

> ✎ 2026-08-11 (ADR-017): las condiciones "semana(s) libre(s)" de este resumen eran
> la regla de entrada de la *contingencia* y quedaron **derogadas** — la jornada está
> comprometida. Siguen vigentes los costos estimados, los riesgos de ingeniería y los
> go/no-go técnicos de cada tier.

- **YOLOE linear probing: entrada de la jornada** — costo ~horas en una A30 y riesgo
  acotado si el freeze se demuestra. El backbone debe quedar congelado, pero el head se
  ajusta y fusiona con vocabulario fijo: la retención open-vocabulary **no está garantizada**.
  Responde una pregunta propia valiosa: ¿el ajuste rescata el hueco de `vest` de YOLOE?
- **YOLOE fine-tuning completo: GO condicional** — barato (~<1 día GPU) pero exige
  la evaluación de retención de la Tabla 32 para ser publicable.
- **MM-GDINO fine-tuning: NO-GO salvo ≥2 semanas libres** — es la rama de mayor
  ganancia potencial pero la única receta madura asume 8 GPUs, requiere adaptación
  de batch/LR a 1×A30 y armado de entorno MMDetection en el clúster: el riesgo de
  ingeniería se come el margen del deadline.

## 2. Qué tenemos ya (inventario local — todo verificado en los repos)

| Activo | Estado | Relevancia |
|---|---|---|
| Datos en formato **ODVG** (el formato de entrenamiento de MM-GDINO) | ✅ `datasets/processed/odvg/canonical_v2/{construction_site_safety,chv,ppe_siabar}` — emitidos por `convert_datasets.py`; hay además una conversión legacy que valida el pipeline | El paso que la comunidad hace con `coco2odvg.py` acá ya está hecho |
| Datos en formato **YOLO** | ✅ `processed/yolo/canonical_v2/` | Entrada directa para Ultralytics/YOLOE |
| Split de entrenamiento | ✅ `splits/v2/train.txt` = 5.540 imágenes; BENCH=196 **congelado** como eval (disjunto por construcción) | Cumple la condición de partición de la Tabla 37 |
| Baseline zero-shot | ✅ R1/Sprint 2: GDINO-tiny mAP 0.441 sobre BENCH | Prerequisito de la Tabla 37 cumplido |
| Hardware TN | ✅ Mendieta (CCAD-UNC): 2×A30 24 GB por nodo, asignación mínima 1 GPU + 10 cores + 64 GB RAM, CUDA 12.x candidato (Anexo B, Tablas B.4/B.5) | 1×A30 24 GB es el escenario a presupuestar |
| Pesos base | ✅ GDINO tiny/base, MM-GDINO t/b/l, YOLOE-26 s/m/l/x descargados en media-plane | Checkpoints de partida listos |
| Protocolo comparativo | ✅ Tabla 32 del informe (ΔAP/ΔRecall/ΔPrecision/ΔSDR + retención generalista + costo documentado) | El diseño experimental ya está escrito |

**Lectura:** la preparación de datos —que suele ser el 50% del esfuerzo de una rama
de fine-tuning— ya está amortizada. Lo que falta es solo entorno + corrida + eval.

## 3. Camino A — MM-Grounding-DINO (MMDetection)

### 3.1 Lo que dice la fuente oficial

- Es **la única vía madura** para entrenar la familia GDINO: el repo original nunca
  publicó código de entrenamiento; MM-GDINO existe precisamente para eso
  (arXiv:2401.02361).
- (✓) Los mantenedores documentan **tres modos de fine-tuning** con trade-offs
  explícitos: *closed-set* ("maximiza el rendimiento en el dominio pero **pierde la
  generalidad** open-vocabulary" — cita textual), *open-set continued pretraining* y
  *open-vocabulary fine-tuning*. Las mitigaciones documentadas: bajar LR + congelar
  módulos (el recipe de referencia congela BERT), o mezclar datos de preentrenamiento.
- **Ganancia esperable — las dos caras:**
  - (✓) Cuando el zero-shot ya es fuerte, la ganancia es **marginal**: su ejemplo
    canónico (dataset "cat") mejora 88.1 → 90.1 AP, y advierten fluctuación de
    métricas por dataset chico.
  - Cuando hay corrimiento de dominio, las ganancias reportadas son **grandes**:
    RTTS 49.8→69.1, RUOD 29.8→65.5, Cityscapes 34.2→51.5 box AP; y con schedule 1x
    el propio paper reporta saltos de dos dígitos (41.4→58.7). Nuestro 0.441 en
    BENCH está en zona intermedia: ni "ya fuerte" ni colapsado → ganancia probable
    pero no garantizada de dos dígitos.
  - Con los configs open-vocabulary dedicados, **el olvido no es inevitable**:
    reportan retención e incluso mejora en clases no vistas (COCO-OVD novel
    58.9→60.4; LVIS APr 34.2→43.2).
- **Pitfalls:** (✓) todos los recipes de referencia asumen **8 GPUs × batch 4**
  (`8xb4`) con `dist_train.sh`; no hay guía oficial single-GPU ni de VRAM — adaptar
  batch/LR corre por cuenta nuestra. Advertencia explícita de **overfitting rápido**
  en continued-pretraining sobre datasets chicos (su corrida pico en la época 3).

### 3.2 Presupuesto estimado (1×A30 24 GB)

Sin cifra oficial single-GPU, estimación de ingeniería: GDINO-tiny (Swin-T) con
batch 2–4 + acumulación de gradiente entra en 24 GB; 5.540 imágenes × 10–20 épocas ≈
**8–24 GPU-horas** de cómputo. El costo real dominante es el **entorno**: MMDetection
+ mmcv con CUDA del clúster (fricción clásica), adaptación del config, y colas de
Slurm. Estimación honesta de calendario: **1–2 semanas** de pared incluyendo
depuración. En la RTX 4060 (8 GB): no recomendable.

### 3.3 Modo recomendado si se ejecuta

**Open-vocabulary fine-tuning** (no closed-set): es el único modo cuya narrativa es
coherente con la tesis ("ajustar sin renunciar al lenguaje") y el único que permite
medir retención como pide la Tabla 32. Congelar BERT (default del recipe), LR bajo,
schedule corto (1x), eval en BENCH cada época y **early stop contra overfitting**.

## 4. Camino B — YOLOE (Ultralytics / THU-MIG)

### 4.1 Lo que dicen las fuentes oficiales

- Ultralytics da **soporte de primera clase** al fine-tuning de YOLOE sobre datasets
  YOLO: procedimiento estándar con trainer dedicado (`YOLOEPETrainer`). Gotcha
  documentado: los checkpoints preentrenados son de segmentación — para detección
  hay que inicializar desde YAML y cargar el checkpoint de la misma escala.
- **Linear probing (la joya para nuestro caso):** existe una vía oficial liviana que
  entrena **solo la última capa conv (el embedding del prompt)** (`train_pe.py`).
  En COCO: 10 épocas de linear probing vs 160 de full-tuning, alcanzando la mayor
  parte de la precisión (LP de v8-L: 45.4 AP vs full de v8-S: 45.0). El resto del
  modelo queda congelado → **la capacidad open-vocabulary no se toca**.
- Transferencia barata y sin sacrificio: YOLOE-v8-L fine-tuned supera levemente al
  YOLOv8-L cerrado (+0.6 box AP) con ~4× menos tiempo de entrenamiento. El
  preentrenamiento pesado (8×RTX 4090, 12–22 h) ya lo pagó THU; el downstream es
  single-GPU.
- `set_classes()` + RepRTA re-parametrizable = fijar vocabulario sin entrenar (lo
  que ya hacemos hoy); tras re-parametrizar, YOLOE es estructuralmente un YOLO
  cerrado → sin costo de inferencia.

### 4.2 Presupuesto estimado

- **Linear probing** (5.540 imgs, ~10 épocas, YOLOE-26s/m): **1–3 GPU-horas** en la
  A30; probablemente viable en la RTX 4060 8 GB para la variante S. Riesgo: bajo.
  Calendario: **1–2 días** incluyendo evaluación.
- **Full fine-tuning:** ~4–10 GPU-horas; exige medir retención (un full FT sobre 3–4
  clases es en la práctica un cierre de vocabulario → la Tabla 32 manda evaluar un
  subset generalista post-tuning).

### 4.3 La hipótesis propia que lo hace interesante

Sprint 2 mostró que YOLOE-26l es rápido pero **no detecta `vest`** (ni `bare_head`).
El linear probing con nuestros datos es el experimento natural: *¿10 épocas de
ajuste de embeddings rescatan la clase que el vocabulario zero-shot no trae?* Si sí,
la conclusión para la tesis es potente: "la adaptación liviana repara huecos de
vocabulario específicos sin reentrenar el modelo" — un punto intermedio entre
zero-shot y fine-tuning que enriquece los criterios de adopción del doc 09 §5.3.

## 5. Corrección de cita importante para el informe (Abdalwhab et al.)

El paper que el informe usa como evidencia de que "los OVD rinden peor que
detectores ajustados en construcción" (arXiv:2501.09267) **no fine-tunea ningún
modelo OVD**: compara un YOLO11 cerrado *fine-tuned* contra tres OVD *zero-shot*
(GDINO, Grounded-SAM2, DETIC) en componentes **MEP** (cajas de conexión, conductos —
vocabulario mucho más exótico que EPP), donde GDINO zero-shot colapsa a precisión
0.02 vs 0.87 del YOLO11 ajustado. Dos consecuencias:

1. **Precisión de cita:** el paper evidencia la *brecha de vocabulario de dominio en
   zero-shot*, no el efecto de fine-tunear OVDs. En el informe conviene citarlo así
   — y nuestro propio 0.441 en EPP (clases bien representadas en preentrenamiento
   web) es el contraste perfecto: la severidad de la brecha depende del vocabulario.
2. **Hueco en la literatura que nos favorece:** no encontramos ganancias publicadas
   de fine-tuning de GDINO/YOLOE *específicamente en EPP/construcción* — si la rama
   se ejecutara, el resultado tendría valor de novedad genuino para el nicho.

## 6. Escalera de ejecución de la jornada (✎ 2026-08-11, ADR-017 — *decía "condicionada (si aparece tiempo)"*)

Pre-condición de todas: BENCH congelado como eval (ya cumplido), tuning/hiperparámetros
del resto del pipeline congelados, y bitácora Tabla D.6.

| Tier | Qué | Costo estimado | Riesgo | Produce |
|---|---|---|---|---|
| **T1** | YOLOE-26s/m **linear probing** (10 ep, YOLO format ya listo) | 1–3 GPU-h · 1–2 días pared | Bajo si el freeze se prueba | ΔAP/ΔRecall sobre BENCH + hipótesis `vest`; backbone congelado pretendido, head fijo ajustado, sin afirmar retención open-vocabulary automática |
| **T2** | YOLOE **full fine-tuning** + eval de retención en subset generalista (COCO val u OVDEval parcial) | 4–10 GPU-h · +2–3 días | Medio | Tabla 32 completa para YOLOE (Δ + retención + costo) |
| **T3** | MM-GDINO-tiny **open-vocabulary fine-tuning** en Mendieta (ODVG ya listo; BERT congelado, 1x, early-stop) | 8–24 GPU-h · 1–2 semanas pared | Alto (entorno + adaptación 8×→1 GPU + overfitting) | La comparación estrella zero-shot vs tuned del modelo líder |

### Enmienda 2026-08-14 — clase objetivo de T1: de `vest` a `bare_head` (pre-resultado)

La pre-registración original fijaba `vest` como hipótesis de T1 (§4.3 y tabla §6).
D-FT-12 (doc 117) propone `bare_head`: es evidencia directa de CR-01 y tiene 6.181
anotaciones en `bench_v3` (vs 1.863 de `vest`). Esto cambia qué estrato carga el
resultado: `vest` no existe en `shel5k` y `bare_head` no existe en `chv`. La enmienda
es previa a cualquier entrenamiento full (0 jobs full al 2026-08-14) y queda
supeditada a la aprobación de D-FT-12 por el usuario.

✎ **2026-08-15 — la enmienda queda FIRME.** El usuario aprobó D-FT-12 sin cambios, con la
baseline T-FT-032 todavía sin correr y cero jobs full. La sustitución de `vest` por
`bare_head` es por lo tanto **pre-resultado en sentido estricto** y así debe reportarse: no
se eligió la clase objetivo después de ver un número.

**Regla de entrada** (✎ 2026-08-11, reescrita conforme ADR-017 — *decía "T1 solo si
el plan core va en fecha al inicio de la semana 9; T3 solo con ≥2 semanas libres"*):
**T1 es la entrada de la jornada comprometida**, tras cerrar las puertas del doc 100
§6 (decisión sobre F-100.1 incluida); T2 solo si T1 mostró ganancia exigible; T3 solo
si T2 la sostiene y la logística del clúster lo permite (entorno MMDetection,
adaptación 8×→1 GPU) — si los go/no-go no lo habilitan, T3 se declara trabajo futuro
**con causa técnica, no temporal**.

**Criterios go/no-go pre-registrados** (fijados ahora para no negociarlos después):

- *Ganancia exigible* (Tabla 37): ΔAP@0.5 ≥ +0.05 absoluto en BENCH sobre la clase
  objetivo, o rescate de una clase colapsada (recall pasa de <0.1 a >0.5).
- *Retención* (Tabla 32): caída ≤ 10% relativa en el subset generalista elegido cuando el
  tier conserve una interfaz comparable. T1 **sí modifica el head** y su checkpoint es de
  vocabulario fijo; no se declara exento por "no tocar el modelo" ni se afirma retención sin
  el contrato D-FT-08 y una medición aplicable.
- *Costo operativo* (Tabla 37): la variante ajustada no debe empeorar la latencia de
  inferencia en el CPN. La re-parametrización de YOLOE permite esperar neutralidad, pero la
  latencia se mide; no se toma como garantía previa.
- Si falla cualquiera → se reporta como resultado negativo con números (también
  publicable) y la rama se cierra.

## 7. Qué NO cambia por esta investigación

> ✎ **2026-08-11 — sección superada por ADR-017.** Lo tachado describía el estatuto
> de julio (E-04 excluida, este doc como anexo de preparación). Desde ADR-017, E-04
> **se ejerce como jornada comprometida** y este doc es su plan pre-registrado. La
> causa "presupuesto de tiempo" queda **derogada como encuadre**: la rama fue
> experimental y condicionada **por datos y protocolo** desde el planteo (Tabla 37,
> F-100.1, licencias) — y esta investigación lo confirma: los datos están listos y
> el TN alcanza.

- ~~**E-04 sigue excluida del plan** — este documento es su anexo de preparación, no
  su reapertura. La declaración del doc 10 se mantiene; solo se enriquece la
  "habilitación futura" con la escalera §6.~~ (derogado, ADR-017)
- ~~El won't se sigue declarando por presupuesto de tiempo (no por recursos ni datos —
  esta investigación lo confirma: los datos están listos y el TN alcanza).~~
  (derogado, ADR-017)

## 8. Fuentes principales

- MM-Grounding-DINO: `configs/mm_grounding_dino/{usage.md, dataset_prepare.md, README.md}`
  (github.com/open-mmlab/mmdetection) · paper arXiv:2401.02361.
- YOLOE: docs.ultralytics.com/models/yoloe · github.com/THU-MIG/yoloe · paper
  arXiv:2503.07465.
- Brecha zero-shot en construcción: arXiv:2501.09267 (Abdalwhab et al. — ver
  corrección de cita en §5).
- Activos locales: repos `e-ovrt_datasets` (processed/odvg|yolo, splits/v2),
  `e-ovrt_media-plane` (pesos), informe Anexo B (Tablas B.4/B.5) y Tablas 32/37.
