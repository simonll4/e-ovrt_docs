# Archivado de los documentos de trabajo por sección

Cada sección del informe se cierra en su propio `.docx` y pasa por varios pases. Acá quedan las
versiones superadas y el material de trabajo cuya función ya se cumplió.

> **Convención de nombres.** El paréntesis dice por qué está archivado: `(base del pase N…)`,
> `(sugerencias sin aceptar, aceptadas por el usuario en la vX)`, `(superada por…)`. Cuando el
> nombre no lleva paréntesis es una versión intermedia de un ciclo ya cerrado.

## Qué se archiva y qué no

**Se archiva:** toda versión de un `.docx` que otra posterior reemplaza, incluidas las bases de un
pase entregado con sugerencias; los **análisis y lecturas previos** a un pase, cuyo diagnóstico
quedó absorbido por el acta; y **el acta de todo pase que ya no es el último**.

**Se queda en `desarrollando/`:** los `.docx` vigentes, el **acta del pase vigente** —una sola, la
del último— y los **mapas de secciones**, que no son documentos de un pase sino la herramienta con
la que se traduce cualquier unidad de corrección anterior a una renumeración.

> ✎ **2026-09-07.** El criterio se ajustó ese mismo día a pedido del usuario: antes se conservaban
> todas las actas en `desarrollando/`. Ahora la carpeta muestra un solo documento de ajustes, el
> vigente, y el resto de la trazabilidad vive acá.

## Archivado del 2026-09-18: el informe final integró todo

El usuario integró las secciones en Google Docs y bajó **`../E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`**
(portada, §2–§19, Anexos A–F, Referencias; sin comentarios ni cambios rastreados). Por el criterio de esta
carpeta, todo lo que estaba suelto en `desarrollando/` quedó superado y pasó acá con su nombre intacto:

| Grupo | Archivos | Estado al archivarse |
|---|---|---|
| Los cinco `.docx` cerrados por sección | §15/16 **v1.4** · §17.1 **v1.21** · §17.3 **v1.12** · §17.4 **v1.15** · §17.5 **«v1.5»** | Integrados íntegros en el informe final |
| Etapa 6 (§17.6/§18/§19) | v1.0 · v1.1 (sugerencias sin aceptar) · «Copia de … v1.1» · v1.2 · v1.3 (sugerencias sin aceptar) · v1.4 · v1.5 (sugerencias sin aceptar) | Integrada; ⚠ la Figura 4.7 y el Anexo G de la v1.5 (capturas de la consola) **no entraron** en la v0.1 (decisión del usuario al integrar) |
| Secciones iniciales (§2–§14) | v1.0 (sugerencias) · v1.1 (GPT + Claude, sin aceptar) · v1.1 (sugerencias aceptadas) | Integradas |
| Costos (§14.4 / §17.2) | `…Costos_Asociados_v0.1.docx` · `borrador-14-4-…md` · `borrador-17-2-…md` · `analisis-costos-…md` | Integrados con datos reales (sin `[confirmar]`) |
| Mapas de renumeración | `mapa-secciones-17-1-v1-15.md` · `-17-3-v1-6.md` · `-17-4-v1-7.md` | Siguen siendo la traducción de cualquier unidad `AJ-`/`R-`/`E*-` vieja a la numeración de los `.docx` cerrados; los enlaces que los citaban se repararon con `herramientas/reparar_enlaces.py` |
| Actas y análisis del último tramo | `auditoria-bibliografica-2026-09-08.md` · `analisis-comentarios-etapa6-v1.2-…` · `analisis-sugerencias-gpt-secciones-iniciales-…` · `pase-etapa-6-cierre-…` · `pase-etapa-6-v1.3-…` · `pase-etapa-6-v1.5-…` | Aplicadas; ya no hay «acta vigente» porque no hay pase abierto |

Los guiones que produjeron estas versiones (`pase5*_*.py`, `pase_etapa6_*.py`, `pase_secciones_iniciales_v11.py`,
`generar_docx_costos.py`) pasaron a `herramientas/archivado/` el mismo día. En `desarrollando/` quedan el informe
final, la revisión externa de la v0.6 (`revision-informe-final-v0.6-2026-09-15.md`) y esta carpeta.

## Documentos de ajustes archivados

| Documento | Por qué |
|---|---|
| `lectura-transversal-etapas-1-5-2026-09-07.md` | Diagnóstico de las cinco secciones; su lista de trabajo se aplicó entera en el pase 5 y el acta la resume |
| `correcciones-etapa-3-pase-4.md` · `correcciones-etapa-4-pase-4.md` · `correcciones-etapa-5-pase-4.md` | Actas del pase 4, superadas como documento vigente por el acta del pase 5 |
| `analisis-17-3-etapa-3.md` · `analisis-17-4-17-5-etapas-4-5.md` | Análisis previos a esos pases |

## Las bases del pase 5 (2026-09-07)

Las cinco versiones del 06-09 que el usuario bajó de Google Docs quedaron archivadas cuando el
pase 5 entregó su sucesora con sugerencias:

| Base archivada | Su sucesora con sugerencias |
|---|---|
| §15/16 v1.2 | v1.3 |
| §17.1 v1.16 | v1.17 |
| §17.3 v1.8 | v1.9 |
| §17.4 v1.8 | v1.9 |
| §17.5 v1.5 | v1.6 |

**Rechazar todas las sugerencias de la sucesora devuelve exactamente la base**, y eso está
verificado con `herramientas/rechazar_cambios.py`. Los cinco guiones `herramientas/pase5_*.py`
leen desde acá, así que cualquiera de los pases se puede repetir tal cual: se comprobó que el
resultado es idéntico parte por parte.

## Las bases del pase 5b (2026-09-07, mismo día)

El pase 5b llevó la configuración del entrenamiento a §17.4.7 y amplió la remisión de §17.5.6. Es
**incremental**: parte de las versiones vigentes, no de las bases del pase 5, para no pisar los
comentarios que el usuario y su colega tuvieran sin resolver.

| Base archivada | Su sucesora con sugerencias |
|---|---|
| §17.4 v1.9 *(entrega del pase 5)* | v1.10 |
| §17.5 v1.6 *(bajada del usuario con sus 3 comentarios)* | v1.7 |

Rechazar todo en la v1.10 y la v1.7 devuelve la base del **pase 5**, no la del 5b, porque las
sugerencias del 5 siguen sin aceptar y las del 5b se apilan encima. Verificado igual.

## Las bases de los pases 5c y 5d (2026-09-07, mismo día)

| Base archivada | Su sucesora con sugerencias | Pase |
|---|---|---|
| §17.4 v1.10 *(entrega del pase 5b)* | v1.11 | 5c, baja de la fila de pruebas de la Tabla 59 |
| §17.4 v1.11 *(entrega del pase 5c)* | v1.12 | 5d, revisión completa |
| §17.5 v1.7 *(entrega del pase 5b)* | v1.8 | 5d |
| §17.3 v1.9 *(entrega del pase 5)* | v1.10 | 5d |
| §17.1 v1.17 *(entrega del pase 5)* | v1.18 | 5d |

Las cuatro sucesoras del 5d devuelven la base del **pase 5** al rechazar todo, con los mismos
conteos de párrafos, tablas y figuras. `herramientas/pase5d_revision.py` las reproduce parte por
parte desde acá.

> ⚠ **Dos documentos distintos podían llamarse igual.** Había dos §17.4 v1.9 y dos §17.5 v1.6 con
> contenido diferente: la primera entrega del pase 5 y la definitiva en un caso, y la entrega del
> pase 5 frente a la bajada del usuario en el otro. El paréntesis del nombre ahora los distingue.
> La diferencia de la §17.5 tiene una causa que conviene recordar: **resolver un comentario en
> Google Docs lo elimina de la exportación**, así que la bajada trae 8 comentarios míos donde la
> entrega tenía 9. No se perdió ninguno, se cerró uno.

## Las entregas del pase 5/5d y las bajadas del 2026-09-08 (pase 5e)

El usuario aceptó en Google Docs las cinco entregas y bajó los documentos el 09-08. Las entregas
pasan acá con el paréntesis que dice en qué versión las aceptó; las dos bajadas que el pase 5e tomó
como base también, con su propio paréntesis:

| Archivado | Qué es | Sucesora vigente |
|---|---|---|
| §15/16 v1.3 *(entrega del pase 5; base de la bajada v1.3 del 2026-09-08)* | la entrega con sugerencias | §15/16 v1.3 (bajada, mismo número: sigue abierta a los colegas) |
| §17.1 v1.18 *(entrega del pase 5d; el usuario la aceptó como v1.19)* | la entrega con sugerencias | — |
| §17.1 v1.19 *(bajada del usuario 2026-09-08; base del pase 5e)* | la bajada limpia | §17.1 **v1.20** (sugerencias sin aceptar) |
| §17.3 v1.10 *(entrega del pase 5d; el usuario la aceptó como v1.11)* | la entrega con sugerencias | §17.3 **v1.11** (bajada, limpia) |
| §17.4 v1.12 *(entrega del pase 5d; el usuario la aceptó como v1.13)* | la entrega con sugerencias | — |
| §17.4 v1.13 *(bajada del usuario 2026-09-08; base del pase 5e)* | la bajada limpia | §17.4 **v1.14** (sugerencias sin aceptar) |
| §17.5 v1.8 *(entrega del pase 5d; el usuario la aceptó como v1.9)* | la entrega con sugerencias | §17.5 **v1.9** (bajada, limpia) |

`herramientas/pase5e_cierre.py` lee las dos bases desde acá y reproduce v1.14 y v1.20. Rechazar todo
en v1.20 devuelve v1.19 exactamente; en v1.14 devuelve v1.13 más las tres líneas de código que Google
Docs había descartado al aceptar (repuestas en limpio, con comentario; acta §14).

## La segunda bajada del 2026-09-08: el pase 5e aceptado

El usuario aceptó las tres sugerencias del pase 5e y bajó las cinco secciones con números nuevos. Estas
son las que quedaron superadas:

| Archivado | Qué es | Sucesora vigente |
|---|---|---|
| §15/16 v1.3 *(bajada del 09-08; renumerada v1.4 sin tocar el contenido)* | la bajada anterior | §15/16 **v1.4** |
| §17.1 v1.20 *(entrega del pase 5e; el usuario la aceptó como v1.21)* | la entrega con sugerencias | §17.1 **v1.21** |
| §17.3 v1.11 *(bajada del 09-08; renumerada v1.12 sin tocar el contenido)* | la bajada anterior | §17.3 **v1.12** |
| §17.4 v1.14 *(entrega del pase 5e; el usuario la aceptó como v1.15)* | la entrega con sugerencias | §17.4 **v1.15** |
| §17.5 v1.9 *(bajada del 09-08; renumerada v1.5 sin tocar el contenido)* | la bajada anterior | §17.5 **«v1.5»** |

> ⚠ **El número de §17.5 retrocedió.** La sucesora vigente se llama v1.5 y en esta carpeta ya vivía una
> **v1.5 histórica distinta**, la base del pase 5. Los nombres de archivo no chocan gracias al paréntesis,
> pero la cita sí: nombrar «§17.5 v1.5» hoy es ambiguo. Se cita por estado hasta que se renumere en Drive.

También se borraron, en vez de archivarse, siete copias que eran **duplicados exactos** verificados por
sha256: la §17.1 v1.19 y la §17.4 v1.13 que habían vuelto a `desarrollando/` teniendo ya su base acá, y
las cinco que se habían copiado a `borradores/`, que vuelve a estar vacía a propósito.

## El acta de los pases 5 a 5e (archivada el 2026-09-08)

`correcciones-pase-5-etapas-1-5.md` documenta la ronda completa: el pase 5 sobre las cinco
secciones, los incrementales 5b, 5c y 5d del 09-07, la bajada del 09-08 con el pase 5e, y el cierre
con las cuatro secciones cerradas. **La ronda terminó**, así que por el criterio de esta carpeta el
acta se archiva y en `desarrollando/` queda el documento de ajustes vigente, que ahora es la
auditoría bibliográfica.
