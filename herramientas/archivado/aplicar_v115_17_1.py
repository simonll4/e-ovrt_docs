#!/usr/bin/env python3
"""v1.15 de §17.1 = v1.11 + conjunto acumulado de la v1.14 + reescritura de §17.1.8→17.1.11 y Anexos
C/D + mecánicos de §17.1.6, todo como CAMBIOS CONTROLADOS (w:ins / w:del sin aceptar, autor Claude).

Decisiones del usuario (analisis-17-1-8-anexos.md §7, todas aprobadas el 2026-09-03):
  D-A  fundir 17.1.8.1 · 17.1.9.1/.2 · 17.1.11.1/.2 en sus secciones madre
  D-B  fundir 17.1.10.1/.2 (opción B) y cambiar las tres remisiones internas a "sección 17.1.10"
  D-C  casa del registro mínimo = Tabla D.3 (17.1.7.6 §1 se acorta)
  D-D  cita legal como en §16.6 `(Argentina, 2000, 2015)` + "en línea con los principios de la sección 16.6"
  D-E  Tabla C.2 citada desde 17.1.4.2
  D-F  mecánicos de §17.1.6 (fila truncada Tabla 26 · 3 [[PENDIENTE]] · nota C.3 · SH17 4.0)
  D-G  notación t_alert-system / t_G2A en texto plano (caen los 2 OMML inline de 17.1.11.2)

Regla de oficio: los párrafos que llevan `w:sectPr` (los que preceden a cada tabla apaisada y sus
notas) NUNCA se borran: se reemplaza su contenido. Los títulos de nivel 4 se borran como párrafo
completo (runs + marca de párrafo). No se inserta ningún párrafo nuevo en el tramo final.
"""
from __future__ import annotations
import copy, glob, re, sys, zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
SRC = BASE / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.11.docx"
DST = BASE / "E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.15 (sugerencias sin aceptar).docx"

AUTHOR = "Claude"
DATE = "2026-09-03T09:00:00Z"
NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
      "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
      "w14": "http://schemas.microsoft.com/office/word/2010/wordml"}
for k, v in NS.items():
    ET.register_namespace(k, v)

FONTS = ('<w:rFonts w:ascii="Times New Roman" w:cs="Times New Roman" w:eastAsia="Times New Roman" '
         'w:hAnsi="Times New Roman"/><w:sz w:val="24"/><w:szCs w:val="24"/>')
RPR_RUN = "<w:rPr>" + FONTS + '<w:rtl w:val="0"/></w:rPr>'
_id = [9300]
def nid(): _id[0] += 1; return _id[0]
def tc(tag): return f'<w:{tag} w:id="{nid()}" w:author="{AUTHOR}" w:date="{DATE}"'
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
def ins_run(text, rpr=RPR_RUN): return f'{tc("ins")}><w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:ins>'
def del_run(text, rpr=RPR_RUN): return f'{tc("del")}><w:r>{rpr}<w:delText xml:space="preserve">{esc(text)}</w:delText></w:r></w:del>'
def ppr_inserted(center=False):
    align = '<w:jc w:val="center"/>' if center else '<w:ind w:firstLine="720"/>'
    return '<w:pPr><w:spacing w:line="480" w:lineRule="auto"/>' + align + '<w:rPr>' + tc("ins") + '/>' + FONTS + '</w:rPr></w:pPr>'
def new_para(text): return "<w:p>" + ppr_inserted() + ins_run(text) + "</w:p>"
def new_eq_para(om): return "<w:p>" + ppr_inserted(center=True) + tc("ins") + ">" + om + "</w:ins></w:p>"

# ------------------------------------------------------------------ OMML (plantilla v1.10)
def template_omath():
    cands = glob.glob(str(BASE / "**" / "*Consolidacion_Metodologica_v1.10.docx"), recursive=True)
    assert cands
    x10 = zipfile.ZipFile(cands[0]).read("word/document.xml").decode("utf8")
    hits = [p for p in re.findall(r"<w:p[ >].*?</w:p>", x10, flags=re.S)
            if "".join(re.findall(r"<m:t(?: [^>]*)?>([^<]*)</m:t>", p)).startswith("talert-system ≈ tevidencia")]
    assert len(hits) == 1
    om = ET.fromstring("<root " + " ".join(f'xmlns:{k}="{v}"' for k, v in NS.items()) + ">" + hits[0] + "</root>").find(".//m:oMath", NS)
    assert om is not None
    return om
def mtext(el): return "".join(t.text or "" for t in el.iter(f"{{{NS['m']}}}t"))
def build_eq(terms, first_op="≈"):
    tpl = template_omath(); kids = list(tpl); ssub_tpl, op_tpl = kids[2], kids[3]
    assert mtext(ssub_tpl) == "tevidencia" and mtext(op_tpl).strip() == "+"
    def ssub(term):
        base, sub = term.split("_", 1); el = copy.deepcopy(ssub_tpl)
        el.find("m:e/m:r/m:t", NS).text = base; el.find("m:sub/m:r/m:t", NS).text = sub; return el
    def op(sym): el = copy.deepcopy(op_tpl); el.find("m:t", NS).text = f" {sym} "; return el
    om = copy.deepcopy(tpl)
    for k in list(om): om.remove(k)
    for i, t in enumerate(terms):
        if i == 1: om.append(op(first_op))
        elif i > 1: om.append(op("+"))
        om.append(ssub(t))
    return ET.tostring(om, encoding="unicode")

# ------------------------------------------------------------------ utilidades
def ptext(p): return "".join(re.findall(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", p))
RUN_RE = re.compile(r"<w:r[ >](?:(?!</w:r>).)*</w:r>", re.S)

class Doc:
    def __init__(self, xml): self.xml = xml
    def paras(self): return re.findall(r"<w:p[ >].*?</w:p>", self.xml, flags=re.S)
    def find(self, start, end=None, contains=None):
        hits = [p for p in self.paras() if ptext(p).startswith(start) and (end is None or ptext(p).endswith(end)) and (contains is None or contains in ptext(p))]
        assert len(hits) == 1, (start, len(hits)); assert self.xml.count(hits[0]) == 1
        return hits[0]
    def find_all_containing(self, sub):
        hits = [p for p in self.paras() if sub in ptext(p)]
        for h in hits: assert self.xml.count(h) == 1
        return hits
    def replace(self, old, new):
        assert self.xml.count(old) == 1, old[:80]; self.xml = self.xml.replace(old, new)
    def insert_after(self, para, new_xml): self.replace(para, para + new_xml)
    def append_run(self, para, text):
        assert para.endswith("</w:p>"); self.replace(para, para[:-6] + ins_run(text) + "</w:p>")
    def runs(self, para): return RUN_RE.findall(para)
    def insert_after_run(self, para, run_text, text):
        rs = [r for r in self.runs(para) if ptext(r) == run_text]; assert len(rs) == 1 and para.count(rs[0]) == 1
        self.replace(para, para.replace(rs[0], rs[0] + ins_run(text)))
    def replace_run_text(self, para, run_text, new_text):
        rs = [r for r in self.runs(para) if ptext(r) == run_text]; assert len(rs) == 1 and para.count(rs[0]) == 1, run_text
        rpr = re.search(r"<w:rPr>.*?</w:rPr>", rs[0], flags=re.S).group(0)
        self.replace(para, para.replace(rs[0], del_run(run_text, rpr) + ins_run(new_text, rpr)))
    def _split(self, para, anchor, mode, text):
        rs = [r for r in self.runs(para) if anchor in ptext(r)]; assert len(rs) == 1 and para.count(rs[0]) == 1, anchor
        r = rs[0]; rpr = re.search(r"<w:rPr>.*?</w:rPr>", r, flags=re.S).group(0)
        t = re.search(r"<w:t(?: [^>]*)?>([^<]*)</w:t>", r).group(1); assert t.count(anchor) == 1, anchor
        i = t.index(anchor)
        def run(txt): return f'<w:r>{rpr}<w:t xml:space="preserve">{txt}</w:t></w:r>' if txt else ""
        if mode == "replace": new_r = run(t[:i]) + del_run(anchor, rpr) + ins_run(text, rpr) + run(t[i + len(anchor):])
        elif mode == "before": new_r = run(t[:i]) + ins_run(text, rpr) + run(t[i:])
        elif mode == "after": new_r = run(t[:i + len(anchor)]) + ins_run(text, rpr) + run(t[i + len(anchor):])
        elif mode == "delete": new_r = run(t[:i]) + del_run(anchor, rpr) + run(t[i + len(anchor):])
        self.replace(para, para.replace(r, new_r))
    def replace_in_run(self, para, old, new): self._split(para, old, "replace", new)
    def insert_before_in_run(self, para, anchor, text): self._split(para, anchor, "before", text)
    def insert_after_in_run(self, para, anchor, text): self._split(para, anchor, "after", text)
    def delete_in_run(self, para, old): self._split(para, old, "delete", None)
    def replace_content(self, para, new_text, keep=0):
        """Borra (tracked) todos los runs a partir del índice `keep` y agrega un run insertado. Conserva pPr (y sectPr)."""
        rs = self.runs(para); assert len(rs) > keep, ptext(para)[:60]
        rpr = re.search(r"<w:rPr>.*?</w:rPr>", rs[keep], flags=re.S)
        rpr = rpr.group(0) if rpr else RPR_RUN
        new = para
        for r in rs[keep:]:
            assert new.count(r) >= 1
            dr = r.replace("<w:t>", "<w:delText>").replace("<w:t ", "<w:delText ").replace("</w:t>", "</w:delText>")
            new = new.replace(r, tc("del") + ">" + dr + "</w:del>", 1)
        assert new.endswith("</w:p>"); new = new[:-6] + ins_run(new_text, rpr) + "</w:p>"
        self.replace(para, new)
    def delete_para(self, para):
        """Borra el párrafo completo con control de cambios (runs, oMath y marca de párrafo). Prohibido si lleva sectPr."""
        assert "<w:sectPr" not in para, "no se borra un párrafo con sectPr"
        new = re.sub(r"(<m:oMath>(?:(?!</m:oMath>).)*</m:oMath>)", lambda m: tc("del") + ">" + m.group(1) + "</w:del>", para, flags=re.S)
        def conv(m):
            r = m.group(0).replace("<w:t>", "<w:delText>").replace("<w:t ", "<w:delText ").replace("</w:t>", "</w:delText>")
            return tc("del") + ">" + r + "</w:del>"
        new = RUN_RE.sub(conv, new)
        m = re.search(r"<w:pPr>(.*?)</w:pPr>", new, flags=re.S)
        mark = tc("del") + "/>"
        if m:
            inner = m.group(1)
            if "<w:rPr>" in inner: inner2 = inner.replace("<w:rPr>", "<w:rPr>" + mark, 1)
            else: inner2 = inner + "<w:rPr>" + mark + "</w:rPr>"
            new = new.replace(m.group(0), "<w:pPr>" + inner2 + "</w:pPr>", 1)
        else:
            new = re.sub(r"^(<w:p[^>]*>)", lambda mm: mm.group(1) + "<w:pPr><w:rPr>" + mark + "</w:rPr></w:pPr>", new, count=1)
        self.replace(para, new)

def no_ai_punct(s):
    s2 = re.sub(r"\([^()]*\d{4}[^()]*\)", "", s)   # citas APA exentas
    assert ":" not in s2 and ";" not in s2, s[:90]

# ------------------------------------------------------------------ textos (v1.14)
P_A = ("El nivel de compromiso de una métrica es independiente de su estado de aplicabilidad. Una métrica obligatoria es la que el núcleo del prototipo debe reportar cuando sus precondiciones se cumplen. Una métrica deseable amplía el análisis y su omisión justificada no invalida el protocolo. Un tratamiento conceptual conserva valor metodológico aunque requiera datos o módulos que exceden una corrida determinada. Una métrica se considera exigible cuando responde a la pregunta experimental, dispone de una referencia anotada verificable, el módulo que produce la señal existe, el tramo está suficientemente instrumentado y el costo de anotación o procesamiento es compatible con el alcance del proyecto. Bajo estos criterios una métrica puede estar correctamente definida en el framework y aun así no corresponder en una corrida concreta. Si los recursos experimentales no permiten ejecutar todo el repertorio con la misma profundidad, el núcleo evaluativo queda dado por las métricas obligatorias de los tres niveles y por los diagnósticos mínimos del pipeline.")
P_C = ("Para instrumentar la cadena y estimar la plausibilidad del presupuesto se adopta además un modelo de presupuesto de ingeniería con notación propia, separada de las métricas medidas por hitos. B denota la estimación orientativa de un tramo y W una espera funcional. Los componentes sólo se suman cuando son sucesivos y no se solapan.")
P_D = ("B_captura-host corresponde al tramo capture_to_host de la Tabla 29 y sólo se incluye cuando la fuente aporta una marca de captura confiable. B_identidad corresponde a la identidad temporal cuando está habilitada y B_reglas al cómputo de la evaluación del patrón. B_alerta es una referencia de plausibilidad y no reemplaza a t_alert-system, que se obtiene de los hitos reales del episodio y de la alerta. La latencia vidrio a alerta de un episodio se aproxima entonces a la suma de TTFD y B_alerta. t_alert-system, medida entre hitos del reloj de la fuente, comprende la reacción perceptiva inicial y la ventana funcional, pero no la cola de procesamiento del cuadro que confirma, que se informa por separado mediante capture_to_host y t_G2A. La estimación orientativa que sigue corresponde a B_procesamiento.")
S_BRIDGE = (" El objetivo de t_alert-system de cada severidad debe ser compatible con la ventana de persistencia fijada para sus patrones en la sección 17.1.5.2 y dejar margen para el procesamiento y la variabilidad de la cadena. Los valores orientativos deben recalibrarse antes de utilizarse como criterio de aceptación cuando cambien el modelo, la resolución de entrada, la cadencia o las condiciones de transporte.")
S_D1 = " Las definiciones operativas, el formato de reporte y los criterios de estabilidad de estas medidas se consolidan en la Tabla D.1 del Anexo D."
S_D2 = " Los insumos mínimos que habilitan cada familia de métricas se consolidan en la Tabla D.2 del Anexo D."
S_D3_INLINE = " con los campos mínimos consolidados en la Tabla D.3 del Anexo D."
T_G2A_NEW = "Intervalo entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia. La captura y el transporte hasta el dequeue se informan aparte como capture_to_host."
T_CLOCK_NEW = "Hitos y dominio de reloj declarados"
S_B2_A = " o la presencia de guantes y gafas de protección"
S_B2_B = " También quedan fuera, aunque son preventivamente relevantes, condiciones de escena como la obstrucción de pasillos o la presencia de materiales inestables, que no admiten una definición visual estable para su anotación."
# ------------------------------------------------------------------ textos nuevos (tramo final y anexos)
P8A = "La secuencia experimental busca evitar que decisiones tardías alteren la validez comparativa del estudio. Ninguna fase que modifique el estado del modelo o del conjunto de datos se ejecuta antes de congelar el software relevante, los checkpoints retenidos, el banco de evaluación y la estructura mínima de bitácora. Sobre esa base el protocolo se ordena en las fases sucesivas de la Tabla 33 y no como un conjunto abierto de ensayos."
P8B = "El conjunto de métricas aplicables a cada corrida se fija antes de ejecutarla con las reglas de aplicabilidad de la sección 17.1.7.6. Las métricas temporales y las de seguimiento sólo se exigen cuando la evidencia disponible las habilita."
N33 = "La secuencia expresa dependencias entre fases y no un calendario. El orden y las fechas efectivas de ejecución se documentan en la implementación."
P9A = "La adaptación al dominio se mantiene como una rama comparativa condicionada y no como un requisito para demostrar la viabilidad del enfoque. Adoptarla de antemano convertiría una hipótesis todavía no probada en un supuesto metodológico. La rama sólo se habilita cuando existe soporte de datos suficiente y la comparación puede sostenerse sin romper la integridad del protocolo. Sus condiciones de habilitación son de datos y de protocolo y no de disponibilidad de cómputo. El TN aporta el entrenamiento y el CPN conserva la referencia operativa."
P9B = "La comparación se concentra como máximo en dos candidatos, Grounding DINO y YOLOE, que representan compromisos distintos entre expresividad semántica y eficiencia de inferencia (Liu et al., 2024; Wang et al., 2025). Cuál de ellos se ajusta depende de la factibilidad real de integración, exportación y ejecución sobre el CPN y no sólo de su rendimiento en benchmarks generales."
P9C = "La rama se ejecuta como una jornada experimental completa con criterios prerregistrados, una única línea base, márgenes fijados antes de evaluar y un veredicto determinado por reglas de aceptación declaradas de antemano. La Tabla 34 consolida esa regla de decisión."
N34 = "La regla no prescribe que el ajuste deba ejecutarse. Define cuándo vale la pena hacerlo sin distorsionar el objetivo principal del prototipo."
P10A = "El marco ético-legal del protocolo se apoya en la minimización de datos y en el uso asistivo del sistema. Cuando el proyecto genera material propio para el EBE rigen salvaguardas de finalidad determinada, acceso restringido, retención acotada y ausencia de reconocimiento de identidad personal o tratamiento biométrico, en línea con los principios de la sección 16.6 y con el régimen argentino de protección de datos personales y videovigilancia (Argentina, 2000, 2015)."
P10B = "La interpretación de los resultados descansa en cinco supuestos. El prototipo es un sistema asistivo y una alerta no equivale a una sanción ni a una determinación automática de incumplimiento normativo. La evaluabilidad de varias condiciones depende de variables que el detector no controla del todo, como la escala aparente, el ángulo de cámara, la oclusión o la iluminación. CR-06 presupone una parametrización espacial externa al prompt y no se evalúa como si el lenguaje por sí solo definiera la zona restringida. El EBE valida en entorno controlado o simulado y no en obra real."
P10C = "El quinto supuesto es que la disyunción entre datos de entrenamiento y banco de evaluación sólo es verificable sobre el ajuste propio del trabajo. Los modelos preentrenados de vocabulario abierto provienen de corpus de terceros no inspeccionables, de modo que no puede descartarse que imágenes del banco hayan participado de ese preentrenamiento. Es una condición estructural de toda evaluación de modelos preentrenados y no una particularidad de este protocolo. Por eso las cifras zero-shot se leen como una comparación entre combinaciones bajo condiciones idénticas y no como afirmaciones sobre generalización a material inédito. La Tabla 35 reúne los riesgos metodológicos y operativos que condicionan las instancias siguientes y la mitigación adoptada para cada uno."
P11A = "La consolidación metodológica cierra con un protocolo experimental integrado y ajustado al alcance real del prototipo. El núcleo obligatorio queda en las condiciones de detección directa de Nivel 1, la comparación controlada en DBE se separa de la plausibilidad operativa en EBE, la estrategia de datos evita la filtración entre entrenamiento y evaluación, el framework de métricas se centra en el valor operativo de la alerta y una regla explícita decide cuándo habilitar o descartar la adaptación al dominio."
P11B = "Las instancias siguientes toman estas definiciones como referencia. El análisis y diseño arquitectónico las traduce en una organización técnica y la validación experimental produce resultados sobre las condiciones, los escenarios y las métricas fijadas, con la instrumentación de t_G2A y t_alert-system definida en la sección 17.1.7. En todos los casos debe declararse qué elementos del catálogo se implementaron, cuáles no aplicaron y cuáles permanecieron condicionados. Esa trazabilidad entre definición metodológica, diseño, implementación y validación es el principal resultado de esta parte del proyecto y sostiene su orientación central, que es evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva para el monitoreo de condiciones de riesgo en construcción civil."
NC1 = "En las estrategias indirecta y descompuesta el separador punto y coma indica consultas independientes al modelo y su materialización depende de la sintaxis de cada detector. Para CR-05 y CR-06 no se formulan prompts integrados sino prompts de entidades componentes, y la condición completa se evalúa en el módulo de razonamiento contextual."
NC2 = "Los niveles consignados son candidatos de diseño y se cierran al definir la topología y el espacio físico de prueba, siguiendo la secuencia progresiva de la sección 17.1.3.3."
NC3 = "La secuencia de gestión se describe en la sección 17.1.6.5 y los volúmenes y versiones por fuente en la Tabla 23. El esfuerzo de conversión es directo cuando basta un paso y en dos pasos cuando exige inspección o normalización previa."
S_C2 = " Las variables de sensibilidad candidatas para el EBE se consolidan en la Tabla C.2 del Anexo C."
D2_TOOLS = "Motor de patrones instrumentado, registro interno de alertas, event log del pipeline, bitácora de corrida y scripts de agregación temporal."
D2_OUT = "TTFD, SDR y t_alert-system por episodio. t_alert-notification sólo si existe trayecto instrumentado. Toda métrica sin insumos se declara no aplicable."
N23 = "Los papeles indicados no constituyen una asignación efectiva y son mutuamente excluyentes dentro de una misma comparación principal."
N24 = "Las licencias consignadas son las que declara cada paquete de datos. Cuando la declaración proviene de un repositorio de código, de una publicación o de una copia y no del paquete original, la fuente se mantiene en estado condicional."
N27 = "TrackingNet y LaSOT se excluyen porque corresponden a seguimiento de objeto único. OVT-B se prioriza sobre OV-TAO por su mayor escala. TETA es Track Every Thing Accuracy y se descompone en LocA, ClsA y AssA, que miden localización, clasificación y asociación. Las referencias primarias son Milan et al. (2016) para MOT17 y Liang y Han (2024) para OVT-B."
T26_DEDUP = " en especial en colecciones obtenidas de la Web o mediante contribución distribuida."
T34_R2 = "Se priorizan CR-01 y CR-02. CR-03 y CR-04 quedan fuera del camino ordinario mientras no exista cobertura suficiente."
T34_R2S = "Concentra el ajuste donde puede producir evidencia útil y comparaciones válidas."
T34_R4 = "La variante ajustada debe superar el margen fijado antes de evaluar y no mostrar sólo una ventaja marginal."
T35_R4 = "Sostener el diseño reducido de la sección 17.1.3.3, con la prueba de mayor exigencia sólo sobre la configuración retenida."
for s in (P_A, P_C, P_D, S_BRIDGE, S_D1, S_D2, S_D3_INLINE, T_G2A_NEW, S_B2_A, S_B2_B, P8A, P8B, N33, P9A, P9B, P9C, N34, P10A, P10B, P10C, P11A, P11B, NC1, NC2, NC3, S_C2, D2_TOOLS, D2_OUT, N23, N24, N27, T26_DEDUP, T34_R2, T34_R2S, T34_R4, T35_R4):
    no_ai_punct(s)

# ------------------------------------------------------------------ aplicar
def main():
    zin = zipfile.ZipFile(SRC); doc = Doc(zin.read("word/document.xml").decode("utf8")); n0 = len(doc.paras())

    # ===== conjunto v1.14 =====
    doc.insert_after(doc.find("Cada métrica debe acompañarse de un estado explícito.", "como resultado omitido."), new_para(P_A))
    doc.replace_in_run(doc.find("Predicciones exportadas y métricas primarias calculadas.", "calculadas."), "primarias", "obligatorias")
    p507 = doc.find("El tramo computacional reúne el preprocesamiento"); assert doc.xml.find(p507) < doc.xml.find(doc.find("Con el perfil de hardware de referencia"))
    eq1 = build_eq(["B_procesamiento", "B_captura-host", "B_preprocesamiento", "B_inferencia", "B_identidad", "B_reglas"]); eq2 = build_eq(["B_alerta", "W_evidencia", "B_procesamiento"])
    doc.insert_after(p507, new_para(P_C) + new_eq_para(eq1) + new_eq_para(eq2) + new_para(P_D))
    p509 = doc.find("La latencia de alerta incorpora además la ventana de evidencia", "respuesta perceptiva inicial."); assert "<w:sectPr" in p509; doc.append_run(p509, S_BRIDGE)
    doc.insert_after_run(doc.find("El banco de evaluación queda definido antes de entrenar", "ni aumento de datos."), "hiperparámetros", ", selección de checkpoints")
    doc.append_run(doc.find("La viabilidad operativa se caracteriza mediante la cadencia efectiva"), S_D1)
    doc.append_run(doc.find("La aplicabilidad se determina antes de interpretar el valor."), S_D2)
    # D-C: 17.1.7.6 §1 → dos oraciones con remisión a la Tabla D.3
    p534 = doc.find("Toda corrida debe registrar el contexto necesario para reproducirla.")
    mid = re.search(r"\. Como mínimo, se conservan .*? identidad temporal\.", ptext(p534)).group(0)
    doc.replace_in_run(p534, mid, S_D3_INLINE)
    old_def = "Intervalo entre captura o lectura del cuadro y disponibilidad del resultado de inferencia."
    doc.replace_run_text(doc.find(old_def, old_def), old_def, T_G2A_NEW)
    doc.replace_run_text(doc.find("Timestamps monotónicos", "Timestamps monotónicos"), "Timestamps monotónicos", T_CLOCK_NEW)
    doc.replace_in_run(doc.find("Sobre esa base, la evaluación se organiza en dos escenarios", "Sección 17.1.4.4."), "17.1.4.4", "17.1.4.2")
    s88 = "El primero es la representatividad"
    doc.insert_after_in_run(doc.find(s88), "calzado de seguridad y calzado común", S_B2_A)
    doc.insert_after_in_run(doc.find(s88), "como una capacitación insuficiente.", S_B2_B)
    doc.replace_in_run(doc.find("Rango objetivo orientativo de t_alert-system", "-system"), "Rango objetivo orientativo", "Máximo orientativo")

    # ===== D-F: mecánicos de §17.1.6 =====
    doc.replace_run_text(doc.find("construction_site_safety. Versión o fecha de acceso por consignar."), "construction_site_safety. Versión o fecha de acceso por consignar.", "construction_site_safety. Roboflow Universe, versión 27.")
    doc.replace_run_text(doc.find("ppe_siabar. Versión o fecha de acceso por consignar."), "ppe_siabar. Versión o fecha de acceso por consignar.", "ppe_siabar. Roboflow Universe, versión 1.")
    doc.replace_content(doc.find("Nota. Los papeles indicados no constituyen"), N23, keep=1)
    p306 = doc.find("Nota. [[PENDIENTE: verificar las licencias"); assert "<w:sectPr" in p306; doc.replace_content(p306, N24, keep=1)
    doc.insert_after_in_run(doc.find("La licencia CC BY-NC-SA y el predominio"), "CC BY-NC-SA", " 4.0")
    doc.append_run(doc.find("Cuando se combinan fuentes, se verifican duplicados y casi duplicados,", "casi duplicados,"), T26_DEDUP)
    p382 = doc.find("Nota. TrackingNet y LaSOT se excluyen", "fuentes oficiales]]."); assert "<w:sectPr" in p382
    rs382 = doc.runs(p382); assert ptext(rs382[0]) == "Nota" and ptext(rs382[1]) == ". "; doc.replace_content(p382, N27, keep=2)
    # D-E: Tabla C.2 citada desde 17.1.4.2
    p62 = doc.find("La relación entre ambos escenarios no es de reemplazo.", "variable experimental."); assert "<w:sectPr" in p62; doc.append_run(p62, S_C2)
    # D-B: remisiones a 17.1.10.1 → 17.1.10 (las tres del cuerpo; la de la Tabla 35 se hace abajo)
    doc.replace_in_run(doc.find("Cuando una condición brechada permanezca dentro del alcance exploratorio"), "17.1.10.1", "17.1.10")
    doc.replace_in_run(doc.find("El uso de los datos se limita a investigación académica"), "17.1.10.1", "17.1.10")

    # ===== 17.1.8 =====
    doc.delete_para(doc.find("17.1.8.1. Secuencia general del protocolo"))
    doc.replace_content(doc.find("La secuencia experimental busca evitar que decisiones tardías"), P8A)
    p543 = doc.find("En cada corrida, el conjunto de métricas aplicables"); assert "<w:sectPr" in p543; doc.replace_content(p543, P8B)
    doc.replace_in_run(doc.find("Medir cada modelo candidato en zero-shot"), "test set", "banco de evaluación")
    doc.replace_in_run(doc.find("Medir tG2A, FPS"), "tG2A", "t_G2A")
    doc.replace_in_run(doc.find("Comparación válida respecto de baseline y test compartido."), "test compartido", "banco de evaluación compartido")
    p578 = doc.find("Nota. La baseline zero-shot y el test congelado"); assert "<w:sectPr" in p578; doc.replace_content(p578, N33, keep=1)

    # ===== 17.1.9 =====
    doc.delete_para(doc.find("17.1.9.1. Criterio metodológico general"))
    doc.delete_para(doc.find("17.1.9.2. Candidatos de comparación y condiciones de decisión"))
    doc.replace_content(doc.find("La adaptación al dominio se mantiene como una rama comparativa progresiva"), P9A)
    p583 = doc.find("En términos operativos, la comparación se concentrará"); assert "<w:sectPr" in p583; doc.replace_content(p583, P9B)
    doc.replace_content(doc.find("La rama se define para su ejecución como una jornada"), P9C)
    doc.replace_in_run(doc.find("Ningún ajuste se evalúa sin baseline zero-shot previa sobre el mismo test."), "mismo test", "mismo banco de evaluación")
    doc.replace_run_text(doc.find("Se priorizan CR-01 y CR-02; CR-03"), ptext(doc.find("Se priorizan CR-01 y CR-02; CR-03")), T34_R2)
    doc.replace_run_text(doc.find("El ajuste debe concentrarse donde puede producir"), ptext(doc.find("El ajuste debe concentrarse donde puede producir")), T34_R2S)
    doc.replace_in_run(doc.find("El test set debe ser compartido y permanecer congelado."), "test set", "banco de evaluación")
    doc.replace_run_text(doc.find("La variante ajustada debe mostrar una mejora"), ptext(doc.find("La variante ajustada debe mostrar una mejora")), T34_R4)
    p605 = doc.find("Nota. La regla no prescribe que el fine-tuning"); assert "<w:sectPr" in p605; doc.replace_content(p605, N34, keep=1)

    # ===== 17.1.10 =====
    doc.delete_para(doc.find("17.1.10.1. Política de minimización y uso asistivo"))
    doc.delete_para(doc.find("17.1.10.2. Supuestos de interpretación"))
    doc.replace_content(doc.find("El marco ético-legal del proyecto se apoya"), P10A)
    p610 = doc.find("También conviene fijar con claridad los supuestos"); assert "<w:sectPr" in p610; doc.replace_content(p610, P10B)
    p611 = doc.find("Quinto, la disyunción entre datos de entrenamiento"); assert "<w:sectPr" in p611; doc.replace_content(p611, P10C)
    doc.replace_run_text(doc.find("Sostener un diseño reducido con condición base"), ptext(doc.find("Sostener un diseño reducido con condición base")), T35_R4)
    doc.replace_in_run(doc.find("Aplicar las salvaguardas de la Sección 17.1.10.1"), "Sección 17.1.10.1", "sección 17.1.10")

    # ===== 17.1.11 =====
    doc.delete_para(doc.find("17.1.11.1. Cierre del alcance metodológico"))
    doc.delete_para(doc.find("17.1.11.2. Articulación con las instancias de diseño e implementación"))
    doc.replace_content(doc.find("La consolidación metodológica queda cerrada con un protocolo"), P11A)
    doc.replace_content(doc.find("Las definiciones consolidadas en esta instancia orientan"), P11B)
    p638 = doc.find("Esta consolidación distribuye sus salidas"); assert p638.count("<m:oMath") == 2; doc.delete_para(p638)
    doc.delete_para(doc.find("Estas definiciones preservan el carácter experimental"))

    # ===== Anexos =====
    pC1 = doc.find("Nota. Las estrategias"); assert "<w:sectPr" in pC1; doc.replace_content(pC1, NC1, keep=1)
    pC2 = doc.find("Nota. El EBE se organiza de manera secuencial"); assert "<w:sectPr" in pC2; doc.replace_content(pC2, NC2, keep=1)
    pC3 = doc.find("Nota. La secuencia de gestión"); assert "<w:sectPr" in pC3; doc.replace_content(pC3, NC3, keep=1)
    doc.replace_run_text(doc.find("Motor de evaluación de patrones instrumentado;"), ptext(doc.find("Motor de evaluación de patrones instrumentado;")), D2_TOOLS)
    doc.replace_run_text(doc.find("TTFD, SDR y t_alert-system por evento;"), ptext(doc.find("TTFD, SDR y t_alert-system por evento;")), D2_OUT)

    # ===== verificación y escritura =====
    ET.fromstring(doc.xml.encode("utf8"))
    n1 = len(doc.paras())
    print(f"párrafos {n0} → {n1} (+{n1 - n0}, esperado +5)")
    print("w:ins:", doc.xml.count("<w:ins "), " w:del:", doc.xml.count("<w:del "), " oMath:", doc.xml.count("<m:oMath"), " sectPr:", doc.xml.count("<w:sectPr"), " tbl:", doc.xml.count("<w:tbl>"), " comentarios:", doc.xml.count("commentRangeStart"))
    if DST.exists(): DST.unlink()
    with zipfile.ZipFile(DST, "w") as zout:
        for it in zin.infolist():
            data = zin.read(it.filename)
            if it.filename == "word/document.xml": data = doc.xml.encode("utf8")
            zout.writestr(it, data, compress_type=zipfile.ZIP_DEFLATED)
    print("escrito:", DST.name, DST.stat().st_size, "bytes")
    return 0

if __name__ == "__main__":
    sys.exit(main())
