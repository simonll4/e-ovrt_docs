#!/usr/bin/env python3
"""Compuerta del pase de las Etapas 4 y 5: §17.4 v1.6 → v1.7 y §17.5 v1.3 → v1.4.

Verifica sobre la VISTA ACEPTADA lo que el pase se fijó, y sobre la VISTA RECHAZADA la
propiedad que hace segura la entrega: rechazar todos los cambios devuelve exactamente el
documento de partida. Sale con código 1 si algo falla.

    python3 herramientas/verificar_pase_17_4_17_5.py
"""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

BASE = Path("/home/simonll4/projects/docs/informe/entregable/desarrollando")
DOCS = {
    "17.4": (BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.6.docx",
             BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.7 (sugerencias sin aceptar).docx"),
    "17.5": (BASE / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.3.docx",
             BASE / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.4 (sugerencias sin aceptar).docx"),
}

fallos: list[str] = []


def check(ok: bool, msg: str) -> None:
    print(("  OK    " if ok else "  FALLA ") + msg)
    if not ok:
        fallos.append(msg)


# --------------------------------------------------------------- vistas aceptada y rechazada
def vista(path: Path, aceptar: bool) -> str:
    x = zipfile.ZipFile(path).read("word/document.xml").decode("utf8")
    quita, mantiene = ("del", "ins") if aceptar else ("ins", "del")

    def marca_de_parrafo(p: str) -> bool:
        ppr = re.search(r"<w:pPr>.*?</w:pPr>", p, re.S)
        return bool(ppr and re.search(r"<w:rPr>(?:(?!</w:rPr>).)*<w:%s " % quita,
                                      ppr.group(0), re.S))

    def resolver(frag: str) -> str:
        frag = re.sub(r"<w:(ins|del) [^>]*/>", "", frag)                       # autocerradas primero
        frag = re.sub(r"<w:%s [^>]*>.*?</w:%s>" % (quita, quita), "", frag, flags=re.S)
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


def split_units(body: str):
    units, i = [], 0
    while i < len(body):
        m = re.search(r"<w:(p|tbl)\b", body[i:])
        if not m:
            break
        kind = m.group(1)
        start = i + m.start()
        tag_end = body.index(">", start)
        if body[tag_end - 1] == "/":
            units.append((kind, body[start:tag_end + 1]))
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
        units.append((kind, body[start:j]))
        i = j
    return units


def texto(x: str) -> str:
    return "".join(re.findall(r"<w:t(?: [^>]*)?>(.*?)</w:t>", x, re.S))


CODIGO = re.compile(r'^(\{|class |runs/|\s*")')


def desglose(xml: str):
    """(párrafos de prosa, párrafos de código, textos de tabla, títulos)."""
    body = xml[xml.index("<w:body>") + 8: xml.rindex("</w:body>")]
    prosa, codigo, tablas, titulos = [], [], [], []
    for kind, raw in split_units(body):
        t = texto(raw).strip()
        if kind == "tbl":
            tablas.append(texto(raw))
            continue
        if not t:
            continue
        if re.search(r'<w:pStyle w:val="Heading\d"/>', raw):
            titulos.append((int(re.search(r"Heading(\d)", raw).group(1)), t))
            continue
        (codigo if CODIGO.match(t) else prosa).append(t)
    return prosa, codigo, tablas, titulos


def oraciones(p: str):
    t = re.sub(r"(\d)\.(\d)", r"\1<D>\2", p)
    return [s.replace("<D>", ".") for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÑ¿«\"(])", t)]


PROHIBIDOS = {
    "17.4": [
        (r"sección 17\.3\.8\.4", "la remisión a una subsección que ya no existe"),
        (r"primero la distribución", "el orden de arranque falso"),
        (r"La presente sección|[Ll]o que sigue|del presente trabajo|[Ee]ste capítulo", "metadiscurso"),
        (r"\bopen-vocabulary\b", "«open-vocabulary» en vez de vocabulario abierto"),
        (r"\blive\b|\boffline\b|\breplay\b", "anglicismos de camino de ejecución"),
        (r"\brunner\b|\bwebconsole\b|\bbackend\b|\bendpoints?\b", "anglicismos de plataforma"),
        (r"\bcontratos preliminares\b", "«contratos preliminares», que el diseño llama mínimos"),
        (r"17\.4\.9|17\.4\.10|17\.4\.11", "numeración de subsección anterior a la fusión"),
    ],
    "17.5": [
        (r"17\.5\.8", "la síntesis eliminada"),
        (r"person-frames", "«person-frames» sin traducir"),
        (r"AP@0,5", "una tercera notación de la métrica de detección"),
        (r"\bin-domain\b", "«in-domain» sin traducir"),
        (r"50\s*[–-]\s*250", "un presupuesto de latencia propio en vez de la remisión"),
        (r"La presente sección", "metadiscurso"),
        (r"L1\s*[-–]\s*L8", "las limitaciones citadas por código en vez de declaradas"),
    ],
}

EXIGIDOS = {
    "17.4": [
        (r"control, después el módulo de distribución y por último el plano de medios",
         "el orden de arranque real (H2-01)"),
        (r"unidad de conteo del tramo es la notificación", "el detalle del ledger (E4-31)"),
        (r"2\.946 imágenes", "la desviación del rango de entrenamiento (H2-02)"),
        (r"sección 17\.1\.4\.1", "la remisión a la infraestructura (comentario 1)"),
        (r"espera a que haya un suscriptor antes de emitir", "la garantía del publicador"),
        (r"Figura 4\.5", "la figura renumerada"),
    ],
    "17.5": [
        (r"0,704 a 0,622", "el costo medido del vocabulario activo (AJ-5.14)"),
        (r"no se ejecutó sobre las combinaciones finalistas", "la no ejecución del sub-experimento"),
        (r"Ocho limitaciones acotan", "la declaración de las ocho limitaciones (D-H)"),
        (r"3 alertas", "la celda restaurada de la tabla de tiempo real"),
        (r"MM-Grounding DINO", "la familia descartada, nombrada como en §17.4"),
    ],
}

ESTRUCTURA = {"17.4": (9, 0), "17.5": (8, 0)}          # títulos, títulos de nivel 4 o más
TABLAS = {"17.4": [56, 57, 58, 59, 60], "17.5": [61, 62, 63, 64, 65]}


def main() -> int:
    for nombre, (viejo, nuevo) in DOCS.items():
        print(f"\n=== §{nombre}  {nuevo.name}")
        if not nuevo.exists():
            check(False, "el documento existe")
            continue

        # 1. rechazar todos los cambios devuelve el documento de partida
        norm = lambda s: re.sub(r"\s+", " ", s).strip()
        orig = norm(texto(zipfile.ZipFile(viejo).read("word/document.xml").decode("utf8")))
        check(norm(texto(vista(nuevo, False))) == orig,
              "rechazar todos los cambios devuelve exactamente el documento de partida")

        acep = vista(nuevo, True)
        prosa, codigo, tablas, titulos = desglose(acep)
        pw = sum(len(p.split()) for p in prosa)
        tw = sum(len(t.split()) for t in tablas)
        dp = sum(p.count(":") for p in prosa)
        pc = sum(p.count(";") for p in prosa)
        print(f"  · prosa {pw} w en {len(prosa)} párrafos · tablas {tw} w en {len(tablas)} · "
              f"código {len(codigo)} · títulos {len(titulos)}")
        print(f"  · dos puntos {dp} · punto y coma {pc} · rayas {sum(p.count('—') for p in prosa)}")

        # 2. estructura
        n_tit, n_hondos = ESTRUCTURA[nombre]
        check(len(titulos) == n_tit, f"{n_tit} títulos ({len(titulos)})")
        hondos = [t for lv, t in titulos if lv >= 4]
        check(len(hondos) == n_hondos, f"cero títulos de nivel 4 o más ({hondos})")

        # 3. puntuación de prosa
        check(dp <= 2, f"dos puntos en prosa ≤ 2 ({dp})")
        check(pc <= 2, f"punto y coma en prosa ≤ 2 ({pc})")

        # 4. párrafos y oraciones
        gordos = [(len(p.split()), p[:60]) for p in prosa if len(p.split()) > 150]
        check(not gordos, f"ningún párrafo supera 150 palabras ({gordos})")
        largas = [(len(s.split()), s[:60]) for p in prosa for s in oraciones(p) if len(s.split()) > 45]
        check(not largas, f"ninguna oración supera 45 palabras ({largas})")

        # 5. greps prohibidos y exigidos, sobre prosa y tablas
        cuerpo = "\n".join(prosa + tablas + [t for _, t in titulos])
        for pat, desc in PROHIBIDOS[nombre]:
            hits = re.findall(pat, cuerpo)
            check(not hits, f"sin {desc} ({len(hits)})")
        for pat, desc in EXIGIDOS[nombre]:
            check(bool(re.search(pat, cuerpo)), f"presente {desc}")

        # 6. cada tabla con su rótulo y citada exactamente una vez.
        # El párrafo que sólo dice «Tabla N» es el rótulo, no una cita: se excluye del conteo.
        etiquetas = {f"Tabla {n}" for n in TABLAS[nombre]}
        citas = "\n".join([p for p in prosa if p.strip() not in etiquetas] + tablas
                          + [t for _, t in titulos])
        for n in TABLAS[nombre]:
            rot = sum(1 for p in prosa if p.strip() == f"Tabla {n}")
            cit = len(re.findall(rf"\bTabla {n}\b", citas))
            check(rot == 1 and cit == 1,
                  f"la Tabla {n} lleva un rótulo y se cita una vez (rótulo {rot}, citas {cit})")

        # 7. la evidencia que no se toca
        z = zipfile.ZipFile(nuevo)
        x = z.read("word/document.xml").decode("utf8")
        vx = zipfile.ZipFile(viejo).read("word/document.xml").decode("utf8")
        check(x.count("commentRangeStart") == vx.count("commentRangeStart"),
              f"los comentarios sobreviven ({x.count('commentRangeStart')})")
        check(x.count("<w:drawing") == vx.count("<w:drawing"),
              "las figuras sobreviven")
        check(x.count("<w:sectPr") == vx.count("<w:sectPr"), "el sectPr del cuerpo sobrevive")
        check("<w:ins " in x and "<w:del " in x, "la entrega trae cambios controlados")

    print()
    if fallos:
        print(f"FALLAS: {len(fallos)}")
        for f in fallos:
            print("  ·", f)
        return 1
    print("compuerta verde: 0 fallas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
