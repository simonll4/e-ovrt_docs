#!/usr/bin/env python3
"""§17.5 v1.3 → v1.4: pase de consolidación de la Etapa 5, como CAMBIOS CONTROLADOS
(w:ins / w:del sin aceptar, autor Claude).

Decisiones aplicadas (`desarrollando/analisis-17-4-17-5-etapas-4-5.md` §8, firmadas por el
usuario el 2026-09-04):
  D-H  §17.5.8 se borra (comentario del usuario) y las ocho limitaciones cierran §17.5.7
  D-I  La Tabla 65 (dos filas) pasa a prosa
  D-J  La prosa cita las figuras producidas; el pegado es del usuario
  D-K  El presupuesto de latencia se cita desde §17.1.7 en vez de repetir una cifra propia
  D-L  La familia de modelos descartada se nombra, como en §17.4
  D-M  Los comentarios quedan abiertos con su ancla (el único se re-ancla al texto que lo absorbe)
  D-N  Notación unificada: mAP50/AP50, «cuadros con persona», «en dominio», bare_head una vez
  AJ-5.14  Entra el costo medido del vocabulario activo (§17.5.4) y su no-ejecución (§17.5.7)

Reparaciones de hecho, no de estilo:
  · Tabla 66, fila «CR-02 en vivo»: se restaura la celda vacía de la exportación del 08-27.
  · Los denominadores de la latencia de alerta bajan a la tabla y su párrafo desaparece.

Renumeración de tablas: 62→61, 63→62, 64→63, 66→64, 67→65 (la 65 pasa a prosa). §17.4 cierra
en la Tabla 60, de modo que el capítulo queda contiguo.

Reglas de oficio heredadas de los pases de las Etapas 2 y 3:
  · el `w:sectPr` final del cuerpo no pertenece a ningún párrafo y viaja en el «resto»;
  · las marcas autocerradas se quitan antes que las emparejadas al calcular vistas;
  · los comentarios conservan sus anclas salvo re-anclaje explícito;
  · autocontención: ningún código interno, ADR, ruta ni ficha entra al texto.
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
SRC = BASE / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.3.docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.4 (sugerencias sin aceptar).docx"

AUTHOR = "Claude"
DATE = "2026-09-04T12:00:00Z"

RPR = '<w:rPr><w:rtl w:val="0"/></w:rPr>'
RPR_B = '<w:rPr><w:b w:val="1"/><w:bCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'
RPR_I = '<w:rPr><w:i w:val="1"/><w:iCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'
RPR_M = ('<w:rPr><w:rFonts w:ascii="Courier New" w:cs="Courier New" w:eastAsia="Courier New"'
         ' w:hAnsi="Courier New"/><w:sz w:val="21"/><w:szCs w:val="21"/><w:rtl w:val="0"/></w:rPr>')

_ID = [7000]


def nid() -> int:
    _ID[0] += 1
    return _ID[0]


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _tokens(text: str):
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
    runs = []
    for rpr, frag in _tokens(text):
        if rpr is RPR and base_rpr is not RPR:
            rpr = base_rpr
        runs.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(frag)}</w:t></w:r>')
    return f'<w:ins w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}">' + "".join(runs) + "</w:ins>"


RUN_RE = re.compile(r"<w:r\b(?![a-zA-Z])[^>]*>.*?</w:r>", re.S)


def _has_text(run: str) -> bool:
    return "<w:t" in run


def _to_del(run: str) -> str:
    d = (run.replace("<w:t>", "<w:delText>").replace("<w:t ", "<w:delText ")
            .replace("</w:t>", "</w:delText>"))
    return f'<w:del w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}">{d}</w:del>'


def del_all_runs(xml: str, incluir_figuras: bool = False) -> str:
    def repl(m):
        r = m.group(0)
        if _has_text(r) or (incluir_figuras and "<w:drawing" in r):
            return _to_del(r)
        return r
    return RUN_RE.sub(repl, xml)


def strip_comment_anchors(p: str, ids) -> str:
    for cid in ids:
        p = re.sub(r"<w:sdt><w:sdtPr>(?:(?!</w:sdt>).)*?"
                   r'<w:commentRangeStart w:id="%d"/>.*?</w:sdt>' % cid, "", p, flags=re.S)
        p = re.sub(r'<w:commentRangeStart w:id="%d"/>' % cid, "", p)
        p = re.sub(r'<w:commentRangeEnd w:id="%d"/>' % cid, "", p)
        p = re.sub(r'<w:r\b(?![a-zA-Z])[^>]*>(?:<w:rPr>.*?</w:rPr>)?'
                   r'<w:commentReference w:id="%d"/></w:r>' % cid, "", p, flags=re.S)
    return p


def mark_para_deleted(p: str) -> str:
    m = re.search(r"<w:pPr>(.*?)</w:pPr>", p, re.S)
    if not m:
        return p
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
    runs = [m for m in RUN_RE.finditer(p) if _has_text(m.group(0))]
    if not runs:
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


def new_para(text: str, sample: str | None = None, base_rpr: str = RPR) -> str:
    tag = f'<w:ins w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
    m = re.search(r"<w:pPr>.*?</w:pPr>", sample or "", re.S)
    ppr = m.group(0) if m else "<w:pPr><w:rPr/></w:pPr>"
    ppr = re.sub(r"<w:sectPr>.*?</w:sectPr>", "", ppr, flags=re.S)
    ppr = re.sub(r"<w:pStyle w:val=\"Heading\d\"/>", "", ppr)
    if "<w:rPr/>" in ppr:
        ppr = ppr.replace("<w:rPr/>", f"<w:rPr>{tag}</w:rPr>", 1)
    elif "<w:rPr>" in ppr:
        ppr = ppr.replace("<w:rPr>", f"<w:rPr>{tag}", 1)
    else:
        ppr = ppr.replace("</w:pPr>", f"<w:rPr>{tag}</w:rPr></w:pPr>", 1)
    return f"<w:p>{ppr}{ins_runs(text, base_rpr)}</w:p>"


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
    return units, body[i:]


TR_RE = re.compile(r"<w:tr\b[^>]*>.*?</w:tr>", re.S)
TC_RE = re.compile(r"<w:tc\b[^>]*>.*?</w:tc>", re.S)


def del_row(tr: str) -> str:
    tag = f'<w:del w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
    if "<w:trPr>" in tr:
        tr = tr.replace("<w:trPr>", f"<w:trPr>{tag}", 1)
    else:
        tr = re.sub(r"(<w:tr\b[^>]*>)", r"\1<w:trPr>" + tag + "</w:trPr>", tr, count=1)
    tr = del_all_runs(tr)
    return re.sub(r"<w:p\b[^>]*>.*?</w:p>", lambda m: mark_para_deleted(m.group(0)), tr, flags=re.S)


def edit_cell(tbl: str, row: int, col: int, text: str) -> str:
    rows = list(TR_RE.finditer(tbl))
    tr = rows[row].group(0)
    cells = list(TC_RE.finditer(tr))
    tc = cells[col].group(0)
    paras = list(re.finditer(r"<w:p\b[^>]*>.*?</w:p>", tc, re.S))
    first = paras[0].group(0)
    newfirst = edit_para(first, text)
    newtc = tc[:paras[0].start()] + newfirst + tc[paras[0].end():]
    if len(paras) > 1:
        cut = newtc.index(newfirst) + len(newfirst)
        newtc = newtc[:cut] + re.sub(r"<w:p\b[^>]*>.*?</w:p>",
                                     lambda m: delete_para(m.group(0)), newtc[cut:], flags=re.S)
    newtr = tr[:cells[col].start()] + newtc + tr[cells[col].end():]
    return tbl[:rows[row].start()] + newtr + tbl[rows[row].end():]


def del_table(tbl: str) -> str:
    out, last = [], 0
    for m in TR_RE.finditer(tbl):
        out.append(tbl[last:m.start()])
        out.append(del_row(m.group(0)))
        last = m.end()
    out.append(tbl[last:])
    return "".join(out)


# =============================================================================== TEXTO DEL PASE
#   ("E", texto)  reemplaza el contenido      ("D",)  borra el párrafo
E = {}

# ------------------------------------------------- 17.5.1 Encuadre y reglas de lectura
E[2] = ("E",
        "La evaluación informa cuánto produjo el prototipo bajo las condiciones experimentales "
        "definidas. Los resultados se organizan por pregunta de medición y distinguen tres niveles. "
        "La percepción sobre imágenes caracteriza al detector, el estado observable por persona "
        "evalúa la reconstrucción de una condición por sujeto, y la alerta temporal por episodio "
        "representa a la plataforma completa. La sección 17.4 documentó qué componentes se "
        "construyeron y cómo se verificaron. Acá se reportan sus mediciones, y la interpretación de "
        "conjunto corresponde a las conclusiones.")

E[3] = ("E",
        "Rigen las reglas de lectura fijadas en la sección 17.1.7.3. Cada cifra se acompaña de la "
        "combinación que la produjo, del material o estrato sobre el que se calculó y de su "
        "denominador. Precisión, recall y F1 se calcularon sólo sobre casos positivos con referencia "
        "aplicable, los materiales negativos se analizaron por conteo de falsos positivos, las "
        "re-alertas se contabilizaron aparte y los percentiles de tramos con relojes distintos no se "
        "sumaron.")

# ------------------------------------------------------- 17.5.2 Percepción sobre imágenes
E[7] = ("E",
        "La primera pregunta examinó la capacidad perceptiva de las combinaciones sobre un banco "
        "congelado de 6.477 imágenes y 55.165 anotaciones. El material se dividió en tres estratos "
        "independientes de 147, 1.330 y 5.000 imágenes, correspondientes a obra curada, a obra con "
        "mayor cobertura de chaleco y a una fuente con clase nativa de cabeza descubierta. El tercero "
        "aportó el 77 % del banco, de modo que el agregado se leyó siempre junto con el desglose por "
        "estrato.")

E[8] = ("E",
        "La Tabla 61 muestra que la combinación gdino-tiny-560 alcanzó el mAP50 más alto en el "
        "agregado y en el núcleo curado, mientras que gdino-base-560 produjo el recall más alto para "
        "CR-01. El veredicto se formuló entonces por combinación. El primer perfil se retuvo como "
        "configuración operativa por un criterio fijado antes de leer los resultados, y el segundo "
        "como contraste especializado para cabeza descubierta y chaleco. No se estableció una "
        "jerarquía universal entre modelos.")

E[9] = ("E", "**Tabla 61**")

E[13] = ("E",
         "La especialización del perfil base también apareció en chaleco, con AP 0,582 frente a 0,520 "
         "del perfil operativo sobre el estrato de mayor cobertura de esa clase. En los tres estratos, "
         "persona y casco se mantuvieron entre 0,70 y 0,89 de AP, mientras que chaleco quedó entre "
         "0,55 y 0,58. La asimetría no dependió de una única fuente, porque se sostuvo en los tres.")

E[14] = ("E",
         "La familia YOLOE presentó una limitación distinta. Sus cuatro variantes produjeron AP 0,000 "
         "para bare_head, la clase de cabeza descubierta, en el estrato que la anota de forma nativa. "
         "Aunque resultó adecuada para rutas de mayor velocidad, esa ceguera la volvió inservible para "
         "CR-01 en la configuración evaluada.")

E[15] = ("E",
         "La extensibilidad semántica se ejerció sobre una clase nueva, cuyo costo de incorporación "
         "informa la sección 17.4.8. Sin ninguna corrida de entrenamiento alcanzó AP50 de 0,662 sobre "
         "99 cajas de referencia. El costo reducido no eliminó la necesidad de validación semántica. "
         "Sobre el mismo material, un sinónimo produjo 0 detecciones y otra palabra generó 252 cajas, "
         "ninguna correcta.")

# ---------------------------------------------------------------- 17.5.3 Estado por persona
E[17] = ("E",
         "El nivel intermedio evaluó si la evidencia perceptiva permitía determinar el estado "
         "observable de cada persona. La calibración se realizó sobre una mitad del material y las "
         "métricas sobre la otra, con IoU mayor o igual que 0,5. Se compararon E-IND, la estrategia "
         "indirecta que reconstruye la ausencia desde evidencia positiva, y E-DIR, la formulación "
         "directa retenida para el contraste. La Tabla 62 reúne los resultados.")

E[18] = ("E", "**Tabla 62**")

E[23] = ("E",
         "La medición sobre 17 clips de obra real mostró un cambio de régimen. La caída del F1 provino "
         "de la precisión y no del recall, por acumulación de falsos positivos sobre personas cuyo "
         "estado no podía determinarse visualmente. El evaluador excluyó del denominador 1.414 cuadros "
         "con persona no juzgables para CR-01 y 1.409 para CR-02, y contabilizó como falso positivo "
         "cualquier predicción emitida sobre ellos.")

# ------------------------------------- 17.5.4 Alerta por episodio contra la referencia humana
E[25] = ("E",
         "La alerta por episodio constituyó el resultado principal porque integra percepción, "
         "asociación, histéresis, estado temporal y registro de alerta. El bloque de rodaje guionado "
         "reunió 34 clips y 35 episodios de referencia, 28 de CR-01 y 7 de CR-02. Treinta y cuatro "
         "episodios resultaron evaluables y uno quedó censurado con causa, y cuatro clips fueron "
         "negativos. La Tabla 63 reúne las combinaciones ejecutadas sobre ese mismo material, cada una "
         "con una sola variable cambiada respecto de la línea de base.")

E[26] = ("E", "**Tabla 63**")

E[29] = ("E",
         "*Nota.* Las métricas temporales se calcularon sobre 34 episodios evaluables de 35 en el "
         "bloque de rodaje, y la columna de latencia declara cuántos episodios confirmados sostienen "
         "cada valor. Los falsos positivos se cuentan sobre los cuatro clips negativos y no incluyen "
         "re-alertas.")

E[30] = ("D",)   # los denominadores bajan a la Tabla 63

E[31] = ("E",
         "La histéresis rescató evidencia intermitente. CR-02 confirmó sus 7 episodios, con recall "
         "1,000 y SDR 0,281, aunque requirió una latencia de alerta de 8.572 ms frente a 4.314 ms para "
         "CR-01, medida sobre 23 episodios confirmados. La diferencia fue coherente con ventanas de "
         "confirmación de 7,0 y 4,0 s. Una detección sostenida sólo durante una fracción del episodio "
         "pudo producir una alerta correcta si acumuló evidencia suficiente dentro de la ventana.")

E[32] = ("E",
         "La identidad temporal fue la capa con mayor aporte medido dentro del banco. Con las mismas "
         "detecciones, la granularidad por sujeto elevó el F1 de 0,789 a 0,930, una diferencia de "
         "0,141 sobre los 34 episodios evaluables. En el escenario de mayor dificultad el resultado "
         "pasó de 0,400 a 1,000, es decir de dos episodios confirmados sobre cinco a los cinco. La "
         "mejora no provino del detector, sino de evitar que la evidencia de personas distintas se "
         "mezclara dentro de un mismo estado de escena.")

E[33] = ("E",
         "El estrato de obra real no guionada se informó por separado y comprendió 13 clips. Una "
         "revisión ciega encontró que 5 de las 7 declaraciones de episodio eran errores de anotación "
         "por sobre-declarar estados que no resultaban observables, y dejó 2 episodios evaluables y 11 "
         "clips negativos. Ese denominador impidió ordenar granularidades. El resultado robusto del "
         "estrato fue la asimetría de falsos positivos, 26 con granularidad de escena frente a 323 con "
         "granularidad por sujeto sobre los mismos 11 clips negativos.")

E[34] = ("D",)   # rótulo de la Tabla 65
E[35] = ("D",)   # título de la Tabla 65
E[37] = ("D",)   # nota de la Tabla 65

E[38] = ("E",
         "Sobre el único tramo continuo de cumplimiento, de 6 minutos y 9,6 segundos, los conteos "
         "fueron 3 falsos positivos con granularidad de escena y 190 con granularidad por sujeto. Las "
         "tasas de 29,2 y 1.850,8 falsas alarmas por hora se derivan de esa exposición de 0,1027 h y "
         "se informan como magnitudes derivadas, nunca como cota operativa, porque la exposición "
         "disponible estuvo dos órdenes de magnitud por debajo de la necesaria para sostener una.")

# --------------------------------------------------------------------------- 17.5.5 Tiempo real
E[40] = ("E",
         "La evaluación en vivo examinó qué parte del resultado temporal sobrevivía cuando la densidad "
         "de procesamiento descendía respecto de la evidencia disponible. El banco se representó a 30 "
         "fps, mientras que el camino en vivo entregó entre 1,16 y 4,42 fps en cuatro densidades "
         "medidas sobre los 34 clips del bloque de rodaje, remuestreados de manera pareada. La Tabla "
         "64 reúne esas mediciones junto con las de integridad y latencia por tramo.")

E[41] = ("E", "**Tabla 64**")

E[45] = ("E",
         "La cobertura del episodio no se comparó entre cadencias porque depende de cuántas unidades "
         "sobreviven al muestreo. Tampoco se comparó la latencia agregada entre densidades sin "
         "controlar la supervivencia, porque los episodios que no alcanzan a confirmar desaparecen del "
         "promedio y lo sesgan. Entre los episodios supervivientes, el costo de bajar la densidad fue "
         "de 0,7 a 1,3 s sobre ventanas de 4 a 7 s, medido sobre 21, 20 y 16 episodios comunes a las "
         "cadencias comparadas.")

E[46] = ("E",
         "La medición confirmó además la separación entre captura, procesamiento y distribución. Los "
         "tres tramos corresponden a relojes distintos y por eso sus percentiles no se suman. El del "
         "tramo de distribución describe el intervalo desde el bus de alertas hasta la confirmación "
         "del canal, y no la latencia completa de la plataforma.")

# ----------------------------------------------------- 17.5.6 Caminos probados y no adoptados
E[48] = ("E",
         "Los caminos no adoptados se evaluaron contra criterios fijados antes de leer sus resultados. "
         "La estrategia directa quedó descartada por un veto de precisión, cuyo umbral de 0,5 se fijó "
         "de antemano y quedó muy por encima del valor obtenido. La brecha que ya mostraba en el "
         "estado por persona se amplió al atravesar el motor temporal.")

E[49] = ("E",
         "La fusión híbrida por disyunción fue ejecutada y refutada, porque el recall descendió "
         "respecto del núcleo indirecto en lugar de crecer. La unión de evidencia no resultó monótona "
         "dentro del motor temporal, ya que las detecciones más tempranas desplazaron confirmaciones "
         "fuera de la ventana de referencia. La variante por conjunción no se ejecutó, porque no podía "
         "medirse contra el banco sin romper la comparabilidad de las seis combinaciones. La familia "
         "MM-Grounding DINO se integró por el mismo mecanismo de adaptación, se evaluó y se archivó "
         "durante la selección, sin incorporarse al perfil operativo.")

E[50] = ("E",
         "La rama comparativa de ajuste fino se cerró como una curva de capacidad, con criterios y "
         "expectativas registrados antes de cada evaluación, y sus cifras se mantuvieron separadas de "
         "las del núcleo sin entrenamiento. La Tabla 65 recorre sus tres puntos.")

E[51] = ("E", "**Tabla 65**")

E[54] = ("E",
         "*Nota.* Los puntos medidos pertenecen a una rama comparativa separada. Las métricas en "
         "dominio de la línea base y de los dos tramos entrenados se calcularon sobre el banco "
         "congelado de 6.477 imágenes. El primer tramo agregó principalmente recall y el segundo, AP, "
         "de modo que no existe una combinación ajustada universalmente superior.")

E[55] = ("E",
         "El segundo tramo duplicó el AP50 de cabeza descubierta respecto del primero, pero colapsó "
         "durante el entrenamiento y falló las dos retenciones. El patrón conjunto mostró que el "
         "límite no fue capacidad de cómputo sino estructura experimental, con 2.946 imágenes de "
         "ajuste frente a 10,35 millones de parámetros. Ningún checkpoint se adoptó como modelo de "
         "servicio, y los veredictos negativos se conservaron como resultados pre-registrados y no "
         "como trabajo pendiente.")

# ------------------------------------- 17.5.7 Lo no ejecutado y lo no implementado
E[58] = ("E",
         "Las métricas formales de seguimiento multiobjeto tampoco se calcularon, porque faltó una "
         "referencia de identidad apta para ese propósito. La exclusión no alcanzó a la capacidad de "
         "identidad temporal, que sí fue implementada y medida por su efecto sobre la alerta. La "
         "ganancia informada más arriba y su persistencia en las cuatro densidades pertenecen a esa "
         "capacidad y no a una métrica de seguimiento.")

E[59] = ("E",
         "La preselección liviana en el dispositivo de captura fue implementada para la fuente propia "
         "y caracterizada mediante una comparación pareada. Descartó el 87 % de las unidades antes de "
         "abandonar el dispositivo, 206 de las 236 que vio la compuerta, frente a las 277 que procesó "
         "la rama sin preselección, y permaneció deshabilitada en todas las corridas evaluativas. La "
         "exclusión fue deliberada, porque un filtro de cuadros sin persona habría suprimido la "
         "evidencia sostenida que la medición de falsas alarmas debía observar y habría superpuesto el "
         "error de un detector auxiliar sobre la cadena evaluada.")

# ------------------------------------------------------- 17.5.8 Síntesis — se elimina (D-H)
E[62] = ("D",)
E[63] = ("D",)
E[64] = ("D",)
E[65] = ("D",)

# ------------------------------------------------------------------ párrafos nuevos (INSERTS)
# unidad → lista de (texto[, id de comentario a re-anclar])
INS = {
    32: [("El vocabulario activo también se comportó como una variable experimental. Sobre la "
          "combinación de contraste base-560, un ensayo posterior mantuvo fijos el modelo, el "
          "evaluador, el conjunto de patrones, la referencia y los tiempos, y sumó al vocabulario una "
          "sola palabra, la de cabeza descubierta. El F1 por episodio bajó de 0,704 a 0,622, el recall "
          "de 0,735 a 0,676 y la precisión de 0,676 a 0,575. La interacción entre términos de un mismo "
          "vocabulario no resultó despreciable, de modo que dos configuraciones sólo son comparables "
          "cuando declaran el vocabulario completo que vieron.",)],
    61: [("El sub-experimento formal que evaluaba cada prompt en aislamiento y dentro del vocabulario "
          "completo no se ejecutó sobre las combinaciones finalistas. La pregunta que lo motivaba "
          "quedó respondida por el contraste de variable única informado más arriba, que midió el "
          "costo de sumar un término al vocabulario activo.",),
         ("Ocho limitaciones acotan la lectura de todo lo anterior. La tasa de falsas alarmas por hora "
          "no sostiene una cota operativa. La referencia temporal no tuvo doble anotación ni medida de "
          "acuerdo entre anotadores, y los bordes de episodio se adjudicaron por criterio único en "
          "seis clips. El material guionado proviene de un solo bloque de rodaje, y la medición sobre "
          "obra real precisó esa limitación sin levantarla, porque caracteriza por mecanismo dónde el "
          "sistema deja de ser evaluable en lugar de validarlo sobre obra real. Los escenarios "
          "quedaron desbalanceados, de modo que todo resultado se reporta por estrato además del "
          "agregado. El seguimiento no se midió en obra real con multitud. Una de las fuentes de "
          "imágenes conserva licencia parcial. Y la condición de chaleco no quedó cerrada al nivel del "
          "estado por persona.", 0)],
}

# --------------------------------------------------------------------------- operaciones de tabla
TBL = {
    20: [("cell", 4, 3, "n+ = 92 de 10.356 cuadros con persona"),
         ("cell", 5, 3, "n+ = 170 de 10.361 cuadros con persona")],
    28: [("cell", 0, 4, "t_alert en ms (n de episodios confirmados)"),
         ("cell", 1, 4, "5.327 (n = 28)"),
         ("cell", 2, 4, "4.899 (n = 25)"),
         ("cell", 3, 4, "6.611 (n = 6)"),
         ("cell", 4, 4, "6.956 (n = 12)"),
         ("cell", 5, 4, "5.236 (n = 33)"),
         ("cell", 6, 4, "3.919 (n = 13)")],
    36: [("delall",)],                                    # Tabla 65 → prosa (D-I)
    43: [("cell", 9, 2, "3 alertas: ≥ 7,1 s"),            # celda perdida en la exportación 08-27
         ("cell", 5, 4, "Dentro del presupuesto declarado en la sección 17.1.7.")],
}

REANCLA = {0: None}   # el comentario 0 se re-ancla a un párrafo insertado


def wrap_comment(p: str, cid: int) -> str:
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
    st = {"E": 0, "D": 0, "K": 0, "INS": 0, "TBL": 0}
    for i, (kind, raw, gap) in enumerate(units):
        out.append(gap)
        if kind == "tbl":
            if i in TBL:
                t = raw
                for op in TBL[i]:
                    if op[0] == "cell":
                        t = edit_cell(t, op[1], op[2], op[3])
                    elif op[0] == "delall":
                        t = del_table(t)
                st["TBL"] += 1
                out.append(t)
            else:
                out.append(raw)
            continue

        op = E.get(i)
        if op is None:
            out.append(raw)
            st["K"] += 1
        elif op[0] == "D":
            p = raw
            quitar = [cid for cid in REANCLA
                      if f'<w:commentRangeStart w:id="{cid}"/>' in raw]
            if quitar:
                p = strip_comment_anchors(p, quitar)
            out.append(delete_para(p))
            st["D"] += 1
        else:
            rpr = op[2] if len(op) > 2 else RPR
            out.append(edit_para(raw, op[1], rpr))
            st["E"] += 1

        for entry in INS.get(i, []):
            p = new_para(entry[0], sample=raw)
            if len(entry) > 1:
                p = wrap_comment(p, entry[1])
            out.append(p)
            st["INS"] += 1

    out.append(resto)
    newxml = head + "".join(out) + tail
    assert newxml.count("<w:sectPr") == xml.count("<w:sectPr"), "se perdió un sectPr"
    assert newxml.count("commentRangeStart") == xml.count("commentRangeStart"), "comentario perdido"

    with zipfile.ZipFile(DST, "w") as zo:
        for it in src.infolist():
            data = newxml.encode("utf8") if it.filename == "word/document.xml" else src.read(it.filename)
            zo.writestr(it, data, compress_type=zipfile.ZIP_DEFLATED)

    print("editados:", st["E"], "| borrados:", st["D"], "| intactos:", st["K"],
          "| nuevos:", st["INS"], "| tablas tocadas:", st["TBL"])
    print("w:ins:", newxml.count("<w:ins "), " w:del:", newxml.count("<w:del "),
          " sectPr:", newxml.count("<w:sectPr"), " tbl:", newxml.count("<w:tbl>"),
          " commentRangeStart:", newxml.count("commentRangeStart"))
    print("salida:", DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
