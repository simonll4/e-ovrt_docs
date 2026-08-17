# 116 — Plan maestro de fine-tuning (2026-08-13)

- **Estado:** ✎ **2026-08-17 — JORNADA T1 CERRADA, veredicto D-FT-12 = NO-GO**
  ([doc 123](123-cierre-jornada-t1-no-go.md)). El full corrió (job `1167640`, `COMPLETED`,
  10/10 épocas), se promovió el checkpoint por hash y se evaluó una sola vez contra `bench_v3`:
  `bare_head` AP50 **0,0000 → 0,0455**, recall CR-01 **0,0002 → 0,2089**, pero faltaron **0,0045**
  para el umbral de ganancia y `person` cayó **−11,62 %** (tope 10 %). Checkpoint **no adoptado**.
  **Cuidado al leer lo que sigue:** el «NO-GO para T1 completo» del histórico de abajo era la
  **puerta de autorización** —levantada el 2026-08-15—, no este veredicto. Son dos cosas
  distintas: un permiso y un resultado.

  *(histórico, sin cambios)* **NO-GO para T1 completo.** El smoke corregido `1166583` validó el alcance exacto
  de 12 tensores/3.096 parámetros y cerró el gate técnico. ✎ **2026-08-15: el usuario firmó
  D-FT-08, D-FT-12 y D-FT-13**, con lo que T-FT-005 quedó `done` y **no resta ninguna decisión
  humana**; siguen abiertas sólo la evaluación T-FT-031 (ya `ready`) y la baseline T-FT-032.
  ✎ **2026-08-15, misma jornada: T-FT-031 y T-FT-032 CERRADAS** (doc 120) — comando de
  evaluación congelado, enforcement canónico v2 en config, y **baseline YOLOE-26s one-shot
  ejecutada** (`bare_head` AP50 0,000; recall CR-01 agregado 0,0002; retención a proteger
  person 0,7843/helmet 0,6286/vest 0,2642). **Las 7 gates del full-authorization están
  cerradas**; falta emitirla y el `RUN` manual del usuario.
  T-FT-023 ya quedó cerrado mediante
  un snapshot inmutable de las fuentes. El dual gate
  impide autorizar el full mientras falte cualquiera de ellos. No se envió ningún job de
  10 épocas.
- **Alcance:** gobierno, preparación, ejecución y cierre de la jornada E-04 autorizada por
  ADR-017.
- **Tablero vivo:** [`117-decisiones-y-tareas-finetuning.md`](117-decisiones-y-tareas-finetuning.md).
- **Workspace operativo:**
  [`e-ovrt_experimental-setup/finetuning/`](../../e-ovrt_experimental-setup/finetuning/README.md).

## 1. Objetivo

Convertir el relevamiento de preparación en un flujo controlado de decisiones, tareas y
evidencia. El hito inmediato no es entrenar todos los modelos: es completar un circuito T1
portable y reproducible, desde los datos permitidos hasta la evaluación local del checkpoint,
sin usar `bench_v3` para seleccionar hiperparámetros o pesos.

El plan separa cuatro cosas que no deben confundirse:

1. **Decisiones:** elecciones metodológicas u operativas que cambian el experimento.
2. **Tareas:** trabajo ejecutable que nace de una decisión ya cerrada.
3. **Gates:** evidencia necesaria para avanzar de fase.
4. **Resultados:** observaciones de una corrida; nunca se convierten retrospectivamente en
   criterios de selección.

El trabajo histórico de datasets se trata como **insumo auditable**. Sólo se reutilizan
patrones, contratos o funciones que puedan adaptarse al vocabulario `canonical_v2`, al
congelamiento de `bench_v3` y a las fronteras actuales de la plataforma. Sus splits, vistas y
mapeos v1 no son una base de entrenamiento vigente.

## 2. Autoridad y documentos de entrada

Ante conflicto se aplica este orden:

1. [ADR-017](../decisiones/adr-017-fine-tuning-jornada-experimental.md): E-04 se ejerce como
   jornada experimental completa y conserva la escalera T1→T2→T3.
2. [Documento 100](100-t1-dimensionamiento-medido.md): datos efectivos, smoke medido y puertas
   técnicas de T1.
3. Este plan: organización del trabajo y gates de implementación/ejecución.
4. [Tablero 117](117-decisiones-y-tareas-finetuning.md): estado vivo de decisiones y tareas.
5. [Relevamiento consolidado](../../e-ovrt_datasets/docs/finetuning/2026-08-12-estado-y-plan-finetuning-yoloe-gdino.md):
   fotografía técnica y riesgos conocidos.

El plan de contingencia 20 conserva los criterios go/no-go pre-registrados, pero ADR-017 ya
derogó sus condiciones temporales de entrada.

## 3. Decisión de organización

El proceso de fine-tuning vive en el repositorio transversal
`e-ovrt_experimental-setup`, bajo un único directorio `finetuning/`. La decisión queda
registrada como **D-FT-07, aprobada por el usuario el 2026-08-13**.

La reutilización del trabajo previo queda gobernada por **D-FT-10, aprobada por el usuario el
2026-08-13**: se recupera únicamente lo compatible y se adapta a la plataforma vigente. No se
incorporan en bloque artefactos históricos ni se mantiene código por el solo hecho de existir.

La centralización no cambia la propiedad de los componentes fuente:

| Recurso | Fuente de verdad | Uso desde `finetuning/` |
|---|---|---|
| Datos canónicos y licencias | `e-ovrt_datasets` | selección derivada, split propio y payload materializado |
| Configuración del experimento, scripts, Slurm y Apptainer | `e-ovrt_experimental-setup/finetuning` | fuente operativa versionada |
| Pesos base y nuevos checkpoints de trabajo | `finetuning/weights/` | almacenamiento local ignorado por Git, identificado por hash |
| Adaptadores y catálogo de serving | `e-ovrt_media-plane` | promoción sólo después del gate de integración |
| Decisiones, gates y evidencia citable | `docs/operacion` | plan, tablero y cierre de cada fase |
| Resultados pesados de entrenamiento | `finetuning/runs/` | locales/remotos, ignorados por Git; se cura sólo evidencia liviana |

No se mueven todavía los pesos originales que consume el media-plane: sus catálogos actuales
los referencian en ese repositorio. La tarea de staging deberá copiar o materializar los pesos
de entrenamiento y registrar igualdad por SHA-256. Un checkpoint aprobado podrá promoverse al
media-plane mediante copia verificada, sin convertir dos rutas en fuentes de verdad rivales.

## 4. Layout operativo

```text
e-ovrt_experimental-setup/finetuning/
├── README.md
├── configs/              # configs congeladas por tier/run
├── scripts/              # preparación, entrenamiento, export y verificadores
├── containers/           # recetas Apptainer versionadas; imágenes ignoradas
├── slurm/                # jobs de smoke y corrida completa
├── manifests/            # datos, pesos, entorno, run y promoción; sólo texto
├── data/payloads/        # bundles transportables; ignorados por Git
├── weights/
│   ├── base/             # inputs de entrenamiento; ignorados por Git
│   └── finetuned/        # checkpoints producidos; ignorados por Git
├── runs/                 # logs, métricas y checkpoints intermedios; ignorados
└── tests/                # fixtures sintéticas y gates del tooling
```

Credenciales, claves SSH, tokens, imágenes raw, pesos, payloads y salidas de `runs/` nunca se
versionan. Sí se versionan recetas, contratos, manifiestos, hashes, procedencia y resúmenes
curados.

## 5. Flujo de trabajo

### Fase P0 — Gobierno y decisiones

1. Registrar una propuesta en el tablero 117 con alternativas, recomendación e impacto.
2. Cerrar la decisión con la determinación explícita del usuario o con una autoridad previa
   inequívoca, como ADR-017.
3. Crear tareas sólo después de conocer la decisión que gobierna su implementación.
4. Mantener las decisiones diferidas fuera del camino crítico; no decidir T2/T3 con supuestos
   antes de tener el resultado de T1.
5. Resolver primero el contrato de datos y splits; la selección de checkpoint depende de la
   cobertura real del nuevo `val`, no de los splits heredados.

**Gate P0-A (cumplido 2026-08-13):** D-FT-11 cerrada; quedan habilitados el auditor y el
builder de `finetuning_v1`.

**Gate P0-B (cumplido 2026-08-13):** manifiesto del split auditado, `val` con las cuatro clases
y D-FT-01 cerrados. F-100.1 quedó resuelta sin modificar `bench_v3`: `finetuning_v1/val`
aporta el monitor independiente que faltaba. Este cierre habilita la receta, pero no reemplaza
los gates posteriores de alcance entrenable, serving, evaluación y procedencia.

### Fase P1 — Kit portable T1

1. Inventariar la lógica reutilizable de los prototipos `operacion/datos/100-t1-*` y del trabajo
   histórico de `e-ovrt_datasets/main`; migrar sólo funciones compatibles a
   `finetuning/scripts/`.
2. Construir `finetuning_v1` desde `canonical_v2`, sin modificar los datos fuente ni
   `bench_v3`, y emitir un manifiesto de inclusión/exclusión por imagen y linaje.
3. Excluir cualquier linaje fuente que alcance el bench y agrupar variantes Roboflow o
   duplicados perceptuales antes de asignar `train`/`val`.
4. Parametrizar raíces de datos, peso base, caché, salida y nombre de run.
5. Materializar el payload sin symlinks absolutos y emitir conteos, hashes, licencia,
   atribución y huella del split.
6. Implementar la política de checkpoint que resulte de D-FT-01.
7. Cubrir el builder, los guards y la CLI con fixtures sintéticas.

**Gate P1:** kit reproducible sin rutas personales; `train` y `val` disjuntos por hash, linaje
y grupo perceptual; las cuatro clases cubiertas en `val`; intersección cero con `bench_v3` por
los mismos criterios; y SHA-256 del benchmark sin cambios. Los conteos quedan fijados por el
manifiesto generado, no por la estimación anterior de 3.723+326 imágenes.

**Estado del gate P1 tras la corrección del 2026-08-13:** cumplido. El artefacto de `1166552`
mostró estado de optimizador para 366/366 tensores y reabrió la parte de entrenamiento. El fix
fue validado después por `1166583`: exactamente 12 tensores/3.096 parámetros entrenables, sólo
en `cv3`/`one2one_cv3`; el optimizador de `epoch0` contiene 12 parámetros en grupos `[6, 0, 6]`
y 12 estados. El guard falla ante cualquier tensor upstream.

### Fase P2 — Entorno y scheduler

1. Congelar dependencias en una receta Apptainer.
2. Crear jobs Slurm separados para smoke y corrida completa.
3. Capturar dentro del job: versiones, GPU real, commit, manifiesto de datos, peso base,
   configuración, asignación Slurm, tiempos y rutas de salida.
4. Preparar checkpoints y reanudación cuando el tier pueda acercarse al walltime solicitado.

**Gate P2:** preflight local verde, definición Apptainer reproducible, `sbatch` validado sin
enviar el job y procedencia durable de las fuentes. **Estado actual: cumplido.** Bundle/SIF
están identificados por hash y T-FT-023 congeló 72 fuentes exactas de `experimental-setup`,
`docs` y `media-plane` en un tar determinístico, copiado a Mendieta y verificado allí.

### Fase P3 — Serving y evaluación preparados

1. Definir el contrato de vocabulario del checkpoint T1.
2. Preparar test de carga/inferencia y binding de ids canónicos.
3. Preparar la entrada de catálogo finetuned y el manifiesto de evaluación, sin requerir aún
   que el peso exista.
4. Congelar el comando de evaluación contra `bench_v3` y la sonda generalista/clase nueva.

**Gate P3:** un checkpoint de smoke puede atravesar entrenamiento remoto → descarga → carga
local → inferencia, sin reinterpretar clases ni tocar el benchmark. **Estado actual: abierto.**
La parte técnica T-FT-030 está cumplida con el checkpoint real de `1166583`: servicio
media-plane listo fuera del sandbox, carga CPU en 2,37 s e inferencia en 0,276 s; `set_classes`
queda prohibido y el caché dinámico permanece intacto. D-FT-08 sigue como propuesta y
T-FT-005/T-FT-031 siguen `blocked`; por eso la prueba técnica no aprueba el contrato ni congela
todavía el comando de evaluación. ✎ **2026-08-15: D-FT-08 aprobada por el usuario**; T-FT-005
pasó a `done` y T-FT-031 a `ready`. La prueba técnica sigue sin aprobar nada por sí sola —
la firma es humana y es lo que desbloqueó el congelamiento del comando de evaluación.

### Fase P4 — Smoke remoto

1. Revalidar en vivo scheduler, GPU, CUDA y almacenamiento de Mendieta.
2. Transportar el bundle verificado.
3. Ejecutar una época/fracción pequeña en `short` mediante Slurm.
4. Descargar todos los artefactos declarados y ejercer el gate P3.
5. Corregir infraestructura, no hiperparámetros experimentales, si el smoke falla.

**Gate P4:** smoke `rc=0`, checkpoint íntegro, manifiesto completo, alcance entrenable conforme
a T1 y serving local verde. **Estado técnico: cumplido por `1166583`; no autoriza el full.** El
job terminó `COMPLETED 0:0` en A30, ejerció el contrato 12/3.096, produjo checkpoints y pasó el
gate v2 con verificación live de 20 insumos críticos. La autorización integral permanece
imposible mientras estén abiertos D-FT-08/T-FT-005, D-FT-12, T-FT-031 y T-FT-032. ✎ 2026-08-15:
D-FT-08/T-FT-005 y D-FT-12 quedaron cerradas por firma del usuario; restan T-FT-031 y T-FT-032.
✎ 2026-08-15, misma jornada: **T-FT-031 y T-FT-032 también cerradas** (doc 120) — la
autorización integral quedó al alcance de `prepare_t1_full_authorization.py` + confirmación
manual, sin ningún prerequisito abierto.

### Fase P5 — T1 completo y evaluación única

1. Ejecutar las 10 épocas congeladas en `multi`.
2. Conservar checkpoint seleccionado, `last.pt`, argumentos, logs, métricas y costo.
3. Descargar y promover el peso sólo si pasa integridad y serving.
4. Evaluar una sola vez contra `bench_v3`, por clase y estrato.
5. Aplicar el go/no-go sin cambiar umbrales después de observar el resultado.

El control de lanzamiento separa dos responsabilidades: `technical-smoke-ready.txt` sólo
declara T-FT-042R verde; `full-authorization.json` sólo puede emitirse con estados exactos
T-FT-005/023/026/030/031/032/042R, D-FT-08=`aprobada` y hashes vigentes. El wrapper full exige
ambos artefactos y la confirmación manual del usuario; ninguno reemplaza esa decisión. Una
prueba negativa de `RUN` sin autorización terminó `exit=1` y no envió ningún job full.

**Gate P5:** resultado T1 documentado y decisión de escalamiento T2 cerrada.

### Fase P6 — T2 y T3 condicionados

- T2 requiere que T1 habilite el escalamiento y que D-FT-04 congele retención antes de correr.
- T3 requiere que la escalera lo habilite, una baseline MM-GDINO geométricamente sana y el
  cierre de D-FT-02, D-FT-05 y D-FT-06.
- Un resultado negativo cierra la rama con evidencia; no convierte la jornada en una omisión.

## 6. Gates invariantes

1. **Bench inmutable:** `bench_v3` no se copia, redivide, edita ni usa para construir `val`.
2. **Sin leakage:** CHV y SHEL5K no entran al fine-tuning; tampoco puede entrar ningún linaje
   de CSS que tenga una variante en el bench.
3. **Split por grupo:** variantes de una misma imagen fuente y duplicados perceptuales nunca se
   reparten entre `train`, `val` y bench.
4. **Sin tuning contra el bench:** no se eligen épocas, prompts, umbrales o checkpoints mirando
   `bench_v3`.
5. **Sin selección implícita:** la regla de checkpoint se decide antes del job completo.
6. **Sin rutas personales:** ningún artefacto transportable depende de `/home/simonll4/...`.
7. **Sin pesos opacos:** cada peso tiene familia, variante, origen, licencia, tamaño y SHA-256.
8. **Sin entorno supuesto:** GPU/CUDA se registran dentro del job asignado.
9. **Sin jobs largos desde SSH:** toda corrida usa Slurm y logs persistentes.
10. **Sin secretos en repos:** acceso remoto y tokens permanecen fuera del workspace.
11. **Walltime ex post:** el límite de 48 h sólo se declara vinculante si la evidencia de la
   corrida muestra que condicionó el resultado.
12. **Freeze demostrado:** T1 sólo avanza si el manifiesto declara los tensores entrenables y
   una auditoría prueba que el optimizador no contiene parámetros upstream.
13. **Procedencia durable:** hashes de bundle y contenedor no reemplazan los commits de las
   fuentes; un árbol dirty requiere snapshot inmutable y explícito, nunca un `HEAD` ambiguo.

14. **Sonda `machinery`:** D-FT-13 la derogó para T1 y la reasignó a T2/T3. ✎ **2026-08-15:
    firmada por el usuario; este ítem de la puerta queda cerrado.** La derogación vale sólo
    para T1: en T2/T3, de vocabulario abierto, la sonda sigue siendo exigible.

**Limitación de diseño de T1 (declarada):** T1 NO mide retención open-vocabulary
generalista. D-FT-08 prohíbe `set_classes()` sobre el checkpoint y la retención de
D-FT-12 es in-domain (`person`/`helmet`/`vest` dentro de `bench_v3`). El riesgo de
erosión OV de ADR-017 §1.3 queda fuera del alcance medible de T1: cualquier GO se
acota a in-domain. COCO val / OVDEval quedan para T2/T3.

## 7. Contrato mínimo de artefactos

Cada corrida, incluido el smoke, debe poder reconstruirse con:

- id del tier y del run;
- commits de los repos implicados;
- config congelada y comando efectivo;
- manifiestos y hashes de datos/peso base/contenedor;
- versiones de Python, Torch, Ultralytics o MMDetection;
- GPU, nodos, CPU, memoria, partición, walltime solicitado/asignado/real y estado Slurm;
- seed, épocas, batch, workers, resolución y política de checkpoint;
- **seeds registrados:** split 42 · trainer 100 · inferencia 42; son tres etapas con
  generadores independientes;
- logs, métricas, checkpoints, timestamps y reanudaciones;
- resultado de integridad, serving, evaluación y go/no-go.

## 8. Próximo punto de decisión

### Turnos consumidos vs la puerta (ADR-017 §5.2)

Los 7 jobs enviados a Mendieta (1166382, 1166456, 1166465, 1166520, 1166552,
1166583, 294502) fueron **smokes técnicos** en partición `short`, no entrenamiento
full. F-100.1 ya estaba decidida; T-FT-031/T-FT-032 corresponden a evaluación local;
cinco jobs murieron por infraestructura (Docker Hub, AMP o SIGILL de Polars) y
`1166552` fue revocado metodológicamente por la auditoría del freeze. El turno que
protege la puerta —10 épocas full— sigue sin pedirse: NO-GO vigente y cero jobs full.

> ✎ **2026-08-15 (noche) — el turno se pidió: T1 full ENVIADO.** Con las 7 gates
> cerradas se emitió y verificó `full-authorization.json` dentro del contenedor, pasó el
> ensayo `--test-only` y se encoló `RUN_T1_10_EPOCHS` como **job `1167640`** (1 GPU /
> 10 CPU / 60 GB / 2 h). Desde acá, **el párrafo de arriba es historia**: hay un (1) job
> full enviado, con autorización. Lo abierto es la corrida y la cadena T-FT-044 →
> T-FT-050 → T-FT-051 → T-FT-052; **hasta que se evalúe el checkpoint no existe ninguna
> cifra del modelo ajustado.**
>
> ✎ **2026-08-16/17 — la cadena se completó.** El job corrió el 16/08 (13m08s, A30) y el 17/08
> se cerraron T-FT-044/050/051/052. **Ya existen cifras del modelo ajustado** y están en el
> [doc 123](123-cierre-jornada-t1-no-go.md): veredicto **NO-GO**.

D-FT-01 y D-FT-09 quedaron aprobadas el 2026-08-13. El kit portable T1, el payload
`finetuning_v1`, la receta Apptainer y los jobs Slurm pasaron el preflight local y el bundle se
transportó a Mendieta con integridad completa. El bootstrap remoto `1166382` probó la asignación
A30 pero falló antes del entrenamiento porque el nodo no alcanzó Docker Hub. La corrección dejó
la SIF construida desde el login, íntegra y con preflight de carga verde. `1166456` se canceló
todavía pendiente y sin consumo GPU cuando Slurm anunció una ventana más temprana que luego no
materializó. `1166465` recibió una A30, pero venció antes de entrenar esperando la descarga del
activo AMP `yolo26n.pt` desde un nodo sin red; el activo quedó incorporado y probado offline.
`1166520` entrenó y validó la mini época en una A30, pero falló al guardar porque Polars 1.43.2
requiere instrucciones CPU ausentes en el Xeon E5-2690 v2 asignado. El trainer usa ahora el
lector CSV estándar en esa ruta, con regresión, integridad y preflight dentro de la SIF verdes.
El smoke `1166552` cerró `COMPLETED 0:0` en una A30, con 1:44 de wall-clock y 7,82 GB de
memoria máxima. Produjo `best.pt`, `last.pt`, manifiesto y métricas; recargó el checkpoint y pasó
la inferencia de vocabulario fijo sobre `val`. El auditor posterior se corrigió para resolver
checkpoints bajo `weights/` y no escribir bytecode dentro del inventario, sin repetir la corrida.
El bundle ejercido, sus 6.883 hashes, la SIF y el gate técnico de 11 insumos críticos quedaron
verificados.

Una revisión adversarial posterior abrió el checkpoint y encontró estado del optimizador para
**366/366 tensores**. Esa evidencia contradice el alcance T1: el backbone/upstream debía quedar
congelado y sólo el head previsto podía participar del ajuste. Por tanto, `1166552` se conserva
como evidencia técnica de infraestructura, pero **se revoca como gate metodológico**; sus
`smoke-ready.json` y `ready-for-manual-full.txt` no autorizan el full vigente.

El job completo sigue materializado con 1 GPU, 10 CPU, 60 GB y 2 h, y Slurm aceptó su forma con
`sbatch --test-only`; esto prueba admisibilidad, no autorización ni suficiencia metodológica.

La corrección del trainer pasó preflight y luego el smoke `1166583`: quedaron exactamente **12
tensores / 3.096 parámetros** entrenables, limitados a `cv3` y `one2one_cv3`. El bundle activo
`r20` contiene 6.888 entradas; el índice `bundle.sha256` tiene SHA-256
`1049b3ea1bebd8ebbeb78224daf0febf8dfcaac22503721feeaa0ca39893e026` y `bundle.json`,
`084c8842f54e531f5065192b3b733b068b046f0d9789c463dfeda8c144d14954`; `r19` quedó archivado.
`1166583` terminó `COMPLETED 0:0` en A30: 3:10 Slurm, 1:51 CPU, 7,64 GB/16 GB, 40,83445 s del
script de entrenamiento y `GPU_mem=0.543G` en el log. Ejecutó 1 época al 5 %, produjo
`best.pt`, `last.pt`, `epoch0.pt` y `results.csv`; `epoch0` confirmó grupos `[6, 0, 6]`, 12
parámetros y 12 estados de optimizador. El artefacto de alcance tiene hash `ce114033…` y
`best.pt`, `22fc034b…`. Gate v2 y verificación live cerraron verdes con 20 críticos.

T-FT-026 quedó `done`: el autorizador dual valida estados, D-FT-08 y hashes; la prueba negativa
sin autorización terminó `exit=1` y mantuvo cero jobs full. T-FT-030 también quedó técnicamente
`done`: el servicio real cargó el checkpoint fuera del sandbox y ejerció inferencia; la evidencia
`finetuning/manifests/t1_smoke_1166583_media_plane.json` tiene SHA-256 `4cd51708…`; 39 tests
focalizados, 100 ampliados y Ruff quedaron verdes. Esto no aprueba D-FT-08 ni cierra T-FT-031.

El job full pasó `sbatch --test-only` en `ivb`/`multi` con 2 h. La fecha proyectada por Slurm
fue **2026-08-18** bajo el estado de cola observado; es una estimación puntual del scheduler,
no reserva ni promesa de inicio. T-FT-023 quedó cerrado con snapshot inmutable: inventario
`431e43a4…3617`, manifiesto `f487347b…9bc8` y tar `639e60df…3ebe`, verificados también en
Mendieta; la atestación posterior tiene SHA-256 `4fe5aa3c…1bbda`. El NO-GO sólo se levanta
después de aprobar D-FT-08/T-FT-005 y D-FT-12, cerrar
T-FT-031/T-FT-032 y emitir `full-authorization.json`. ✎ **2026-08-15: las dos aprobaciones
están firmadas**; el NO-GO ahora depende únicamente de cerrar T-FT-031/T-FT-032 y emitir la
autorización. T-FT-043
permanece `blocked` y continúa en cero jobs enviados.
