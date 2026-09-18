#!/usr/bin/env python3
"""§17.3 v1.5 → v1.6: pase de consolidación de la Etapa 3, como CAMBIOS CONTROLADOS
(w:ins / w:del sin aceptar, autor Claude).

Decisiones aplicadas (`desarrollando/analisis-17-3-etapa-3.md` §8, recomendadas y aprobadas
el 2026-09-03 con la instrucción «continuá»):
  D-A  Opción A: 18 → 11 secciones de nivel 3, cero títulos de nivel 5, renumeración interna
  D-B  §17.3.2 «Insumos metodológicos» se funde en la introducción
  D-C  Tabla 43 se reduce al núcleo y a las ramas comparativas (8 filas de CR-03…CR-06 fuera)
  D-D  Tabla 44 conserva sus 4 columnas y acorta la columna de evidencia (enmienda: no se
       suprime la columna, se le quita la duplicación con la Tabla 21 de §17.1 — el borrado de
       columnas con control de cambios es frágil y el objetivo se cumple igual)
  D-E  Tabla 47 (hechos persistibles) se elimina y pasa a prosa
  D-F  Tabla 49 (diccionario de métricas) se elimina con remisión a §17.1.7.3/17.1.7.5 y Anexo D
  D-G  Tabla 51 (comparación DBE/EBE) se elimina con remisión a la Tabla 17 de §17.1
  D-H  Figuras 4.3 (plano de control) y 4.6 (roles) se eliminan; la cadena de traducción cierra
       el plano de control (enmienda: cierre en vez de intro, evita mover la imagen)
  D-I  El detalle operativo del ledger sale de §17.3; queda handoff E4-31 hacia §17.4
  D-J  Las cinco citas de 17.3.6.3 se reemplazan por remisión a §17.1.5.3
  D-K  Los 7 comentarios se conservan con sus anclas (2 re-ancladas al texto que los absorbe)
  D-L  «debe/deben» se reduce donde sólo re-enuncia una decisión ya tomada
  D-M  El cierre se conserva corto

Reglas de oficio heredadas del pase de la Etapa 2:
  · los párrafos con `w:sectPr` NUNCA se borran: se les reemplaza el contenido (20 en el cuerpo);
  · los comentarios se conservan con sus anclas (`commentRangeStart/End` intactos);
  · autocontención: ningún código interno, ADR, ruta ni cifra de verificación entra al texto.
"""
from __future__ import annotations

import re
import shutil
import sys
import zipfile
from pathlib import Path

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
SRC = BASE / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.5.docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.6 (sugerencias sin aceptar).docx"

AUTHOR = "Claude"
DATE = "2026-09-03T12:00:00Z"

RPR = '<w:rPr><w:rtl w:val="0"/></w:rPr>'
RPR_B = '<w:rPr><w:b w:val="1"/><w:bCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'
RPR_I = '<w:rPr><w:i w:val="1"/><w:iCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'
RPR_M = ('<w:rPr><w:rFonts w:ascii="Courier New" w:cs="Courier New" w:eastAsia="Courier New"'
         ' w:hAnsi="Courier New"/><w:sz w:val="21"/><w:szCs w:val="21"/><w:rtl w:val="0"/></w:rPr>')

_ID = [9000]


def nid() -> int:
    _ID[0] += 1
    return _ID[0]


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _tokens(text: str):
    """Parte el texto en (rpr, fragmento) según marcadores ~mono~, **negrita**, *cursiva*."""
    out = []
    pat = re.compile(r"~([^~]+)~|\*\*([^*]+)\*\*|\*([^*]+)\*")
    pos = 0
    for m in pat.finditer(text):
        if m.start() > pos:
            out.append((RPR, text[pos:m.start()]))
        if m.group(1) is not None:
            out.append((RPR_M, m.group(1)))
        elif m.group(2) is not None:
            out.append((RPR_B, m.group(2)))
        else:
            out.append((RPR_I, m.group(3)))
        pos = m.end()
    if pos < len(text):
        out.append((RPR, text[pos:]))
    return out


def ins_runs(text: str, base_rpr: str = RPR) -> str:
    """Runs nuevos envueltos en <w:ins>."""
    runs = []
    for rpr, frag in _tokens(text):
        if rpr is RPR and base_rpr is not RPR:
            rpr = base_rpr
        runs.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(frag)}</w:t></w:r>')
    return (f'<w:ins w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}">' + "".join(runs) + "</w:ins>")


RUN_RE = re.compile(r"<w:r\b(?![a-zA-Z])[^>]*>.*?</w:r>", re.S)


def _has_text(run: str) -> bool:
    return "<w:t" in run


def _to_del(run: str) -> str:
    d = run.replace("<w:t>", "<w:delText>").replace("<w:t ", "<w:delText ").replace("</w:t>", "</w:delText>")
    return f'<w:del w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}">{d}</w:del>'


def del_all_runs(xml: str, incluir_figuras: bool = False) -> str:
    """Marca como borrados los runs con texto. Con `incluir_figuras`, también los que llevan
    imágenes, para que al aceptar el cambio la figura desaparezca con su párrafo."""
    def repl(m):
        r = m.group(0)
        if _has_text(r) or (incluir_figuras and "<w:drawing" in r):
            return _to_del(r)
        return r
    return RUN_RE.sub(repl, xml)


def strip_comment_anchors(p: str, ids) -> str:
    """Quita las anclas de los comentarios indicados (se re-anclan en otro párrafo)."""
    for cid in ids:
        p = re.sub(r"<w:sdt><w:sdtPr>(?:(?!</w:sdt>).)*?"
                   r'<w:commentRangeStart w:id="%d"/>.*?</w:sdt>' % cid, "", p, flags=re.S)
        p = re.sub(r'<w:commentRangeStart w:id="%d"/>' % cid, "", p)
        p = re.sub(r'<w:commentRangeEnd w:id="%d"/>' % cid, "", p)
        p = re.sub(r'<w:r\b(?![a-zA-Z])[^>]*>(?:<w:rPr>.*?</w:rPr>)?'
                   r'<w:commentReference w:id="%d"/></w:r>' % cid, "", p, flags=re.S)
    return p


def mark_para_deleted(p: str) -> str:
    """Marca también la marca de párrafo como borrada, dentro de <w:pPr><w:rPr>."""
    m = re.search(r"<w:pPr>(.*?)</w:pPr>", p, re.S)
    if not m:
        return p.replace("<w:p ", f'<w:p ', 1)
    ppr = m.group(0)
    tag = f'<w:del w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
    if "<w:rPr/>" in ppr:
        new = ppr.replace("<w:rPr/>", f"<w:rPr>{tag}</w:rPr>", 1)
    elif "<w:rPr>" in ppr:
        new = ppr.replace("<w:rPr>", f"<w:rPr>{tag}", 1)
    else:
        new = ppr.replace("</w:pPr>", f"<w:rPr>{tag}</w:rPr></w:pPr>", 1)
    return p.replace(ppr, new, 1)


def edit_para(p: str, text: str, base_rpr: str = RPR, after: int | None = None) -> str:
    """Borra el contenido textual y coloca el nuevo detrás del run borrado `after`
    (por defecto, detrás del último). `after` permite que el texto nuevo quede dentro
    de un rango de comentario que sólo cubre parte del párrafo."""
    runs = [m for m in RUN_RE.finditer(p) if _has_text(m.group(0))]
    if not runs:
        # párrafo sin texto (p. ej. sólo drawing): insertar antes de </w:p>
        return p.replace("</w:p>", ins_runs(text, base_rpr) + "</w:p>", 1)
    pos = len(runs) - 1 if after is None else after
    out, last = [], 0
    for k, m in enumerate(runs):
        out.append(p[last:m.start()])
        out.append(_to_del(m.group(0)))
        if k == pos:
            out.append(ins_runs(text, base_rpr))
        last = m.end()
    out.append(p[last:])
    return "".join(out)


def delete_para(p: str) -> str:
    return mark_para_deleted(del_all_runs(p, incluir_figuras=True))


def new_para(text: str, style: str | None = None, sample: str | None = None,
             base_rpr: str = RPR) -> str:
    """Párrafo nuevo completo, con marca de párrafo insertada."""
    tag = f'<w:ins w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
    if sample:
        m = re.search(r"<w:pPr>.*?</w:pPr>", sample, re.S)
        ppr = m.group(0) if m else "<w:pPr><w:rPr/></w:pPr>"
        ppr = re.sub(r"<w:sectPr>.*?</w:sectPr>", "", ppr, flags=re.S)
        if "<w:rPr/>" in ppr:
            ppr = ppr.replace("<w:rPr/>", f"<w:rPr>{tag}</w:rPr>", 1)
        elif "<w:rPr>" in ppr:
            ppr = ppr.replace("<w:rPr>", f"<w:rPr>{tag}", 1)
        else:
            ppr = ppr.replace("</w:pPr>", f"<w:rPr>{tag}</w:rPr></w:pPr>", 1)
    else:
        st = f'<w:pStyle w:val="{style}"/>' if style else ""
        ppr = (f'<w:pPr>{st}<w:widowControl w:val="1"/><w:spacing w:after="0" w:before="0"'
               f' w:line="480" w:lineRule="auto"/><w:ind w:firstLine="720"/>'
               f'<w:rPr>{tag}</w:rPr></w:pPr>')
    return f'<w:p>{ppr}{ins_runs(text, base_rpr)}</w:p>'


# --------------------------------------------------------------------------- unidades del cuerpo
def split_units(body: str):
    units = []
    i = 0
    while i < len(body):
        m = re.search(r"<w:(p|tbl)\b", body[i:])
        if not m:
            break
        kind = m.group(1)
        start = i + m.start()
        tag_end = body.index(">", start)
        if body[tag_end - 1] == "/":
            units.append([kind, body[start:tag_end + 1], body[i:start]])
            i = tag_end + 1
            continue
        depth, j = 0, start
        while True:
            mm = re.search(r"<(/?)w:%s\b([^>]*)>" % kind, body[j:])
            closing = mm.group(1) == "/"
            selfclose = (not closing) and mm.group(2).endswith("/")
            if not closing and not selfclose:
                depth += 1
            elif closing:
                depth -= 1
            j += mm.end()
            if depth == 0:
                break
        units.append([kind, body[start:j], body[i:start]])
        i = j
    return units, body[i:]   # el resto incluye el <w:sectPr> final del cuerpo


# --------------------------------------------------------------------------- tablas
TR_RE = re.compile(r"<w:tr\b[^>]*>.*?</w:tr>", re.S)
TC_RE = re.compile(r"<w:tc\b[^>]*>.*?</w:tc>", re.S)


def del_row(tr: str) -> str:
    tag = f'<w:del w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
    if "<w:trPr>" in tr:
        tr = tr.replace("<w:trPr>", f"<w:trPr>{tag}", 1)
    else:
        tr = re.sub(r"(<w:tr\b[^>]*>)", r"\1<w:trPr>" + tag + "</w:trPr>", tr, count=1)
    tr = del_all_runs(tr)
    # marcar borradas las marcas de párrafo de las celdas
    return re.sub(r"<w:p\b[^>]*>.*?</w:p>", lambda m: mark_para_deleted(m.group(0)), tr, flags=re.S)


def edit_cell(tbl: str, row: int, col: int, text: str) -> str:
    rows = list(TR_RE.finditer(tbl))
    tr = rows[row].group(0)
    cells = list(TC_RE.finditer(tr))
    tc = cells[col].group(0)
    # editar el primer párrafo de la celda, borrar el resto de sus runs con texto
    paras = list(re.finditer(r"<w:p\b[^>]*>.*?</w:p>", tc, re.S))
    first = paras[0].group(0)
    newfirst = edit_para(first, text)
    newtc = tc[:paras[0].start()] + newfirst + tc[paras[0].end():]
    if len(paras) > 1:
        rest = newtc[newtc.index(newfirst) + len(newfirst):]
        newtc = newtc[:newtc.index(newfirst) + len(newfirst)] + re.sub(
            r"<w:p\b[^>]*>.*?</w:p>", lambda m: delete_para(m.group(0)), rest, flags=re.S)
    newtr = tr[:cells[col].start()] + newtc + tr[cells[col].end():]
    return tbl[:rows[row].start()] + newtr + tbl[rows[row].end():]


def del_rows(tbl: str, idxs) -> str:
    rows = list(TR_RE.finditer(tbl))
    out, last = [], 0
    for i, m in enumerate(rows):
        out.append(tbl[last:m.start()])
        out.append(del_row(m.group(0)) if i in idxs else m.group(0))
        last = m.end()
    out.append(tbl[last:])
    return "".join(out)


def del_table(tbl: str) -> str:
    return del_rows(tbl, set(range(len(TR_RE.findall(tbl)))))


# =============================================================================== TEXTO DEL PASE
# Claves = índice de unidad en la v1.5 (ver herramientas/indice_xml.py).
#   ("H", texto)            título: reemplaza el texto conservando el estilo
#   ("E", texto[, rpr])     reemplaza el contenido del párrafo
#   ("D",)                  borra el párrafo
#   ("K",)                  se conserva sin tocar
E = {}

# --------------------------------------------------------- 17.3.1 Propósito y pregunta rectora
E[0] = ("H", "17.3.1. Propósito y pregunta rectora")
E[1] = ("E", "El diseño arquitectónico transforma el alcance metodológico, el catálogo de condiciones "
             "de riesgo, los escenarios de evaluación, el marco de métricas y los lineamientos "
             "ético-legales ya consolidados en una organización técnica capaz de orientar la "
             "implementación del prototipo. Esos insumos operan como restricciones, de modo que cada "
             "módulo, frontera y flujo del capítulo se derive de una decisión metodológica previa y no "
             "de una preferencia técnica aislada.")
E[2] = ("E", "La plataforma se estructura alrededor de la separación entre el procesamiento visual en "
             "tiempo real y la lógica de interpretación posterior, fundamentada en la sección 16.5.3. "
             "El plano de medios produce evidencia perceptiva y el plano de control la interpreta. Esa "
             "división protege la ruta crítica de video y sostiene la trazabilidad experimental "
             "necesaria para analizar cada corrida.")
for i in (3, 4, 5, 6, 7, 8, 9, 10):
    E[i] = ("D",)
E[11] = ("E", "La pregunta que orienta el capítulo es qué arquitectura permite materializar una "
              "plataforma experimental de detección open-vocabulary sobre video en tiempo real "
              "conservando modularidad, desacoplamiento, trazabilidad y evaluabilidad dentro del "
              "alcance ya definido. El capítulo la responde fijando las responsabilidades de los "
              "componentes, los flujos de información, las fronteras entre módulos, los contratos "
              "versionados, las interfaces de gobierno y transporte, los escenarios experimentales y "
              "los criterios de observabilidad que acompañan la implementación.")

# ------------------------------------- 17.3.2 Alcance, capacidades y decisiones arquitectónicas
E[12] = ("H", "17.3.2. Alcance, capacidades y decisiones arquitectónicas")
E[13] = ("E", "El diseño se formula para un prototipo experimental ejecutado en un entorno local y "
              "controlado, y orienta la implementación, la medición y la reconstrucción de resultados "
              "sin asumir responsabilidades propias de una solución productiva. Sobre el núcleo "
              "validable la plataforma demuestra un flujo completo, medible y trazable desde una "
              "fuente visual hasta una alerta asistiva registrada. El objetivo no es ampliar la "
              "cantidad de condiciones cubiertas, sino asegurar una base capaz de procesar evidencia "
              "visual, publicar eventos, evaluar patrones, registrar alertas y reconstruir resultados "
              "experimentales.")
E[14] = ("D",)
E[15] = ("D",)
E[16] = ("E", "El núcleo comprende las capacidades necesarias para operar sobre fuentes controladas, "
              "ejecutar inferencia open-vocabulary, versionar prompts, normalizar detecciones, aplicar "
              "reglas temporales simples, registrar eventos y producir métricas comparables. El "
              "seguimiento multiobjeto formal, las reglas espaciales, las zonas parametrizadas, la "
              "preselección liviana en el borde y la adaptación al dominio quedan previstas como "
              "extensiones condicionadas que no desplazan la validación inicial ni agregan "
              "dependencias al flujo base. La gestión de prompts pertenece al núcleo porque en una "
              "plataforma open-vocabulary cada resultado se atribuye a una formulación, una estrategia "
              "de detección y un vocabulario activo registrados.")
E[17] = ("D",)
E[18] = ("D",)
E[19] = ("H", "17.3.2.1. Capacidades arquitectónicas requeridas")
E[20] = ("E", "La arquitectura habilita un conjunto mínimo de capacidades que permiten desarrollar un "
              "prototipo medible, trazable y extensible. La enumeración reúne responsabilidades del "
              "diseño y no componentes de implementación.")
E[21] = ("E", "La Tabla 39 declara el régimen de cada capacidad mediante cinco compromisos, cuyo "
              "alcance precisa la nota. La clasificación ordena el desarrollo sin convertir "
              "funcionalidades deseables en dependencias obligatorias del flujo base y evita que una "
              "capacidad quede habilitada de manera implícita.")
E[25] = ("E", "**Nota.** El compromiso declara el régimen de cada capacidad. «Núcleo» identifica las "
              "capacidades necesarias para el flujo base. «Complementario previsto» agrupa las útiles "
              "para la validación, la revisión técnica o la comunicación académica. «Capacidad "
              "opcional» identifica las que el diseño contempla pero se declaran en la configuración "
              "de cada corrida y permanecen deshabilitadas por defecto, de modo que ninguna opere como "
              "comportamiento implícito. «Extensión condicionada» identifica las que exigen evidencia "
              "e instrumentación adicionales. «Rama comparativa condicionada» refiere a variantes que "
              "sólo se incorporan si se cumplen las condiciones metodológicas correspondientes.")
E[26] = ("H", "17.3.2.2. Requisitos no funcionales de referencia")
E[27] = ("E", "Las cualidades no funcionales condicionan la validez experimental del prototipo. No "
              "alcanza con detectar una condición de riesgo si el sistema no registra la configuración "
              "de la corrida, no mide latencia, no conserva trazabilidad o no controla la evidencia "
              "visual generada. La Tabla 40 reúne las cualidades que el diseño trata como condiciones "
              "arquitectónicas y no como aspiraciones.")
E[31] = ("E", "**Nota.** Los requisitos no funcionales expresan las cualidades necesarias para "
              "preservar la validez experimental del prototipo y aseguran comparabilidad entre "
              "corridas, trazabilidad de resultados y control de las decisiones que afectan la "
              "latencia, la privacidad, la reproducibilidad o la observabilidad.")
E[32] = ("H", "17.3.2.3. Decisiones arquitectónicas y principios de lectura")
E[33] = ("E", "Las decisiones arquitectónicas iniciales no fijan tecnologías concretas y establecen "
              "reglas estructurales que se preservan durante el desarrollo del prototipo. La Tabla 41 "
              "las reúne alrededor de cuatro ejes. La **separación entre ruta crítica y lógica de "
              "control** mantiene la inferencia y la publicación de evidencia perceptiva desacopladas "
              "de la evaluación de patrones, la persistencia, los reportes y las notificaciones "
              "externas (DA-01, DA-02). La **modularidad por contratos** hace que fuentes, modelos, "
              "prompts, detecciones, patrones y métricas se intercambien mediante estructuras "
              "explícitas, sin dependencias internas que dificulten la sustitución o la evaluación "
              "comparativa (DA-05, DA-12). La **trazabilidad experimental** permite reconstruir toda "
              "alerta a partir de la configuración de corrida, los eventos de percepción, el patrón "
              "evaluado y las métricas registradas (DA-03, DA-04, DA-13). La **medición desde el "
              "diseño** instrumenta tiempos, cadencia efectiva, descartes, errores y estados de patrón "
              "desde las primeras corridas, porque forman parte de la validez experimental.")
for i in (38, 39, 40, 41, 42, 43, 44, 45, 46):
    E[i] = ("D",)
E[47] = ("E", "A esos cuatro ejes se suma un criterio transversal de **evolución incremental**, por el "
              "cual las capacidades condicionadas (DA-06, DA-07, DA-11) se incorporan sin desplazar el "
              "núcleo ni convertirse en dependencias del flujo base.")

# ----------------------------------------------------- 17.3.3 Vista general y patrones de acople
E[48] = ("H", "17.3.3. Vista general y patrones de acople")
E[49] = ("E", "La plataforma se organiza como una arquitectura lógica por bloques que procesa fuentes "
              "de video, genera evidencia perceptiva, evalúa patrones de riesgo y conserva resultados "
              "reconstruibles. La vista separa responsabilidades y no prescribe una distribución "
              "obligatoria en procesos, servicios o nodos físicos.")
E[50] = ("D",)
E[51] = ("E", "El flujo principal parte de fuentes visuales externas, como datasets, videos locales, "
              "cámaras o flujos de streaming, y entra al plano de medios por el adaptador de ingesta "
              "visual, que encapsula los distintos orígenes bajo una representación común. Desde ese "
              "punto se concentra la ruta crítica, que va de la lectura o la captura hasta la "
              "publicación de evidencia perceptiva normalizada. El plano no depende de tareas "
              "posteriores para continuar procesando unidades visuales. La configuración experimental "
              "atraviesa ese flujo y define las condiciones de cada corrida, entre ellas el escenario, "
              "el modelo, los prompts activos, los umbrales, las políticas de evidencia y los "
              "parámetros de ejecución, sin intervenir en el procesamiento frame a frame.")
E[52] = ("E", "A partir de los eventos publicados, el plano de control evalúa patrones, administra "
              "estados de corrida y registra alertas asistivas internas cuando confirma una condición "
              "de riesgo. Las alertas confirmadas viajan por un bus dedicado hacia el módulo de "
              "distribución. El ciclo de vida de los tres módulos se gobierna mediante interfaces "
              "independientes, que la interfaz de inspección y el orquestador experimental utilizan "
              "sin consumir los buses.")
E[53] = ("E", "La trazabilidad, la observabilidad y la inspección se agrupan en el bloque de soporte "
              "experimental, que es una capacidad transversal y no una etapa del flujo frame a frame. "
              "Ese bloque conserva evidencia reconstruible, consolida telemetría técnica y permite "
              "revisar corridas, métricas, alertas y resultados sin interferir con la ruta crítica. La "
              "Figura 4.1 presenta esa organización.")
E[57] = ("E", "**Nota.** La figura presenta una vista lógica de alto nivel. Las flechas sólidas "
              "representan el flujo principal de datos y eventos, y las punteadas, la influencia de la "
              "configuración o las capacidades de soporte. La vista no prescribe una distribución "
              "física ni una asignación definitiva a tecnologías específicas.")
E[58] = ("E", "La vista se materializa mediante dos patrones de acople complementarios. El gobierno de "
              "las corridas ocurre por interfaces ~HTTP~ gobernadas por configuración en los tres "
              "módulos ejecutables. Se adopta ~HTTP~ porque el ciclo de vida de una corrida, que "
              "abarca crear, consultar, cancelar y cerrar, tiene semántica de solicitud y respuesta, "
              "admite múltiples clientes sin acoplarlos entre sí y permite disponer los módulos en un "
              "mismo host o en hosts distintos sin modificar su lógica. El gobierno por configuración "
              "obliga a que cada corrida declare sus parámetros en lugar de heredarlos de constantes "
              "ocultas.")
E[59] = ("E", "Esta organización mantiene separados, y coordinados por contratos explícitos, el "
              "procesamiento de video, la interpretación de patrones, la distribución de alertas y el "
              "análisis experimental.")

# ------------------ 17.3.4 Configuración experimental, vocabulario y estrategia del núcleo
E[60] = ("H", "17.3.4. Configuración experimental, vocabulario y estrategia del núcleo")
E[61] = ("E", "La configuración experimental concentra las decisiones que gobiernan una corrida y "
              "declara de manera explícita y reproducible el escenario, la fuente visual, el modelo "
              "OVD, los prompts activos, los umbrales, la política de muestreo, los módulos "
              "habilitados, los criterios de patrón, la política de evidencia y la instrumentación de "
              "métricas. Al fijarlas antes de la ejecución, separa la definición de las condiciones "
              "del procesamiento efectivo de frames y eventos, y permite que cada detección, "
              "transición de patrón, alerta interna, métrica o evidencia conservada se asocie con una "
              "configuración efectiva de corrida.")
E[62] = ("E", "Esa separación protege la ruta crítica, porque el pipeline dispone de la configuración "
              "efectiva sin consultas externas bloqueantes para decidir qué modelo ejecuta, qué "
              "prompts utiliza o qué política de muestreo aplica. También delimita la interpretación "
              "posterior de los resultados, ya que una detección sólo resulta experimentalmente útil "
              "si puede relacionarse con su fuente, modelo, prompt, umbral, postproceso y patrón "
              "evaluado. Sin esa asociación no es posible atribuir diferencias de desempeño a una "
              "variable concreta de la corrida.")
for i in (63, 64, 65, 66, 67):
    E[i] = ("D",)
E[68] = ("E", "El gobierno se sostiene sólo si la configuración se resuelve y se valida antes de "
              "iniciar la ejecución, de manera que una corrida con declaración incompleta falle al "
              "crearse y no produzca artefactos inatribuibles. La configuración alcanza a tres "
              "destinatarios. El plano de medios recibe los parámetros que aplica sin diseñarlos ni "
              "versionarlos, el plano de control recibe los criterios con los que evalúa y el soporte "
              "experimental la utiliza como clave de reconstrucción, de modo que todo evento, métrica, "
              "alerta o evidencia conservada pueda rastrearse hasta la corrida que le dio origen.")
E[69] = ("H", "17.3.4.1. Configuración de corrida como artefacto de reproducibilidad")
E[70] = ("E", "La configuración de corrida se materializa como un manifiesto de experimento que "
              "referencia y congela las configuraciones efectivas de cada componente. El plano de "
              "medios, el plano de control y el tramo de distribución tienen ciclos de vida y "
              "destinatarios distintos, y una configuración monolítica no tendría un único consumidor "
              "ni permitiría reconstruir con precisión qué versión recibió cada servicio.")
E[71] = ("E", "Se denomina ejecución experimental a la unidad lógica que agrupa las ejecuciones "
              "independientes de los componentes que participan en una misma instancia del "
              "experimento. Esa unidad se identifica mediante un ~experiment_id~, mientras que cada "
              "componente conserva su propio identificador de corrida. La separación entre ambos "
              "niveles permite correlacionar configuraciones, eventos, métricas, alertas, entregas y "
              "artefactos bajo una clave común, sin imponer un ciclo de vida único ni una "
              "configuración monolítica a los servicios participantes.")
E[72] = ("E", "El manifiesto declara un ~experiment_id~, las referencias a las configuraciones de cada "
              "plano, el orden de disparo y los artefactos congelados, entre ellos el modelo, el "
              "conjunto de prompts, el conjunto de patrones y la política de distribución. Dos "
              "corridas sólo son comparables cuando se conoce qué variable cambió y cuáles "
              "permanecieron constantes. La Tabla 42 reúne los elementos mínimos de ese gobierno "
              "reproducible.")
E[76] = ("E", "**Nota.** La tabla presenta los elementos mínimos del manifiesto y de las "
              "configuraciones referenciadas. Los contratos concretos se desarrollan en la sección "
              "17.3.8.")
E[77] = ("H", "17.3.4.2. Diseño de prompts y vocabulario activo")
E[78] = ("E", "El diseño de prompts expresa las condiciones de riesgo como consultas consumibles por "
              "un modelo OVD. La sección 17.1.5.3 estableció la sensibilidad de estos modelos a la "
              "formulación de la consulta y fijó el inglés como idioma primario del vocabulario, de "
              "modo que aquí sólo se fija la consecuencia arquitectónica. La consulta textual incide "
              "sobre la evidencia perceptiva generada, y por eso se registra, se versiona y se "
              "mantiene trazable hasta los resultados que contribuye a producir.")
E[79] = ("D",)
E[80] = ("E", "Cada prompt se asocia a una condición de riesgo, un texto de consulta, una estrategia "
              "de formulación, una versión y un conjunto de prompts activos. Una modificación de "
              "redacción se registra como variante experimental y no como reemplazo informal, de "
              "manera que pueda explicarse qué formulación produjo una detección y compararse "
              "resultados sin perder el vínculo con la condición original.")
E[81] = ("E", "El vocabulario activo es el conjunto de prompts habilitados en una corrida. Su tamaño y "
              "su composición afectan el comportamiento semántico del detector y, según el modelo, el "
              "costo de inferencia. Por eso el núcleo validable trabaja con un vocabulario reducido y "
              "controlado, suficiente para evaluar la sensibilidad de formulación y sin listas amplias "
              "que dificulten atribuir resultados.")
E[82] = ("E", "Un prompt y una estrategia de detección no son lo mismo. Un prompt es una consulta "
              "semántica, mientras que una estrategia puede combinar prompts, postproceso, evidencia "
              "indirecta o reglas espaciales.")
E[83] = ("H", "17.3.4.3. Vocabulario y estrategia del núcleo validable")
E[84] = ("E", "El diseño inicial distingue el vocabulario positivo del núcleo, los conjuntos de las "
              "ramas comparativas y el vocabulario condicionado de las condiciones de mayor "
              "complejidad. Para CR-01 y CR-02 el núcleo utiliza ~person~, ~helmet~ y ~vest~, donde la "
              "primera categoría identifica la entidad sujeto y las restantes representan los "
              "elementos de protección cuya presencia se evalúa espacialmente respecto de cada "
              "persona.")
E[85] = ("E", "La ausencia de casco o chaleco no se formula como consulta principal del núcleo. Se "
              "infiere en el plano de control cuando existe evidencia suficiente de una persona y no "
              "se encuentra evidencia del EPP correspondiente dentro de la región configurada. Las "
              "consultas negativas o de estado observable se mantienen en conjuntos separados para las "
              "estrategias directa (~E-DIR~) e híbrida (~E-HYB~) definidas en la consolidación "
              "metodológica, de modo que sus resultados sean atribuibles a una estrategia explícita y "
              "no a una mezcla informal de vocabularios.", RPR, 3)
E[86] = ("E", "CR-03 y CR-04 conservan consultas compuestas y descompuestas de carácter condicionado, "
              "porque su confirmación requiere contexto espacial adicional. CR-05 y CR-06 se expresan "
              "mediante entidades componentes, ya que la condición completa depende de proximidad, "
              "seguimiento o zonas declaradas externamente. La Tabla 43 organiza el vocabulario del "
              "núcleo y de las ramas comparativas, y el catálogo completo de formulaciones candidatas "
              "por condición y estrategia se consolida en el Anexo C.")
E[88] = ("E", "Vocabulario de prompts en inglés del núcleo validable y de las ramas comparativas", RPR_I)
E[90] = ("E", "**Nota.** El vocabulario del núcleo validable está compuesto por ~person~, ~helmet~ y "
              "~vest~. Las formulaciones directas pertenecen a ramas comparativas independientes y el "
              "vocabulario condicionado de CR-03 a CR-06 se consolida en el Anexo C. Cada corrida "
              "conserva ~prompt_set_id~, de modo que toda detección pueda atribuirse al conjunto que "
              "la produjo.")
E[91] = ("H", "17.3.4.4. Reglas de comparabilidad entre configuraciones")
E[92] = ("E", "La configuración permite comparar variantes sin producir conclusiones ambiguas. Al "
              "comparar prompts se mantienen constantes el modelo, la fuente visual, la resolución, la "
              "política de muestreo, los umbrales, el postproceso y los criterios de patrón, de modo "
              "que una variación de desempeño pueda atribuirse a la formulación evaluada. Al comparar "
              "modelos OVD se conserva el mismo conjunto de prompts y condiciones equivalentes de "
              "fuente, resolución y postproceso, y si un modelo requiere umbrales distintos por la "
              "escala de sus puntajes, esa diferencia se declara como parte de la configuración y no "
              "se oculta como detalle de implementación.")
E[93] = ("D",)
E[94] = ("E", "Al comparar DBE y EBE se declara que cambia la naturaleza temporal de la fuente. En EBE "
              "intervienen la captura continua, la variabilidad de iluminación, la codificación o "
              "decodificación cuando corresponda, la continuidad temporal, las omisiones, los "
              "descartes y la disponibilidad efectiva de frames, de modo que las diferencias "
              "observadas no se atribuyan automáticamente al detector OVD.")
E[95] = ("E", "Por la misma razón, ningún módulo opcional opera como comportamiento implícito. La "
              "evidencia visual, la identidad temporal, las zonas, la preselección en el rol de "
              "captura y la distribución externa se habilitan en la configuración de la corrida, "
              "porque una activación silenciosa alteraría la interpretación de la latencia, la "
              "cobertura temporal, la privacidad y la aplicabilidad de las métricas. Es esa referencia "
              "declarada, y no una reinterpretación posterior de los artefactos, la que permite "
              "atribuir una diferencia de resultados a la variante evaluada y no a un cambio no "
              "declarado en la cadena.")

# ------------------------------------------------- 17.3.5 Diseño conceptual del plano de medios
E[96] = ("H", "17.3.5. Diseño conceptual del plano de medios")
E[97] = ("E", "El plano de medios se materializa en el componente lógico Pipeline de Medios, que "
              "concentra la ruta sensible a latencia. Comienza cuando el adaptador de ingesta visual "
              "recibe, lee o decodifica una unidad visual proveniente de una fuente externa y termina "
              "cuando publica evidencia perceptiva normalizada hacia la frontera de integración. Su "
              "alcance abarca ingesta, decodificación cuando corresponda, control de ritmo, "
              "normalización visual, inferencia open-vocabulary, postproceso y publicación no "
              "bloqueante.")
E[98] = ("E", "El límite del componente es estricto. El Pipeline de Medios no confirma condiciones de "
              "riesgo, no asigna severidad, no ejecuta reglas de patrón, no genera alertas y no "
              "depende de persistencia pesada para continuar procesando frames. Su salida es evidencia "
              "perceptiva primaria asociada a una corrida, una fuente, una referencia temporal, un "
              "modelo y una configuración de procesamiento, y su interpretación corresponde al plano "
              "de control.")
E[99] = ("D",)
E[100] = ("E", "Las fuentes utilizadas en DBE y EBE ingresan por una misma frontera conceptual, el "
               "adaptador de ingesta visual, y la diferencia entre escenarios se resuelve en la forma "
               "de lectura, la disponibilidad del frame, los metadatos temporales y el control de "
               "ritmo, no en la salida del plano. En DBE predomina la lectura reproducible. En EBE "
               "pueden aparecer irregularidad temporal, atraso acumulado, variabilidad de captura o "
               "disponibilidad de frames recientes. En ambos casos la salida conserva trazabilidad "
               "suficiente para reconstruir qué se procesó, bajo qué configuración y con qué "
               "resultado. La Figura 4.2 representa ese flujo interno.")
E[101] = ("D",)
E[105] = ("E", "**Nota.** La figura representa el flujo interno del plano de medios. Las fuentes "
               "visuales son externas al plano, que comienza en el adaptador de ingesta visual, "
               "responsable de recibir, leer o decodificar la fuente y transformarla en una unidad "
               "visual procesable. La configuración de corrida parametriza la ejecución como entrada "
               "transversal, sin formar parte del procesamiento frame a frame. El evento de percepción "
               "normalizado se ubica por fuera del recuadro para señalar la frontera de salida hacia "
               "el bus interno de eventos y el plano de control.")
E[106] = ("H", "17.3.5.1. Flujo operativo del Pipeline de Medios")
E[107] = ("E", "El flujo interno se organiza como una cadena de transformación progresiva. Cada etapa "
               "recibe una representación visual o perceptiva, aplica una operación acotada y entrega "
               "una salida que mantiene relación con la corrida y con la referencia temporal original, "
               "de modo que fuentes, modelos o políticas de procesamiento puedan sustituirse sin "
               "modificar la responsabilidad general del plano.")
E[108] = ("E", "**Ingesta y decodificación.** La primera responsabilidad interna del plano es recibir la "
               "entrada visual desde fuentes externas, como datasets, imágenes, videos locales, "
               "cámaras o streams. La fuente queda encapsulada por un adaptador de ingesta visual que "
               "oculta diferencias de formato sin eliminar información relevante para la evaluación. "
               "Cuando la entrada proviene de video codificado o de streaming, la decodificación "
               "convierte el flujo en frames procesables y registra la información necesaria para "
               "distinguir disponibilidad, recepción, orden lógico y referencia temporal. En DBE suele "
               "alcanzar con conservar el índice de secuencia y el orden de lectura. En EBE puede ser "
               "necesario registrar además timestamps de captura o recepción, irregularidad temporal y "
               "descartes por atraso.")
E[109] = ("E", "**Control de ritmo y selección de unidades visuales.** Antes de ingresar a inferencia, el "
               "pipeline decide qué unidades visuales se procesan. La decisión puede aceptar todos los "
               "frames, aplicar una selección determinista, reducir la frecuencia de procesamiento o "
               "priorizar unidades recientes cuando existe captura continua. La política se declara "
               "por corrida, porque cambiar la selección de unidades, la frecuencia de procesamiento o "
               "el criterio de omisión equivale a cambiar la variante experimental evaluada. Lo que el "
               "diseño exige no es una política concreta sino la ausencia de decisiones invisibles, de "
               "manera que toda unidad omitida, reemplazada o descartada quede asociada a una causa y "
               "a una política declarada.")
E[111] = ("E", "**Inferencia open-vocabulary.** La inferencia ejecuta el detector configurado sobre la "
               "entrada normalizada y el conjunto de prompts activos. El modelo se integra mediante un "
               "adaptador para evitar que el resto del plano dependa de la salida particular de un "
               "detector concreto. Esta etapa produce resultados crudos, como cajas, puntajes, "
               "etiquetas o frases asociadas, según el formato propio del detector utilizado. Cuando "
               "el modelo lo permita, el adaptador puede reutilizar representaciones textuales "
               "precalculadas o mecanismos equivalentes para reducir el costo de inferencia, siempre "
               "que esa optimización no altere la trazabilidad de la corrida.")
E[112] = ("E", "**Postproceso y normalización de detecciones.** Luego de la inferencia, el pipeline aplica "
               "los filtros definidos por la configuración de corrida, entre ellos umbrales, supresión "
               "de detecciones redundantes, normalización de etiquetas y remapeo de coordenadas, para "
               "convertir las salidas del modelo en evidencia perceptiva común. Esa salida queda "
               "asociada al frame, al prompt, a la condición y al nivel de confianza correspondiente. "
               "No interpreta riesgo ni genera alertas, y sólo entrega evidencia normalizada al plano "
               "de control.")
E[113] = ("E", "**Publicación de evidencia perceptiva.** La publicación cierra el plano de medios. La "
               "evidencia normalizada se entrega como evento liviano hacia la frontera de integración, "
               "asociada a la corrida, la fuente, la referencia temporal, el modelo, los prompts y los "
               "timestamps relevantes. A partir de ese punto la evidencia puede evaluarse en el plano "
               "de control, persistirse de manera reconstruible o inspeccionarse desde el soporte "
               "experimental, y ninguna de esas tareas es requisito para que el pipeline continúe con "
               "la siguiente unidad visual.")
E[114] = ("E", "En consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin "
               "contexto y tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. "
               "Su producto es evidencia visual primaria, normalizada y trazable, cuya interpretación "
               "corresponde al plano de control.")
for i in range(115, 127):
    E[i] = ("D",)
E[127] = ("H", "17.3.5.2. Capacidades opcionales y degradación segura")
E[128] = ("E", "El núcleo validable del plano de medios opera sin seguimiento multiobjeto formal, sin "
               "preselección en borde y sin adaptación de modelos al dominio. Estas capacidades se "
               "incorporan como variantes del flujo, no son requisito para demostrar el procesamiento "
               "de CR-01 y CR-02 y no modifican el contrato de salida. La preselección en borde se "
               "adopta bajo un criterio de degradación segura, denominado fail-open, por el cual una "
               "falla o una decisión incierta del preselector conserva la unidad visual para el flujo "
               "principal. La variante puede descartar carga y nunca ser causa de pérdida de "
               "evidencia.")
E[129] = ("E", "El seguimiento puede ubicarse después del postproceso cuando resulte necesario "
               "estabilizar entidades, reducir oscilaciones entre frames o entregar identificadores "
               "temporales al plano de control. Un identificador temporal no equivale a una condición "
               "de riesgo sostenida.")
E[130] = ("E", "Las variantes orientadas a eficiencia reciben el mismo tratamiento. Las reducciones de "
               "resolución, los cambios de modo de inferencia o las exportaciones a motores "
               "optimizados corresponden a la implementación, y cualquier variante que altere la ruta "
               "frame-evento se declara en la configuración de corrida.")

# ------------------------------------------------ 17.3.6 Diseño conceptual del plano de control
E[131] = ("H", "17.3.6. Diseño conceptual del plano de control")
E[132] = ("E", "El plano de control interpreta la evidencia perceptiva producida por el plano de "
               "medios. Su responsabilidad comienza cuando ingresa un evento de percepción normalizado "
               "y termina cuando el sistema registra estados de patrón, alertas internas, eventos "
               "persistibles, métricas y salidas de inspección o distribución desacopladas. A "
               "diferencia del Pipeline de Medios no procesa frames crudos ni opera al ritmo constante "
               "de captura, porque trabaja sobre eventos y sobre cambios de estado derivados de reglas "
               "configuradas.")
E[133] = ("E", "La separación entre detección, patrón y alerta es su decisión arquitectónica central. "
               "Una detección puntual expresa una observación del modelo sobre una unidad visual. Un "
               "patrón confirmado expresa que esa evidencia fue evaluada durante una ventana temporal "
               "bajo criterios explícitos de persistencia, umbral e histéresis. Una alerta interna "
               "registra un episodio asistivo generado por una transición válida del patrón. El plano "
               "no transforma cada detección en una alerta, sino que estabiliza la evidencia antes de "
               "producir salidas operativas.")
E[134] = ("E", "Esa organización evita que la variabilidad propia de la inferencia OVD, con sus falsos "
               "positivos, falsos negativos, fluctuación de puntajes, sensibilidad al prompt u "
               "oclusiones parciales, se traslade directamente al sistema de alertas. También mantiene "
               "al plano de medios aislado de consumidores lentos, persistencia histórica, reportes, "
               "notificaciones externas o interfaces de inspección, que el plano de control ejecuta de "
               "forma asíncrona.")
E[135] = ("E", "En el alcance del prototipo el plano de control se orienta al núcleo validable. Para "
               "CR-01 y CR-02 la evaluación se resuelve mediante persistencia temporal simple y "
               "estados de patrón, sin exigir seguimiento multiobjeto formal. El seguimiento, las "
               "zonas espaciales y las reglas relacionales enriquecen escenarios posteriores y no son "
               "dependencia del núcleo validable.")
for i in (136, 137, 138, 139, 140, 141, 142, 143, 144, 145):
    E[i] = ("D",)
E[146] = ("H", "17.3.6.1. Máquina de estados y ciclo del episodio")
E[147] = ("E", "La máquina de estados distingue ~inactive~, ~candidate~, ~confirmed~, ~sustained~ y "
               "~resolved~. Una evidencia inicial abre el estado candidato. La confirmación ocurre "
               "cuando la condición satisface la ventana temporal y los umbrales declarados. La "
               "continuidad mantiene el episodio y la ausencia sostenida durante la histéresis lo "
               "resuelve.")
E[148] = ("E", "La transición a ~confirmed~ registra una alerta interna por episodio. El estado "
               "sostenido actualiza duración y evidencia sin convertir cada frame positivo en una "
               "alerta nueva. Una nueva confirmación posterior se conserva como re-alerta y se evalúa "
               "por separado de los falsos positivos.")
E[149] = ("E", "Las ventanas se expresan en milisegundos y no en frames, de modo que la semántica "
               "temporal no cambie con la cadencia de procesamiento. Los valores adoptados para los "
               "patrones del núcleo se documentan junto con la configuración efectiva en la sección "
               "17.4.6.")
E[150] = ("E", "El ciclo de evaluación selecciona evidencias, actualiza la memoria, aplica la ventana "
               "de confirmación y la histéresis, registra la transición y conserva la causa. Los "
               "descartes de fuente, los huecos temporales y la pérdida de identidad se distinguen de "
               "la ausencia real de evidencia. La confirmación representa el cumplimiento de una regla "
               "interna bajo la configuración de la corrida y no constituye certificación normativa ni "
               "decisión automática de intervención. La Figura 4.3 representa ese ciclo.")
E[151] = ("E", "Figura 4.3", RPR_B)
E[154] = ("E", "**Nota.** La figura representa el ciclo de vida temporal de un patrón de riesgo en el "
               "plano de control. La condición observada abre el estado ~candidate~ y, cuando la "
               "evidencia satisface la ventana de confirmación configurada, el patrón pasa a "
               "~confirmed~ y se registra la alerta interna correspondiente. Mientras la condición "
               "permanece activa el patrón evoluciona a ~sustained~. Cumplida la ventana de "
               "resolución, el episodio pasa a ~resolved~ y retorna a ~inactive~. Si la evidencia "
               "inicial resulta insuficiente o no persiste durante la ventana de confirmación, el "
               "patrón vuelve a ~inactive~ sin generar una alerta.")
E[155] = ("H", "17.3.6.2. Motor de evaluación y definición de patrón")
E[156] = ("E", "El motor de evaluación es el componente lógico del plano de control que transforma "
               "evidencia perceptiva normalizada en estados de patrón, episodios y alertas internas. "
               "No procesa imágenes ni ejecuta inferencia OVD. Consume los eventos publicados por el "
               "plano de medios, consulta las definiciones activas de patrón declaradas en la "
               "configuración experimental y actualiza el estado correspondiente dentro de la corrida.")
E[157] = ("D",)   # tercera formulación de «detección ≠ patrón», que ya fijan 17.3.6 y 17.3.6.2
E[158] = ("E", "El motor admite el catálogo completo de patrones del prototipo y su activación "
               "efectiva depende de la configuración de corrida, los módulos habilitados y la "
               "disponibilidad de evidencia suficiente, de modo que la arquitectura pueda incorporar "
               "patrones de mayor complejidad sin modificar la lógica central del plano de control.")
E[159] = ("D",)
E[160] = ("E", "El motor no evalúa condiciones de riesgo aisladas, sino patrones activos que las "
               "operacionalizan durante una corrida. La condición identificada mediante CR-01 a CR-06 "
               "conserva el significado semántico del fenómeno observable, y el patrón correspondiente, "
               "identificado mediante PR-01 a PR-06, establece la regla con la que ese fenómeno se "
               "convierte en un estado evaluable. La separación permite modificar la estrategia de "
               "evidencia, la granularidad o el comportamiento temporal sin alterar el catálogo de "
               "condiciones de riesgo.")
E[161] = ("E", "Cada patrón se declara mediante configuración y reúne, como una única definición "
               "evaluable, los criterios necesarios para admitir evidencia, mantener estado y producir "
               "una salida trazable, de modo que la lógica del motor no dependa de reglas particulares "
               "incorporadas de manera rígida en el código. La definición comprende siete elementos.")
E[163] = ("E", "**Evidencia admisible.** El patrón especifica qué detecciones o relaciones pueden "
               "intervenir en la evaluación. En el núcleo, el motor utiliza detecciones positivas de "
               "~person~ y del elemento de protección correspondiente, ~helmet~ o ~vest~, y determina "
               "su presencia o ausencia mediante asociación espacial. La condición de riesgo no se "
               "deriva de una detección negativa opaca.")
E[164] = ("E", "**Granularidad y región de evaluación.** La granularidad scene mantiene el estado por "
               "patrón y fuente, mientras que subject lo mantiene además por identidad temporal de "
               "sujeto. Cuando la condición depende de un elemento asociado a la persona, el patrón "
               "también declara la región relativa de la caja donde se busca la evidencia, que es la "
               "región cefálica para PR-01 y el torso para PR-02.")
E[168] = ("E", "**Estado y salida observable.** A partir de los criterios anteriores, el motor actualiza "
               "el estado del patrón y registra las transiciones correspondientes. Cuando la evidencia "
               "satisface la regla de confirmación, produce la alerta interna y los eventos necesarios "
               "para reconstruir posteriormente la evaluación.")
E[169] = ("D",)
E[170] = ("D",)
E[171] = ("E", "La granularidad de la memoria temporal es un parámetro explícito de la definición de "
               "patrón. Bajo granularidad de escena el estado se indexa por ~(patrón, fuente)~ y "
               "evalúa la continuidad de la condición en la escena. Bajo granularidad de sujeto se "
               "indexa por ~(patrón, fuente, identidad)~ y exige una identidad temporal válida.")
E[172] = ("E", "La granularidad de sujeto sólo puede utilizar una identidad producida por un "
               "componente de seguimiento o por un decorador equivalente del plano de control, porque "
               "el identificador de detección no vale entre frames. La capacidad se habilita por "
               "configuración sin modificar el contrato de percepción, y la identidad resultante se "
               "conserva en los artefactos del control y no en el registro ordinario del plano de "
               "medios.")
E[173] = ("E", "La granularidad de escena sostiene una afirmación precisa, que es la persistencia de "
               "la condición en la escena. No permite concluir que el mismo sujeto sostuvo el riesgo "
               "durante toda la ventana, porque una rotación de personas podría mantener la condición "
               "de forma continua. Esa segunda afirmación requiere granularidad de sujeto.")
E[174] = ("E", "La exclusión de las métricas formales de seguimiento multiobjeto no elimina esta "
               "capacidad, porque la arquitectura separa la identidad necesaria para indexar el estado "
               "del patrón de la evaluación formal del desempeño de seguimiento.")
E[175] = ("D",)
E[176] = ("D",)
E[177] = ("E", "El motor respeta la clasificación metodológica de condiciones por nivel de "
               "complejidad. Desde el diseño arquitectónico, esa clasificación se traduce en "
               "requisitos de evaluación distintos, porque algunos patrones se resuelven con evidencia "
               "perceptiva y persistencia temporal simple y otros sólo se activan cuando la corrida "
               "habilita insumos adicionales como seguimiento, zonas parametrizadas o reglas "
               "espaciales.")
E[178] = ("E", "Esa diferenciación permite diseñar un motor único sin sobredimensionar el prototipo "
               "experimental, con una lógica común de evaluación que adapta sus entradas y criterios "
               "según el patrón activo y la configuración de corrida. La Tabla 44 reúne las "
               "dependencias arquitectónicas de cada patrón y su tratamiento en el prototipo.")
E[182] = ("E", "**Nota.** La tabla declara las dependencias arquitectónicas de cada patrón y el "
               "tratamiento que recibe en el prototipo. El tratamiento «núcleo validable» identifica "
               "los patrones obligatorios del prototipo experimental. El tratamiento «extensión "
               "condicionada» indica capacidades previstas que sólo deben habilitarse cuando existan "
               "datos, módulos e instrumentación suficientes. Las reglas de evidencia, la severidad y "
               "los rangos de persistencia de cada patrón se establecen en la sección 17.1.5.2.")
E[183] = ("D",)
E[184] = ("E", "La salida principal del motor no es una alerta aislada, sino una secuencia de eventos "
               "derivados que describen el ciclo de vida del patrón, desde el inicio del candidato "
               "hasta la confirmación, el sostenimiento y la resolución o el descarte por evidencia "
               "insuficiente. La alerta interna se registra sólo cuando una transición válida confirma "
               "el patrón, lo que evita emitir alertas por cada frame positivo y permite analizar "
               "episodios con inicio, duración, evidencia causal y cierre.")
E[185] = ("D",)
E[186] = ("D",)
E[187] = ("E", "Cada transición conserva trazabilidad suficiente para explicar su origen, con la "
               "configuración de corrida, el patrón evaluado, la condición asociada, la evidencia "
               "considerada, la ventana temporal, los umbrales aplicados, el estado previo, el estado "
               "nuevo y la referencia temporal. Esa información permite reconstruir por qué se generó "
               "una alerta, por qué se resolvió un episodio, qué evidencia se descartó y qué "
               "parámetros condicionaron el resultado.")
E[188] = ("H", "17.3.6.3. Transporte, persistencia y trazabilidad experimental")
E[189] = ("E", "La arquitectura diferencia el canal de transporte del repositorio persistente, de modo "
               "que la durabilidad no se atribuya a un mecanismo de mensajería diseñado para baja "
               "latencia. El repositorio es la fuente de verdad. Cada evento de percepción se escribe "
               "en un archivo ~JSONL~ de sólo adición antes de publicarse, y los cambios de estado, "
               "las alertas, las métricas y los errores siguen la misma regla en sus componentes "
               "respectivos. Si el canal falla, el hecho persistido permanece disponible para "
               "relectura.")
E[190] = ("D",)
E[191] = ("E", "En el camino de ejecución en vivo el canal adopta ~ZeroMQ~ con patrón "
               "publicador-suscriptor, ~msgpack~, tópicos por tipo de evento y un número de secuencia "
               "monótono dentro del envoltorio versionado del bus. El plano de control consume ese "
               "contrato por el canal de detecciones y no interpreta formatos propios de un detector "
               "ni recibe frames crudos. El payload publicado corresponde al mismo contenido lógico "
               "persistido, de manera que la corrida pueda releerse por el camino diferido sin "
               "redefinir la evidencia.")
E[192] = ("E", "Todo consumidor se suscribe antes de que su productor publique, y el orquestador "
               "verifica esa precondición al crear la corrida, porque la respuesta de creación de un "
               "consumidor implica su disponibilidad. El orden efectivo de arranque de los módulos se "
               "documenta en la sección 17.4.")
E[193] = ("E", "La pérdida se detecta mediante huecos de secuencia. Un hueco incrementa "
               "~bus_dropped_events~, degrada la corrida y queda expuesto en el reporte, y nunca se "
               "interpreta como ausencia de evidencia en la escena.")
E[194] = ("E", "El cierre de la corrida se propaga mediante un evento de ciclo de vida cuyo hito de "
               "finalización delimita el final lógico y permite cerrar consumidores, consolidar "
               "artefactos y distinguir un fin normal de una interrupción.")
E[195] = ("E", "La sustitución futura por un broker conserva la misma frontera contractual, porque la "
               "durabilidad, la re-evaluación y la causalidad no dependen de la tecnología del canal "
               "sino de la regla de persistir antes de publicar y de los esquemas versionados.")
E[196] = ("H4", "17.3.6.4. Cadena de traducción entre condición, evidencia, patrón y alerta")
E[197] = ("E", "La cadena que va de la condición observable hasta la alerta atraviesa los dos planos. "
               "La condición del catálogo metodológico define qué fenómeno se monitorea, la estrategia "
               "de detección establece si la evidencia se busca mediante un prompt directo, una "
               "combinación de consultas, evidencia auxiliar o reglas contextuales, el plano de medios "
               "publica evidencia perceptiva normalizada y el plano de control la evalúa mediante el "
               "patrón correspondiente. Cuando la evaluación confirma el episodio, registra una alerta "
               "interna, que es una salida asistiva del sistema y no equivale a una notificación "
               "externa ni a una certificación normativa. La Figura 4.4 resume esa cadena.")
for i in (198, 199, 200, 201):
    E[i] = ("D",)
E[202] = ("E", "Figura 4.4", RPR_B)
E[205] = ("E", "**Nota.** La figura muestra cómo una condición definida metodológicamente se "
               "materializa en la arquitectura. La estrategia orienta la producción de evidencia en "
               "el plano de medios, el patrón la evalúa en el plano de control y la alerta interna "
               "registra el episodio confirmado.")
for i in (206, 207, 208, 209, 210):
    E[i] = ("D",)

# ------------------------------------------------- 17.3.7 Distribución de alertas confirmadas
E[211] = ("H", "17.3.7. Distribución de alertas confirmadas")
E[212] = ("E", "La alerta interna es el hecho terminal del plano de control y todavía no es un aviso. "
               "El tramo de distribución la convierte en intentos de entrega registrados sin participar "
               "del razonamiento que la produjo.")
E[213] = ("D",)
E[214] = ("E", "El plano de control publica cada alerta confirmada en un bus de alertas dedicado, y el "
               "módulo de distribución la consume desde allí, aplica la política de notificación y "
               "registra el resultado de cada intento. No constituye un tercer plano ni un cuarto rol "
               "funcional, sino un módulo desacoplado, y esa condición es la que impide que la "
               "indisponibilidad de un canal externo se propague al motor de patrones.")
E[215] = ("E", "El pipeline de distribución comprende una fuente de alertas, una política de "
               "notificación, un sobre versionado, un adaptador de canal y un ~ledger~ de entregas. La "
               "misma lógica admite la relectura desde artefactos persistidos y el consumo en vivo "
               "desde el bus de alertas, sin modificar la semántica de la alerta de entrada.")
E[216] = ("E", "La política ordinaria prioriza trazabilidad, idempotencia y operación no bloqueante. "
               "Una falla del canal genera un resultado de entrega y un error interpretable, y no "
               "invalida ni elimina la alerta interna. Toda notificación externa es una salida "
               "derivada de la alerta interna y se mide por separado.")
E[217] = ("D",)
E[218] = ("E", "El tramo separa el dato del gobierno. Las alertas confirmadas llegan por el bus de "
               "alertas en sentido único desde el plano de control, mientras que las órdenes de ciclo "
               "de vida llegan por una interfaz de gobierno propia del módulo, que permite crear, "
               "consultar, cancelar y descartar corridas de entrega. Para la relectura diferida el "
               "módulo conserva una entrada offline sobre alertas persistidas, y ambos caminos "
               "utilizan los mismos contratos de alerta interna, sobre de notificación y registro de "
               "entrega, por lo que la modalidad de ejecución no modifica la semántica de la alerta "
               "ni la del resultado.")
E[223] = ("E", "**Nota.** El módulo de distribución conserva su propio estado operativo y su "
               "~ledger~, y no utiliza el almacenamiento continuo de video ni requiere acceso a "
               "frames crudos.")
E[224] = ("D",)
E[225] = ("E", "El conjunto de patrones adoptado no suprime confirmaciones, porque cada alerta interna "
               "se registra para conservar la dinámica real del episodio. La decisión es deliberada. "
               "El motor dispone de control de re-confirmación por patrón y sujeto y el núcleo lo deja "
               "inactivo, ya que un motor que suprimiera dejaría de reflejar la duración del episodio "
               "y no permitiría distinguir una condición que persiste de una que se resolvió.")
E[226] = ("E", "La supresión de re-notificación se reubica en la política del módulo de distribución "
               "y, al reubicarse, cambia de granularidad. El motor la aplicaría por patrón y sujeto, "
               "mientras que la política de entrega aplica una ventana de silencio por condición y "
               "fuente, porque para una notificación asistiva lo relevante es que esa condición en esa "
               "cámara ya fue avisada. La agrupación de avisos y la limitación de tasa quedan como "
               "punto de extensión de la política. Una alerta suprimida para comunicación existió y "
               "continúa siendo medible, y las re-alertas de un episodio activo se informan por "
               "separado y no se computan como falsos positivos, de modo que una decisión de "
               "comunicación no altere la precisión del motor.")
E[227] = ("E", "El ~ledger~ de entregas es de sólo agregado, aplica una clave de idempotencia por "
               "notificación y canal y acumula entre corridas, de manera que un reprocesamiento no "
               "vuelva a entregar lo ya entregado. Cada fila conserva el número de intento, la marca "
               "temporal, el resultado, el motivo de error y la confirmación del canal, y distingue "
               "entrega exitosa, supresión por política, descarte por duplicado, falla de un intento y "
               "descarte definitivo por agotamiento de reintentos. Cada fila registra además la "
               "modalidad en que se midió la latencia del tramo, que se informa siempre separada por "
               "modalidad, porque en relectura diferida el intervalo incorpora el ritmo de reinyección "
               "de las alertas persistidas, que es propiedad del reprocesamiento y no del canal. El "
               "detalle operativo del ~ledger~, incluida la unidad de conteo del tramo, se documenta "
               "en la sección 17.4.")
E[228] = ("D",)

# ---------------------------------------- 17.3.8 Contratos, trazabilidad y evidencia visual
E[229] = ("H", "17.3.8. Contratos, trazabilidad y evidencia visual")
E[230] = ("E", "Los contratos estabilizan la semántica de intercambio entre componentes y definen qué "
               "información cruza cada frontera y bajo qué versión. En la arquitectura consolidada del "
               "núcleo se expresan como modelos de datos versionados, con serializaciones explícitas e "
               "interfaces concretas, y cada uno queda asociado a una corrida para que productores y "
               "consumidores evolucionen de forma independiente. La versión viaja dentro del payload y "
               "no en el envoltorio de transporte, de manera que el canal pueda cambiar sin que el "
               "hecho persistido pierda la identificación de su esquema. Las capacidades futuras "
               "evolucionan de forma aditiva sin romper la lectura de corridas históricas.")
E[231] = ("D",)
E[232] = ("E", "Las fronteras son lógicas y no prescriben que cada responsabilidad se despliegue en "
               "una máquina, un proceso o un contenedor independiente.")
E[233] = ("H", "17.3.8.1. Contratos mínimos e interfaces")
E[234] = ("E", "Todo contrato declara su identidad de esquema y su versión como primer elemento del "
               "payload. La Tabla 46 reúne los contratos mínimos de la ejecución experimental.")
E[238] = ("E", "**Nota.** Los contratos de referencia temporal y distribución tienen el mismo "
               "estatuto formal que los eventos de percepción y control, porque una medición o una "
               "entrega no es reproducible si su entrada carece de versión y procedencia.")
E[239] = ("E", "El evento central del sistema es el evento de percepción, que agrupa la identidad de "
               "esquema versionada, la corrida, la unidad visual, la fuente, el modelo, los prompts, "
               "las detecciones y los tiempos. Cada detección conserva etiqueta, prompt, confianza, "
               "caja en píxeles y normalizada, y área. El ~detection_id~ sólo identifica una detección "
               "dentro de la unidad visual y no constituye identidad entre frames. Los campos "
               "opcionales se incorporan de forma aditiva y se omiten cuando no están disponibles.")
E[240] = ("E", "La referencia temporal de evaluación impone dos invariantes de validez. La identidad "
               "de la fuente de la corrida y la del clip anotado deben coincidir, y para el banco "
               "temporal se utiliza ~source_id~ = ~clip_id~. Y la incertidumbre no fabrica una "
               "infracción, de modo que cuando el estado del EPP no es juzgable el episodio no se "
               "extiende como violación.")
E[241] = ("E", "La cadena temporal conserva cinco hitos por alerta, que son la primera evidencia "
               "positiva identificada por ~unit_id~, la transición a candidato, la transición a "
               "confirmado, el registro de la alerta interna y, cuando existe distribución, la "
               "confirmación de entrega. Esos hitos permiten medir cada tramo sin mezclar relojes ni "
               "poblaciones.")
E[242] = ("D",)
E[243] = ("E", "La superficie de crecimiento del evento de percepción se mantiene acotada y separada "
               "de las reglas de riesgo. La identidad temporal de sujeto es un campo opcional y la "
               "única identidad válida entre frames, que el plano de control puede materializar por "
               "configuración sin que el plano de medios necesite emitirla. La velocidad, la "
               "dirección, los puntos clave de pose y las máscaras de segmentación quedan previstos "
               "como campos opcionales que no modifican la semántica mínima del evento ni desplazan al "
               "bounding box. Las relaciones entre sujeto, evidencia de soporte y clase ausente "
               "pertenecen al plano de control, porque el plano de medios publica detecciones "
               "individuales.")
E[244] = ("H4", "17.3.8.2. Repositorio de hechos y reconstrucción experimental")
E[245] = ("E", "La trazabilidad experimental permite reconstruir cómo una corrida produjo una alerta "
               "interna. La arquitectura conserva la relación entre la configuración de corrida, la "
               "fuente visual, el modelo utilizado, los prompts activos, la evidencia perceptiva, la "
               "transición de estado del patrón, la alerta registrada y las métricas o errores "
               "asociados. Sin esa relación una alerta pierde valor experimental, porque no puede "
               "auditarse, compararse ni analizarse con suficiente rigor.")
E[246] = ("D",)
E[247] = ("D",)
E[248] = ("E", "El repositorio utiliza archivos ~JSONL~ de sólo adición por corrida y por tipo de "
               "hecho. La regla impide la sobrescritura silenciosa y ofrece una representación simple, "
               "inspeccionable y re-evaluable sin introducir una base de datos como dependencia del "
               "núcleo.")
E[250] = ("E", "Toda alerta puede reconstruirse hasta la configuración efectiva, el conjunto de "
               "prompts, el modelo, la fuente y la versión de código que la produjeron. La "
               "persistencia no requiere video crudo continuo y mantiene separados los hechos "
               "originales de sus proyecciones tabulares o reportes.")
E[251] = ("D",)
E[252] = ("E", "Los hechos que la reconstrucción exige exceden a los contratos de intercambio. Junto "
               "al inicio y cierre de corrida, al manifiesto con las configuraciones efectivas y a la "
               "procedencia e identidad de la fuente, el repositorio conserva los eventos de "
               "percepción, las unidades omitidas o descartadas con su causa, los cambios de estado "
               "del patrón, la primera evidencia positiva, las alertas internas, las entregas cuando "
               "el tramo está habilitado, las métricas con su estado de aplicabilidad y los errores y "
               "anomalías. Los hechos asociados a seguimiento temporal, zonas, distribución externa, "
               "adaptación de modelos o evidencia visual controlada se incorporan sólo cuando la "
               "corrida habilita esas capacidades y no forman parte del conjunto mínimo para CR-01 y "
               "CR-02.")
E[253] = ("D",)
E[254] = ("D",)
E[256] = ("E", "Esta selección prioriza la reconstrucción de la cadena causal de la alerta. Una "
               "detección aislada no explica un episodio, porque debe relacionarse con la "
               "configuración que la produjo, el patrón que la evaluó, la transición que confirmó la "
               "condición y las métricas o anomalías que condicionaron el resultado. Por esa razón los "
               "errores y descartes relevantes tienen el mismo valor interpretativo que los eventos "
               "funcionales, ya que permiten distinguir una ausencia real de evidencia de una falla "
               "técnica, un descarte por muestreo o una limitación de la fuente.")
E[257] = ("E", "Las extensiones condicionadas mantienen esta lógica. Si se incorpora seguimiento "
               "temporal, zonas, reglas espaciales, notificaciones externas o adaptación de modelos, "
               "esos hechos se persisten como información adicional de la corrida, sin desplazar la "
               "cadena mínima de reconstrucción ni convertir capacidades exploratorias en requisitos "
               "del núcleo experimental.")
E[258] = ("D",)
E[259] = ("H", "17.3.8.3. Política de evidencia visual mínima")
E[260] = ("E", "La arquitectura adopta una política de minimización de evidencia visual. En el "
               "comportamiento ordinario del prototipo la trazabilidad se apoya en identificadores, "
               "metadatos, eventos, métricas, coordenadas, referencias temporales y relaciones "
               "causales entre hechos persistidos. El almacenamiento continuo de video crudo no forma "
               "parte del flujo base, porque aumenta volumen, complejidad y riesgo de privacidad sin "
               "ser necesario para reconstruir las decisiones experimentales.")
E[261] = ("E", "Cuando la revisión técnica, la validación o la comunicación académica requieren "
               "evidencia visual, ésta se conserva como artefacto controlado, en forma de ~snapshot~, "
               "recorte anotado, clip breve, huella criptográfica, referencia a archivo o vínculo "
               "asociado a una alerta o corrida específica. Su uso se justifica por la finalidad "
               "experimental, cuenta con criterios explícitos de acceso, retención y anonimización, y "
               "no reemplaza métricas, eventos persistidos ni criterios de evaluación.")
E[262] = ("E", "La política preserva el carácter asistivo y no identificatorio de la plataforma. El "
               "sistema no realiza reconocimiento facial, no identifica nominalmente a trabajadores, "
               "no extrae biometría y no emite decisiones normativas autónomas. La alerta interna "
               "orienta la atención humana sobre una condición visualmente observable, y la "
               "interpretación final y cualquier acción preventiva permanecen fuera del sistema "
               "automatizado.")

# ------------------------------------- 17.3.9 Observabilidad y aplicabilidad de métricas
E[263] = ("H", "17.3.9. Observabilidad y aplicabilidad de métricas")
E[264] = ("E", "La observabilidad forma parte del contrato experimental. Cada métrica declara la señal "
               "que utiliza, el inicio y el cierre del reloj, la unidad, la población y la condición "
               "de aplicabilidad. Cuando una medición no tiene significado, la plataforma conserva la "
               "causa en lugar de publicar cero u omitir el campo.")
E[265] = ("D",)
E[266] = ("E", "Tabla 47", RPR_B)
E[269] = ("E", "**Nota.** La cadena temporal completa se informa por tramos, y cada tramo declara su "
               "hito inicial, su hito final y su dominio de reloj. Los percentiles de tramos "
               "diferentes no son aditivos y no deben sumarse para fabricar una latencia de extremo a "
               "extremo. La medición del plano de medios comienza en el ingreso de la unidad al host "
               "de procesamiento y no en la captura física, que constituye un tramo propio.")
E[270] = ("D",)
E[271] = ("D",)
E[272] = ("D",)
E[274] = ("E", "Las latencias dentro de un mismo host utilizan reloj monotónico local, y los "
               "monotónicos de hosts distintos no se restan. Cuando un trayecto cruza dominios de "
               "reloj sin una sincronización válida, la métrica se declara no interpretable con su "
               "causa.")
E[275] = ("E", "El criterio de detección positiva se comparte con el motor de patrones, de modo que la "
               "evaluación no reimplemente una segunda definición de evidencia y no aparezcan "
               "divergencias silenciosas entre el sistema que decide y el sistema que mide. La Tabla "
               "48 reúne las señales observables sobre las que se apoyan estas mediciones.")
E[276] = ("D",)
E[277] = ("E", "Tabla 48", RPR_B)
E[280] = ("E", "Cada métrica incluye un estado y una causa. Los estados admitidos son ~computed~, "
               "~applicable_not_computed~, ~not_applicable~ y ~not_interpretable~, y la plataforma no "
               "publica un cero cuando lo correcto es declarar una causa.")
E[281] = ("E", "Una fuente de imágenes independientes produce ~not_applicable~ con causa "
               "~non_temporal_source~ para los patrones temporales. Un trayecto con monotónicos de dos "
               "hosts produce ~not_interpretable~ con causa ~cross_node_monotonic_clock~. Una corrida "
               "sin referencia anotada produce ~not_applicable~ con causa ~no_ground_truth~. Y un "
               "tiempo hasta la primera detección sin evidencia positiva permanece nulo con su causa.")
E[282] = ("D",)
E[283] = ("E", "El reporte consolida el manifiesto, las configuraciones efectivas, las métricas por "
               "tramo, el estado de aplicabilidad, las alertas, las re-alertas, los descartes, los "
               "errores, los recursos y las limitaciones de interpretación, y cada valor mantiene la "
               "condición, el escenario y la población sobre la que se calculó.")
E[284] = ("D",)
E[285] = ("E", "El reporte constituye una proyección de hechos persistidos. Puede regenerarse sin "
               "modificar los eventos originales y no se utiliza como fuente de verdad cuando existe "
               "el artefacto primario.")

# ------------------------- 17.3.10 Escenarios experimentales y topología de referencia
E[286] = ("H", "17.3.10. Escenarios experimentales y topología de referencia")
E[287] = ("E", "La definición metodológica de ambos escenarios corresponde a la sección 17.1.4.2, y "
               "aquí se conservan únicamente sus consecuencias arquitectónicas. En DBE la fuente es "
               "regulable y puede releerse bajo la misma configuración, de modo que la arquitectura "
               "priorice identidad estable de unidades, orden lógico, persistencia previa y "
               "reconstrucción determinista de eventos, patrones y alertas. En EBE la fuente opera en "
               "vivo y la escena continúa evolucionando aunque el pipeline se retrase, de modo que la "
               "arquitectura instrumente captura o recepción, colas, descartes, ~jitter~, actualidad y "
               "dominio de reloj. Ninguno de los dos es una topología física.")
for i in (288, 289, 290, 291):
    E[i] = ("D",)
E[292] = ("H", "17.3.10.1. Equivalencia arquitectónica y alcance de EBE")
E[293] = ("E", "DBE y EBE convergen en la misma arquitectura una vez normalizada la entrada visual. La "
               "diferencia entre escenarios se ubica antes y alrededor de la disponibilidad del frame, "
               "en el origen de la fuente, la referencia temporal, la política de muestreo, el control "
               "de ritmo y la instrumentación de omisiones o descartes. Después de esa frontera, la "
               "inferencia OVD, el postproceso, la publicación de evidencia perceptiva, la evaluación "
               "de patrones y el registro de alertas internas mantienen la misma semántica.")
E[294] = ("E", "La equivalencia evita construir dos flujos incompatibles, cuyos resultados dejarían de "
               "ser comparables. Al conservar la misma estructura de eventos, métricas y hechos "
               "persistibles, la arquitectura permite distinguir qué parte de la variación proviene de "
               "la fuente continua y qué parte del detector o de la evaluación de patrones.")
E[295] = ("D",)
E[296] = ("D",)
E[297] = ("E", "La comparación entre escenarios declara explícitamente qué variables cambiaron. Una "
               "corrida DBE y una corrida EBE pueden compartir modelo, prompts, umbrales y reglas de "
               "patrón y diferir en fuente, temporización, iluminación, compresión o criterio de "
               "descarte, y esas diferencias se registran como parte de la configuración y de la "
               "observabilidad.")
E[298] = ("D",)
E[299] = ("D",)
E[301] = ("E", "EBE admite cámaras IP por RTSP, la OAK-D Pro PoE y otras fuentes continuas declaradas "
               "mediante el mismo adaptador conceptual. La arquitectura contempla tanto el dispositivo "
               "candidato como la contingencia con cámara IP convencional, y ninguna alternativa "
               "modifica los contratos de percepción y control.")
E[302] = ("D",)
E[303] = ("D",)
E[304] = ("E", "El rol de captura puede operar como ingesta, preprocesamiento no semántico o "
               "preselección conservadora. La variante de preselección liviana en el borde es "
               "opcional, está deshabilitada por defecto y opera con el criterio de degradación segura "
               "fijado para las capacidades opcionales del plano de medios, de modo que una falla o "
               "una incertidumbre del preselector no elimine la unidad del flujo principal. Toda "
               "transformación, descarte o cambio de resolución se registra.")
E[305] = ("E", "La comparación entre una corrida DBE sobre archivo y una corrida EBE del mismo "
               "contenido exige un ancla común entre el tiempo de medio y el reloj de pared. Sin ese "
               "ancla, el matching temporal contra la referencia anotada se declara no interpretable, "
               "mientras que la integridad del bus y la relectura offline continúan siendo evaluables "
               "por separado. La Tabla 49 reúne las condiciones que cada corrida EBE debe registrar "
               "para que sus resultados sean interpretables.")
E[306] = ("D",)
E[307] = ("E", "Tabla 49", RPR_B)
E[311] = ("H", "17.3.10.2. Naturaleza temporal de la fuente y aplicabilidad")
E[312] = ("E", "La procedencia DBE o EBE no determina por sí sola si una fuente sostiene razonamiento "
               "temporal. Un video de archivo y un stream en vivo son temporales, mientras que un "
               "conjunto de imágenes independientes no lo es. La configuración deriva esta propiedad "
               "del tipo de fuente y no permite que el operador la contradiga.")
E[314] = ("E", "Las imágenes permiten afirmar sobre percepción. Los clips temporales permiten afirmar "
               "además sobre estado y episodios. Las fuentes en vivo permiten afirmar también sobre "
               "transporte, actualidad y comportamiento operativo. Cada reporte limita sus "
               "conclusiones al régimen que la fuente permite observar.")
E[315] = ("H4", "17.3.10.3. Roles funcionales y unidades desplegables de referencia")
E[316] = ("E", "La topología de referencia materializa los roles funcionales establecidos en la "
               "sección 17.1.4.1 y ubica en ella al módulo de distribución. Ninguno de los roles "
               "equivale necesariamente a una máquina dedicada, y la distribución física de los "
               "componentes no forma parte del compromiso conceptual del diseño.")
E[317] = ("E", "La topología dispone un nodo de borde para captura y un nodo central con GPU para "
               "procesamiento. El nodo de entrenamiento permanece fuera del camino operativo de "
               "inferencia, porque cualquier adaptación produce un ~checkpoint~ candidato que se "
               "evalúa después sobre el nodo central y se mantiene como rama comparativa separada. El "
               "módulo de distribución se modela como una unidad desplegable propia, gobernada por su "
               "propia interfaz de gobierno y consumidora del bus de alertas, y puede co-ubicarse con "
               "el nodo central o separarse sin modificar los contratos de alerta interna, "
               "notificación y entrega. La Tabla 50 fija la correspondencia entre roles y unidades "
               "desplegables.")
for i in (318, 319, 320, 321):
    E[i] = ("D",)
E[322] = ("E", "Tabla 50", RPR_B)

# ---------------------------- 17.3.11 Riesgos, plan de materialización y cierre
E[326] = ("H", "17.3.11. Riesgos, plan de materialización y cierre")
E[327] = ("E", "Los riesgos arquitectónicos se formulan como modos de falla observables y se vinculan "
               "con una mitigación concreta. La arquitectura no presupone que una mitigación elimina "
               "el riesgo, sino que exige instrumentarlo y declarar su efecto sobre la interpretación "
               "de la corrida. La Tabla 51 reúne esos riesgos y sus mitigaciones de diseño.")
E[328] = ("E", "Tabla 51", RPR_B)
E[331] = ("E", "**Nota.** La materialización y la verificación de estos riesgos se documentan en las "
               "secciones de implementación y evaluación. Aquí se conserva su tratamiento de diseño.")
E[332] = ("D",)
E[333] = ("E", "El plan de materialización ordena dependencias de diseño y no reemplaza el registro de "
               "implementación. El núcleo se construye primero sobre DBE para estabilizar contratos, "
               "evidencia, patrones y reporte, y luego se incorporan EBE y las capacidades opcionales "
               "sin modificar la semántica del flujo base. La Tabla 52 fija el entregable "
               "arquitectónico de cada incremento y el criterio que permite decidir si es verificable. "
               "El estado ejecutado de cada ítem corresponde a la sección 17.4.")
E[334] = ("D",)
E[335] = ("E", "Tabla 52", RPR_B)
E[339] = ("E", "La frontera de extensibilidad distingue tres clases de cambio. Una condición nueva del "
               "tipo «sujeto sin EPP» requiere una definición declarativa de patrón y vocabulario, sin "
               "modificar contratos ni reentrenar el modelo. Una familia relacional, zonal o de "
               "trayectoria requiere un evaluador nuevo en el plano de control. Un modelo, una fuente "
               "o un canal nuevos requieren sus respectivos adaptadores y mantienen estables los "
               "contratos centrales. Esa frontera evita presentar la extensibilidad open-vocabulary "
               "como una capacidad ilimitada, y el costo medido de incorporar extensiones se documenta "
               "en las secciones de implementación y evaluación.")
E[340] = ("D",)
E[341] = ("E", "El diseño define una plataforma experimental compuesta por el plano de medios, el "
               "plano de control, el soporte experimental y un tramo desacoplado de distribución, que "
               "protege la ruta crítica, separa la evidencia de su interpretación y conserva una "
               "cadena causal reconstruible desde la fuente hasta la entrega. La granularidad de "
               "escena y la granularidad de sujeto se tratan como configuraciones semánticamente "
               "distintas, y la identidad personal permanece fuera del alcance.")
E[342] = ("D",)
E[343] = ("D",)
E[344] = ("D",)
E[345] = ("E", "El capítulo deja preparado el paso a la implementación sin anticipar sus resultados. "
               "La sección 17.4 documenta qué componentes se materializaron y cómo se verificaron, y "
               "la sección 17.5 concentra las mediciones y su interpretación experimental.")
E[346] = ("E", "El diseño se considera completo cuando cada una de sus decisiones, desde la separación "
               "de responsabilidades hasta la extensibilidad delimitada, posee un criterio verificable "
               "en la implementación.")

# ------------------------------------------------------------------ párrafos nuevos (INSERTS)
INS = {
    58: [("El intercambio de datos en ejecución ocurre mediante un bus ~ZeroMQ~ con patrón "
          "publicador-suscriptor y serialización binaria ~msgpack~, con un canal de detecciones entre "
          "los planos y un canal de alertas hacia la distribución. Se adopta ~ZeroMQ~ porque ofrece "
          "transporte de baja latencia sin requerir un broker como dependencia adicional del "
          "prototipo, y porque el patrón publicador-suscriptor desacopla al productor de sus "
          "consumidores sin bloquear la ruta crítica. ~msgpack~ reduce el costo de serialización "
          "respecto del texto plano y conserva estructuras autodescriptivas."),
         ("La durabilidad no se le exige al canal. Cada hecho se persiste en archivos ~JSONL~ de sólo "
          "adición antes de publicarse, de modo que la evidencia pueda releerse y reevaluarse sin "
          "depender de la mensajería. El gobierno fija la configuración y el ciclo de vida, el bus "
          "transporta los hechos de ejecución y la persistencia sostiene la relectura sin constituir "
          "un tercer patrón de acople.")],
    109: [("En corridas DBE, o con fuentes cuya lectura puede regularse, la prioridad es preservar "
           "reproducibilidad, orden lógico y trazabilidad de las unidades procesadas, y si no se "
           "procesan todos los frames la selección es determinista y se mantiene constante entre "
           "corridas comparables. En corridas EBE, o con fuentes en vivo, la prioridad es que el "
           "atraso acumulado no crezca indefinidamente y que toda omisión, irregularidad temporal o "
           "descarte quede registrada. El resultado esperado no es maximizar la cadencia de forma "
           "aislada sino hacer interpretable el comportamiento del pipeline, porque un sistema que "
           "procesa menos frames puede ser válido para una corrida exploratoria y esa reducción debe "
           "ser visible para no confundir rendimiento con cobertura temporal. Los detalles de colas, "
           "buffers o algoritmos de descarte corresponden a la implementación.")],
    114: [("Sobre esa cadena el diseño mantiene una ruta no bloqueante. Si el bus interno, la "
           "persistencia, la inspección o una salida externa fallan o se saturan, esa condición se "
           "registra como parte de la ejecución y no convierte a esos consumidores en dependencia "
           "directa del procesamiento visual. El plano hace visible además la variabilidad temporal, "
           "porque una latencia aparentemente baja puede ocultar pérdida de frames, colas saturadas o "
           "reemplazo de frames antiguos por frames recientes, y por eso registra timestamps por "
           "tramo, profundidad de cola cuando corresponde, frames aceptados, frames omitidos y "
           "descartes."),
          ("Los adaptadores absorben la heterogeneidad de los detectores OVD, que difieren en formato "
           "de entrada, tipo de prompt, estructura de salida, semántica de puntajes y costo de "
           "inferencia, y entregan una evidencia perceptiva estable que no acopla al plano de control "
           "con un modelo específico ni con los detalles internos de su implementación. La "
           "persistencia temporal de un patrón, la histéresis, la severidad y el registro interno de "
           "la alerta pertenecen al motor de patrones, de modo que el plano de medios pueda mejorar "
           "la calidad de la evidencia perceptiva sin decidir si una condición observada se convirtió "
           "en una situación de riesgo confirmada.")],
    135: [("El plano recibe evidencia perceptiva normalizada, selecciona los patrones activos, evalúa "
           "la evidencia espacial y temporal, administra el estado de cada patrón y registra una "
           "alerta interna cuando confirma un episodio, mientras persiste transiciones, métricas y "
           "errores. La evaluación no ejecuta inferencia visual, no asigna identidad personal y no "
           "determina cumplimiento normativo, porque aplica reglas declaradas de asociación espacial, "
           "persistencia, granularidad e histéresis. La alerta interna que sigue a la confirmación es "
           "el hecho principal del sistema y precede a cualquier notificación.")],
    85: [("Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de "
          "ausencia (~E-IND~). La frontera que esa elección fija es explícita. El plano de medios "
          "informa qué entidades observó, dónde y con qué confianza. El plano de control decide si la "
          "evidencia del elemento de protección se asocia al sujeto, construye el estado evaluable de "
          "la condición y lo estabiliza antes de registrar una alerta."),
         ("La estrategia se adopta por auditabilidad, porque cada evaluación puede reconstruirse a "
          "partir de la caja del sujeto, la región analizada, las detecciones de protección, los "
          "umbrales y la regla aplicada, y así la ausencia no se presenta como una conclusión opaca "
          "del modelo. La detección directa (~E-DIR~) y las variantes híbridas (~E-HYB~) se conservan "
          "como ramas comparativas configurables, con conjuntos de prompts y reglas identificados por "
          "separado, y comparten los contratos de publicación, evaluación temporal y registro, de modo "
          "que la comparación no requiera alterar la arquitectura central.")],
    264: [("La instrumentación se ancla en los puntos donde la arquitectura ya produce hechos. Las "
           "transiciones del motor sostienen las métricas del plano de control, porque el tiempo hasta "
           "la primera detección se ancla en la primera evidencia perceptiva relevante, la latencia de "
           "alerta del sistema se cierra con el registro de la alerta interna que sigue a la "
           "transición a confirmado y la tasa de detección sostenida se calcula sobre la continuidad "
           "del episodio. Las definiciones operacionales de cada métrica, sus hitos y sus reglas de "
           "lectura se establecen en las secciones 17.1.7.3 y 17.1.7.5 y en el Anexo D. La Tabla 47 "
           "ubica cada medición en el tramo arquitectónico que la produce.")],
}

# --------------------------------------------------------------------------- operaciones de tabla
# (índice de unidad de la tabla) → lista de operaciones
TBL = {
    36: [("cell", 3, 2,  # DA-03, justificación (COM4 vive en esta celda)
          "Cada preocupación tiene un régimen propio, porque el gobierno es puntual y de solicitud y "
          "respuesta, el transporte es continuo y no debe bloquear la ruta crítica, y la persistencia "
          "sobrevive a la corrida para habilitar su relectura."),
         ("cell", 11, 1,  # DA-11, decisión (COM5)
          "Permitir preselección liviana en el rol de captura como variante opcional, conservadora, "
          "deshabilitada por defecto y fail-open.")],
    75: [("cell", 10, 2,  # política de distribución: quitar la segunda mención del cooldown
          "Concentra los controles de comunicación aguas abajo de la alerta interna.")],
    89: [("delrows", [6, 7, 8, 9, 10, 11, 12, 13])],  # CR-03…CR-06 (8 filas) → Anexo C
    181: [("cell", 1, 1, "Detecciones positivas de ~person~ y ~helmet~, con evaluación de la región "
                         "cefálica por sujeto."),
          ("cell", 2, 1, "Detecciones positivas de ~person~ y ~vest~, con evaluación de la región del "
                         "torso por sujeto."),
          ("cell", 3, 1, "Persona en altura o sobre estructura elevada junto con ausencia o baja "
                         "evidencia de sistema anticaídas visible."),
          ("cell", 4, 1, "Borde, plataforma o zona elevada sin protección colectiva, con personas "
                         "próximas."),
          ("cell", 5, 1, "Maquinaria y personas con relación de proximidad sostenida."),
          ("cell", 6, 1, "Persona dentro de un polígono o zona definida externamente.")],
    255: [("delall",)],   # Tabla 47 — hechos persistibles (D-E)
    273: [("delall",)],   # Tabla 49 — diccionario de métricas (D-F)
    300: [("delall",)],   # Tabla 51 — comparación DBE/EBE (D-G)
}

# ------------------------------------------------- comentarios re-anclados (id → unidad destino)
REANCLA = {1: 1, 2: 1}


def wrap_comment(p: str, cid: int) -> str:
    """Envuelve los runs insertados del párrafo con el rango del comentario `cid`."""
    m = re.search(r'<w:ins w:id="\d+" w:author="[^"]*" w:date="[^"]*">', p)
    if not m:
        return p
    start = f'<w:commentRangeStart w:id="{cid}"/>'
    end = (f'<w:commentRangeEnd w:id="{cid}"/><w:r>{RPR}'
           f'<w:commentReference w:id="{cid}"/></w:r>')
    idx_end = p.index("</w:ins>", m.end()) + len("</w:ins>")
    return p[:m.start()] + start + p[m.start():idx_end] + end + p[idx_end:]


# ================================================================================ aplicación
def main() -> int:
    src = zipfile.ZipFile(SRC)
    xml = src.read("word/document.xml").decode("utf8")
    bs = xml.index("<w:body>") + len("<w:body>")
    be = xml.rindex("</w:body>")
    head, body, tail = xml[:bs], xml[bs:be], xml[be:]
    units, resto = split_units(body)
    print(f"unidades: {len(units)} | resto del cuerpo: {len(resto)} bytes")

    out = []
    stats = {"E": 0, "D": 0, "H": 0, "K": 0, "INS": 0, "TBL": 0}
    for i, (kind, raw, gap) in enumerate(units):
        out.append(gap)
        if kind == "tbl":
            if i in TBL:
                t = raw
                for op in TBL[i]:
                    if op[0] == "cell":
                        t = edit_cell(t, op[1], op[2], op[3])
                    elif op[0] == "delrows":
                        t = del_rows(t, set(op[1]))
                    elif op[0] == "delall":
                        t = del_table(t)
                stats["TBL"] += 1
                out.append(t)
            else:
                out.append(raw)
            continue

        op = E.get(i)
        if op is None:
            out.append(raw)
            stats["K"] += 1
        elif op[0] == "D":
            p = raw
            quitar = [cid for cid, dest in REANCLA.items()
                      if f'<w:commentRangeStart w:id="{cid}"/>' in raw]
            if quitar:
                p = strip_comment_anchors(p, quitar)
            out.append(delete_para(p))
            stats["D"] += 1
        elif op[0] in ("H", "H4"):
            p = edit_para(raw, op[1])
            if op[0] == "H4":
                p = p.replace('<w:pStyle w:val="Heading3"/>', '<w:pStyle w:val="Heading4"/>', 1)
            out.append(p)
            stats["H"] += 1
        else:
            rpr = op[2] if len(op) > 2 else RPR
            after = op[3] if len(op) > 3 else None
            p = edit_para(raw, op[1], rpr, after)
            for cid, dest in REANCLA.items():
                if dest == i:
                    p = wrap_comment(p, cid)
            out.append(p)
            stats["E"] += 1

        for text in INS.get(i, []):
            out.append(new_para(text, sample=raw))
            stats["INS"] += 1

    out.append(resto)
    newbody = "".join(out)
    newxml = head + newbody + tail
    assert newxml.count("<w:sectPr") == xml.count("<w:sectPr"), "se perdió un sectPr"

    DST.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(DST, "w") as zo:
        for it in src.infolist():
            data = newxml.encode("utf8") if it.filename == "word/document.xml" else src.read(it.filename)
            zo.writestr(it, data, compress_type=zipfile.ZIP_DEFLATED)

    print("editados:", stats["E"], "| títulos:", stats["H"], "| borrados:", stats["D"],
          "| intactos:", stats["K"], "| nuevos:", stats["INS"], "| tablas tocadas:", stats["TBL"])
    print("w:ins:", newxml.count("<w:ins "), " w:del:", newxml.count("<w:del "),
          " sectPr:", newxml.count("<w:sectPr"), " tbl:", newxml.count("<w:tbl>"),
          " drawing:", newxml.count("<w:drawing"),
          " commentRangeStart:", newxml.count("commentRangeStart"))
    print("salida:", DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
