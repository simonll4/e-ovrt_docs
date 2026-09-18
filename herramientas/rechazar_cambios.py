#!/usr/bin/env python3
"""Rechaza los cambios controlados de un `.docx` (inverso de aceptar) y compara con el original.

Existe para sostener la propiedad que hace segura una entrega con sugerencias: **rechazar todas
las sugerencias tiene que devolver exactamente el documento de partida**. Si el pase rompió algo,
la comparación lo muestra antes de que el usuario abra el archivo.

Semántica de "rechazar", inversa de la de [[aceptar-cambios-docx-por-xml]]:
  1. `w:ins` contenedor  → se elimina el subárbol (la inserción no ocurrió).
  2. `w:del` contenedor  → se desenvuelve y `w:delText` vuelve a ser `w:t`.
  3. `ins`/`del` dentro de `rPr`/`trPr`/`tcPr` → sólo se quita la marca.
  4. `w:pPr/w:rPr/w:del` → marca de párrafo borrada que se conserva: se quita la marca.
  5. `w:pPr/w:rPr/w:ins` → marca de párrafo insertada: el párrafo se fusiona con el siguiente
     (si el pase lo agregó entero, queda vacío y desaparece).
  6. `w:pPrChange` → se restaura el `w:pPr` anterior que el cambio guardó.

Los comentarios NO son cambios controlados: sobreviven al rechazo. Por eso la comparación es
sobre texto, tablas y figuras, no byte a byte.

Uso:
    python3 herramientas/rechazar_cambios.py ORIGINAL.docx CON_SUGERENCIAS.docx
"""
from __future__ import annotations

import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _registrar_ns(xml: bytes) -> None:
    for prefijo, uri in re.findall(rb'xmlns:([A-Za-z0-9_]+)="([^"]+)"', xml):
        ET.register_namespace(prefijo.decode(), uri.decode())


def _padres(raiz):
    return {h: p for p in raiz.iter() for h in p}


def rechazar(raiz) -> dict:
    st = {"ins": 0, "del": 0, "marcas": 0, "fusiones": 0, "pPrChange": 0}

    # 6. pPrChange: restaurar el pPr anterior
    pm = _padres(raiz)
    for cambio in list(raiz.iter(W + "pPrChange")):
        ppr = pm.get(cambio)
        anterior = cambio.find(W + "pPr")
        if ppr is None:
            continue
        hijos_previos = list(anterior) if anterior is not None else []
        for h in list(ppr):
            ppr.remove(h)
        for h in hijos_previos:
            ppr.append(h)
        st["pPrChange"] += 1

    # 1/3. w:ins
    cambio = True
    while cambio:
        cambio = False
        pm = _padres(raiz)
        for el in list(raiz.iter(W + "ins")):
            p = pm.get(el)
            if p is None:
                continue
            if p.tag in (W + "rPr", W + "trPr", W + "tcPr"):
                abuelo = pm.get(p)
                if p.tag == W + "rPr" and abuelo is not None and abuelo.tag == W + "pPr":
                    continue          # marca de párrafo insertada: paso 5
                p.remove(el)
                st["marcas"] += 1
            else:
                p.remove(el)
                st["ins"] += 1
            cambio = True

    # 2/3. w:del
    cambio = True
    while cambio:
        cambio = False
        pm = _padres(raiz)
        for el in list(raiz.iter(W + "del")):
            p = pm.get(el)
            if p is None:
                continue
            if p.tag in (W + "rPr", W + "trPr", W + "tcPr"):
                p.remove(el)          # 3 y 4: la marca se quita, el contenido queda
                st["marcas"] += 1
            else:
                idx = list(p).index(el)
                p.remove(el)
                for k, h in enumerate(list(el)):
                    p.insert(idx + k, h)
                st["del"] += 1
            cambio = True
    for t in raiz.iter(W + "delText"):
        t.tag = W + "t"

    # 5. marca de párrafo insertada → fusión con el siguiente
    pm = _padres(raiz)
    for para in list(raiz.iter(W + "p")):
        ppr = para.find(W + "pPr")
        if ppr is None:
            continue
        rpr = ppr.find(W + "rPr")
        if rpr is None or rpr.find(W + "ins") is None:
            continue
        rpr.remove(rpr.find(W + "ins"))
        padre = pm[para]
        hermanos = list(padre)
        idx = hermanos.index(para)
        siguiente = next((h for h in hermanos[idx + 1:] if h.tag == W + "p"), None)
        if siguiente is None:
            continue
        contenido = [h for h in list(para) if h.tag != W + "pPr"]
        destino_ppr = siguiente.find(W + "pPr")
        base = 1 if destino_ppr is not None else 0
        for k, h in enumerate(contenido):
            siguiente.insert(base + k, h)
        padre.remove(para)
        st["fusiones"] += 1
    return st


def texto(raiz) -> str:
    return "".join(t.text or "" for t in raiz.iter(W + "t"))


def main(orig: str, mod: str) -> int:
    with zipfile.ZipFile(mod) as z:
        xml = z.read("word/document.xml")
    _registrar_ns(xml)
    raiz = ET.fromstring(xml)
    st = rechazar(raiz)
    with zipfile.ZipFile(orig) as z:
        raiz0 = ET.fromstring(z.read("word/document.xml"))

    t0, t1 = texto(raiz0), texto(raiz)
    tablas = (len(list(raiz0.iter(W + "tbl"))), len(list(raiz.iter(W + "tbl"))))
    figs = (len(list(raiz0.iter(W + "drawing"))), len(list(raiz.iter(W + "drawing"))))
    paras = (len(list(raiz0.iter(W + "p"))), len(list(raiz.iter(W + "p"))))
    print(f"rechazadas: {st}")
    print(f"texto original {len(t0)} · tras rechazar {len(t1)} · idéntico: {t0 == t1}")
    print(f"tablas {tablas[0]} → {tablas[1]} · figuras {figs[0]} → {figs[1]} · párrafos {paras[0]} → {paras[1]}")
    if t0 != t1:
        import difflib
        sm = difflib.SequenceMatcher(None, t0, t1, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                print(f"  {tag}: original[{i1}:{i2}]={t0[i1:i2][:120]!r} → nuevo={t1[j1:j2][:120]!r}")
        return 1
    if tablas[0] != tablas[1] or figs[0] != figs[1]:
        print("  ✗ cambió el inventario de tablas o figuras")
        return 1
    print("✓ rechazar todas las sugerencias devuelve el documento de partida")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
