# Guía para redactar el informe — para quien NO participó del trabajo experimental

**Vos sos el lector previsto de este documento.** Todo el resto del set `docs/` está
escrito como memoria de trabajo de quienes hicieron los experimentos: usa voseo, da por
sabido el contexto y cita códigos sin definirlos. Este archivo es la única puerta de
entrada pensada para alguien que llega de cero y tiene que escribir el capítulo de
resultados.

- **Fecha:** 2026-08-10 · **Estado:** tramo experimental **cerrado y verificado**.
- **Qué NO vas a encontrar acá:** cifras. Las cifras tienen una sola fuente y está más
  abajo. Si un número aparece en este documento es como ejemplo de cómo citarlo, no como
  fuente.

---

## 1. El proyecto en cinco minutos

Se construyó una **plataforma de detección de riesgos de seguridad en obra** que usa
modelos de **detección open-vocabulary** (OVD): modelos a los que se les describe en
**lenguaje natural** qué buscar, en vez de entrenarlos con ejemplos etiquetados.

Se detectan dos condiciones de riesgo:

- **CR-01** — una persona **sin casco**.
- **CR-02** — una persona **sin chaleco** reflectivo.

**La tesis NO es "OVD detecta mejor que un modelo entrenado".** Eso sería perder: un
modelo entrenado para cascos detecta cascos mejor. La tesis es:

> *¿Qué rendimiento se obtiene **hoy**, en construcción civil, expresando las condiciones
> de riesgo **en lenguaje** y **sin entrenar el modelo**, y qué aporta la **plataforma**
> construida alrededor del modelo?*

Esa distinción gobierna todo el capítulo. **Cada número es el rendimiento medido de una
combinación concreta, no una nota de aprobación.** Un recall de 0,40 en multitud no es un
fracaso del proyecto: es el dato. **El contraste entre filas ES el experimento.**

### Las tres piezas de software

| Pieza | Qué hace |
|---|---|
| **media-plane** | Recibe video (archivo o cámara), corre el modelo OVD y emite **detecciones** |
| **control-plane** | Consume detecciones y decide si hay que **alertar**, aplicando una ventana temporal (no alerta con un solo frame: exige que la condición persista) |
| **experimental-setup** | La consola web y el runner de experimentos; también guarda los **resultados** |

> **Hay un cuarto repo, y NO es una cuarta pieza.** `e-ovrt_alert-distribution`
> (distribución de alertas confirmadas por MQTT, **§17.3.10**) está **diseñado y
> especificado pero no implementado**. En disco es un esqueleto de paquetes vacíos, sin
> lógica y **sin un solo commit**. **Ninguna cifra del informe sale de él.** Se redacta
> desde `docs/informe/92b` *describiendo el diseño y declarando el estado* — nunca en
> presente como si funcionara, aunque el 92b esté escrito en presente (es un documento de
> diseño).
>
> ✎ **2026-08-10 — cambió su ESTATUTO, no su estado.** Hasta el 08-10 era *exclusión
> ejercida y cerrada* (ADR-015 §2c). **[ADR-016](decisiones/adr-016-reapertura-acotada-distribucion.md)
> derogó esa cláusula**: ahora es **trabajo comprometido**, con el recorte exacto de
> ADR-005 (E-06 sigue excluida). Para quien redacta cambia una sola cosa: **no se declara
> como algo que se decidió no hacer, sino como módulo en alcance con su estado al momento
> de la entrega.** Sigue sin implementarse y sigue sin aportar una sola cifra. El cierre
> **arquitectónico** —dónde vive el ciclo de vida de la alerta y sus políticas de
> notificación— lo da `nucleo/19`, no el código.
> Lo único construido de ese tramo es la **frontera de salida** que un módulo futuro
> consumiría: el publisher `control.alert.v1` del control-plane, apagado por default.
> Corolario: §17.3.10 **no tiene figuras ni tablas** en `informe/99` §1, y eso es
> correcto — no hay nada medido que mostrar.

### Dos escenarios de despliegue

- **DBE** — todo en un host, sobre archivos de video. Es el modo con el que se midió casi
  todo, porque es **reproducible**: la misma entrada da la misma salida.
- **EBE** — en vivo, con cámara, y los dos planos comunicándose por un bus. Es el modo que
  demuestra que funciona en tiempo real.

### Tres niveles de medición — **no los confundas, es el error más caro**

| Nivel | Qué mide | Unidad | Dónde |
|---|---|---|---|
| **Percepción (imágenes)** | ¿El modelo ve las cosas? AP por clase | una imagen | `bench_imagenes/` |
| **Nivel A** | ¿Determina bien el **estado de cada persona** (con/sin casco)? Sin tiempo | una persona | `bench_nivel_a/` |
| **Nivel B** | ¿La **plataforma entera** emite la alerta correcta? Con motor temporal | un episodio de video | `clip_bench/` |

Nivel B es **el resultado principal de la tesis**, porque es el único que mide la
plataforma y no solo el modelo.

---

## 2. Orden de lectura — cinco pasos, en este orden

1. **Este documento**, hasta el final. Incluye las trampas; saltearlas cuesta caro.
2. **`docs/sintesis/fundamentos-teoricos.md`** — la teoría, sin cifras. Es lo más
   pedagógico del set y explica por qué el diseño experimental es el que es.
3. **`docs/13-glosario-y-convenciones-de-lectura.md`** — siglas, las reglas de oro de
   lectura y (en §4.1–4.3) los códigos, los IDs de campaña y las colisiones de símbolos.
4. **`docs/sintesis/resultados-y-conclusiones.md`** — la narrativa completa con cifras.
   **Es el documento central para escribir el capítulo.** Su §8 trae la escala
   **AF-1…AF-11**: qué se afirma y **con qué fuerza**.
5. **`e-ovrt_experimental-setup/results/index.md`** y sus cuatro índices — **la única
   fuente de cifras**. Cada tabla de ahí tiene su artefacto en disco.

Cuando ya entendiste el trabajo y vas a **escribir**, el sexto paso es
**`docs/informe/ajustes/00-mapa-de-ajustes.md`**: te dice, etapa por etapa (1 → 6), qué hay
que corregir del texto que ya existe y qué hay que escribir desde cero. **Tres secciones del
informe están vacías —§17.4 Implementación, §17.5 Evaluación y §17.6 Cierre—**, y ese mapa
es el que dice qué va en cada una y de dónde sale.

> **Las etapas son seis, y son la guía de desarrollo del proyecto** (Gantt del §14.3 =
> §14.2): 1 investigación bibliográfica · 2 análisis metodológico · 3 diseño arquitectónico ·
> 4 implementación MVP · 5 evaluación y validación · 6 documentación y defensa. **El informe
> está ordenado por sección, no por etapa**, así que la correspondencia etapa → sección la
> tenés en el §0 del mapa. Ojo con un detalle: **el Gantt numera las tareas 0–5 y el §14.2
> numera las etapas 1–6** — misma secuencia, corrida en uno.
>
> **Y la regla que gobierna el tiempo narrativo (no-anacronismo, mapa regla 5): una etapa
> temprana no menciona resultados de etapas posteriores.** §15/§16 dejan la brecha con
> literatura; §17.1 deja decisiones y criterios; **todo número propio vive en §17.5/§18**.
> Si al corregir §15 te ves escribiendo una cifra medida por el proyecto, estás en la
> sección equivocada.

Recién después, y solo si necesitás el detalle de un experimento puntual, vas al documento
de `docs/operacion/NN` que la síntesis te indique.

### Qué **no** abrir

| No abras | Por qué |
|---|---|
| `docs/GUIA-CIERRE.md` y `docs/operacion/113` | Son el checklist operativo **del equipo experimental**, no material de redacción |
| `docs/informe/92` y `docs/operacion/56` y `92` | **Derogados como fuente de cifras** |
| `docs/operacion/32`, `36`, `50` | Estado de plataforma superado por `operacion/97` |
| ~~`informe-project-kit/`~~ | ✎ **regenerado el 2026-08-10** (76 archivos según `informe/98` §1) — es la copia plana para subir al Project. **Si estás leyendo el repo, leé los originales**; el kit es solo para el knowledge |
| Cualquier doc de `operacion/` con banner ⚠️ | Los banners dicen qué quedó superado. **Leé el banner antes que el cuerpo, siempre** |

**Regla general del set:** un documento con banner de corrección **manda por el banner, no
por el cuerpo**. Los cuerpos se conservan a propósito, para trazabilidad.

---

## 3. Cómo citar una cifra — ejemplos pareados

Estas fórmulas no son estilo: son **precisión**. Cada una existe porque la versión de la
izquierda ya se escribió mal alguna vez.

| ❌ Así NO | ✅ Así SÍ | Por qué |
|---|---|---|
| "El sistema alcanza F1 0,930" | "La mejor combinación medida (**G1**: identidad por sujeto) alcanza **F1 0,930** sobre el banco del rodaje, contra 0,789 de la línea de base" | Un número sin su combinación y su banco no significa nada |
| "El banco tiene 34 clips" | "El banco tiene **47 clips** (32 positivos / 15 negativos, **37 episodios**), en dos bloques: **A**, el rodaje guionado (34), y **B**, el lote de obra real (13)" | 34 es el **Bloque A**, no el banco |
| "34 episodios evaluables sobre 35" *(como denominador del banco)* | "34 evaluables sobre 35 **en el bloque del rodaje**" | Es el denominador de un bloque, no del banco |
| "El FAR es de 29,2 falsas alarmas por hora" | "**3 falsos positivos en 6:09,6** del único clip de soak; la tasa horaria derivada es 29,2 FA/h, sobre un denominador de 0,1027 h" | La tasa desnuda sugiere una hora observada que **no existe** |
| "El sistema cumple ≤1 FA/hora" | *(no se puede afirmar)* — "para sostener una cota harían falta ~3 h de cumplimiento anotado; el banco llega a 0,1027 h" | **Limitación L1** |
| "A nivel de escena (0,333) el sistema supera al de sujeto (0,190)" | "En el estrato B, con **solo 2 episodios evaluables**, la diferencia de F1 **no es interpretable**. Lo robusto es la **asimetría de falsos positivos**: 26 contra 323 sobre 11 clips negativos (**12×**)" | Con n=2 eso es ruido |
| "El lote de internet valida el sistema en obra real" | "El lote aporta medición en obra real **acotada**, y su aporte principal es **caracterizar dónde el sistema deja de ser evaluable**" | **Limitación L4, precisada** |
| "mAP50 0,551" | "mAP50 **0,551** sobre `bench_v3` (6.477 imágenes de **3 fuentes independientes**), con el desglose por estrato" | **Nunca solo el agregado** (limitación L5) |
| "Los clips negativos bajan el F1" | "Los clips negativos **no entran** a precision/recall/F1: su métrica son los falsos positivos" | Promediarlos cuenta aciertos como catástrofes |
| "El sistema emitió 12 falsos positivos" *(contando re-alertas)* | "…sin contar `re_alerts`, que son re-confirmaciones con la infracción **todavía activa**" | Una re-alerta no es un error |
| "La latencia de vidrio a alerta es de 14,7 ms" | "El tramo medido G2A es de 14,7 ms **desde el dequeue**; de vidrio a alerta hay que sumarle la captura (202–217 ms en el rodaje)" | Se mide desde el dequeue, no desde el fotón |
| "El SDR mejora al bajar la densidad" | *(no se compara)* — "el SDR **solo es comparable dentro de una misma cadencia**" | Es artefacto del instrumento |

**Regla que resume todas:** un número va siempre con **(a)** qué combinación lo produjo,
**(b)** sobre qué material, y **(c)** con qué `n`.

---

## 4. Las cinco trampas que más caro salen

**1. Escribir el capítulo sobre el banco de 34 clips.** Es el error más probable, porque
varios documentos del kit fueron escritos cuando ese era el banco. **Vigente: 47 clips,
37 episodios.** Si un documento dice 34 sin aclarar "bloque A", está desactualizado.

**2. Decir que no se midieron falsas alarmas** (porque un doc viejo dice que FAR/hora "no
es una métrica de este trabajo"). **Se mide y se reporta**, pero no sostiene una cota. Ver
la tabla de arriba.

**3. Rankear granularidades en el estrato B.** Con 2 episodios evaluables no sale ningún
ranking. Lo publicable de ese estrato es la asimetría de falsos positivos y la frontera de
juzgabilidad.

**4. Decir que el lote de internet "levanta" la limitación L4.** La decisión firmada dice
**precisada, no levantada**. Varios documentos viejos usan "levanta".

**5. Citar el "BENCH de 196 imágenes" o el clip `cb_b01_p7`.** Los dos están **retirados**:
el primero por estar 20–25 % fuera de dominio, el segundo por licencia sin registrar y GT
generado por IA. Si los ves citados en un doc, ese doc es viejo.

---

## 5. Cómo se decide qué se puede afirmar

No lo decidís vos ni lo decide el número: está pre-registrado en la escala
**AF-1…AF-11** (síntesis §8), que clasifica cada conclusión por **fuerza de evidencia**:

- **Establecida** — se afirma sin hedging.
- **Establecida direccionalmente** — se afirma el sentido, no la magnitud.
- **Tendencia con mecanismo** — se describe el mecanismo, se declara que no es efecto
  establecido.
- **No cerrada** — se declara como limitación, no se afirma.

**Consultá esa tabla antes de escribir cualquier afirmación.** Y las **limitaciones
L1–L8** (versión vigente en `results/index.md`) se declaran, no se esconden: en este
trabajo lo que no se pudo medir es parte del resultado.

Un principio que atraviesa el capítulo: **varias de las cosas más valiosas del trabajo son
refutaciones de predicciones propias** — hipótesis escritas *antes* de medir y que la
medición tumbó. Eso se cuenta como fortaleza metodológica, no se disimula.

---

## 6. Dónde vive cada cosa

| Necesitás | Está en |
|---|---|
| **Cifras de cualquier tipo** | `e-ovrt_experimental-setup/results/index.md` + sus 4 índices |
| La narrativa completa con contexto | `docs/sintesis/resultados-y-conclusiones.md` |
| Teoría, definiciones, por qué el diseño es así | `docs/sintesis/fundamentos-teoricos.md` |
| Qué calcula cada métrica | `docs/sintesis/inventario-de-metricas.md` |
| Cómo está implementada la plataforma (concreción técnica) | `docs/operacion/97-relevamiento-plataforma-2026-08-05.md` — la foto verificada contra código (2.203 tests verdes) |
| El módulo de **distribución de alertas** (§17.3.10) | `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md` — diseño completo, y **`nucleo/19`** para el ciclo de vida de la alerta y sus fronteras. **Ojo: está diseñado y especificado, no implementado** — ✎ 2026-08-10 se redacta como **trabajo comprometido** (ADR-016), no como exclusión cerrada; describiendo el diseño y declarando el estado |
| Siglas, códigos, colisiones de símbolos | `docs/13-glosario-y-convenciones-de-lectura.md` §3 y §4 |
| Reglas de estilo y honestidad al redactar | `docs/informe/97` §1–§3 (⚠️ **su §5 está superada**) |
| Qué figura/tabla va en cada sección | `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md` §1 (✎ al día al 2026-08-10 — incluye el tramo de video, T-82…T-84/FIG-F) |
| **Qué hay que cambiarle al informe, etapa por etapa** | ✎ **`docs/informe/ajustes/00-mapa-de-ajustes.md`** — el mapa de Etapa 1 a Etapa 6, con un documento por etapa (`01`…`06`). **Empezá por acá y no por el 93**: el 93 cubre solo la Etapa 3 |
| Qué hay que corregir del **§17.3** (Etapa 3) | `docs/informe/93` — los **26 redlines** (R-01…R-26). Enrutados desde `informe/ajustes/03-etapa-3-diseno-arquitectonico.md` |
| Las secciones que hay que **escribir desde cero** | **§17.4, §17.5 y §17.6 están vacías** en el informe. Qué tiene que decir cada una: `informe/ajustes/04-etapa-4-implementacion.md`, `05-etapa-5-evaluacion-y-validacion.md` y `06-etapa-6-documentacion-y-cierre.md` |
| Qué **recortar** del informe (está muy extenso) | ✎ `docs/informe/ajustes/07-critica-extension-y-poda.md` — 18 podas medidas (`PODA-nn`, ~27% del texto), con guardrails de qué NO tocar. Se aplica junto con los `AJ-`/`R-` de cada sección |
| Texto ya redactado para adaptar | `docs/informe/94` (§1–§9: cubre 9 de los 26 redlines, y es el modelo de estilo) |
| Por qué se decidió algo | Los **ADR** (`docs/decisiones/`) + `docs/nucleo/10` (alcance y exclusiones) |
| El detalle de un experimento puntual | `docs/operacion/NN` — entrá por la síntesis, que te dice cuál |

---

## 7. Si algo no cierra

**El set es grande y tiene tres semanas de correcciones encima.** Si encontrás dos
documentos que se contradicen, la jerarquía es:

1. `results/index.md` y sus índices — para **cifras**, siempre gana.
2. `docs/sintesis/resultados-y-conclusiones.md` — para **interpretación**.
3. El banner ⚠️ o ✎ de un documento — gana sobre el cuerpo de ese documento.
4. La fecha — más nuevo gana, y las fechas están en la cabecera de cada doc.

**Y si aun así no cierra, preguntá antes de escribir.** Una contradicción que sobrevive a
esa jerarquía probablemente sea un error real que conviene arreglar en el repo, no algo
que haya que resolver escribiendo con ambigüedad.

**Verificación mecánica disponible:** `python3 docs/operacion/datos/96-verificar-indices.py`
comprueba que las cifras citadas en los índices coincidan con los artefactos en disco (19
cifras sobre las 16 campañas). Si dudás de un número, corrélo.
