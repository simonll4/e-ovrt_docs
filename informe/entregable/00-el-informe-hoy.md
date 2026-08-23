# El informe tal como está hoy

> **Esta carpeta es el entregable, no una fuente.** Es el TFG en sí (`.docx`) más su texto
> extraído para poder leerlo, buscarlo y citarlo desde el resto del set documental.
> **Ningún ajuste se aplica desde acá** — para eso está
> [`../ajustes/00-mapa-de-ajustes.md`](../ajustes/00-mapa-de-ajustes.md).
>
> ⚠️ **El texto extraído es una foto, no un espejo.** Se extrajo del `.docx` en su
> momento y **no se regenera automáticamente**: si alguien edita el Word, estos `.md`
> quedan viejos. Sirven para leer y ubicar secciones, no para verificar el estado actual
> del documento.

---

## Los dos entregables

| Archivo | Qué es | Fecha |
|---|---|---|
| `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` | **El informe completo, v1.1** | 05/06/2026 |
| `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` | El capítulo de **Etapa 3** (Diseño arquitectónico) | — |

> ✎ **2026-08-22 — regla D-C aplicada sobre las dos secciones en desarrollo.** Se re-extrajeron
> ambos textos base desde los `.docx` vigentes, porque el kit estaba entregando material viejo:
> - `90-etapa3-texto-extraido.md` — **regenerado** desde §17.3 **v1.1**. Lo que había era la
>   extracción v0.1: 24.389 palabras contra las **20.622** actuales, y decía "contratos
>   preliminares" donde el informe hoy dice "contratos versionados".
> - `90b-etapa4-texto-extraido.md` — **nuevo**, desde §17.4 **v1.2** (**5.477** palabras). Antes
>   la etapa 4 no tenía texto base extraído y el kit entregaba `borradores/17-4.md`, que es el
>   borrador previo al pegado y anterior al pase 2.

> ✎ **2026-08-19 — pase de cierre de §17.3/§17.4 en curso.** Las versiones de trabajo
> VIGENTES de ambas secciones son los `.docx` de [`desarrollando/`](desarrollando/) —hoy
> **§17.3 v1.1** y **§17.4 v1.2**, con los comentarios del autor—. El standalone
> `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` (16-08) queda como versión PREVIA de
> §17.3. Al cerrar cada sección en el maestro: re-extraer su `.md` y fechar acá (regla D-C).
>
> ✅ **✎ 2026-08-23 — ENTREGA: los tres `.docx` FINALES están en `desarrollando/`, listos
> para integrar al maestro** (desarrollados por ChatGPT bajo las
> `instrucciones-correccion-gpt-2026-08-23.md` y verificados mecánicamente sección por
> sección; las versiones intermedias quedaron en `archivado/`):
> - **§17.3 v1.4** — pases 2 y 3 aplicados completos; 17 tablas renumeradas **39–55**;
>   subsecciones renumeradas (la ex 7.5 es 7.4; las ex 11.2/11.3/11.4 son 11.1/11.2/11.3).
> - **§17.4 v1.5** — pases 2 y 3 aplicados; 6 tablas renumeradas **56–61**; identificadores
>   versionados solo en la tabla de correspondencia (única excepción glosada: la referencia
>   temporal en §17.4.8); conserva el `[[PENDIENTE]]` de URLs del lote (C1).
> - **§17.5 v1.3** — redactada bajo D-P3-6 (8 bloques, por pregunta de medición); tablas
>   **62–67**; 185 cifras verificadas contra la hoja de datos, cero inventadas; **cero
>   `[[CIFRA]]`**: los 4 denominadores restantes se resolvieron el 2026-08-23 contra
>   artefactos primarios — G2A en vivo n = 47/93/55 y captura n = 47–295 por corrida
>   (tabla de corridas del rodaje en el índice de tiempo real), supervivientes por densidad
>   n = 21/20/16 (computados de las campañas de densidad; reproducen exactos los
>   +1.251/+685/+1.175 ms publicados) y preselección 206 de 236 unidades vistas (rama sin
>   filtro 277; tabla A/B de `oak-d-integration.md` del plano de medios). Solo quedan los
>   `[[FIGURA]]` y el `[[PENDIENTE]]` de URLs, que resuelve el usuario.
>
> ✎ **Decisión del usuario (2026-08-23): cada sección se cierra en SU PROPIO documento; la
> integración al maestro se resuelve después.** Consecuencias ya aplicadas: los tres textos
> base del kit se re-extrajeron de los documentos de trabajo (**`90`** ← §17.3 v1.4 ·
> **`90b`** ← §17.4 v1.5 · **`90c`** ← §17.5 v1.3, nuevo), y las notas del generador
> pasaron de "pases 2 y 3 PENDIENTES de aplicar" a **"YA APLICADOS Y VERIFICADOS"** — los
> pases entran al kit como criterio de lectura, no como lista de tareas. Re-aplicarlos sobre
> texto ya corregido es la falla que costó la pasada del 08-23.
>
> **El maestro sigue con §17.3/§17.4 en su versión previa y §17.5 vacía.** Cuando cada
> sección cierre y se integre, re-extraer su `.md` y fechar acá (regla D-C).
>
> ✎ **Las correcciones firmadas son TRES pases, y hay que leer los tres** (✎ 2026-08-22):
> - [`desarrollando/archivado/correcciones-etapa-3-4.md`](desarrollando/archivado/correcciones-etapa-3-4.md)
>   — **pase 1**, ítems E3-01…E3-18 y E4-01…E4-19. Sus decisiones **D1–D4** y la regla de
>   autocontención **siguen rigiendo**. (Se movió a `archivado/` el 2026-08-20; el enlace
>   anterior desde este archivo apuntaba a la ruta vieja.)
> - [`desarrollando/correcciones-etapa-3-4-pase-2.md`](desarrollando/correcciones-etapa-3-4-pase-2.md)
>   — **pase 2**, ítems E3-19…E3-31, E4-20…E4-23 y opcionales C-01…C-04. Continúa la
>   numeración del pase 1, **no reabre** sus decisiones y agrega **D-P2-1…D-P2-6**. Manda
>   sobre el resto del material de estas dos etapas.
> - [`desarrollando/correcciones-etapa-3-4-5-pase-3.md`](desarrollando/correcciones-etapa-3-4-5-pase-3.md)
>   — **pase 3** (2026-08-22), sobre los 40 comentarios traídos en los dos `.docx`. Ítems
>   **E3-32…E3-42** y **E4-27…E4-30**, decisiones **D-P3-1…D-P3-6**, y **dos enmiendas que
>   MANDAN sobre el pase 2**: a **E3-22** (las viñetas que proponía ya existen como prosa) y a
>   **E4-22** (afirmaba que la preselección en el borde no se ejerció, y es falso). Su §D fija
>   las restricciones de redacción de la **etapa 5** — con el esquema temático de organización
>   del §17.5 en **§D.0** (D-P3-6: por pregunta de medición, nunca por cronología de campañas)
>   — y su **§H** es la tabla de verificación cruzada de alineación entre §17.3 y §17.4.
>
> Los tres entran al project-kit: los pases 1 y 2 en las etapas 3 y 4; el pase 3 también en la 5.
>
> ✎ **2026-08-20 — enmienda E4-19 (a E4-14) en el mismo doc de correcciones:** §17.4.8 se
> amplía a cuatro subsecciones ("Construcción del banco temporal y de la referencia humana
> de evaluación": adquisición/rodaje · segmentación con criterios ex-ante · preanotación y
> revisión en CVAT · derivación y congelamiento), con ajuste breve en §17.4.1. Al aplicar
> las correcciones de §17.4, usar E4-19 y NO el texto guía original de E4-14 (quedó
> marcado como enmendado). Kit regenerado ese día.
>
> ✎ **2026-08-22 — cuatro unidades nuevas y una decisión nueva en el pase 2.** **E3-29**
> (§17.3.10.3 reescrita: dos afirmaciones falsas sobre el ledger de entregas y dos límites
> de interpretación ausentes), **E3-30** (§17.3.11.1 se elimina y se absorbe en el
> párrafo introductorio de §17.3.11), **E3-31** + **E4-23** y la decisión **D-P2-5**: los
> identificadores versionados de contrato (`media.detection.v1`, `clip_gt.v2`, …) y los
> literales de protocolo **salen de §17.3 y se declaran en §17.4**, donde la Tabla 63 ya es
> su punto de declaración; §17.3 conserva el versionado como compromiso abstracto. Además,
> **enmienda a E3-28**: `fail-open` pasa a definirse en prosa en §17.3.7.5 en vez de en una
> celda de tabla. Al aplicar §17.3, usar **E3-31 y la enmienda**, no sus versiones previas.
>
> ✎ **2026-08-22 (cont.) — D-P2-6 y E4-24: un identificador se declara UNA vez.** Medido: de
> los 11 identificadores del par, **9 son `.v1`**, así que el sufijo casi nunca informa y sólo
> quiebra el registro del texto. Regla: la **prosa se lee en castellano** ("evento de
> percepción", "alerta interna", "envoltorio del bus") y un identificador literal **nunca es
> sujeto gramatical**; cada uno aparece **una sola vez, en la Tabla 63** de §17.4.2, único
> punto de declaración. Única excepción: la referencia temporal en §17.4.8, donde la versión
> *es* el argumento. El **CamelCase** (`PerceptionEvent`) **no se persigue**: es la
> denominación de diseño de D1 y aparece sólo en celdas de tabla (cero en prosa, verificado).

## El texto extraído

| Archivo | Qué contiene | Etapa del plan |
|---|---|---|
| `96a-informe-v11-frontmatter-intro-objetivos-plan.md` | frontmatter, §11 Glosario, §12 Introducción, §13 Objetivos, §14 Plan de trabajo (**§14.2 define las etapas**) | transversal |
| `96c-informe-v11-estado-del-arte.md` | **§15 Estado del Arte** | **1** |
| `96d-informe-v11-marco-teorico.md` | **§16 Marco Teórico** | **1** |
| `96b-informe-v11-17-1-consolidacion-metodologica.md` | **§17.1 Consolidación Metodológica** + §17.2 Costos | **2** |
| `90-etapa3-texto-extraido.md` | **§17.3 Diseño arquitectónico**, §17.3.1 a §17.3.18 | **3** |
| `96e-informe-v11-cierre-anexos-referencias.md` | §17.4–§17.6 (**los tres placeholders**), §18 Cierre, §19 Anexos A–D, Referencias | 4, 5, 6 |

---

## Lo que está vacío, y es lo que importa

En `96e`, las tres secciones finales del capítulo 17 son placeholders literales:

```
### 17.4. Implementación del prototipo experimental
[Agregado futuro correspondiente a la Etapa 4]

### 17.5. Evaluación y validación del prototipo
[Agregado futuro correspondiente a la Etapa 5]

### 17.6. Documentación técnica, repositorio y evidencias de cierre
[Agregado futuro correspondiente a la Etapa 6]
```

**Ese es el estado del informe hoy:** las etapas 1 a 3 están escritas y necesitan
correcciones; las etapas 4 a 6 no existen todavía. El trabajo experimental que las
sostiene está cerrado y verificado — lo que falta es escribirlas.

## De acá salen los ajustes

| Sección | Ajustes | Documento |
|---|---|---|
| §11–§14 | 7 (`AJ-0.x`) | [`../ajustes/00-mapa-de-ajustes.md`](../ajustes/00-mapa-de-ajustes.md) §4 |
| §15, §16, Anexo A | 16 (`AJ-1.x`) | [`../ajustes/01-etapa-1-fundamentacion-teorica.md`](../ajustes/01-etapa-1-fundamentacion-teorica.md) |
| §17.1, Anexos C y D | 12 (`AJ-2.x`) | [`../ajustes/02-etapa-2-consolidacion-metodologica.md`](../ajustes/02-etapa-2-consolidacion-metodologica.md) |
| §17.3 | 26 (`R-01…R-26`) | [`../ajustes/03-etapa-3-diseno-arquitectonico.md`](../ajustes/03-etapa-3-diseno-arquitectonico.md) |
| §17.4 | 12 (`AJ-4.x`) | [`../ajustes/04-etapa-4-implementacion.md`](../ajustes/04-etapa-4-implementacion.md) |
| §17.5 | 13 (`AJ-5.x`) | [`../ajustes/05-etapa-5-evaluacion-y-validacion.md`](../ajustes/05-etapa-5-evaluacion-y-validacion.md) |
| §17.6 · §18 · §19 | 5 (`AJ-6.x`) | [`../ajustes/06-etapa-6-documentacion-y-cierre.md`](../ajustes/06-etapa-6-documentacion-y-cierre.md) |
