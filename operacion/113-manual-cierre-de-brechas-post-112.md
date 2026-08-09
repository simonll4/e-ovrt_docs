# 113 — Manual de cierre de brechas: del doc 112 a la redacción

**Fecha:** 2026-08-09. **Qué es:** el paso a paso ejecutable para cerrar TODAS las
brechas que dejó la revisión crítica del doc 112 (auditoría del 08-09: 3 pasadas
paralelas — cifras contra `metrics.json`/GT, registro contra los docs 102–111, y estado
real del workspace). Reemplaza al §8 del doc 112 como orden operativo: incorpora lo que
esa revisión encontró después de escribirlo.

**Punto de partida verificado (no re-litigar):**
- Las **23 cifras del doc 112 dan VERDE** contra artefactos primarios (12 de §3.1, 5 de
  §3.2, 6 de §2, 4 valores del bug de FAR). Ningún número de resultados cambia.
- La **deuda git está saldada**: 0 archivos pendientes en los 5 repos, commits del 08-09
  (`05f715b` docs · `907d50fa` datasets · `ff5c22b` exp-setup · `b9a5e79` control-plane)
  y pushes en sync. Queda **solo el backup a otro disco** (bloque C2).
- Lo que sigue son las brechas reales, en el orden en que conviene cerrarlas.

**Regla transversal:** ningún paso de este manual corre inferencia nueva ni abre
capacidad nueva (ADR-015). "Re-evaluar es barato, re-inferir no" — si el bloque B
corrige GT, se re-evalúa y re-agrega; las detecciones no se tocan. Y ningún commit sin
pedido explícito del usuario.

---

## Mapa de brechas → pasos

> ## ✅ Estado al 2026-08-09, cierre: **lo que no depende del usuario está HECHO o en curso.**
> Cerrados: **A1, A2, A3, A4, A6, D3** completos y **A5 en su parte factual** (las
> celdas stale de `results/index.md` — que resultaron ser **tres**, no una: L1, L4 y
> L6). **D1/D2 (stress-tests) EJECUTADOS: 110 tests nuevos, suite 418 verde, un bug
> real corregido (`f1_micro`, impacto cero en lo publicado) y un hallazgo mayor que
> queda a decisión del usuario — la regla `unknown` del scorer de Nivel A (misma forma
> que el bug de FAR; 48%/22% de los FP del piloto). Detalle en el bloque D.** La pasada de consistencia posterior cerró
> además **la fila del 111 en el índice** (A2.3, que había quedado sin ejecutar) y **el
> punto 1 del estrato B en `results/clip_bench/index.md`**, que afirmaba el ranking
> contradiciendo a su propio punto 5. Los dos verificadores mecánicos quedaron verdes
> después de tocar los índices (`datos/96-verificar-indices.py` y
> `datos/109-verificar-organizacion.py`).
> **✅ A5 CERRADO 2026-08-09 (D-113.1: se precisa L4, no se crea L9).**
> **✅ D-D CERRADO 2026-08-09 (D-113.2: se mantiene la regla `unknown`, ahora declarada).**
> **✅ B EJECUTADO 2026-08-09 — el resultado más importante del manual: la revisión
> ciega tiró 3 de los 5 episodios (cuenta final: 5 de 7 declaraciones del lote eran
> errores, ~71%). Estrato B vigente: 2 evaluables, `scene` F1 0,333 / `subject` 0,190,
> Nivel A 0,031/0,018. Cadena completa re-derivada, re-evaluada y propagada; D-G cayó
> de paso (13 evals archivados por campaña). Ver la CONSTANCIA en el Bloque B.**
> **✅ C2 (backup a otro disco) HECHO por el usuario, 2026-08-09.**
>
> ### 📌 LO QUE QUEDA — TODO DEL USUARIO, y en este orden
>
> 1. **C1 — las URLs de los 18 `clip.yaml`** (14 del lote + 4 del piloto) y la
>    propagación a las 13 copias promovidas. Solo el usuario tiene las fuentes; la
>    propagación (re-promover, regenerar manifest, registry) es delegable una vez
>    que las URLs estén escritas. **Cierra el último hallazgo abierto de `informe/99`
>    §6 junto con el de licencias de catálogos de modelos.**
> 2. **E — videos V1–V3** (falta V2; regla registrada: auditar visualmente la clase
>    antes de afirmar que funciona).
> 3. **F — redacción §17.x.** **NO se arranca hasta que el usuario lo indique
>    explícitamente** (orden vigente desde el 08-05, ratificada el 08-09). Cuando se
>    arranque, entrar por el checklist de encuadre de 6 reglas del Bloque F.
>
> **Nada de esto está commiteado** (regla del proyecto: el usuario maneja todo el git).

| # | Brecha | Paso | Quién | Tiempo |
|---|---|---|---|---|
| 1 | ~~Banners de la corrección de `v06_c01` faltan en 102/105/106~~ ✅ **HECHO** (+ 3 entradas del índice) | A1 | — | hecho |
| 1b | ~~La síntesis describe el frente de video como el 08-06~~ ✅ **HECHO** (banner de estado + §11) | A6 | — | hecho |
| 2 | ~~F-111.1 afirma un ranking que n=4 no sostiene~~ ✅ **HECHO** (enmienda firmada en el 111) | A2 | — | hecho |
| 3 | ~~Celda combinada en limbo~~ ✅ **HECHO** (cerrada con causa en el 110 §4) | A3 | — | hecho |
| 4 | ~~7 redacciones imprecisas en el doc 112~~ ✅ **HECHO** (6 bloques ✎ + fila del índice) | A4 | — | hecho |
| 5 | ~~L4 desactualizada + decisión de nombre~~ ✅ **CERRADO — D-113.1: precisar L4, no crear L9** (propagado a 6 lugares) | A5 | — | hecho |
| 6 | ~~GT re-revisado solo donde el modelo discrepó + `v01_c01` pendiente~~ ✅ **EJECUTADO — 2/5 confirmados, 3 corregidos (v04_c02×2, v01_c01); cuenta final 5-de-7; cadena completa re-derivada y re-evaluada** | B1–B2 | — | hecho |
| 7 | `video_url: TODO` en 18 yamls + 13 copias promovidas que lo arrastran | C1 | usuario (las URLs) + delegable (propagación) | 1 h |
| 8 | ~~Backup a otro disco pendiente desde el 05-08~~ ✅ **HECHO por el usuario (2026-08-09)** | C2 | — | hecho |
| 9 | ~~Métricas sin stress de composición~~ ✅ **D1/D2 HECHOS** (110 tests, suite 418 verde; bug real de `f1_micro` corregido con impacto CERO en lo publicado; medias con su `n`); ~~`far_basis` engañoso en gen.2~~ ✅ **D3 HECHO** | D1–D3 | — | hecho |
| 12 | ~~La regla `unknown` del scorer de Nivel A~~ ✅ **CERRADO — D-113.2: se mantiene, ahora DECLARADA** en `bench_nivel_a/index.md` y doc 105 | D §(D) | — | hecho |
| 13 | ~~Brecha de reproducibilidad en I1/I2~~ ✅ **CERRADO junto con B: la re-evaluación archivó los 13 `eval_*.json` en cada campaña** (contra el GT vigente) | D §(G) | — | hecho |
| 10 | V1–V3 pausados (V2 pendiente) | E | usuario+delegable | 1 jornada timebox |
| 11 | Redacción §17.x sin arrancar | F | usuario | — |

Los bloques A y D son delegables enteros. El camino crítico del usuario es B → C → E → F.

---

## Bloque A — Higiene documental (~1,5 h total)

### A1. Banners de la corrección de `v06_c01` en los docs 102, 105 y 106 — ✅ **HECHO 2026-08-09**

> **Ejecutado.** Los 6 docs de la serie (102–107) tienen ahora el banner
> `⚠️ CORRECCIÓN POSTERIOR`. Cada banner nombra la cifra que corrige y separa *qué NO
> cambia* de *qué SÍ cambia*, con el formato del 103/104. Además de los tres banners:
> - **Doc 102** (origen del GT): el banner lista **4 afirmaciones invertidas** — el
>   episodio, el escenario (P5 era correcto: el error estaba en la anotación, no en la
>   curación), **§2.2 entera incluido su título** ("no salió negativo" → sí salió, y es
>   el único soak del banco), y **§2.3(a)**, cuya adjudicación pendiente se resolvió *en
>   la dirección opuesta* a la que el doc anticipaba (no era oclusión que ampliara el
>   episodio a 24,5 s: no había violación). Marca ✎ inline al inicio de §2.2.
> - **Doc 105** (Nivel A): banner + ✎ inline en la tabla §4.1. Deltas verificados contra
>   `na1_.../metrics.json` y doc 109 §9.3: violadores CR-02 de `v06_c01` **37 → 10**,
>   recall **0,108 → 0,300**, F1 **≈0,002 sin cambio** (lo domina la precision) ⇒
>   **F-105.4 se sostiene**, con la salvedad de que la celda descansa sobre 10
>   violaciones y no 37.
> - **Doc 106** (relevamiento): banner + ✎ inline en la "tabla de bolsillo" §2, que no
>   es citable en sus dos mitades (Nivel B tenía 1 episodio evaluable, no 2; la celda de
>   Nivel A se puntuó con el XML previo).
> - **Índice (`00-indice.md`)**: la entrada del 102 **repetía la afirmación invertida**
>   ("no salió negativo ⇒ 0 clips soak ⇒ L1 no se mueve") — reescrita; ✎ en las entradas
>   de 105 y 106.
>
> Verificado: `grep -l "CORRECCIÓN POSTERIOR" docs/operacion/*.md` → 102–107; barrido de
> `342.400` fuera de la serie → 0 hits. **Hallazgo colateral → ver A6.**

**Registro del procedimiento (para auditar o repetir):**

El doc 112 §4 afirma "con banner en los docs originales" — es cierto para 103/104/107 y
**falso para 102, 105 y 106**. El 105 es el caso material: publica la única cifra que el
doc 109 §9.3 declaró incorrecta, sin advertencia.

**Pasos:**
1. Copiar el formato del banner existente (encabezado del 103:
   `## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-07, doc 108 §6)`).
   Mantener la fecha `2026-08-07, doc 108 §6` — es la que usan los banners ya puestos.
2. **Doc 102**: banner que cubra la fila de `v06_c01` en `102:56` ("1 ep CR-02
   342.400→355.533 ms") y la frase de `102:64` ("los dos episodios son evaluables") —
   tras la corrección, `v06_c01` es NEGATIVO y el único soak del banco.
3. **Doc 105**: banner que cubra **los dos lugares**: la fila `105:129` ("0,002 / 37"
   violadores de `v06_c01`) y la tabla agregada `105:182` + conclusión `105:185`. Nota:
   la corrección de Nivel B (episodio eliminado) convive con que el GT de atributos de
   Nivel A conserve person-frames CR-02 — si el banner lo menciona, distinguir niveles.
4. **Doc 106**: nota ✎ en `106:86` (cita el 0,002 heredado).
5. Verificación: `grep -l "CORRECCIÓN POSTERIOR\|✎" 102-*.md 105-*.md 106-*.md` → 3
   archivos; releer que cada banner nombre la cifra que corrige.

### A2. Enmienda firmada a F-111.1 (en el doc 111 — no "en el informe") — ✅ **HECHO 2026-08-09**

> **Ejecutado en los cuatro lugares donde el ranking estaba afirmado:** el doc 111
> (bloque ✎ bajo F-111.1 con la formulación vigente), el 112 §3.3 (espejo), la **fila
> del 111 en el índice** (que repetía "LE GANA" en negrita) y — encontrado en la pasada
> de consistencia — **`results/clip_bench/index.md` punto 1 del estrato B**, que
> afirmaba "le gana… y la brecha se agrandó" contradiciendo a su propio punto 5 ("n=4 no
> establece un ranking"); como los índices de `results/` son documentos vivos, ese punto
> se reescribió a la formulación enmendada con nota ✎ inline.

El §7.1 del 112 diagnostica bien pero apunta la corrección al lugar equivocado: el 111
es el doc de procedencia citable. Si solo se suaviza en el informe, queda el desfase
doc-vs-informe que este proyecto viene cazando.

**Pasos:**
1. En `111:135` (F-111.1), agregar bloque `> ✎ Enmienda 2026-08-09 (revisión del 112
   §7.1):` con la formulación que queda: *"con n=4 episodios evaluables y 5 vs 32 FP, el
   enunciado afirma un ranking que el n no sostiene. Formulación vigente: **en este
   régimen la ventaja de la identidad (G1, rodaje) no se reproduce** — sin base para
   afirmar el orden inverso ni que 'la brecha se agranda'. Los números quedan como
   están; cambia qué se puede afirmar con ellos."*
2. Espejo en el 112 §3.3 (fila F-111.1/2): nota de que F-111.1 está enmendado.
3. Actualizar la fila del 111 en `00-indice.md:161`, que repite "**LE GANA**" en negrita.
4. Verificación: `grep -n "le gana" docs/operacion/111*.md docs/00-indice.md` — cada
   ocurrencia debe tener la enmienda a la vista o estar reformulada.

### A3. Cerrar la celda combinada con causa firmada — ✅ **HECHO 2026-08-09** (nota ✎ en 110 §4 con la causa de F-108.2 y el estatuto vigente de las palancas)

Estado real: 107 §4 la reservó para out-of-sample; 108 §3 la cerró *de facto* ("valida
la decisión de NO correrla"); **`110:137-138` la reabrió** ("pendiente desde el doc
107: la celda combinada `gate` + `min_subject_confidence 0,50` + persistencia"); el 111
corrió sobre esos clips y la ignoró; el 112 no la menciona. Un lector del 110 espera un
resultado que no existe.

**Pasos:**
1. Nota ✎ en `110:137`: *"✎ Cierre 2026-08-09: **CERRADA SIN EJECUTAR, con causa** —
   F-108.2 refutó fuera de muestra la palanca central de la celda
   (`min_subject_confidence 0,50` costó un episodio real); ejecutar la combinación
   sobre el lote no valida una config recomendable y contradice el cierre del tramo
   (112 §8: no más barridos). Las palancas quedan como caracterización de mecanismos
   (108 §3)."*
2. Una línea en el 112 (registro, §4 o donde encaje): la celda combinada quedó cerrada
   sin ejecutar con causa, referencia 110 §4.
3. Verificación: `grep -rn "celda combinada" docs/operacion/*.md` — ninguna mención debe
   quedar en estado "pendiente" sin el cierre a la vista.

### A4. Fe de erratas del doc 112 (y las dos filas del índice) — ✅ **HECHO 2026-08-09** (6 bloques ✎ en el 112 — arco/jornadas, 7×, 2-de-7, censura, git/URLs, salvedad Nivel A, tres-documentos, selección §3.3 — + ✎ en las filas del 112 y del 111 del índice; el "7×" también precisado en el cuerpo del 111 §6.3 y en `clip_bench/index.md`)

Correcciones puntuales, cada una con ✎ inline (estilo del proyecto), en
`112-cierre-del-tramo-video-y-analisis-critico.md`:

1. **§4.3 "Inflaba 7×"** → induce a leer que lo publicado estaba inflado 7×. Redacción
   correcta: *"las cifras publicadas (48,7 y 2.045,6, gen. 2) estaban infladas **1,67× y
   1,11×**; en la corrida gen. 3 el mismo bug habría impreso 204,6 para escena — **7×**
   el valor real (21 FP totales / 3 FP soak) — y eso fue lo que lo delató antes de
   publicarse"*. **Ojo**: el "inflaba 7×" también está en 111 §6.3/F-111.2 **y en la
   fila del 111 del índice** — misma aclaración en los tres lugares. (El 111 §6.3 además
   mezcla bases entre su "1,2×" —ratio de duraciones gen. 2— y su "7×" — dejarlo dicho.)
2. **§7.2 "de los 5 episodios positivos, 2 resultaron errores"** → el lote produjo **7**
   declaraciones de episodio positivo (v04_c01 · v06_c01 · v04_c02×2 · v03_c02 ·
   v01_c01 · v01_c02); 2 eran errores (v06, v03) → **5 vigentes = 4 evaluables + 1
   censurado**. La frase para el informe es *"2 de 7 producidas"* (tasa ~29% — más
   honesta y no menos contundente). El "5" del §7.2 era una foto al 08-07 que coincide
   por casualidad con el 5 post-corrección.
3. **§7.2/§8.1 "si v01_c01 también es error, el estrato queda con 3 evaluables"** — NO
   cierra con la semántica de censura del banco: `v01_c01` ya está **censurado por A1**
   y fuera de los 4 evaluables (los 4 son v01_c02, v04_c01 y los 2 de v04_c02). Si su
   episodio cae, los **vigentes** bajan 5→4 y los **evaluables siguen en 4**. Corregir
   la frase (o, si la intención era otra, explicitarla). Resolver junto con B1.
4. **§7.5 deuda git** → ✎: saldada el mismo 08-09 (commits + push, 4 repos; `docs` en
   `main` local). Queda solo el backup (→ C2 de este manual).
5. **§7.5/§8.2 URLs** → son **18** yamls (14 del lote, incluido `v08_c01`, + 4 pilotos
   en `_retired/`), y las **13 copias promovidas** en `processed/clip_bench/meta/`
   arrastran el TODO (→ C1).
6. **§1/§2 "4 jornadas"** → las fechas documentadas son **3** (08-06, 08-07, 08-09);
   o se corrige a "3 jornadas" o se explicita que la maratón del 06 se cuenta doble. Y
   el arco del §1: la reorganización (109, 08-07) **precede** a los 8 clips (08-09), y
   falta `v03_c02` (doc 110) en la cadena.
7. **§7.3 "tres documentos"** → nombrarlos: 108, 109 y `results/clip_bench/index.md`
   (el registry fue un cuarto lugar). Los tres ya están corregidos.
8. **§3.3** → declarar que es selección, no inventario, y agregar **F-108.3** (Nivel A
   pésimo con Nivel B perfecto en el mismo clip) — es la clave de lectura del §3.2.
9. **Índice**: actualizar la fila del 112 (`00-indice.md:160`) — hoy repite "172
   archivos sin commitear", "2 de 5" y "quedan 3 episodios".

Verificación global de A4: `grep -rn "172 archivos\|2 de 5\|[Ii]nflaba 7×" docs/` → cada
hit restante debe ser una mención corregida o histórica con ✎.

### A5. L4 al día + decisión de nombre — ✅ **CERRADO 2026-08-09 (D-113.1)**

> **DECISIÓN FIRMADA (D-113.1, 2026-08-09): se PRECISA L4. NO se crea `L9`.** El set
> L1–L8 de `informe/99` §6 sigue "canónico y cerrado"; la frontera de juzgabilidad
> (F-105.2/3/4, tres ejes: escala × iluminación × oclusión) es el **contenido nuevo**
> de L4, no una etiqueta aparte. Formulación de cita fijada: *"L4 se precisó: existe
> medición en obra real no guionada, y esa medición caracteriza por mecanismo dónde el
> sistema deja de ser evaluable — no la valida sobre obra real"* (doc 112 §6).
>
> **Propagado a los 6 lugares que citaban la decisión como abierta:**
> - `results/index.md` §L4 — celda reescrita con la decisión y su justificación.
> - `docs/operacion/103` §3 — sus dos ítems pendientes cerrados con causa (el segundo,
>   "¿anotar más clips en densidad intermedia?", cerrado por ratificación del 112 §8:
>   fuera de alcance de esta tesis).
> - `docs/operacion/98` §6 (conclusiones transversales, parte del kit) — fila L4 al día.
> - `docs/sintesis/resultados-y-conclusiones.md` §11 — las dos preguntas de esa fila
>   marcadas cerradas.
> - Este doc (arriba) y `MEMORY.md` / memoria de proyecto.
>
> **De paso, al abrir la tabla de limitaciones aparecieron otras dos celdas stale, sin
> relación con la decisión de nombre pero que hubiera sido un error dejar así:**
> - **L1** decía *"FAR/hora **no reportable**"*: hoy **es computable y se reporta**
>   (29,2 / 1.850,8 = **3 y 190 FP en 6:09,6** del único soak). Se precisa, no se
>   deroga (0,1027 h contra las 3,0 h de la regla de 3 ⇒ no sostiene ninguna cota).
> - **L6** decía *"el tracker **no está medido** en obra real con multitud"*: sí lo
>   está — `v06_c01`, 127 personas, **182 identidades con FP** (F-103.2).
>
> **§17.x ya no tiene bloqueo de esta fuente.**

### A6. La síntesis quedó atrás del tramo — ✅ **HECHO 2026-08-09**

> **Ejecutado.** Se decidió NO esperar a A5/B: la síntesis es el punto de entrada del
> proyecto y estaba describiendo un estado de tres jornadas atrás. Se le puso un
> **banner de estado al 08-09** (cifras vigentes del estrato B + las **tres afirmaciones
> del cuerpo que ya no son ciertas**) y se reescribieron las dos filas de §11 más la de
> las URLs. Lo que **sí** depende de A5 quedó marcado como abierto dentro de la fila, no
> resuelto por mí. El resto del cuerpo se conserva con su fecha, como corresponde a un
> documento de registro.

Detectado al barrer el repo durante A1: **`sintesis/resultados-y-conclusiones.md` §11**
—que la memoria del proyecto declara punto de entrada ("leer el estado de una sola
pasada")— sigue describiendo el frente de video **como estaba el 08-06**:

- fila "CVAT del lote de internet": *"llegaron **3**… banco **34→37**… L4 parcialmente
  levantada (**n = 2 episodios**)"* y *"dos escenarios corregidos (`v04_c01` P8→P1,
  `v06_c01` P5→P2)"* — hoy: 13/14, banco 47, 4 episodios evaluables, y el escenario de
  `v06_c01` **no** estaba mal (A1).
- fila "Runs/evals del estrato B": describe I1/I2 con las cifras de los 3 clips y
  arrastra **la misma decisión abierta que A5** (*"si esto entra al informe como
  limitación nueva (densidad de escena) o como ampliación de L4/L6"*) — confirma que la
  decisión sigue viva en dos lugares distintos.
- filas de pendientes: "URL por video" y "backup de `docs/`" siguen listadas (correcto:
  → C1 y C2), pero no refleja que la deuda git se saldó.

**No se tocó en A1 a propósito**: es una reescritura de sección, no un banner, y **su
contenido depende de A5** (la etiqueta de limitación) y de B (el `n` definitivo).
**Hacerlo después de A5+B, y antes de F.** Cuando se haga, verificar de paso que §11 no
liste como pendiente nada ya cerrado.

---

## Bloque B — GT: re-revisión ciega de los 5 episodios vigentes — ✅ **EJECUTADO 2026-08-09**

> ## CONSTANCIA DE LA RE-REVISIÓN CIEGA (la frase citable del informe sale de acá)
>
> **Los 5 episodios vigentes del estrato B se re-revisaron a ciegas el 2026-08-09
> (usuario mirando el video, sin acceso a alertas ni métricas): 2 CONFIRMADOS con
> evidencia de frame, 3 CORREGIDOS.** Con las 2 correcciones previas (v06_c01,
> v03_c02), la cuenta final del lote es **5 de 7 declaraciones de episodio erróneas
> (~71%), todas sobre-declarando violación donde el estado no era observable** —
> el mismo error que comete el motor, medido ahora también en el anotador.
>
> | episodio | track | veredicto | evidencia |
> |---|---|---|---|
> | `v01_c02` CR-01 | 4 | ✅ CONFIRMADO sin casco | f200: cabeza descubierta, pelo a la vista (persona de al lado, T3, SÍ tiene casco — el contraste ayuda) |
> | `v04_c01` CR-01 | 0 | ✅ CONFIRMADO sin casco | f300: nocturno, cabeza descubierta claramente visible |
> | `v04_c02` CR-01 | 6 | ❌ ERROR → `unknown` | operador EN CABINA de la máquina los 716 frames; ni casco ni chaleco observables |
> | `v04_c02` CR-02 | 6 | ❌ ERROR → `unknown` | ídem — el clip pasa a NEGATIVO |
> | `v01_c01` CR-01 | 9 | ❌ ERROR → `unknown` | f947–1115: cabeza en sombra, a contraluz dentro del edificio (el chaleco sí se ve); criterio del usuario: "si no se distingue, es unknown" |
>
> **Lección de método que quedó firmada en los yaml:** la identificación por "person N"
> de la UI de CVAT **no es confiable** — los números de la UI no coinciden con los
> `track_id` del XML (pasó en 3 de los 4 clips; ya lo documentaba v03_c02: su "person
> 3" era el track 0). El protocolo que funcionó: **extraer el frame del mp4 y dibujar
> encima la caja del track del XML**, y que el humano dé el veredicto sobre esa imagen.
>
> **Cadena ejecutada tras los veredictos** (toda verificada): correcciones firmadas con
> `previous_value` (v04_c02: 1.432 cajas; v01_c01: 169) → guard `--check` verde →
> re-derivación → `validate_clip_gt` 0 errores → re-promoción → banco regenerado
> (**32 positivos / 15 negativos / 37 episodios**, manifest `3f14f50a…`, freeze
> 189/189) → re-evaluación de I1/I2 (mismas alertas; determinismo 11/11; **13 evals
> archivados por campaña — cierra D-G**) → re-agregación → re-puntuación Nivel A →
> propagación a índices, campaign.yaml y docs (banners en 111 y 108; notas en 110,
> 112 y `results/`). Escenarios: `v04_c02` P6→P5, `v01_c01` P1→P5 (en ambos, la
> expectativa ORIGINAL de curación era la correcta).
>
> **Cifras vigentes del estrato B:** Nivel B `scene` F1 **0,333** / `subject` **0,190**
> sobre 2 evaluables · asimetría de FP intacta (26 vs 323 en 11 negativos) · FAR sin
> cambio (3 y 190 FP en 0,1027 h) · Nivel A CR-01 **0,031** / CR-02 **0,018**.

*(Lo que sigue es el protocolo tal como se planificó, conservado por trazabilidad.)*

El §7.2 del 112 identifica el sesgo pero propone poco: revisar solo `v01_c01`. El
problema de fondo es **circularidad**: las 2 correcciones se dispararon porque el
resultado del modelo llamó la atención — solo se re-escrutó donde el modelo discrepaba.
Los episodios donde modelo y GT coinciden nunca recibieron la misma mirada. Con n=5, la
salida total es barata y deja al capítulo blindado ante la pregunta obvia de la defensa.

### B1. Protocolo (a ciegas: sin abrir `alerts.jsonl`, evals ni métricas)

1. Lista: `v01_c01` (CR-01, censurado, ya marcado ⚠️ en su yaml — contraluz),
   `v01_c02` (CR-01, onset t=0), `v04_c01` (CR-01 nocturno), `v04_c02` (CR-01 y CR-02).
2. Por episodio, responder mirando SOLO el video: ¿el estado (casco/chaleco) es
   **observable** en la ventana declarada? ¿el atributo es correcto? ¿los bordes
   temporales son defendibles? Registrar veredicto **también cuando es "confirmado"** —
   la constancia de confirmación es lo citable.
3. Si un episodio cae → cadena completa, la misma del tramo:
   `apply_attribute_corrections.py` (corrección firmada, `previous_value`, `track_id`)
   → re-derivar GT (el GT embebe `annotation` — lección del 111 §4) → re-promote →
   guard `--check` → re-aggregate → **re-evaluar** (evaluate-alerts + agregador; NO
   re-inferir: las detecciones no cambian) → actualizar `metrics.json`, índices y
   registry con banner, como se hizo con v06/v03.
4. Dejar constancia escrita del resultado — una nota corta al 111 o un ✎ acá: *"re-revisión
   ciega 2026-08-XX: N/5 confirmados, M corregidos"*. **Esa frase es la que va al
   informe** junto con "2 de 7": convierte el sesgo del GT en un dato de calidad
   auditado, que fortalece en vez de debilitar.

### B2. Cerrar la marca de `v01_c01`

Resuelto B1, quitar (o resolver en) el yaml el bloque `⚠️ REVISIÓN VISUAL PENDIENTE`
(`datasets-videos/v01_c01.clip.yaml:9`), con el veredicto que sea — si cae, recordar el
punto A4.3: los evaluables siguen en 4; lo que cambia es el conteo de vigentes y la
frase del informe ("3 de 8 producidas" si cae, etc.).

**Verificación del bloque:** `grep -rn "REVISIÓN VISUAL PENDIENTE" e-ovrt_datasets/` →
0; guard `--check` verde; suite de datasets verde; si hubo corrección, diff de métricas
propagado con banner.

---

## Bloque C — Evidencia perecedera y backup (**usuario**, ~2 h)

### C1. URLs de los videos (la media hora del 112 es optimista: es ~1 h)

1. Completar `video_url:` + fecha de acceso en los **18** yamls:
   los 14 `datasets-videos/v*.clip.yaml` (incluido `v08_c01`: excluido del banco pero
   citado "con causa" — su evidencia también debe ser rastreable) + los 4 de
   `_retired/piloto_2026-07-18/`. De paso, verificar el campo de licencia **por video**
   ("público" ≠ CC BY — salvedad ya registrada).
2. Propagar a las **13 copias promovidas** de `processed/clip_bench/meta/`: re-promover
   (no editar a mano). Antes, verificar con el chequeo de re-derivación si el cambio
   toca el GT — no debería (el bloque `license:` no vive en `annotation`), pero la
   lección del 111 manda comprobarlo, no asumirlo.
3. Si el `manifest.yaml` hashea los meta y cambia de sha256: regenerarlo y registrar el
   nuevo hash en el registry con causa *"solo metadata de licencia; GT sin cambios"*
   (mismo patrón que el cambio de manifest del doc 102).
4. Completar `license_registry.md` §Material de VIDEO con las URLs — esto **cierra el
   hallazgo abierto "falta URL por video" de informe/99 §6** (quedaría abierto solo el
   de licencias de catálogos de modelos).
5. Verificación: `grep -rn "video_url: TODO" e-ovrt_datasets/` → **0**;
   `109-verificar-organizacion.py` verde; suite verde.

### C2. Backup a otro disco — ✅ **HECHO por el usuario (2026-08-09)**

> Cerrado. Con esto cae la deuda que arrastraba desde el 05-08 y que el doc 112 §7.5
> señalaba como "riesgo puro": las 4+ jornadas de trabajo verificado ya no viven en un
> solo disco. Lo que sigue abajo es el alcance que se recomendó, conservado como
> referencia para el próximo backup.

El commit no protege lo gitignorado, y ahí vive lo irreproducible:

1. Alcance mínimo del `rsync -a`: los 5 repos **con su `.git/`** (docs no tiene remoto:
   su único clon es este disco) + `docs/operacion/datos/` (evidencia cruda, ~734 MB,
   gitignorada por diseño) + `e-ovrt_datasets/datasets-videos/` (los mp4 del lote:
   evidencia perecedera — YouTube borra) + `cameras/` si hay presets que duelan perder.
2. Verificación: `du -sh` origen vs destino comparables; spot-check de un GT json y un
   mp4 abiertos desde el destino.
3. Anotar fecha del backup donde el usuario lleve ese registro (pendiente desde 08-05).

---

## Bloque D — Protección de cifras del informe (~media jornada, delegable, TDD)

El argumento del 112 §7.3 es correcto y ya tiene **una segunda víctima identificada sin
correr nada** (ver D3). Diseño:

### ✅ D1/D2 EJECUTADOS (2026-08-09) — resultado: 110 tests nuevos, 1 bug real corregido, 1 hallazgo mayor A DECISIÓN DEL USUARIO

> **Suite: 308 → 418, todo verde** (`test_aggregate_clip_campaign_stress.py` +
> `test_score_clip_person_state_stress.py`). La pregunta del 112 §7.3 —"¿qué otra
> métrica tiene una inconsistencia latente que la composición actual no estresa?"—
> tenía respuesta. Siete hallazgos, por severidad:
>
> **(A) BUG REAL CORREGIDO — `f1_micro` devolvía `None` donde el 0,0 estaba medido.**
> Con recall 0,0 y precision 0,0 **medidos**, el `and` de la fórmula cortaba por falsy y
> la campaña salía "no evaluable" (`—`) en vez de F1 0,0: una campaña que falla entera
> se reportaba como no medida — el error simétrico al que el proyecto sí cuidaba.
> Corregido conservando `None` cuando el recall es genuinamente indefinido (todos
> censurados, caso del piloto doc 102). **Impacto en cifras publicadas: CERO**,
> verificado regenerando las campañas de `results/clip_bench/`: las 12 reproducibles
> dan valores **byte-idénticos** (el bug estaba latente: ninguna campaña publicada tiene
> recall 0).
>
> **(B) CORREGIDO (aditivo) — las medias no declaraban su `n` de supervivencia.**
> `t_alert`/`ttfd`/`sdr` promedian solo los clips que alertaron, sin decirlo: `d1`
> reporta t_alert 6.611 ms **sobre 6 de 30 clips**; `g1`, 5.236 ms sobre 29 de 30.
> Compararlos es la trampa F-96 exacta, y el JSON no daba forma de verla. Ahora cada
> media lleva su `*_n` (campos nuevos; ningún valor cambia).
>
> **(C) DOCUMENTADO — `by_condition` doble-cuenta FP** en clips con episodios de ambas
> condiciones (3 en el banco): `d1` tiene 35 FP y la columna suma 41 (+17%). Inherente
> al eval por clip; nota en el JSON + test que fija el invariante `suma ≥ total`.
>
> **(D) ✅ DECISIÓN FIRMADA 2026-08-09 (D-113.2): SE MANTIENE LA REGLA ACTUAL, DECLARADA.**
> El scorer de Nivel A tiene **la misma forma que el bug de FAR**: la persona `unknown`
> sale del denominador (no es evaluable) pero la predicción que cae sobre ella **entra
> al numerador como FP**. Medido sobre el piloto: **48% de los FP de CR-01 (91/190) y
> 22% de los de CR-02 (77/346)** son predicciones sobre personas `unknown`.
> **Decisión: no se cambia el código.** La lectura operativa es la que se adopta —
> **la alerta sobre una persona no juzgable suena igual**; un supervisor la recibe como
> falsa alarma real sin importar que el anotador no pudiera juzgar el estado. La
> alternativa (excluir también del numerador; precision CR-01 0,0052→0,0100, recall
> intacto) **se evaluó y se descartó**. Ningún número publicado cambia.
> **Propagado**: la regla quedó **declarada explícitamente** —no lo estaba antes—
> en `results/bench_nivel_a/index.md` (bloque ⚠️ bajo la tabla de `na1_*`) y en
> `docs/operacion/105` (nota junto a los "190 FP" que ya citaba sin la regla dicha).
> Test con el número en el docstring, sin cambio de comportamiento.
>
> **(E) LATENTE, NO SE DISPARA HOY — asimetría del salteo de frames**: si en un frame
> ninguna persona tiene atributo conocido, se saltea entero (predicciones gratis); si
> hay una sola conocida, las predicciones sobre las `unknown` cuestan FP. Verificado
> que en el piloto no se dispara (FP idénticos con y sin salteo); se disparará en
> material far-field con frames enteros `unknown`. Fijado en test.
>
> **(F) CONVENCIÓN EXPLICITADA — `R = — / F1 = 0,000`** cuando el GT no tiene
> violadores (0 en el denominador): coincide con sklearn `zero_division=0`, no se
> cambió; test que lo fija. Al citar esas filas del doc 105 / `na1_*`, leerlas por su
> precision.
>
> **(G) BRECHA DE REPRODUCIBILIDAD (pre-existente, pendiente):** `i1`/`i2` declaran
> `clips_total = 13` pero archivan **solo 4 `eval_*.json`** — los otros 9 no son
> re-derivables desde los artefactos de la campaña. Toca el anexo de reproducibilidad
> de `informe/99`. Delegable: re-evaluar es barato y determinista (re-evaluar ≠
> re-inferir); queda como ítem nuevo del mapa.
>
> Producción tocada: solo `aggregate_clip_campaign.py` (fix A + campos B + nota C).
> `prf1`/`match_predictions_to_gt` (D/F) **sin tocar**. Nada commiteado.

### D1. Stress-test del agregador (`datasets/scripts/bench/aggregate_clip_campaign.py`)

Fixtures sintéticas de composición extrema, cada una con valores esperados calculados a
mano: **1 solo clip** (positivo / negativo / soak) · **todos negativos** · **todos
positivos** · **0 soak** (FAR debe ser `None`, no 0) · **2+ soaks** · duraciones
heterogéneas (6 s vs 6 min) · clip con `re_alerts` (no deben contar como FP — ADR-011)
· episodios censurados mezclados. Invariantes a asertar: numerador y denominador de
cada tasa salen del MISMO subconjunto; los conteos por clip suman al agregado;
micro-métricas consistentes con los conteos crudos; `None` donde no computable.

### D2. Mismo trato para las otras dos fuentes de cifras del informe

- `score_clip_person_state.py` (Nivel A sobre video, hoy 8 tests): fixtures con 0
  person-frames, todos `unknown`, un solo frame, GT sin la condición.
- `evaluate-alerts` (control-plane): los promedios de `t_alert`/TTFD/SDR sobre
  conjuntos heterogéneos — las dos trampas ya conocidas del doc 96 (SDR no comparable
  entre cadencias; `t_alert` agregado no comparable sin control de supervivencia)
  merecen un test que las haga explotar si alguien las mezcla.

### D3. El `far_basis` engañoso de la gen. 2 preservada — ✅ **HECHO 2026-08-09**

> **Ejecutado, sin tocar los artefactos congelados.** La advertencia quedó en tres
> lugares donde un auditor la va a encontrar: `registry/clip_bench.md` §L1 y el
> `provenance` de los dos `campaign.yaml` (I1 e I2, YAML revalidado). Se agregó además la
> **regla de cita** que faltaba en los tres: el dato es *"3 FP (escena) y 190 (sujeto) en
> 6:09,6 del único clip soak"* y la tasa horaria es una **derivada** sobre 0,1027 h — no
> una hora de operación observada. En el `campaign.yaml` de I2 se sumó también el aviso
> de que **F-111.1 está enmendado**, para que nadie levante el F1 0,200 vs 0,500 como
> ranking.

`metrics.gen2.json` (I1 e I2) conserva el valor buggy (48,7/2.045,6) con el string
`far_basis = "solo clips soak (…)"` — que describe la base **corregida**, no la buggy
con la que ese número se computó. Quien audite la gen. 2 sin leer el 111 leerá una base
falsa. **NO editar el artefacto congelado**: registrar la aclaración en el registry
(§2.1 del estrato B) y en el bloque `provenance` de los `campaign.yaml` de I1/I2:
*"el `far_basis` de metrics.gen2.json es descriptivo de la fórmula corregida; el valor
gen. 2 se computó con la base inconsistente descrita en 111 §6.3"*.

**Verificación del bloque:** suites verdes (datasets + control-plane); las fixtures y
sus esperados commiteables como tests de regresión permanentes.

---

## Bloque E — Videos V1–V3 (caja de tiempo dura: 1 jornada)

Estado: V1/V3/VG1/VG1e + montaje lado-a-lado listos; renderer en
`experimental-setup/defensa/` (`armar_videos.py`; los .mp4 van gitignorados). Falta
**V2**, con la lección registrada: el intento con `gloves` era falso (las cajas caían
sobre el casco) — **auditar visualmente la clase elegida ANTES de afirmar que funciona**.
Regla del timebox: si V2 no sale limpio en la jornada, la decisión de recortarlo es del
usuario y se registra — no se abren frentes nuevos para salvarlo (es exactamente el
"efecto imán" del 112 §7.4).

---

## Bloque F — Redacción §17.x (precondición: A–D cerrados)

B define el `n` definitivo y la frase de calidad del GT; A5 define la etiqueta de
limitación. Con eso, entrar por el kit (informe/97 brief · informe/98 manifiesto ·
informe/99 materiales · los 4 índices de `results/`) y regenerar `informe-project-kit`
al final. **Reglas de encuadre que este tramo dejó fijadas** (checklist para el
capítulo del estrato B):

1. Título por lo que mide: *frontera del sobre de operación*, nunca "validación sobre
   obra real" (112 §6 — y definir el sobre por dentro con los 3 ejes medidos:
   escala × iluminación × oclusión, gate en px², para que "frontera" tenga contenido).
2. FAR: citar **"3 FP en 6:09,6 del único clip soak (0,1027 h)"** con la tasa horaria
   como derivada — no al revés. AF-11/D-90.1 siguen vigentes (limitación precisada, no
   derogada; la regla de 3 pide 3,0 h).
3. Calidad del GT: **"2 de 7 declaraciones producidas resultaron errores, ambas
   sobre-declarando donde el estado no era observable"** + el resultado de la
   re-revisión ciega (B1.4). De frente, como dato de rigor.
4. F-111.1 en su formulación enmendada (A2): la ventaja de la identidad no se reproduce
   en este régimen — sin ranking inverso.
5. Nivel A: la comparación 0,41→0,039 **confunde dominio y modalidad** (bench_obra es
   dominio-rodaje; los 17 clips son pilotos+internet) — una oración de salvedad, y usar
   F-108.3 (Nivel A pésimo con Nivel B perfecto en el mismo clip) como la evidencia que
   separa parcialmente los factores.
6. Cifras SOLO desde los índices de `results/` verificados — nunca tablas-atajo (regla
   vigente desde informe/97).

---

## Lo que NO hacer (ratificado y ampliado)

- No anotar `v08_c01`, no buscar más clips, no correr más barridos **ni re-inferir**
  (re-evaluar sí, si B corrige GT). El material dice lo que tiene para decir.
- No editar `metrics.gen2.json` ni ningún artefacto congelado (D3 se resuelve por
  registry/provenance).
- No crear L9 sin pesar el costo de reabrir informe/99 §6 (A5, decisión del usuario).
- Ninguna capacidad nueva hasta la defensa (ADR-015). Ningún commit/push sin pedido
  explícito. Ningún doc operativo nuevo después de este, salvo la constancia de B1 —
  el 112 §7.4 aplica también a este manual.

## Criterio de terminado global (todo verificable)

```
[x] A1  banners en 102/105/106 + ✎ inline + 3 entradas del índice   ✅ 2026-08-09
[x] A6  sintesis: banner de estado 08-09 + §11 reescrito            ✅ 2026-08-09
[x] A2  F-111.1 enmendado en 111 + espejo 112 §3.3 + filas índice 111/109
        + clip_bench/index.md punto 1 + cuerpo del 109 §9.2          ✅ 2026-08-09
[x] A3  celda combinada cerrada con causa en 110 §4                 ✅ 2026-08-09
[x] A4  112: 6 bloques ✎ (7×, 2-de-7, censura, git, URLs, arco/jornadas,
        tres-documentos, selección de hallazgos, salvedad Nivel A) + índice ✅
[x] A5  DECISIÓN FIRMADA D-113.1 (precisar L4, no crear L9); propagada a
        results/index.md (L1/L4/L6) + docs 103/98 + síntesis + memoria  ✅ 2026-08-09
[x] B   CONSTANCIA escrita (Bloque B): 2/5 confirmados, 3 corregidos ⇒ 5-de-7;
        marca ⚠️ de v01_c01 resuelta; guards y suites verdes; banco 32/15/37
        (manifest 3f14f50a…); re-eval determinista 11/11; métricas propagadas
        con banner a 111/108/110/112, índices y campaign.yaml      ✅ 2026-08-09
[ ] C1  grep "video_url: TODO" → 0; license_registry §VIDEO completo;
        hallazgo "URL por video" de informe/99 §6 CERRADO; verificador 109 verde
[x] C2  backup a otro disco — HECHO por el usuario                    ✅ 2026-08-09
[x] D3  far_basis: advertencia en registry §L1 + provenance de I1/I2 + regla
        de cita ("3 y 190 FP en 6:09,6"), sin editar los artefactos   ✅ 2026-08-09
[x] D1/D2  110 stress-tests, suite datasets 418 VERDE; bug f1_micro
        corregido (impacto cero verificado byte-idéntico)             ✅ 2026-08-09
[x] D-D  DECISIÓN D-113.2: regla `unknown` se MANTIENE, declarada en
        bench_nivel_a/index.md + doc 105                              ✅ 2026-08-09
[x] D-G  cerrado con B: los 13 eval_*.json archivados en I1 e I2 (GT vigente) ✅ 08-09
[ ] E   V1–V3 cerrados o recorte de V2 decidido y registrado
[ ] F   §17.x arrancado con el checklist de encuadre de este doc
```
