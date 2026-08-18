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
            {"00-contexto-base.md", "01-etapa-1-activa.md"},
        )

    def test_stage_filename_is_unique_per_stage(self) -> None:
        names = {kit.stage_filename(stage) for stage in range(7)}

        self.assertEqual(len(names), 7)
        for stage in range(7):
            self.assertEqual(kit.stage_filename(stage), f"01-etapa-{stage}-activa.md")

    def test_generating_one_stage_does_not_touch_another_stages_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            repo_root = Path(temp_dir)
            outputs_three = kit.build_outputs(REPO_ROOT, 3, generated_on="2026-08-17")
            kit.write_outputs(
                {repo_root / path.name: content for path, content in outputs_three.items()}
            )
            stage_three_path = repo_root / "01-etapa-3-activa.md"
            before = stage_three_path.read_text(encoding="utf-8")

            outputs_four = kit.build_outputs(REPO_ROOT, 4, generated_on="2026-08-17")
            kit.write_outputs(
                {repo_root / path.name: content for path, content in outputs_four.items()}
            )

            self.assertEqual(stage_three_path.read_text(encoding="utf-8"), before)
            self.assertTrue((repo_root / "01-etapa-4-activa.md").is_file())

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
        self.assertIn("E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx", readme)
        self.assertIn("E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx", readme)
        self.assertIn("nunca subir", readme)
        for stage in range(7):
            self.assertIn(f"--etapa {stage}", readme)
            self.assertIn(f"`01-etapa-{stage}-activa.md`", readme)
        self.assertIn("--etapa all", readme)
        self.assertNotIn("nivel1/", readme)

    def test_project_instructions_fit_the_settings_box(self) -> None:
        # El cuadro de Project settings de ChatGPT corta en 8.000 caracteres. Nadie
        # avisa al pegar: lo que sobra se pierde en silencio, y lo último del archivo
        # es justamente el control final. El contrato no chequeaba largo, así que el
        # archivo llegó a 8.172 sin que se notara (2026-08-17).
        instructions = (
            REPO_ROOT / "informe/project-kit/INSTRUCCIONES-PROJECT.md"
        ).read_text(encoding="utf-8")

        self.assertLessEqual(
            len(instructions),
            8_000,
            f"las instrucciones miden {len(instructions)} caracteres y no entran en "
            "el cuadro de Project settings (limite 8.000)",
        )

    def test_project_instructions_do_not_freeze_volatile_state(self) -> None:
        # Las instrucciones declaran "nunca infieras avance ni resultados desde estas
        # instrucciones". Congelar ahi el estado de una jornada en curso contradice esa
        # regla y se desactualiza sin que el generador pueda enterarse: el estado vive
        # en el inventario CERRADO/ABIERTO del contexto base, que si se regenera.
        instructions = (
            REPO_ROOT / "informe/project-kit/INSTRUCCIONES-PROJECT.md"
        ).read_text(encoding="utf-8")

        for congelado in ("sin resultado", "no hay cifra del modelo ajustado", "Hoy:"):
            self.assertNotIn(congelado, instructions)
        self.assertIn("lo fija ese inventario, no", instructions)

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
        # 2026-08-17: la jornada T1 CERRÓ con NO-GO. El inventario CERRADO/ABIERTO es el
        # bloque que gana la jerarquía de verdad (INSTRUCCIONES §"Knowledge"), así que si
        # sigue diciendo que no hay cifra del ajustado, ChatGPT descarta un resultado
        # firmado. Mismo defecto de propagación que T-FT-023 y "sin commits" (doc 119),
        # pero en el peor lugar posible.
        self.assertIn("brazo T1: CERRADO con veredicto NO-GO", base)
        self.assertIn("0,0455", base)
        self.assertIn("-11,62 %", base)
        self.assertIn("hallazgo, no como fracaso", base)
        self.assertNotIn("(encolada, sin resultado)", base)
        # El hueco que queda es T2, y sólo T2.
        self.assertIn("**Resultado del brazo T2**: no existe", base)
        self.assertIn("T1 ya no es un hueco", base)
        self.assertIn("D-FT-14", base)
        self.assertIn("D-FT-15", base)
        self.assertIn("0,391208", base)  # umbral OV de T2, firmado antes del resultado
        # La secuencia (veredicto → enmienda posterior → márgenes pre-firmados) es el
        # argumento: si se suaviza, el encuadre se vuelve indefendible.
        self.assertIn("la\n  transparencia de la secuencia ES el argumento", base)
        self.assertIn('jamas por "falta de tiempo"', base)
        # Ninguna afirmación absoluta de "no hay cifra del ajustado" puede quedar suelta:
        # donde aparezca, la corrección tiene que estar pegada (patrón de adyacencia).
        desde = 0
        while (encontrado := base.find("no hay cifra del checkpoint", desde)) != -1:
            # Las fuentes enmiendan con saltos de línea y prefijos de cita en el medio
            # ("SUPERADO\n> el 2026-08-17"), así que la ventana se normaliza antes de
            # buscar: si no, el guard falla por formato y no por contenido.
            ventana = " ".join(
                base[max(0, encontrado - 300) : encontrado + 700].replace(">", " ").split()
            ).casefold()
            self.assertTrue(
                "superado el 2026-08-17" in ventana or "brazo t2" in ventana,
                "«no hay cifra del checkpoint ajustado» quedó sin la enmienda al lado",
            )
            desde = encontrado + 1
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

    def test_generated_context_declares_two_coupling_patterns(self) -> None:
        """ADR-020 (2026-08-18) derogó ADR-018: los acoples volvieron a ser DOS.

        Historia del guard, que importa porque el número cambió tres veces en cuatro
        días: eran dos (ADR-008/009 + ADR-003) → ADR-018 sumó BFF-subproceso y fueron
        tres → ADR-019 le dio servicio HTTP al distribuidor (seguían siendo tres, con
        un borrador que llegó a decir "cuatro" y se corrigió) → ADR-020 bajó el
        subproceso a fallback operativo y volvieron a ser **dos**. Lo que este test
        protege es que el kit describa el estado VIGENTE, no cualquiera de los tres
        anteriores.
        """
        generated = kit.build_outputs(REPO_ROOT, 1)
        base = next(
            text
            for path, text in generated.items()
            if path.name == "00-contexto-base.md"
        )

        # El estado vigente: dos patrones, y el distribuidor dentro del primero.
        self.assertIn("los patrones de acople son DOS, no tres", base)
        self.assertIn("ADR-020", base)
        self.assertIn("HTTP config-driven en los TRES modulos", base)
        # El fallback existe en el código pero NO es arquitectura: no va al informe.
        self.assertIn("fallback operativo", base)
        self.assertIn("NO escribir", base)
        # Ninguna de las tres versiones superadas puede quedar suelta: el cuerpo
        # histórico se conserva (convención del set), pero con la enmienda pegada.
        for superada in (
            "TRES patrones de acople, no dos",
            "BFF-subproceso",
            "que es CLI y no servicio",
        ):
            desde = 0
            while (encontrado := base.find(superada, desde)) != -1:
                # Ventana SIMÉTRICA y ancha: la enmienda puede ir antes (cuando cita la
                # frase para declararla superada) o después (cuerpo histórico enmendado).
                ventana = base[max(0, encontrado - 1600) : encontrado + 1600]
                self.assertIn(
                    "ADR-020",
                    ventana,
                    f"«{superada}» quedó sin la enmienda de ADR-020 al lado",
                )
                desde = encontrado + 1
        # Y el error del borrador de ADR-019 no puede reaparecer.
        self.assertNotIn("cuarto patron de acople", base)

    def test_generated_context_allows_talking_about_containerization(self) -> None:
        """La containerización está diferida, pero SÍ se menciona en el informe.

        Precisión del usuario (2026-08-18): "no es un resultado del informe" se leía
        como "no lo menciones", y no es eso. Es trabajo comprometido posterior a la
        entrega, su razón es la reproducibilidad, su documentación operativa vive en
        los repos, y en el informe se describe como compromiso con su causa. El riesgo
        que este guard cubre es el opuesto al habitual: no que se afirme de más, sino
        que un redactor lo omita creyendo que está prohibido.
        """
        generated = kit.build_outputs(REPO_ROOT, 1)
        base = next(
            text for path, text in generated.items() if path.name == "00-contexto-base.md"
        )

        self.assertIn("La containerizacion SI se puede mencionar en el informe", base)
        self.assertIn("reproducibilidad", base)
        # …pero sin habilitar el error simétrico: nunca en presente ni como manual.
        self.assertIn("Como NO escribirla", base)
        self.assertIn("el informe no es un manual", base)

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
            text for path, text in stage_three.items() if path.name == "01-etapa-3-activa.md"
        )
        active_four = next(
            text for path, text in stage_four.items() if path.name == "01-etapa-4-activa.md"
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
