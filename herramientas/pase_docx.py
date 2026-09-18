#!/usr/bin/env python3
"""Motor de pases sobre `.docx` del informe, como CAMBIOS CONTROLADOS y COMENTARIOS.

Extraído y ampliado a partir de `aplicar_v16_17_3.py` / `aplicar_v17_17_4.py` (pases 3 y 4),
que reescribían el párrafo entero en cada edición. Acá la edición es **quirúrgica**: se marca
como borrado sólo el tramo que cambia y se inserta el texto nuevo a su lado, de modo que la
revisión en Google Docs muestre la diferencia real y no un párrafo completo tachado.

Qué agrega respecto de los pases anteriores:
  · `reemplazar` / `borrar` / `agregar_al_final` — edición por tramo dentro de un párrafo o celda;
  · `comentario` — comentario nuevo anclado a un tramo, creando `word/comments.xml`,
    `commentsExtended.xml`, la relación y el content type cuando el documento no los tiene;
  · `figura` — inserta una imagen como sugerencia (`w:ins`), agregando la parte a `word/media/`
    y su relación;
  · `estilo_titulo` — repara un encabezado que perdió su `pStyle`, dejando `pPrChange` para que
    el cambio de formato también se revise.

Reglas de oficio heredadas (no negociables):
  · nunca LibreOffice: round-trip que arriesga ecuaciones OMML y estilos;
  · el `w:sectPr` final del cuerpo no pertenece a ningún párrafo y viaja en el «resto»;
  · los comentarios existentes conservan sus anclas; no se resuelven ni se borran;
  · se valida el XML antes de escribir el zip, y se comprueba que no se pierda ninguna parte;
  · rechazar todas las sugerencias debe devolver el documento de partida.
"""
from __future__ import annotations

import datetime
import re
import shutil
import struct
import zipfile
from pathlib import Path

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
RPR = '<w:rPr><w:rtl w:val="0"/></w:rPr>'
RPR_B = '<w:rPr><w:b w:val="1"/><w:bCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'
RPR_I = '<w:rPr><w:i w:val="1"/><w:iCs w:val="1"/><w:rtl w:val="0"/></w:rPr>'

RUN_RE = re.compile(r"<w:r\b(?![a-zA-Z])[^>]*>.*?</w:r>", re.S)
T_RE = re.compile(r"<w:t(?:\s[^>]*)?>(.*?)</w:t>", re.S)
P_RE = re.compile(r"<w:p\b[^>]*>.*?</w:p>", re.S)
TR_RE = re.compile(r"<w:tr\b[^>]*>.*?</w:tr>", re.S)
TC_RE = re.compile(r"<w:tc\b[^>]*>.*?</w:tc>", re.S)


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def desesc(t: str) -> str:
    return t.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def _tokens(text: str):
    """`**negrita**` y `*cursiva*` se convierten en runs con su formato."""
    out, pos = [], 0
    for m in re.finditer(r"\*\*([^*]+)\*\*|\*([^*]+)\*", text):
        if m.start() > pos:
            out.append((None, text[pos:m.start()]))
        out.append((RPR_B, m.group(1)) if m.group(1) is not None else (RPR_I, m.group(2)))
        pos = m.end()
    if pos < len(text):
        out.append((None, text[pos:]))
    return out


class Documento:
    """Un `.docx` abierto para recibir un pase. Las ediciones se acumulan y se escriben al guardar."""

    def __init__(self, src: Path | str, autor: str = "Claude", fecha: str = "2026-09-07T12:00:00Z"):
        self.src = Path(src)
        self.autor = autor
        self.fecha = fecha
        with zipfile.ZipFile(self.src) as z:
            self.partes = {i.filename: z.read(i.filename) for i in z.infolist()}
            self.orden = [i.filename for i in z.infolist()]
        xml = self.partes["word/document.xml"].decode("utf8")
        self.xml0 = xml
        bs = xml.index("<w:body>") + len("<w:body>")
        be = xml.rindex("</w:body>")
        self.head, body, self.tail = xml[:bs], xml[bs:be], xml[be:]
        self.units, self.resto = self._split(body)
        self.prefijo_titulo = self._prefijo_titulo()
        self._id = 9000
        self._cid = self._prox_comment_id()
        self._docpr = 900
        self.nuevos: dict[int, list[str]] = {}     # unidad → párrafos nuevos que la siguen
        self.comentarios: list[tuple[int, str]] = []   # (id, texto) para comments.xml
        self.medios: list[tuple[str, bytes]] = []      # (nombre de parte, bytes)
        self.log: list[str] = []

    # ------------------------------------------------------------------ infraestructura
    def _nid(self) -> int:
        self._id += 1
        return self._id

    def _prefijo_titulo(self) -> str:
        """Cómo se llaman los estilos de título EN ESTE documento: `Heading` o `Ttulo`.

        ⚠ 2026-09-08: Google Docs nombra el estilo según la interfaz en que se editó el documento
        y le quita los acentos, así que uno editado en español trae `Ttulo1`…`Ttulo5` («Título»
        sin la í). Escribir `Heading3` en un documento de la familia `Ttulo` deja el párrafo con
        un estilo inexistente, que Word muestra como texto normal.
        """
        estilos = self.partes.get("word/styles.xml", b"").decode("utf8", "ignore")
        for prefijo in ("Heading", "Ttulo", "Título", "Titulo"):
            if re.search(r'w:styleId="%s\d"' % prefijo, estilos):
                return prefijo
        return "Heading"

    def _prox_comment_id(self) -> int:
        c = self.partes.get("word/comments.xml")
        if not c:
            return 500
        ids = [int(x) for x in re.findall(r'<w:comment [^>]*w:id="(\d+)"', c.decode("utf8"))]
        return max(ids) + 1 if ids else 500

    @staticmethod
    def _split(body: str):
        units, i = [], 0
        while i < len(body):
            m = re.search(r"<w:(p|tbl)\b", body[i:])
            if not m:
                break
            kind, start = m.group(1), i + m.start()
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

    # ------------------------------------------------------------------ lectura y localización
    @staticmethod
    def texto_de(xml: str) -> str:
        """Texto visible: lo que quedaría al ACEPTAR las sugerencias (los `w:delText` no cuentan)."""
        return "".join(desesc(m.group(1)) for m in T_RE.finditer(xml))

    def texto(self, i: int) -> str:
        return self.texto_de(self.units[i][1])

    def buscar(self, frag: str, kind: str | None = None) -> list[int]:
        return [i for i, (k, raw, _) in enumerate(self.units)
                if (kind is None or k == kind) and frag in self.texto_de(raw)]

    def unica(self, frag: str, kind: str | None = None) -> int:
        hits = self.buscar(frag, kind)
        if len(hits) != 1:
            raise LookupError(f"{len(hits)} unidades contienen {frag[:60]!r}: {hits}")
        return hits[0]

    def volcar(self, limite: int = 120) -> str:
        out = []
        for i, (k, raw, _) in enumerate(self.units):
            t = self.texto_de(raw).strip()
            style = re.search(r'<w:pStyle w:val="([^"]+)"', raw)
            marca = f"[{style.group(1)}]" if style else ("[TBL]" if k == "tbl" else "")
            out.append(f"{i:4d} {marca:12s} {t[:limite]}")
        return "\n".join(out)

    # ------------------------------------------------------------------ partición de un tramo
    def _partir(self, xml: str, frag: str, ocurrencia: int = 0):
        """Parte los runs para que `frag` quede entre fronteras de run.

        Devuelve `(xml_nuevo, ini, fin)`, offsets dentro de `xml_nuevo` que delimitan
        exactamente los runs que contienen el tramo.
        """
        # mapa offset de texto visible → posiciones de cada <w:t>
        spans = []   # (ini_txt, fin_txt, match del w:t)
        pos = 0
        for m in T_RE.finditer(xml):
            t = desesc(m.group(1))
            spans.append((pos, pos + len(t), m))
            pos += len(t)
        texto = "".join(desesc(m.group(1)) for _, _, m in spans)
        idx = -1
        for _ in range(ocurrencia + 1):
            idx = texto.find(frag, idx + 1)
            if idx < 0:
                raise LookupError(f"no aparece {frag[:70]!r}")
        ini_txt, fin_txt = idx, idx + len(frag)
        if texto.find(frag, fin_txt) >= 0 and ocurrencia == 0:
            raise LookupError(f"ambiguo, {texto.count(frag)} ocurrencias de {frag[:50]!r}")

        # runs afectados: los que contienen algún w:t que intersecta el tramo
        afectados = []
        for a, b, m in spans:
            if b > ini_txt and a < fin_txt:
                run = self._run_de(xml, m.start())
                if run is None:
                    raise ValueError("un tramo del texto no está dentro de un <w:r>")
                afectados.append((a, b, m, run))
        if not afectados:
            raise ValueError("tramo vacío")
        if any("<w:ins " in xml[max(0, r[0] - 400):r[0]].rsplit("<w:r", 1)[0][-200:]
               for r in [(x[3][0], x[3][1]) for x in afectados]):
            pass  # informativo; Word admite borrar una inserción previa

        primero, ultimo = afectados[0], afectados[-1]
        r0_ini, r0_fin = primero[3]
        rN_ini, rN_fin = ultimo[3]

        piezas, cursor = [], 0
        piezas.append(xml[:r0_ini])
        cursor = r0_ini

        # prefijo dentro del primer run
        pre = ""
        if primero[0] < ini_txt:
            pre = self._run_con(xml[r0_ini:r0_fin], primero[2],
                                desesc(primero[2].group(1))[:ini_txt - primero[0]])
        # sufijo dentro del último run
        post = ""
        if ultimo[1] > fin_txt:
            post = self._run_con(xml[rN_ini:rN_fin], ultimo[2],
                                 desesc(ultimo[2].group(1))[fin_txt - ultimo[0]:])

        # el cuerpo: runs completos, con el primero y el último recortados al tramo
        cuerpo = []
        for k, (a, b, m, (ri, rf)) in enumerate(afectados):
            trozo = xml[ri:rf]
            t_run = desesc(m.group(1))
            desde = max(0, ini_txt - a)
            hasta = min(len(t_run), fin_txt - a)
            if desde > 0 or hasta < len(t_run):
                trozo = self._run_con(trozo, m, t_run[desde:hasta])
            cuerpo.append(trozo)
            if k < len(afectados) - 1:
                cuerpo.append(xml[rf:afectados[k + 1][3][0]])   # lo que hubiera entre runs

        nuevo = xml[:r0_ini] + pre
        ini = len(nuevo)
        nuevo += "".join(cuerpo)
        fin = len(nuevo)
        nuevo += post + xml[rN_fin:]
        return nuevo, ini, fin

    @staticmethod
    def _run_de(xml: str, pos_t: int):
        """Offsets `(ini, fin)` del `<w:r>` que contiene la posición del `<w:t>` dada."""
        ini = xml.rfind("<w:r>", 0, pos_t)
        ini2 = xml.rfind("<w:r ", 0, pos_t)
        ini = max(ini, ini2)
        if ini < 0:
            return None
        fin = xml.index("</w:r>", pos_t) + len("</w:r>")
        return (ini, fin)

    @staticmethod
    def _run_con(run_xml: str, m_t, texto: str) -> str:
        """El mismo run con otro texto en su `<w:t>` (conserva rPr y el resto)."""
        ini_t = run_xml.index("<w:t")
        fin_t = run_xml.index("</w:t>", ini_t) + len("</w:t>")
        return run_xml[:ini_t] + f'<w:t xml:space="preserve">{esc(texto)}</w:t>' + run_xml[fin_t:]

    # ------------------------------------------------------------------ marcas de cambio
    def _ins(self, texto: str, base: str = RPR) -> str:
        runs = []
        for rpr, frag in _tokens(texto):
            runs.append(f'<w:r>{rpr or base}<w:t xml:space="preserve">{esc(frag)}</w:t></w:r>')
        return (f'<w:ins w:id="{self._nid()}" w:author="{self.autor}" w:date="{self.fecha}">'
                + "".join(runs) + "</w:ins>")

    def _del(self, xml: str, incluir_figuras: bool = False) -> str:
        def repl(m):
            r = m.group(0)
            if T_RE.search(r) or (incluir_figuras and "<w:drawing" in r):
                d = re.sub(r"<w:t(\s[^>]*)?>", lambda mm: "<w:delText%s>" % (mm.group(1) or ""), r)
                d = d.replace("</w:t>", "</w:delText>")
                return (f'<w:del w:id="{self._nid()}" w:author="{self.autor}" '
                        f'w:date="{self.fecha}">{d}</w:del>')
            return r
        return RUN_RE.sub(repl, xml)

    # ------------------------------------------------------------------ operaciones públicas
    def reemplazar(self, i: int, viejo: str, nuevo: str, ocurrencia: int = 0) -> None:
        """Marca `viejo` como borrado e inserta `nuevo` en su lugar, dentro de la unidad `i`."""
        xml = self.units[i][1]
        part, ini, fin = self._partir(xml, viejo, ocurrencia)
        medio = self._del(part[ini:fin])
        ins = self._ins(nuevo) if nuevo else ""
        self.units[i][1] = part[:ini] + medio + ins + part[fin:]
        self.log.append(f"u{i}: {viejo[:45]!r} → {nuevo[:45]!r}")

    def borrar(self, i: int, viejo: str, ocurrencia: int = 0) -> None:
        self.reemplazar(i, viejo, "", ocurrencia)

    def agregar_al_final(self, i: int, texto: str) -> None:
        """Inserta texto al final del párrafo (antes de la marca de párrafo)."""
        xml = self.units[i][1]
        corte = xml.rindex("</w:p>")
        self.units[i][1] = xml[:corte] + self._ins(texto) + xml[corte:]
        self.log.append(f"u{i}: += {texto[:60]!r}")

    def borrar_parrafo(self, i: int) -> None:
        """Marca todo el párrafo como borrado, incluida su marca de párrafo."""
        p = self._del(self.units[i][1], incluir_figuras=True)
        m = re.search(r"<w:pPr>(.*?)</w:pPr>", p, re.S)
        tag = f'<w:del w:id="{self._nid()}" w:author="{self.autor}" w:date="{self.fecha}"/>'
        if m:
            ppr = m.group(0)
            if "<w:rPr/>" in ppr:
                new = ppr.replace("<w:rPr/>", f"<w:rPr>{tag}</w:rPr>", 1)
            elif "<w:rPr>" in ppr:
                new = ppr.replace("<w:rPr>", f"<w:rPr>{tag}", 1)
            else:
                new = ppr.replace("</w:pPr>", f"<w:rPr>{tag}</w:rPr></w:pPr>", 1)
            p = p.replace(ppr, new, 1)
        self.units[i][1] = p
        self.log.append(f"u{i}: párrafo borrado")

    def parrafo_nuevo(self, i: int, texto: str, muestra: int | None = None,
                      estilo: str | None = None, contenido: str | None = None) -> None:
        """Agrega un párrafo nuevo (sugerencia) inmediatamente después de la unidad `i`."""
        base = self.units[muestra if muestra is not None else i][1]
        m = re.search(r"<w:pPr>.*?</w:pPr>", base, re.S)
        ppr = m.group(0) if m else "<w:pPr><w:rPr/></w:pPr>"
        ppr = re.sub(r"<w:sectPr>.*?</w:sectPr>", "", ppr, flags=re.S)
        if estilo is None:
            ppr = re.sub(r'<w:pStyle w:val="[^"]*"/>', "", ppr)
        else:
            ppr = re.sub(r'<w:pStyle w:val="[^"]*"/>', "", ppr)
            ppr = ppr.replace("<w:pPr>", f'<w:pPr><w:pStyle w:val="{estilo}"/>', 1)
        tag = f'<w:ins w:id="{self._nid()}" w:author="{self.autor}" w:date="{self.fecha}"/>'
        if "<w:rPr/>" in ppr:
            ppr = ppr.replace("<w:rPr/>", f"<w:rPr>{tag}</w:rPr>", 1)
        elif "<w:rPr>" in ppr:
            ppr = ppr.replace("<w:rPr>", f"<w:rPr>{tag}", 1)
        else:
            ppr = ppr.replace("</w:pPr>", f"<w:rPr>{tag}</w:rPr></w:pPr>", 1)
        cuerpo = contenido if contenido is not None else self._ins(texto)
        self.nuevos.setdefault(i, []).append(f"<w:p>{ppr}{cuerpo}</w:p>")
        self.log.append(f"u{i}: + párrafo nuevo {texto[:50]!r}")

    def bloque_codigo(self, i: int, texto: str, muestra: int) -> None:
        """Agrega un bloque de código como sugerencia, con el formato del documento.

        `muestra` debe ser un párrafo que ya sea bloque de código: de él se copian el `pPr`
        (borde, sombreado, sangría) y el `rPr` del primer run (tipografía monoespaciada y
        cuerpo). Los saltos de línea del texto se emiten como `w:br`, que es como Word
        representa un bloque de varias líneas dentro de un mismo párrafo.
        """
        base = self.units[muestra][1]
        m_ppr = re.search(r"<w:pPr>.*?</w:pPr>", base, re.S)
        ppr = m_ppr.group(0) if m_ppr else "<w:pPr><w:rPr/></w:pPr>"
        m_run = RUN_RE.search(base)
        m_rpr = re.search(r"<w:rPr>.*?</w:rPr>", m_run.group(0), re.S) if m_run else None
        rpr = m_rpr.group(0) if m_rpr else RPR
        tag = f'<w:ins w:id="{self._nid()}" w:author="{self.autor}" w:date="{self.fecha}"/>'
        if "<w:rPr/>" in ppr:
            ppr_ins = ppr.replace("<w:rPr/>", f"<w:rPr>{tag}</w:rPr>", 1)
        elif "<w:rPr>" in ppr:
            ppr_ins = ppr.replace("<w:rPr>", f"<w:rPr>{tag}", 1)
        else:
            ppr_ins = ppr.replace("</w:pPr>", f"<w:rPr>{tag}</w:rPr></w:pPr>", 1)
        partes = []
        for k, linea in enumerate(texto.split("\n")):
            if k:
                partes.append('<w:br w:type="textWrapping"/>')
            partes.append(f'<w:t xml:space="preserve">{esc(linea)}</w:t>')
        run = f"<w:r>{rpr}{''.join(partes)}</w:r>"
        cuerpo = (f'<w:ins w:id="{self._nid()}" w:author="{self.autor}" '
                  f'w:date="{self.fecha}">{run}</w:ins>')
        self.nuevos.setdefault(i, []).append(f"<w:p>{ppr_ins}{cuerpo}</w:p>")
        self.log.append(f"u{i}: + bloque de código de {len(texto.splitlines())} líneas")

    def celda(self, i: int, fila: int, col: int, viejo: str, nuevo: str,
              rpr: str | None = None) -> None:
        """Edición quirúrgica dentro de una celda de tabla.

        `rpr` fija el formato de lo insertado (p. ej. `RPR_B` en una celda de encabezado);
        sin él se usa el formato base.
        """
        tbl = self.units[i][1]
        filas = list(TR_RE.finditer(tbl))
        tr = filas[fila].group(0)
        celdas = list(TC_RE.finditer(tr))
        tc = celdas[col].group(0)
        part, ini, fin = self._partir(tc, viejo)
        ins = self._ins(nuevo, base=rpr or RPR) if nuevo else ""
        nuevo_tc = part[:ini] + self._del(part[ini:fin]) + ins + part[fin:]
        nuevo_tr = tr[:celdas[col].start()] + nuevo_tc + tr[celdas[col].end():]
        self.units[i][1] = tbl[:filas[fila].start()] + nuevo_tr + tbl[filas[fila].end():]
        self.log.append(f"u{i} celda[{fila}][{col}]: {viejo[:35]!r} → {nuevo[:35]!r}")

    def celda_agregar(self, i: int, fila: int, col: int, texto: str) -> None:
        tbl = self.units[i][1]
        filas = list(TR_RE.finditer(tbl))
        tr = filas[fila].group(0)
        celdas = list(TC_RE.finditer(tr))
        tc = celdas[col].group(0)
        corte = tc.rindex("</w:p>")
        nuevo_tc = tc[:corte] + self._ins(texto) + tc[corte:]
        nuevo_tr = tr[:celdas[col].start()] + nuevo_tc + tr[celdas[col].end():]
        self.units[i][1] = tbl[:filas[fila].start()] + nuevo_tr + tbl[filas[fila].end():]
        self.log.append(f"u{i} celda[{fila}][{col}]: += {texto[:40]!r}")

    def fila_nueva(self, i: int, tras: int, celdas: list[str], modelo: int | None = None) -> None:
        """Agrega una fila de tabla como sugerencia, clonando el formato de otra fila.

        La marca `w:ins` va en el `w:trPr`, que es lo que hace que Word la muestre como fila
        insertada y que rechazarla la quite entera.
        """
        tbl = self.units[i][1]
        filas = list(TR_RE.finditer(tbl))
        base = filas[modelo if modelo is not None else tras].group(0)
        tcs = list(TC_RE.finditer(base))
        if len(tcs) != len(celdas):
            raise ValueError(f"la fila modelo tiene {len(tcs)} celdas y se pasaron {len(celdas)}")
        piezas, cursor = [], 0
        for tc, texto in zip(tcs, celdas):
            piezas.append(base[cursor:tc.start()])
            cuerpo = tc.group(0)
            paras = list(P_RE.finditer(cuerpo))
            p0 = paras[0].group(0)
            m_ppr = re.search(r"<w:pPr>.*?</w:pPr>", p0, re.S)
            ppr = m_ppr.group(0) if m_ppr else ""
            nuevo_p = f"<w:p>{ppr}{self._ins(texto)}</w:p>"
            piezas.append(cuerpo[:paras[0].start()] + nuevo_p + cuerpo[paras[-1].end():])
            cursor = tc.end()
        piezas.append(base[cursor:])
        nueva = "".join(piezas)
        tag = f'<w:ins w:id="{self._nid()}" w:author="{self.autor}" w:date="{self.fecha}"/>'
        if "<w:trPr>" in nueva:
            nueva = nueva.replace("<w:trPr>", f"<w:trPr>{tag}", 1)
        else:
            nueva = re.sub(r"(<w:tr\b[^>]*>)", r"\1<w:trPr>" + tag + "</w:trPr>", nueva, count=1)
        corte = filas[tras].end()
        self.units[i][1] = tbl[:corte] + nueva + tbl[corte:]
        self.log.append(f"u{i}: + fila tras la {tras} → {celdas[0][:40]!r}")

    def borrar_fila(self, i: int, fila: int) -> None:
        """Marca una fila de tabla entera como borrada (sugerencia).

        Inversa de `fila_nueva`: la marca `w:del` va en el `w:trPr`, que es lo que hace que Word
        la muestre como fila eliminada y que aceptarla la quite. El contenido se convierte a
        `w:delText` para que el texto siga visible tachado mientras la sugerencia no se resuelva.
        """
        tbl = self.units[i][1]
        filas = list(TR_RE.finditer(tbl))
        tr = filas[fila].group(0)
        nueva = self._del(tr, incluir_figuras=True)
        tag = f'<w:del w:id="{self._nid()}" w:author="{self.autor}" w:date="{self.fecha}"/>'
        if "<w:trPr>" in nueva:
            nueva = nueva.replace("<w:trPr>", f"<w:trPr>{tag}", 1)
        else:
            nueva = re.sub(r"(<w:tr\b[^>]*>)", r"\1<w:trPr>" + tag + "</w:trPr>", nueva, count=1)
        self.units[i][1] = tbl[:filas[fila].start()] + nueva + tbl[filas[fila].end():]
        self.log.append(f"u{i}: − fila {fila} {self.texto_de(tr)[:45]!r}")

    def comentario_en_celda(self, i: int, fila: int, col: int, ancla: str,
                            texto: str, ocurrencia: int = 0) -> int:
        """Comentario anclado a un tramo de una celda de tabla."""
        cid = self._cid
        self._cid += 1
        tbl = self.units[i][1]
        filas = list(TR_RE.finditer(tbl))
        tr = filas[fila].group(0)
        celdas = list(TC_RE.finditer(tr))
        tc = celdas[col].group(0)
        part, ini, fin = self._partir(tc, ancla, ocurrencia)
        marca_fin = (f'<w:commentRangeEnd w:id="{cid}"/>'
                     f'<w:r>{RPR}<w:commentReference w:id="{cid}"/></w:r>')
        nuevo_tc = (part[:ini] + f'<w:commentRangeStart w:id="{cid}"/>'
                    + part[ini:fin] + marca_fin + part[fin:])
        nuevo_tr = tr[:celdas[col].start()] + nuevo_tc + tr[celdas[col].end():]
        self.units[i][1] = tbl[:filas[fila].start()] + nuevo_tr + tbl[filas[fila].end():]
        self.comentarios.append((cid, texto))
        self.log.append(f"u{i} celda[{fila}][{col}]: comentario {cid} sobre {ancla[:35]!r}")
        return cid

    def texto_celda(self, i: int, fila: int, col: int) -> str:
        tr = list(TR_RE.finditer(self.units[i][1]))[fila].group(0)
        return self.texto_de(list(TC_RE.finditer(tr))[col].group(0))

    def filas(self, i: int) -> list[list[str]]:
        out = []
        for tr in TR_RE.finditer(self.units[i][1]):
            out.append([self.texto_de(tc.group(0)) for tc in TC_RE.finditer(tr.group(0))])
        return out

    def estilo_titulo(self, i: int, nivel: int) -> None:
        """Devuelve a un párrafo su estilo de encabezado, dejando `pPrChange` para revisarlo."""
        p = self.units[i][1]
        m = re.search(r"<w:pPr>(.*?)</w:pPr>", p, re.S)
        if not m:
            raise ValueError("el párrafo no tiene pPr")
        viejo_interior = m.group(1)
        if re.search(r'<w:pStyle w:val="(?:Heading|T[íi]?tulo)', viejo_interior):
            raise ValueError("ya tiene estilo de encabezado")
        anterior = re.sub(r"<w:sectPr>.*?</w:sectPr>", "", viejo_interior, flags=re.S)
        cambio = (f'<w:pPrChange w:id="{self._nid()}" w:author="{self.autor}" '
                  f'w:date="{self.fecha}"><w:pPr>{anterior}</w:pPr></w:pPrChange>')
        estilo = f"{self.prefijo_titulo}{nivel}"
        nuevo = f'<w:pPr><w:pStyle w:val="{estilo}"/>{viejo_interior}{cambio}</w:pPr>'
        self.units[i][1] = p.replace(m.group(0), nuevo, 1)
        self.log.append(f"u{i}: estilo → {estilo}")

    def comentario(self, i: int, ancla: str, texto: str, ocurrencia: int = 0) -> int:
        """Comentario nuevo anclado al tramo `ancla` de la unidad `i`."""
        cid = self._cid
        self._cid += 1
        xml = self.units[i][1]
        part, ini, fin = self._partir(xml, ancla, ocurrencia)
        marca_ini = f'<w:commentRangeStart w:id="{cid}"/>'
        marca_fin = (f'<w:commentRangeEnd w:id="{cid}"/>'
                     f'<w:r>{RPR}<w:commentReference w:id="{cid}"/></w:r>')
        self.units[i][1] = part[:ini] + marca_ini + part[ini:fin] + marca_fin + part[fin:]
        self.comentarios.append((cid, texto))
        self.log.append(f"u{i}: comentario {cid} sobre {ancla[:40]!r}")
        return cid

    def comentario_en_nuevo(self, i: int, k: int, texto: str) -> int:
        """Comentario sobre el párrafo nuevo `k` agregado tras la unidad `i`."""
        cid = self._cid
        self._cid += 1
        p = self.nuevos[i][k]
        m = re.search(r'<w:ins w:id="\d+" w:author="[^"]*" w:date="[^"]*">', p)
        idx_fin = p.index("</w:ins>", m.end()) + len("</w:ins>")
        marca_fin = (f'<w:commentRangeEnd w:id="{cid}"/>'
                     f'<w:r>{RPR}<w:commentReference w:id="{cid}"/></w:r>')
        self.nuevos[i][k] = (p[:m.start()] + f'<w:commentRangeStart w:id="{cid}"/>'
                             + p[m.start():idx_fin] + marca_fin + p[idx_fin:])
        self.comentarios.append((cid, texto))
        self.log.append(f"u{i}: comentario {cid} sobre párrafo nuevo {k}")
        return cid

    # ------------------------------------------------------------------ figuras
    def figura(self, i: int, png: Path | str, ancho_emu: int = 5943600,
               muestra: int | None = None) -> None:
        """Inserta una imagen como párrafo nuevo (sugerencia) después de la unidad `i`."""
        png = Path(png)
        datos = png.read_bytes()
        ancho_px, alto_px = struct.unpack(">II", datos[16:24])
        alto_emu = int(round(ancho_emu * alto_px / ancho_px))
        n = 1
        while f"word/media/image{n}.png" in self.partes or \
                any(nom == f"word/media/image{n}.png" for nom, _ in self.medios):
            n += 1
        parte = f"word/media/image{n}.png"
        self.medios.append((parte, datos))
        self._content_type_default("png", "image/png")
        rid = self._rel_nueva(
            "http://schemas.openxmlformats.org/officeDocument/2006/relationships/image",
            f"media/image{n}.png")
        did = self._docpr = self._docpr + 1
        nombre = png.name
        drawing = (
            f'<w:drawing><wp:inline distB="0" distT="0" distL="0" distR="0">'
            f'<wp:extent cx="{ancho_emu}" cy="{alto_emu}"/>'
            f'<wp:effectExtent b="0" l="0" r="0" t="0"/>'
            f'<wp:docPr id="{did}" name="{nombre}"/>'
            f'<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
            f'<pic:pic><pic:nvPicPr><pic:cNvPr id="0" name="{nombre}"/>'
            f'<pic:cNvPicPr preferRelativeResize="0"/></pic:nvPicPr>'
            f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
            f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{ancho_emu}" cy="{alto_emu}"/></a:xfrm>'
            f'<a:prstGeom prst="rect"/><a:ln/></pic:spPr></pic:pic></a:graphicData></a:graphic>'
            f"</wp:inline></w:drawing>")
        run = (f'<w:ins w:id="{self._nid()}" w:author="{self.autor}" w:date="{self.fecha}">'
               f"<w:r>{RPR}{drawing}</w:r></w:ins>")
        self.parrafo_nuevo(i, "", muestra=muestra, contenido=run)
        self.log.append(f"u{i}: + figura {nombre} ({ancho_px}×{alto_px} px)")

    def borrar_figura(self, i: int) -> None:
        """Marca como borrado el run que contiene el dibujo de la unidad `i`."""
        xml = self.units[i][1]
        def repl(m):
            r = m.group(0)
            if "<w:drawing" in r:
                return (f'<w:del w:id="{self._nid()}" w:author="{self.autor}" '
                        f'w:date="{self.fecha}">{r}</w:del>')
            return r
        nuevo = RUN_RE.sub(repl, xml)
        if nuevo == xml:
            raise ValueError("la unidad no contiene ningún dibujo")
        self.units[i][1] = nuevo
        self.log.append(f"u{i}: figura marcada como borrada")

    def _rel_nueva(self, tipo: str, destino: str) -> str:
        rels = self.partes["word/_rels/document.xml.rels"].decode("utf8")
        usados = {int(x) for x in re.findall(r'Id="rId(\d+)"', rels)}
        n = max(usados) + 1 if usados else 1
        rid = f"rId{n}"
        nuevo = f'<Relationship Id="{rid}" Type="{tipo}" Target="{destino}"/>'
        rels = rels.replace("</Relationships>", nuevo + "</Relationships>")
        self.partes["word/_rels/document.xml.rels"] = rels.encode("utf8")
        return rid

    # ------------------------------------------------------------------ comentarios: partes
    def _ns_document(self) -> str:
        m = re.search(r"<w:document\s([^>]*?)>", self.xml0, re.S)
        return " ".join(x for x in m.group(1).split() if x.startswith("xmlns:"))

    def _escribir_comentarios(self) -> None:
        if not self.comentarios:
            return
        ns = self._ns_document()
        cuerpo = []
        for cid, texto in self.comentarios:
            partes = []
            for rpr, frag in _tokens(texto):
                partes.append(f'<w:r>{rpr or RPR}<w:t xml:space="preserve">{esc(frag)}</w:t></w:r>')
            partes.append(f'<w:r>{RPR}<w:annotationRef/></w:r>')
            cuerpo.append(
                f'<w:comment w:id="{cid}" w:author="{self.autor}" w:initials="C" '
                f'w:date="{self.fecha}"><w:p w14:paraId="{0xC0000000 + cid:08X}">'
                f"<w:pPr><w:rPr/></w:pPr>" + "".join(partes) + "</w:p></w:comment>")
        existente = self.partes.get("word/comments.xml")
        if existente:
            c = existente.decode("utf8")
            c = c.replace("</w:comments>", "".join(cuerpo) + "</w:comments>")
        else:
            c = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 f"<w:comments {ns}>" + "".join(cuerpo) + "</w:comments>")
            self._rel_nueva(
                "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments",
                "comments.xml")
            self._content_type(
                "/word/comments.xml",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml")
        self.partes["word/comments.xml"] = c.encode("utf8")

        ex = self.partes.get("word/commentsExtended.xml")
        nuevos_ex = "".join(f'<w15:commentEx w15:paraId="{0xC0000000 + cid:08X}" w15:done="0"/>'
                            for cid, _ in self.comentarios)
        if ex:
            e = ex.decode("utf8").replace("</w15:commentsEx>", nuevos_ex + "</w15:commentsEx>")
        else:
            e = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 f"<w15:commentsEx {ns}>" + nuevos_ex + "</w15:commentsEx>")
            self._rel_nueva(
                "http://schemas.microsoft.com/office/2011/relationships/commentsExtended",
                "commentsExtended.xml")
            self._content_type(
                "/word/commentsExtended.xml",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.commentsExtended+xml")
        self.partes["word/commentsExtended.xml"] = e.encode("utf8")

    def _content_type(self, parte: str, tipo: str) -> None:
        ct = self.partes["[Content_Types].xml"].decode("utf8")
        if f'PartName="{parte}"' in ct:
            return
        ct = ct.replace("</Types>", f'<Override ContentType="{tipo}" PartName="{parte}"/></Types>')
        self.partes["[Content_Types].xml"] = ct.encode("utf8")

    def _content_type_default(self, extension: str, tipo: str) -> None:
        """Sin este `Default`, un `.docx` que estrena imágenes se abre como archivo dañado."""
        ct = self.partes["[Content_Types].xml"].decode("utf8")
        if f'Extension="{extension}"' in ct:
            return
        ct = ct.replace("<Types ", "<Types ", 1)
        ct = ct.replace("</Types>", f'<Default ContentType="{tipo}" Extension="{extension}"/></Types>')
        self.partes["[Content_Types].xml"] = ct.encode("utf8")

    # ------------------------------------------------------------------ guardado
    def ensamblar(self) -> str:
        out = []
        for i, (_, raw, gap) in enumerate(self.units):
            out.append(gap)
            out.append(raw)
            out.extend(self.nuevos.get(i, []))
        out.append(self.resto)
        return self.head + "".join(out) + self.tail

    def guardar(self, dst: Path | str, verificar: bool = True) -> dict:
        import xml.etree.ElementTree as ET
        nuevo = self.ensamblar()
        ET.fromstring(nuevo)                      # el XML tiene que parsear antes de escribir
        self._escribir_comentarios()
        for parte in ("word/comments.xml", "word/commentsExtended.xml",
                      "[Content_Types].xml", "word/_rels/document.xml.rels"):
            if parte in self.partes:
                ET.fromstring(self.partes[parte])
        self.partes["word/document.xml"] = nuevo.encode("utf8")
        for nombre, datos in self.medios:
            self.partes[nombre] = datos
        for nombre in self.partes:            # partes estrenadas por el pase (comentarios, medios)
            if nombre not in self.orden:
                self.orden.append(nombre)
        if verificar:
            assert nuevo.count("<w:sectPr") == self.xml0.count("<w:sectPr"), "se perdió un sectPr"
            viejos = set(re.findall(r'<w:commentRangeStart w:id="(\d+)"/>', self.xml0))
            nuevos_ids = set(re.findall(r'<w:commentRangeStart w:id="(\d+)"/>', nuevo))
            assert viejos <= nuevos_ids, f"anclas de comentario perdidas: {viejos - nuevos_ids}"
            assert nuevo.count("<w:tbl>") == self.xml0.count("<w:tbl>"), "se perdió una tabla"
        dst = Path(dst)
        # ⚠ 2026-09-07: un pase sobrescribió un `.docx` que el usuario había bajado de Google
        # Docs con comentarios nuevos, y sólo se recuperó porque había una copia de casualidad.
        # Desde entonces, si el destino existe y su contenido difiere del que este pase produce,
        # se respalda antes de escribir y se avisa. Nunca se pierde una versión de otra mano.
        if dst.exists():
            import hashlib
            previo = zipfile.ZipFile(dst).read("word/document.xml")
            if hashlib.sha256(previo).digest() != hashlib.sha256(nuevo.encode("utf8")).digest():
                marca = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
                respaldo = dst.with_name(f"{dst.stem} [respaldo {marca}]{dst.suffix}")
                shutil.copy2(dst, respaldo)
                autores = set(re.findall(
                    rb'<w:comment [^>]*w:author="([^"]*)"',
                    zipfile.ZipFile(dst).read("word/comments.xml")
                    if "word/comments.xml" in zipfile.ZipFile(dst).namelist() else b""))
                ajenos = {a.decode() for a in autores} - {self.autor}
                aviso = f"⚠ el destino existía y difería; respaldado en {respaldo.name}"
                if ajenos:
                    aviso += f" — TRAÍA COMENTARIOS DE {', '.join(sorted(ajenos))}"
                print(aviso)
                self.log.append(aviso)
        with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
            for nombre in self.orden:
                z.writestr(nombre, self.partes[nombre])
        return {
            "ins": nuevo.count("<w:ins "), "del": nuevo.count("<w:del "),
            "pPrChange": nuevo.count("<w:pPrChange "), "comentarios": len(self.comentarios),
            "figuras": nuevo.count("<w:drawing"), "tablas": nuevo.count("<w:tbl>"),
            "salida": str(dst),
        }
