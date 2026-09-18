# Archivado del entregable

Material del entregable que quedó **superado** por una versión posterior. No se borra: sirve para
reconstruir de dónde salió cada cifra y cada texto, y para volver atrás si hiciera falta.

> **Regla de la carpeta.** Acá entra lo superado, no lo histórico-vigente. Un documento que sigue
> siendo la única constancia de un hecho —un acta de pase, un mapa de renumeración— se queda en su
> lugar aunque el pase esté cerrado. El nombre del archivo dice el motivo entre paréntesis cuando
> no es evidente.

## Archivado del 2026-09-18: el informe final está completo

`../desarrollando/E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx` (§2–§19 + Anexos A–F + Referencias)
supersede todo lo que estaba suelto en `entregable/`. Entró acá, con el mismo nombre (git detecta el
movimiento):

| Archivo | Superado por |
|---|---|
| `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` (el maestro, export del 09-08, estilos `Ttulo1…5`) | el Informe Final v0.1; queda junto a su hermano del 08-16 |
| `90-etapa3-texto-extraido.md` · `90b-etapa4` · `90c-etapa5` · `90d-etapa1` · `90e-etapa1-anexo-a-y-referencias` · `90f-etapa2` · `90g-etapa2-anexos-c-y-d` | `../90-informe-final-2026-09-16-v0.1-texto-extraido.md` (la foto del informe completo) |
| `96a-informe-v11-frontmatter-intro-objetivos-plan.md` · `96e-informe-v11-cierre-anexos-referencias.md` | ídem — §11–§14 y §18–§19 ya están en el informe final |
| `resumen-cambios-etapa-1.md` · `resumen-cambios-etapa-2.md` | Comparaban versión inicial vs. final de cada etapa; función cerrada |
| `00-que-va-aca.md` (era el README de `borradores/`, carpeta eliminada) | Ya no queda nada por escribir desde cero |

Los enlaces relativos que apuntaban a estos archivos se repararon con `herramientas/reparar_enlaces.py`.
**Vivo en `informe/entregable/`** queda sólo: los dos tableros `00-*`, la foto `90-informe-final-…` y
`desarrollando/` con el informe final, la revisión externa de la v0.6 y su propio `archivado/`.

## Qué hay (2026-09-07)

| Archivo | Superado por |
|---|---|
| `96b-informe-v11-17-1-consolidacion-metodologica.md` | `90f-etapa2-texto-extraido.md` |
| `96c-informe-v11-estado-del-arte.md` | `90d-etapa1-texto-extraido.md` |
| `96d-informe-v11-marco-teorico.md` | `90d-etapa1-texto-extraido.md` |
| `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico (standalone del 16-08…).docx` | el ciclo de §17.3 en `desarrollando/` |
| `E-OVRT-VDP_v1.1_05062026-sin-etapa3 (variante superada…).docx` | `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` |

Los tres `96*` son fotos del informe v1.1 de junio de 2026, anteriores a todo el pase de
redacción. Se conservan porque varios documentos del set los citan por su número.

**Lo que sigue vivo en `informe/entregable/`:** los textos base `90*` (la foto vigente de cada
sección), `96a` y `96e` (que cubren §11–§14 y §18–§19, sin reemplazo todavía), el informe completo
v1.1 sin índice, los dos tableros `00-*` y los dos resúmenes de cambios.

El archivado de los documentos de trabajo por sección vive aparte, en
[`../desarrollando/archivado/`](../desarrollando/archivado/00-que-hay-aca.md).

## El export del maestro del 2026-08-16 (archivado el 09-08)

`E-OVRT-VDP_v1.1_05062026-sin-indice (export del 2026-08-16, estilos Heading; superado por el export del
09-08 que vive en desarrollando).docx`

El usuario trajo un export nuevo del informe completo el 09-08 y lo puso en `../desarrollando/`, que es
donde vive ahora porque es el **destino de la integración**. Los dos exports traen el mismo contenido: sus
420 títulos son idénticos, uno por uno.

Se conservan los dos porque se distinguen en un detalle que cuesta caro descubrir tarde: **el nuevo nombra
sus estilos de título `Ttulo1`…`Ttulo5` y el viejo `Heading1`…`Heading5`**. Google Docs los nombra según el
idioma de la interfaz en que se editó el documento y les quita los acentos al normalizar el identificador.
Las herramientas ya reconocen las dos familias, pero si alguna vez hay que comparar comportamiento entre
familias, este archivo es el par de control.
