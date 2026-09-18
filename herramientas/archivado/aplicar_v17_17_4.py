#!/usr/bin/env python3
"""§17.4 v1.6 → v1.7: pase de consolidación de la Etapa 4, como CAMBIOS CONTROLADOS
(w:ins / w:del sin aceptar, autor Claude).

Decisiones aplicadas (`desarrollando/analisis-17-4-17-5-etapas-4-5.md` §8, firmadas por el
usuario el 2026-09-04):
  D-A  Opción A: 11 → 8 secciones de nivel 3, cero títulos de nivel 4, renumeración interna
  D-B  Los cuatro títulos de nivel 4 de la construcción del banco pasan a entradillas en negrita
  D-C  La Tabla 60 pasa a prosa ordenada por estatuto (comentario 6 del usuario)
  D-D  La evolución aditiva del contrato vive sólo en extensibilidad
  D-E  La cifra de pruebas se fecha contra su verificación en vez de actualizarse
  D-F  La nota de la figura enuncia el orden real; el reemplazo de la imagen es del usuario
  D-G  El esfuerzo de anotación se afirma por lo revisado, sin inventar horas
  D-M  Los comentarios quedan abiertos; los seis cuyo párrafo desaparece se re-anclan

Handoffs que este pase aterriza:
  H2-01  Orden de arranque real, control → distribución → medios, con la garantía del publicador
  H2-02  Las 2.946 imágenes de ajuste y su causa, el cumplimiento de la regla de partición
  E4-31  Detalle operativo del ledger que salió de §17.3

Renumeración de tablas: 56–59 se conservan, la 60 pasa a prosa y la 61 se vuelve 60.
La figura 4.7 pasa a 4.5, contigua con las cuatro de §17.3.

Reglas de oficio heredadas de los pases de las Etapas 2 y 3:
  · el `w:sectPr` final del cuerpo no pertenece a ningún párrafo y viaja en el «resto»;
  · un párrafo borrado que contiene una imagen deja la imagen viva si sólo se marcan los runs;
  · los comentarios conservan sus anclas salvo re-anclaje explícito;
  · autocontención: ningún código interno, ADR, ruta ni ficha entra al texto.
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
SRC = BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.6.docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.7 (sugerencias sin aceptar).docx"

AUTHOR = "Claude"
DATE = "2026-09-04T12:00:00Z"

RPR = '<w:rPr><w:rtl w:val="0"/></w:rPr>'
RPR_B = '<w:rPr><w:b w:val="1"/><w:bCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'
RPR_I = '<w:rPr><w:i w:val="1"/><w:iCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'

_ID = [8000]


def nid() -> int:
    _ID[0] += 1
    return _ID[0]


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _tokens(text: str):
    out = []
    pat = re.compile(r"\*\*([^*]+)\*\*|\*([^*]+)\*")
    pos = 0
    for m in pat.finditer(text):
        if m.start() > pos:
            out.append((RPR, text[pos:m.start()]))
        if m.group(1) is not None:
            out.append((RPR_B, m.group(1)))
        else:
            out.append((RPR_I, m.group(2)))
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


def edit_para(p: str, text: str, base_rpr: str = RPR) -> str:
    runs = [m for m in RUN_RE.finditer(p) if _has_text(m.group(0))]
    if not runs:
        return p.replace("</w:p>", ins_runs(text, base_rpr) + "</w:p>", 1)
    out, last = [], 0
    for k, m in enumerate(runs):
        out.append(p[last:m.start()])
        out.append(_to_del(m.group(0)))
        if k == len(runs) - 1:
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
    ppr = re.sub(r'<w:pStyle w:val="Heading\d"/>', "", ppr)
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
#   ("H", texto)  título     ("E", texto)  reemplaza contenido     ("D",)  borra el párrafo
E = {}

# ------------------------------------------------------------------------- entrada del capítulo
E[1] = ("E",
        "La implementación materializa el diseño arquitectónico de la sección 17.3 en componentes "
        "construidos, contratos e interfaces concretados, mecanismos de acople y persistencia, y "
        "evidencia de verificación del funcionamiento técnico del prototipo. Los resultados de "
        "desempeño se presentan en "
        "la sección 17.5, de modo que la existencia de una capacidad no se confunda con su "
        "rendimiento cuantitativo.")
E[2] = ("D",)

# --------------------------------------------- 17.4.1 Componentes construidos y cadena de datos
E[4] = ("E",
        "El prototipo se materializó en tres componentes de plataforma, un módulo funcional de "
        "distribución y una cadena de datos externa a la plataforma que produce los insumos "
        "experimentales. La Figura 4.5 muestra esa organización con sus dos patrones de acople.")

E[5] = ("E",
        "El plano de medios implementa la cadena de inferencia de vocabulario abierto, desde la "
        "ingesta hasta la publicación de evidencia perceptiva normalizada. El plano de control "
        "implementa el motor de patrones de riesgo, que consume esa evidencia, mantiene estado "
        "temporal y registra alertas internas. El soporte experimental no es un plano de ejecución. "
        "Reúne los catálogos de prompts y de experimentos, el orquestador reproducible de corridas, la "
        "consolidación de artefactos y la consola de inspección con su servicio intermediario.")

E[6] = ("E",
        "El módulo de distribución de alertas es el cuarto componente funcional. Consume las alertas "
        "confirmadas desde el bus de alertas, aplica la política de notificación, controla idempotencia "
        "y supresión, entrega por MQTT con confirmación de calidad de servicio y conserva un ledger de "
        "entregas de sólo adición. Su vista de resultados y su lanzamiento desde la orquestación "
        "quedaron integrados a la consola.")

E[7] = ("E",
        "La cadena de datos comprende adquisición, validación, conversión y congelamiento de datasets "
        "y bancos de evaluación, y la sección 17.4.6 documenta cómo se construyó la del banco temporal "
        "de video. Alimenta a la plataforma pero no forma parte de su cadena operativa, porque su "
        "función es producir material reproducible y con procedencia para entrenamiento, selección y "
        "evaluación.")

E[8] = ("E", "**Figura 4.5**")

E[11] = ("E",
         "*Nota.* La figura representa la materialización efectiva de los dos patrones de acople. El "
         "gobierno de las corridas ocurre por interfaces HTTP en el plano de medios, el plano de "
         "control y el módulo de distribución, con el orquestador y la consola como clientes de los "
         "tres. El flujo de datos se desacopla mediante buses ZeroMQ de patrón publicador-suscriptor "
         "con serialización msgpack, uno para los eventos de percepción entre medios y control y otro "
         "para las alertas confirmadas entre control y distribución. El repositorio por ejecución "
         "experimental conserva los artefactos persistentes de cada corrida.")

# ------------------------------------ 17.4.2 Correspondencia y contratos materializados (fusión)
E[12] = ("H", "17.4.2. Correspondencia y contratos materializados")

E[13] = ("E",
         "Los contratos mínimos definidos durante el diseño se materializaron como modelos de datos, "
         "configuraciones versionadas, esquemas serializables, servicios ejecutables y artefactos "
         "persistentes. La Tabla 56 establece la correspondencia entre cada denominación conceptual y "
         "su realización efectiva.")

E[18] = ("E",
         "La correspondencia permite verificar que la implementación no sustituyó silenciosamente las "
         "fronteras del diseño, y que cada componente conservó la responsabilidad que la arquitectura "
         "le asignó.")

E[19] = ("D",)   # el título de la vieja 17.4.3 desaparece con la fusión

E[20] = ("E",
         "Cinco de esos contratos concentran los hechos principales de la ejecución, y son el evento de "
         "percepción, el envoltorio del bus, el contrato de ciclo de vida, el evento de transición de "
         "patrón y la alerta interna. La tabla anterior los declara con su identificador de esquema.")

E[21] = ("E",
         "Cada contrato es una clase de modelo declarada en el módulo de contratos de su componente, "
         "con tipos y campos obligatorios explícitos, validada en la frontera de entrada y persistida "
         "como un objeto JSON por línea, omitiendo los campos sin valor. Dentro del plano de medios la "
         "evidencia atraviesa además una cadena interna de contratos antes de publicarse. La unidad "
         "visual normaliza la lectura de la fuente, y la unidad preparada transporta los píxeles junto "
         "con la transformación espacial que devuelve del espacio del modelo al de la imagen original. "
         "La detección cruda recoge la salida del adaptador y la detección normalizada es la que se "
         "persiste. Esa cadena hace de la reproyección de coordenadas una operación declarada.")

E[22] = ("E",
         "El evento de percepción normaliza la salida del detector. Identifica la corrida y la unidad "
         "visual, y agrupa en bloques estructurados la fuente, el perfil de modelo, el conjunto de "
         "prompts efectivo, las detecciones y los tiempos medidos por unidad. Cada detección lleva su "
         "etiqueta, el identificador del prompt que la originó, el puntaje, la caja en píxeles y su "
         "equivalente normalizado. Esa composición permite que una detección se atribuya después a una "
         "variable concreta de la corrida y no a una combinación desconocida. La forma efectiva del "
         "evento, tal como se persiste, es la siguiente.")

E[24] = ("E",
         "El envoltorio del bus no reempaqueta ese contenido. Transporta como carga la misma cadena "
         "que ya se escribió en el artefacto y le agrega cuatro campos propios del transporte, que son "
         "el tópico, la clave de particionado, un número de secuencia monótono por publicador y el "
         "instante de publicación en reloj de pared. El módulo de distribución conserva ese instante "
         "como marca de confirmación. El número de secuencia se consume incluso cuando el envío se "
         "descarta por saturación del canal, de modo que la pérdida se vuelva un hueco observable del "
         "lado del consumidor.")

E[25] = ("E",
         "El evento de transición registra los cambios entre los estados del patrón que fija la máquina "
         "de estados del diseño, junto con la evidencia y los hitos temporales que los motivaron. "
         "Incorpora además el instante y la unidad de la primera evidencia positiva del episodio, que "
         "es el punto de partida de la medición de latencia. Un contrato hermano registra el progreso "
         "parcial mientras la condición está en curso y todavía no fue confirmada.")

E[26] = ("E",
         "La alerta interna registra la confirmación del episodio, y su identificador no es un valor "
         "aleatorio. Se deriva de forma determinista sobre la cadena que concatena el identificador de "
         "corrida de control, el de corrida de medios, la unidad, el patrón y la clave de sujeto, que "
         "incorpora el identificador del sujeto sólo cuando el patrón opera con esa granularidad. La "
         "alerta conserva además el sujeto observado, las detecciones de soporte, la clase de "
         "protección ausente, la región evaluada, el puntaje y una justificación legible.")

E[27] = ("E",
         "Los contratos admiten además información que la implementación actual no produce, y la "
         "sección 17.4.8 informa cómo se ejerció esa capacidad sin romper la compatibilidad.")
E[28] = ("D",)   # el bloque de código migra con la evolución aditiva (D-D)
E[29] = ("D",)

# ------------------------------- 17.4.3 Servicios, gobierno por configuración y acople (fusión)
E[30] = ("H", "17.4.3. Servicios, gobierno por configuración y acople")

E[31] = ("E",
         "Los tres módulos de la cadena se implementaron como servicios independientes, gobernados por "
         "configuración y expuestos mediante HTTP. Cada uno carga su configuración al iniciarse, admite "
         "una corrida activa por vez, rechaza las solicitudes concurrentes señalando la que está en "
         "curso y persiste la configuración efectiva que utilizó. El plano de medios carga además el "
         "modelo una sola vez al arrancar. Rutas, fuentes, umbrales, ventanas temporales y opciones de "
         "instrumentación se declaran en configuración, sin constantes ocultas en el código. La Tabla "
         "57 reúne sus operaciones de gobierno.")

E[35] = ("E",
         "*Nota.* La tabla resume las operaciones de gobierno principales y no es un inventario "
         "exhaustivo. Se omiten los listados, la consulta de la corrida actual, los artefactos por "
         "corrida, las comprobaciones de salud y la limpieza del registro. La detención figura "
         "únicamente donde el servicio la expone.")

E[36] = ("E",
         "El modelo no se transmite en la solicitud de corrida, de modo que comparar perfiles implica "
         "disponer procesos con perfiles distintos en lugar de reconfigurar pesos dentro de una "
         "corrida. La decisión mantiene el costo de carga fuera de la ruta crítica y evita estados "
         "ambiguos del servicio.")

E[37] = ("E",
         "Las operaciones de consulta de configuración y de perfil de modelo permiten verificar antes "
         "de disparar que el servicio cargó lo que el experimento requiere. Sin ellas, una discrepancia "
         "entre lo configurado y lo desplegado sólo se descubriría en los resultados.")

E[38] = ("E",
         "En una corrida en vivo el orquestador inicia primero el plano de control, después el módulo "
         "de distribución y por último el plano de medios. El control arranca primero porque debe "
         "quedar suscripto al canal de detecciones antes de que los medios publiquen, y la distribución "
         "va después porque su corrida se declara contra la corrida de control ya creada. La no "
         "pérdida en el canal de alertas no depende de ese orden sino del publicador, que espera a que "
         "haya un suscriptor antes de emitir. Un consumidor suscripto tarde perdería los eventos ya "
         "publicados sin ningún error observable, y las dos garantías juntas excluyen esa pérdida por "
         "construcción.")

E[39] = ("E",
         "La detención de corridas es cooperativa en los dos servicios que la exponen. La solicitud "
         "marca la corrida y el hilo de ejecución la observa entre unidades, sin cortes abruptos que "
         "dejarían artefactos a medio escribir. El plano de control no expone detención y la asimetría "
         "es deliberada, porque su corrida en vivo se cierra con el evento de finalización que publica "
         "el plano de medios, con el que mantiene una relación uno a uno. El módulo de distribución sí "
         "requiere cancelación propia, porque una corrida de entrega puede quedar a la espera de "
         "alertas y debe poder abortarse sin reiniciar el servicio.")

E[40] = ("D",)   # el título de la vieja 17.4.5 desaparece con la fusión

E[41] = ("E",
         "Sobre esos servicios se materializan los dos caminos experimentales, que describen cómo "
         "circula la evidencia entre los planos según la naturaleza de la ejecución.")

E[42] = ("E",
         "En el camino DBE el acople entre planos se realiza por archivo. El plano de medios persiste "
         "su registro de detecciones y el plano de control lo relee, de modo que el repositorio de "
         "corrida es la fuente de verdad y permite repetir el procesamiento bajo condiciones "
         "controladas. En el camino EBE la evidencia se transmite por el bus dentro del envoltorio "
         "versionado.")

E[43] = ("D",)   # el orden de arranque queda enunciado una sola vez, más arriba

E[44] = ("E",
         "La evidencia se persiste antes de publicarse, y el contenido lógico de la línea persistida y "
         "del mensaje transmitido es el mismo, lo que permite reevaluar una corrida en vivo por el "
         "camino diferido y reproducir sus artefactos. En los experimentos, los tres servicios se "
         "ejecutaron en un mismo equipo con unidad de procesamiento gráfico, el nodo central de "
         "procesamiento que describe la sección 17.1.4.1. Los contratos entre módulos no fijan esa "
         "topología, y la configuración de cada corrida registra la disposición efectiva.")

# ----------------------------------- 17.4.4 Configuración efectiva y catálogo de modelos
E[45] = ("H", "17.4.4. Configuración efectiva y catálogo de modelos")

E[46] = ("E",
         "El conjunto de patrones efectivo del núcleo es cr01_cr02_v2. CR-01, persona sin casco, se "
         "configuró con severidad alta, confirmación a los 4.000 ms y resolución a los 2.000 ms. CR-02, "
         "persona sin chaleco reflectivo, se configuró con severidad media, confirmación a los 7.000 ms "
         "y resolución a los 3.000 ms. Las precondiciones de evidencia exigen confianza mínima de 0,35 "
         "y área mínima de 400 píxeles cuadrados para el sujeto, y confianza mínima de 0,25 para el "
         "elemento de protección. La región de búsqueda se define de forma relativa a la caja del "
         "sujeto. Para CR-01 es la franja superior entre el 0 % y el 45 % de la altura con margen "
         "lateral del 12 %, y para CR-02 la franja del torso entre el 25 % y el 85 % con margen lateral "
         "del 8 %.")

E[47] = ("E",
         "El conjunto opera con granularidad de escena y el motor registra cada confirmación sin "
         "supresión, conforme a la decisión de diseño DA-13. La identidad por sujeto se implementó como "
         "capacidad activable por configuración del plano de control y se trata en la sección 17.4.8.")

E[48] = ("E",
         "El vocabulario activo del núcleo se compone de person como entidad y de helmet y vest como "
         "elementos de protección.")

E[49] = ("E",
         "El catálogo de perfiles de modelo materializa la sustituibilidad prevista en el diseño. Reúne "
         "variantes de Grounding DINO en sus versiones tiny y base, cada una con resolución de entrada "
         "de 800 y de 560 píxeles, y YOLOE en cuatro tamaños, todas integradas mediante adaptadores "
         "sobre el mismo contrato de salida. Una tercera familia, MM-Grounding DINO, se integró por el "
         "mismo mecanismo y se archivó fuera del catálogo activo tras la evaluación, cuyo resultado "
         "informa la sección 17.5.")

E[50] = ("E",
         "El núcleo no fija un modelo único. Cada instancia del servicio de medios carga un perfil al "
         "iniciarse, de modo que comparar perfiles equivale a disponer instancias distintas bajo la "
         "misma configuración de corrida, y el despliegue integral instancia un servicio por perfil del "
         "catálogo. Las campañas temporales y en vivo fijan un perfil por corrida, declarado en el "
         "manifiesto.")

E[51] = ("E",
         "Cada perfil declara sus umbrales y su postproceso en el catálogo. El perfil fijado por "
         "criterio pre-registrado para las corridas en vivo declara umbral de caja de 0,30 y de texto "
         "de 0,25. Su postproceso aplica confianza mínima de 0,25, supresión de solapamientos con IoU "
         "de 0,50 y área mínima de caja de 100 píxeles cuadrados, y el control de ritmo opera con "
         "selección determinista de paso 1 y una cola máxima de ocho unidades.")

# ------------------------------------------ 17.4.5 Artefactos y trazabilidad por corrida
E[52] = ("H", "17.4.5. Artefactos y trazabilidad por corrida")

E[53] = ("E",
         "Cada ejecución produce un repositorio de artefactos de sólo adición. La organización por "
         "componente que reúne la Tabla 58 conserva la evidencia necesaria para reproducir el flujo, "
         "analizar fallas y reconstruir una alerta desde su configuración hasta su salida distribuida.")

E[58] = ("D",)   # repetía las dos primeras filas de la Tabla 58 (comentario 2)

E[60] = ("E",
         "La ejecución experimental consolida así los cuatro componentes bajo una misma clave.")

E[61] = ("E",
         "El manifiesto de corrida registra la versión de código que produjo los artefactos. Junto con "
         "la configuración efectiva, el conjunto de prompts y la procedencia de la fuente, ese dato "
         "permite reconstruir cada alerta hasta el modelo y la revisión de código que intervinieron. El "
         "reporte consolidado declara el estado de aplicabilidad de cada métrica como computada, "
         "aplicable no computada, no aplicable o no interpretable, siempre con una causa explícita.")

# --------------------------- 17.4.6 Banco temporal y referencia humana (sin títulos de nivel 4)
E[62] = ("H", "17.4.6. Banco temporal y referencia humana de evaluación")

E[63] = ("E",
         "La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada "
         "mediante el esquema clip_gt.v2. La primera generación registraba alertas esperadas por sujeto "
         "y fue reemplazada por episodios a nivel de escena y condición, con tiempos en milisegundos y "
         "estados de aplicabilidad por clip. Para la anotación se seleccionó CVAT, una herramienta de "
         "código abierto con soporte de interpolación temporal y exportación estructurada.")

E[64] = ("D",)   # 17.4.8.1

E[65] = ("E",
         "**Adquisición del material.** El banco proviene de dos fuentes con procedencia y grado de "
         "control experimental distintos, y esa diferencia se conserva como atributo de cada clip. La "
         "primera es un rodaje guionado ejecutado con el hardware real de captura del prototipo. Cada "
         "escenario se diseñó en función de una condición de riesgo del núcleo. Un guion segundo a "
         "segundo fija la entrada del sujeto en cumplimiento, el inicio diferido de la infracción y "
         "su persistencia sostenida durante lapsos muy superiores a las ventanas de confirmación. El "
         "guion incluye además escenas negativas y escenas deliberadamente por debajo de ese umbral. "
         "Las tomas se registraron con margen temporal adicional respecto del clip previsto, y tanto la "
         "grabación como el recorte se hicieron desde la propia consola del prototipo.")

E[67] = ("D",)   # 17.4.8.2

E[68] = ("E",
         "**Segmentación temporal.** Los videos maestros se conservaron sin modificación y las unidades "
         "de evaluación se generaron como clips derivados, con criterios temporales fijados antes de "
         "ejecutar las campañas y aplicados como reglas ejecutables. Cada clip del rodaje se recortó "
         "con un preludio fijo de 3,5 s antes del inicio de la condición, porque un episodio que "
         "arranca en el primer fotograma impide medir el tiempo hasta la primera detección. Lleva "
         "además una cola posterior al cierre del episodio de entre 3 y 10 s según el escenario, y un "
         "piso de duración que garantiza que una alerta válida pero lenta ocurra dentro del clip.")

E[69] = ("D",)   # 17.4.8.3

E[70] = ("E",
         "**Preanotación y revisión humana.** La anotación no partió de video crudo. Cada clip se "
         "preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad que el "
         "modelo evaluado, elección deliberada para evitar circularidad entre el sistema medido y su "
         "referencia. Ese detector se acopló a un algoritmo de seguimiento que propone trayectorias por "
         "sujeto, con los atributos de protección inicializados por asociación espacial.")

E[71] = ("D",)   # 17.4.8.4

E[72] = ("E",
         "**Derivación y congelamiento.** La salida de la anotación se procesa mediante una cadena "
         "reproducible de separación, derivación, validación, promoción y agregación. La cadena valida "
         "la estructura de cada exportación antes de derivar. La derivación clasifica los episodios "
         "con las mismas ventanas de confirmación que utiliza el motor de patrones, de modo que la "
         "referencia y el sistema evaluado apliquen un criterio temporal idéntico. Una divergencia "
         "entre ambos produciría omisiones ficticias. Las correcciones humanas posteriores "
         "se aplican como registros firmados sobre los artefactos versionados, nunca editando la "
         "herramienta, y un control automático falla cuando una corrección firmada no aparece en la "
         "referencia derivada. Las anotaciones promovidas quedan congeladas bajo control de versiones, "
         "con huella criptográfica por clip y un manifiesto agregado del banco. La referencia "
         "experimental es la versión promovida en el repositorio y no el estado mutable de CVAT.")

# --------------------------------- 17.4.7 Verificación, alcance efectivo y brechas (fusión)
E[73] = ("H", "17.4.7. Verificación, alcance efectivo y brechas")

E[74] = ("E",
         "El criterio de cierre de la implementación exigió que cada unidad funcional produjera "
         "evidencia verificable dentro de una corrida y que su comportamiento pudiera repetirse "
         "mediante pruebas automatizadas o artefactos persistidos. La Tabla 59 reúne esa evidencia, "
         "concentrada en corrección de contratos, cierre de corridas, paridad entre caminos, "
         "determinismo y funcionamiento de la integración.")

E[79] = ("E",
         "La verificación confirmó además que las fallas instrumentales no se convierten en ceros "
         "silenciosos, porque una pérdida de bus degrada la corrida, una métrica sin reloj comparable "
         "se declara no interpretable y un canal no habilitado se declara no aplicable.")

E[80] = ("D",)   # el título de la vieja 17.4.10 desaparece con la fusión

E[81] = ("E",
         "El cierre de la implementación requiere declarar con precisión qué capacidades se ejercieron, "
         "cuáles permanecen fuera del núcleo y con qué estatuto, porque no todas las brechas son del "
         "mismo tipo.")

E[82] = ("E",
         "La concentración del prototipo en el núcleo validable no responde a una reducción tardía del "
         "alcance sino a las condiciones de evaluabilidad de cada condición del catálogo. Las de Nivel "
         "1 cuentan con datasets públicos y bancos con verdad de terreno para persona y elementos de "
         "protección, lo que permite medir percepción, estado temporal y alerta con denominadores "
         "declarados. Las de Nivel 2 y Nivel 3 exigen insumos que el material disponible no provee, y "
         "su justificación se desarrolla en la sección 17.5.7. Incorporarlas sin esa base habría "
         "producido capacidades no medibles, de modo que el esfuerzo se concentró en llevar el núcleo a "
         "capacidad medida.")

E[83] = ("D",)   # rótulo de la Tabla 60
E[84] = ("D",)   # título de la Tabla 60 (comentario 6)
E[86] = ("D",)   # nota de la Tabla 60

E[87] = ("E",
         "El prototipo conserva su carácter experimental y asistivo. No implementa reconocimiento de "
         "identidad personal, no determina incumplimientos normativos y no reemplaza la supervisión de "
         "seguridad, conforme a las salvaguardas de la sección 17.1.10.")

# ------------------------------------------ 17.4.8 Extensibilidad y costo de extensión
E[88] = ("H", "17.4.8. Extensibilidad y costo de extensión")

E[89] = ("E",
         "La extensibilidad se verificó en dos dimensiones, la incorporación de nuevas capacidades "
         "mediante puntos de extensión acotados y la evolución aditiva del evento de percepción. La "
         "plataforma no sostiene que toda condición pueda incorporarse sólo con lenguaje, y la Tabla 60 "
         "delimita qué cambios requieren configuración y cuáles requieren código nuevo.")

E[90] = ("E", "**Tabla 60**")

E[93] = ("E",
         "*Nota.* La frontera entre la primera y la segunda fila delimita la extensibilidad por "
         "configuración. Una ausencia de EPP sobre un sujeto observable reutiliza el evaluador "
         "existente, mientras que una relación nueva entre entidades requiere lógica de evaluación "
         "específica.")

E[94] = ("E",
         "El costo de incorporar vocabulario nuevo se midió en un piloto sobre la clase machinery. No "
         "requirió entrenamiento y demandó 48 líneas de configuración y nueve minutos de trabajo. El "
         "ejercicio mostró también que la extensión no termina al obtener detecciones, porque la "
         "alineación entre el término elegido y el concepto visual debe validarse. La sección 17.5.2 "
         "informa su desempeño y los dos fallos semánticos que aparecieron.")

E[95] = ("E",
         "La identidad de sujeto recorrió el segundo camino de extensión. Se implementó como un "
         "decorador configurable de la fuente de eventos del plano de control, desactivado por defecto y "
         "utilizable tanto en el camino diferido como en el camino en vivo. La incorporación no exigió "
         "modificar el plano de medios ni romper el contrato de percepción. El identificador se conserva "
         "en los artefactos de control y no en los del plano de medios, pero el seguidor y el orden del "
         "flujo son deterministas, de modo que una relectura reproduce las mismas identidades. Su "
         "efecto cuantitativo se informa en la sección 17.5.")

E[96] = ("E",
         "Lo excluido son las métricas formales de seguimiento multiobjeto y no la capacidad de asociar "
         "sujetos. De manera análoga, la velocidad, la dirección, la pose y la segmentación permanecen "
         "previstas como campos opcionales, sin presentarse como implementadas.")

E[97] = ("E",
         "En conjunto, la Etapa 4 materializó la cadena que va del video a la alerta distribuida como "
         "un prototipo ejecutable, configurable, reproducible y auditable, que conserva la separación "
         "entre planos, opera por archivo o por bus y explicita sus brechas. Sobre esa base, la sección "
         "17.5 evalúa su rendimiento sin atribuirle capacidades que no fueron medidas.")

# ------------------------------------------------------------------ párrafos nuevos (INSERTS)
INS = {
    24: [("El contrato de ciclo de vida no delimita el inicio de la corrida sino su cierre, y publica "
          "un único evento de finalización con el identificador de corrida y su estado, para que el "
          "final lógico se distinga de una interrupción. Ambos contratos se emplean sin variantes en "
          "los dos buses, porque el publicador de alertas del plano de control es un espejo deliberado "
          "del publicador de medios.")],
    26: [("La identidad de la alerta es entonces una función pura de esa quíntupla, con tres "
          "consecuencias verificables. Reprocesar la misma evidencia bajo el mismo identificador de "
          "corrida reproduce exactamente los mismos identificadores de alerta. La deduplicación no "
          "requiere estado compartido entre componentes, porque el módulo de distribución construye su "
          "clave de idempotencia a partir del identificador de alerta y la asienta en su propio "
          "registro sin consultar al plano de control. Y la identidad se asigna por confirmación y no "
          "por episodio, de modo que una confirmación posterior sobre el mismo sujeto recibe identidad "
          "propia y la idempotencia no oculta reincidencias reales.")],
    61: [("El ledger de entregas del módulo de distribución registra una fila por intento y una más por "
          "el descarte definitivo cuando se agotan los reintentos, de modo que la unidad de conteo del "
          "tramo es la notificación y no la fila. Al reutilizar un directorio de salida, la generación "
          "anterior se archiva íntegra y la deduplicación considera todas las generaciones, para que un "
          "reprocesamiento no vuelva a entregar lo ya entregado ni pierda la traza de lo entregado "
          "antes.")],
    65: [("La segunda fuente es un lote de obra real no guionada, obtenido de videos públicos e "
          "incorporado como bloque separado con criterios de selección definidos de antemano. Reúne "
          "material de obra en cumplimiento destinado a medir especificidad y falsos positivos, no "
          "sensibilidad, prohíbe concatenar segmentos cortos para fabricar unidades largas y exige que "
          "toda exclusión se declare con causa y firma en lugar de descartarse en silencio.")],
    68: [("Ese piso resulta de sumar al inicio del episodio el techo del objetivo de latencia de alerta "
          "de su patrón, la ventana de resolución y un margen final, y se verifica mediante un control "
          "automático durante la derivación de la referencia. El clip que no lo alcanza no se vuelve a "
          "recortar, y sus métricas de latencia y sensibilidad quedan censuradas y así se declaran."),
         ("El fundamento del dimensionamiento es bidireccional. Un clip demasiado corto subestima al "
          "sistema, porque produce latencias artefactuales y cuenta como omisión una alerta que no tuvo "
          "tiempo de ocurrir. Un clip sin tiempo muerto sobreestima la precisión, porque elimina los "
          "tramos donde aparecen los falsos positivos. La selección de tomas se hizo por calidad visual "
          "de la escena y no por duración, y los límites de todos los clips quedaron congelados bajo "
          "control de versiones antes de ejecutar las campañas. Los clips del lote de obra real no se "
          "segmentaron, porque recortarlos alteraría el tiempo negativo que ese bloque aporta.")],
    70: [("Sobre esa propuesta se realizó la pasada humana en CVAT. Esa revisión corrigió las cajas y "
          "las trayectorias de los 47 clips del banco, verificó la identidad de cada sujeto a lo largo "
          "de la secuencia y asignó los atributos observables tramo por tramo. Marcó como estado "
          "desconocido aquellos tramos donde el atributo no resulta observable, en lugar de forzar un "
          "valor, y fijó los límites temporales de los 37 episodios de referencia. La interpolación "
          "temporal y la preanotación redujeron las operaciones repetitivas, pero no sustituyeron "
          "ninguna de esas decisiones. La referencia experimental es el producto de esa revisión.")],
    86: [("Cuatro capacidades quedaron implementadas y medidas. La identidad persistente de sujeto opera "
          "como decorador configurable de la fuente del plano de control y constituye una capacidad "
          "medida, aunque las métricas formales de seguimiento permanezcan excluidas por falta de "
          "anotación de identidad. Las tres estrategias de detección se implementaron y su comparación "
          "se ejecutó. La distribución de alertas quedó implementada, verificada e integrada a la "
          "consola y a la orquestación, con MQTT como canal ejercido. Y la paridad entre la relectura "
          "por archivo y el transporte por bus quedó verificada. Los valores de todas ellas se informan "
          "en la sección 17.5."),
         ("Una capacidad se implementó y se caracterizó fuera del régimen evaluativo. La preselección "
          "liviana en el rol de captura funciona como filtro de personas ejecutado en el dispositivo, "
          "con criterio de degradación segura y deshabilitada por defecto, y no existe para las fuentes "
          "por red. Permaneció deshabilitada en todas las corridas evaluativas, y esa exclusión es "
          "deliberada y anterior a los resultados, porque un filtro de cuadros sin persona suprimiría "
          "las detecciones sostenidas que la tasa de falsas alarmas existe para medir. La sección "
          "17.5.7 informa su reducción de carga medida."),
         ("Las condiciones de riesgo de Nivel 2 y Nivel 3 quedaron especificadas y no implementadas. Su "
          "incorporación requiere evaluadores relacionales, zonales o de trayectoria y evidencia "
          "adecuada, y por eso no forman parte del núcleo validable."),
         ("La rama comparativa de ajuste fino se ejerció por completo. El protocolo, la procedencia, el "
          "servicio de inferencia, la evaluación y la línea base quedaron congelados, y la escalera de "
          "tramos pre-registrada se ejecutó entera. Los dos tramos entrenados se evaluaron una única "
          "vez contra el banco congelado, sin que ninguno superara los criterios de incorporación, que "
          "se firmaron antes de que existiera el punto de control al que se aplicarían. El tercer tramo se "
          "cerró con causa técnica, porque el único corpus disponible de ese volumen comparte fuentes "
          "con el banco de evaluación. Ninguno se incorporó como modelo de servicio, y los valores por "
          "tramo se informan en la sección 17.5.6."),
         ("El subconjunto de ajuste reunió 2.946 imágenes, por encima del rango orientativo de 500 a "
          "2.000 que fija el protocolo, y la desviación es consecuencia de cumplir la regla de "
          "partición y no de apartarse de ella. Se tomó el total de los linajes elegibles después de "
          "excluir íntegramente la fuente que el banco de evaluación comparte y de deduplicar de forma "
          "perceptual contra él, sin submuestrear hasta el techo del rango. Los controles de "
          "solapamiento con el banco y de componentes compartidos entre entrenamiento y validación "
          "quedaron en cero, y la semilla de partición se registró con el resto de la configuración.")],
    95: [("El evento de percepción admite además información que la implementación actual no produce, y "
          "esa capacidad se ejerció antes de declararse. La detección normalizada incluye hoy un campo "
          "de identidad entre fotogramas que ningún productor emite, declarado como opcional con valor "
          "por defecto y omitido al serializar cuando no tiene valor, de modo que su presencia no "
          "altera un solo byte de los artefactos existentes. El plano de control ya lo consume como "
          "clave de estado cuando opera con granularidad por sujeto, y el contrato conservó su "
          "versión."),
         ("Tres decisiones de implementación sostienen esa propiedad. Los campos nuevos se agregan como "
          "opcionales con valor por defecto, los consumidores validan contra su propia declaración del "
          "contrato y descartan sin error los campos que no conocen, y la frontera de la distribución "
          "admite explícitamente campos adicionales. Cada plano mantiene además su propia declaración "
          "del evento en lugar de una biblioteca compartida, de modo que la frontera entre ellos es el "
          "esquema serializado y no una dependencia de código, y ambos pueden versionarse y desplegarse "
          "por separado.")],
}

# --------------------------------------------------------------------------- operaciones de tabla
TBL = {
    34: [("cell", 3, 2, "Detiene cooperativamente la corrida en curso y el cierre se propaga a los "
                        "consumidores por el bus."),
         ("cell", 7, 2, "Dispara una corrida en modo diferido o en vivo."),
         ("cell", 16, 0, "Orquestador y consola"),
         ("cell", 16, 2, "Gobiernan corridas y consolidan artefactos, sin consumir los buses de datos.")],
    77: [("cell", 1, 1, "Las operaciones de salud, disponibilidad, creación y consulta de corridas "
                        "operan sobre configuraciones validadas, y cada servicio limita la concurrencia "
                        "de corridas activas."),
         ("cell", 2, 1, "La relectura por archivo produce detecciones, transiciones, alertas, métricas, "
                        "resumen y configuración efectiva, y repetir el camino conserva los artefactos "
                        "deterministas."),
         ("cell", 4, 1, "La evidencia persistida y la transmitida conservan el mismo contenido lógico, y "
                        "una corrida en vivo puede reevaluarse por el camino diferido."),
("cell", 6, 1,
          "Se verificaron la relectura diferida, el consumo en vivo, la supresión, la idempotencia, la "
          "entrega MQTT con confirmación contra un broker real, el ledger y el reporte."),
         ("cell", 7, 1,
          "Una verificación integral registró 2.203 pruebas aprobadas sin fallos en cinco suites, y el "
          "módulo de distribución incorporó después su propia suite. El conteo corresponde a esa "
          "verificación.")],
    85: [("delall",)],   # Tabla 60 → prosa por estatuto (D-C)
    92: [("cell", 1, 1, "Entrada declarativa en el conjunto de patrones y formulaciones de prompt, con "
                        "clase del sujeto, clase ausente, región, umbrales y ventanas."),
         ("cell", 2, 2, "Código acotado al evaluador, con los contratos y el resto de la cadena "
                        "conservados.")],
}

# Párrafo modelo para los insertos cuyo ancla no es prosa corriente (la nota de una tabla
# arrastra su sangría y su cursiva).
INS_SAMPLE = {86: 82}

# ------------------------------------- comentarios re-anclados: id → ("u", unidad) | ("ins", unidad, k)
REANCLA = {
    0: ("u", 20),        # DTO: del título borrado al párrafo que presenta los cinco contratos
    1: ("u", 44),        # la PC como recurso: al párrafo que ahora remite a §17.1.4.1
    2: ("ins", 61, 0),   # falta distribución: al párrafo nuevo del ledger
    3: ("u", 60),        # dato de más: al párrafo del que se quitó la oración
    4: ("u", 70),        # horas de anotación: al bloque de preanotación y revisión
    5: ("ins", 70, 0),   # esfuerzo de la revisión: al párrafo que lo afirma
    6: ("ins", 86, 0),   # la tabla a desarrollo: al primer párrafo de la prosa que la reemplaza
}


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
    st = {"E": 0, "H": 0, "D": 0, "K": 0, "INS": 0, "TBL": 0}
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

        # las anclas de los comentarios que se re-anclan salen de su párrafo de origen
        presentes = [cid for cid in REANCLA
                     if f'<w:commentRangeStart w:id="{cid}"/>' in raw]
        p = strip_comment_anchors(raw, presentes) if presentes else raw

        op = E.get(i)
        if op is None:
            out.append(p)
            st["K"] += 1
        elif op[0] == "D":
            out.append(delete_para(p))
            st["D"] += 1
        else:
            p = edit_para(p, op[1])
            st["H" if op[0] == "H" else "E"] += 1
            for cid, dest in REANCLA.items():
                if dest == ("u", i):
                    p = wrap_comment(p, cid)
            out.append(p)

        muestra = units[INS_SAMPLE[i]][1] if i in INS_SAMPLE else raw
        for k, text in enumerate(INS.get(i, [])):
            np = new_para(text, sample=muestra)
            for cid, dest in REANCLA.items():
                if dest == ("ins", i, k):
                    np = wrap_comment(np, cid)
            out.append(np)
            st["INS"] += 1

    out.append(resto)
    newxml = head + "".join(out) + tail
    assert newxml.count("<w:sectPr") == xml.count("<w:sectPr"), "se perdió un sectPr"
    assert newxml.count("commentRangeStart") == xml.count("commentRangeStart"), "comentario perdido"
    assert newxml.count("<w:drawing") == xml.count("<w:drawing"), "se perdió la figura"

    with zipfile.ZipFile(DST, "w") as zo:
        for it in src.infolist():
            data = newxml.encode("utf8") if it.filename == "word/document.xml" else src.read(it.filename)
            zo.writestr(it, data, compress_type=zipfile.ZIP_DEFLATED)

    print("editados:", st["E"], "| títulos:", st["H"], "| borrados:", st["D"],
          "| intactos:", st["K"], "| nuevos:", st["INS"], "| tablas tocadas:", st["TBL"])
    print("w:ins:", newxml.count("<w:ins "), " w:del:", newxml.count("<w:del "),
          " sectPr:", newxml.count("<w:sectPr"), " tbl:", newxml.count("<w:tbl>"),
          " drawing:", newxml.count("<w:drawing"),
          " commentRangeStart:", newxml.count("commentRangeStart"))
    print("salida:", DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
