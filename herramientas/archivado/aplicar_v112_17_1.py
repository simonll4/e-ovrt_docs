#!/usr/bin/env python3
"""Aplica sobre la v1.11 de §17.1, como CAMBIOS CONTROLADOS (w:ins / w:del sin aceptar), las
reparaciones acordadas el 2026-09-03 (relevamiento-17-1-v1-11.md, decisiones del usuario):

  E1  C-1 + C-3  : 17.1.7.1 — niveles de compromiso + jerarquía + criterios de factibilidad (2 párrafos)
  E2  C-2 + C-4  : 17.1.7.5 — modelo aditivo orientativo (párrafo + 2 ecuaciones OMML + párrafo)
                   y puente 2–4 s → 3–5 s + cláusula de recalibración (al final del párrafo previo a Tabla 30)
  E3  C-5        : Tabla 26, fila "Congelamiento previo" — "…, selección de checkpoints"
  E4  Anexo D    : remisiones a Tablas D.1 (17.1.7.3), D.3 y D.2 (17.1.7.6)
  E5  D-2 (a)    : Tabla D.1, fila "Latencia G2A" — definición desde el dequeue + criterio de reloj
  E6  ref        : 17.1.3.3 — "Sección 17.1.4.4" → "17.1.4.2"
  E7  B-2        : 17.1.6.1 — condiciones fuera del catálogo (calzado, guantes, gafas, pasillos)

NO toca: §17.1.6 mecánicos (Tabla 26 fila truncada, [[PENDIENTE]], nota C.3), huecos de numeración,
comentarios, saltos de sección. Edición byte a byte de word/document.xml; el resto del zip se copia igual.
"""
from __future__ import annotations
import copy, re, sys, zipfile, shutil
import xml.etree.ElementTree as ET
from pathlib import Path

SRC = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.11.docx")
DST = SRC.with_name("E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.12 (sugerencias sin aceptar).docx")

AUTHOR = "Claude"
DATE = "2026-09-03T03:00:00Z"
NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
}
for k, v in NS.items():
    ET.register_namespace(k, v)

FONTS = ('<w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman" '
         'w:hAnsi="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/>')
RPR_RUN = "<w:rPr>" + FONTS + '<w:rtl w:val="0"/></w:rPr>'

_id = [9000]
def nid() -> int:
    _id[0] += 1
    return _id[0]

def tc(tag: str) -> str:
    return f'<w:{tag} w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"'

def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def ins_run(text: str, rpr: str = RPR_RUN) -> str:
    return f'{tc("ins")}><w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:ins>'

def del_run(text: str, rpr: str = RPR_RUN) -> str:
    return f'{tc("del")}><w:r>{rpr}<w:delText xml:space="preserve">{esc(text)}</w:delText></w:r></w:del>'

def ppr_inserted(center: bool = False) -> str:
    align = '<w:jc w:val="center"/>' if center else '<w:ind w:firstLine="720"/>'
    return ('<w:pPr><w:spacing w:line="480" w:lineRule="auto"/>' + align +
            '<w:rPr>' + tc("ins") + '/>' + FONTS + '</w:rPr></w:pPr>')

def new_para(text: str) -> str:
    return "<w:p>" + ppr_inserted() + ins_run(text) + "</w:p>"

def new_eq_para(omath_xml: str) -> str:
    return "<w:p>" + ppr_inserted(center=True) + tc("ins") + ">" + omath_xml + "</w:ins></w:p>"

# ----------------------------------------------------------------- OMML (desde la v1.10)
def load_omath(which: str) -> ET.Element:
    """Toma el m:oMath de la v1.10 cuyo texto matemático empieza por `which`
    (los párrafos 556/557 de la v1.10: 'tG2A = tcaptura…' y 'talert-system ≈ tevidencia…')."""
    import glob
    cands = glob.glob(str(SRC.parent / "**" / "*Consolidacion_Metodologica_v1.10.docx"), recursive=True)
    assert cands, "no encuentro la v1.10 (desarrollando/ o archivado/)"
    x10 = zipfile.ZipFile(cands[0]).read("word/document.xml").decode("utf8")
    hits = [p for p in re.findall(r"<w:p[ >].*?</w:p>", x10, flags=re.S)
            if "".join(re.findall(r"<m:t(?: [^>]*)?>([^<]*)</m:t>", p)).startswith(which)]
    assert len(hits) == 1, (which, len(hits))
    wrapped = ("<root " + " ".join(f'xmlns:{k}="{v}"' for k, v in NS.items()) + ">" + hits[0] + "</root>")
    om = ET.fromstring(wrapped).find(".//m:oMath", NS)
    assert om is not None
    return om

def mtext(el: ET.Element) -> str:
    return "".join(t.text or "" for t in el.iter(f"{{{NS['m']}}}t"))

def build_eq1() -> str:
    """t_G2A = t_preprocesamiento + t_inferencia (desde tG2A = tcaptura + ttransporte + tpre + tinf)."""
    om = load_omath("tG2A = tcaptura")
    kids = list(om)
    assert [mtext(k).strip() for k in kids] == ["tG2A", "=", "tcaptura", "+", "ttransporte", "+", "tpreprocesamiento", "+", "tinferencia"], [mtext(k) for k in kids]
    for k in kids[2:6]:
        om.remove(k)
    assert mtext(om) == "tG2A = tpreprocesamiento + tinferencia", mtext(om)
    return ET.tostring(om, encoding="unicode")

def build_eq2() -> str:
    """t_alert-system ≈ t_evidencia + t_captura-host + t_G2A + t_tracking + t_razonamiento."""
    om = load_omath("talert-system ≈ tevidencia")
    kids = list(om)
    assert [mtext(k).strip() for k in kids] == ["talert-system", "≈", "tevidencia", "+", "tG2A", "+", "ttracking", "+", "trazonamiento"], [mtext(k) for k in kids]
    sub_new = copy.deepcopy(kids[2])      # sSub t_evidencia
    plus_new = copy.deepcopy(kids[3])     # r " + "
    tnode = sub_new.find("m:sub/m:r/m:t", NS)
    assert tnode is not None and tnode.text == "evidencia"
    tnode.text = "captura-host"
    om.insert(4, plus_new)
    om.insert(4, sub_new)
    assert mtext(om) == "talert-system ≈ tevidencia + tcaptura-host + tG2A + ttracking + trazonamiento", mtext(om)
    return ET.tostring(om, encoding="unicode")

# ----------------------------------------------------------------- utilidades sobre document.xml
def ptext(p: str) -> str:
    return "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", p))

class Doc:
    def __init__(self, xml: str):
        self.xml = xml

    def paras(self):
        return re.findall(r"<w:p[ >].*?</w:p>", self.xml, flags=re.S)

    def find(self, start: str, end: str | None = None) -> str:
        hits = [p for p in self.paras() if ptext(p).startswith(start) and (end is None or ptext(p).endswith(end))]
        assert len(hits) == 1, (start, len(hits))
        assert self.xml.count(hits[0]) == 1, "párrafo no único en el XML"
        return hits[0]

    def replace(self, old: str, new: str):
        assert self.xml.count(old) == 1
        self.xml = self.xml.replace(old, new)

    def insert_after(self, para: str, new_xml: str):
        self.replace(para, para + new_xml)

    def append_run(self, para: str, text: str):
        assert para.endswith("</w:p>")
        self.replace(para, para[:-len("</w:p>")] + ins_run(text) + "</w:p>")

    def runs(self, para: str):
        return re.findall(r"<w:r[ >].*?</w:r>", para, flags=re.S)

    def insert_after_run(self, para: str, run_text: str, text: str):
        rs = [r for r in self.runs(para) if ptext(r) == run_text]
        assert len(rs) == 1 and para.count(rs[0]) == 1, run_text
        self.replace(para, para.replace(rs[0], rs[0] + ins_run(text)))

    def replace_run_text(self, para: str, run_text: str, new_text: str):
        """Reemplaza el texto completo de un run: del(viejo) + ins(nuevo), misma rPr."""
        rs = [r for r in self.runs(para) if ptext(r) == run_text]
        assert len(rs) == 1 and para.count(rs[0]) == 1, run_text
        rpr = re.search(r"<w:rPr>.*?</w:rPr>", rs[0], flags=re.S).group(0)
        self.replace(para, para.replace(rs[0], del_run(run_text, rpr) + ins_run(new_text, rpr)))

    def replace_in_run(self, para: str, old: str, new: str):
        """Reemplaza un fragmento dentro de un run (split en tres runs)."""
        rs = [r for r in self.runs(para) if old in ptext(r)]
        assert len(rs) == 1 and para.count(rs[0]) == 1, old
        r = rs[0]
        rpr = re.search(r"<w:rPr>.*?</w:rPr>", r, flags=re.S).group(0)
        m = re.search(r"(<w:t(?: [^>]*)?>)([^<]*)(</w:t>)", r)
        t = m.group(2)
        assert t.count(old) == 1
        before, after = t.split(old)
        def run(txt):
            return f'<w:r>{rpr}<w:t xml:space="preserve">{txt}</w:t></w:r>' if txt else ""
        new_r = run(before) + del_run(old, rpr) + ins_run(new, rpr) + run(after)
        self.replace(para, para.replace(r, new_r))

# ----------------------------------------------------------------- textos nuevos (sin dos puntos ni punto y coma)
P_A = ("El framework asigna además a cada métrica un nivel de compromiso. Una métrica obligatoria es la que el "
       "núcleo del prototipo debe reportar para sostener sus conclusiones. Una métrica deseable enriquece el análisis "
       "y su omisión no invalida el experimento si se explicita la razón. Un tratamiento conceptual tiene una "
       "formulación analítica pertinente aunque su evaluación empírica completa exceda el alcance del prototipo. "
       "Sobre ese eje se ordena una jerarquía interpretativa en tres niveles. El nivel primario reúne las métricas "
       "con valor operativo directo para la alerta, como t_alert-system, TTFD, SDR y la precisión y el recall por "
       "severidad. El nivel secundario reúne las métricas que explican el comportamiento del detector, de la "
       "identidad temporal y del pipeline sin constituir por sí mismas evidencia de valor operativo, como AP, las "
       "métricas MOT y los indicadores de rendimiento. El nivel transversal reúne las métricas de comparación entre "
       "la línea base zero-shot y la variante ajustada. La pertenencia al nivel primario expresa prioridad "
       "interpretativa y no aplicabilidad automática. Si los recursos experimentales no permiten ejecutar todo el "
       "repertorio con la misma profundidad, el núcleo evaluativo queda dado por las métricas primarias y por los "
       "diagnósticos mínimos del pipeline.")
P_B = ("Una métrica sólo se asume como obligatoria cuando cumple cinco condiciones a la vez. Debe ser necesaria para "
       "responder la pregunta de validación del prototipo. Debe contar con una referencia anotada verificable. Debe "
       "existir el módulo que produce la señal evaluada. Debe disponer de instrumentación suficiente mediante marcas "
       "temporales, registros o exportación de resultados, y su costo de anotación o procesamiento debe ser "
       "compatible con el proyecto. Bajo estos criterios una métrica puede estar correctamente definida en el "
       "framework y aun así no corresponder en una corrida concreta.")
P_C = ("Para instrumentar la cadena y estimar la plausibilidad del presupuesto se adopta además un modelo aditivo "
       "orientativo. El modelo no reemplaza la medición por hitos ni constituye una regla de cálculo de "
       "t_alert-system. Su descomposición es la siguiente.")
P_D = ("En esta descomposición t_evidencia es la ventana funcional de persistencia, t_captura-host es el tramo "
       "capture_to_host de la Tabla 29 y sólo se incluye cuando la fuente aporta una marca de captura confiable, "
       "t_tracking es la identidad temporal cuando está habilitada y t_razonamiento es el cómputo de la evaluación "
       "del patrón. El modelo es deliberadamente aditivo y conservador. Aunque una implementación real puede "
       "presentar solapamientos, buffering o paralelismo, la descomposición lineal sigue siendo útil para "
       "instrumentar mediciones, detectar cuellos de botella y comparar configuraciones. La estimación orientativa "
       "que sigue corresponde a la suma de todos los términos salvo t_evidencia.")
S_BRIDGE = (" Para la severidad crítica, la ventana de 2 a 4 s propuesta en la sección 17.1.5.2 sumada al tramo "
            "computacional estimado vuelve coherente el objetivo de 3 a 5 s de la Tabla 30. Para las severidades alta "
            "y media, ventanas más largas hacen igualmente plausibles los objetivos de 5 a 10 s y de 10 a 20 s. Si el "
            "hardware efectivo difiere del perfil de referencia, por ejemplo con modelos más pesados, una resolución "
            "de entrada mayor o un transporte con más latencia, las referencias de la Tabla 30 deben recalibrarse "
            "antes de operar como criterio de aceptación.")
S_D1 = (" Las definiciones operativas, el formato de reporte y los criterios de estabilidad de estas medidas se "
        "consolidan en la Tabla D.1 del Anexo D.")
S_D3 = " El detalle de campos de la bitácora se consolida en la Tabla D.3 del Anexo D."
S_D2 = " Los insumos mínimos que habilitan cada familia de métricas se consolidan en la Tabla D.2 del Anexo D."
T_G2A_NEW = ("Intervalo entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia. La "
             "captura y el transporte hasta el dequeue se informan aparte como capture_to_host.")
T_CLOCK_NEW = "Hitos y dominio de reloj declarados"
S_B2 = (" Las condiciones de calzado inadecuado, ausencia de guantes o gafas de protección y obstrucción de pasillos "
        "o materiales inestables no integran el catálogo de la sección 17.1.5.1, por lo que su cobertura de datos "
        "sólo correspondería analizarse si se ampliara el conjunto de condiciones evaluadas.")

for s in (P_A, P_B, P_C, P_D, S_BRIDGE, S_D1, S_D2, S_D3, T_G2A_NEW, S_B2):
    assert ":" not in s and ";" not in s, "prosa nueva con dos puntos o punto y coma"

# ----------------------------------------------------------------- aplicar
def main() -> int:
    zin = zipfile.ZipFile(SRC)
    doc = Doc(zin.read("word/document.xml").decode("utf8"))
    n0 = len(doc.paras())

    # E1 — 17.1.7.1: después del párrafo de los tres niveles, antes de "Cada métrica debe acompañarse…"
    p392 = doc.find("La factibilidad no se determina mediante una cifra aislada.")
    p393 = doc.find("Cada métrica debe acompañarse de un estado explícito.")
    assert doc.xml.find(p392) < doc.xml.find(p393)
    doc.insert_after(p392, new_para(P_A) + new_para(P_B))

    # E2 — 17.1.7.5: después de "El tramo computacional reúne…", antes de "Con el perfil de hardware…"
    p507 = doc.find("El tramo computacional reúne el preprocesamiento")
    p508 = doc.find("Con el perfil de hardware de referencia")
    assert doc.xml.find(p507) < doc.xml.find(p508)
    doc.insert_after(p507, new_para(P_C) + new_eq_para(build_eq1()) + new_eq_para(build_eq2()) + new_para(P_D))
    # E2b — puente + recalibración al final del párrafo previo a la Tabla 30 (lleva el sectPr portrait: no se
    # inserta ningún párrafo nuevo ahí, sólo runs dentro del mismo párrafo)
    p509 = doc.find("La latencia de alerta incorpora además la ventana de evidencia", "respuesta perceptiva inicial.")
    assert "<w:sectPr" in p509
    doc.append_run(p509, S_BRIDGE)

    # E3 — Tabla 26 fila "Congelamiento previo"
    p361 = doc.find("El banco de evaluación queda definido antes de entrenar", "ni aumento de datos.")
    doc.insert_after_run(p361, "hiperparámetros", ", selección de checkpoints")

    # E4 — remisiones al Anexo D
    doc.append_run(doc.find("La viabilidad operativa se caracteriza mediante la cadencia efectiva"), S_D1)
    doc.append_run(doc.find("Toda corrida debe registrar el contexto necesario para reproducirla."), S_D3)
    doc.append_run(doc.find("La aplicabilidad se determina antes de interpretar el valor."), S_D2)

    # E5 — Tabla D.1 fila "Latencia G2A"
    old_def = "Intervalo entre captura o lectura del cuadro y disponibilidad del resultado de inferencia."
    p801 = doc.find(old_def, old_def)
    doc.replace_run_text(p801, old_def, T_G2A_NEW)
    p804 = doc.find("Timestamps monotónicos", "Timestamps monotónicos")
    doc.replace_run_text(p804, "Timestamps monotónicos", T_CLOCK_NEW)

    # E6 — 17.1.3.3 referencia colgante
    p20 = doc.find("Sobre esa base, la evaluación se organiza en dos escenarios", "Sección 17.1.4.4.")
    doc.replace_in_run(p20, "17.1.4.4", "17.1.4.2")

    # E7 — 17.1.6.1 condiciones fuera del catálogo
    p227 = doc.find("El inventario distingue fuentes de gestión directa y benchmarks de referencia.", "con escenas reales.")
    doc.append_run(p227, S_B2)

    # --- verificación de buena formación y conteos
    ET.fromstring(doc.xml.encode("utf8"))
    n1 = len(doc.paras())
    print(f"párrafos {n0} → {n1} (+{n1 - n0}, esperado +6)")
    print("w:ins:", doc.xml.count("<w:ins "), " w:del:", doc.xml.count("<w:del "), " oMath:", doc.xml.count("<m:oMath"),
          " sectPr:", doc.xml.count("<w:sectPr"), " tbl:", doc.xml.count("<w:tbl>"), " comentarios:", doc.xml.count("commentRangeStart"))

    # --- escribir el zip copiando todo lo demás byte a byte
    if DST.exists():
        DST.unlink()
    with zipfile.ZipFile(DST, "w") as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = doc.xml.encode("utf8")
            zout.writestr(item, data, compress_type=zipfile.ZIP_DEFLATED)
    print("escrito:", DST.name, DST.stat().st_size, "bytes")
    return 0

if __name__ == "__main__":
    sys.exit(main())
