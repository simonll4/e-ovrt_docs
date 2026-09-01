#!/usr/bin/env python3
"""Compuerta del pase 6 de la Etapa 2 (desacople normativo de §17.1).

Uso:
  python3 verificar_anclas_pase6.py --pre  <ruta a la v1.6.docx>   # antes de aplicar
  python3 verificar_anclas_pase6.py --post <ruta a la v1.7.docx>   # después de aplicar

--pre  verifica que las 32 anclas del mapa de reemplazos existan exactamente 1 vez.
--post verifica que las anclas hayan desaparecido, que los greps prohibidos den cero
       y que los invariantes se conserven (76 ecuaciones OMML, 27 comentarios,
       1 sola cita a Disposición 10/2015, marcador [[PENDIENTE]] intacto).

Sale con código 0 sólo si TODO pasa. Especificación: correcciones-etapa-2-pase-6.md.
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"

ANCLAS = {
 "E2-68": "derivadas del marco de seguridad laboral y construcción (Decreto N.º 911/1996, 1996; Ley N.º 19.587, 1972).",
 "E2-69": "configuración de escenas con y sin infracción deliberada.",
 "E2-70": "requiere gestión de consentimiento libre, expreso e informado e información previa a los participantes, conforme al régimen de protección de datos personales y videovigilancia aplicable (Argentina, 2000; Disposición 10/2015, 2015).",
 "E2-71a": "Ley N.º 25.326 y Disposición 10/2015",
 "E2-71b": "Las pruebas con personas en el campo visual requieren consentimiento informado e información previa. El carácter académico y controlado del prototipo atenúa el perfil de riesgo, pero no elimina las obligaciones de resguardo y minimización.",
 "E2-72": "y el marco normativo argentino aplicable a protección de datos personales y videovigilancia.",
 "E2-73": "la brecha entre la identificación normativa de condiciones de riesgo y su traducción en consultas textuales",
 "E2-74": "El universo de condiciones de riesgo identificado en el análisis normativo de la fundamentación teórica abarca categorías como uso de EPP (casco, chaleco, calzado), protección contra caídas en altura, delimitación de áreas de riesgo, control de circulación con maquinaria, orden y limpieza e instalaciones eléctricas provisorias.",
 "E2-75a": "la categoría normativa de origen",
 "E2-75b": "Cat. normativa",
 "E2-75c": "con su categoría normativa, componente evaluador",
 "E2-76a": "que refleja el perfil temporal del riesgo, entendido como",
 "E2-76b": "La fundamentación de cada nivel se apoya en la normativa argentina aplicable y en el perfil temporal de consecuencias asociado a cada tipo de exposición.",
 "E2-77": "El Decreto 911/96 establece las medidas de prevención frente al riesgo de caída de personas y los trabajos con riesgo de caída a distinto nivel (arts. 52 a 57), y regula la operación de vehículos y maquinaria automotriz junto con la protección frente a la circulación vehicular —señalización, vallado, equipos de alta visibilidad, vigías— (arts. 246 a 249). En ambos casos, la exposición observada",
 "E2-78": "El Decreto 911/96 regula la provisión, uso, condiciones y vida útil de los equipos de protección personal y la vestimenta de trabajo (arts. 98 a 106), y la provisión de casco de seguridad para tareas con riesgos específicos (art. 107). La ausencia de casco",
 "E2-79": "La obligación de emplear elementos reflectivos o de alta visibilidad se vincula con los trabajos nocturnos y con la construcción de carreteras en uso (Decreto 911/96, arts. 63 y 70), y puede complementarse con la Resolución SRT 299/2011 sobre registración y constancia de entrega de ropa de trabajo y EPP. La ausencia de chaleco",
 "E2-80a": "el perfil temporal del riesgo que fundamenta la asignación de severidad",
 "E2-80b": "Perfil temporal del riesgo",
 "E2-80.PR-01": " (Decreto 911/96, arts. 50, 98–102 y 107)",
 "E2-80.PR-02": " (Decreto 911/96, arts. 47, 63 y 70)",
 "E2-80.PR-03": " (Decreto 911/96, arts. 52, 54–56 y 112)",
 "E2-80.PR-04": " (Decreto 911/96, arts. 52 y 54–56)",
 "E2-80.PR-05": " (Decreto 911/96, arts. 47, 61, 70, 71 y 246–249; Ley 19.587, arts. 8 y 9)",
 "E2-80.PR-06": " (Decreto 911/96, arts. 66–69, 95(a), 139, 140(e)–(f), 156 y 176)",
 "E2-81": "Los artículos normativos referenciados en la columna “Perfil temporal del riesgo” fundamentan la severidad asignada a cada patrón a partir del tipo de exposición, la barrera preventiva omitida y la potencialidad de daño; no definen por sí mismos los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. Fuente: Elaboración propia basada en el análisis normativo del Decreto 911/96 y la Ley 19.587.",
 "E2-82": "aunque presentes en la taxonomía normativa de la fundamentación teórica, no integran",
 "E2-83a": "y la cobertura normativa (C2)",
 "E2-83b": "Proporción de categorías anotadas que se corresponden con alguna condición de riesgo de la taxonomía operacionalizada en la taxonomía de condiciones de riesgo, patrones y prompts, derivada del marco normativo argentino.",
 "E2-87": "Ese régimen prevé, además, la inscripción de las bases de datos con datos personales ante la autoridad de aplicación (AAIP); su aplicabilidad al material experimental del proyecto y el recaudo adoptado se documentan a continuación.",
 "E2-84": "producción de material controlado en el EBE bajo consentimiento y minimización.",
 "E2-85": "rigen las salvaguardas de minimización, consentimiento y ausencia de tratamiento biométrico de la Sección 17.1.10.1.",
 "E2-86": "La taxonomía de severidad definida en la taxonomía de condiciones de riesgo, patrones y prompts exige",
 "E2-88": "Aplicar minimización, acceso restringido y registro explícito de finalidad y condiciones de captura.",
}

# E2-80b ("Perfil temporal del riesgo", con mayúscula) aparece 2 veces en la v1.6:
# el encabezado de la Tabla 21 y la nota p0134 (que E2-81 reescribe entera).
OCURRENCIAS_PRE = {"E2-80b": 2}

GREPS_PROHIBIDOS_POST = [
    "911/96", "19.587", "SRT 299", "arts.", "normativa argentina aplicable",
    "taxonomía normativa", "análisis normativo", "obertura normativa",
    "Cat. normativa", "categoría normativa", "infracción deliberada",
    "atenúa el perfil", "identificación normativa", "Perfil temporal del riesgo",
]

# Texto que DEBE seguir existiendo tras el pase (frases-escudo y decisiones).
GUARDRAILS_POST = [
    "no equivale a una sanción ni a una determinación automática de incumplimiento normativo",
    "[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción",
    "(Argentina, 2000; Disposición 10/2015, 2015)",  # única cita directa (D-P6-1)
    "La severidad ordena prioridades temporales del protocolo",  # E2-76 aplicado
]


def extraer_texto(docx_path):
    z = zipfile.ZipFile(docx_path)
    doc = ET.fromstring(z.read("word/document.xml"))
    parrafos = []
    for p in doc.iter(W + "p"):
        parrafos.append("".join(t.text or "" for t in p.iter(W + "t")))
    n_omath = sum(1 for _ in doc.iter(M + "oMath"))
    n_marcas = sum(1 for tag in (W + "ins", W + "del") for _ in doc.iter(tag))
    try:
        com = ET.fromstring(z.read("word/comments.xml"))
        n_com = len(com.findall(W + "comment"))
    except KeyError:
        n_com = 0
    return "\n".join(parrafos), n_omath, n_com, n_marcas


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ("--pre", "--post"):
        print(__doc__)
        return 2
    modo, ruta = sys.argv[1], sys.argv[2]
    texto, n_omath, n_com, n_marcas = extraer_texto(ruta)
    fallas = []

    if modo == "--pre":
        for k, a in ANCLAS.items():
            esperado = OCURRENCIAS_PRE.get(k, 1)
            n = texto.count(a)
            estado = "OK " if n == esperado else "FALLA"
            if n != esperado:
                fallas.append(k)
            print(f"{estado} {k}: {n} (esperado {esperado})")
    else:
        for k, a in ANCLAS.items():
            n = texto.count(a)
            if n:
                fallas.append(k)
                print(f"FALLA {k}: el ancla sigue presente ({n})")
        for g in GREPS_PROHIBIDOS_POST:
            n = texto.count(g)
            estado = "OK " if n == 0 else "FALLA"
            if n:
                fallas.append(g)
            print(f"{estado} grep prohibido {g!r}: {n}")
        for g in GUARDRAILS_POST:
            n = texto.count(g)
            estado = "OK " if n >= 1 else "FALLA"
            if not n:
                fallas.append(g)
            print(f"{estado} guardrail {g[:60]!r}…: {n}")
        for nombre, val, esperado in [
            ("ecuaciones m:oMath", n_omath, 76),
            ("comentarios", n_com, 27),
            ("cambios controlados", n_marcas, 0),
            ("citas 'Disposición 10/2015'", texto.count("Disposición 10/2015"), 1),
            ("marcador [[PENDIENTE", texto.count("[[PENDIENTE"), 1),
            ("escudo 'incumplimiento normativo'", texto.count("incumplimiento normativo"), 1),
        ]:
            estado = "OK " if val == esperado else "FALLA"
            if val != esperado:
                fallas.append(nombre)
            print(f"{estado} invariante {nombre}: {val} (esperado {esperado})")

    print(f"\n{'✅ TODO OK' if not fallas else '❌ ' + str(len(fallas)) + ' falla(s): ' + ', '.join(map(str, fallas))}")
    return 0 if not fallas else 1


if __name__ == "__main__":
    sys.exit(main())
