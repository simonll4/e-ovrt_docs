# Etapa 2 — ajustes a la consolidación metodológica (§17.1) y a los Anexos C y D

> **Estado (2026-08-10):** relevado, **sin pase de correcciones aplicado**. El
> relevamiento es `nucleo/historicos/08-alineacion-consolidacion-metodologica.md`, que leyó el
> §17.1 completo contra lo que el proyecto construyó. Su §1 registra lo que el informe
> **valida y refuerza** (no se toca); su §2 las **desalineaciones**; su §4 las acciones.
> Este documento las convierte en ajustes con ID y las cruza con el estado real de hoy.
>
> **Particularidad de esta etapa:** varias desalineaciones **ya se resolvieron en el
> código** (el pattern set `cr01_cr02_v2` existe y es el oficial). Lo que queda
> pendiente es que **el informe lo diga** — el ajuste es documental, no de
> implementación. Están marcados 🛠️ *ya resuelto en código*.
>
> ✎ **2026-08-11 — regla de no-anacronismo (mapa, regla 5), aplicada a esta etapa:**
> el §17.1 es Etapa 2 y **se corrige como protocolo** — entran decisiones, definiciones
> y criterios (valores de configuración elegidos dentro de rangos declarados incluidos);
> **no entran resultados medidos** ni estados de implementación, que se reportan en
> §17.4/§17.5. Los ajustes AJ-2.05, AJ-2.09 y AJ-2.11 se reescribieron para respetar
> esa frontera.
>
> ✎ **2026-08-28 — LA ETAPA 2 ARRANCA. Este documento queda como tablero histórico; el pase que
> se aplica es [`entregable/desarrollando/archivado/correcciones-etapa-2.md`](../entregable/desarrollando/archivado/correcciones-etapa-2.md)
> (E2-01…E2-26, decisiones D-E2-1…9), que integra estas 12 fichas, agrega **AJ-2.13** y las
> podas 12–14, y MANDA donde difiera.** Texto base vigente: `entregable/90f` (el §17.1 del v1.1 sin
> correcciones, en su propio `.docx`); el `96b` queda como foto histórica. Fuente de los hechos:
> `operacion/130` (relevamiento de los cinco repos, 2026-08-28) y `revision-previa-etapa-2.md`.
> Cambios de estado de las fichas: **AJ-2.02 → ⊘** (premisa falsa: §17.1 no menciona cooldown ni
> re-alertas; la regla de conteo entra por AJ-2.12) · **AJ-2.04 → ⊘ para §17.1** (los tres ejes ya
> están en el protocolo; la ficha apuntaba a nuestro diseño de campañas) · **AJ-2.11 con el ✎
> vencido corregido** · **AJ-2.07 corregido** (el fine-tuning NO usó `chv`) · **AJ-2.09** (nombres de
> artefactos). Decisiones firmadas por el usuario: D-E2-1 (sólo §17.1 en el `.docx`), D-E2-2
> (bautismo E-DIR/E-IND/E-HYB en §17.1.5.4.2), D-E2-5 (AJ-2.13), D-E2-6 (MOT intacto con ⊘).
>
> ✅ **2026-08-28 (noche) — PASE APLICADO Y VERIFICADO: §17.1 v1.3** (`desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx`,
> 28.534 palabras, verificador OK). Las 12 fichas + AJ-2.13 + podas 12–14 quedaron resueltas (⊘ para
> AJ-2.02 y AJ-2.04). Constancia y residuales: `desarrollando/archivado/correcciones-etapa-2-pase-2.md`.
> **No reaplicar nada de este tablero.**

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96b` (§17.1 Consolidación Metodológica + §17.2 Costos) · `entregable/96e` §19.3–19.4 (Anexos C y D) |
| Fuente del relevamiento | `nucleo/08` §1–§5 |
| Texto ya redactado | `material-etapa-3/94` §5 (diccionario de métricas, cubre `AJ-2.03`) |

---

## 1. Tablero de ajustes

| ID | Sección | Tipo | Pri | Enunciado |
|---|---|---|---|---|
| **AJ-2.01** | §17.1.5.3.3 / Tabla 24 | PRECISA | 🟠 | Severidades y ventanas: reportar los **valores efectivos** (`high`/4000 ms, `medium`/7000 ms) y que la persistencia se parametriza **en ms, no en frames**. 🛠️ |
| **AJ-2.02** | §17.1 (política de alerta) | CONTRADICE | 🔴 | El **cooldown no es del motor**: por ADR-011 la supresión de re-notificación es política del tramo de distribución. Y **`re_alerts` ≠ FP**. |
| **AJ-2.03** | §17.1.7 / Tabla 35 | CONCRETA | 🟠 | Diccionario de métricas con nombres, definiciones operacionales y umbrales — **más** las dos métricas derivadas propias, declaradas como descomposición. |
| **AJ-2.04** | §17.1.5.4.2/.5 | PRECISA | 🟠 | Ejes del protocolo de prompts que el diseño original no tenía: **vocabulario aislado vs completo**, variantes **template**, **hiperparámetros congelados**. |
| **AJ-2.05** | §17.1.5.4 | PRECISA | 🟡 | Piso muestral: **~200 instancias positivas por condición** o tamaño efectivo + IC. Declarar por cuál vía se cumplió. |
| **AJ-2.06** | §17.1.5.4.5 | EVIDENCIA | 🟠 | **Doble anotación ≥20% + kappa de Cohen: NO se hizo.** Hay que declararlo como decisión, y es la **limitación L2**. |
| **AJ-2.07** | §17.1.5.4 / Anexo C | PRECISA | 🟡 | El prompt set debe declararse construido desde el **Anexo C (Tabla C.1)**; sumar **confianza media de los TP** y **métricas por entidad componente**. |
| **AJ-2.08** | §17.1.6 / Tabla 36 | PRECISA | 🟡 | Usar los **nombres de fase de la Tabla 36** y declarar la correspondencia 1:1 con lo ejecutado (con la nota ADR-010). |
| **AJ-2.09** | §17.1.7.8 | CONCRETA | 🟠 | Instrumentación: los **cinco hitos por alerta**, **P50/P95/P99**, warm-up declarado por corrida, bitácora mínima. |
| **AJ-2.10** | §17.1.4.2.4 | PRECISA | 🟡 | Fuente EBE (H4): la **contingencia oficial se ejerció primero**; la OAK-D está integrada; el RTSP sintético es herramienta, no fuente experimental. |
| **AJ-2.11** | §17.1 / Tabla 37 | PRECISA | 🟡 | Reencuadrar el **fine-tuning (I1)** conforme **ADR-017**: rama experimental condicionada (Tabla 37) que **se ejerce como jornada completa**; condiciones de datos y protocolo, no de cómputo — la causa "presupuesto de tiempo" queda **prohibida**. |
| **AJ-2.12** | §17.1.7 | PRECISA | 🟠 | Declarar los **estados de aplicabilidad** (`not_applicable:<causa>`, ADR-006/013) y las **reglas de lectura** que ninguna métrica puede violar. ✎ 08-28: + la regla de conteo `re-alerta ≠ FP` (D-E2-3, E2-22). |
| **AJ-2.13** | §17.1.7.3.1 | CONCRETA | 🟠 | ✎ **2026-08-28 (D-E2-5, nueva):** declarar el **nivel intermedio de análisis "estado observable por persona"** entre la percepción por imagen y la alerta temporal por episodio — §17.5 lo usa como eje y §17.1 no lo pre-registraba (0 apariciones). Texto guía en E2-18. Sin cifras. |

---

## 2. Los ajustes, desarrollados

### AJ-2.01 · §17.1.5.3.3 y Tabla 24 · PRECISA · 🟠 · 🛠️ ya resuelto en código

**Qué pedía el informe.** La Tabla 24 fija PR-01 (CR-01, sin casco) severidad **Alto**,
persistencia **3–5 s**; PR-02 (CR-02, sin chaleco) severidad **Medio**, persistencia
**5–10 s**. Y §17.1.5.3.3 exige parametrizar la persistencia **en segundos, no en
frames** (la conversión depende del throughput).

**Qué había.** El control-plane usaba severidad `medium` para ambos y
`confirm_after_frames: 1`.

**Qué hay hoy.** El pattern set oficial **`cr01_cr02_v2`**: CR-01 `high` /
`confirm_after_ms: 4000`, CR-02 `medium` / `7000`, con histéresis
activación≠desactivación (`resolve_after_*`). El set con `confirm=1 frame` quedó como
**configuración de diagnóstico DBE-imágenes**, documentada como tal.

**El ajuste, entonces, es documental:** el §17.1 debe reportar los **valores efectivos**
y que caen dentro de los rangos declarados. Cruza con **R-14** en Etapa 3 (§17.3.8.2 y
Tabla 46), que es la ficha canónica de esos valores.

> ✎ **2026-08-28 (D-E2-4, E2-07):** en §17.1 los 4.000/7.000 ms (y 2.000/3.000 de desactivación)
> entran como **decisión de protocolo dentro del rango de la Tabla 24**, sin tocar la tabla y **sin
> la palabra "efectivos"**: por la doctrina de reparto (08-19) los valores efectivos viven sólo en
> §17.4 (`90b` los tiene; §17.3 v1.4 ya no). El puntero "Tabla 46" es de la numeración vieja de
> §17.3 (v1.4 renumeró a 39–55).

---

### AJ-2.02 · §17.1 · CONTRADICE · 🔴 — el cooldown no vive en el motor

**Por ADR-011 el motor emite en cada confirmación**; la supresión de re-notificación es
política del **tramo de distribución de alertas**, no de la evaluación de patrones.
Corolario que hay que escribir: **las `re_alerts` no son falsos positivos** — contarlas
como FP degrada artificialmente toda la precisión reportada.

Su ficha canónica es **R-02** (Tabla 44) en Etapa 3; acá se registra porque el §17.1
también describe la política de alerta y arrastra el mismo error.

> ⊘ **2026-08-28 — PREMISA FALSA (E2-26):** §17.1 **no menciona** cooldown, supresión, re-alertas ni
> re-notificación (0 apariciones en `90f`; el pase 2 de la Etapa 3 ya lo había verificado: *"cero
> apariciones en todo el capítulo de Etapa 2"*). Lo único cercano es la frase de la histéresis
> (§17.1.5.3.3, *"evita alertas repetidas"*), que E2-08 precisa. El corolario `re_alerts ≠ FP` entra
> como **regla de conteo** en §17.1.7.8.3 vía AJ-2.12/E2-22 (D-E2-3). Esta ficha se cierra como ⊘.

---

### AJ-2.03 · §17.1.7 y Tabla 35 · CONCRETA · 🟠 — el diccionario de métricas

**Adoptar los nombres del informe, textuales** — no hay que inventar nada, es
transcribir §17.1.7 + Tabla 35:

| Métrica | Definición | Nota |
|---|---|---|
| **G2A** (Glass-to-Algorithm) | captura/lectura del frame → resultado algorítmico. Componentes: `t_capture` + `t_transport` + `t_preprocess` + `t_inference` | presupuesto **50–250 ms** |
| **t_alert-system** | **inicio anotado del evento** → alerta confirmada y registrada. Integra G2A + `t_track` + `t_reasoning` + `T_persistencia` | métrica operativa **principal** |
| **t_alert-notification** | complementaria; solo con trayecto instrumentado | |
| **TTFD** | inicio anotado → primera detección positiva válida (criterio declarado) | |
| **SDR** | proporción del intervalo anotado con detecciones positivas sostenidas | |
| **ΔFP_tracker** | delta de FP con/sin tracker, unidad de conteo declarada | |

Reporte temporal mínimo: **P50/P95/P99 + promedio**, con warm-up previo declarado y
timestamps monotónicos de fuente explícita.

**Y hay que declarar las dos métricas derivadas propias** (spec 40 §5.2), que **no son
del informe**: `t_capture→alert` (captura del frame de primera evidencia → alerta
registrada) y `t_compute-budget` (= `t_capture→alert` − `T_persistencia_efectiva`).
**No sustituyen a `t_alert-system`: la descomponen.** Existen porque son las únicas
métricas end-to-end computables **sin GT**, lo que permitió validar el tramo plataforma
antes de que existiera el clip bench (ADR-010).

**El texto para esto ya está escrito**: `material-etapa-3/94` §5 (redline R-10).

> ✎ **2026-08-28 (E2-19, D-P3-4):** el reparto vigente es **§17.1 = nombres, definiciones y criterios**
> (ya están: G2A, Glass-to-Alert, `t_alert-system`, `t_alert-notification`, TTFD, SDR, ΔFP_tracker,
> Tablas 34/35) · **§17.3.13 (v1.4) = materialización** (relojes, señales, estados de aplicabilidad) ·
> **§17.4 = valores**. En §17.1 sólo se verifica consistencia terminológica. Las dos métricas
> derivadas (`t_capture→alert`, `t_compute-budget`) **NO se declaran**: ninguna sección del informe
> las usa (0 apariciones en `90`/`90b`/`90c`) — regla del aporte (D-E2-6 bis). El texto de `94` §5
> se escribió para §17.3.13, no para acá.

---

### AJ-2.04 · §17.1.5.4.2/.5 · PRECISA · 🟠 — los ejes del protocolo de prompts

El protocolo del informe (5 fases) exige tres cosas que el diseño de prompts original no
contemplaba:

1. **Contexto de vocabulario como variable**: cada prompt se evalúa **en aislamiento y
   en vocabulario completo**, porque prompts semánticamente próximos compiten. Aplicar
   al menos a las formulaciones finalistas.
2. **Variantes con template** (*"a photo of a [CLASS]"*) como eje de estructura
   sintáctica: sumar 1–2 variantes template al prompt set.
3. **Hiperparámetros congelados** (confianza y NMS constantes entre variantes de
   prompt): explicitarlo en la configuración de las corridas.

> ⊘ **2026-08-28 para §17.1 (E2-10):** verificado sobre `90f`, **los tres ejes ya están en el
> protocolo** (§17.1.5.4.2 "en aislamiento y en contexto completo", "a photo of a [CLASS]";
> §17.1.5.4.5 Fase 2 "hiperparámetros constantes"). La ficha apuntaba a lo que le faltaba a nuestro
> diseño de campañas (`nucleo/08` §2.3), no al informe. §17.1 no se edita; **§17.5 declara** lo
> ejercido: vocabulario en régimen asimétrico (E-DIR aislada, E-IND conjunta) sustituido por un
> control único (B1 vs T2); templates definidas (`cr01_template`/`cr02_template`) y **no medidas**;
> hiperparámetros `box 0,30 / text 0,25` idénticos en todos los brazos, umbrales operativos
> calibrados por brazo con grid idéntico (`operacion/130` §4.2).
>
> ✎ **2026-08-28 (D-E2-2, E2-09) — el bautismo E-DIR/E-IND/E-HYB SÍ va en §17.1.5.4.2**, en el
> párrafo "Estrategia de detección", con el texto guía de C-1 del pase 1 de la Etapa 3. **Dependencia
> inversa** (E3-42, pase 3 §I): §17.3.6.4 v1.4 debe recortar su glosa a una remisión; si no, el
> informe define los códigos dos veces.

---

### AJ-2.05 · §17.1.5.4 · PRECISA · 🟡 — el piso muestral

El protocolo pide **~200 instancias positivas por condición**, o bien reportar tamaño
efectivo **+ intervalos de confianza**. En **§17.1** el ajuste es declarar la vía
elegida como decisión de protocolo (IC por bootstrap) — **el n efectivo contra ese piso
se reporta en §17.5**, que es donde el n existe (regla de no-anacronismo, mapa regla 5).

---

### AJ-2.06 · §17.1.5.4.5 · EVIDENCIA · 🟠 — la doble anotación que no se hizo

El protocolo pide **≥20% doblemente anotado, kappa de Cohen para etiquetas e IoU para
cajas**, aplicable al clip bench y a cualquier anotación nueva de estado EPP.

**No se hizo.** Es la **limitación L2** de la lista canónica, y hay que escribirla como
decisión declarada, no omitirla. Hay un contrapeso que sí conviene reportar: la
**revisión ciega del GT del lote de internet** (2026-08-09) encontró que **5 de 7
declaraciones de episodio eran errores de anotación (~71%)** — evidencia directa, y
medida en el propio trabajo, de por qué el protocolo pedía doble anotación. Eso vive en
Etapa 5 como `AJ-5.07` y como tabla **T-84**.

> ✎ **2026-08-28 (E2-12):** en §17.1 el requisito **se conserva** y gana su **criterio de
> aplicabilidad** (cuando la referencia se reutiliza de anotaciones de fuente sin re-anotación, la
> doble anotación no aplica y la ausencia de acuerdo se declara como limitación del material);
> "no se hizo" es de §17.5. Dato nuevo del relevamiento: la **auditoría humana del GT de imágenes
> (Task 4.3) tampoco se ejecutó** — sólo su kit; `bench_gt_audit.md` §4–6 vacíos (`operacion/130`
> R-14). El informe **no debe afirmar** que hubo auditoría humana del GT de imágenes.

---

### AJ-2.07 · §17.1.5.4 y Anexo C · PRECISA · 🟡

- El catálogo de formulaciones candidatas vive en el **Anexo C (Tabla C.1)** del propio
  informe: el prompt set debe declararse **construido desde ahí**.
- Sumar **confianza media de los TP** como indicador de estabilidad por formulación.
- Para la estrategia indirecta, **métricas por entidad componente** (`person`, `helmet`,
  `vest` por separado) para atribuir la degradación — el bench ya las produce.

> ✎ **2026-08-18 — el Anexo C también trae el catálogo de DATASETS, y ahí hay dos
> precisiones que no son de esta ficha pero se escriben en la misma sección:**
> **(1)** hay que separar **candidatos evaluados** (la lista larga: SH17, Pictor-PPE,
> GDUT-HWD, SHWD, SODA, MOCS…, con por qué no se retuvieron) de **utilizados**, y dentro
> de utilizados distinguir los de **entrenamiento** (`construction_site_safety`, `chv`,
> `ppe_siabar`) de las **fuentes del banco de imágenes** (`construction_site_safety`,
> `chv`, `shel5k`) — comparten dos nombres de tres, y confundirlos es el error fácil.
>
> ⚠ ✎ **2026-08-28 — CORRECCIÓN (`operacion/130` R-02):** la lista de "entrenamiento" de arriba es
> el rol TRAIN **histórico** (`train_v2`, archivado el 08-15). El **entrenamiento efectivo**
> (`finetuning_v1`, T1 y T2) usó `construction_site_safety` 2.203 + `ppe_siabar` 743 = **2.946 / 483**
> y **EXCLUYÓ `chv`** por anti-leakage: el 100 % de sus 1.330 imágenes es estrato de `bench_v3`.
> Copiar la lista vieja al informe violaría su propia Tabla 28 (disyunción estricta). También:
> las licencias de la Tabla 26 se escriben **como están en el registro** (GDUT-HWD/SHWD "verificar";
> CHV sin licencia del dataset — L7; MOCS = copia pública de 1.471 imgs), y css/ppe_siabar entran al
> inventario como candidatos incorporados después del protocolo (E2-13/E2-14; anexos en `90g`).
> **(2)** `bench_obra` **no es un dataset**: es el estrato curado internamente a partir de
> `construction_site_safety`. Guía completa con la cadena de procedencia y una frase lista
> para el informe: **redline R-24** (`material-etapa-3/93`) y glosario `13` §4.4.

---

### AJ-2.08 · §17.1.6 y Tabla 36 · PRECISA · 🟡 — las fases

Usar los **nombres de fase de la Tabla 36** (Preparación · Baseline DBE zero-shot ·
Sensibilidad de prompts · Pipeline y tracking · Fine-tuning condicionado · EBE
complementario · Reporte) y declarar la correspondencia con lo ejecutado. Es coherencia
metodológica gratis.

**Con la nota de ADR-010:** las semanas del plan **no se leen literalmente** — vale la
correspondencia de fases y sus dependencias. Cruza con `AJ-0.03` (§14.2/§14.3).

---

### AJ-2.09 · §17.1.7.8 · CONCRETA · 🟠 — instrumentación

El informe exige, por alerta, cinco hitos con timestamp: **primera evidencia positiva ·
patrón candidato · confirmado · alerta registrada · notificación**. Estado real:

- El control-plane **persiste candidate/confirmed/alert** (`pattern_events.jsonl`) ✓
- **Falta explicitar la primera evidencia positiva** — es derivable del primer hit;
  dejarlo como campo del episodio.
- **Percentiles P50/P95/P99** en las métricas del control-plane (hoy solo promedio).
- **Warm-up declarado por corrida** (verificar en media-plane; N/A en replay).
- **Bitácora mínima por corrida** ≈ `report.json` consolidado + `effective_config`, ya
  cubierta. ✎ 2026-08-28: en el plano de medios los artefactos son `summary.json` +
  `metrics.jsonl` + `run_manifest.json` + `run_provenance.json` (**no** `report.json`/`metrics.json`,
  que son del consolidado del experimento). Estado real verificado (`operacion/130` §4.4): hitos
  **4 de 5** en el control (notificación en el distribuidor); percentiles P50/P95/P99 en
  `summary.json` de medios y control **pero `evaluate-alerts` sólo produce promedios**; hardware,
  SO y versiones **no se registran** por corrida; `warmup_units = 0` en todas las corridas
  (warm-up de modelo sí). Todo eso se declara en §17.4 (E2-21); §17.1.7.8 no cambia.

**Dónde aterriza cada cosa (no-anacronismo):** el §17.1.7.8 **ya exige** los cinco
hitos — como protocolo casi no se edita. Los bullets de "estado real" de arriba son el
**cumplimiento**, y eso se escribe en **§17.4** (qué se instrumentó, con sus huecos:
percentiles solo promedio, primera evidencia derivable). Su ficha canónica en Etapa 3 es
**R-25** (§17.3.11 Tabla 50 y §17.3.13), que trae el contrato de GT temporal y los cinco
hitos juntos — a nivel de *diseño*, que sí corresponde a esa etapa.

---

### AJ-2.10 · §17.1.4.2.4 · PRECISA · 🟡 — la fuente del escenario EBE

El informe define el nodo de captura candidato (**OAK-D Pro PoE**, integrada como fuente
`oak_d` del media-plane desde 2026-07-13) **con plan de contingencia oficial: cámara IP
convencional**. En la práctica **la contingencia se ejerció primero**. Actualizar la
prioridad declarada: contingencia oficial primero, y el **RTSP sintético
(mediamtx+ffmpeg) como herramienta de desarrollo y vía de reproducibilidad DBE↔EBE con
fuente idéntica** — no como fuente experimental.

---

### AJ-2.11 · §17.1 y Tabla 37 · PRECISA · 🟡 — el encuadre del fine-tuning

> ✎ **2026-08-11 — reescrito conforme
> [ADR-017](../../decisiones/adr-017-fine-tuning-jornada-experimental.md)**; *decía "la
> exclusión es por presupuesto de tiempo y por secuenciación"* — esa causa queda
> **prohibida** en el informe.

Reformular citando la Tabla 37 **tal como está escrita**: la regla *"no prescribe que
el fine-tuning deba ejecutarse; define cuándo vale la pena"* — es decir, la rama es
**experimental y condicionada desde el diseño metodológico**, no una exclusión ni un
descarte. Aclarar que **el nodo de entrenamiento existe** (clúster Mendieta, CCAD-UNC)
y que las condiciones que gobiernan la rama son **de datos y de protocolo**. ✎ **Estado
2026-08-13:** F-100.1, freeze/smoke técnico, dual gate y serving real están cerrados;
permanecen D-FT-08/T-FT-005, evaluación T-FT-031 y baseline T-FT-032. La procedencia
T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`). ✎ **2026-08-15:
D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas; T-FT-031 y T-FT-032 cerradas la misma jornada
(doc 120, baseline 26s one-shot). Resta sólo `full-authorization.json` + `RUN` manual.** Son gates
técnicos, **no una falta de cómputo ni de plazo**. La rama **se ejerce como jornada
completa** (ADR-017): escalera T1→T2/T3 con
sus criterios pre-registrados, documentando resultados y limitaciones. **En §17.1 va
la regla y su criterio**; la jornada, el **costo T1 por extrapolación medida: ≈16 min
centrales (prudente 30–45 min; walltime 2 h) — `operacion/100` adenda; la cifra
histórica “≈1 GPU-h” quedó superada**
y sus resultados son datos posteriores y se citan donde corresponde: §17.4 (estado a
la entrega), la sección comparativa de resultados (si la jornada produjo datos a la
entrega) y §18 (`AJ-6.05`: lo que quede más allá de la escalera) — regla de
no-anacronismo.

> ✎ **2026-08-28 — los ✎ del 08-13/08-15 de arriba están VENCIDOS** ("resta sólo
> `full-authorization.json` + RUN"): la jornada está **COMPLETA y CERRADA** — T1 NO-GO (08-17,
> `operacion/123`), T2 NO-GO (08-21, `127`), T3 cerrado con causa técnica; acta `128`. En §17.1 va
> **la regla y su criterio** (E2-23): la rama se ejerce como jornada completa con criterios
> pre-registrados, condicionada por datos y protocolo, nunca por cómputo ni plazo. Dos hechos
> nuevos para §17.4/§17.5 (no para §17.1): el split de entrenamiento fue de **2.946** imágenes contra
> el rango 500–2.000 de la Tabla 28 (**desviación sin justificar en ninguna bitácora**, E2-15), y los
> checkpoints ajustados **sólo se evaluaron en imágenes**, nunca en clips ni en EBE.

---

### AJ-2.12 · §17.1.7 · PRECISA · 🟠 — aplicabilidad y reglas de lectura

Dos cosas que el §17.1 no declara y que gobiernan todo el §17.5:

- **Estados de aplicabilidad**: una métrica que no aplica se reporta como
  `not_applicable:<causa>`, nunca como 0 ni omitida (ADR-006 / ADR-013).
- **Reglas de lectura no negociables** (familia F-EV): reportar **por estrato y
  escenario**, nunca solo el agregado · los clips negativos **no** entran a P/R/F1 (su
  métrica son los FP) · `re_alerts` ≠ FP · el **SDR no se compara entre cadencias** ·
  `t_alert` no se compara entre densidades sin control de supervivencia.

---

## 3. 🚫 Lo que no hay que tocar

1. **Los "nombres de métrica vacíos"** de §17.1.5.3.2, §17.1.7 y Tabla 33 **no son una
   errata del documento**: son objetos de ecuación de Word que la extracción XML no
   captura. En el Word original casi seguro se ven bien. **Verificar visualmente, no
   corregir.** (Esta es una autocorrección: se había reportado como errata en `nucleo/02`
   §4.8 y `nucleo/07`, y se retiró — `nucleo/08` §3.)
2. **Todo el §1 de `nucleo/08`** — lo que el informe **valida y refuerza**. El §17.1 es
   metodológicamente sólido; lo que tiene son desalineaciones puntuales y huecos de
   concreción, no un problema de fondo.
3. **La histéresis activación≠desactivación** ya estaba pedida por §17.1.5.3.3 y ya está
   soportada. No es un agregado nuestro: es cumplimiento.
4. ✎ 2026-08-28 — **§17.1.6.3 (MOT17/OVT-B) y §17.1.7.4.2 (métricas MOT)**: pre-registradas y no
   ejercidas; quedan **intactas con ⊘ explícito** (D-E2-6, E2-16). Lo no ejercido lo reporta §17.5.
5. ✎ 2026-08-28 — **CPN/EN/TN, TTFD/SDR/`t_alert-system` y §17.1.4.4**: nacen acá y §17.3/§17.4 los
   usan por nombre o por número. No renombrar, no renumerar (`correcciones-etapa-2.md` §D).

## 4. Fuentes

`nucleo/historicos/08-alineacion-consolidacion-metodologica.md` (§1 lo validado · §2.1–2.6 las
desalineaciones · §3 la autocorrección · §4 las acciones · §5 adenda de Anexos C y D,
leídos 2026-07-07) · `decisiones/adr-006`, `adr-010`, `adr-011`, `adr-013`, `adr-015` ·
`specs/40` §5.2 · `material-etapa-3/94` §5 · `gobierno/99` §4.1 (limitación L2).
