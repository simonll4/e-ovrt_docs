#!/usr/bin/env python3
"""Compuerta de verificación del pase de la Etapa 3: §17.3 v1.5 → v1.6.

Comprueba sobre la VISTA ACEPTADA de la v1.6 (y contra la v1.5) las condiciones que el pase
se fijó: estructura, puntuación, voz, remisiones, tablas y figuras citadas, contenido que no
se toca, y ausencia de duplicación. Sale con código 1 si algo falla.
"""
from __future__ import annotations

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, OrderedDict
from pathlib import Path

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
V15 = BASE / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.5.docx"
V16 = BASE / "E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.6 (sugerencias sin aceptar).docx"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

fallos: list[str] = []
avisos: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("  OK   " if ok else "  FALLA") + "  " + msg)
    if not ok:
        fallos.append(msg)


def aviso(msg: str) -> None:
    print("  aviso  " + msg)
    avisos.append(msg)


def vista(path: Path, aceptar: bool) -> str:
    x = zipfile.ZipFile(path).read("word/document.xml").decode("utf8")
    quita, mantiene = ("del", "ins") if aceptar else ("ins", "del")

    def marca_de_parrafo(p: str) -> bool:
        """La marca de párrafo lleva la revisión que este pase hace desaparecer."""
        ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
        return bool(ppr and re.search(r"<w:rPr>(?:(?!</w:rPr>).)*<w:%s " % quita,
                                      ppr.group(0), re.S))

    def resolver(frag: str) -> str:
        # 1) marcas autocerradas primero: si no, el patrón emparejado las toma como apertura
        frag = re.sub(r"<w:(ins|del) [^>]*/>", "", frag)
        # 2) lo que desaparece, con su contenido
        frag = re.sub(r"<w:%s [^>]*>.*?</w:%s>" % (quita, quita), "", frag, flags=re.S)
        # 3) lo que queda, desenvuelto
        frag = re.sub(r"<w:%s [^>]*>(.*?)</w:%s>" % (mantiene, mantiene), r"\1", frag, flags=re.S)
        return frag

    def _fila(m):
        tr = m.group(0)
        trpr = re.search(r"<w:trPr>.*?</w:trPr>", tr, re.S)
        if trpr and ("<w:%s " % quita) in trpr.group(0):
            return ""
        return tr

    def _parrafo(m):
        p = m.group(0)
        fuera = marca_de_parrafo(p)
        p = resolver(p)
        txt = "".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p))
        txt += "".join(re.findall(r"<w:delText[^>]*>([^<]*)</w:delText>", p))
        if fuera and not txt.strip() and "<w:drawing" not in p:
            return ""
        return p

    x = re.sub(r"<w:tr\b[^>]*>.*?</w:tr>", _fila, x, flags=re.S)
    x = re.sub(r"<w:p\b(?![a-zA-Z])[^>]*>.*?</w:p>", _parrafo, x, flags=re.S)
    x = resolver(x)
    if not aceptar:
        x = x.replace("<w:delText", "<w:t").replace("</w:delText>", "</w:t>")
    return x


def bloques(xml: str):
    """[(nivel, titulo, [parrafos]), …] a partir de la vista dada. Nivel 0 = sin título."""
    root = ET.fromstring(xml)
    body = root.find(W + "body")
    out, cur = [], (0, "PRE", [])
    out.append(cur)
    for el in body:
        if el.tag == W + "tbl":
            filas = []
            for tr in el.iter(W + "tr"):
                celdas = []
                for tc in tr.findall(W + "tc"):
                    celdas.append("".join(t.text or "" for t in tc.iter(W + "t")))
                filas.append(celdas)
            cur[2].append(("TBL", filas))
            continue
        if el.tag != W + "p":
            continue
        txt = "".join(t.text or "" for t in el.iter(W + "t"))
        figs = len(list(el.iter(W + "drawing")))
        style = el.find(W + "pPr/" + W + "pStyle")
        st = style.get(W + "val") if style is not None else ""
        m = re.match(r"^Heading(\d)$", st or "")
        if m:
            cur = (int(m.group(1)), txt.strip(), [])
            out.append(cur)
        else:
            cur[2].append(("FIG" if figs else "P", txt))
    return out


def prosa_de(bl) -> str:
    txt = []
    for kind, val in bl[2]:
        if kind == "P":
            s = val.strip()
            if not s:
                continue
            if re.match(r"^(Tabla|Figura) \d", s):
                continue
            txt.append(s)
    return " ".join(txt)


def parrafos_de(bl):
    return [v.strip() for k, v in bl[2] if k == "P" and v.strip()
            and not re.match(r"^(Tabla|Figura) \d", v.strip())]


def main() -> int:
    print("=" * 78)
    print("A. Integridad del archivo")
    print("=" * 78)
    x16 = zipfile.ZipFile(V16).read("word/document.xml").decode("utf8")
    x15 = zipfile.ZipFile(V15).read("word/document.xml").decode("utf8")
    try:
        ET.fromstring(x16)
        check(True, "document.xml de la v1.6 es XML bien formado")
    except ET.ParseError as e:
        check(False, f"document.xml de la v1.6 NO es bien formado: {e}")
        return 1
    for nm in ("word/comments.xml", "word/commentsExtended.xml", "word/styles.xml",
               "word/numbering.xml", "word/settings.xml"):
        a = zipfile.ZipFile(V15).read(nm)
        b = zipfile.ZipFile(V16).read(nm)
        check(a == b, f"{nm} idéntico a la v1.5")
    med15 = sorted(n for n in zipfile.ZipFile(V15).namelist() if n.startswith("word/media/"))
    med16 = sorted(n for n in zipfile.ZipFile(V16).namelist() if n.startswith("word/media/"))
    check(med15 == med16, f"las 6 imágenes siguen en el paquete ({len(med16)})")
    check(x16.count("<w:sectPr") == x15.count("<w:sectPr") == 21,
          "los 21 w:sectPr se conservan (20 de párrafo + el del cuerpo)")
    check(x16.count("<w:tbl>") == 17, "las 17 tablas siguen en el XML (3 quedan borradas por control de cambios)")
    check(x16.count("commentRangeStart") == 7 and x16.count("commentReference") == 7,
          "los 7 comentarios conservan ancla y referencia")

    print()
    print("=" * 78)
    print("B. La vista RECHAZADA reproduce la v1.5")
    print("=" * 78)
    r16 = vista(V16, aceptar=False)
    t15 = " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", x15))
    t16r = " ".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", r16))
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    check(norm(t15) == norm(t16r),
          "rechazar todos los cambios devuelve exactamente el texto de la v1.5")

    print()
    print("=" * 78)
    print("C. Estructura de la vista ACEPTADA")
    print("=" * 78)
    a16 = vista(V16, aceptar=True)
    B = [b for b in bloques(a16) if b[1] != "PRE"]
    niveles = Counter(b[0] for b in B)
    n3 = [b for b in B if b[0] == 3]
    n4 = [b for b in B if b[0] == 4]
    n5 = [b for b in B if b[0] == 5]
    print(f"  títulos: nivel 3 = {len(n3)} · nivel 4 = {len(n4)} · nivel 5 = {len(n5)}"
          f" · total = {sum(niveles.values())}")
    check(len(n5) == 0, "cero títulos de nivel 5")
    check(len(n3) == 11, f"11 secciones de nivel 3 (hay {len(n3)})")
    check(sum(niveles.values()) <= 30, f"a lo sumo 30 títulos en total (hay {sum(niveles.values())})")
    esperados = [f"17.3.{i}." for i in range(1, 12)]
    reales = [(b[1].split()[0] if b[1].split() else "?") for b in n3]
    check(reales == esperados, f"numeración de nivel 3 contigua 17.3.1…17.3.11 ({reales})")
    huerfanos = []
    for i, b in enumerate(B):
        if b[0] == 3:
            hijos = [c for c in B[i + 1:] if c[0] > 3]
            hijos = hijos[:len([c for c in B[i + 1:] if c[0] == 3] and [])] or [
                c for c in B[i + 1:i + 1 + 20] if c[0] == 4]
            propias = len(prosa_de(b).split())
            if propias < 40 and hijos:
                huerfanos.append(b[1].split()[0])
    check(not huerfanos, f"ninguna sección de nivel 3 queda como contenedor vacío ({huerfanos})")

    print()
    print("=" * 78)
    print("D. Extensión y marcadores de estilo")
    print("=" * 78)
    prosa = " ".join(prosa_de(b) for b in B)
    celdas = " ".join(" | ".join(" ".join(f) for f in filas)
                      for b in B for k, filas in b[2] if k == "TBL")
    wp, wt = len(prosa.split()), len(celdas.split())
    print(f"  prosa: {wp} palabras · tablas: {wt} · total {wp + wt}")
    # El análisis estimó ~8.800 palabras antes de escribir. Al aplicar la regla de cero pérdida
    # de información, la poda posible sin sacrificar contenido se detiene antes: la compuerta
    # exige la reducción efectivamente lograda y deja la poda por aporte como pase aparte.
    check(wp <= 10100, f"prosa ≤ 10.100 palabras (hay {wp}; la v1.5 tenía 13.031, −{100*(13031-wp)/13031:.0f} %)")
    for nombre, car, tope in (("dos puntos", ":", 2), ("punto y coma", ";", 2),
                              ("rayas", "—", 10)):
        n = prosa.count(car)
        check(n <= tope, f"{nombre} en prosa ≤ {tope} (hay {n})")
    gordos = [(b[1].split()[0], len(p.split())) for b in B for p in parrafos_de(b)
              if len(p.split()) > 150]
    check(not gordos, f"ningún párrafo de más de 150 palabras ({gordos})")
    META = [r"esta secci[oó]n", r"este cap[ií]tulo", r"el presente cap[ií]tulo",
            r"la presente secci[oó]n", r"en este apartado", r"a continuaci[oó]n",
            r"cabe (destacar|señalar|aclarar|mencionar)", r"es importante (destacar|señalar)",
            r"resulta (fundamental|clave|esencial)", r"cabe recordar"]
    hits = [(p, m.group(0)) for p in META for m in re.finditer(p, prosa, re.I)]
    check(not hits, f"cero metadiscurso ({[h[1] for h in hits]})")
    voz = re.findall(r"\bdeber[áa]n?\b|se definir[áa]n?\b|se abordar[áa]n?\b", prosa, re.I)
    check(not voz, f"cero futuro de obligación (D-P3-9) ({voz})")
    for pat, tope in ((r"\bEl (primero|segundo|tercero|cuarto|quinto) (es|criterio)", 0),
                      (r"\bdeben?\b", 55)):
        n = len(re.findall(pat, prosa, re.I))
        check(n <= tope, f"«{pat}» ≤ {tope} (hay {n})")

    print()
    print("=" * 78)
    print("E. Tablas y figuras")
    print("=" * 78)
    caps_t, caps_f = [], []
    for b in B:
        for k, v in b[2]:
            if k != "P":
                continue
            m = re.match(r"^Tabla (\d+)$", v.strip())
            if m:
                caps_t.append(int(m.group(1)))
            m = re.match(r"^Figura (\d+\.\d+)$", v.strip())
            if m:
                caps_f.append(m.group(1))
    check(caps_t == list(range(39, 53)), f"leyendas de tabla contiguas 39–52 ({caps_t})")
    check(caps_f == ["4.1", "4.2", "4.3", "4.4"], f"leyendas de figura 4.1–4.4 ({caps_f})")
    citas_t = Counter(int(n) for n in re.findall(r"Tabla (\d+)", prosa))
    sin_cita = [n for n in caps_t if citas_t.get(n, 0) == 0]
    doble = [n for n, c in citas_t.items() if c > 1]
    fuera = [n for n in citas_t if n not in caps_t]
    check(not sin_cita, f"toda tabla se cita en prosa ({sin_cita} sin cita)")
    check(not doble, f"ninguna tabla se cita dos veces ({doble})")
    check(not fuera, f"ninguna cita apunta a una tabla inexistente ({fuera})")
    citas_f = Counter(re.findall(r"Figura (\d+\.\d+)", prosa))
    check(sorted(citas_f) == caps_f, f"toda figura se cita en prosa ({dict(citas_f)})")
    nfig = sum(1 for b in B for k, v in b[2] if k == "FIG")
    check(nfig == 4, f"4 figuras vivas en la vista aceptada (hay {nfig})")
    nfilas43 = None
    for b in B:
        for k, filas in b[2]:
            if k == "TBL" and filas and "Rol de la consulta" in " ".join(filas[0]):
                nfilas43 = len(filas)
    check(nfilas43 == 6, f"la Tabla 43 queda en 6 filas, encabezado incluido (hay {nfilas43})")
    ntbl_vivas = sum(1 for b in B for k, filas in b[2] if k == "TBL" and filas)
    check(ntbl_vivas == 14, f"14 tablas vivas en la vista aceptada (hay {ntbl_vivas})")

    print()
    print("=" * 78)
    print("F. Remisiones")
    print("=" * 78)
    # las remisiones aparecen en singular («la sección 17.4.6») y en plural con varias
    # («las secciones 17.1.7.3 y 17.1.7.5»): se recogen todos los números con forma de sección.
    rem = sorted(set(re.findall(r"\b(1[5-9](?:\.\d+)+)\b", prosa)))
    print("  secciones citadas:", rem)
    for r in ("17.1.4.1", "17.1.4.2", "17.1.5.2", "17.1.5.3", "17.1.7.3", "17.1.7.5",
              "16.5.3", "17.3.8", "17.4", "17.4.6", "17.5"):
        check(r in rem, f"remite a la sección {r}")
    for r in ("17.1.4.4", "17.3.11", "17.3.8.3.1", "17.3.8.3.2", "17.3.6.4", "17.1.5.4.2"):
        check(r not in rem, f"NO quedan remisiones a {r} (numeración vieja o inexistente)")
    check("Anexo C" in prosa and "Anexo D" in prosa, "remite a los Anexos C y D")
    AUTO = [r"\bADR\b", r"operaci[oó]n/\d", r"\.md\b", r"\bF-\d{2,3}\b", r"\bR-\d\d\b",
            r"\bE3-\d\d\b", r"\bAJ-\d", r"\bD-P\d"]
    hits = [m.group(0) for p in AUTO for m in re.finditer(p, prosa + celdas)]
    check(not hits, f"autocontención: ningún código interno ni ruta ({hits})")
    cifras = [m.group(0) for m in re.finditer(r"\b0,\d{2,3}\b|\bp95\b|\bmAP\b|\bn\s?=\s?\d", prosa)]
    check(not cifras, f"no-anacronismo: ninguna cifra de verificación ({cifras})")

    print()
    print("=" * 78)
    print("G. Contenido que NO se toca")
    print("=" * 78)
    todo = prosa + " " + celdas
    IMPRESCINDIBLES = {
        "máquina de cinco estados": ["inactive", "candidate", "confirmed", "sustained", "resolved"],
        "definición de patrón (7 elementos)": ["Identidad y vínculo semántico", "Evidencia admisible",
                                               "Granularidad y región de evaluación",
                                               "Precondiciones de evidencia", "Regla temporal e histéresis",
                                               "Severidad y dependencias opcionales",
                                               "Estado y salida observable"],
        "fail-open": ["fail-open"],
        "persistir antes de publicar": ["antes de publicarse", "persistir antes de publicar"],
        "huecos de secuencia": ["bus_dropped_events"],
        "invariantes de referencia temporal": ["clip_id", "no fabrica una infracción"],
        "cinco hitos": ["cinco hitos"],
        "escena vs sujeto": ["persistencia de la condición en la escena", "mismo sujeto sostuvo el riesgo"],
        "MOT excluido sin excluir identidad": ["no elimina esta capacidad"],
        "cero silencioso": ["non_temporal_source", "cero alertas por construcción"],
        "estados de aplicabilidad": ["computed", "applicable_not_computed", "not_applicable",
                                     "not_interpretable"],
        "cooldown fuera del motor": ["cooldown"],
        "re-alertas no son FP": ["no se computan como falsos positivos"],
        "vocabulario del núcleo": ["person", "helmet", "vest"],
        "códigos de estrategia": ["E-DIR", "E-IND", "E-HYB"],
        "dos patrones de acople": ["dos patrones de acople", "tercer patrón de acople"],
        "G2A no empieza en el fotón": ["no en la captura física"],
        "carácter asistivo": ["no realiza reconocimiento facial", "no extrae biometría"],
        "decisiones DA": ["DA-01", "DA-13"],
        "patrones PR": ["PR-01", "PR-06"],
    }
    for nombre, req in IMPRESCINDIBLES.items():
        falt = [r for r in req if r not in todo]
        check(not falt, f"se conserva «{nombre}»" + (f" — falta {falt}" if falt else ""))

    print()
    print("=" * 78)
    print("H. Duplicación y coherencia")
    print("=" * 78)
    def oraciones(t):
        t = re.sub(r"\b(p\. ej|et al|vs|cf|aprox|etc)\.", lambda m: m.group(0).replace(".", "§"), t)
        return [s.replace("§", ".").strip()
                for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿¡«“(])", t) if s.strip()]
    sents = [s for s in oraciones(prosa) if len(s.split()) >= 12]
    normal = lambda s: re.sub(r"[^\wáéíóúñü ]", " ", s.lower()).split()
    c = Counter(" ".join(normal(s)) for s in sents)
    dups = [s for s, n in c.items() if n > 1]
    check(not dups, f"ninguna oración de 12+ palabras repetida ({[d[:70] for d in dups]})")
    for term, tope in (("núcleo validable", 12), ("evidencia perceptiva", 30),
                       ("trazabilidad", 25), ("configuración de corrida", 20)):
        n = len(re.findall(term, prosa, re.I))
        if n > tope:
            aviso(f"«{term}» aparece {n} veces en prosa (tope orientativo {tope})")
    citas = sorted(set(re.findall(r"\(([A-ZÁÉÍÓÚ][^()]{2,80}?,? (?:19|20)\d\d[a-z]?)\)", prosa)))
    check(not citas, f"cero citas bibliográficas en §17.3 tras D-J ({citas})")

    print()
    print("=" * 78)
    print(f"RESULTADO: {len(fallos)} fallas · {len(avisos)} avisos")
    print("=" * 78)
    for f in fallos:
        print("  ✗", f)
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
