# Diseño — Serie de relevamientos por servicio + cierre de la arquitectura de alertas

- **Fecha:** 2026-08-10
- **Tipo:** spec de diseño (previo al plan de ejecución)
- **Decisor:** usuario (2026-08-10)
- **Estado:** propuesto — pendiente de revisión del usuario
- **Motivación inmediata:** cerrar la documentación para arrancar la redacción del
  informe (§17.x) sin dejar atrás referencias que mienten.

---

## 1. El problema

`nucleo/01` (relevamiento del control-plane) es una foto del 2026-07-06 con una
actualización del 07-09. Auditado contra el código el 2026-08-10, **siete de sus once
secciones están vencidas**, y dos son trampas activas para quien redacte:

| § | Dice | Estado real |
|---|---|---|
| §2 | "Modo único actual: replay offline DBE. **Sin servicio HTTP, sin broker**" | Falso: servicio FastAPI `:8081` y fuente bus ZeroMQ live (`runtime/live.py`) |
| §3 | Árbol de ~12 módulos | 48 archivos: `service/` (10), `sources/{bus,tracking}.py`, `runtime/{live,core}.py`, `transport/alert_bus.py`, `tools/track_detections.py`, `metrics/latency.py` |
| §5 | Un solo evaluador; "**no usa `bare_head`**" | Existe `evaluators/direct_evidence.py` + estrategias por patrón (spec 41 §6) y el set `cr01_bare_head_v1.yaml` |
| §6 | `subject_key` = punto débil; no hay tracking | Superado: G0 por escena es el default; identidad opt-in en `sources/tracking.py` |
| §8 | Pattern sets = `cr01_cr02_v1` + `cr01_cr02_temporal_eval` | **Trampa**: v1 está DEPRECADO en el propio YAML (F-DR9). El oficial es `cr01_cr02_v2`. Hay 7 sets |
| §9 | Fixture sintético, P/R/F1 | 5 métricas (precision, recall, TTFD, SDR, FAR/hora), matching bipartito, censura |
| §10 | 5 pendientes | Superados — `progress.md` del control-plane los declara así desde el 2026-07-29 |

`nucleo/11` (media-plane) está en la misma condición: arrastra desde el 2026-07-18 un
banner que admite que quedó superado y nunca se reemplazó.

**El diagnóstico de fondo:** parchar relevamientos con banners ✎ tocó su techo. Y no hay
ningún documento que sea *referencia estructural por repo*: `operacion/97` es una memoria
de implementación en clave de delta ("qué cambió desde el 56"), no un "qué es y cómo
funciona cada servicio".

Hay un segundo hueco, señalado por el usuario: **la arquitectura no cierra**. El ciclo de
vida de la alerta —dónde se gestiona, hacia dónde se distribuye, dónde viven el cooldown y
la re-notificación— está escrito, pero repartido en cinco documentos (`nucleo/06`,
ADR-005, ADR-011, `specs/45`, `informe/92b`). Ninguno es el lugar al que ir.

## 2. Decisiones tomadas (usuario, 2026-08-10)

1. **Los relevamientos históricos se archivan y se escriben nuevos, por servicio**,
   ordenados según la cadena.
2. **Orden:** `experimental-setup` → `datasets` → `media-plane` → `control-plane` →
   `alert-distribution`. Es la vista del operador: experimental-setup es el centro desde
   el que se dispara todo, y datasets entra como los insumos que alimentan al media-plane.
3. **`datasets` entra en la serie.** Es cabecera real de la cadena (vocabulario canónico,
   `bench_v3`, splits) y el media-plane lo consume cross-repo por path relativo.
4. **La distribución de alertas se implementa antes de la defensa.** El usuario decidió
   esto tras advertírsele que colisiona con ADR-015 (ver §6). Su propósito declarado es
   **cerrar la arquitectura de la plataforma**: explicar dónde se gestiona todo el ciclo
   de vida de la alerta y hacia dónde se distribuye, con MQTT como ejemplo, incluyendo
   cooldown y re-notificación.
5. **`operacion/97` no se toca.** La serie nueva es referencia estructural; el 97 sigue
   siendo la memoria de implementación y capacidades.

## 3. La serie nueva: `nucleo/14–19`

Números verificados libres (nucleo llega a 12, la raíz tiene el 13; no hay ningún doc
14–19 en el set).

| Doc | Título | Repo |
|---|---|---|
| `nucleo/14` | Mapa de la cadena — quién habla con quién | — (prólogo de la serie) |
| `nucleo/15` | Relevamiento: `e-ovrt_experimental-setup` | consola + runner + catálogos |
| `nucleo/16` | Relevamiento: `e-ovrt_datasets` | insumos y vocabulario canónico |
| `nucleo/17` | Relevamiento: `e-ovrt_media-plane` | percepción (`:8080`) |
| `nucleo/18` | Relevamiento: `e-ovrt_control-plane` | patrones y alertas (`:8081`) |
| `nucleo/19` | Cierre de la arquitectura: el ciclo de vida de la alerta | `e-ovrt_alert-distribution` |

### 3.1 Plantilla común (docs 15–18)

Misma estructura en los cuatro, para que sean comparables y para que la ausencia de una
sección sea visible:

1. **Qué es y qué no es** — incluido lo que el repo deliberadamente no hace.
2. **Cómo se ejecuta** — comandos verificados en esta máquina, no copiados de un README.
3. **Estructura del código** — árbol real, con la responsabilidad de cada módulo.
4. **Contratos** de entrada y salida, con su nombre versionado.
5. **Configuración y catálogos** — qué se parametriza y dónde; cuáles son los vigentes y
   cuáles están deprecados.
6. **Acople con los vecinos** — qué consume, qué produce, por qué camino (DBE/EBE).
7. **Estado de implementación y límites** — qué está construido y qué no.
8. **Trampas conocidas** — las que costaron caro descubrir.

### 3.2 `nucleo/19` es de otro género

No es el relevamiento de un repo vacío: es **el documento que cierra la arquitectura**.
Consolida en un solo lugar lo que hoy está repartido:

- **La cadena completa y sus cuatro fronteras**: detección → patrón → alerta →
  notificación → entrega.
- **Qué vive de cada lado de la frontera** (ADR-011): el motor emite en cada confirmación
  y absorbe solo *ruido perceptual* (memoria de cobertura, histéresis confirm/resolve,
  expiración de sujetos); la distribución absorbe *política de consumo* (cooldown por
  `(condition_id, source_id/subject_key)`, supresión por ventana, agrupación,
  rate-limiting), con outcome trazable `suppressed_cooldown`.
- **El ciclo de vida del objeto**: `AlertEvent` (`control.alert.v1`) →
  `NotificationEnvelope` → ledger de idempotencia por `(notification_id, channel)` →
  retry → `DeliveryRecord`.
- **Por qué MQTT como canal ejemplar**: peso mínimo, estándar de integración IoT, y
  medición limpia de `t_alert-notification` sin la variabilidad de una API externa. Y su
  consecuencia: QoS 1 puede duplicar entregas ⇒ el ledger no es opcional.
- **Qué está construido hoy y qué no**, sin maquillaje: existe la frontera de salida
  (`control.alert.v1` + publisher del control-plane, apagado por default); el repo
  `e-ovrt_alert-distribution` tiene **cero commits**, `src/eovrt_distribution/` son cuatro
  `__init__.py` vacíos y `tests/` solo `conftest.py`.

Fuentes que consolida y cita (no reemplaza): `nucleo/06`, ADR-005, ADR-011, `specs/45`,
`informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md`.

**Consecuencia de diseño:** el cierre arquitectónico que motiva el pedido se consigue con
este documento, y **no depende de que aterrice el código**. La redacción del informe puede
arrancar con la arquitectura cerrada.

## 4. Reglas duras

Son las que evitan que esta serie se convierta en el próximo `nucleo/01`.

1. **Los relevamientos no publican ninguna cifra de resultado.** Las cifras salen de los
   cuatro índices de `e-ovrt_experimental-setup/results/`; la historia de capacidades sale
   de `operacion/97`. Un relevamiento que cita un F1 es un relevamiento que en dos semanas
   contradice a `results/`.
2. **Se releva contra git y código, no contra memoria**, y cada doc lo declara en su
   encabezado — el método que `operacion/97` ya fijó.
3. **Cada doc lleva fecha de relevamiento en el encabezado** y la convención de banner ✎
   del doc 13 para futuras correcciones.
4. **Archivado lógico, nunca físico.** Ver §5.

## 5. Archivado de `nucleo/01` y `nucleo/11`

Los archivos **se quedan donde están, con su número**. Mover o renumerar rompería las
~2.800 referencias por número que tiene el set.

- Banner de derogación al tope de cada uno, en el formato ✎ del doc 13, apuntando al
  reemplazo (`nucleo/18` y `nucleo/17` respectivamente) y diciendo qué conserva vigencia.
- De `nucleo/01` conservan valor: §1 (qué es y la cadena `condición → patrón → evidencia →
  estado → alerta`, incluido *"una detección no es una alerta"*), §4 (contrato de entrada),
  §12 (registro histórico de la rama `mati`). Se dice explícitamente en el banner.
- El índice los reclasifica como registro histórico, igual que hizo con el doc 56.

## 6. Cirugía del bloque de decisiones

### 6.1 La colisión

ADR-015 §2c declara la distribución MQTT *"NO implementada, **y no se reabre** […] como
exclusión ejercida con su justificación, **no como deuda**"*. Su §6 fija que si se agrega
cualquier capacidad nueva —nombrando la distribución MQTT— el ADR *"queda **violado** y hay
que **reemplazarlo, no enmendarlo**"*.

Se advirtió al usuario y ratificó la decisión de implementar antes de la defensa.

### 6.2 ADR-016 — construcción

**ADR-016 deroga puntualmente §2b, §2c y §6 de ADR-015, y ratifica expresamente §2a, §3,
§4 y §5.**

Fundamento de por qué derogación puntual y no reemplazo total: §2a (la tabla del alcance
que creció) y §3 (la lista de límites que reemplaza a R-13, con L1–L8) son la fuente de la
sección de límites del informe y están citadas nominalmente desde `informe/99` y el brief.
Reemplazar el documento entero dejaría esas citas colgando. El §6 pedía reemplazo para
impedir que la puerta se reabriera **en silencio**; un sucesor firmado que nombra qué
cláusulas caen cumple ese propósito. Esto queda escrito en el propio ADR-016 para que no se
lea como atajo.

**La mitad restrictiva de ADR-016** (calcada de cómo §2b hacía de freno en ADR-015):

- **Se reabre una sola cosa**: la distribución con el recorte exacto de ADR-005 — un canal
  MQTT + `NotificationEnvelope` + ledger de idempotencia + retry mínimo + vista en la
  webconsole existente. **E-06 sigue excluida**: nada de canales adicionales ni dashboard
  nuevo.
- **No se reabre nada más**: fine-tuning (E-04), inferencia en borde (EN-3), métricas MOT
  (E-10) y condiciones CR nuevas siguen cerradas.
- **No bloquea el informe**: la redacción arranca ya, con la arquitectura cerrada por
  `nucleo/19`. La sección de distribución se escribe cuando el módulo aterrice; si no
  aterriza a tiempo, se declara como estaba.
- **Criterio de invalidación**: si la distribución compromete el cronograma del informe, se
  revierte a exclusión declarada.

### 6.3 Propagación de la cirugía

| Archivo | Qué cambia |
|---|---|
| `decisiones/adr-016-reapertura-acotada-distribucion.md` | Nuevo |
| `decisiones/adr-015-cierre-de-alcance.md` | Banner: §2b/§2c/§6 derogados por ADR-016; §2a/§3/§4/§5 vigentes |
| `decisiones/adr-005-distribucion-mqtt-repo-propio.md` | Banner: de "NO implementado a propósito" a "implementación comprometida (ADR-016)" |
| `decisiones/README.md` | Filas 005 y 015; fila nueva 016 |
| `decisiones/estado-de-implementacion-adrs.md` | Fila 005, fila 015, fila 016; el detalle de ADR-005 (donde hoy dice *"Pendiente: ninguno"*); la tabla de condicionales (fila 005: *"RESUELTO: NO"*); la línea del §284 |
| `nucleo/10-registro-alcance-y-exclusiones.md` | El ítem de distribución y el encabezado que cita ADR-015 |
| `informe/ajustes/gobierno/99-materiales-de-cierre.md` | Fila de R-13 (*"exclusión ejercida y cerrada, no como deuda"*) |
| `GUIA-REDACTORES.md` | La aclaración de estado del módulo de distribución (actualizada el 08-10) |

## 7. Propagación al set documental

- `00-indice.md` — alta de `nucleo/14–19`, reclasificación de `01` y `11` como histórico,
  y actualización del mapa por tramos.
- `CRONOLOGIA.md` — entrada de la jornada.
- `GUIA-REDACTORES.md` — orden de lectura con la serie nueva.
- `informe/ajustes/gobierno/98` (manifiesto del Project) — ruteo a la serie nueva.
- `informe-project-kit/` — regenerar. Los relevamientos nuevos suben a **nivel2**;
  `nucleo-01` y `nucleo-11` salen de nivel3 o se reemplazan por los nuevos.
- Verificadores `operacion/datos/96-verificar-indices.py` y
  `operacion/datos/109-verificar-organizacion.py` en verde antes de dar por cerrado.

## 8. Criterio de terminado

1. Los seis documentos `nucleo/14–19` existen y siguen la plantilla.
2. Ningún relevamiento contiene una cifra de resultado (verificable por revisión dirigida).
3. `nucleo/01` y `nucleo/11` tienen banner y están reclasificados en el índice.
4. ADR-016 existe; ADR-015 y ADR-005 tienen banner; las 8 filas de §6.3 están aplicadas.
5. Los dos verificadores dan verde.
6. El kit está regenerado y su README refleja el conteo nuevo.
7. Ninguna afirmación de los relevamientos sale de un mensaje de commit sin haber mirado
   el código.
8. Los 236 runs no citados están archivados con MANIFEST de origen, no borrados — la
   decisión de borrarlos se toma después de escrito el informe.

El respaldo en Drive (§8ter) **no es criterio de terminado de este trabajo**: lo ejecuta el
usuario por su cuenta. Lo que §8ter sí fija y sigue vigente es el encuadre —carpeta privada,
sin link público, acceso al tribunal concedido puntualmente— porque de eso depende la
declaración de "sin redistribución" que va al informe.

## 8bis. Auditoría de material — resultados (2026-08-10)

Medido con `clasificar_runs.py`, contra-verificado con una muestra de 40 runs buscados
por nombre exacto en todo el workspace: **cero errores de clasificación**. El clasificador
necesitó cuatro pasadas para converger (se le escapaban los `.jsonl` de
`operacion/datos/`, los nombres con prefijo `smoke_*`, y los specs internos de cada repo);
los números de abajo son los que sobrevivieron a la contra-verificación.

### 8bis.1 Runs

| Repo | Runs | Citados | No citados | Peso no citado |
|---|---|---|---|---|
| media-plane | 462 | 428 | 34 | 262 MiB |
| control-plane | 41 | 5 | 36 (9 con nombre smoke/diag) | 5 MiB |
| experimental-setup | 167 | 1 | 166 | 3,6 MiB |
| **Total** | **670** | **434** | **236** | **0,26 GiB** |

**Cero huérfanos**: los 670 conservan `effective_config.yaml` o `run_provenance.json`. Los
no citados tienen firma nítida: era piloto (`video16_clip10`, naming viejo),
`exp_*_orq_alerts`, `exp_*_diag_riesgo_activo` y `control_ebe_*_live_*` del 25-07 — la
misma categoría que `_archived/README.md` ya había declarado archivable.

**Conclusión: `runs/` no es el lastre.** 0,26 GiB. La limpieza ahí se justifica por
claridad, no por espacio.

### 8bis.2 El dato que reordena el problema

Lo que recibe quien clona:

| Repo | Archivos versionados | Peso |
|---|---|---|
| media-plane | 333 | 5,6 MB |
| control-plane | 156 | 1,5 MB |
| experimental-setup | 877 | 7,1 MB |
| datasets | 13.161 | 180 MB |
| docs | 3.089 | 160 MB |

Los 14 G del media-plane (`models/` 5,6 G + `.venv/` 5,7 G + `runs/` 1,9 G), los 15 G de
datasets y los 670 runs están **todos gitignoreados**: no existen para un tercero. El
objetivo *"que todo lo del repo sea evidencia"* se juega en esos ~17.600 archivos
versionados, no en el disco.

### 8bis.3 Dos hallazgos que corrigen supuestos

- **El raw versionado NO contradice la política.** `raw/shel5k` son 5.000 `.xml` de
  anotación y `raw/chv` 1.333 `.txt` de etiquetas: **cero imágenes**. Se cumple exactamente
  lo que `informe/99` afirma ("raw gitignorado, solo se versionan anotaciones derivadas").
  No hay nada que corregir.
- **`scripts/` (5,7 G) está fuera de todos los repos** y es material de un intento inicial
  abandonado: 16 videos de YouTube cuyos IDs **no aparecen en ningún lado** (docs,
  `datasets-videos`, banco, `results`). Se borra conservando la lista de los 16 IDs en un
  `.txt` — el puntero pesa nada y deja el material re-descargable.

### 8bis.4 Decisión abierta

> ✎ **2026-08-11 — RESUELTA por ADR-017:** la vista YOLO **se conserva** — dejó de ser
> solo evidencia del encuadre y pasó a ser **insumo directo de la jornada de
> fine-tuning comprometida** (T1 entrena sobre el formato YOLO de `canonical_v2`).
> Borrarla ya no es una opción de limpieza.

La **vista YOLO** de `datasets` (6.338 archivos versionados) existe para fine-tuning, que
ADR-015 declara no ejercido (E-04). Pero el doc 100 usa "splits materializados y camino
operacionalizado" como fundamento de que E-04 fue *decisión de secuenciación* y no falta de
preparación. Borrarla limpia el repo y debilita ese argumento. **Decisión de encuadre, del
usuario.**

## 8ter. Respaldo en Drive

**Propósito, según el usuario (2026-08-10):** persistir el material que no entra en git —
por peso y por privacidad— con acceso restringido, concedido al tribunal solo si necesita
verificar. **No es distribución.**

**Encuadre de diseño:** no es un backup, es **el respaldo físico del anexo de
reproducibilidad**. `informe/99` ya tiene 9 sha256 de artefactos que sí entran en git; lo
que no entra queda hoy sin respaldo verificable. Organizada como extensión de ese anexo
—cada artefacto con su sha256 y su ruta— la carpeta permite verificar cualquier número de
punta a punta, y la declaración se escribe sola: *material conservado en almacenamiento
privado, con acceso concedido al tribunal para verificación, sin redistribución pública*.

**Restricciones ya resueltas:** los consentimientos del rodaje y las pruebas de tiempo real
están cubiertos —los grabados son los integrantes del proyecto (ADR-015 §3; `informe/99`
los registra como cerrados)—. El "sin redistribución" de `chv`, MOCS y el lote de internet
se sostiene mientras **la carpeta sea privada y sin link público**; eso hay que dejarlo
escrito, porque el informe lo declara y es razonable que lo pregunten.

**Qué se respalda, por irremplazabilidad:**

| Categoría | Material | Acción |
|---|---|---|
| Irremplazable | `datasets-videos/` (8,4 G) + `datasets/raw/clip_bench/clips/` | **A Drive** |
| Ya respaldado | GT y anotaciones | Versionados en git |
| Re-descargable | chv, shel5k, MOCS | Scripts de descarga versionados |
| Regenerable | `models/` (`make download-models`), `.venv/`, los 434 runs citados (DBE determinista, F-109.1) | No se sube |

El núcleo real son **~8,4 G**, no los 29 G que suman los repos.

**Nota:** la convención ya estaba escrita — `datasets-videos/README.md` línea 197 dice
`datasets/raw/clip_bench/clips/<clip_id>.mp4  # GIT-IGNORED (sube a Drive a mano)`. Lo que
falta es ejecutarla y dejar constancia.

**Mecánica:** la subida la ejecuta el usuario (`rclone` o cliente de escritorio); el
volumen no pasa por las herramientas de esta sesión. Lo que sí se produce acá: el
inventario, el MANIFEST con sha256 por archivo y el script de verificación de la copia.

**C1 (URL por video) no se puede cerrar desde el disco.** No hay registro del origen de
`datasets-videos/raw/N.M.mp4`; los `.clip.yaml` del lote guardan `master: raw/N.M.mp4` y
`license.video_url: TODO`, y el doc 109 §245 lista "URL por video" como sin cambios. Los 16
videos de `scripts/` no son las fuentes del banco (0 coincidencias de tamaño, 0 citas).
Sigue siendo tarea manual del usuario.

## 9. Fuera de alcance

- **Implementar el módulo de distribución.** Este spec cubre la documentación y el registro
  de decisiones. La implementación es trabajo aparte, con su propio plan.
- **Reescribir `operacion/97`.** Queda como está.
- **Tocar cifras.** Ningún número medido cambia por este trabajo.
- **Commits.** Nada se commitea salvo pedido explícito del usuario (regla del workspace).

## 10. Riesgos

- **El más grande: que esto retrase la redacción.** El doc 112 §7(4) ya advirtió que la
  documentación puede estar sustituyendo a la tesis. Mitigación: la serie es acotada (seis
  documentos con plantilla fija) y el cierre arquitectónico que la motiva se consigue sin
  esperar código.
- **Contradicción con `results/` y el 97.** Mitigación: la regla de §4.1 (cero cifras).
- **Propagación incompleta.** Es el modo de falla histórico del set (~40 desfases
  corregidos el 08-06). Mitigación: la tabla de §6.3 y la lista de §7 son la checklist, y
  los verificadores son el gate.
