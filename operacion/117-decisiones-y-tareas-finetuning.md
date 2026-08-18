# 117 — Decisiones y tareas de fine-tuning (2026-08-13)

- **Estado:** ✎ **2026-08-17 — JORNADA T1 CERRADA. Veredicto D-FT-12: NO-GO**
  ([doc 123](123-cierre-jornada-t1-no-go.md)). T-FT-043/044/050/051/052 `done`: el full corrió
  (job `1167640`, `COMPLETED`, 10/10 épocas), el checkpoint se promovió por hash y se evaluó
  **una sola vez** contra `bench_v3`. `bare_head` AP50 **0,0000 → 0,0455** y recall CR-01
  **0,0002 → 0,2089**, pero el gain gate pedía +0,05 (faltó **0,0045**) o recall >0,5, y
  `person` cayó **−11,62 %** sobre un tope de 10 %. El checkpoint **no se adopta**.
  > **Trampa de lectura: hay dos «NO-GO» distintos en este doc.** El de arriba es el
  > **veredicto científico** de D-FT-12 sobre el resultado. El que aparece más abajo en el
  > histórico —«NO-GO para T1 completo»— era la **puerta de autorización** previa al envío, y
  > quedó **levantada** el 2026-08-15 al emitirse `full-authorization.json`. No confundirlos:
  > el primero es un resultado, el segundo era un permiso.

  Antecedentes (histórico, sin cambios): freeze, smoke corregido, dual gate y serving técnico
  verdes; T-FT-023 congeló la procedencia; el 2026-08-15 el usuario firmó D-FT-08, D-FT-12 y
  D-FT-13 (§3) y se cerraron T-FT-031/032 con la baseline one-shot (doc 120).

  ✎ **2026-08-17 (misma jornada, después del veredicto) — ENMIENDA D-FT-14: T2 se reabre
  como tier EXPLORATORIO; T3 confirmado trabajo futuro.** Tras revisión crítica pedida por el
  usuario, la escalera se enmienda por la vía que D-FT-03 prevé (enmienda explícita): el
  NO-GO de T1 queda **intacto** como resultado confirmatorio, y T2 se ejecuta para responder
  una pregunta nueva — *¿el fallo de T1 es artefacto de capacidad del linear probing o es
  estructural?* — con **pre-registración propia (D-FT-15, pendiente de firma) emitida antes
  de cualquier resultado T2**. La transparencia es total por construcción: la enmienda es
  post-resultado-T1 (se declara) y pre-resultado-T2 (que es lo que valida a T2). **T2 será el
  último brazo admitido contra `bench_v3`** — la puerta de comparaciones múltiples se cierra
  con él. T-FT-060 pasa a `in_progress`; T-FT-070 (T3) se cierra como **trabajo futuro con
  causa técnica**: sin baseline MM-GDINO geométricamente sana el Δ es ininterpretable, y
  producirla es arqueología de entorno de 1–2 semanas contra el reloj de la defensa — el
  bloqueo no es de cómputo.
- **Plan rector:** [`116-plan-maestro-finetuning.md`](116-plan-maestro-finetuning.md).
- **Regla:** una tarea puede estar descrita antes de su decisión, pero no pasa a `ready` ni se
  ejecuta mientras su dependencia metodológica siga abierta.

## 1. Convenciones

Estados de decisión: `propuesta`, `aprobada`, `rechazada`, `diferida`, `superada`.

Estados de tarea: `blocked`, `ready`, `in_progress`, `done`.

Las decisiones D-FT-01…D-FT-06 conservan los ids del relevamiento del 2026-08-12. Las nuevas
decisiones continúan desde D-FT-07.

## 2. Hechos verificados sobre datasets y antecedentes

Revisión local y remota del 2026-08-13:

- `origin/main` de `e-ovrt_datasets` termina en `f5d3e4e` (2026-06-16) y es ancestro de la
  rama actual, que contiene 28 commits posteriores. No hay que fusionar ni hacer cherry-pick
  para recuperar ese antecedente.
- El manifiesto histórico `cr01_cr02` tenía 15.845 imágenes y su vista curada de fine-tuning
  13.827. Usaba CHV, Construction-PPE, SH17 y SHEL5K con las clases v1
  `person/helmet/vest/no_helmet`.
- Ese corpus no es compatible con el contrato vigente: CHV y SHEL5K integran `bench_v3`, y
  SH17 convertía `head`/`face` en `no_helmet`. `canonical_v2` prohíbe derivar `bare_head` de
  esa forma.
- Son reutilizables como referencia el esquema de manifiesto, los hashes, la trazabilidad, los
  resúmenes y parte de la serialización COCO/YOLO/ODVG. No lo son los archivos derivados, el
  conjunto de fuentes, los mapeos ni los splits históricos.
- El control por basename/stem usado en el prototipo actual es insuficiente. Al normalizar el
  linaje Roboflow aparecen 5 progenitores compartidos entre CSS train y `bench_obra`, que
  representan 25 imágenes aumentadas dentro del train candidato.
- PPE Siabar tampoco conserva independencia entre sus splits: 188 linajes aparecen en train y
  val y afectan 215 de las 326 imágenes de ese `val`; muchas parejas son visualmente idénticas
  o casi idénticas aunque sus bytes difieran.

Estos hechos invalidan los conteos 3.723 train + 326 val como contrato de lanzamiento. Siguen
siendo una estimación histórica útil, no el split que debe materializarse.

Actualización T-FT-003/T-FT-010 del 2026-08-13:

- El auditor versionado comprobó 4.210 candidatas (CSS train + PPE completo) contra las 6.477
  imágenes del `bench_v3`, cuya huella permaneció
  `4557024ecc4ee497ab1fad01d6819206395c10fd794010ed8c1d9198b19a4462`.
- Se excluyeron 81 candidatas relacionadas con el bench: 25 variantes de 5 linajes CSS y 56
  imágenes PPE de 29 linajes visuales compartidos con CHV.
- PPE quedó refinado por similitud visual porque sus stems genéricos no identifican siempre una
  única imagen fuente. Se eligió una representante por linaje visual, excluyendo 700 copias.
- `finetuning_v1` seleccionó 3.429 imágenes: 2.946 train y 483 val, con 1.008 y 178 grupos
  respectivamente. No comparte SHA-256, linaje ni componente entre train/val.
- `val` contiene `person=1.829`, `helmet=759`, `vest=784` y `bare_head=408`; por tanto ya existe
  un monitor independiente con cobertura de las cuatro clases sin tocar el bench.

## 3. Registro de decisiones

| Id | Decisión | Estado | Determinación o recomendación | Desbloquea |
|---|---|---|---|---|
| **D-FT-01** | Selección de checkpoint T1 | **aprobada, usuario 2026-08-13** | 10 épocas; fijar Ultralytics 8.4.86 y seleccionar `best.pt` por máximo `metrics/mAP50-95(B)` agregado sobre las 4 clases de `val`; conservar `last.pt` para auditoría | trainer y job completo |
| **D-FT-02** | Variante GDINO | **diferida** | no elegir hasta obtener una baseline MM-GDINO con geometría sana | T3 |
| **D-FT-03** | Escalera o ramas independientes | **aprobada por ADR-017** | conservar T1→T2→T3; cualquier cambio requiere enmienda explícita | orden de toda la jornada |
| **D-FT-04** | Retención T2 | ✎ **en diseño (2026-08-17, habilitada por D-FT-14)** | subset propuesto: **COCO val2017 completo** (5.000 imgs, 80 clases, prompts = nombres canónicos COCO), pipeline media-plane + evaluador congelado, mismos umbrales que los brazos bench; métrica = caída relativa de mAP50 tuned vs base. La baseline de retención (base yoloe-26s sobre COCO) se corre y congela **antes** del entrenamiento T2. Se congela junto con D-FT-15, antes del RUN | T2 |
| **D-FT-05** | Salida MM-GDINO | **diferida** | decidir conversión HF o adapter MMDetection antes del smoke T3 | T3 |
| **D-FT-06** | Recursos distribuidos T3 | **diferida** | recalcular batch global, acumulación y LR para la asignación real; no escalar a ciegas | T3 |
| **D-FT-07** | Hogar del proceso | **aprobada, usuario 2026-08-13** | `e-ovrt_experimental-setup/finetuning/`; pesos/payloads/runs locales ignorados, recetas y manifiestos versionados | organización y tareas P1–P6 |
| **D-FT-08** | Contrato serving T1 | **aprobada, usuario 2026-08-15** | tratar el head fusionado como vocabulario fijo y ordenado hasta que una prueba demuestre otra capacidad; rechazar planes incompatibles | integración y catálogo |
| **D-FT-09** | Envelope Slurm T1 | **aprobada, usuario 2026-08-13** | smoke en `short`; completo en `multi`, inicialmente 1 nodo/1 GPU/10 CPU/60 GB/2 h; validar GPU y CUDA dentro del job | jobs T1 |
| **D-FT-10** | Reutilización del antecedente | **aprobada, usuario 2026-08-13** | adoptar sólo patrones y utilidades compatibles con la plataforma vigente; adaptar, probar y mantener una única implementación canónica | diseño del kit y revisión de `main` |
| **D-FT-11** | Contrato `finetuning_v1` | **aprobada, usuario 2026-08-13** | derivar `train`/`val` propios desde CSS+PPE, por grupos de linaje y duplicado perceptual, sin copiar ni alterar `bench_v3`; objetivo 85/15 por grupos, seed 42 | builder, manifiesto y nueva F-100.1 |
| **D-FT-12** | Objetivo y márgenes go/no-go T1 | **aprobada, usuario 2026-08-15 — antes de la baseline** | `bare_head` como clase objetivo; conservar el gate ya pre-registrado ΔAP50 ≥ +0,05 absoluto o rescate de recall <0,1→>0,5; retención relativa ≤10 % y latencia local sin degradación material, con método fijado antes de la baseline | protocolo final y T-FT-032 |
| **D-FT-13** | Sonda de clase nueva (`machinery`) en T1 | **aprobada, usuario 2026-08-15** | derogar la sonda **sólo para T1** (vocabulario cerrado por D-FT-08) y reasignarla a T2/T3, de vocabulario abierto | puerta del doc 100 §6 |
| **D-FT-14** | Enmienda de escalera post-NO-GO | ✎ **aprobada, usuario 2026-08-17** | reabrir T2 como tier **exploratorio** con pre-registración propia emitida antes de cualquier resultado T2; T1 intacto; T2 = **último brazo contra `bench_v3`**; T3 confirmado trabajo futuro con causa técnica (sin baseline MM-GDINO sana; D-FT-02/05/06 siguen diferidas) | escalera completa |
| **D-FT-15** | Márgenes go/no-go T2 | ✎ **APROBADA, usuario 2026-08-17 — firmada ANTES de todo resultado T2** | detalle en §3 (sección D-FT-15). Gain y retención in-domain idénticos a D-FT-12; retención OV nueva sobre COCO val2017 (D-FT-04, **base congelada mAP50 0,434676 ⇒ umbral NO-GO 0,391208**); latencia pareada ≤5 %; expectativa pre-registrada declarada (NO-GO probable, el valor es la curva de capacidad) | protocolo T2 y T-FT-064 |

### D-FT-01 — decisión posterior al split

El monitor `ppe_siabar val` anterior no contiene `bare_head` y además comparte linajes con
train. Ya no debe tratarse como validación canónica. El nuevo `finetuning_v1/val` superó los
gates de independencia y cobertura; con esa evidencia el usuario aprobó D-FT-01 el
2026-08-13.

Verificación local del 2026-08-13: el entorno vigente del media-plane usa Ultralytics 8.4.86;
`YOLOEPETrainer` hereda `DetectionTrainer`, crea `DetectionValidator` y su fitness de detección
es exactamente `metrics/mAP50-95(B)`. Por eso la selección propuesta no depende de una fórmula
implícita ni excluye `bare_head` del promedio.

La regla aprobada es:

1. mantener las 10 épocas pre-registradas;
2. fijar Ultralytics 8.4.86 en el entorno T1 y seleccionar `best.pt` por el máximo
   `metrics/mAP50-95(B)` agregado sobre `person/helmet/vest/bare_head`, sin consultar el bench;
3. conservar siempre `last.pt` y el historial completo para auditoría;
4. evaluar `best.pt` una única vez contra `bench_v3`; `last.pt` queda como artefacto auditable,
   no como segundo candidato post hoc.

La existencia de `bare_head` en CSS train permite construir un `val` con cobertura sin tocar
SHEL5K ni ninguna parte del benchmark.

El usuario autorizó preparar el stack completo y ejecutar un smoke remoto antes de las 10
épocas. Se adopta la regla recomendada porque el nuevo `val` ya cubre las cuatro clases y el
smoke necesita ejercer exactamente el trainer que luego ejecutará T1; esta autorización no
habilita por sí sola el job completo.

### D-FT-08 — aprobada por el usuario el 2026-08-15

Se aprobó la recomendación **sin cambios**. Queda como contrato vigente y T-FT-005 pasa a `done`.

La evidencia técnica ya permite formular el contrato sin suposiciones: el checkpoint fusionado
expone un vocabulario fijo y ordenado. La recomendación es aprobar los ids canónicos
`[person, helmet, vest, bare_head]`, enlazados en ese orden a los nombres internos
`[person, helmet, vest, "bare head"]`; media-plane debe rechazar cualquier diferencia de ids,
nombres u orden y no puede invocar `set_classes()` sobre el checkpoint T1. Este contrato no
afirma retención open-vocabulary: limita explícitamente lo que el artefacto puede servir y
evaluar.

### D-FT-12 — aprobada por el usuario el 2026-08-15, antes de la baseline

Se aprobaron los márgenes **sin cambios**. La firma es anterior a T-FT-032 (baseline YOLOE-26s,
`blocked` en la fecha de la firma) y a cualquier corrida full: **la pre-registración conserva su
valor**, y así debe reportarse en el informe. Con esto queda cerrada la enmienda de
`contingencia/20` §4.3/§6 que cambió la hipótesis de `vest` a `bare_head`, que estaba supeditada
a esta firma.

La clase objetivo propuesta es `bare_head`: es evidencia directa de CR-01, tiene 6.181
anotaciones en `bench_v3` y la familia YOLOE medida colapsó en esa clase. La ganancia exigible
no es nueva: se conserva la Tabla 37, ΔAP50 ≥ +0,05 absoluto o rescate de recall desde <0,1 a
>0,5. Para volver ejecutable la regla de retención, se propone medir `person`, `helmet` y `vest`
con el mismo protocolo y no aceptar una caída relativa superior al 10 % ni agregada ni en una
clase individual. La latencia se compara en el mismo host/runtime después de warmup; se propone
tratar hasta 5 % relativo como tolerancia instrumental y rechazar una degradación mayor. Estos
márgenes deben aprobarse o corregirse antes de ejecutar la baseline; no se completan en el
manifiesto por inferencia. ✎ 2026-08-15: aprobados sin corrección, con la baseline aún sin correr.

Esta decisión constituye una **ENMIENDA** a la pre-registración de `contingencia/20`
§4.3/§6, registrada allí el 2026-08-14: la hipótesis original era `vest`.

La retención propuesta aquí es in-domain (`person`/`helmet`/`vest` en `bench_v3`):
T1 no mide retención open-vocabulary generalista por su contrato de vocabulario fijo.

### D-FT-13 — sonda de clase nueva (`machinery`) para T1 — aprobada, usuario 2026-08-15

El doc 100 §6.2 listaba el GT de `machinery` del doc 94 como sonda. Ese ítem no es
aplicable al artefacto T1: D-FT-08 fija vocabulario cerrado y ordenado y prohíbe
`set_classes()`; una clase externa no puede ejercitarse sobre ese checkpoint. Se
derogó la sonda **sólo para T1** y se reasignó a T2/T3, de vocabulario abierto.

✎ **2026-08-15: firmada.** La puerta del doc 100 §6 queda **cerrada en este ítem**. La
derogación es alcance-específica: no toca T2/T3, donde la sonda sigue siendo exigible, y
depende de D-FT-08 — si ese contrato se revisara, esta derogación pierde su premisa y debe
reabrirse.

### D-FT-14 — enmienda de escalera post-NO-GO — aprobada, usuario 2026-08-17

El veredicto NO-GO de T1 activó el cierre mecánico de la escalera (`contingencia/20` §6,
constancia en su adenda). El usuario pidió revisión crítica y decidió, por la vía de enmienda
explícita que D-FT-03 prevé: **T2 se reabre como tier exploratorio**, no como reintento de T1.

- **Pregunta que T2 responde** (T1 la deja abierta): ¿el fallo es artefacto de capacidad del
  linear probing (3.096 params) o el trade-off ganancia/retención es estructural? Cualquier
  desenlace suma: si T2 pasa ganancia y rompe retención, la curva de tres puntos (zero-shot →
  probe → full) demuestra que el costo es estructural; si pasa todo, se reporta el GO bajo su
  vara pre-registrada.
- **Qué protege la validez:** T1 intacto (su NO-GO es el resultado confirmatorio y no se
  re-corre); márgenes T2 (D-FT-15) firmados **antes** de cualquier resultado T2; `bench_v3`
  sigue one-shot por brazo y **T2 es el último brazo admitido** contra este bench; la
  secuencia temporal (enmienda post-T1, pre-T2) se declara en el informe, no se disimula.
- **T3 confirmado trabajo futuro con causa técnica:** el bloqueo no es de cómputo — sin
  baseline MM-GDINO geométricamente sana (Sprint 2 descartó la tiny por bboxes rotos, causa
  nunca diagnosticada) el Δ de T3 no se puede interpretar, y el linaje tuneado ni siquiera
  sería el del campeón desplegado (`gdino-tiny-560` HF). D-FT-02/05/06 quedan diferidas.

### D-FT-15 — márgenes go/no-go T2 — **APROBADA, usuario 2026-08-17**

> ✎ **Firmada el 2026-08-17, y lo que importa de esa fecha: es DESPUÉS del resultado de T1
> (que la enmienda D-FT-14 declara abiertamente) y **ANTES de todo resultado T2** — no
> existía el checkpoint T2 ni ninguna cifra suya; el único job T2 enviado hasta acá era el
> smoke técnico `1167862`, que no produce cifra citable. La baseline de retención OV ya
> estaba corrida y **congelada** (mAP50 0,434676, `t2_coco_retention_base_frozen.json`), así
> que el umbral de retención quedó fijado en **0,391208** antes de existir el brazo tuned.
> Aprobada **sin correcciones**, incluida la expectativa pre-registrada del punto 6.



Espejo de D-FT-12 más la retención OV que T1 no podía medir. **Contrato de comparabilidad:**
mismos datos (`finetuning_v1`, 2.946/483), mismas 10 épocas, mismo `imgsz` 640/batch 8/seed
100/ultralytics 8.4.86, mismo protocolo bench; la **única variable vs T1 es el alcance
entrenable** (pesos de detección completos vs proyección de clase fusionada; text encoder
congelado, inventario exacto de tensores congelado en el perfil por preflight antes del RUN,
como en T1). El brazo bench de T2 sirve por `set_classes` con las frases fijadas (modo
baseline): el checkpoint T2 conserva la interfaz OV — no hereda el contrato de vocabulario
fijo D-FT-08, que es específico del head fusionado de T1.

1. **Gain gate** (idéntico a D-FT-12): ΔAP50 de `bare_head` ≥ +0,05 absoluto agregado sobre
   la baseline T-FT-032, **o** rescate de recall CR-01 ponderado <0,1 → >0,5.
2. **Retención in-domain** (idéntica): caída relativa ≤10 % por clase (`person`/`helmet`/
   `vest`) y en mAP50 agregado, sobre `bench_v3`.
3. **Retención OV** (nueva, D-FT-04): mAP50 sobre COCO val2017 (80 clases) tuned vs base
   yoloe-26s, mismo pipeline y evaluador; **gate de adopción ≤10 % relativa**. Una erosión
   mayor implica NO-GO **y es a la vez la medición central del tier** (completa la Tabla 32):
   se reporta con el mismo peso que un GO.
4. **Latencia**: pareada, ambos brazos con corriente, post-warmup, misma sesión; degradación
   >5 % relativa se rechaza (ahora medible: no arrastra la trampa F-120.1).
5. **Selección y one-shot**: `best.pt` por `mAP50-95(B)` sobre `finetuning_v1/val` (D-FT-01);
   `last.pt` sólo auditoría; brazo bench evaluado **exactamente una vez**.
6. **Expectativa pre-registrada** (se firma junto con los márgenes, para que nadie pueda
   decir que se persiguió un GO): lo más probable es que el gain gate **pase**, la retención
   in-domain quede **en riesgo** (T1 rompió `person` moviendo sólo el head; full FT mueve
   más) y la erosión OV sea **sustancial** ⇒ **NO-GO probable**. El valor declarado del
   experimento es la curva capacidad/retención y el cierre de la objeción de capacidad
   contra T1 — no el GO.

### D-FT-07 — alcance de la centralización

La carpeta `finetuning/` es la fuente operativa del proceso, no una copia indiscriminada de
los repos hermanos:

- los payloads se derivan de `e-ovrt_datasets` y llevan manifiesto;
- los pesos base se materializan localmente por tarea y se identifican por hash;
- los checkpoints nuevos viven primero en `finetuning/weights/finetuned`;
- sólo un peso que pase integridad y serving se copia a `e-ovrt_media-plane/models/...` y se
  registra en su catálogo;
- `docs/operacion` conserva las decisiones y evidencia citable.

### D-FT-10 — criterio de reutilización

Para incorporar una pieza anterior deben cumplirse todos estos puntos:

1. responde a una necesidad del plan actual, no sólo a una estructura histórica;
2. consume `canonical_v2` o implementa una frontera explícita hacia él;
3. respeta el contrato de anotación, especialmente la procedencia de `bare_head`;
4. no introduce datos, clases o decisiones incompatibles con `bench_v3`;
5. es portable, parametrizable y queda cubierta por tests;
6. no crea una segunda implementación divergente en otro repositorio.

Aplicación concreta: se pueden adaptar helpers de manifiestos/exportación de `main`, pero el
builder de splits y los guards de leakage deben ser nuevos o sustancialmente endurecidos.

### D-FT-11 — contrato aprobado de datasets y splits

Se aprueba un split derivado y aislado:

1. candidatos: `construction_site_safety/train` y los splits canónicos disponibles de
   `ppe_siabar`;
2. exclusiones duras: CHV, SHEL5K, cualquier fila del bench y cualquier linaje relacionado con
   una fila del bench; actualmente se conocen 5 linajes CSS/25 variantes afectadas;
3. reagrupar PPE completo antes de dividir, porque sus splits de origen no son independientes;
4. construir grupos por SHA-256, linaje Roboflow normalizado y similitud perceptual;
5. asignar grupos, nunca imágenes sueltas, con seed 42 y objetivo 85 % train / 15 % val;
6. estratificar por dataset y presencia multiclase; `val` debe contener
   `person/helmet/vest/bare_head`;
7. colapsar copias equivalentes donde sólo agreguen re-encoding; las augmentaciones que se
   conserven permanecen siempre en el mismo grupo y se declaran en el manifiesto;
8. no crear un tercer split: `bench_v3` conserva el rol de test externo final;
9. materializar todo bajo `experimental-setup/finetuning`, dejando intactas las fuentes.

Los porcentajes se calculan sobre grupos, por lo que el conteo de imágenes puede apartarse del
85/15. El builder debe reportar ambas distribuciones y fallar si no cumple disjunción o cobertura.

### Actualización de staging y smoke — 2026-08-13

- payload autocontenido: 2.946 train + 483 val, sin symlinks ni contenido del bench;
- activos base verificados: `yoloe-26s-seg.pt`, `mobileclip2_b.ts` y el activo offline del
  chequeo AMP `yolo26n.pt`, con tamaño y SHA-256;
- bundle usado por el smoke: 6.877 archivos declarados, hash raíz
  `3f62f567695793f9f9ec5b057e9c1ef47194e6772c050572a147383fe13e6ed8`;
- bundle con activo AMP: 6.883 archivos declarados, hash raíz
  `a60ded79384e2ab4464a1a8f2290d3ad61f80e63e763ec1e437d3aeedfb687db`. Agrega el gate
  firmado por los insumos críticos del smoke y el wrapper de envío manual, sin modificar
  configuración, trainer, payload, pesos ni imagen ejercidos por la prueba;
- directorio remoto: `~/eovrt-finetuning/t1-yoloe26s-20260813`;
- el primer bootstrap `1166382` obtuvo una A30 pero falló antes de entrenar: el nodo de cómputo
  no pudo alcanzar Docker Hub (`i/o timeout`, 58 s, 0 checkpoints). La ruta quedó descartada;
- la SIF se construyó desde el login con conectividad y base fijada por digest. Mide
  3.546.914.816 bytes, SHA-256 `958cabd60f4daadd886944e682b2679bda87dea7e7d89fc1eb266854599f1cc1`,
  y su preflight de carga confirmó Python 3.11.11, Torch 2.6.0+cu124/CUDA 12.4 y Ultralytics
  8.4.86;
- `1166456` se canceló todavía pendiente (`Elapsed=0`) después de reducir el límite a 15 min:
  una consulta `--test-only` anunció una ventana más temprana que Slurm no materializó al
  reenviar. No hubo asignación ni consumo GPU;
- `1166465` recibió una A30 y validó CUDA, pesos y configuración, pero terminó `TIMEOUT` tras
  5:22, antes de entrenar: el chequeo AMP de Ultralytics intentó descargar `yolo26n.pt` desde
  GitHub y el nodo no tiene salida. Usó 5,17 GB; no emitió checkpoints ni métricas;
- la corrección incorporó ese activo oficial al bundle y comprobó su carga offline dentro de la
  SIF. `1166520` recibió una A30 y completó entrenamiento y validación de la época de smoke,
  pero terminó `FAILED` (`SIGILL`, exit 132) a 1:41 al serializar el checkpoint: Polars 1.43.2
  fue compilado para AVX2/FMA y el nodo Intel Xeon E5-2690 v2 no ofrece esas instrucciones.
  Consumió 7,69 GB de 16 GB, dejó `results.csv` pero no checkpoints;
- el trainer dejó de usar Polars únicamente para releer `results.csv` durante el guardado y usa
  ahora `csv` de la biblioteca estándar. La regresión está cubierta por tests; el bundle
  corregido conserva 6.883 archivos y tiene hash raíz
  `4b2b65b9d2f9c9aa8a46f5422dddfbd7d04a0d96d67621335921f8b04ce397a9`. Pasó integridad,
  lectura del CSV y preflight dentro de la misma SIF sin pedir GPU;
- el smoke final `1166552` terminó `COMPLETED` (`0:0`) en una A30: 1:44 de wall-clock, 7,82 GB
  máximos de 16 GB y 45,264 s medidos dentro del trainer. Ejecutó 1 época con `fraction=0.05`,
  recargó `best.pt`, comprobó el vocabulario fijo e hizo inferencia sobre una imagen de `val`;
- produjo `best.pt` y `last.pt` de 20.319.673 bytes, manifiesto, métricas y postcheck. Los hashes
  del gate son `c1698964...7b967b47` para `best.pt` y `c52f68a2...14d97e7` para `last.pt`;
  las métricas de esta fracción sólo prueban funcionamiento y no se usan como resultado T1;
- el primer cierre automático encontró que el auditor buscaba los checkpoints en la raíz del
  run y no en `weights/`. Se corrigió el mapeo y se bloqueó la escritura de `__pycache__`; los
  18 tests, Ruff, shell e inventario dentro de la SIF quedaron verdes, sin otra corrida GPU;
- el bundle final activo contiene 6.883 archivos, hash raíz
  `31397d4b305dd9104deec9e3d1068b860257fd09f94395efb2459fa5f0bf363c`.
  `smoke-ready.json` vincula 11 insumos críticos con `1166552`, y
  `ready-for-manual-full.txt` declara `ready_for_manual_full_t1`;
- el job completo está sólo preparado: conserva 1 GPU, 10 CPU, 60 GB y 2 h. Slurm lo aceptó
  con `sbatch --test-only`, pero no se envió. Su wrapper exige confirmación literal, integridad
  completa y un `smoke-ready.json` que vincule imagen, trainer, configuración, payload y pesos
  con el smoke aprobado;
- Mendieta rechazó el diseño inicial de postcheck CPU en `ivb`: la política del clúster exige
  al menos una GPU por job. No se sometió ningún finalizador. Un preflight de 1 s en `bdw`
  (`294502`) tampoco llegó a ejecutar comandos (`RaisedSignal:53`), por lo que esa ruta se
  descartó sin reintentos;
- el watcher `eovrt-t1-finalize-1166552` cerró tras `COMPLETED`. El finalizador del login auditó
  artefactos y hashes, emitió el gate, archivó recuperablemente el bundle ejercido por el smoke,
  activó el bundle final y repitió `sbatch --test-only`; nunca envió el full.

### Reapertura del gate metodológico — auditoría posterior del 2026-08-13

- al inspeccionar el checkpoint de `1166552`, el optimizador conservó estado para **366/366
  tensores**. En Adam, ese estado se materializa para parámetros que participaron del paso de
  optimización; por tanto, la evidencia no es compatible con el alcance previsto de T1, que
  debía congelar backbone/upstream y ajustar únicamente el head de linear probing;
- `1166552` sigue siendo un smoke **técnicamente verde** de Slurm, CUDA, I/O, serialización,
  recarga e inferencia, pero queda **invalidado como gate metodológico**. Sus métricas no eran
  resultado científico y sus marcadores `smoke-ready.json`/`ready-for-manual-full.txt` se
  consideran revocados para cualquier envío full;
- el cierre anterior tampoco ejerció el checkpoint mediante el consumidor local del
  media-plane. D-FT-08 continúa en `propuesta`; en consecuencia T-FT-030/T-FT-031 y Gate P3
  permanecen abiertos [✎ 2026-08-15: D-FT-08 **aprobada**; T-FT-030 ya estaba `done` y
  T-FT-031 pasó a `ready`];
- la procedencia local aún no cumple el contrato del plan: `finetuning/` y los planes 116/117
  no tienen una revisión Git durable. Los hashes del bundle permiten auditar el remoto, pero no
  sustituyen commits o un snapshot dirty inmutable de las fuentes;
- el contraste final requiere una baseline **YOLOE-26s** sobre el mismo `bench_v3`. La evidencia
  reportable existente sobre `bench_v3` corresponde a YOLOE-26x; la corrida 26s debe prepararse
  con peso, prompt, resolución, thresholds, evaluador y benchmark congelados antes de observar
  el resultado fine-tuned;
- el pedido Slurm de 2 h permanece como envelope provisional y prudente, no como costo medido
  del full: `finetuning_v1` contiene 2.946 train/483 val; el smoke consumió 1:44 de pared,
  45,264 s dentro del trainer y 7,82 GB máximos. `sbatch --test-only` sólo demostró que el pedido
  1 GPU/10 CPU/60 GB/2 h es admisible.

### Corrección cerrada técnicamente — 2026-08-13

- el preflight del freeze corregido dejó exactamente **12 tensores / 3.096 parámetros**
  entrenables, todos en `cv3` y `one2one_cv3`; ningún parámetro upstream integra el alcance
  declarado;
- el bundle activo `r20` tiene 6.888 entradas; el índice `bundle.sha256` tiene SHA-256
  `1049b3ea1bebd8ebbeb78224daf0febf8dfcaac22503721feeaa0ca39893e026` y `bundle.json`,
  `084c8842f54e531f5065192b3b733b068b046f0d9789c463dfeda8c144d14954`; `r19` quedó archivado;
- T-FT-026 está `done`: `technical-smoke-ready.txt` representa sólo el smoke y
  `full-authorization.json` exige estados exactos T-FT-005/023/026/030/031/032/042R,
  D-FT-08=`aprobada` y hashes vigentes. El wrapper requiere ambos y confirmación manual. La
  prueba negativa `RUN` sin autorización terminó `exit=1` y mantuvo cero jobs full;
- el smoke `1166583` terminó `COMPLETED 0:0` en A30: 3:10 Slurm, 1:51 CPU, 7,64 GB/16 GB,
  40,83445 s del trainer y `GPU_mem=0.543G`. Ejecutó 1 época al 5 %, produjo
  `best`/`last`/`epoch0`/`results`, confirmó 12 tensores/3.096 parámetros y optimizer con 12
  parámetros en grupos `[6, 0, 6]` y 12 estados. Hashes: alcance `ce114033…`, `best.pt`
  `22fc034b…`; gate v2/live verify verde sobre 20 críticos;
- T-FT-030 está técnicamente `done`: media-plane real fuera del sandbox quedó listo, cargó en
  CPU en 2,37 s e infirió en 0,276 s; `set_classes` quedó prohibido y el caché dinámico intacto.
  La evidencia `finetuning/manifests/t1_smoke_1166583_media_plane.json` tiene SHA-256
  `4cd51708…`; pasaron 39 tests focalizados, 100 ampliados y Ruff. D-FT-08 sigue en `propuesta`
  [✎ 2026-08-15: **aprobada**; la tarea técnica nunca la aprobó por sí sola, la firma es del usuario];
- el full fue aceptado por `sbatch --test-only` en `ivb`/`multi` con 2 h. Su proyección de inicio
  2026-08-18 refleja sólo la cola observada: no es reserva ni promesa.

### Cierre de procedencia T-FT-023 — 2026-08-13

- se congelaron **72 fuentes / 512.774 bytes** mediante inventario explícito: 46 de
  `experimental-setup`, 6 de `docs` y 20 de `media-plane`; quedaron excluidos pesos, payloads,
  BENCH, runs, cachés, binarios, symlinks, archivos ignorados y credenciales;
- el inventario tiene SHA-256 `431e43a4241357b65e8124b86171a8fa5c7555ff3d5abd129b729b633b483617`;
  el manifiesto durable, `f487347b058997e9e5d1a9f7721377a3dd86784f807fdcb95633c84f54229bc8`;
  y el tar POSIX PAX determinístico, `639e60df1bcca25590357f54c6897cedcb83cb6e21a651328f6b828cefac3ebe`;
- una segunda generación resultó byte-idéntica. La copia read-only en Mendieta fue publicada
  sólo después de verificar los tres hashes. El snapshot conserva correctamente el tablero
  previo con T-FT-023 `blocked`; este apartado es la atestación posterior que lo cierra;
- la atestación durable `t1_source_provenance_attestation.json`, SHA-256
  `4fe5aa3c8427d19ce04f15bdce02c6fa683e47506782409cee9a7438b321bbda`, enlaza el snapshot,
  el bundle activo y la copia remota, y también quedó read-only y verificada en Mendieta;
- no hubo commit ni staging. El snapshot inmutable satisface la alternativa de procedencia
  prevista por el plan, sin afirmar que el checkout completo esté limpio o versionado.

## 4. Backlog generado

| Tarea | Estado | Depende de | Repositorio principal | Salida / criterio de terminado |
|---|---|---|---|---|
| **T-FT-000** Crear plan 116, tablero 117 y layout `finetuning/` | **done** | D-FT-07 | `docs`, `experimental-setup` | navegación y fronteras documentadas; artefactos pesados ignorados |
| **T-FT-001** Cerrar D-FT-11 | **done** | usuario | `docs` | contrato `finetuning_v1` aprobado antes de implementar el builder |
| **T-FT-002** Revisar el antecedente de `main` | **done** | D-FT-10 | `datasets`, `docs` | piezas reutilizables e incompatibilidades identificadas sin incorporar artefactos v1 |
| **T-FT-003** Versionar el auditor de linaje/perceptual | **done** | D-FT-11 | `experimental-setup` | inventario/reporte reproducibles; SHA, source key, linaje refinado, componentes y cruces con bench |
| **T-FT-004** Cerrar D-FT-01 | **done** | T-FT-010/013, usuario | `docs` | regla de checkpoint apoyada en la cobertura medida de `finetuning_v1/val` |
| **T-FT-005** Cerrar D-FT-08 | **done** | decisión explícita del usuario | `docs` | contrato del checkpoint fusionado **aprobado por el usuario el 2026-08-15**, sin cambios; el serving T-FT-030 ya estaba implementado contra ese contrato |
| **T-FT-010** Implementar builder `finetuning_v1` | **done** | D-FT-11 | `experimental-setup` | CLI portable; split por grupos; cero cruces train/val/bench; fuentes intactas |
| **T-FT-011** Migrar/endurecer el trainer T1 | **done** | D-FT-01, T-FT-010 | `experimental-setup` | freeze corregido: preflight real 12 tensores/3.096 params sólo en `cv3`/`one2one_cv3`; guard contra upstream |
| **T-FT-012** Crear tests sintéticos del kit | **done** | T-FT-010/011 | `experimental-setup` | guards de clases, conteos, colisiones, paths, payload, bundle, gate, perfiles y CSV portable; 18 tests verdes |
| **T-FT-013** Emitir manifiesto de datos `finetuning_v1` | **done** | T-FT-003/010 | `experimental-setup` | inventario, auditoría, split y resumen con hashes, origen, linaje, conteos y disjunción |
| **T-FT-015** Emitir manifiesto del peso base | **done** | D-FT-01 | `experimental-setup` | origen, licencia, tamaño y SHA-256 del checkpoint y text encoder T1 |
| **T-FT-014** Materializar payload T1 | **done** | T-FT-010/013 | `experimental-setup` | `train`/`val` autocontenidos, sin symlinks absolutos ni contenido del bench |
| **T-FT-020** Crear definición Apptainer T1 | **done** | T-FT-011/014 | `experimental-setup` | SIF construida desde login, base por digest, hash/entorno manifestados y preflight de carga verde |
| **T-FT-021** Crear `sbatch` smoke/completo | **done** | D-FT-09, T-FT-020 | `experimental-setup` | build login y jobs smoke/full separados; recursos, logs, timeout, salida y captura de entorno explícitos |
| **T-FT-022** Preflight local sin enviar jobs | **done** | T-FT-012/013/020/021 | `experimental-setup` | tests/lint/shell/preflight verdes y bundle íntegro |
| **T-FT-023** Congelar procedencia de fuentes T1 | **done** | T-FT-022 | `experimental-setup`, `docs`, `media-plane`, remoto | snapshot explícito de 72 fuentes, determinístico y verificado local/remoto; tar `639e60df…3ebe`, atestación `4fe5aa3c…1bbda`, sin depender de un `HEAD` ambiguo |
| **T-FT-024** Auditar alcance entrenable T1 | **done** | D-FT-01 | `experimental-setup` | modelo real: 12 tensores/3.096 params sólo `cv3`/`one2one_cv3`; 0 upstream en alcance declarado |
| **T-FT-025** Revocar gate anterior y reconstruir bundle | **done** | T-FT-011/024 | `experimental-setup`, remoto | `1166552` revocado; r19 archivado; bundle activo r20, 6.888 entradas; hashes `bundle.sha256=1049b3ea…93e026`, `bundle.json=084c8842…d14954` |
| **T-FT-026** Separar smoke técnico de autorización full | **done** | T-FT-025 | `experimental-setup`, remoto | dual gate implementado; auth exige T005/023/026/030/031/032/042R + D-FT-08 aprobada + hashes; negativa `exit=1`, cero full |
| **T-FT-030** Implementar contrato de vocabulario fijo | **done** | T-FT-005/D-FT-08 | `media-plane` | checkpoint `1166583` cargado por servicio real fuera del sandbox; inferencia y contrato fijos verdes; la tarea técnica no aprueba D-FT-08 |
| **T-FT-031** Preparar catálogo y evaluación T1 | **done** (✎ 2026-08-15, misma jornada de la firma) | T-FT-005/030 | `media-plane`, `experimental-setup` | CERRADA con cinco piezas: (1) `pycocotools` instalado en el venv de media-plane (30 tests de evaluación verdes); (2) **enforcement del vocabulario canónico v2 en config** — `CANONICAL_V2_FIXED_VOCABULARY` en `config/schemas.py`, cualquier `fixed_vocabulary` ≠ contrato D-FT-08 se rechaza (5 tests nuevos de mutación; suite 665 verdes, Ruff limpio); (3) catálogo finetuned `configs/models/yoloe/yoloe-26s-ft-t1.yaml` (sha `97129219…`, pesos aterrizan en T-FT-050); (4) **comando de evaluación congelado** `finetuning/scripts/evaluate_t1_bench_v3.py` (sha `88797bee…`, 4 tests sintéticos: hash-mismatch aborta, cobertura incompleta aborta) — emite los 3 artefactos del protocolo; (5) run E2E con checkpoint smoke `run_20260815_193622_dbe_yoloe_e31020` (8/8 CPU, jsonl parseable por el evaluador congelado; manifest `t1_smoke_e2e_run_20260815.json`). El protocolo `t1_yoloe26s_bench_v3_protocol.json` quedó **frozen_pre_baseline** con el `go_no_go` de D-FT-12 completo y la enmienda trazada (schemas.py re-congelado `a81c51df…`→`d026cdc3…` PRE-resultado, guards en `false`). |
| **T-FT-032** Congelar y ejecutar baseline YOLOE-26s | **done** (✎ 2026-08-15, one-shot) | T-FT-031/023 | local | `run_20260815_193750_dbe_yoloe_1113f7` → `finetuning/runs/t1_yoloe26s_baseline_bench_v3/`: 6.477/6.477, 0 fallos/drops, evaluada con el comando congelado. **mAP50 0,4193; `bare_head` AP50 0,000 (6.181 GT / 10 det); recall CR-01 0,0167 bench_obra · 0,0000 shel5k · 0,0002 agregado** — la vía del rescate del gate D-FT-12 queda abierta y exigible. Retención a proteger: person 0,7843 / helmet 0,6286 / vest 0,2642. **F-120.1**: latencias del run NO citables (cambio batería→AC en curso); el gate de latencia se mide pareado aparte. Cifras, estratos y hashes: **doc 120** |
| **T-FT-040** Revalidar Mendieta antes del staging | **done** | autorización de staging | remoto, sólo lectura | Slurm, particiones, política GPU, Apptainer 1.5.3 y almacenamiento registrados |
| **T-FT-041** Transportar bundle verificado | **done** | T-FT-040 | remoto | bundle final con 6.883 hashes, activo AMP y CSV portable verificados dentro de la SIF |
| **T-FT-042** Ejecutar smoke técnico T1 | **done** | T-FT-041 | remoto/local | `1166552` `COMPLETED 0:0`; infraestructura verde, pero gate metodológico revocado por estado optimizer 366/366 |
| **T-FT-042R** Repetir smoke T1 con freeze corregido | **done** | T-FT-026 | remoto/local | `1166583` `COMPLETED 0:0`; 12 tensores/3.096 params, optimizer 12/12, artefactos, gate v2/live verify 20 críticos y serving real verdes |
| **T-FT-043** Ejecutar T1 completo | ✎ **done (2026-08-15 noche)** | T-FT-005/023/026/030/031/032/042R, ejecución manual usuario | remoto | `full-authorization.json` emitida y verificada en el clúster (`gates=7`, D-FT-08 registrada), `TEST_ONLY` en verde y **`RUN_T1_10_EPOCHS` encolado: `job_id=1167640`** (`ivb`/`multi`, 1 GPU/10 CPU/60 GB/2 h). *Se envió un (1) job full, con autorización.* Constancia: doc 120 §5 y 122 |
| **T-FT-044** Monitorear y finalizar T1 completo | ✎ **done (2026-08-16)** | T-FT-043 | remoto/local | job `1167640` `COMPLETED` exit 0, 10/10 épocas, 13m08s en A30. El watcher `tmux` disparó el finalize solo y emitió `full-ready-1167640.json` (auditoría con hashes + contrato de 12 tensores/3.096 params). Copia local verificada en `weights/finetuned/full-1167640/` (`MANIFEST.sha256` 22/22). Doc 123 §1 |
| **T-FT-050** Promover el checkpoint T1 | ✎ **done (2026-08-17)** | T-FT-044 | `media-plane` | integridad + binding de clases + serving smoke `cuda` (`fixed_vocabulary_serving_passed`) ANTES de copiar; `best.pt` a `models/yoloe/finetuned/t1/` con **sha256 preservado** (`5714f833…`); catálogo verificado contra el hash congelado. Manifiesto `t1_promotion_1167640.json`. Doc 123 §1 |
| **T-FT-051** Evaluar una vez contra `bench_v3` | ✎ **done (2026-08-17)** | T-FT-050 | local | corrida única 6.477/6.477, 0 fallos/0 drops, 40.696 det, 256,7 s; config validada en seco contra la baseline (15 campos congelados idénticos). Métricas por clase y **por estrato**, sin tuning post hoc. Doc 123 §2 |
| **T-FT-052** Aplicar y registrar go/no-go T1 | ✎ **done (2026-08-17)** — **NO-GO** | T-FT-051 | `docs` | gain gate falla por las dos vías (Δ`bare_head` +0,0455 vs 0,05; recall 0,2089 vs >0,5) y retención falla por `person` (−11,62 % sobre tope 10 %). Márgenes pre-registrados. Manifiesto `t1_go_no_go_1167640.json`. Doc 123 §3 |
| **T-FT-053** Cerrar guard de `--allow-cpu` de `train_t1.py` | **done** | D-100.1 | `media-plane`, `experimental-setup` | `--allow-cpu` queda restringido a `--check-only`/`--check-freeze` (preflight) en `finetuning/scripts/train_t1.py`; ejecución de full sin GPU sin esos flags falla con error de argparse |
| **T-FT-060** Diseñar/ejecutar T2 | ✎ **in_progress (2026-08-17, habilitada por enmienda D-FT-14 — ya no por "go T1")** | D-FT-14 ✓, **D-FT-15 pendiente de firma** | `experimental-setup`, remoto | tier exploratorio; desglose en T-FT-061…066 |
| **T-FT-061** Perfil trainer T2 full-FT | **ready** | D-FT-14 | `experimental-setup` | `YOLOETrainer` (interfaz de texto conservada), contrato de alcance entrenable con inventario exacto por preflight (análogo al freeze guard T1), tests |
| **T-FT-062** Arnés de retención OV (D-FT-04) | **ready** | D-FT-14 | `experimental-setup`, `datasets` | COCO val2017 + prompts 80 clases + pipeline media-plane + evaluador congelado; baseline de retención corrida y congelada ANTES del entrenamiento T2 |
| **T-FT-063** Bundle, smoke y protocolo T2 | ✎ **done (2026-08-17)** | T-FT-061/062 ✓, D-FT-15 firmada ✓ | `experimental-setup`, remoto | protocolo congelado pre-resultado en `t2_yoloe26s_protocol.json`; smoke verde en `short` (job `1167862`: el entrenamiento arranca y la interfaz OV se preserva); sonda `machinery` exigible (D-FT-13) |
| **T-FT-064** RUN T2 full + eval única bench | ✎ **enviado — en cola, sin empezar (2026-08-17)** | T-FT-063 ✓ | remoto, local | **job `1167864`** (`eovrt-t2-full`, cluster `ivb`, partición `multi`, 10 épocas, walltime 3 h). Verificado en el clúster el 17/08: estado `PD (Priority)`, `Start: Unknown`. **Enviar no es medir**: no existe ninguna cifra de T2. Brazo bench one-shot (el ÚLTIMO contra `bench_v3`) |
| **T-FT-065** Retención OV + latencia pareada | **blocked** | T-FT-064 | local | COCO tuned vs base; latencia baseline/T1/T2 en una sesión, todo con corriente |
| **T-FT-066** Go/no-go T2 y constancia | **blocked** | T-FT-065 | `docs` | aplicar D-FT-15 sin renegociar; doc de cierre y propagación |
| **T-FT-070** Diseñar/ejecutar T3 MM-GDINO | ✎ **closed — trabajo futuro con causa técnica (D-FT-14, 2026-08-17)** | — | — | sin baseline MM-GDINO geométricamente sana el Δ es ininterpretable; conseguirla es arqueología de 1–2 semanas contra la defensa; el linaje tuneado no sería el del campeón desplegado. No es bloqueo de cómputo |

## 5. Próxima acción

**No ejecutar el wrapper full todavía.** El circuito técnico T-FT-026/030/042R está cerrado y
su negativa sin autorización bloqueó correctamente el envío.

✎ **2026-08-15 — cambió la naturaleza del bloqueo, no el bloqueo.** Con D-FT-08, D-FT-12 y
D-FT-13 firmadas, T-FT-005 quedó `done` y T-FT-023 ya estaba cerrado: **no queda ninguna
decisión humana en la cadena**. La acción inmediata es enteramente técnica y en este orden:

1. **T-FT-031** (`ready`) — catálogo y evaluación T1. Dependencia local previa: instalar
   `pycocotools` en el venv del media-plane, hoy ausente.
2. **T-FT-032** (`blocked` por T-FT-031) — congelar y ejecutar la baseline YOLOE-26s. Los
   márgenes contra los que se leerá ya están firmados y pre-registrados (D-FT-12).

✎ **2026-08-15, misma jornada — LAS DOS SE EJECUTARON Y CERRARON** (doc 120): pycocotools
instalado, enforcement canónico v2 en config, catálogo finetuned, comando de evaluación
congelado con tests, y la baseline one-shot corrida y evaluada por estrato. **La acción
inmediata pasó a ser la del usuario**: emitir `full-authorization.json`
(`prepare_t1_full_authorization.py`, token `APPROVE_D_FT_08`, evidencia por archivo de las
7 gates T-FT-005/023/026/030/031/032/042R) y ejecutar el `RUN` manual (T-FT-043). Después:
T-FT-050 promoción → T-FT-051 eval única `--arm tuned` → T-FT-052 go/no-go con los márgenes
firmados → medición pareada de latencia (F-120.1).

Al cierre había cero jobs `eovrt-t1-full`. La
proyección Slurm 2026-08-18 obtenida por `--test-only` es coyuntural, no una fecha prometida.

✎ **2026-08-15/17 — toda esa cadena se ejecutó y quedó cerrada.** La autorización se emitió en
el clúster (`gates=7`), el `RUN` se envió (job `1167640`, que arrancó el 16/08 a las 16:46, seis
horas antes de la proyección coyuntural de arriba) y el 17/08 se completaron promoción,
evaluación única y go/no-go: **veredicto NO-GO** ([doc 123](123-cierre-jornada-t1-no-go.md)).
La medición pareada de latencia **no se hizo y no es decisión-relevante** (F-123.1): gain y
retención ya fallan, y el brazo baseline tiene sus latencias no citables por F-120.1.
