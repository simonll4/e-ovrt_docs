#!/usr/bin/env python3
"""Índice de unidades del cuerpo de un `.docx`: el mapa que consumen los aplicadores.

Cada unidad es un `<w:p>` o un `<w:tbl>` de primer nivel del cuerpo, en el mismo orden y con
el mismo criterio de troceo que usan `aplicar_*.py`. El índice que imprime es la clave con la
que esos scripts direccionan cada párrafo.

    python3 herramientas/indice_xml.py <archivo.docx> [--out salida.md] [--full]

Trampa que este script respeta (lección del pase de la Etapa 2): **el `<w:sectPr>` final del
cuerpo no pertenece a ningún párrafo**; se devuelve aparte como "resto" y nunca se pierde.
"""
from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path


def split_units(body: str):
    """Trocea el cuerpo en unidades de primer nivel. Idéntico al de los aplicadores."""
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


def text_of(xml: str) -> str:
    return "".join(re.findall(r"<w:t(?: [^>]*)?>(.*?)</w:t>", xml, re.S))


def style_of(xml: str) -> str:
    m = re.search(r'<w:pStyle w:val="([^"]+)"/>', xml)
    return m.group(1) if m else ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("docx")
    ap.add_argument("--out", help="archivo de salida (default: stdout)")
    ap.add_argument("--full", action="store_true", help="texto completo en vez de los primeros 160 caracteres")
    args = ap.parse_args()

    xml = zipfile.ZipFile(args.docx).read("word/document.xml").decode("utf8")
    bs = xml.index("<w:body>") + len("<w:body>")
    be = xml.rindex("</w:body>")
    units, resto = split_units(xml[bs:be])

    lines = [f"# Índice de unidades — {Path(args.docx).name}", ""]
    lines.append(f"unidades: {len(units)} · resto del cuerpo: {len(resto)} bytes · "
                 f"sectPr: {xml.count('<w:sectPr')} · comentarios: {xml.count('commentRangeStart')}")
    lines.append("")
    for i, (kind, raw, _gap) in enumerate(units):
        if kind == "tbl":
            filas = len(re.findall(r"<w:tr\b", raw))
            cols = len(re.findall(r"<w:tc\b", re.search(r"<w:tr\b.*?</w:tr>", raw, re.S).group(0)))
            lines.append(f"[{i}] TBL {filas}×{cols} · {text_of(raw)[:120]}")
            continue
        t = text_of(raw)
        st = style_of(raw)
        marca = []
        if "<w:drawing" in raw:
            marca.append("FIGURA")
        if "<w:sectPr" in raw:
            marca.append("sectPr")
        if "commentRangeStart" in raw:
            ids = re.findall(r'<w:commentRangeStart w:id="(\d+)"/>', raw)
            marca.append("COM" + ",".join(ids))
        if not t.strip() and not marca:
            marca.append("vacío")
        tag = (" [" + " ".join(marca) + "]") if marca else ""
        cuerpo = t if args.full else t[:160]
        lines.append(f"[{i}] {st or 'p':<10}{tag} {len(t.split()):>4}w · {cuerpo}")

    out = "\n".join(lines) + "\n"
    if args.out:
        Path(args.out).write_text(out, encoding="utf8")
        print(f"escrito: {args.out} ({len(units)} unidades)")
    else:
        sys.stdout.write(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
