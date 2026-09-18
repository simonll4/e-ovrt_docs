"""Tests de `verificar_entregable.py` — fixtures sintéticas, sin `.docx` real."""

from __future__ import annotations

import sys
import unittest
import zipfile
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import verificar_entregable as v  # noqa: E402

PLANTILLA = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body>{cuerpo}</w:body></w:document>"""


def parrafo(texto: str, estilo: str | None = None) -> str:
    ppr = f'<w:pPr><w:pStyle w:val="{estilo}"/></w:pPr>' if estilo else ""
    return f"<w:p>{ppr}<w:r><w:t>{texto}</w:t></w:r></w:p>"


def docx(ruta: Path, parrafos: list[str]) -> Path:
    with zipfile.ZipFile(ruta, "w") as zf:
        zf.writestr("word/document.xml", PLANTILLA.format(cuerpo="".join(parrafos)))
    return ruta


class TitulosSinEstiloTest(unittest.TestCase):
    """El defecto que motivó la herramienta: título que se ve como título y no lo es."""

    def test_detecta_el_titulo_numerado_sin_estilo(self) -> None:
        parrafos = [
            ("Heading2", "16. Marco Teórico"),
            ("", "16.6. Marco Ético-Legal"),
            ("Heading4", "16.6.2. Delimitación"),
        ]
        sueltos = v.titulos_sin_estilo(parrafos)
        self.assertEqual([("16.6", "16.6. Marco Ético-Legal")], sueltos)

    def test_no_marca_prosa_que_empieza_con_numero_de_otra_forma(self) -> None:
        parrafos = [("", "16 modelos fueron evaluados en el relevamiento.")]
        self.assertEqual([], v.titulos_sin_estilo(parrafos))

    def test_acepta_variantes_de_estilo_de_titulo(self) -> None:
        # `Ttulo3` no es un error de tipeo: es lo que exporta Google Docs cuando el documento
        # se editó en español (le quita la tilde a «Título» al normalizar el identificador).
        # El maestro del informe llegó así el 2026-09-08 y sus 420 títulos se reportaron como
        # «sin estilo de encabezado».
        for estilo in ("Heading3", "heading3", "Ttulo3", "Ttulo1", "Titulo2", "Título2", "Title"):
            with self.subTest(estilo=estilo):
                self.assertEqual([], v.titulos_sin_estilo([(estilo, "16.3. Percepción")]))

    def test_filtra_por_seccion_pedida(self) -> None:
        parrafos = [("", "15.9. Suelto en 15"), ("", "16.6. Suelto en 16")]
        self.assertEqual(["16.6"], [n for n, _ in v.titulos_sin_estilo(parrafos, ("16",))])


class NumeracionTest(unittest.TestCase):
    def test_detecta_el_hueco_que_deja_una_subseccion_eliminada(self) -> None:
        # Caso real: sobrevive 16.7.6 tras eliminar 16.7.3, .4 y .5.
        problemas = v.huecos_de_numeracion(["16.7.1", "16.7.2", "16.7.6"])
        self.assertEqual(1, len(problemas))
        self.assertIn("16.7.3", problemas[0])
        self.assertIn("16.7.5", problemas[0])

    def test_detecta_desorden(self) -> None:
        problemas = v.huecos_de_numeracion(["15.2.1", "15.2.3", "15.2.2"])
        self.assertTrue(any("fuera de orden" in p for p in problemas))

    def test_detecta_arranque_distinto_de_uno(self) -> None:
        # Caso real: el Bloque A quedó con 15.2.1.1.3 y 15.2.1.1.5 tras podar fichas.
        problemas = v.huecos_de_numeracion(["15.2.1.1.3", "15.2.1.1.5"])
        self.assertTrue(any("arranca en 3" in p for p in problemas))

    def test_secuencia_completa_no_reporta_nada(self) -> None:
        self.assertEqual([], v.huecos_de_numeracion(["16.1", "16.2", "16.3"]))


class FugasTest(unittest.TestCase):
    def test_detecta_identificadores_internos(self) -> None:
        for texto in ("aplicar AJ-1.09 acá", "ver R-17", "según PODA-04", "el ítem E1-25"):
            with self.subTest(texto=texto):
                self.assertTrue(v.fugas_de_andamiaje(texto), texto)

    def test_detecta_procedencia_del_kit(self) -> None:
        self.assertTrue(v.fugas_de_andamiaje("> SHA-256 del bloque: abc"))
        self.assertTrue(v.fugas_de_andamiaje("> Seleccion: documento completo"))

    def test_detecta_texto_de_instruccion_de_plantilla(self) -> None:
        self.assertTrue(v.fugas_de_andamiaje("Esto es clave para la plantilla: cuando…"))

    def test_no_confunde_los_codigos_de_preguntas_rectoras(self) -> None:
        # P-E1-01…P-E1-08 son parte legítima del informe.
        self.assertEqual([], v.fugas_de_andamiaje("**P-E1-01. Presupuesto temporal.** ¿Qué…"))

    def test_prosa_limpia_no_dispara_nada(self) -> None:
        self.assertEqual([], v.fugas_de_andamiaje("El detector opera sobre cada fotograma."))


class MarcadoresTest(unittest.TestCase):
    def test_inventaria_por_tipo(self) -> None:
        texto = "[[PENDIENTE: x]] y [[FIGURA: y]] y [[FIGURA: z]]"
        self.assertEqual({"PENDIENTE": 1, "FIGURA": 2}, v.marcadores(texto))

    def test_sin_marcadores_devuelve_vacio(self) -> None:
        self.assertEqual({}, v.marcadores("prosa sin marcadores"))


class ReferenciasTest(unittest.TestCase):
    CUERPO = "Grounding DINO reporta 52,5 AP (Liu et al., 2024) y OWLv2 (Minderer et al., 2023).\n"
    REFS = ("\nReferencias\n\n"
            "Liu, S., Zeng, Z., & Ren, T. (2024). Grounding DINO. ECCV.\n"
            "Minderer, M., Gritsenko, A., & Houlsby, N. (2023). Scaling open-vocabulary. NeurIPS.\n")

    def test_cita_sin_entrada_es_dura(self) -> None:
        md = self.CUERPO + "Además, ARO (Yuksekgonul et al., 2023) lo muestra.\n" + self.REFS
        self.assertEqual(["Yuksekgonul"], v.citas_sin_referencia(md))

    def test_entrada_sin_cita_es_blanda(self) -> None:
        md = self.CUERPO + self.REFS + "Amirante, A. (2014). Janus. ACM.\n"
        self.assertEqual(["Amirante"], v.referencias_huerfanas(md))

    def test_documento_coherente_no_reporta_nada(self) -> None:
        md = self.CUERPO + self.REFS
        self.assertEqual([], v.citas_sin_referencia(md))
        self.assertEqual([], v.referencias_huerfanas(md))

    def test_sin_seccion_de_referencias_no_inventa_hallazgos(self) -> None:
        self.assertEqual([], v.citas_sin_referencia(self.CUERPO))
        self.assertEqual([], v.referencias_huerfanas(self.CUERPO))

    def test_detecta_la_misma_autoria_con_dos_anios(self) -> None:
        # Caso real: Liu 2023 en §16 y Liu 2024 en §15, misma obra.
        md = "Grounding DINO (Liu et al., 2023) y también (Liu et al., 2024).\n"
        self.assertTrue(any("Liu" in d for d in v.anios_divergentes(md)))

    def test_letras_de_desambiguacion_del_mismo_anio_no_son_divergencia(self) -> None:
        md = "Ver (Ren, 2024a) y (Ren, 2024b).\n"
        self.assertEqual([], v.anios_divergentes(md))


class VerificarIntegracionTest(unittest.TestCase):
    def test_documento_sano_pasa(self) -> None:
        with TemporaryDirectory() as tmp:
            ruta = docx(Path(tmp) / "sano.docx", [
                parrafo("16. Marco Teórico", "Heading2"),
                parrafo("16.1. Alcance", "Heading3"),
                parrafo("El marco delimita el objeto (Liu et al., 2024).", None),
                parrafo("16.2. Condiciones", "Heading3"),
                parrafo("Las condiciones emergen de la normativa.", None),
                parrafo("Referencias", "Heading2"),
                parrafo("Liu, S. (2024). Grounding DINO. ECCV.", None),
            ])
            informe = v.verificar(ruta)
            self.assertTrue(informe.ok, informe.duros)

    def test_documento_con_el_defecto_real_falla_y_lo_nombra(self) -> None:
        with TemporaryDirectory() as tmp:
            ruta = docx(Path(tmp) / "roto.docx", [
                parrafo("16. Marco Teórico", "Heading2"),
                parrafo("16.1. Alcance", "Heading3"),
                parrafo("16.2. Condiciones", None),          # estilo perdido
                parrafo("Prosa cualquiera.", None),
            ])
            informe = v.verificar(ruta)
            self.assertFalse(informe.ok)
            self.assertTrue(any("sin estilo" in x and "16.2" in x for x in informe.duros))

    def test_informa_si_no_hay_cambios_controlados(self) -> None:
        with TemporaryDirectory() as tmp:
            ruta = docx(Path(tmp) / "x.docx", [parrafo("16. Marco", "Heading2")])
            informe = v.verificar(ruta)
            self.assertTrue(any("NO trae cambios controlados" in b for b in informe.blandos))

    def test_informa_los_cambios_controlados_cuando_los_hay(self) -> None:
        """Defecto real (2026-09-03): la comprobación corría sobre el XML pasado por
        ElementTree, que reescribe el prefijo `w:` a `ns0:`, de modo que TODO documento con
        cambios controlados se informaba como si no los trajera."""
        with TemporaryDirectory() as tmp:
            insertado = (
                '<w:p><w:pPr><w:pStyle w:val="Heading2"/></w:pPr>'
                '<w:ins w:id="1" w:author="X" w:date="2026-09-03T00:00:00Z">'
                "<w:r><w:t>16. Marco</w:t></w:r></w:ins>"
                '<w:del w:id="2" w:author="X" w:date="2026-09-03T00:00:00Z">'
                "<w:r><w:delText>viejo</w:delText></w:r></w:del></w:p>"
            )
            ruta = docx(Path(tmp) / "con-cambios.docx", [insertado])
            informe = v.verificar(ruta)
            self.assertTrue(any("trae cambios controlados" in b for b in informe.blandos))
            self.assertFalse(any("NO trae cambios controlados" in b for b in informe.blandos))

    def test_docx_ilegible_da_error_claro(self) -> None:
        with TemporaryDirectory() as tmp:
            ruta = Path(tmp) / "no-es-docx.docx"
            ruta.write_text("esto no es un zip", encoding="utf-8")
            with self.assertRaises(v.VerificacionError):
                v.verificar(ruta)

    def test_cli_devuelve_1_si_falla(self) -> None:
        with TemporaryDirectory() as tmp:
            ruta = docx(Path(tmp) / "roto.docx", [
                parrafo("16. Marco", "Heading2"),
                parrafo("16.1. Uno", None),
            ])
            self.assertEqual(1, v.main([str(ruta)]))


if __name__ == "__main__":
    unittest.main()
