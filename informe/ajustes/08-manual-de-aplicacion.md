# Manual de aplicación — cómo se pasan los 109 ajustes al informe

> **Qué es esto (2026-08-12).** El mapa (`00`) dice **qué** hay que cambiar. Los documentos
> `01`–`07` dicen **qué dice cada ajuste**. Este dice **cómo se aplica**: en qué superficie
> se edita, en qué orden, quién hace qué, y cuándo una sección se puede dar por cerrada.
>
> **Es el documento que se abre el día 1**, y el único de la carpeta que se actualiza a
> diario (el tablero del §5).
>
> **No repite ningún enunciado ni ninguna cifra.** El contenido vive en su ficha; acá vive
> el procedimiento y el estado.

**Punto de partida:** 91 ajustes (`AJ-` + `R-`) + 18 podas (`PODA-`) = **109 unidades de
trabajo. Cero aplicadas.** Los insumos están completos y verificados; lo que falta es el
pase.

---

## 1. El problema que hay que resolver antes de escribir la primera línea

Cuatro hechos que, juntos, son un conflicto de edición esperando:

1. **El entregable es el `.docx` / Google Docs.** El repo no lo edita: produce la
   instrucción y el texto, y la edición se hace en el documento (regla del `93`, ratificada
   en `gobierno/97` §161).
2. **`entregable/*.md` es una foto, no un espejo.** Se extrajo una vez y **no se regenera**:
   si alguien edita el Word, esos `.md` quedan viejos en silencio. **No existe script de
   extracción** — se verificó: no hay ninguna herramienta en el repo que lo haga.
3. **Ahora hay cuatro manos** (los dos colegas que redactan, el usuario y Claude), donde
   antes había una.
4. **Tres secciones no son corrección, son capítulos nuevos** (§17.4, §17.5, §17.6).

Sin resolver esto, el día 1 produce ediciones pisadas y el día 10 nadie sabe cuál es la
versión buena. Las tres decisiones del §2 lo resuelven.

---

## 2. Las tres decisiones previas — con recomendación

Formato del tablero de decisiones (`operacion/90`): opciones, recomendación, qué desbloquea.
**Son del usuario.** Lo que sigue está escrito asumiendo la recomendación; si cambia una,
cambia el §3 y el §4 de este documento y nada más.

> ✎ **2026-08-16 — las tres decisiones FIRMADAS por el usuario, tal como estaban
> recomendadas**: D-A híbrida · D-B reparto por juicio experimental · D-C re-extracción al
> cerrar cada sección (con extractor, la opción barata). Ajuste operativo firmado el mismo
> día: **la vara del §15 (`AJ-1.01`/`AJ-1.02`/`AJ-1.13`) la redacta Claude como borrador**
> —en `entregable/borradores/`, patrón "texto listo para copiar" del `94`— para desbloquear
> §17.5 sin esperar; los colegas la revisan e integran en Google Docs. El día 1 del pase es
> este: T1 full quedó encolado en Mendieta (job 1167640, `operacion/120`) y la redacción
> arranca mientras se espera ese resultado (`AJ-5.13` sigue ⏳).
> ✎ **2026-08-17: ese resultado llegó — veredicto NO-GO (`operacion/123`), `AJ-5.13`
> desbloqueado y redactable con cifras.**
> ✎ **2026-08-21: T2 también cerró — NO-GO (`operacion/127`) y la jornada E-04 está
> COMPLETA**: la subsección de fine-tuning se redacta con la curva de 3 puntos entera
> (baseline/T1/T2) y la secuencia declarada; instrucciones exactas en el bloque de
> fine-tuning de `GUIA-REDACTORES.md`.
>
> ✎ **2026-08-16 (tercera pasada) — D-A ratificada con el carril ChatGPT**: el maestro
> sigue siendo **Google Docs**; los `.docx` que produce el Project de ChatGPT son **por
> sección, sobre copia del base, y se descartan tras integrarse al maestro**. Las
> instrucciones consensuadas del Project y el knowledge de 4 archivos (2 del kit + el
> informe sin §17.3 + la Etapa 3 standalone): `operacion/122` §6-ter.

### D-A · Dónde se escribe cada cosa → **recomendada: híbrida**

| Opción | Qué implica |
|---|---|
| (a) Todo directo en Google Docs | Simple, pero los tres capítulos nuevos se escriben sin control de versiones, sin revisión por diff y sin poder verificar cifras contra el repo |
| (b) Todo en markdown y una transcripción final | Control total, pero obliga a transcribir ~60 correcciones puntuales que sería trivial hacer en el documento |
| **(c) Híbrida** ✅ | **Corrección donde ya hay texto; redacción en el repo donde no lo hay** |

**La recomendada, en concreto:**

- **Secciones que ya existen** (§11–§14, §15, §16, §17.1, §17.3, §18, §19) → **se editan
  directo en Google Docs**, con la ficha del ajuste al lado. Es lo que ya preveían el `93`
  y el `97`, y es lo correcto: son correcciones puntuales sobre prosa existente.
- **Secciones vacías** (§17.4, §17.5, §17.6) → **se escriben en markdown en el repo**, se
  revisan ahí, y se pegan **una sola vez** cuando la sección está cerrada. Es exactamente el
  patrón con el que se escribió el doc `94` ("texto listo para copiar"), que ya funcionó.

**Dónde viven esos borradores:** `informe/entregable/borradores/17-4.md`, `17-5.md`,
`17-6.md`. El nombre dice *borrador* a propósito, para que nunca se confundan con la foto
extraída (`90`, `96a`–`96e`), que es otra cosa.

### D-B · Quién hace qué → **recomendada: por juicio experimental requerido, no por volumen**

Los dos colegas no participaron del trabajo experimental. `GUIA-REDACTORES.md` los habilita
y está bien hecha, pero el riesgo no es parejo entre secciones:

| Sección | Juicio experimental que exige | Riesgo de un error |
|---|---|---|
| **§17.5** resultados | máximo: escala `AF-1…AF-11`, limitaciones `L1–L8`, las 6 trampas, cada cifra con combinación + material + `n` | **error de fondo en la defensa** |
| **§17.4** implementación | bajo: es descriptiva, y los insumos están verificados con ruta:línea (`92`, `operacion/97`) | recuperable |
| **§15 / §16 / §17.1** | bajo: corrección de prosa y literatura; ahí vive además el 100% de la poda | recuperable |

**Reparto recomendado:**

| Quién | Qué | Por qué |
|---|---|---|
| **Los dos colegas** | Etapa 1 (§15, §16) · Etapa 2 (§17.1) · Etapa 0 (§11–§14), **con la poda de cada sección en el mismo pase** | Es el 60% del volumen y el 100% de la poda, con el juicio experimental más bajo. Y arranca por `AJ-1.01`/`AJ-1.02`/`AJ-1.13`, que es **lo único que bloquea el camino crítico** |
| **Usuario + Claude** | **§17.5**, después §17.4 y §17.6/§18 | Son las que exigen la escala `AF` y las cifras |
| **Usuario** | Etapa 3 — las 26 redlines | Tienen casilla de decisión: son **decisiones de diseño**, no redacción |

> **Si aun así los colegas van a tocar §17.5:** que **no escriban ninguna cifra**. Escriben
> estructura y narrativa y dejan marcado `[[CIFRA: qué hace falta acá]]`; el relleno lo hace
> quien tiene el contexto, contra los índices. Es más lento, pero no arriesga el fondo.

### D-C · Cuándo se re-extrae la foto → **recomendada: al cerrar cada sección**

El `.md` extraído lo citan otros documentos del set. Si queda meses viejo, todo lo que lo
cita empieza a mentir sin avisar. **Regla:** una sección cerrada en Google Docs ⇒ se
re-extrae su `.md` y se anota la fecha en `entregable/00-el-informe-hoy.md`.

**Ojo:** hoy no hay herramienta para hacerlo. O se escribe un extractor una vez (una hora de
trabajo, y sirve para siempre), o se acepta la deriva y se declara en el banner de
`entregable/`. **La primera es la barata.**

---

## 3. El orden de trabajo, resuelto

El mapa (`00` §6) da el orden recomendado. Lo que le falta es la dependencia dura, y con
ella el orden queda cerrado.

**Hay una sola dependencia real entre etapas**, y está declarada en `05` (`AJ-5.11`): el
§17.5 escribe cada conclusión en **tres tiempos** —*qué dice la literatura* → *qué medimos*
→ *qué aporte queda*—, y la vara de la literatura la construyen `AJ-1.01`, `AJ-1.02` y
`AJ-1.13` en el §15. **Hoy esa vara no existe**, así que el §17.5 no tiene contra qué
contrastar.

⇒ **No se empieza por el §17.5. Se empieza por esos tres ajustes del §15**, que son 3 de 16
y desbloquean el camino crítico.

| # | Tramo | Quién | Desbloquea |
|---|---|---|---|
| **0** | `AJ-1.01` · `AJ-1.02` · `AJ-1.13` — **la vara del §15** | colegas *(✎ 2026-08-16: borrador de Claude; colegas revisan e integran)* | **§17.5** |
| 1 | **§17.5** — evaluación y validación | usuario + Claude | §17.6 · §18 |
| 2 | **§17.4** — implementación *(en paralelo con 1)* | usuario + Claude | — |
| 3 | **§17.3** — las 26 redlines, las 7 🔴 primero *(en paralelo)* | usuario | — |
| 4 | **Etapa 1 restante** + poda de §15/§16 *(en paralelo)* | colegas | — |
| 5 | **§17.6 · §18 · §19** | usuario + Claude | — |
| 6 | **Etapa 2** (§17.1) + **Etapa 0** + poda restante | colegas | — |

**Los tramos 1–4 son paralelos de verdad**: tocan secciones distintas del documento y no se
pisan. Eso es lo que hace que cuatro manos rindan cuatro manos.

---

## 4. El pase por sección — el loop repetible

Se hace igual para toda sección, sea corrección o redacción nueva.

1. **Abrir las tres fuentes de esa sección**: la ficha del ajuste (su doc de etapa), la poda
   que le toca (`07` §8) y el inventario de figuras y tablas que aterrizan ahí
   (`gobierno/99` §1).
2. **Leer los banners antes que los cuerpos.** Regla general del set: un documento con ✎ o
   ⚠️ **manda por el banner**, no por el cuerpo. Los cuerpos se conservan para trazabilidad.
3. **Aplicar `AJ-`/`R-` y `PODA-` en el mismo pase.** No dos pasadas: la poda cambia qué hay
   que corregir, y corregir algo que después se elimina es trabajo tirado.
4. **Cada cifra sale de `results/`**, nunca de una tabla-atajo. El formato de cita es
   **combinación + material + `n`** (`GUIA-REDACTORES` §3, con los pares ❌/✅).
5. **Cada afirmación se declara con su fuerza** según la escala `AF-1…AF-11`. No se decide
   al escribir: está pre-registrada.
6. **Chequeo de no-anacronismo.** Si escribiendo §15, §16, §17.1 o §17.3 aparece una cifra
   medida por el proyecto, **estás en la sección equivocada** — eso vive en §17.5/§18.
   Decisiones y correcciones de diseño sí van hacia atrás; resultados no.
7. **Cerrar**: marcar el estado en el tablero (§5); si te apartaste de lo que decía la
   ficha, anotarlo como ✎ **en la ficha**; y re-extraer el `.md` si la sección se editó en
   Google Docs (D-C).

> ✎ **2026-08-16 — regla de autocontención (fijada por el usuario).** El texto del
> informe **no referencia jamás la documentación local de desarrollo**: ni docs de
> `operacion/`, ni ADRs, ni specs, ni fichas `AJ-`/`R-`/`PODA-`, ni IDs internos
> (`F-`, `D-`, `T-FT-`), ni rutas del repo o índices de `results/`. Todo eso guía el
> pase pero es andamiaje local; la procedencia va en las notas `> ✎` de los borradores
> (que no se pegan) y en este tablero. Formulación completa y qué identificadores SÍ
> se usan: `GUIA-REDACTORES` §3.1.

---

## 5. Tablero de aplicación

**Esto es estado, no contenido.** El enunciado de cada ajuste vive en su documento de etapa
y no se copia acá. Etapa 3 conserva además sus casillas granulares
(`acepto`/`modifico`/`rechazo`) en `material-etapa-3/93`, que es donde se registra la
**decisión**; acá solo se registra que el pase se hizo.

Marcá `[x]` al cerrar. `⊘` = resuelto como "no se aplica", con la causa anotada en la ficha.

**Etapa 0 · §11–§14 — 7 · responsable: colegas** *(sus fichas viven en `00` §4, no en un doc propio)*
```
[ ] AJ-0.01   [ ] AJ-0.02   [ ] AJ-0.03   [ ] AJ-0.04   [ ] AJ-0.05   [ ] AJ-0.06
[ ] AJ-0.07
```

**Etapa 1 · §15 · §16 · Anexo A — 16 · responsable: colegas** *(la vara ★: borrador de Claude, ✎ 2026-08-16)*
```
[ ] AJ-1.01 ★  [ ] AJ-1.02 ★  [ ] AJ-1.03   [ ] AJ-1.04   [ ] AJ-1.05   [ ] AJ-1.06
[ ] AJ-1.07    [ ] AJ-1.08    [ ] AJ-1.09   [ ] AJ-1.10   [ ] AJ-1.11   [ ] AJ-1.12
[ ] AJ-1.13 ★  [ ] AJ-1.14    [ ] AJ-1.15   [ ] AJ-1.16
```
★ = **la vara**. Son el tramo 0 del §3: se hacen primero y solos.

**Etapa 2 · §17.1 · Anexos C y D — 12 · responsable: colegas**
```
[ ] AJ-2.01   [ ] AJ-2.02   [ ] AJ-2.03   [ ] AJ-2.04   [ ] AJ-2.05   [ ] AJ-2.06
[ ] AJ-2.07   [ ] AJ-2.08   [ ] AJ-2.09   [ ] AJ-2.10   [ ] AJ-2.11   [ ] AJ-2.12
```

**Etapa 3 · §17.3 — 26 · responsable: usuario** *(la decisión se registra en el `93`)*
```
[ ] R-01 🔴  [ ] R-02 🔴  [ ] R-03 🔴  [ ] R-04 🔴  [ ] R-05 🔴  [ ] R-06 🔴  [ ] R-07 🔴
[ ] R-08     [ ] R-09     [ ] R-10     [ ] R-11     [ ] R-12     [ ] R-13     [ ] R-14
[ ] R-15     [ ] R-16     [ ] R-17     [ ] R-18     [ ] R-19     [ ] R-20     [ ] R-21
[ ] R-22     [ ] R-23     [ ] R-24     [ ] R-25     [ ] R-26
```

**Etapa 4 · §17.4 *(redacción)* — 12 · responsable: usuario + Claude**
```
[ ] AJ-4.01   [ ] AJ-4.02   [ ] AJ-4.03   [ ] AJ-4.04   [ ] AJ-4.05   [ ] AJ-4.06
[ ] AJ-4.07   [ ] AJ-4.08   [ ] AJ-4.09   [ ] AJ-4.10   [ ] AJ-4.11   [ ] AJ-4.12
```

**Etapa 5 · §17.5 *(redacción)* — 13 · responsable: usuario + Claude**
```
[ ] AJ-5.01   [ ] AJ-5.02   [ ] AJ-5.03   [ ] AJ-5.04   [ ] AJ-5.05   [ ] AJ-5.06
[ ] AJ-5.07   [ ] AJ-5.08   [ ] AJ-5.09   [ ] AJ-5.10   [ ] AJ-5.11   [ ] AJ-5.12
[ ] AJ-5.13 ✅ DESBLOQUEADO 2026-08-17 — la jornada CERRÓ: veredicto NO-GO (`operacion/123`)
```

**Etapa 6 · §17.6 · §18 · §19 *(redacción)* — 5 · responsable: usuario + Claude**
```
[ ] AJ-6.01   [ ] AJ-6.02   [ ] AJ-6.03   [ ] AJ-6.04   [ ] AJ-6.05
```

**Poda · transversal — 18 · se aplica con el pase de su sección**
```
[ ] PODA-01  [ ] PODA-02  [ ] PODA-03  [ ] PODA-04  [ ] PODA-05  [ ] PODA-06
[ ] PODA-07  [ ] PODA-08  [ ] PODA-09  [ ] PODA-10  [ ] PODA-11  [ ] PODA-12
[ ] PODA-13  [ ] PODA-14  [ ] PODA-15  [ ] PODA-16  [ ] PODA-17  [ ] PODA-18
```

---

## 6. Lo único que faltaba producir: cinco figuras — ✅ **HECHAS (2026-08-21)**

> ✎ **2026-08-21 — las cinco están producidas y documentadas en
> [`informe/figuras/`](../figuras/README.md)** (PNG 300 dpi + SVG, ancho de diseño 16 cm,
> generadores reproducibles). Con esto **el inventario de materiales del informe queda
> completo**: no falta ningún material para redactar. Detalle, notas al pie listas para
> pegar y las tres advertencias que hay que respetar al citarlas —el módulo de
> distribución va en línea CONTINUA, el orden de arranque es el inverso del flujo de
> datos, y la máquina de estados tiene CINCO estados con la reapertura hacia
> `candidate`— están en el README de esa carpeta. La tabla de abajo queda como registro
> de lo que se pidió; la columna «estado» ya no aplica.

El inventario de `gobierno/99` §1 tiene 23 materiales. **Las 17 tablas (`T-68`…`T-84`) están
en disco y se llenan copiando**, igual que `FIG-D`. Lo que falta son **cinco figuras**, y
son trabajo real que conviene hacer **antes** de escribir la sección que las contiene —un
capítulo escrito sin sus figuras se reescribe.

| Figura | Qué es | Estado | Va en |
|---|---|---|---|
| **FIG-A** | Arquitectura de los dos planos — vista de procesos | 📐 **especificada, no dibujada** (`94` §4) | **§17.4.1** (✎ 08-19: destino único; antes decía §17.3.5 · §17.4) |
| **FIG-B** | Calidad vs densidad (F1 escena y sujeto contra fps) | ⚙ generar desde `results/clip_bench/r{1..6}_*/metrics.json` | §17.5 |
| **FIG-C** | Frame con overlay de alerta confirmada | ⚙ generar con el renderer de `experimental-setup/defensa/` | §17.5 |
| **FIG-E** | Máquina de estados del motor (`inactive → candidate → confirmed → sustained → resolved`) | ⚙ generar desde el contrato `pattern_events` | **§17.3.8.2** (✎ 08-19: antes decía §17.4) |
| **FIG-F** | Frontera de juzgabilidad de 3 ejes (escala × iluminación × oclusión) | ⚙ generar | §17.5 |

**FIG-A es la más urgente de las cinco**: es la respuesta gráfica al *"cómo está hecho"* del
tutor técnico, ya está especificada caja por caja, y la piden dos secciones distintas.

> ✎ **2026-08-19 — enmienda del pase de cierre de §17.3/§17.4**
> (`entregable/desarrollando/correcciones-etapa-3-4.md`, decisiones firmadas por el usuario):
> la doctrina de reparto dejó a §17.3 **sin puertos ni vista de procesos** — FIG-A pasa a
> destino **único §17.4.1** (en §17.3.5 la necesidad de R-09 la cubren la Figura 4.1
> conceptual y la justificación de tecnologías, así que ya **no la piden dos secciones**);
> y la máquina de estados es diseño, no implementación — **FIG-E va en §17.3.8.2 con los
> CINCO estados reales del motor** (el rótulo `open → confirmed → resolved` de la versión
> anterior era una simplificación incorrecta). Con esto, la puerta P4 de §17.4 exige solo
> FIG-A, y la de §17.3 exige FIG-E.

---

## 7. Las cuatro puertas antes de dar una sección por cerrada

| Puerta | Qué se verifica | Cómo |
|---|---|---|
| **P1 · Cifras** | Toda cifra de la sección rastrea a un índice de `results/` | `python3 docs/operacion/datos/96-verificar-indices.py` en verde |
| **P2 · NO-TOCAR** | No se "corrigió" nada de la lista de falsos errores | `00` §7 — el que más muerde son las **ecuaciones de Word que la extracción no captura** y parecen campos vacíos |
| **P3 · Trampas** | Las seis de `GUIA-REDACTORES` §4 | banco **47** (no 34) · FAR se mide pero no sostiene cota · no rankear el estrato B · L4 **precisada**, no levantada · nada del bench de 196 ni de `cb_b01_p7` · fine-tuning **nunca** "por tiempo" (ADR-017) |
| **P4 · Figuras** | Las figuras de la sección **existen**, no están prometidas | §6 de este documento |

---

## 8. Lo que NO bloquea escribir

Por decisión de secuenciación del usuario (2026-08-10, `GUIA-CIERRE`), estos van en **carril
paralelo** y no detienen la redacción:

- **C1 — URL y fecha de acceso de los 18 `clip.yaml`** del lote de internet. Es procedencia
  de las citas del estrato B: **vuelve a ser bloqueante antes de cerrar la versión final**,
  no antes de escribir. Paso a paso en `operacion/113` §C1.
- **E — el video de defensa V2.** Material de defensa, no del informe.

---

## 9. Fuentes

`00-mapa-de-ajustes.md` (§0 correspondencia etapa→sección, §6 orden, §7 NO-TOCAR) ·
`01`…`07` (las fichas) · `material-etapa-3/93` (casillas de Etapa 3) ·
`gobierno/99` §1 (inventario de figuras y tablas, verificado contra disco el 2026-08-12) ·
`gobierno/97` §161 y `gobierno/98` §154 (el `.docx` no se edita desde el repo) ·
`entregable/00-el-informe-hoy.md` (la foto no es espejo) ·
`../../GUIA-REDACTORES.md` (§3 cómo citar, §4 las siete trampas) ·
`../../GUIA-CIERRE.md` (secuenciación del 2026-08-10) · `05` `AJ-5.11` (la única dependencia
entre etapas).
