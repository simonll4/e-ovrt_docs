#!/usr/bin/env python3
"""Aplica el pase 6 de la Etapa 2 (desacople normativo de §17.1): v1.6 → v1.7.

Uso:
  python3 aplicar_pase6.py <v1.6.docx> <v1.7.docx>

Método: edita word/document.xml a nivel de bytes, tocando únicamente el contenido
de los nodos <w:t> que solapan cada ancla (el resto del XML queda byte-idéntico:
ecuaciones OMML, rangos de comentario, formato y atributos no se re-serializan).
Cada reemplazo declara cuántas ocurrencias espera; cualquier desvío ABORTA sin
escribir la salida. Especificación: correcciones-etapa-2-pase-6.md.
Después de aplicar, correr: verificar_anclas_pase6.py --post <v1.7.docx>.
"""
import re
import shutil
import sys
import zipfile

# (id, ancla, reemplazo, ocurrencias esperadas) — el ORDEN importa:
# E2-81 (nota de la Tabla 21) va antes que E2-80b, porque la nota contiene la
# cadena "Perfil temporal del riesgo" que E2-80b renombra en el encabezado.
REEMPLAZOS = [
 ("E2-68", "derivadas del marco de seguridad laboral y construcción (Decreto N.º 911/1996, 1996; Ley N.º 19.587, 1972).",
  "cuya relevancia preventiva, observabilidad y evaluabilidad están fundamentadas en la sección 16.2.", 1),
 ("E2-69", "configuración de escenas con y sin infracción deliberada.",
  "configuración de escenas con y sin las condiciones observables objetivo.", 1),
 ("E2-70", "requiere gestión de consentimiento libre, expreso e informado e información previa a los participantes, conforme al régimen de protección de datos personales y videovigilancia aplicable (Argentina, 2000; Disposición 10/2015, 2015).",
  "requiere gestión de consentimiento informado e información previa a los participantes, conforme a las salvaguardas de la Sección 17.1.10.1.", 1),
 ("E2-71a", "Ley N.º 25.326 y Disposición 10/2015",
  "Criterios ético-legales de la sección 16.6", 1),
 ("E2-71b", "Las pruebas con personas en el campo visual requieren consentimiento informado e información previa. El carácter académico y controlado del prototipo atenúa el perfil de riesgo, pero no elimina las obligaciones de resguardo y minimización.",
  "Las pruebas con personas en el campo visual requieren consentimiento informado e información previa, finalidad explícita, minimización, acceso restringido y retención acotada, conforme a la Sección 17.1.10.1.", 1),
 ("E2-72", "y el marco normativo argentino aplicable a protección de datos personales y videovigilancia.",
  "y los criterios ético-legales establecidos en la sección 16.6 y operacionalizados en la Sección 17.1.10.1.", 1),
 ("E2-73", "la brecha entre la identificación normativa de condiciones de riesgo y su traducción en consultas textuales",
  "la brecha entre la identificación de condiciones de riesgo preventivamente relevantes y su traducción en consultas textuales", 1),
 ("E2-74a", "El universo de condiciones de riesgo identificado en el análisis normativo de la fundamentación teórica abarca categorías como uso de EPP (casco, chaleco, calzado), protección contra caídas en altura, delimitación de áreas de riesgo, control de circulación con maquinaria, orden y limpieza e instalaciones eléctricas provisorias.",
  "La fundamentación teórica delimita las condiciones de riesgo observables por su relevancia preventiva, su evidencia visual anotable y su formulación evaluable (sección 16.2), y señala como posibles extensiones situaciones como el trabajo en altura, las zonas restringidas o la interacción con maquinaria.", 1),
 ("E2-74b", "no pretende cubrir la totalidad de ese espacio, sino",
  "no pretende cubrir ese espacio de manera exhaustiva, sino", 1),
 ("E2-75a", "la categoría normativa de origen", "el tipo de condición", 1),
 ("E2-75b", "Cat. normativa", "Tipo de condición", 1),
 ("E2-75c", "con su categoría normativa, componente evaluador", "con su tipo de condición, componente evaluador", 1),
 ("E2-76a", "que refleja el perfil temporal del riesgo, entendido como",
  "que refleja el perfil temporal de la condición, entendido como", 1),
 ("E2-76b", "La fundamentación de cada nivel se apoya en la normativa argentina aplicable y en el perfil temporal de consecuencias asociado a cada tipo de exposición.",
  "Cada nivel se define como una categoría metodológica de prioridad temporal, fundamentada en el perfil temporal de consecuencias asociado a cada tipo de exposición; la relevancia preventiva de las condiciones subyacentes está establecida en la sección 16.2. La severidad ordena prioridades temporales del protocolo y no constituye una calificación normativa de la situación observada.", 1),
 ("E2-77", "El Decreto 911/96 establece las medidas de prevención frente al riesgo de caída de personas y los trabajos con riesgo de caída a distinto nivel (arts. 52 a 57), y regula la operación de vehículos y maquinaria automotriz junto con la protección frente a la circulación vehicular —señalización, vallado, equipos de alta visibilidad, vigías— (arts. 246 a 249). En ambos casos, la exposición observada",
  "Es el caso de la exposición en altura sin protección visible y de la interacción próxima entre peatones y maquinaria en operación: en ambos, la exposición observada", 1),
 ("E2-78", "El Decreto 911/96 regula la provisión, uso, condiciones y vida útil de los equipos de protección personal y la vestimenta de trabajo (arts. 98 a 106), y la provisión de casco de seguridad para tareas con riesgos específicos (art. 107). La ausencia de casco",
  "La ausencia de casco", 1),
 ("E2-79", "La obligación de emplear elementos reflectivos o de alta visibilidad se vincula con los trabajos nocturnos y con la construcción de carreteras en uso (Decreto 911/96, arts. 63 y 70), y puede complementarse con la Resolución SRT 299/2011 sobre registración y constancia de entrega de ropa de trabajo y EPP. La ausencia de chaleco",
  "La ausencia de chaleco", 1),
 ("E2-80a", "el perfil temporal del riesgo que fundamenta la asignación de severidad",
  "el perfil temporal de la condición que fundamenta la asignación de severidad", 1),
 ("E2-81", "Los artículos normativos referenciados en la columna “Perfil temporal del riesgo” fundamentan la severidad asignada a cada patrón a partir del tipo de exposición, la barrera preventiva omitida y la potencialidad de daño; no definen por sí mismos los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. Fuente: Elaboración propia basada en el análisis normativo del Decreto 911/96 y la Ley 19.587.",
  "La severidad es una clasificación interna del protocolo, fundamentada en el perfil temporal de la condición; no constituye una calificación normativa de la situación observada ni define por sí misma los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. La relevancia preventiva de las condiciones se fundamenta en la sección 16.2. Fuente: elaboración propia.", 1),
 ("E2-80b", "Perfil temporal del riesgo", "Perfil temporal de la condición", 1),
 ("E2-80.PR-01", " (Decreto 911/96, arts. 50, 98–102 y 107)", "", 1),
 ("E2-80.PR-02", " (Decreto 911/96, arts. 47, 63 y 70)", "", 1),
 ("E2-80.PR-03", " (Decreto 911/96, arts. 52, 54–56 y 112)", "", 1),
 ("E2-80.PR-04", " (Decreto 911/96, arts. 52 y 54–56)", "", 1),
 ("E2-80.PR-05", " (Decreto 911/96, arts. 47, 61, 70, 71 y 246–249; Ley 19.587, arts. 8 y 9)", "", 1),
 ("E2-80.PR-06", " (Decreto 911/96, arts. 66–69, 95(a), 139, 140(e)–(f), 156 y 176)", "", 1),
 ("E2-82", "aunque presentes en la taxonomía normativa de la fundamentación teórica, no integran",
  "aunque preventivamente relevantes, no integran", 1),
 ("E2-83a", "y la cobertura normativa (C2)", "y la cobertura del catálogo experimental (C2)", 1),
 ("E2-83b", "Proporción de categorías anotadas que se corresponden con alguna condición de riesgo de la taxonomía operacionalizada en la taxonomía de condiciones de riesgo, patrones y prompts, derivada del marco normativo argentino.",
  "Proporción de categorías anotadas que se corresponden con alguna condición de riesgo del catálogo experimental (CR-01 a CR-06) definido en la Sección 17.1.5.2.", 1),
 ("E2-83c", "Cobertura normativa", "Cobertura del catálogo experimental", 1),
 ("E2-87", "Ese régimen prevé, además, la inscripción de las bases de datos con datos personales ante la autoridad de aplicación (AAIP); su aplicabilidad al material experimental del proyecto y el recaudo adoptado se documentan a continuación.",
  "Ese régimen contempla, además, requisitos administrativos asociados a las bases de datos con datos personales ante la autoridad de aplicación (AAIP), cuya aplicabilidad al contexto experimental debe determinarse; la decisión y el recaudo adoptado se documentan a continuación.", 1),
 ("E2-84", "producción de material controlado en el EBE bajo consentimiento y minimización.",
  "producción de material controlado en el EBE bajo las salvaguardas de la Sección 17.1.10.1.", 1),
 ("E2-85", "rigen las salvaguardas de minimización, consentimiento y ausencia de tratamiento biométrico de la Sección 17.1.10.1.",
  "rigen las salvaguardas de la Sección 17.1.10.1.", 1),
 ("E2-86", "La taxonomía de severidad definida en la taxonomía de condiciones de riesgo, patrones y prompts exige",
  "La clasificación de severidad definida en la Sección 17.1.5.3.2 exige", 1),
 ("E2-88", "Aplicar minimización, acceso restringido y registro explícito de finalidad y condiciones de captura.",
  "Aplicar las salvaguardas de la Sección 17.1.10.1, con registro explícito de finalidad y condiciones de captura.", 1),
]

WT = re.compile(r"<w:t(?P<attrs> [^>]*)?>(?P<txt>.*?)</w:t>", re.S)
PEND = re.compile(r"</w:p>")


def decode(s):
    return s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def encode(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def aplicar_uno(xml, ancla, nuevo):
    """Reemplaza la PRIMERA ocurrencia de `ancla` en el texto plano, editando
    sólo los <w:t> que la solapan. Devuelve el XML nuevo o None si no está."""
    # Flujo plano: fragmentos w:t + salto en cada </w:p> (nunca cruzar párrafos)
    frags = []      # (inicio_xml, fin_xml, attrs, texto_decodificado)
    stream = []     # piezas del texto plano
    pos_map = []    # (inicio_stream, fin_stream, idx_frag) sólo para w:t
    cursor = 0
    eventos = sorted(
        [(m.start(), m.end(), "t", m) for m in WT.finditer(xml)]
        + [(m.start(), m.end(), "p", m) for m in PEND.finditer(xml)]
    )
    for ini, fin, tipo, m in eventos:
        if tipo == "p":
            stream.append("\n")
            cursor += 1
        else:
            txt = decode(m.group("txt"))
            frags.append((m.start(), m.end(), m.group("attrs") or "", txt))
            stream.append(txt)
            pos_map.append((cursor, cursor + len(txt), len(frags) - 1))
            cursor += len(txt)
    plano = "".join(stream)
    i = plano.find(ancla)
    if i < 0:
        return None
    j = i + len(ancla)
    # nuevas cadenas por fragmento tocado
    nuevos = {}
    primero = True
    for s0, s1, k in pos_map:
        if s1 <= i or s0 >= j:
            continue
        _, _, attrs, txt = frags[k]
        pre = txt[: max(0, i - s0)]
        suf = txt[max(0, min(len(txt), j - s0)):]
        nuevos[k] = pre + (nuevo if primero else "") + suf
        primero = False
    # reconstrucción por bytes, de atrás hacia adelante
    out = xml
    for k in sorted(nuevos, reverse=True):
        ini, fin, attrs, _ = frags[k]
        t = nuevos[k]
        if (t != t.strip()) and 'xml:space="preserve"' not in attrs:
            attrs = attrs + ' xml:space="preserve"'
        out = out[:ini] + f"<w:t{attrs}>{encode(t)}</w:t>" + out[fin:]
    return out


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    origen, destino = sys.argv[1], sys.argv[2]
    with zipfile.ZipFile(origen) as z:
        xml = z.read("word/document.xml").decode("utf-8")

    for rid, ancla, nuevo, esperadas in REEMPLAZOS:
        n = 0
        while True:
            res = aplicar_uno(xml, ancla, nuevo)
            if res is None:
                break
            xml, n = res, n + 1
            if n > esperadas:
                print(f"❌ {rid}: más ocurrencias que las {esperadas} esperadas — ABORTO")
                return 1
        if n != esperadas:
            print(f"❌ {rid}: {n} reemplazos (esperados {esperadas}) — ABORTO, no se escribe salida")
            return 1
        print(f"OK  {rid}: {n} reemplazo(s)")

    shutil.copyfile(origen, destino)
    # reescribir el zip con el document.xml nuevo, resto byte-idéntico
    import os, tempfile
    tmp = destino + ".tmp"
    with zipfile.ZipFile(origen) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = xml.encode("utf-8")
            zout.writestr(item, data)
    os.replace(tmp, destino)
    print(f"\n✅ {len(REEMPLAZOS)} reemplazos aplicados → {destino}")
    print("Ahora correr: python3 verificar_anclas_pase6.py --post " + destino)
    return 0


if __name__ == "__main__":
    sys.exit(main())
