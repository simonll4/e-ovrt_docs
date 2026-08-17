# 122 — Día 1 del pase de redacción: decisiones firmadas, extractor y primeros borradores (2026-08-16)

- **Contexto:** T1 full quedó encolado en Mendieta la noche anterior (job `1167640`,
  constancia ✎ en [`120`](120-cierre-t031-t032-baseline-26s.md) §5). Orden del usuario de
  hoy: **cerrar documentación y resultados, y arrancar el desarrollo del informe** mientras
  se espera el resultado del entrenamiento. Con esto se levanta el bloqueo que regía sobre
  la redacción ("no arrancar §17.x hasta orden explícita", ratificado el 08-09).
- **Normativa del pase:** [`informe/ajustes/08-manual-de-aplicacion.md`](../informe/ajustes/08-manual-de-aplicacion.md)
  (el manual es la fuente del procedimiento; este doc es la constancia de la jornada).
- **Regla heredada del doc 119:** ninguna fila de evidencia sin haber corrido el comando.
  Todo lo de abajo fue ejecutado y observado el 2026-08-16.

---

## 1. Verificación de arranque (todo corrido hoy)

| Verificador / suite | Resultado |
|---|---|
| `operacion/datos/96-verificar-indices.py` | ✅ exit 0 — 26 cifras, 17 campañas cubiertas, deltas de bootstrap ok |
| `operacion/datos/109-verificar-organizacion.py` | ✅ exit 0 — freeze 189 archivos, sha del manifest ok |
| `operacion/datos/96-verificar-comparabilidad-t1.py` | ✅ 34 idénticos · 0 difieren · 0 fallos |
| Kit (`herramientas/generar_project_kit.py --check`) | ⚠️→✅ **estaba desactualizado** (`01-etapa-activa.md`, esperable: la sesión del 08-15 anotó el 120 sin regenerar) — regenerado y `--check` en verde |
| `herramientas/tests/` | ✅ 29 passed + 42 subtests (incluye los 13 del extractor nuevo, §3) |

## 2. Decisiones firmadas hoy

Las tres decisiones previas del manual `08` §2 quedaron **firmadas por el usuario tal
como estaban recomendadas** (constancia ✎ en el propio manual):

- **D-A — híbrida:** corrección en Google Docs donde ya hay texto; §17.4/§17.5/§17.6 se
  redactan en `informe/entregable/borradores/` y se pegan una sola vez al cerrar.
- **D-B — reparto por juicio experimental:** colegas → Etapas 0/1/2 + poda; usuario →
  redlines de Etapa 3; usuario + Claude → §17.4/§17.5/§17.6/§18.
- **D-C — re-extracción al cerrar cada sección**, con extractor (la opción barata). La
  herramienta se escribió hoy (§3).

**Ajuste operativo firmado el mismo día:** la **vara del §15** (`AJ-1.01`/`AJ-1.02`/
`AJ-1.13`), que el manual asignaba a los colegas y es lo único que bloquea §17.5, la
redacta Claude como **borrador**; los colegas revisan e integran.

**Ratificada (ya estaba firmada el 08-15, doc 119 §7.3):** las tres métricas de alertas
de `report.json` siguen **emitidas y no citables**; `t_alert-system` citable. Sin cambios.

## 3. Herramienta nueva: `herramientas/extraer_informe.py` (la que D-C pedía)

El manual advertía: "hoy no hay herramienta" para re-extraer la foto de `entregable/`.
Ahora hay: extractor `.docx` → markdown en **stdlib puro** (el entorno no tiene pandoc ni
python-docx), hecho con TDD (**13 tests**, `herramientas/tests/test_extraer_informe.py`).

- Títulos por estilo (`Heading N` → `#`×(N+1)), negrita/cursiva, tablas GFM, listas,
  recorte por sección numerada (`--seccion 15` / `17.1`), banner de derivada con fecha.
- **Ecuaciones y figuras quedan con marca visible** (`⟦ECUACIÓN…⟧`/`⟦FIGURA…⟧`) — ataca
  de frente la trampa NO-TOCAR de "ecuaciones que parecen campos vacíos" (`00` §7).
- **Prueba de aceptación contra el `.docx` real:** la extracción de §15 produce
  **títulos idénticos** a la foto vigente (`96c`), marca la única ecuación del capítulo, y
  el documento completo resuelve las secciones tope 2–19.

## 4. Primeros borradores del informe (patrón "texto listo para copiar" del doc 94)

| Borrador | Cubre | Estado |
|---|---|---|
| [`entregable/borradores/vara-15.md`](../informe/entregable/borradores/vara-15.md) | **La vara del §15** (`AJ-1.01`/`AJ-1.02`/`AJ-1.13`): línea base supervisada in-domain, la pregunta que los benchmarks generales no responden, la brecha OVD×EPP. Anclaje propuesto: §15.2.5 + nota a la Tabla 3 | **Listo para revisión de los colegas.** Cero cifras propias (no-anacronismo); cada cifra de literatura con su métrica declarada; referencias para el `96e` con aviso de verificar títulos exactos |
| [`entregable/borradores/17-4.md`](../informe/entregable/borradores/17-4.md) | **§17.4 completo** (los 12 `AJ-4.x`; absorbe la prosa de R-12/R-13/R-26 — anotarlo en `93` al hacer el pase de Etapa 3) | **Borrador completo para revisión del usuario.** Las 4 cifras citadas se verificaron hoy contra sus fuentes (`machinery` 0,662 y 48 líneas/9 min → `results/bench_imagenes/`; 0,789→0,930 → `results/clip_bench/`; 2.203 → `operacion/97`). Pendientes marcados en el propio archivo: **FIG-A y FIG-E sin producir (P4 no pasa)**, una `[DECISIÓN AL INTEGRAR]` (fila de verificación de instrumento: el clip era `cb_b01_p7`, retirado) y un `[ACTUALIZAR A LA ENTREGA]` (estado de la jornada T1) |

**El tablero del manual `08` §5 NO se marca todavía:** un ajuste se marca cuando el pase
llega al documento entregable, no cuando existe el borrador.

## 5. Constancia recuperada

El **envío de T1 full no tenía constancia en `docs/`** (la memoria de sesión lo daba por
documentado en 119/120, pero esos docs cubren las firmas y la baseline, no el `sbatch`).
Anotado hoy como ✎ en `120` §5: autorización emitida y verificada en el clúster
(`gates=7`), `TEST_ONLY` verde, `RUN_T1_10_EPOCHS` encolado como **job `1167640`**
(`ivb`/`multi`, 1 GPU/10 CPU/60 GB/2 h, inicio estimado 2026-08-17 ~06:20), watcher de
finalización en `tmux`. **T-FT-043 CERRADA.**

## ✎ 6-bis. Mismo día, segunda pasada — regla de autocontención y kit para ChatGPT listo

El usuario fijó una regla nueva y pidió dejar el material listo para el Project de
ChatGPT. Hecho:

- **Regla de autocontención (del usuario):** el informe **no referencia jamás la
  documentación local de desarrollo** (docs de `operacion/`, ADRs, specs, fichas, IDs
  internos, rutas del repo e índices) — es andamiaje para guiarnos, no parte del
  entregable. Formulación canónica en **`GUIA-REDACTORES` §3.1**; replicada como regla
  11 de `INSTRUCCIONES-PROJECT.md` y como ✎ en el §4 del manual `08`.
- **El borrador `17-4.md` se limpió contra la regla**: su cuerpo tenía referencias a
  `operacion/97`/`114`, ADR-016/017, E-06/E-10, F-94.1 y a los índices de `results/` —
  todas movidas a bloques `> ✎` de procedencia (que no se pegan) o reescritas como
  prosa autocontenida (la cita queda por combinación + material + n). `vara-15.md` ya
  cumplía.
- **De paso, la regla 8 de `INSTRUCCIONES-PROJECT.md` estaba stale** (declaraba
  pendientes la vista de webconsole, la orquestación y el versionado de distribución —
  cerrados el 08-13). Corregida.
- **Los borradores ahora viajan en el kit**: `vara-15.md` como fuente de la etapa 1 y
  `17-4.md` de la etapa 4 (`generar_project_kit.py`, tests 29 OK). Kit regenerado y
  `--check` verde: `00-contexto-base.md` (~280 KB) + `01-etapa-activa.md` +
  `INSTRUCCIONES-PROJECT.md` para pegar en settings. *(✎ la etapa activa quedó
  finalmente en la **4**, no en la 1 — ver §6-quater.)*

## ✎ 6-ter. Tercera pasada — instrucciones del Project consensuadas y saneo de los DOCX

El usuario trajo su propia versión de las instrucciones del Project y se fusionó con la
del repo (**la fusionada reemplaza a ambas**, `INSTRUCCIONES-PROJECT.md`, 8.001
caracteres — al límite del cuadro de ChatGPT; el test de contrato del generador la
verifica). De la versión del usuario entraron el rol de coautor/revisor, el contexto
institucional estable, el encuadre de tesis ("NO afirma que OVD supere a supervisado"),
el encuadre ético y toda la salida **DOCX + APA 7 + control final**; del repo se
conservaron la jerarquía de verdad explícita, las 12 reglas no negociables (incluida la
autocontención) y el método por unidades `AJ-`/`R-`/`PODA-`.

**Dos decisiones del usuario en la misma pasada:** (a) **el maestro sigue siendo Google
Docs** — los `.docx` que produzca ChatGPT son por sección, sobre copia, y se descartan
tras integrarse (D-A ratificada); (b) el knowledge lleva **4 archivos**: los 2 del kit +
2 DOCX — el informe **sin** la §17.3 y la Etapa 3 **aparte**.

**Hallazgo del saneo de DOCX (verificado con el extractor, diff de títulos):** la §17.3
embebida en el v1.1 completo **NO es la Etapa 3 vigente** (títulos distintos en
17.3.7.3 y toda la estructura de 17.3.14 — es la versión vieja que el banner de la
serie 96 ya declaraba desactualizada), y el standalone vigente
(`E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx`) había sido borrado esta mañana.
Se restauró desde git (la eliminación no estaba commiteada) y se reordenaron los
nombres para no romper la procedencia de la foto: el nombre original
`E-OVRT-VDP_v1.1_05062026-sin-indice.docx` vuelve a contener el **informe completo**
(del que se extrajo la serie 96), y la variante sin §17.3 quedó como
`E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx` (esa es la que sube al Project, junto con el
standalone de Etapa 3).

**Relevamiento final de consistencia (previo a la carga):** el standalone de Etapa 3 es
**idéntico en títulos al doc 90** (diff = 0 líneas: es la vigente); los nombres de
archivo citados en las instrucciones existen tal cual en disco; y la **familia "el
knowledge son dos archivos" estaba stale en 7 sitios** tras pasar a cuatro — corregidos
en fuente (README del kit, `GUIA-REDACTORES` ×2, `gobierno/98`, `gobierno/00-README`,
`00-indice`, `00-indice-informe`), kit regenerado y **el test del contrato del README
actualizado para guardar el contrato nuevo** (cuatro archivos, los DOCX por nombre, y
la prohibición de subir el v1.1 completo). Batería al cierre: 96 ✅ · 109 ✅ · kit
`--check` ✅ · 29 tests ✅ · barrido de menciones stale = 0.

## ✎ 6-quater. El orden del carril ChatGPT, corregido — la etapa activa es la 4

El usuario señaló que lo acordado era **cerrar 4 y 5, después 3, y por último limpiar 1
y 2**. Tiene razón y coincide con el manual `08` §3: de la etapa 1 solo van primero
**tres ajustes** (la vara, `AJ-1.01`/`1.02`/`1.13`), y de ahí se salta a los capítulos
nuevos; el resto de la etapa 1 es el tramo 4 y la etapa 2 el tramo 6. La formulación
"empezar por la etapa 1" que había quedado en el README (y que se repitió al explicar el
flujo) **comprimía mal ese tramo 0** y además ya estaba vencida: **la vara está
redactada** (`borradores/vara-15.md`, 2026-08-16), así que el camino crítico no pasa más
por ahí.

Correcciones aplicadas:

- **La etapa activa del Project pasa a ser la 4** (§17.4: tiene borrador completo y es la
  más barata de cerrar). `README.md` §Primera carga reescrito con el orden real del
  carril: **4 → 5 → 6**, y recién después las correcciones de prosa (etapa 3 = usuario;
  etapas 1, 2 y 0 = colegas).
- **Hueco encontrado al revisar: el paquete de la etapa 5 no incluía la vara.** Sin ella,
  §17.5 no puede escribirse en los tres tiempos que exige `AJ-5.11` (literatura → lo
  medido → el aporte). `vara-15.md` se agregó a las fuentes de la etapa 5 (ya estaba en
  la 1); verificado en el paquete generado.
- Kit regenerado con `--etapa 4` y `--check` verde; 29 tests del generador OK.

## ✎ 6-quinquies. Cerrado se afirma, abierto se marca — y la propagación del envío de T1

El usuario pidió que el knowledge distinga con claridad **lo resuelto (que debe quedar
impactado) de lo abierto (que debe quedar como pendiente)**. Al implementarlo apareció
la deuda: **cinco fuentes del contexto base seguían declarando T1 full como no enviado**
("NO-GO en su último eslabón", "cero jobs full", T-FT-043 `blocked`) — es el mismo
defecto de propagación que costó T-FT-023 y la familia "sin commits" del doc 119.

Lo aplicado:

- **Inventario CERRADO / ABIERTO al frente del contexto base.** Cerrado se escribe como
  hecho, en pasado y sin condicionales (5 ítems: distribución, identidad, comparación de
  estrategias, GT humano, decisiones de la rama de ajuste + envío). Abierto no se
  escribe (3 ítems: resultado del modelo ajustado, cinco figuras sin producir,
  procedencia de origen del lote).
- **Convención de marcadores, obligatoria y greppable**: `[[PENDIENTE: …]]`,
  `[[CIFRA: …]]`, `[[FIGURA: …]]` — nunca se completan con una estimación ni se borran
  para que el texto fluya; viajan hasta el entregable. Replicada como regla 10 de
  `INSTRUCCIONES-PROJECT.md`, que además **corrigió una contradicción recién
  introducida**: su control final mandaba "eliminá placeholders", lo que habría borrado
  justamente estos marcadores.
- **Envío de T1 propagado a las 7 fuentes**: `GUIA-REDACTORES`, `sintesis/…`,
  `nucleo/10` (×2), `decisiones/estado-de-implementacion-adrs`, `operacion/116` y el
  tablero vivo `117` (T-FT-043 → `done` con el job; T-FT-044 → `in_progress`). Los
  cuerpos históricos **se conservan**; la enmienda ✎ va al lado.
- **Guard nuevo con prueba negativa**: el test del generador ya no prohíbe las frases
  superadas (eso rompería la convención de conservar historia) sino que **exige que la
  enmienda del envío esté adyacente** a cada una. Verificado en negativo: al borrar la
  enmienda de `nucleo/10`, el test pasa a rojo; restaurada, verde.
- La distinción que sostiene todo: **enviar no es medir**. El job está encolado y **no
  existe cifra del modelo ajustado**; esa subsección va reservada.

Batería: kit `--check` ✅ · 29 tests ✅ · verificadores 96 y 109 ✅ ·
`INSTRUCCIONES-PROJECT.md` 8.172 caracteres.

## 6. Qué sigue (en el orden del manual `08` §3)

1. **Figuras antes que secciones** (`08` §6): FIG-A y FIG-E cierran §17.4; FIG-B, FIG-C y
   FIG-F preceden a §17.5. **Es lo único que hoy bloquea la puerta P4 del §17.4.**
2. **§17.4** (etapa activa): revisión crítica del borrador e integración al maestro.
3. **§17.5**, en tres tiempos contra la vara (que ya viaja en su paquete); después
   **§17.6/§18/§19** (etapa 6).
4. Usuario: redlines de Etapa 3 (las 7 🔴 primero). Colegas: integrar la vara, después
   resto de Etapa 1 + poda, y por último Etapa 2 y Etapa 0.
5. Al volver el checkpoint de Mendieta: T-FT-050→052 y recién entonces cerrar `AJ-5.13`
   y el `[ACTUALIZAR A LA ENTREGA]` del borrador de §17.4.
   > ✎ **2026-08-17 — el checkpoint volvió y T-FT-050→052 están cerradas: veredicto
   > **NO-GO** ([doc 123](123-cierre-jornada-t1-no-go.md)). **`AJ-5.13` y el
   > `[ACTUALIZAR A LA ENTREGA]` de §17.4 ya tienen su número** y quedan desbloqueados.
