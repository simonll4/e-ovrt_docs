#!/usr/bin/env python3
"""Pase sobre las Secciones Iniciales (§2–§14) · v1.0 con sugerencias de GPT → v1.1 (GPT + Claude, sin aceptar).

⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE si el usuario ya trabajó la v1.1 en Google Docs:
el origen por default es la bajada del 2026-09-12 con las sugerencias de GPT sin aceptar, y volver a
correrlo pisaría lo que haya hecho después (el motor respalda el destino, pero la regla es no hacerlo).

Qué es este pase. GPT revisó §11–§13 del documento v1.0 y dejó 114 cambios controlados y 29
comentarios; un colega dejó 7 comentarios más. El análisis
(`informe/entregable/desarrollando/analisis-sugerencias-gpt-secciones-iniciales-2026-09-12.md`)
concluye que una parte de esas sugerencias actualiza bien el alcance (AJ-0.01, AJ-0.02) y otra parte
adelanta a la introducción la arquitectura y el cierre del informe, o reescribe hipótesis y objetivos
desde el resultado. Este pase aplica ese veredicto SIN resolver nada por el usuario:

MECÁNICA DE CAPAS (leer antes de revisar en Google Docs)
  · Las sugerencias de GPT quedan intactas. Rechazarlas devuelve el texto original de la v1.0.
  · Donde el veredicto es «aceptar con cambios» o «rechazar y retocar el original», Claude tacha la
    inserción de GPT (borrado anidado, como hace Word cuando un revisor edita la inserción pendiente
    de otro) e inserta su alternativa a continuación, como sugerencia propia. Aceptar TODO deja la
    alternativa de Claude; rechazar sólo lo de Claude deja la propuesta de GPT; rechazar TODO deja el
    original.
  · Donde el veredicto es «rechazar» sin retoque, sólo hay un comentario: basta rechazar la
    sugerencia de GPT.
  · Donde el veredicto es «aceptar», no hay marca de Claude (a veces un comentario).
  · Los comentarios de GPT y del colega se conservan con sus anclas; no se resuelven ni se borran.

Propiedad que se verifica al final: quitar sólo las marcas de Claude devuelve el documento de origen
(mismo texto en la vista aceptada y en la vista rechazada, mismas anclas de comentario).

Uso:
    python3 herramientas/pase_secciones_iniciales_v11.py [--origen X.docx] [--destino Y.docx]
"""
from __future__ import annotations

import argparse
import hashlib
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import RPR, TC_RE, TR_RE, Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
ORIGEN = BASE / "E-OVRT-VDP_Secciones_Iniciales_hasta_14_v1.0_sugerencias.docx"
DESTINO = BASE / "E-OVRT-VDP_Secciones_Iniciales_hasta_14_v1.1 (sugerencias GPT + Claude, sin aceptar).docx"
FECHA = "2026-09-12T12:00:00Z"
AUTOR = "Claude"

# Formato de los runs de las celdas del glosario (Times New Roman 12): el motor usa por default un
# rPr mínimo, que en la tabla se vería distinto al resto.
RPR_TABLA = ('<w:rPr><w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" '
             'w:eastAsia="Times New Roman" w:hAnsi="Times New Roman"/><w:b w:val="0"/>'
             '<w:bCs w:val="0"/><w:i w:val="0"/><w:iCs w:val="0"/><w:smallCaps w:val="0"/>'
             '<w:strike w:val="0"/><w:color w:val="000000"/><w:sz w:val="24"/><w:szCs w:val="24"/>'
             '<w:u w:val="none"/><w:shd w:fill="auto" w:val="clear"/>'
             '<w:vertAlign w:val="baseline"/><w:rtl w:val="0"/></w:rPr>')


# ══════════════════════════════════════════════════════════ primitivas de la capa Claude
def _tras_cierre_ins(xml: str, fin: int) -> int:
    """Posición justo después del `</w:ins>` de GPT que sigue a `fin`, saltando el envoltorio
    `w:sdt` con que Google Docs rodea cada sugerencia."""
    cierre = xml.index("</w:ins>", fin)
    resto = Documento.texto_de(xml[fin:cierre]).strip()
    assert not resto, f"queda texto de GPT fuera del tramo reemplazado: {resto[:60]!r}"
    pos = cierre + len("</w:ins>")
    m = re.match(r"\s*</w:sdtContent>\s*</w:sdt>", xml[pos:])
    if m:
        pos += m.end()
    return pos


def _sustituir_en(d: Documento, xml: str, frag: str, nuevo: str, rpr: str) -> str:
    part, ini, fin = d._partir(xml, frag)
    assert "<w:ins " in part[:ini], "el tramo no está dentro de una inserción de GPT"
    medio = d._del(part[ini:fin])
    corte = _tras_cierre_ins(part, fin)
    return part[:ini] + medio + part[fin:corte] + d._ins(nuevo, base=rpr) + part[corte:]


def sustituir(d: Documento, i: int, nuevo: str) -> None:
    """Tacha la inserción de GPT que constituye la unidad `i` (vista aceptada) e inserta `nuevo`
    como sugerencia de Claude, hermana de la de GPT."""
    frag = d.texto(i).strip()
    d.units[i][1] = _sustituir_en(d, d.units[i][1], frag, nuevo, RPR)
    d.log.append(f"u{i}: GPT tachado ({len(frag.split())} palabras) → Claude ({len(nuevo.split())})")


def sustituir_celda(d: Documento, i: int, fila: int, col: int, nuevo: str) -> None:
    tbl = d.units[i][1]
    filas = list(TR_RE.finditer(tbl))
    tr = filas[fila].group(0)
    celdas = list(TC_RE.finditer(tr))
    tc = celdas[col].group(0)
    frag = Documento.texto_de(tc).strip()
    nuevo_tc = _sustituir_en(d, tc, frag, nuevo, RPR_TABLA)
    nuevo_tr = tr[:celdas[col].start()] + nuevo_tc + tr[celdas[col].end():]
    d.units[i][1] = tbl[:filas[fila].start()] + nuevo_tr + tbl[filas[fila].end():]
    d.log.append(f"u{i} celda[{fila}][{col}]: GPT tachado → Claude {nuevo[:40]!r}")


def fila_nueva_tabla(d: Documento, i: int, tras: int, celdas: list[str], modelo: int) -> None:
    """`Documento.fila_nueva` con el rPr de la tabla en los runs insertados."""
    original_ins = d._ins
    d._ins = lambda texto, base=RPR: original_ins(texto, base=RPR_TABLA)  # type: ignore[assignment]
    try:
        d.fila_nueva(i, tras, celdas, modelo=modelo)
    finally:
        d._ins = original_ins  # type: ignore[assignment]


def _asegurar_w14(d: Documento) -> None:
    """El motor escribe `w14:paraId` en los comentarios nuevos; la exportación de Google Docs no
    declara ese prefijo en `word/comments.xml`."""
    c = d.partes.get("word/comments.xml")
    if not c:
        return
    s = c.decode("utf8")
    cab = s[:s.index("<w:comments") + 2000]
    if "xmlns:w14=" not in cab:
        s = s.replace("<w:comments ",
                      '<w:comments xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" ', 1)
        d.partes["word/comments.xml"] = s.encode("utf8")


# ══════════════════════════════════════════════════════════ §7 · palabras clave
def palabras_clave(d: Documento) -> None:
    i = d.unica("Identidad temporal por sujeto", kind="p")
    d.comentario(
        i, "Identidad temporal por sujeto",
        "Recomiendo RECHAZAR y conservar «Seguimiento multiobjeto». Lo que el proyecto no ejerció "
        "son las métricas MOT (MOTA, IDF1, HOTA), no el seguimiento: el tracker está implementado y "
        "su aporte se mide en las alertas (F1 0,930 por sujeto frente a 0,789 por escena, §17.5.4 y "
        "§18.1). Además, §15.3 y §16.4 tratan el seguimiento multiobjeto por ese nombre, y una palabra "
        "clave debe ser un término que un lector busque; «identidad temporal por sujeto» es "
        "vocabulario interno del informe. Si se quiere evitar la connotación de MOT completo, la "
        "alternativa es «Seguimiento temporal de personas».")


# ══════════════════════════════════════════════════════════ §11 · glosario
def glosario(d: Documento) -> None:
    tablas = [k for k, u in enumerate(d.units) if u[0] == "tbl"]
    assert len(tablas) == 1, tablas
    t = tablas[0]
    filas = d.filas(t)
    assert filas[7][0].strip() == "Zero-shot", filas[7][0]
    assert filas[30][0].strip() == "MOTA", filas[30][0]
    assert filas[61][0].strip() == "Latencia por tramo", filas[61][0]
    assert filas[62][0].strip() == "CR-01 / CR-02", filas[62][0]
    assert filas[63][0].strip() == "Vocabulario canónico", filas[63][0]
    assert len(filas) == 69, len(filas)

    # --- Zero-shot: la definición de GPT es sólo la operativa; §15/§16 usan el término en su
    # sentido general 17 veces. Se funden las dos.
    sustituir_celda(
        d, t, 7, 1,
        "Modalidad de inferencia en la que el modelo reconoce conceptos que no fueron objeto de un "
        "entrenamiento supervisado específico. En este trabajo designa el uso de modelos "
        "preentrenados sin ajuste de pesos con datos del dominio; la selección de consultas, "
        "umbrales y resolución es calibración operativa, no entrenamiento.")
    d.comentario_en_celda(
        t, 7, 1, "Modalidad de inferencia en la que el modelo reconoce",
        "ACEPTAR CON CAMBIOS. La definición de GPT reemplazaba la noción general por la operativa "
        "del proyecto, pero §15 y §16 usan «zero-shot» en el sentido de la literatura (17 veces) y "
        "§17.1 en ambos. La alternativa conserva la definición general y agrega la precisión de "
        "GPT, que sí vale: calibrar consultas y umbrales no es entrenar.")

    # --- MOTA / IDF1 / HOTA: el colega propone sacarlas. Posición contraria, con datos.
    d.comentario_en_celda(
        t, 30, 0, "MOTA",
        "Sobre el pedido de quitar MOTA, IDF1 y HOTA: recomiendo CONSERVAR las tres filas. El "
        "glosario define lo que el informe usa, y estas métricas aparecen en §15.3.3 (métricas de "
        "evaluación para MOT), en §17.1.7 (donde se declaran condicionadas) y en §18.6 («la "
        "evaluación MOT ... mantiene los límites ya expuestos»). Un lector que llega a §16 o §18 "
        "necesita saber qué son. Lo que sí conviene es que las tres filas digan lo mismo con la "
        "misma fórmula; hoy ya dicen «no se utilizó para evaluar el prototipo», que es lo correcto.")

    # --- Fila CR-01 / CR-02 (nueva de GPT): sumar los patrones PR-01/PR-02 que usan §17.1 y §17.3.
    sustituir_celda(
        d, t, 62, 1,
        "Condiciones nucleares de evaluación: persona sin casco (CR-01) y persona sin chaleco "
        "reflectivo (CR-02). Los patrones que las operacionalizan se identifican como PR-01 y PR-02.")
    d.comentario_en_celda(
        t, 62, 0, "CR-01 / CR-02",
        "Sobre las siete filas nuevas de GPT («me parecen al vicio»): las revisé una por una contra "
        "el uso real en las secciones vigentes. CR-01/CR-02 es la más necesaria: los códigos "
        "aparecen desde §16.2.2 hasta §18.6 y ahora también en §12.4 y §13.2. La retoco para "
        "sumar los códigos de patrón PR-01/PR-02, que §17.1.5 y §17.3.6 usan y nadie define. "
        "Identidad temporal por sujeto (§17.1, §17.3, §17.5, §18), Granularidad (scene/subject, "
        "§17.3.6, §17.5.4, §18.1), Distribución de alertas (§17.3.7) y FAR (§17.1.7, §18.3) están "
        "justificadas por el mismo criterio: son términos del proyecto que el lector encuentra "
        "sin definición. Evento de percepción se usa 14 veces en §17.3 y 7 en §17.4. La única "
        "que retoco de fondo es «Vocabulario canónico» (ver su comentario). Mi recomendación es "
        "ACEPTAR las siete.")

    # --- Fila Vocabulario canónico: el identificador de configuración no aparece en el informe.
    sustituir_celda(
        d, t, 63, 1,
        "Conjunto de etiquetas de evidencia perceptiva compartido por los componentes de la "
        "plataforma: person, helmet, vest y bare_head. Una etiqueta expresa lo que el detector "
        "localiza y no equivale a una alerta.")
    d.comentario_en_celda(
        t, 63, 1, "Conjunto de etiquetas de evidencia perceptiva",
        "ACEPTAR CON CAMBIOS. AJ-0.02 pide declarar el vocabulario person/helmet/vest/bare_head y "
        "GPT lo hace, pero introduce el nombre de configuración «canonical_v2», que ninguna "
        "sección del informe usa (cero apariciones en §15–§19) y que es un identificador interno "
        "de los repositorios. Se conservan las cuatro etiquetas y la distinción etiqueta/alerta, "
        "que es lo que el lector necesita.")

    # --- Filas que faltan: términos del proyecto con uso intenso en §17–§18 y sin definición.
    # Se insertan tras la última fila original (61) para no anidarlas en los envoltorios de
    # Google Docs de las filas de GPT; en orden inverso porque cada una se coloca justo tras la 61.
    nuevas = [
        ("Vocabulario activo",
         "Conjunto de consultas (prompts) simultáneamente activas en una corrida. Su composición "
         "condiciona el desempeño del detector, por lo que se declara en cada configuración."),
        ("Estrategia de detección",
         "Forma de formular una condición ante el detector. La estrategia directa (E-DIR) describe "
         "la condición completa en un prompt; la indirecta (E-IND) consulta las entidades por "
         "separado y reconstruye la condición con reglas de asociación externas al modelo; la "
         "híbrida (E-HYB) combina ambas bajo una regla explícita."),
        ("G2A",
         "Glass-to-Algorithm. Latencia entre el dequeue de la unidad visual y la disponibilidad "
         "del resultado de inferencia. No incluye la captura ni el transporte hasta el host, que se "
         "informan aparte cuando la fuente aporta una marca de tiempo confiable."),
        ("Episodio",
         "Unidad de la evaluación temporal: intervalo anotado por la referencia humana durante el "
         "cual una condición de riesgo está presente en un clip. Las alertas se juzgan por "
         "episodio, no por cuadro."),
        ("Re-alerta",
         "Nueva confirmación de un patrón sobre el mismo episodio después de su resolución. Se "
         "contabiliza por separado y no se computa como falsa alerta."),
    ]
    for termino, definicion in reversed(nuevas):
        fila_nueva_tabla(d, t, tras=61, celdas=[termino, definicion], modelo=61)
    d.comentario_en_celda(
        t, 62, 0, "Vocabulario activo",
        "Cinco filas que agrego (Vocabulario activo, Estrategia de detección, G2A, Episodio, "
        "Re-alerta), con el mismo criterio que apliqué a las de GPT: son términos propios del "
        "proyecto, sin definición en el texto, con uso intenso en las secciones vigentes "
        "(«vocabulario activo» 20 veces en §17.1–§18; E-DIR/E-IND 27; G2A 26; «episodio» más de "
        "120; «re-alerta» 11). Si el criterio es un glosario mínimo, las prioritarias son G2A y "
        "Estrategia de detección, que son siglas opacas para el tribunal.")


# ══════════════════════════════════════════════════════════ §12.1 · motivación
def seccion_12_1(d: Documento) -> None:
    # u053 ya está aceptado (sin marca): la edición previa perdió «seguridad laboral» del cruce
    # de disciplinas, que es el dominio del trabajo.
    i = d.unica("El presente Proyecto Integrador aborda esta necesidad")
    d.reemplazar(
        i, "procesamiento de video en tiempo real y diseño responsable de sistemas asistivos",
        "procesamiento de video en tiempo real, seguridad laboral y diseño responsable de sistemas "
        "asistivos")
    d.comentario(
        i, "seguridad laboral y diseño responsable",
        "Este párrafo ya venía editado y aceptado en la bajada (no tiene marca de GPT). La versión "
        "del maestro v1.1 nombraba cinco campos y la editada dejó cuatro: se cayó «seguridad "
        "laboral», que es justamente el dominio de aplicación. Lo repongo.")

    # u055: el colega tiene razón («acá ya se pone a explicar lo que hace la plataforma»).
    i = d.unica("Frente a esta restricción, la detección de vocabulario abierto permite")
    sustituir(
        d, i,
        "Frente a esta limitación, los enfoques de detección de vocabulario abierto permiten "
        "formular consultas mediante lenguaje natural. Esta capacidad habilita un modo de "
        "especificación más flexible: el usuario puede definir las entidades de interés sin depender "
        "de un conjunto rígido de etiquetas preestablecidas, aunque una consulta lingüísticamente "
        "válida no garantiza por sí sola una detección correcta. Sobre esa base, el proyecto evalúa "
        "la factibilidad técnica de una plataforma que procese video, interprete consultas "
        "open-vocabulary, detecte entidades y condiciones observables, aplique criterios de "
        "persistencia temporal y genere alertas asistivas trazables.")
    d.comentario(
        i, "Frente a esta limitación, los enfoques de detección de vocabulario abierto",
        "RECHAZAR la de GPT y tomar esta alternativa, que retoca el original. Coincido con el "
        "comentario del colega: en §12.1 todavía no corresponde explicar cómo se articulan "
        "consultas, estrategias y reglas dentro de la plataforma. Del texto de GPT conservo dos "
        "cosas que sí corrigen el original: sale «imágenes de referencia» (la modalidad visual "
        "no se ejerció; sólo aparece en §15) y entra la advertencia de que una consulta válida no "
        "garantiza una detección correcta. También paso a presente («evalúa») y quito «y "
        "académica».")


# ══════════════════════════════════════════════════════════ §12.2 · problema
def seccion_12_2(d: Documento) -> None:
    # u057: el original construía el problema de a poco (riesgos abiertos vs. vocabularios
    # cerrados); GPT lo reemplaza por la pregunta de ingeniería. Se conserva el original con la
    # pregunta al cierre.
    i = d.unica("El problema que orienta el trabajo es determinar cómo transformar")
    sustituir(
        d, i,
        "El problema que orienta el trabajo puede expresarse como una discontinuidad entre la "
        "naturaleza dinámica y semánticamente abierta de los riesgos en obra y el vocabulario fijo "
        "de los sistemas de detección visual closed-set. Mientras que el entorno de construcción "
        "introduce situaciones variables, dependientes del contexto y difíciles de reducir a "
        "categorías fijas, muchos sistemas de visión computacional requieren que las clases "
        "detectables hayan sido definidas, anotadas y entrenadas previamente. De ahí la pregunta que "
        "orienta el desarrollo: cómo transformar condiciones de riesgo expresadas en lenguaje "
        "natural en alertas trazables sobre un flujo de video, y con qué desempeño y limitaciones "
        "puede sostenerse esa transformación.")
    d.comentario(
        i, "El problema que orienta el trabajo puede expresarse como una discontinuidad",
        "RECHAZAR la de GPT y tomar esta alternativa. El original planteaba el problema del "
        "dominio (riesgos abiertos frente a detectores de vocabulario cerrado) y GPT lo sustituye "
        "por la pregunta de ingeniería que responde §18.1. Las dos cosas hacen falta, en ese orden: "
        "primero el problema, después la pregunta. Del texto de GPT tomo la pregunta como cierre "
        "del párrafo y su objeción a «estática», que cambio por «vocabulario fijo».")

    # u058: aceptable; se repone el costo de incorporar una categoría, que el original sí decía.
    i = d.unica("Esta problemática tiene consecuencias prácticas. Una categoría no contemplada")
    sustituir(
        d, i,
        "Esta problemática tiene consecuencias prácticas. En primer lugar, una condición no "
        "contemplada por un detector de vocabulario cerrado queda fuera de su capacidad de "
        "detección aunque sea relevante para la seguridad, e incorporarla exige recolectar datos, "
        "anotar y adaptar el modelo, con un costo en tiempo y recursos. En segundo lugar, en un "
        "enfoque open-vocabulary, incorporar o reformular una consulta no elimina la necesidad de "
        "validar sus detecciones ni las asociaciones que sustentan la condición de riesgo. En tercer "
        "lugar, la detección por fotograma aislado no representa por sí sola situaciones que "
        "dependen de duración o reiteración; el análisis de video requiere mecanismos de "
        "persistencia temporal y criterios explícitos para distinguir evidencia aislada de "
        "episodios que justifican una alerta.")
    d.comentario(
        i, "Esta problemática tiene consecuencias prácticas. En primer lugar",
        "ACEPTAR CON CAMBIOS. El fondo de GPT es correcto y mejora el original (la extensibilidad "
        "sin entrenamiento no elimina el costo de validar, §16.3 y §18.2). Repongo dos cosas que "
        "GPT dejó caer: que la condición no contemplada «sea relevante para la seguridad» y el "
        "costo en datos, anotación y recursos, y devuelvo la enumeración en tres pasos del original, "
        "que ordena la lectura.")

    # u059: la dimensión operativa es motivación legítima; la advertencia de GPT sobre lo que no
    # se mide va a §12.4 (alcance).
    i = d.unica("la supervisión de múltiples cámaras o zonas de trabajo motiva la búsqueda")
    d.comentario(
        i, "No se evalúa la reducción de la carga cognitiva del supervisor",
        "RECHAZAR y volver al original. El párrafo original describe la dimensión operativa del "
        "problema (fatiga, simultaneidad, atención sostenida), que es motivación legítima de una "
        "introducción; GPT la reduce a una frase y le agrega una advertencia de cierre («no se "
        "evalúa la reducción de la carga cognitiva...») que pertenece a los límites, no al "
        "problema. Esa advertencia es válida y la llevo a §12.4, al final del párrafo que ya "
        "delimita el carácter asistivo del sistema.")


# ══════════════════════════════════════════════════════════ §12.3 · enfoque e hipótesis
def seccion_12_3(d: Documento) -> None:
    # u062: la hipótesis se reescribe como espejo de la respuesta de §18.1. Se conserva la
    # original con tres retoques.
    i = d.unica("La hipótesis de trabajo plantea que es técnicamente factible integrar")
    sustituir(
        d, i,
        "La hipótesis de trabajo sostiene que los modelos de detección open-vocabulary, al "
        "permitir expresar condiciones de interés mediante lenguaje natural en tiempo de inferencia "
        "y sin ajustar los pesos del modelo, constituyen un habilitador tecnológico viable para "
        "superar parte de la rigidez de los sistemas closed-set en el monitoreo visual de seguridad "
        "en construcción. Bajo esta hipótesis, una plataforma experimental podría recibir consultas "
        "o patrones como \"persona sin casco\" o \"persona sin chaleco reflectivo\" y transformarlos "
        "en alertas evaluables dentro de un flujo de video. La hipótesis no presupone que un "
        "detector open-vocabulary supere a un detector supervisado ni que la plataforma resulte "
        "apta para cualquier escenario de obra.")
    d.comentario(
        i, "La hipótesis de trabajo sostiene que los modelos de detección open-vocabulary",
        "RECHAZAR la de GPT y tomar esta alternativa. La hipótesis de GPT está redactada desde la "
        "respuesta: calca casi palabra por palabra el primer párrafo de §18.1 («factibilidad "
        "técnica de integrar detección open-vocabulary, procesamiento de video, estabilización "
        "temporal... sin ajustar los pesos del núcleo»). Una hipótesis formulada después del "
        "resultado deja de ser contrastable. Conservo la original y le hago tres retoques que sí "
        "corresponden al planteo inicial: explicito «sin ajustar los pesos del modelo» (la línea "
        "base zero-shot fue premisa desde el inicio, §17.1.9), quito el ejemplo «maquinaria cerca "
        "de peatones» (queda fuera del núcleo evaluado) y agrego la frase de GPT que evita leer la "
        "hipótesis como «OVD detecta mejor». §18.1 sigue respondiéndola tal como está escrito "
        "(«afirmativa en ese alcance y condicionada»).")

    # u063: se reponen presupuesto de latencia y transporte de video.
    i = d.unica("La viabilidad no depende únicamente de detectar objetos en imágenes estáticas")
    sustituir(
        d, i,
        "Sin embargo, esta hipótesis se formula de manera condicionada. La viabilidad no depende "
        "únicamente de detectar objetos en imágenes estáticas, sino de integrar la selección de "
        "modelos visión-lenguaje, la formulación de consultas, la asociación de evidencia, la "
        "estabilidad temporal, los datos de evaluación, el rendimiento en el hardware disponible, "
        "la arquitectura de transporte de video, el presupuesto de latencia, la trazabilidad de "
        "eventos y las salvaguardas de privacidad en el tratamiento de video en contextos "
        "laborales.")
    d.comentario(
        i, "la arquitectura de transporte de video, el presupuesto de latencia",
        "ACEPTAR CON CAMBIOS. La lista de GPT es mejor que la original en tres términos "
        "(asociación de evidencia, datos de evaluación, salvaguardas), pero pierde dos que el "
        "informe trabaja a fondo: el presupuesto de latencia (§17.1.7, §18.4; GPT lo cambió por "
        "«instrumentación de latencia», que es otra cosa) y la arquitectura de transporte de "
        "video (§15.4, §17.3.5). Los repongo. Quito la frase final de GPT («estas dimensiones se "
        "estudian mediante configuraciones y protocolos explícitos...»), que describe el método "
        "de §17.1 y ya está dicho en §12.5.")

    # u064: la cadena operativa sin planos ni jerarquía de §17.5; sin «utilidad operativa».
    i = d.unica("La cadena operativa comprende ingesta o lectura de video, inferencia open-vocabulary en el plano de medios")
    sustituir(
        d, i,
        "Por este motivo, el proyecto se estructura como una plataforma experimental y no como un "
        "producto industrial terminado. El objetivo es construir un prototipo que permita evaluar "
        "el comportamiento del enfoque bajo condiciones controladas y reproducibles. La solución "
        "se organiza alrededor de una cadena operativa mínima: ingesta o lectura de video, "
        "inferencia open-vocabulary, seguimiento temporal, evaluación de patrones de riesgo, "
        "registro de alertas y su distribución. Esta cadena permite analizar no sólo la precisión "
        "de detección, sino también la oportunidad y la estabilidad de las alertas generadas, en "
        "tres niveles de evidencia: la percepción por imagen, el estado por persona y la alerta "
        "por episodio.")
    d.comentario(
        i, "La solución se organiza alrededor de una cadena operativa mínima",
        "ACEPTAR CON CAMBIOS. Dos cosas de GPT son correctas y se conservan: la distribución "
        "entra en la cadena (existe, ADR-016 y §17.3.7) y sale «utilidad operativa» como propiedad "
        "evaluada (no hubo estudio de respuesta de operadores, §18.6). Lo que quito: la asignación "
        "de cada eslabón a un plano («en el plano de medios», «en el plano de control»), que es "
        "arquitectura de §17.3 y ya se anuncia en §12.5 y §13.2, y la frase «este último nivel "
        "representa a la plataforma completa», que es la regla de lectura de §17.5.1. Repongo "
        "«bajo condiciones controladas y reproducibles», que GPT borró. Los tres niveles de "
        "evidencia quedan nombrados en una frase, sin desarrollarlos.")

    # u065: correcta; se repone la condicionalidad por datos y protocolo (ADR-017).
    i = d.unica("La propuesta incluye una rama comparativa de ajuste fino al dominio")
    sustituir(
        d, i,
        "La propuesta incluye una rama comparativa de ajuste fino al dominio, separada del núcleo "
        "sin ajuste de pesos y condicionada a la disponibilidad de datos y a la integridad del "
        "protocolo de comparación. Esta rama contrasta variantes adaptadas con una línea base sobre "
        "un banco común y considera tanto la ganancia en el dominio como la retención de capacidad "
        "open-vocabulary, mediante criterios de adopción definidos antes de la evaluación. La "
        "adaptación no se presupone beneficiosa ni se establece como requisito para construir la "
        "plataforma; su valor se determina a partir de la evidencia experimental.")
    d.comentario(
        i, "condicionada a la disponibilidad de datos y a la integridad",
        "ACEPTAR CON UN CAMBIO. El encuadre de GPT es el correcto (rama separada del núcleo, "
        "criterios de adopción previos, sin adelantar el veredicto de §17.5.6/§18.5). Sólo repongo "
        "la condición de habilitación «por datos y protocolo», que el original tenía y §17.1.9 "
        "mantiene como regla: la rama nunca se encuadra por tiempo ni por cómputo.")


# ══════════════════════════════════════════════════════════ §12.4 · alcance
def seccion_12_4(d: Documento) -> None:
    # u067: es AJ-0.01. Sólo comentario.
    i = d.unica("El núcleo evaluativo está constituido por CR-01")
    d.comentario(
        i, "El núcleo evaluativo está constituido por CR-01",
        "ACEPTAR. Es exactamente el ajuste AJ-0.01: el alcance declarado en el maestro sugería una "
        "cobertura (zonas, maquinaria, obstrucciones) que el desarrollo no afirma. La distinción "
        "núcleo/catálogo coincide con §17.1.2.1 y §18.6.")

    # u068 (original, sin marca): recibe la advertencia que GPT había puesto en §12.2.
    i = d.unica("No se busca construir un sistema de fiscalización automática")
    d.agregar_al_final(
        i, " El trabajo tampoco evalúa el efecto del sistema sobre la carga cognitiva del "
           "supervisor ni sobre la incidencia de accidentes; esos beneficios potenciales no forman "
           "parte de sus resultados.")
    d.comentario(
        i, "El trabajo tampoco evalúa el efecto del sistema",
        "Frase movida desde la propuesta de GPT para §12.2: es un límite del trabajo y este es el "
        "párrafo que delimita lo que el sistema no hace. Coincide con lo que §18.6 declara al "
        "cerrar («no prueba reducción de incidentes, utilidad percibida ... esos resultados "
        "requerirían otra evaluación»).")

    # u069: identidad temporal y distribución, en presente y sin el detalle del registro.
    i = d.unica("La identidad temporal por sujeto se implementó para mantener estados")
    sustituir(
        d, i,
        "El prototipo no realiza reconocimiento de identidad personal ni asocia individuos a "
        "nombres, credenciales o perfiles. La identidad temporal por sujeto mantiene estados "
        "independientes por persona durante una secuencia, sin identificación biométrica. La "
        "plataforma incluye además la distribución de alertas confirmadas hacia un canal externo "
        "mediante MQTT. Permanecen fuera de alcance la integración completa con sistemas externos "
        "de gestión de seguridad, los canales adicionales de notificación y la activación de "
        "infraestructura física de alarmas.")
    d.comentario(
        i, "La plataforma incluye además la distribución de alertas confirmadas",
        "ACEPTAR CON CAMBIOS. El contenido es AJ-0.01 y es correcto: la identidad temporal no es "
        "identidad personal, y la distribución dejó de ser «interoperabilidad futura» (ADR-016). "
        "Cambio la voz: «se implementó e integró» es relato de obra terminada; en la introducción "
        "el informe habla en presente de lo que existe. Quito «con registro de sus resultados de "
        "entrega», que es detalle de §17.4.")

    # u070: DBE/EBE sí; la anticipación del cierre sobre latencia, no.
    i = d.unica("La evaluación distingue dos escenarios complementarios: Escenario A o DBE")
    sustituir(
        d, i,
        "La evaluación distingue dos escenarios complementarios: el Escenario A o DBE, evaluación "
        "diferida y reproducible sobre archivos, y el Escenario B o EBE, evaluación en vivo con "
        "captura continua e intercambio de eventos entre componentes. El material de video "
        "comprende un rodaje controlado y material de obra real, cuyos resultados se interpretan "
        "por separado. La procedencia, la referencia humana y las condiciones de observabilidad de "
        "los datos delimitan qué conclusiones pueden sostenerse en cada escenario.")
    d.comentario(
        i, "La evaluación distingue dos escenarios complementarios",
        "ACEPTAR CON CAMBIOS. Los dos escenarios con su nombre (DBE/EBE, ya definidos en el "
        "glosario) mejoran el original, y la separación rodaje/obra real es una condición de "
        "trabajo real. Quito la última frase de GPT («el funcionamiento en vivo no equivale por sí "
        "mismo al cumplimiento del presupuesto de latencia ni a una validación operativa general»): "
        "es la conclusión de §18.4 puesta en la introducción, y se lee como escrita después de "
        "medir. También quito «estrato», que es jerga de §17.5.")

    # u071: aceptable tal cual.
    i = d.unica("El trabajo utiliza modelos preentrenados y herramientas disponibles")
    d.comentario(
        i, "El trabajo utiliza modelos preentrenados y herramientas disponibles",
        "ACEPTAR. Pasa a presente lo que existe (voz del informe) y conserva los criterios de "
        "selección. Que el entrenamiento desde cero quede fuera de alcance es correcto y sigue "
        "vigente.")


# ══════════════════════════════════════════════════════════ §12.5 · enfoque metodológico
def seccion_12_5(d: Documento) -> None:
    i = d.unica("El diseño arquitectónico define los módulos, los flujos de datos, los contratos de interfaz")
    sustituir(
        d, i,
        "El diseño arquitectónico define los módulos, los flujos de datos, los contratos de "
        "interfaz y la separación entre el plano de medios, el plano de control y la distribución "
        "de alertas. La implementación materializa esas decisiones en un prototipo reproducible e "
        "incorpora el soporte experimental y los bancos de evaluación. La evaluación experimental "
        "mide percepción, estado por persona, alertas por episodio y rendimiento de ejecución; el "
        "análisis de esos resultados delimita el alcance de la factibilidad, sus limitaciones y "
        "las líneas de continuidad.")
    d.comentario(
        i, "sus limitaciones y las líneas de continuidad",
        "ACEPTAR CON CAMBIOS. El mapa de lectura actualizado es correcto (las tres instancias "
        "existen: §17.3, §17.4, §17.5). Repongo dos salidas que el original prometía y GPT borró: "
        "«identificar dificultades, discutir limitaciones y proponer líneas futuras», que son "
        "exactamente §18.6 (limitaciones y líneas de continuidad). Sin eso, la introducción deja "
        "de anunciar una parte del cierre.")

    i = d.unica("Los anexos reúnen información técnica complementaria y condiciones de reproducibilidad")
    d.comentario(
        i, "Los anexos reúnen información técnica complementaria",
        "ACEPTAR. Describe el reparto cuerpo/anexos/artefactos tal como quedó en §17.6 y §19, sin "
        "rutas ni referencias a documentación interna.")


# ══════════════════════════════════════════════════════════ §13 · objetivos
def seccion_13(d: Documento) -> None:
    # 13.1
    i = d.unica("sustentada en el análisis crítico de sus fundamentos y alternativas tecnológicas")
    d.comentario(
        i, "sustentada en el análisis crítico de sus fundamentos y alternativas tecnológicas",
        "RECHAZAR y conservar el objetivo general original. Los objetivos son el compromiso "
        "inicial que §18.6 evalúa («el objetivo general ... se alcanzó en el alcance documentado»); "
        "reescribirlos después del resultado invierte esa lógica. El original ya dice diseñar, "
        "implementar y evaluar la factibilidad técnica «mediante la integración de modelos de "
        "visión-lenguaje, procesamiento de video de baja latencia, seguimiento temporal, patrones "
        "de riesgo y mecanismos de alerta evaluables bajo condiciones controladas»: todo eso se "
        "hizo. La versión de GPT agrega «sustentada en el análisis crítico de sus fundamentos», que "
        "es el objetivo específico 1, y quita «bajo condiciones controladas». Criterio general para "
        "§13: como §14 (plan y cronograma) queda congelado en su primera versión, §13 no debería "
        "alejarse del plan; sólo se corrige lo que quedó falso.")

    # 13.2 · objetivo 1
    i = d.unica("Analizar críticamente el estado del arte y los fundamentos técnicos y metodológicos")
    d.comentario(
        i, "Analizar críticamente el estado del arte y los fundamentos técnicos y metodológicos",
        "RECHAZAR y conservar el original. GPT quita tres de los cuatro ejes que la Etapa 1 "
        "efectivamente cubrió: «normativos» (§16.2.1 Marco normativo de referencia), «seguimiento "
        "multiobjeto» (§15.3 y §16.4 llevan ese nombre) y «transmisión de video en tiempo real» "
        "(§15.4). También coincide con las actividades de §14.2.1, que no se tocan. El original es "
        "exacto respecto de lo que se hizo.")

    # 13.2 · objetivo 2
    i = d.unica("Definir y operacionalizar las condiciones nucleares CR-01 y CR-02")
    d.comentario(
        i, "Definir y operacionalizar las condiciones nucleares CR-01 y CR-02",
        "RECHAZAR y conservar el original. El objetivo se planteó sobre «un conjunto de "
        "condiciones de riesgo visualmente observables» y eso es lo que se hizo: un catálogo de "
        "seis, con dos en el núcleo evaluado (§17.1.2.1). Reducir el objetivo a CR-01 y CR-02 lo "
        "ajusta al resultado, y además pierde «niveles de severidad», que la plataforma sí define "
        "(PR-01 alto, PR-02 medio). §18.6 ya dice que «las condiciones mínimas evaluables se "
        "concretaron en CR-01 y CR-02»: esa es la frase que debe cargar con la reducción, no el "
        "objetivo.")

    # 13.2 · objetivo 3: se conserva el original sumando la distribución.
    i = d.unica("Diseñar una arquitectura modular que separe percepción en el plano de medios")
    sustituir(
        d, i,
        "Diseñar una arquitectura modular de procesamiento de video en tiempo real que distinga el "
        "plano de medios y el plano de control, permitiendo integrar de manera desacoplada "
        "componentes de ingesta, inferencia, seguimiento temporal, evaluación de patrones, registro "
        "de eventos, generación de alertas y su distribución hacia canales externos.")
    d.comentario(
        i, "generación de alertas y su distribución hacia canales externos",
        "ACEPTAR CON CAMBIOS: original más la distribución. De la versión de GPT sólo hace falta "
        "incorporar la distribución de alertas, que hoy existe (ADR-016) y no estaba prevista en el "
        "maestro. Quito «contratos explícitos, configuración reproducible y mecanismos de "
        "persistencia e inspección de la evidencia», que son propiedades de la implementación "
        "(§17.4) y no del objetivo, y repongo la lista de componentes del original, que GPT "
        "recortó (ingesta, seguimiento temporal, registro de eventos).")

    # 13.2 · objetivo 4: ídem.
    i = d.unica("Implementar un prototipo experimental que integre lectura de archivos y captura en vivo")
    sustituir(
        d, i,
        "Implementar un prototipo experimental capaz de ejecutar el flujo experimental previsto, "
        "incorporando ingesta o lectura de video, inferencia open-vocabulary, evaluación de "
        "patrones de riesgo, registro de eventos, alertas internas y su distribución, e "
        "instrumentación de métricas técnicas y operativas.")
    d.comentario(
        i, "alertas internas y su distribución, e instrumentación",
        "ACEPTAR CON CAMBIOS: original más la distribución. GPT reescribe el objetivo con el "
        "inventario de lo construido («identidad temporal por sujeto», «herramientas de "
        "orquestación e inspección experimental»): la consola y el runner son entregables reales, "
        "pero describirlos en el objetivo es ajustar el objetivo al resultado. También se pierde "
        "«métricas ... operativas». Sólo sumo la distribución de alertas.")

    # 13.2 · objetivo 5: el más delicado; GPT mismo lo marca «cambio sustantivo para revisión».
    i = d.unica("Diseñar y ejecutar un protocolo de evaluación reproducible, sustentado en bancos de imágenes y video")
    d.comentario(
        i, "Diseñar y ejecutar un protocolo de evaluación reproducible",
        "RECHAZAR y conservar el original. GPT lo marca como «cambio sustantivo para revisión» y "
        "lo es: quita «métricas de seguimiento» y «utilidad operativa de las notificaciones», es "
        "decir, borra del objetivo lo que no se llegó a evaluar. Pero §18.6 ya declara exactamente "
        "esas dos faltas («la evaluación MOT ... mantiene los límites ya expuestos»; «no prueba "
        "... utilidad percibida por responsables de seguridad»). Si el objetivo deja de "
        "nombrarlas, esas frases de §18.6 pierden su referente y el informe oculta una reducción "
        "de alcance en vez de declararla. Lo honesto es conservar el objetivo como se planteó y "
        "dejar que el cierre diga qué no se cumplió. Lo que GPT agrega (bancos anotados, niveles, "
        "latencia por tramo, falsas alertas, extensibilidad) es la descripción de §17.5, no un "
        "objetivo.")


def _palabras(d: Documento, desde: str, hasta: str, vista: str) -> int:
    """Palabras entre dos unidades (títulos), en la vista aceptada o rechazada."""
    a = d.unica(desde)
    b = d.unica(hasta)
    total = 0
    for k in range(a, b):
        xml = d.units[k][1]
        if vista == "rechazada":
            xml = re.sub(r"<w:ins\b[^>]*>.*?</w:ins>", "", xml, flags=re.S)
            xml = xml.replace("<w:delText", "<w:t").replace("</w:delText>", "</w:t>")
        total += len(Documento.texto_de(xml).split())
    return total


def _quitar_capa_claude(xml: str) -> str:
    """Deshace sólo las marcas de Claude: inserciones fuera, borrados desenvueltos, comentarios
    nuevos fuera, filas nuevas fuera. Lo que queda debe ser el documento de origen."""
    # filas nuevas (trPr con ins de Claude)
    def fila(m):
        return "" if re.search(r'<w:trPr>(?:(?!</w:trPr>).)*<w:ins [^>]*w:author="Claude"',
                               m.group(0), re.S) else m.group(0)
    xml = TR_RE.sub(fila, xml)
    xml = re.sub(r'<w:ins w:id="\d+" w:author="Claude"[^>]*>.*?</w:ins>', "", xml, flags=re.S)
    def desdel(m):
        return m.group(1).replace("<w:delText", "<w:t").replace("</w:delText>", "</w:t>")
    xml = re.sub(r'<w:del w:id="\d+" w:author="Claude"[^>]*>(.*?)</w:del>', desdel, xml, flags=re.S)
    return xml


def verificar(origen: Path, destino: Path, cid_desde: int) -> None:
    zo, zd = zipfile.ZipFile(origen), zipfile.ZipFile(destino)
    xo = zo.read("word/document.xml").decode("utf8")
    xd = zd.read("word/document.xml").decode("utf8")
    xd2 = _quitar_capa_claude(xd)
    xd2 = re.sub(r'<w:commentRangeStart w:id="(\d+)"/>', lambda m: "" if int(m.group(1)) >= cid_desde else m.group(0), xd2)
    xd2 = re.sub(r'<w:commentRangeEnd w:id="(\d+)"/>', lambda m: "" if int(m.group(1)) >= cid_desde else m.group(0), xd2)
    xd2 = re.sub(r'<w:r>(?:<w:rPr>.*?</w:rPr>)?<w:commentReference w:id="(\d+)"/></w:r>',
                 lambda m: "" if int(m.group(1)) >= cid_desde else m.group(0), xd2, flags=re.S)

    def secuencia(x: str) -> list[tuple[str, str]]:
        # sin recortar cada pieza: el pase parte runs en medio de una frase y el espacio de la
        # frontera tiene que sobrevivir hasta que se vuelvan a pegar
        return [(m.group(1), m.group(2))
                for m in re.finditer(r"<w:(t|delText)(?:\s[^>]*)?>(.*?)</w:\1>", x, re.S)]

    def compactar(seq):
        # los runs partidos por el pase se vuelven a pegar por tipo consecutivo
        out = []
        for k, v in seq:
            if out and out[-1][0] == k:
                out[-1] = (k, out[-1][1] + v)
            else:
                out.append((k, v))
        return [(k, re.sub(r"\s+", " ", v).strip()) for k, v in out]

    so, sd = compactar(secuencia(xo)), compactar(secuencia(xd2))
    iguales = so == sd
    if not iguales:
        for k, (a, b) in enumerate(zip(so, sd)):
            if a != b:
                print(f"  ✗ primera diferencia en el tramo {k}:\n    origen : {a}\n    destino: {b}")
                break
        print(f"  ✗ longitudes {len(so)} vs {len(sd)}")
    anclas_o = re.findall(r'<w:commentRangeStart w:id="(\d+)"/>', xo)
    anclas_d = re.findall(r'<w:commentRangeStart w:id="(\d+)"/>', xd)
    print(f"  quitar la capa de Claude devuelve el origen (texto e ins/del de GPT): "
          f"{'SÍ' if iguales else 'NO'}")
    print(f"  anclas de comentario del origen conservadas: "
          f"{'SÍ' if set(anclas_o) <= set(anclas_d) else 'NO'} "
          f"({len(anclas_o)} previas, {len(anclas_d)} ahora)")
    print(f"  sha256 document.xml origen  {hashlib.sha256(xo.encode()).hexdigest()[:16]}")
    print(f"  sha256 document.xml destino {hashlib.sha256(xd.encode()).hexdigest()[:16]}")
    print(f"  ins GPT {len(re.findall(r'<w:ins [^>]*ChatGPT', xd))} / del GPT "
          f"{len(re.findall(r'<w:del [^>]*ChatGPT', xd))} · ins Claude "
          f"{len(re.findall(r'<w:ins [^>]*Claude', xd))} / del Claude "
          f"{len(re.findall(r'<w:del [^>]*Claude', xd))}")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--origen", type=Path, default=ORIGEN)
    p.add_argument("--destino", type=Path, default=DESTINO)
    a = p.parse_args()

    d = Documento(a.origen, autor=AUTOR, fecha=FECHA)
    _asegurar_w14(d)
    cid_desde = d._cid
    orig_12_13 = _palabras(d, "12. Introducción", "14. Plan De Trabajo", "rechazada")
    gpt_12_13 = _palabras(d, "12. Introducción", "14. Plan De Trabajo", "aceptada")

    palabras_clave(d)
    glosario(d)
    seccion_12_1(d)
    seccion_12_2(d)
    seccion_12_3(d)
    seccion_12_4(d)
    seccion_12_5(d)
    seccion_13(d)

    claude_12_13 = _palabras(d, "12. Introducción", "14. Plan De Trabajo", "aceptada")
    st = d.guardar(a.destino)
    print("\n".join(d.log))
    print(f"\n  §12–§13, palabras: original {orig_12_13} · GPT {gpt_12_13} "
          f"({100 * (gpt_12_13 - orig_12_13) / orig_12_13:+.1f} %) · Claude {claude_12_13} "
          f"({100 * (claude_12_13 - orig_12_13) / orig_12_13:+.1f} %)")
    print(f"  comentarios nuevos de Claude: {len(d.comentarios)} (ids desde {cid_desde})")
    print(f"  {st}")
    print("\nVerificación:")
    verificar(a.origen, a.destino, cid_desde)
    return 0


if __name__ == "__main__":
    sys.exit(main())
