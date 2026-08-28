# Revisión previa a la Etapa 2 (§17.1) — estado de alineación al 2026-08-28

> **Qué es este documento.** La revisión que pidió el usuario **antes** de arrancar el pase de
> correcciones de la Etapa 2: qué es el `.docx` que entró a `desarrollando/`, qué manda hoy sobre
> §17.1 (doctrina, handoffs de las etapas 1/3/4/5, pases firmados), qué quedó **desalineado en el
> set** desde que se escribió `ajustes/02` (2026-08-10) y qué decisiones hay que tomar antes de
> escribir la primera unidad `E2-`. **No aplica nada**: es el diagnóstico. El pase propiamente
> dicho será `correcciones-etapa-2.md` (E2-01…, D-E2-…), como en las otras etapas.
>
> Todo lo que se afirma acá se verificó por comando sobre los archivos (§6). Donde dice
> "recomendación" es criterio propio, no decisión tomada.
>
> ✎ **2026-08-28 (misma jornada, después) — RESUELTO.** Las decisiones D-E2-1/2/5/6 fueron firmadas por
> el usuario (las demás adoptadas por recomendación), los 12 desvíos D2-01…D2-12 se corrigieron
> (`operacion/130` §7), el `.docx` se renombró a convención, se extrajo `90f`, el kit se regeneró desde
> cero y el pase quedó escrito en `correcciones-etapa-2.md`. Antes de todo eso se hizo el relevamiento
> exhaustivo de los cinco repos (`operacion/130`), que agregó hechos que este documento no tenía
> (orden de arranque real, `chv` excluido del fine-tuning, umbral 0,35 del tiny-800, Task 4.3 no
> ejecutada). Este archivo queda como constancia del punto de partida.

---

## 0. Veredicto en cuatro líneas

1. **`17.1.docx` es el §17.1 del informe v1.1 sin ninguna corrección aplicada.** Mismos 122 títulos,
   mismos 664 párrafos que la foto `96b`; las únicas 29 diferencias son el rótulo `Nota.` con un
   espacio extra por un *run* de negrita partido. **Cero `AJ-2.xx` aplicados**, sin comentarios del
   autor, sin cambios controlados. Es el punto de partida limpio — pero el kit de la etapa 2 no lo
   sabe todavía (redacta desde `96b`, no desde una extracción propia).
2. **La doctrina vigente es estable y suficiente** (no-anacronismo · autocontención · D-P3-3/D-P3-4 ·
   doctrina de reparto §17.3/§17.4 · régimen "cada sección en su documento") — pero **cinco piezas
   del set están vencidas o con premisa falsa** para esta etapa (§3), dos de ellas 🔴.
3. **Hay ocho decisiones que sólo el usuario puede tomar** antes de que un redactor toque el
   texto (§4). Ninguna bloquea armar el paquete; todas bloquean escribir bien.
4. **La Etapa 1 dejó tres handoffs concretos hacia §17.1** (una remisión rota, un `[[PENDIENTE]]`
   espejo y una dependencia de notación) y el pase 3 de §17.3 dejó **una dependencia inversa**
   (E-DIR/E-IND/E-HYB) que hoy no figura en ninguna ficha de la etapa 2.

---

## 1. El documento recibido — hechos verificados

| Hecho | Valor | Cómo se verificó |
|---|---|---|
| Archivo | `informe/entregable/desarrollando/17.1.docx` · 673.782 bytes · md5 `d8259ef7c6f215efe7ac48de8bee0cd0` · mtime 2026-08-28 02:48 | `ls`, `md5sum` |
| Origen | Sin `docProps/`, sin `word/comments.xml`, sin `word/media/` — export limpio (Google Docs), **no** una copia comentada | `unzip -l` |
| Extensión | **32.669 palabras** extraídas · 122 títulos numerados (§17 → §17.1 → §17.1.1…§17.1.12) | `extraer_informe.py` + verificador |
| Contenido vs `96b` (v1.1) | **664 párrafos = 664 párrafos**; 29 bloques distintos, **todos** `Nota.` → `Nota .` (run partido); palabras normalizadas 31.047 vs 31.083 | diff de párrafos normalizados (sin markdown ni ecuaciones) |
| Ecuaciones | **85 objetos OMML** (`t_alert-system`, `G2A`, `ΔFP_tracker`, `T_persistencia`…). La extracción los marca `⟦ECUACIÓN⟧`; el título de §17.1.7.5.1 queda *"Latencia de Alerta (⟦ECUACIÓN⟧)"* | XML; es la trampa NO-TOCAR nº 1 del mapa (`00` §7) |
| Verificador | **FALLA 1**: *"numeración: §17.1. arranca en 2 y no en 1"* · avisos: Liu 2023/2024 y Wang 2021/2025 (misma autoría, años distintos) · sin cambios controlados | `verificar_entregable.py --seccion 17.1` |
| Causa de la falla | **§17.1.1 está en estilo `Heading 2`** (el nivel de §17.1, no el de sus hermanas §17.1.2…§17.1.12 que son `Heading 3`) **y lleva un tabulador** tras el número en vez de espacio. **Heredado del maestro v1.1** (mismo estilo y tab en `E-OVRT-VDP_v1.1_05062026-sin-indice.docx`). Es la misma clase de defecto que E1-52 | XML de ambos `.docx` |
| Tablas | 23: **Tablas 16–38**; sólo 31, 34 y 35 conservan título en el rótulo | grep |
| Figuras | Ninguna, ni referenciada ni requerida (el plan de figuras no asigna ninguna a §17.1) | manual `08` §6 |
| Marcadores | Ningún `[[…]]`; ningún identificador de andamiaje (`AJ-`/`R-`/`PODA-`/`E1-`) | grep |
| Términos clave | `E-DIR`/`E-IND`/`E-HYB` **0** · `cooldown`/re-alertas **0** (sólo *"evita alertas repetidas sobre una misma situación"* en §17.1.5.3.3, que es la histéresis y está bien) · `"sección 16.7.6"` **1** (§17.1.6.1.1) · `P-E1-{01,02,03,04,06,08}` **9 invocaciones** · `"estado por persona"` **0** · `bench_v3` 0 · `196` 1 · MOT 54 / HOTA 8 · `MQTT` 1 · `OAK` 5 · Anexo B **7 remisiones** (Tablas B.1–B.7 existen en `96e` §19.2) | grep |
| Pesos de las podas | §17.1.6.2 = **5.062** (PODA-12 decía 5.054) · §17.1.10 = **659** (637) · §17.1.4 = **3.261** (3.252) — coinciden dentro del ruido de extracción | `awk`/`wc` |

**Lectura:** el documento es exactamente lo que el régimen del 2026-08-23 pide —la sección en su
propio archivo— y todavía no tiene nombre de convención ni extracción propia. Las cifras de las
fichas y de las podas siguen siendo válidas porque el texto es el mismo.

---

## 2. Lo que manda hoy sobre §17.1 — doctrina y handoffs, con fuente

### 2.1 Reglas vigentes que gobiernan el pase

| Regla | Fuente | Consecuencia concreta para §17.1 |
|---|---|---|
| **No-anacronismo** (mapa regla 5) | `ajustes/02` banner 08-11 · manual `08` §4.6 · INSTRUCCIONES regla 11 | Entran decisiones, definiciones, criterios y **valores de configuración elegidos dentro de rangos declarados**; **no** entran resultados medidos ni estados de implementación. AJ-2.05/2.09/2.11 ya están reescritos así. |
| **Autocontención** | `GUIA-REDACTORES` §3.1 · INSTRUCCIONES regla 3 · manual `08` §4 ✎ | Ningún `AJ-`/`R-`/`ADR`/`F-`/ruta en el texto. Sí: CR-xx, `media.detection.v1`, L1–L8, nombres de configuración, y los `P-E1-xx` (excepción explícita del kit). |
| **D-P3-3** — etapas 1 y 2 al final; §17.3/§17.4 **no dependen** de ediciones futuras en §17.1 | pase 3 §A | Todo lo que §17.3 necesitaba de §17.1 ya se resolvió dentro de §17.3. La etapa 2 hereda **dependencias inversas**, no obligaciones (ver 2.3). |
| **D-P3-4** — un concepto se define donde se decide, en prosa, una sola vez | pase 3 §A | Afecta AJ-2.03 y AJ-2.12: §17.3.13 v1.4 ya tiene *"Definiciones operacionales y criterio de relojes"* (13.2) y *"estados de aplicabilidad"* (13.3). Hay que repartir explícitamente qué define §17.1 (protocolo) y qué materializa §17.3. |
| **Doctrina de reparto** (D2, 08-19) — §17.3 conceptual/paramétrico sin valores numéricos del patrón; §17.4 concreto | pase 1 §D2 · manual `08` §6 ✎ | Los 4.000/7.000 ms viven hoy **sólo en §17.4** (`90b` ×2; `90` ×0; `90c` ×0). AJ-2.01 no puede escribirse como "valores efectivos" sin abrir una tercera casa para el mismo número: en §17.1 va la **decisión de protocolo dentro del rango de la Tabla 24**. |
| **Poda en el mismo pase** · guardrails | manual `08` §4.3 · `ajustes/07` §9 | PODA-12/13/14 se aplican con los AJ. **§17.1.5 y §17.1.7 no se comprimen** (guardrail 2; *"no existe segunda vuelta"*). |
| **Régimen de trabajo** (08-23 / 08-27) | `00-el-informe-hoy` · kit §"Cómo se trabaja" | Cada sección en su documento, sobre copia, sin Drive, con verificador; texto base = **extracción propia** del documento de trabajo (como `90d`), nunca la foto v1.1; nombre `E-OVRT-VDP_Seccion_NN_…_vX.Y.docx` (D 08-28). |
| **D-C** — re-extraer | manual `08` §2 | Precedente etapa 1: se extrajo **al arrancar** (`90d` del `Etapa 1.docx`) y en cada cierre. |
| **Lo que no hay que tocar** | mapa `00` §7 · `ajustes/02` §3 | Ecuaciones OMML "vacías" · `cr01_cr02_v1` como diagnóstico · `re_alerts` ≠ FP · BENCH-196 como histórico · §1 de `nucleo/08` (lo que el informe valida) · la histéresis ya pedida por §17.1.5.3.3. |

### 2.2 Lo que otras secciones toman de §17.1 (intocable sin propagar)

Verificado sobre `90` (§17.3 v1.4), `90b` (§17.4 v1.5) y `90c` (§17.5 v1.3):

- **CPN / EN / TN** — definidos en §17.1.4.2 y sus sub-apartados (pase 3, E3-34 los desduplicó en
  §17.3 apoyándose en que **nacen acá**).
- **Siglas `t_alert-system` · TTFD · SDR** — nacen en §17.1.7.5.1/.2/.3 (E3-39: §17.3 las usa
  "porque la etapa 2 ya las definió"). La primera viaja como ecuación OMML: **verificar en el
  `.docx` final que la sigla se lea** (pase 3 §I, "anomalía §17.1.7.5.1").
- **Tabla 24** (ventanas de persistencia y trade-off por severidad) — §17.3.10.3 la cita y *no la
  toca* (pase 2).
- **G2A / Glass-to-Alert** — la delimitación de tramos es de §17.1.7.2; §17.3 sólo agrega el corte
  por modalidad (pase 2). Ojo: el informe usa **G2A = Glass-to-Algorithm** (subtramo) y
  **Glass-to-Alert** para el tramo hasta la alerta — son dos cosas y las dos están bien.
- **Unidad de conteo del falso positivo** — la regla es de §17.1 (pase 2, Tabla de §17.3.10.3).
- **Escenarios DBE/EBE** — §17.1.3.3 y §17.1.4.4: **la única remisión numérica** que §17.3/§17.4
  hacen a §17.1 es `17.1.4.4` (una vez). §17.5 no remite a §17.1 por número.
- **Descomposición de latencia en cuatro componentes** (`t_capture + t_transport + t_preprocess +
  t_inference`) — la Etapa 1 **reescribió §16.5.2 para usar la notación de §17.1.7** (E1-36/E1-37).
  Si §17.1.7.7 cambia la notación, §16 queda desalineado.

### 2.3 Handoffs recibidos — de la Etapa 1 (cerrada 08-28) y del pase 3 de §17.3

| # | Handoff | Origen | Estado / qué hacer en §17.1 |
|---|---|---|---|
| H-1 | §17.1.6.1.1 remite a *"la sección 16.7.6"* → hoy es **§16.7.3** | E1-53 · `resumen-cambios-etapa-1` §5 | **Corregir** (una aparición, L509 de la extracción). |
| H-2 | Las preguntas rectoras que §17.1 invoca | E1-49 / D-E1-12 | ✅ **Consistente**: §16.7.3 conserva exactamente `P-E1-01, 02, 03, 04, 06, 08` y §17.1 invoca exactamente esas seis (9 veces). Las dos huérfanas (05, 07) se eliminaron; nada que reponer. |
| H-3 | AAIP — `[[PENDIENTE: … documentar el recaudo adoptado en §17.1 y §17.4]]` | D-E1-11 (del equipo) | En §17.1.11 (ético-legales) va el **marcador espejo**, no una redacción. Sigue siendo decisión del equipo. |
| H-4 | Lo que PODA-11 sacó de §16.7.4 *"va a §17.1 como decisión metodológica propia"* | E1-44 | **Verificar** si al aplicar la poda de §16 se decidió conservar algo para reponer en §17.1 (el pase 4 no lo lista como pendiente → probablemente nada; confirmar con el cierre de la etapa 1). |
| H-5 | Rótulo *"Nota"* (§17.1 usa `Nota.` sin formato) | pase 4 de la etapa 1 | **No se toca acá**: es del pase de integración final sobre el maestro. Pero si el pase de la etapa 2 termina con un pase de formato (como el F3 de la etapa 1), conviene ya usar `*Nota.*`. |
| H-6 | **C-1 del pase 1** (bautizar E-DIR/E-IND/E-HYB en §17.1.5.4.2) pasó de obligatorio a **armonizador** con **dependencia inversa** | E3-42 · pase 3 §I | Si se aplica, **hay que recortar la glosa de §17.3.6.4 v1.4 a una remisión**; si no, el informe queda correcto igual. **Ninguna ficha de la etapa 2 lo registra** (ver §3, D2-05). |
| H-7 | Solape §17.3.3.1 ↔ §17.3.3.2 *"depende de qué quede en §17.1 tras la etapa 2"* | pase 3 §I (hilo C8/C9) | Al cerrar la etapa 2, revisar ese solape con E3-21 aplicada. Anotar como salida de la etapa. |
| H-8 | Duplicaciones de tablas verificadas | `ajustes/09` §4 | **Tabla 35** (§17.1.7.9, umbrales por severidad) ≡ tabla del Anexo D, que es superconjunto → eliminar una copia (✅ verificado). Tabla 31 ↔ Anexo C y Tabla 34 ↔ Anexo D: 🟡 confirmar al aplicar. **La decisión §4 de `09` sigue sin casilla marcada.** |
| H-9 | Fine-tuning: encuadre ADR-017, jornada COMPLETA y CERRADA (T1 NO-GO · T2 NO-GO · T3 causa técnica) | acta `128` · kit "Estado vigente" | En §17.1 va **la regla y su criterio** (Tabla 37 ya lo dice); la jornada y sus números son de §17.4/§17.5. Nunca "por tiempo". |

---

## 3. Desvíos del set — corregir ANTES de armar el paquete de la etapa 2

| ID | Sev. | Qué está mal | Dónde | Acción |
|---|---|---|---|---|
| **D2-01** | 🔴 | El kit de la etapa 2 redacta desde **`96b`** (foto del v1.1), cuando el régimen vigente exige la **extracción propia del documento de trabajo** (como `90d`←`Etapa 1.docx`). Hoy da lo mismo en contenido, pero en cuanto GPT entregue una v1.1 el kit quedará detrás —la falla exacta del 08-22 y del 08-23. | `generar_project_kit.py` fuentes de la etapa 2 (L200–214) · `00-el-informe-hoy` tabla de textos base | Renombrar el `.docx` a convención → extraer **`90f-etapa2-texto-extraido.md`** (banner D-C) → fuente 2 ← `90f` con nota *"TEXTO BASE VIGENTE, SIN pases aplicados"* → `96b` queda como foto histórica → regenerar y re-pinnear tests. |
| **D2-02** | 🔴 | El **preámbulo del kit** (viaja en `00-contexto-base` y en los siete `01-etapa-N`) dice que la Etapa 1 *"está a mitad de camino: 12 de los 16 AJ aplicados… el pase de alineación y todas las podas siguen sin aplicarse… §16 sigue apoyándose en el 96d"* y que §17.4 está en **v1.5**. **Falso desde el 08-28**: Etapa 1 CERRADA (v1.0, cinco pases), §17.4 en v1.6. El kit se regeneró hoy y lo sigue diciendo → la fuente es el generador (L418–429). Es "material listo para pegar con contenido vencido" (`09` §3). | `generar_project_kit.py` `BASE_PREAMBLE` ABIERTO-3 | Reescribir el punto 3: etapa 1 cerrada (sólo D-E1-11 abierta); 17.3 v1.4 · 17.4 v1.6 · 17.5 v1.3 · 15+16 v1.0; etapa 2 arranca con su documento de trabajo. |
| **D2-03** | 🟠 | **AJ-2.11** arrastra ✎ del 08-13/08-15 que terminan en *"Resta sólo `full-authorization.json` + RUN manual"* y cifras de costo T1 por extrapolación. **Vencido**: T1 NO-GO (08-17), T2 NO-GO (08-21), jornada cerrada (acta `128`). Es el mismo eco que `09` §3 declaró corregido "en TODOS los ecos" — éste se saltó. El "Estado vigente" del kit lo pisa, pero el redactor lee la ficha. | `ajustes/02` AJ-2.11 | ✎ 08-28: jornada completa y cerrada; en §17.1 sólo la regla (Tabla 37) y el criterio; nada de estado de gates. |
| **D2-04** | 🟠 | **AJ-2.02** tiene **premisa falsa**: dice que *"el §17.1 también describe la política de alerta y arrastra el mismo error"* (cooldown en el motor). §17.1 **no menciona** cooldown, re-alertas, supresión ni re-notificación (0 apariciones; el pase 2 ya lo había verificado: *"cero apariciones en todo el capítulo de Etapa 2"*). | `ajustes/02` AJ-2.02 | Resolver como **⊘ (no se aplica)** o reducir a una regla de conteo en §17.1.7.8.3 (ver D-E2-3). Anotar ✎ en la ficha. |
| **D2-05** | 🟠 | La **dependencia inversa E3-42 ↔ C-1** no está registrada en ninguna ficha de la etapa 2, y **el paquete 2 no incluye el pase 3** (ni su §I). Quien redacte §17.1.5.4.2 no sabe que bautizar los códigos obliga a recortar §17.3.6.4 v1.4, y el informe los definiría dos veces. | `ajustes/02` AJ-2.04 · generador (fuentes etapa 2) | ✎ en AJ-2.04 (o ficha nueva) con el texto guía de C-1 y la obligación de recorte; sumar al paquete 2 el §I del pase 3 y los hechos verificados §E (siglas, CPN/EN/TN). |
| **D2-06** | 🟠 | **AJ-2.03 / AJ-2.12 vs §17.3.13 v1.4** (D-P3-4): §17.3 ya tiene definiciones operacionales, criterio de relojes y estados de aplicabilidad. Sin reparto explícito, el diccionario se escribe dos veces. Además, las dos **métricas derivadas** que AJ-2.03 pide declarar (`t_capture→alert`, `t_compute-budget`) **no aparecen en §17.3, §17.4 ni §17.5** (`90`/`90b`/`90c` = 0): si nadie las usa, declararlas en §17.1 viola el filtro del aporte. | `ajustes/02` AJ-2.03, AJ-2.12 | Fijar el reparto: **§17.1** = nombres, definiciones, umbrales, reglas de lectura, estados de aplicabilidad *como criterio*; **§17.3.13** = materialización (relojes, señales). Decidir si las derivadas entran (D-E2-6 bis). |
| **D2-07** | 🟡 | Punteros a tablas de §17.3 en las fichas (R-14 *"Tabla 46"*, R-02 *"Tabla 44"*, R-25 *"Tabla 50"*, 94 §5) son de la **numeración vieja**; §17.3 v1.4 renumeró a 39–55. No llega al informe (autocontención), sólo confunde al que arma. | `ajustes/02` | ✎ con la numeración v1.4 o quitar el número. |
| **D2-08** | 🟡 | `INSTRUCCIONES-PROJECT.md` lista los `.docx` vigentes como *«§15 "Etapa 1" · §17.3 v1.4 · §17.4 v1.6 · §17.5 v1.3»* — el nombre de la etapa 1 cambió (v1.0 con convención) y **no prevé el de §17.1**. Límite 8.001 caracteres pinneado por test. | `project-kit/INSTRUCCIONES-PROJECT.md` | Actualizar la lista al agregar el `.docx` de §17.1, cuidando el largo. |
| **D2-09** | 🟡 | `00-el-informe-hoy`: la tabla "El texto extraído" dice **`90d` = §15 con 12/16 aplicados** y **`96d` = §16 vigente sin pase** (ambas vencidas: `90d` es §15+§16 final; `96d` superado) y `96b` como texto de §17.1. | `00-el-informe-hoy` §"El texto extraído" | Actualizar con D2-01. |
| **D2-10** | 🟡 | **`90b` sigue extraído de v1.5** y §17.4 está en **v1.6** (deuda ya anotada el 08-27). No bloquea la etapa 2. | `90b` | Re-extraer antes de tocar la etapa 4 (o ahora, es un comando). |
| **D2-11** | 🟡 | **Deuda git ≠ 0 en `docs`**: 18 archivos modificados + ~25 sin seguimiento — todo el trabajo 08-25→08-28 (cierre de etapa 1, verificador nuevo con tests, `90d`/`90e`, kit, archivado, este `.docx`). La memoria decía "deuda 0 al 08-23". | repo `docs` | Del usuario (regla: sin commits sin pedido). Se anota para que no se pierda. |
| **D2-12** | 🟡 | Defecto de formato **heredado del maestro**: §17.1.1 en `Heading 2` + tabulador. El verificador lo detecta pero lo reporta como *"arranca en 2"*. | `.docx` de §17.1 (y maestro) | Corregir en el pase (estilo `Heading 3`, espacio); considerar que el verificador nombre la causa. |

---

## 4. Decisiones que necesita el usuario antes del pase (D-E2-x)

| ID | Pregunta | Recomendación y por qué |
|---|---|---|
| **D-E2-1** | **Alcance del documento de trabajo:** ¿sólo §17.1 (como la etapa 1 = sólo el desarrollo) o §17.1 + Anexos C y D? | **Sólo §17.1** en el `.docx`; los Anexos C y D **se corrigen igual** (AJ-2.07 y H-8 los tocan) y quedan en un `90g` como el Anexo A en `90e`, para que el equipo los arme en §19. El pase debe **decidir** sobre ellos aunque no los edite en el mismo archivo. |
| **D-E2-2** | **Bautismo E-DIR/E-IND/E-HYB:** ¿se aplica C-1 en §17.1.5.4.2 (y se recorta §17.3.6.4) o §17.3.6.4 queda como casa única? | **Aplicar C-1.** Los códigos se usan en §17.3, §17.4 y §17.5 (`90c` ×3), y "un concepto se define donde se decide" apunta a la consolidación metodológica, que es donde las familias se distinguen (§17.1.5.4.2, eje *"Estrategia de detección"*). Costo: una edición de recorte en §17.3 v1.4 → v1.5, ya prevista por E3-42. |
| **D-E2-3** | **AJ-2.02:** ¿⊘ o regla de conteo? | **Regla de conteo mínima en §17.1.7.8.3** (*"Precisiones operativas sobre métricas críticas"*, donde ya se exige declarar la unidad de conteo del FP): que la re-emisión por confirmación repetida del mismo patrón **no cuenta como FP**. Es criterio, no resultado, y protege la precisión reportada en §17.5. |
| **D-E2-4** | **AJ-2.01:** ¿cómo entran 4.000/7.000 ms en §17.1? | Una frase en §17.1.5.3.3 como **decisión de protocolo dentro del rango de la Tabla 24** (3–5 s / 5–10 s), **sin tocar la tabla** y sin "valores efectivos" — esa palabra es de §17.4, que sigue siendo su única casa. |
| **D-E2-5** | **Nivel "estado por persona":** §17.5 organiza por *percepción · estado por persona · alerta* y §17.1 **no pre-registra el nivel intermedio** (0 apariciones; su jerarquía es primario/secundario/conceptual y sus familias son OVD/MOT/pipeline/operativas). ¿Se agrega en §17.1.7 como nivel de análisis o lo introduce §17.5? | **Declararlo en §17.1.7.3.1** como nivel intermedio de análisis (criterio de diseño, va hacia atrás), con una **ficha nueva AJ-2.13** — porque §17.5 ya lo usa como eje y hoy no tiene de dónde colgarlo. |
| **D-E2-6** | **MOT17/OVT-B (§17.1.6.3) y métricas MOT (§17.1.7.4.2):** pre-registradas, no ejercidas (E-10/E-03). ¿Se declara la decisión en §17.1 o se deja intacto? | **Intacto**: el texto ya está en condicional (*"deseables sobre subsets específicamente preparados"*, *"función acotada de verificación"*). Lo no ejercido se reporta en §17.5 bloque 7 (D-P3-6). Anotar **⊘ explícito** en el pase para que el redactor no lo "corrija" ni lo pode. **D-E2-6 bis**: las derivadas `t_capture→alert`/`t_compute-budget` sólo entran si §17.5 las va a usar; hoy no aparecen en `90c`. |
| **D-E2-7** | **AAIP (D-E1-11):** ¿el pase de la etapa 2 espera la decisión del equipo o deja el espejo? | Dejar el **`[[PENDIENTE]]` espejo en §17.1.11.1** con el mismo texto; la decisión sigue siendo del equipo. |
| **D-E2-8** | **PODA-14 mueve detalle de §17.1.4 al Anexo B** — que no está en el paquete 2 (Anexo B es §19.2, sin etapa asignada en el mapa). ¿El pase edita el Anexo B o sólo recorta §17.1.4 dejando las 7 remisiones a B.1–B.7? | **Sólo recortar §17.1.4** y verificar que cada dato que se saca ya esté en B.1–B.7 (existen); lo que no esté, se lista como alta al Anexo B para el equipo (mismo mecanismo que `90e`). |

---

## 5. Pre-flight — secuencia concreta (lo que sigue, en orden)

1. Renombrar `17.1.docx` → **`E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.0.docx`** (convención 08-28).
2. Extraer **`90f-etapa2-texto-extraido.md`** con `extraer_informe.py` (banner D-C, fecha 2026-08-28).
3. Generador: fuente 2 ← `90f` (nota "TEXTO BASE VIGENTE · SIN pases aplicados · el pase de la etapa
   2 es el trabajo a hacer"); `96b` → foto histórica fuera del paquete; sumar pase 3 §E/§I y las
   fichas de `09` §4 que tocan §17.1; **reescribir ABIERTO-3 del preámbulo** (D2-02); actualizar
   tests; `--check --etapa all` y `pytest herramientas/tests` en verde.
4. `ajustes/02`: ✎ 08-28 en AJ-2.11 (D2-03), AJ-2.02 (D2-04), AJ-2.04 (D2-05), AJ-2.03/2.12 (D2-06),
   punteros (D2-07); ficha nueva AJ-2.13 si D-E2-5 se firma.
5. `INSTRUCCIONES-PROJECT.md`: lista de `.docx` vigentes (D2-08), sin pasar de 8.001 caracteres.
6. `00-el-informe-hoy`: tabla de textos base (D2-09) + estado de la etapa 2.
7. Opcional y barato: re-extraer `90b` de v1.6 (D2-10).
8. Escribir **`correcciones-etapa-2.md`** — E2-01… sobre el `90f`, con las 12 fichas AJ-2, las 3
   podas, los 9 handoffs de §2.3 y las decisiones D-E2-1…8 firmadas. Recién ahí se le entrega a GPT.

---

## 6. Verificaciones ejecutadas (para repetirlas)

```
# el documento
md5sum informe/entregable/desarrollando/17.1.docx ; unzip -l … | grep -E 'comments|media|docProps'
python3 herramientas/extraer_informe.py informe/entregable/desarrollando/17.1.docx --out /tmp/17-1.md ; wc -w
python3 herramientas/verificar_entregable.py informe/entregable/desarrollando/17.1.docx --seccion 17.1
# diff de párrafos normalizados contra 96b (sin markdown, sin ⟦ECUACIÓN⟧) → 29 bloques, todos "Nota ."
# estilo del título 17.1.1: zipfile + regex sobre word/document.xml → Heading2 + <w:tab/> (también en el maestro v1.1)
# términos: grep -ciE 'E-DIR|cooldown|16\.7\.6|estado por persona|P-E1-' …
# el set
python3 herramientas/generar_project_kit.py --check --etapa all      # OK, 8 archivos
python3 -m pytest herramientas/tests -q                              # 62 passed, 51 subtests
git -C docs status --short | wc -l                                   # 18 M + ~25 ??
grep -c '4000\|7000' informe/entregable/90*.md                       # 90:0 90b:2 90c:0
grep -n '^#\+ 17\.3\.13' informe/entregable/90-etapa3-texto-extraido.md
grep -oE 'P-E1-[0-9]+' informe/entregable/90d-etapa1-texto-extraido.md | sort -u   # 01 02 03 04 06 08
```
