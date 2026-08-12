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
| **AJ-2.12** | §17.1.7 | PRECISA | 🟠 | Declarar los **estados de aplicabilidad** (`not_applicable:<causa>`, ADR-006/013) y las **reglas de lectura** que ninguna métrica puede violar. |

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

---

### AJ-2.02 · §17.1 · CONTRADICE · 🔴 — el cooldown no vive en el motor

**Por ADR-011 el motor emite en cada confirmación**; la supresión de re-notificación es
política del **tramo de distribución de alertas**, no de la evaluación de patrones.
Corolario que hay que escribir: **las `re_alerts` no son falsos positivos** — contarlas
como FP degrada artificialmente toda la precisión reportada.

Su ficha canónica es **R-02** (Tabla 44) en Etapa 3; acá se registra porque el §17.1
también describe la política de alerta y arrastra el mismo error.

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

---

### AJ-2.07 · §17.1.5.4 y Anexo C · PRECISA · 🟡

- El catálogo de formulaciones candidatas vive en el **Anexo C (Tabla C.1)** del propio
  informe: el prompt set debe declararse **construido desde ahí**.
- Sumar **confianza media de los TP** como indicador de estabilidad por formulación.
- Para la estrategia indirecta, **métricas por entidad componente** (`person`, `helmet`,
  `vest` por separado) para atribuir la degradación — el bench ya las produce.

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
  cubierta.

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
y que las condiciones que gobiernan la rama son **de datos y de protocolo**
(disponibilidad de un split de validación con `bare_head` — F-100.1 —, licencias y
transporte de los datasets, go/no-go de la propia Tabla 37), **no de cómputo ni de
plazo**. La rama **se ejerce como jornada completa** (ADR-017): escalera T1→T2/T3 con
sus criterios pre-registrados, documentando resultados y limitaciones. **En §17.1 va
la regla y su criterio**; la jornada, el **costo medido (≈1 GPU-h, `operacion/100`)**
y sus resultados son datos posteriores y se citan donde corresponde: §17.4 (estado a
la entrega), la sección comparativa de resultados (si la jornada produjo datos a la
entrega) y §18 (`AJ-6.05`: lo que quede más allá de la escalera) — regla de
no-anacronismo.

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

## 4. Fuentes

`nucleo/historicos/08-alineacion-consolidacion-metodologica.md` (§1 lo validado · §2.1–2.6 las
desalineaciones · §3 la autocorrección · §4 las acciones · §5 adenda de Anexos C y D,
leídos 2026-07-07) · `decisiones/adr-006`, `adr-010`, `adr-011`, `adr-013`, `adr-015` ·
`specs/40` §5.2 · `material-etapa-3/94` §5 · `gobierno/99` §4.1 (limitación L2).
