import tempfile
import unittest
import zipfile
from pathlib import Path

from herramientas import extraer_informe as ext


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"


def _docx(body_xml: str) -> bytes:
    return (
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        f'<w:document xmlns:w="{W_NS}" xmlns:m="{M_NS}">'
        f"<w:body>{body_xml}</w:body></w:document>"
    ).encode("utf-8")


def _p(text: str, style: str = "", extra_ppr: str = "", run_props: str = "") -> str:
    ppr = ""
    if style or extra_ppr:
        pstyle = f'<w:pStyle w:val="{style}"/>' if style else ""
        ppr = f"<w:pPr>{pstyle}{extra_ppr}</w:pPr>"
    rpr = f"<w:rPr>{run_props}</w:rPr>" if run_props else ""
    return f'<w:p>{ppr}<w:r>{rpr}<w:t xml:space="preserve">{text}</w:t></w:r></w:p>'


class DocxFixtureMixin:
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

    def write_docx(self, body_xml: str) -> Path:
        path = Path(self.temp_dir.name) / "prueba.docx"
        with zipfile.ZipFile(path, "w") as zf:
            zf.writestr("word/document.xml", _docx(body_xml))
        return path


class ConversionTest(DocxFixtureMixin, unittest.TestCase):
    def test_headings_map_to_markdown_one_level_down(self) -> None:
        docx = self.write_docx(
            _p("15. Estado del Arte", style="Heading1")
            + _p("Texto plano del capítulo.")
            + _p("15.1. Alcance", style="Heading2")
        )
        md = ext.docx_a_markdown(docx)
        self.assertIn("## 15. Estado del Arte", md)
        self.assertIn("Texto plano del capítulo.", md)
        self.assertIn("### 15.1. Alcance", md)

    def test_title_style_maps_to_h1(self) -> None:
        docx = self.write_docx(_p("E-OVRT-VDP", style="Title"))
        self.assertIn("# E-OVRT-VDP", ext.docx_a_markdown(docx))

    def test_bold_and_italic_runs(self) -> None:
        body = (
            "<w:p><w:r><w:rPr><w:b/></w:rPr><w:t>negrita</w:t></w:r>"
            '<w:r><w:t xml:space="preserve"> y </w:t></w:r>'
            "<w:r><w:rPr><w:i/></w:rPr><w:t>cursiva</w:t></w:r></w:p>"
        )
        md = ext.docx_a_markdown(self.write_docx(body))
        self.assertIn("**negrita** y *cursiva*", md)

    def test_bold_disabled_explicitly_is_not_bold(self) -> None:
        body = '<w:p><w:r><w:rPr><w:b w:val="0"/></w:rPr><w:t>normal</w:t></w:r></w:p>'
        md = ext.docx_a_markdown(self.write_docx(body))
        self.assertIn("normal", md)
        self.assertNotIn("**normal**", md)

    def test_heading_runs_ignore_bold(self) -> None:
        body = (
            '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr>'
            "<w:r><w:rPr><w:b/></w:rPr><w:t>15. Estado del Arte</w:t></w:r></w:p>"
        )
        md = ext.docx_a_markdown(self.write_docx(body))
        self.assertIn("## 15. Estado del Arte", md)
        self.assertNotIn("**", md)

    def test_table_becomes_gfm_pipe_table(self) -> None:
        cell = lambda t: f"<w:tc><w:p><w:r><w:t>{t}</w:t></w:r></w:p></w:tc>"  # noqa: E731
        body = (
            "<w:tbl>"
            f"<w:tr>{cell('Modelo')}{cell('mAP50')}</w:tr>"
            f"<w:tr>{cell('gdino-tiny-560')}{cell('0,41')}</w:tr>"
            "</w:tbl>"
        )
        md = ext.docx_a_markdown(self.write_docx(body))
        self.assertIn("| Modelo | mAP50 |", md)
        self.assertIn("| --- | --- |", md)
        self.assertIn("| gdino-tiny-560 | 0,41 |", md)

    def test_equation_leaves_visible_marker(self) -> None:
        body = (
            f'<w:p><m:oMath xmlns:m="{M_NS}"><m:r><m:t>x=1</m:t></m:r></m:oMath></w:p>'
        )
        md = ext.docx_a_markdown(self.write_docx(body))
        self.assertIn(ext.MARCA_ECUACION, md)

    def test_drawing_leaves_visible_marker(self) -> None:
        body = "<w:p><w:r><w:drawing/></w:r></w:p>"
        md = ext.docx_a_markdown(self.write_docx(body))
        self.assertIn(ext.MARCA_FIGURA, md)

    def test_list_paragraphs_get_bullet_prefix(self) -> None:
        extra = '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
        docx = self.write_docx(_p("primer ítem", extra_ppr=extra))
        self.assertIn("- primer ítem", ext.docx_a_markdown(docx))


class SeccionTest(unittest.TestCase):
    MD = (
        "# Portada\n\nintro\n\n## 15. Estado del Arte\n\ncuerpo 15\n\n"
        "### 15.1. Alcance\n\ncuerpo 15.1\n\n## 16. Marco Teórico\n\ncuerpo 16\n"
    )

    def test_extrae_desde_heading_hasta_siguiente_mismo_nivel(self) -> None:
        out = ext.extraer_seccion(self.MD, "15")
        self.assertIn("## 15. Estado del Arte", out)
        self.assertIn("cuerpo 15.1", out)
        self.assertNotIn("Marco Teórico", out)
        self.assertNotIn("Portada", out)

    def test_seccion_anidada(self) -> None:
        out = ext.extraer_seccion(self.MD, "15.1")
        self.assertIn("### 15.1. Alcance", out)
        self.assertNotIn("## 15. Estado del Arte", out)

    def test_seccion_inexistente_es_error(self) -> None:
        with self.assertRaises(ext.SeccionNoEncontrada):
            ext.extraer_seccion(self.MD, "99")


class BannerTest(unittest.TestCase):
    def test_banner_declara_derivada_fecha_y_docx(self) -> None:
        banner = ext.construir_banner(
            "96c — Texto extraído del informe v1.1: §15 Estado del Arte",
            "E-OVRT-VDP_v1.1_05062026-sin-indice.docx",
            fecha="2026-08-16",
        )
        self.assertTrue(banner.startswith("# 96c — "))
        self.assertIn("Extracción derivada (2026-08-16)", banner)
        self.assertIn("E-OVRT-VDP_v1.1_05062026-sin-indice.docx", banner)
        self.assertIn("nunca", banner)  # "al editar ... nunca este archivo"


if __name__ == "__main__":
    unittest.main()
