#!/usr/bin/env python3
"""v1.14 de §17.1 = v1.13 + puente entre marcos temporales (P_D) + "Máximo orientativo" en Tabla 30.
v1.13 de §17.1 = v1.11 + el paquete de reparaciones acordado el 2026-09-03, como CAMBIOS
CONTROLADOS (w:ins / w:del sin aceptar). Reemplaza a la v1.12: mantiene sus ediciones E3–E6 y
revisa E1, E2, E2b y E7 con las tres correcciones editoriales de GPT (relevamiento §I.2) y las
decisiones B-2 / B-3 tomadas por coherencia (§J del relevamiento).

  E1'  17.1.7.1, después del párrafo de los cuatro estados — niveles de compromiso (obligatorio /
       deseable / conceptual) + criterio de exigibilidad. SIN la jerarquía primario/secundario/transversal.
  T33  Tabla 33, fila Baseline DBE — "métricas primarias" → "métricas obligatorias" (dependencia de E1').
  E2'  17.1.7.5 — modelo de presupuesto con notación propia: B_procesamiento ≈ B_captura-host +
       B_preprocesamiento + B_inferencia + B_identidad + B_reglas · B_alerta ≈ W_evidencia + B_procesamiento.
       t_alert-system no se reutiliza en ninguna suma.
  E2b' 17.1.7.5, párrafo previo a la Tabla 30 — compatibilidad cualitativa objetivo ↔ ventana + margen,
       y cláusula de recalibración. Sin el puente aritmético.
  E3   Tabla 26 "Congelamiento previo" — "…, selección de checkpoints".
  E4   remisiones a Tablas D.1 (17.1.7.3), D.3 y D.2 (17.1.7.6).
  E5   Tabla D.1 fila "Latencia G2A" — desde el dequeue + criterio de reloj.
  E6   17.1.3.3 — "Sección 17.1.4.4" → "17.1.4.2".
  B-2' 17.1.5.1 — guantes y gafas se suman al ejemplo de detalle irresoluble; pasillos y materiales
       inestables como condiciones de escena fuera del catálogo. (Se retira la inserción de 17.1.6.1 de la v1.12.)
  B-3  Tabla 27, nota — expansión de TETA / LocA / ClsA / AssA, antes del marcador [[PENDIENTE]].

NO toca: mecánicos de §17.1.6 (fila truncada de la Tabla 26, los [[PENDIENTE]], nota C.3),
huecos de numeración, comentarios, saltos de sección. Se parte de la v1.11 porque la v1.12 no fue
modificada por el usuario (mismo tamaño y fecha de creación): rechazar todo devuelve la v1.11.
"""
from __future__ import annotations
import copy, glob, re, sys, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
SRC = BASE / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.11.docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.14 (sugerencias sin aceptar).docx"

AUTHOR = "Claude"
DATE = "2026-09-03T07:00:00Z"
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

_id = [9200]
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

# ----------------------------------------------------------------- OMML: plantilla desde la v1.10
def template_omath() -> ET.Element:
    cands = glob.glob(str(BASE / "**" / "*Consolidacion_Metodologica_v1.10.docx"), recursive=True)
    assert cands, "no encuentro la v1.10 (desarrollando/ o archivado/)"
    x10 = zipfile.ZipFile(cands[0]).read("word/document.xml").decode("utf8")
    hits = [p for p in re.findall(r"<w:p[ >].*?</w:p>", x10, flags=re.S)
            if "".join(re.findall(r"<m:t(?: [^>]*)?>([^<]*)</m:t>", p)).startswith("talert-system ≈ tevidencia")]
    assert len(hits) == 1
    wrapped = "<root " + " ".join(f'xmlns:{k}="{v}"' for k, v in NS.items()) + ">" + hits[0] + "</root>"
    om = ET.fromstring(wrapped).find(".//m:oMath", NS)
    assert om is not None
    return om

def mtext(el: ET.Element) -> str:
    return "".join(t.text or "" for t in el.iter(f"{{{NS['m']}}}t"))

def build_eq(terms: list[str], first_op: str = "≈") -> str:
    """terms como 'B_procesamiento' → sSub(base, sub); operadores: first_op entre el 1.º y el 2.º, '+' después."""
    tpl = template_omath()
    kids = list(tpl)
    ssub_tpl, op_tpl = kids[2], kids[3]          # sSub t_evidencia · r " + "
    assert mtext(ssub_tpl) == "tevidencia" and mtext(op_tpl).strip() == "+"
    def ssub(term: str) -> ET.Element:
        base, sub = term.split("_", 1)
        el = copy.deepcopy(ssub_tpl)
        el.find("m:e/m:r/m:t", NS).text = base
        el.find("m:sub/m:r/m:t", NS).text = sub
        return el
    def op(sym: str) -> ET.Element:
        el = copy.deepcopy(op_tpl)
        el.find("m:t", NS).text = f" {sym} "
        return el
    om = copy.deepcopy(tpl)
    for k in list(om):
        om.remove(k)
    for i, term in enumerate(terms):
        if i == 1:
            om.append(op(first_op))
        elif i > 1:
            om.append(op("+"))
        om.append(ssub(term))
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
        assert self.xml.count(hits[0]) == 1, "párrafo no único"
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
        rs = [r for r in self.runs(para) if ptext(r) == run_text]
        assert len(rs) == 1 and para.count(rs[0]) == 1, run_text
        rpr = re.search(r"<w:rPr>.*?</w:rPr>", rs[0], flags=re.S).group(0)
        self.replace(para, para.replace(rs[0], del_run(run_text, rpr) + ins_run(new_text, rpr)))
    def _split_run(self, para: str, anchor: str, before_anchor: bool, text: str, delete: str | None = None):
        rs = [r for r in self.runs(para) if anchor in ptext(r)]
        assert len(rs) == 1 and para.count(rs[0]) == 1, anchor
        r = rs[0]
        rpr = re.search(r"<w:rPr>.*?</w:rPr>", r, flags=re.S).group(0)
        t = re.search(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", r).group(1)
        assert t.count(anchor) == 1
        i = t.index(anchor)
        def run(txt):
            return f'<w:r>{rpr}<w:t xml:space="preserve">{txt}</w:t></w:r>' if txt else ""
        if delete is not None:                      # sustituir el ancla
            new_r = run(t[:i]) + del_run(anchor, rpr) + ins_run(text, rpr) + run(t[i + len(anchor):])
        elif before_anchor:                         # insertar antes del ancla
            new_r = run(t[:i]) + ins_run(text, rpr) + run(t[i:])
        else:                                       # insertar después del ancla
            new_r = run(t[:i + len(anchor)]) + ins_run(text, rpr) + run(t[i + len(anchor):])
        self.replace(para, para.replace(r, new_r))
    def replace_in_run(self, para, old, new):        self._split_run(para, old, False, new, delete=old)
    def insert_before_in_run(self, para, anchor, text): self._split_run(para, anchor, True, text)
    def insert_after_in_run(self, para, anchor, text):  self._split_run(para, anchor, False, text)

# ----------------------------------------------------------------- textos nuevos (sin dos puntos ni punto y coma)
P_A = ("El nivel de compromiso de una métrica es independiente de su estado de aplicabilidad. Una métrica "
       "obligatoria es la que el núcleo del prototipo debe reportar cuando sus precondiciones se cumplen. Una "
       "métrica deseable amplía el análisis y su omisión justificada no invalida el protocolo. Un tratamiento "
       "conceptual conserva valor metodológico aunque requiera datos o módulos que exceden una corrida "
       "determinada. Una métrica se considera exigible cuando responde a la pregunta experimental, dispone de una "
       "referencia anotada verificable, el módulo que produce la señal existe, el tramo está suficientemente "
       "instrumentado y el costo de anotación o procesamiento es compatible con el alcance del proyecto. Bajo "
       "estos criterios una métrica puede estar correctamente definida en el framework y aun así no corresponder "
       "en una corrida concreta. Si los recursos experimentales no permiten ejecutar todo el repertorio con la "
       "misma profundidad, el núcleo evaluativo queda dado por las métricas obligatorias de los tres niveles y por "
       "los diagnósticos mínimos del pipeline.")
P_C = ("Para instrumentar la cadena y estimar la plausibilidad del presupuesto se adopta además un modelo de "
       "presupuesto de ingeniería con notación propia, separada de las métricas medidas por hitos. B denota la "
       "estimación orientativa de un tramo y W una espera funcional. Los componentes sólo se suman cuando son "
       "sucesivos y no se solapan.")
P_D = ("B_captura-host corresponde al tramo capture_to_host de la Tabla 29 y sólo se incluye cuando la fuente "
       "aporta una marca de captura confiable. B_identidad corresponde a la identidad temporal cuando está "
       "habilitada y B_reglas al cómputo de la evaluación del patrón. B_alerta es una referencia de plausibilidad "
       "y no reemplaza a t_alert-system, que se obtiene de los hitos reales del episodio y de la alerta. La "
       "latencia vidrio a alerta de un episodio se aproxima entonces a la suma de TTFD y B_alerta. "
       "t_alert-system, medida entre hitos del reloj de la fuente, comprende la reacción perceptiva inicial y "
       "la ventana funcional, pero no la cola de procesamiento del cuadro que confirma, que se informa por "
       "separado mediante capture_to_host y t_G2A. La estimación orientativa que sigue corresponde a "
       "B_procesamiento.")
S_BRIDGE = (" El objetivo de t_alert-system de cada severidad debe ser compatible con la ventana de persistencia "
            "fijada para sus patrones en la sección 17.1.5.2 y dejar margen para el procesamiento y la "
            "variabilidad de la cadena. Los valores orientativos deben recalibrarse antes de utilizarse como "
            "criterio de aceptación cuando cambien el modelo, la resolución de entrada, la cadencia o las "
            "condiciones de transporte.")
S_D1 = (" Las definiciones operativas, el formato de reporte y los criterios de estabilidad de estas medidas se "
        "consolidan en la Tabla D.1 del Anexo D.")
S_D3 = " El detalle de campos de la bitácora se consolida en la Tabla D.3 del Anexo D."
S_D2 = " Los insumos mínimos que habilitan cada familia de métricas se consolidan en la Tabla D.2 del Anexo D."
T_G2A_NEW = ("Intervalo entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia. La "
             "captura y el transporte hasta el dequeue se informan aparte como capture_to_host.")
T_CLOCK_NEW = "Hitos y dominio de reloj declarados"
S_B2_A = " o la presencia de guantes y gafas de protección"
S_B2_B = (" También quedan fuera, aunque son preventivamente relevantes, condiciones de escena como la "
          "obstrucción de pasillos o la presencia de materiales inestables, que no admiten una definición visual "
          "estable para su anotación.")
S_B3 = ("TETA es Track Every Thing Accuracy y se descompone en LocA, ClsA y AssA, que miden localización, "
        "clasificación y asociación. ")

for s in (P_A, P_C, P_D, S_BRIDGE, S_D1, S_D2, S_D3, T_G2A_NEW, S_B2_A, S_B2_B, S_B3):
    assert ":" not in s and ";" not in s, "prosa nueva con dos puntos o punto y coma"

# ----------------------------------------------------------------- aplicar
def main() -> int:
    zin = zipfile.ZipFile(SRC)
    doc = Doc(zin.read("word/document.xml").decode("utf8"))
    n0 = len(doc.paras())

    # E1' — 17.1.7.1: después del párrafo de los cuatro estados
    p393 = doc.find("Cada métrica debe acompañarse de un estado explícito.", "como resultado omitido.")
    doc.insert_after(p393, new_para(P_A))
    # T33 — Tabla 33: métricas primarias → obligatorias
    p557 = doc.find("Predicciones exportadas y métricas primarias calculadas.", "calculadas.")
    doc.replace_in_run(p557, "primarias", "obligatorias")

    # E2' — 17.1.7.5: entre "El tramo computacional reúne…" y "Con el perfil de hardware…"
    p507 = doc.find("El tramo computacional reúne el preprocesamiento")
    p508 = doc.find("Con el perfil de hardware de referencia")
    assert doc.xml.find(p507) < doc.xml.find(p508)
    eq1 = build_eq(["B_procesamiento", "B_captura-host", "B_preprocesamiento", "B_inferencia", "B_identidad", "B_reglas"])
    eq2 = build_eq(["B_alerta", "W_evidencia", "B_procesamiento"])
    doc.insert_after(p507, new_para(P_C) + new_eq_para(eq1) + new_eq_para(eq2) + new_para(P_D))
    # E2b' — final del párrafo previo a la Tabla 30 (lleva el sectPr: sólo runs)
    p509 = doc.find("La latencia de alerta incorpora además la ventana de evidencia", "respuesta perceptiva inicial.")
    assert "<w:sectPr" in p509
    doc.append_run(p509, S_BRIDGE)

    # E3 — Tabla 26 "Congelamiento previo"
    p361 = doc.find("El banco de evaluación queda definido antes de entrenar", "ni aumento de datos.")
    doc.insert_after_run(p361, "hiperparámetros", ", selección de checkpoints")

    # E4 — remisiones al Anexo D
    doc.append_run(doc.find("La viabilidad operativa se caracteriza mediante la cadencia efectiva"), S_D1)
    doc.append_run(doc.find("Toda corrida debe registrar el contexto necesario para reproducirla."), S_D3)
    doc.append_run(doc.find("La aplicabilidad se determina antes de interpretar el valor."), S_D2)

    # E5 — Tabla D.1 fila "Latencia G2A"
    old_def = "Intervalo entre captura o lectura del cuadro y disponibilidad del resultado de inferencia."
    doc.replace_run_text(doc.find(old_def, old_def), old_def, T_G2A_NEW)
    doc.replace_run_text(doc.find("Timestamps monotónicos", "Timestamps monotónicos"), "Timestamps monotónicos", T_CLOCK_NEW)

    # E6 — 17.1.3.3
    p20 = doc.find("Sobre esa base, la evaluación se organiza en dos escenarios", "Sección 17.1.4.4.")
    doc.replace_in_run(p20, "17.1.4.4", "17.1.4.2")

    # B-2' — 17.1.5.1: dos inserciones en la frase de exclusión (re-buscar el párrafo entre ambas)
    start88 = "El primero es la representatividad"
    doc.insert_after_in_run(doc.find(start88), "calzado de seguridad y calzado común", S_B2_A)
    doc.insert_after_in_run(doc.find(start88), "como una capacitación insuficiente.", S_B2_B)

    # T30 — Tabla 30, encabezado: "Rango objetivo orientativo" → "Máximo orientativo" (semántica de la v1.10)
    p513 = doc.find("Rango objetivo orientativo de t_alert-system", "-system")
    doc.replace_in_run(p513, "Rango objetivo orientativo", "Máximo orientativo")

    # B-3 — Tabla 27, nota: antes del marcador
    p382 = doc.find("Nota. TrackingNet y LaSOT se excluyen", "fuentes oficiales]].")
    assert "<w:sectPr" in p382
    doc.insert_before_in_run(p382, "[[PENDIENTE", S_B3)

    # --- verificación
    ET.fromstring(doc.xml.encode("utf8"))
    n1 = len(doc.paras())
    print(f"párrafos {n0} → {n1} (+{n1 - n0}, esperado +5)")
    print("w:ins:", doc.xml.count("<w:ins "), " w:del:", doc.xml.count("<w:del "), " oMath:", doc.xml.count("<m:oMath"),
          " sectPr:", doc.xml.count("<w:sectPr"), " tbl:", doc.xml.count("<w:tbl>"), " comentarios:", doc.xml.count("commentRangeStart"))
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
