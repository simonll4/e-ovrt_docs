import re
import tempfile
import unittest
from pathlib import Path

from herramientas import generar_project_kit as kit


REPO_ROOT = Path(__file__).resolve().parents[2]


class GeneratorCoreTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.workspace_root = Path(self.temp_dir.name)
        self.repo_root = self.workspace_root / "docs"
        self.repo_root.mkdir()

    def write(self, relative_path: str, content: str) -> Path:
        path = self.repo_root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def test_extract_source_stops_before_end_heading(self) -> None:
        source = self.write("source.md", "# A\nuno\n## B\ndos\n## C\ntres\n")
        spec = kit.SourceSlice("source.md", "## B", "## C")

        text, resolved, digest = kit.extract_source(spec, self.repo_root)

        self.assertEqual(text, "## B\ndos\n")
        self.assertEqual(resolved, source)
        self.assertRegex(digest, r"^[0-9a-f]{64}$")

    def test_rewrite_relative_links_keeps_label_and_canonical_path(self) -> None:
        text = "Ver [decision](../decisiones/adr.md) y [web](https://example.com)."

        actual = kit.rewrite_relative_links(
            text,
            self.repo_root / "informe/source.md",
            self.workspace_root,
        )

        self.assertIn("decision (fuente: `docs/decisiones/adr.md`)", actual)
        self.assertIn("[web](https://example.com)", actual)
        self.assertIsNone(re.search(r"\]\((?!https?://)", actual))


class ManifestAndCheckTest(unittest.TestCase):
    def test_manifest_covers_exactly_seven_stages(self) -> None:
        self.assertEqual(set(kit.STAGE_SOURCES), set(range(7)))

    def test_build_outputs_returns_exactly_two_knowledge_files(self) -> None:
        outputs = kit.build_outputs(REPO_ROOT, 1)

        self.assertEqual(
            {path.name for path in outputs},
            {"00-contexto-base.md", "01-etapa-activa.md"},
        )

    def test_check_detects_stale_generated_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "00-contexto-base.md"
            path.write_text("contenido obsoleto\n", encoding="utf-8")

            errors = kit.check_outputs({path: "contenido vigente\n"})

        self.assertTrue(any("desactualizado" in error for error in errors), errors)


class ProjectDocumentationContractTest(unittest.TestCase):
    def test_readme_defines_four_file_upload_and_all_stage_commands(self) -> None:
        # Contrato vigente desde 2026-08-16 (operacion/122 §6-ter): 2 .md generados
        # por etapa + los 2 DOCX del entregable. El v1.1 completo NO se sube.
        readme = (REPO_ROOT / "informe/project-kit/README.md").read_text(encoding="utf-8")

        self.assertIn("cuatro archivos", readme)
        self.assertIn("`00-contexto-base.md`", readme)
        self.assertIn("`01-etapa-activa.md`", readme)
        self.assertIn("E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx", readme)
        self.assertIn("E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx", readme)
        self.assertIn("nunca subir", readme)
        for stage in range(7):
            self.assertIn(f"--etapa {stage}", readme)
        self.assertNotIn("nivel1/", readme)

    def test_project_instructions_define_current_truth_hierarchy(self) -> None:
        instructions = (
            REPO_ROOT / "informe/project-kit/INSTRUCCIONES-PROJECT.md"
        ).read_text(encoding="utf-8")

        expected_order = [
            "paquete de etapa activa",
            "estado vigente del contexto base",
            "banners de actualización",
            "cuerpos históricos",
        ]
        positions = [instructions.index(item) for item in expected_order]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("No inventes cifras", instructions)
        self.assertIn("contradicción", instructions)


class GovernanceMigrationTest(unittest.TestCase):
    def test_old_manifest_is_superseded_by_versioned_kit(self) -> None:
        manifest = (
            REPO_ROOT
            / "informe/ajustes/gobierno/98-project-claude-manifiesto-e-instrucciones.md"
        ).read_text(encoding="utf-8")

        self.assertIn("REEMPLAZADO", manifest[:1_200])
        self.assertIn("informe/project-kit/README.md", manifest[:1_200])

    def test_indexes_point_to_versioned_kit(self) -> None:
        index_paths = [
            REPO_ROOT / "00-indice.md",
            REPO_ROOT / "informe/00-indice-informe.md",
            REPO_ROOT / "informe/ajustes/gobierno/00-README-gobierno.md",
        ]
        for path in index_paths:
            with self.subTest(path=path):
                self.assertIn(
                    "informe/project-kit/README.md",
                    path.read_text(encoding="utf-8"),
                )

    def test_writer_guide_points_to_new_kit(self) -> None:
        guide = (REPO_ROOT / "GUIA-REDACTORES.md").read_text(encoding="utf-8")

        self.assertIn("informe/project-kit/README.md", guide)
        self.assertNotIn("kit es solo para el knowledge", guide)

    def test_adr_summary_reports_functional_distribution_and_remaining_gaps(self) -> None:
        status = (
            REPO_ROOT / "decisiones/estado-de-implementacion-adrs.md"
        ).read_text(encoding="utf-8")
        summary = status.split("## 1. Detalle por ADR", maxsplit=1)[0]

        self.assertIn("funcionalmente implementado", summary.lower())
        self.assertIn("webconsole", summary)
        self.assertIn("orquestación", summary)
        self.assertNotIn("repo hermano es esqueleto", summary)
        # Los tres pendientes del 08-12 se cerraron el 08-13: el resumen no puede
        # volver a declararlos abiertos (defecto de propagación, doc 119).
        self.assertNotIn("sin commits", summary)
        self.assertIn("2026-08-13", summary)

    def test_generated_context_carries_current_finetuning_state(self) -> None:
        generated = kit.build_outputs(REPO_ROOT, 1)
        base = next(
            text
            for path, text in generated.items()
            if path.name == "00-contexto-base.md"
        )

        # 2026-08-15 (noche): T-FT-043 se cerró — la corrida full quedó ENVIADA
        # (job 1167640). El estado que "manda sobre el resto" debe decirlo.
        self.assertIn("T-FT-043 esta CERRADA", base)
        self.assertIn("1167640", base)
        # Los cuerpos históricos se conservan (convención del set: se enmienda con ✎, no
        # se reescribe), pero ninguna declaración superada puede quedar suelta: donde
        # aparezca, la corrección tiene que estar pegada. Es el defecto de propagación
        # que costó T-FT-023 y la familia "sin commits" (doc 119).
        for superada in ("cero jobs full", "último eslabón", "cero full"):
            desde = 0
            while (encontrado := base.find(superada, desde)) != -1:
                # La enmienda puede ir antes o después: lo que se exige es adyacencia,
                # no un orden. (Una enmienda que cita la frase para declararla superada
                # lleva el número arriba; un cuerpo histórico lo lleva abajo.)
                ventana = base[max(0, encontrado - 900) : encontrado + 900]
                self.assertIn(
                    "1167640",
                    ventana,
                    f"«{superada}» quedó sin la enmienda del envío al lado",
                )
                desde = encontrado + 1
        # Enviar no es medir: la distinción es la que impide que el informe presente
        # una comparación que todavía no existe.
        self.assertIn("el envio **no es un\n  resultado**", base)
        self.assertIn("1166583", base)
        self.assertIn("optimizer 12/12", base)
        self.assertIn("no es reserva ni promesa", base)
        self.assertNotIn("corrida completa lista para envío manual", base)
        # T-FT-023 se cerró el 2026-08-13: el estado que "manda sobre el resto" no
        # puede seguir listándola como causa abierta del NO-GO (doc 119).
        self.assertIn("procedencia T-FT-023 (cerrada el\n  2026-08-13", base)
        self.assertNotIn("procedencia T023", base)
        # 2026-08-15: D-FT-08/12/13 firmadas Y T-FT-031/032 cerradas la misma jornada
        # (doc 120). El NO-GO quedó reducido a full-authorization + RUN manual; el
        # bloque que "manda sobre el resto" no puede volver a listar decisiones ni
        # gates técnicas como abiertas (mismo defecto de propagación que T-FT-023 y
        # T023 en el doc 119).
        self.assertIn("no queda ninguna decision humana pendiente", base)
        self.assertIn("baseline YOLOE-26s corrio UNA vez", base)
        self.assertIn("0,0002", base)  # recall CR-01 agregado de la baseline (doc 120)
        self.assertNotIn("NO-GO** por D-FT-08/T-FT-005", base)
        self.assertNotIn("evaluacion T-FT-031 y baseline YOLOE-26s T-FT-032", base)
        # La rama no se funde con el núcleo: sin cifra del checkpoint ajustado.
        self.assertIn("no hay cifra del checkpoint\n  ajustado", base)
        # La sonda `machinery` quedó derogada SOLO para T1 — el alcance de la
        # derogación es parte de la declaración, no un detalle.
        self.assertIn("D-FT-13", base)
        self.assertIn("derogada para T1 y reasignada a T2/T3", base)
        self.assertNotIn(
            "en estado `propuesta` y pendiente de firma del usuario", base
        )

    def test_generated_context_declares_three_coupling_patterns(self) -> None:
        """ADR-018 (2026-08-15): el kit no puede seguir describiendo dos acoples."""
        generated = kit.build_outputs(REPO_ROOT, 1)
        base = next(
            text
            for path, text in generated.items()
            if path.name == "00-contexto-base.md"
        )

        self.assertIn("TRES patrones de acople, no dos", base)
        self.assertIn("ADR-018", base)
        self.assertIn("BFF-subproceso", base)

    def test_generated_context_partitions_report_metrics(self) -> None:
        """Sólo `t_alert-system` es citable; las tres de alertas, no (doc 119 §7.3)."""
        generated = kit.build_outputs(REPO_ROOT, 1)
        base = next(
            text
            for path, text in generated.items()
            if path.name == "00-contexto-base.md"
        )

        self.assertIn("`t_alert-system` es **citable**", base)
        self.assertIn("NO son citables", base)

    def test_stage_packages_do_not_reintroduce_obsolete_distribution_state(self) -> None:
        stage_three = kit.build_outputs(REPO_ROOT, 3)
        stage_four = kit.build_outputs(REPO_ROOT, 4)
        active_three = next(
            text for path, text in stage_three.items() if path.name == "01-etapa-activa.md"
        )
        active_four = next(
            text for path, text in stage_four.items() if path.name == "01-etapa-activa.md"
        )

        obsolete_phrases = [
            "Distribución de alertas** (canal de notificación) | Especificada, no implementada",
            "Módulo de distribución** | *(no implementado — línea punteada)",
            "sigue **sin implementar** (el repo es un esqueleto",
            "es un esqueleto de paquete sin lógica ni commits",
        ]
        for phrase in obsolete_phrases:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, active_three)
                self.assertNotIn(phrase, active_four)
        self.assertIn("funcionalmente implementado", active_three)
        self.assertIn("funcionalmente implementado", active_four)

    def test_generated_knowledge_avoids_obsolete_current_claims(self) -> None:
        obsolete_phrases = [
            "distribucion minima - en alcance, aun no implementada",
            "en alcance, aun no implementada",
            "distribucion mqtt declarada no implementada",
            "tramo de distribucion, no implementado",
            "far/hora no reportable",
        ]

        for stage in range(7):
            generated = "\n".join(kit.build_outputs(REPO_ROOT, stage).values())
            normalized = (
                generated.casefold()
                .replace("ó", "o")
                .replace("ú", "u")
                .replace("—", "-")
                .replace("**", "")
            )
            for phrase in obsolete_phrases:
                with self.subTest(stage=stage, phrase=phrase):
                    self.assertFalse(
                        phrase in normalized,
                        f"La etapa {stage} reintrodujo la afirmacion obsoleta: {phrase}",
                    )


if __name__ == "__main__":
    unittest.main()
