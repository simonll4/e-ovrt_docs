#!/usr/bin/env python3
"""Pase 5b — configuración del entrenamiento de la rama de ajuste fino.

Responde a los dos comentarios que el usuario dejó el 2026-09-07 sobre la Tabla 65 de §17.5:
«dejar clara cómo se configuró el entrenamiento: épocas, etc.» y «ver si esto corresponde a este
documento o al de implementación». La decisión, firmada por el usuario, es que la configuración
va a §17.4.7 —donde ya viven el conjunto de ajuste, su regla de partición y la desviación— y que
§17.5 conserva resultados y veredictos, ampliando su remisión.

  §17.4 v1.9 → v1.10   tres párrafos nuevos en 17.4.7, tras el de la desviación
  §17.5 v1.6 → v1.7    la remisión de 17.5.6 nombra la configuración; dos respuestas en comentario

INCREMENTAL: parte de los `.docx` VIGENTES, no de la base archivada, así que preserva los
comentarios que el usuario y su colega tengan sin resolver. Si el usuario baja una versión más
nueva de Google Docs, correr con `--origen-17-4` / `--origen-17-5` apuntando a ella.

Toda cifra sale de los artefactos de la jornada de ajuste fino en
`e-ovrt_experimental-setup/finetuning/`: los perfiles `configs/t1_yoloe26s_lp.yaml` y
`configs/t2_yoloe26s_full_v2.yaml`, y la configuración efectiva que registró cada corrida en
`weights/finetuned/full-1167640/args.yaml` y `weights/finetuned/full-1167982/args.yaml`.
"""
# ⚠️ NO RE-EJECUTAR SOBRE EL DOCUMENTO VIGENTE (2026-09-07).
# Los `--origen-*` por default apuntan a `desarrollando/archivado/`, así que correrlo tal cual
# reproduce la v1.10 y la v1.7 y PISA lo que el usuario haya hecho después en Google Docs. Para
# aplicar estos mismos cambios sobre una bajada nueva, pasar `--origen-17-4` / `--origen-17-5`
# apuntando a ella y `--destino-*` con la versión siguiente. El motor deja respaldo y avisa.

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pase_docx import Documento  # noqa: E402

BASE = Path(__file__).resolve().parent.parent / "informe/entregable/desarrollando"
ORIGEN_174 = BASE / (
    "archivado/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.9 (entrega del pase 5; base "
    "del pase 5b).docx")
DESTINO_174 = BASE / "E-OVRT-VDP_Seccion_17.4_Implementacion_v1.10 (sugerencias sin aceptar).docx"
ORIGEN_175 = BASE / (
    "archivado/E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.6 (bajada del usuario con "
    "sus 3 comentarios; base del pase 5b).docx")
DESTINO_175 = BASE / "E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.7 (sugerencias sin aceptar).docx"

PERFIL_COMUN = (
    "Los dos tramos entrenados compartieron el perfil de entrenamiento, porque la comparación "
    "por única variable obliga a mantenerlo idéntico. Las imágenes se procesaron a 640 píxeles "
    "de lado en lotes de ocho, con semilla fija y ejecución determinista, sobre la partición de "
    "2.946 imágenes de ajuste y 483 de validación. En cada tramo se conservó el punto de control "
    "de mejor precisión media sobre las cuatro clases de validación y no el de la última época."
)

REGIMEN = (
    "El régimen de época y de optimización es la diferencia declarada entre ambos. El primer "
    "tramo recorrió 10 épocas completas con la selección automática de optimizador de la "
    "biblioteca de entrenamiento, y su detención temprana quedó inoperante porque la paciencia "
    "configurada superaba ese techo. El segundo fijó un techo de 60 épocas y una detención "
    "tras 15 sin mejora, ambos valores registrados antes de observar resultado alguno, y "
    "declaró el optimizador de forma explícita, por descenso de gradiente "
    "estocástico con tasa de aprendizaje inicial 0,01, momento 0,937 y tres épocas de "
    "calentamiento. La detención se activó en la época 16 y la mejor época fue la primera, que "
    "es el dato sobre el que se apoya la lectura de colapso durante el entrenamiento."
)

HALLAZGO_OPTIMIZADOR = (
    "La declaración explícita del optimizador responde a un hallazgo de una corrida anterior del "
    "mismo tramo, descartada por esa causa. El modo automático de la biblioteca de entrenamiento "
    "deriva la tasa de aprendizaje del número de clases y no del alcance entrenable, de modo que "
    "asignaba el mismo valor a un tramo de 3.096 parámetros y a otro de 10,35 millones. Esa "
    "corrida se conservó como evidencia del hallazgo y no como candidata a incorporación."
)


def pase_17_4(origen: Path, destino: Path) -> int:
    d = Documento(origen)
    i = d.unica("El subconjunto de ajuste reunió 2.946 imágenes")
    j = d.unica("El cumplimiento de esa regla tuvo un límite que conviene declarar")
    if j != i + 1:
        raise SystemExit(f"anclas inesperadas en §17.4 (subconjunto u{i}, desviación u{j})")

    d.parrafo_nuevo(j, PERFIL_COMUN, muestra=i)
    d.parrafo_nuevo(j, REGIMEN, muestra=i)
    d.parrafo_nuevo(j, HALLAZGO_OPTIMIZADOR, muestra=i)

    d.comentario_en_nuevo(
        j, 0,
        "Responde al comentario sobre la Tabla 65 de §17.5, que pedía dejar clara la "
        "configuración del entrenamiento. Va acá porque §17.4 es donde vive el cómo está hecho, "
        "y estos tres párrafos continúan el del conjunto de ajuste y su regla de partición; "
        "§17.5 conserva resultados y veredictos y remite. Verificado contra el perfil de cada "
        "tramo y la configuración efectiva que registró la corrida: 640 px, lote 8, semilla 100 "
        "determinista, 2.946 y 483 imágenes, punto de control por mejor precisión media.")
    d.comentario_en_nuevo(
        j, 1,
        "Del artefacto de cada corrida: el primer tramo, 10 épocas con detención temprana "
        "inoperante (paciencia 100 sobre un techo de 10); el segundo, 60 épocas con paciencia "
        "15, SGD explícito lr0 0,01, momento 0,937 y 3 de calentamiento, detenido en la época "
        "16 con mejor época 1. Los dos valores del segundo tramo estaban firmados en su perfil "
        "antes de la corrida, que es lo que sostiene leer la parada como resultado y no como "
        "decisión tomada mirando la curva.")
    d.comentario_en_nuevo(
        j, 2,
        "Este párrafo es opcional y se puede borrar sin tocar los otros dos. Documenta por qué "
        "el segundo tramo declara el optimizador en vez de usar el modo automático: ese modo "
        "deriva la tasa de aprendizaje del número de clases, así que le daba la misma a un tramo "
        "de 3.096 parámetros y a otro de 10,35 millones. Es un hallazgo del proceso, no un "
        "resultado del banco. Si te parece detalle de más para el informe, se saca.")

    st = d.guardar(destino)
    print("\n".join(d.log))
    print(" ", st)
    return 0


def pase_17_5(origen: Path, destino: Path) -> int:
    d = Documento(origen)
    i = d.unica("un conjunto cuya composición y regla de partición declara la sección 17.4.7")
    d.reemplazar(
        i,
        "un conjunto cuya composición y regla de partición declara la sección 17.4.7",
        "un conjunto cuya composición, regla de partición y configuración de entrenamiento "
        "declara la sección 17.4.7")

    cap = d.unica("Curva de capacidad de la rama comparativa de ajuste fino")
    d.comentario(
        cap, "Curva de capacidad",
        "Sobre tu comentario «dejar clara cómo se configuró el entrenamiento». Quedó escrito en "
        "§17.4.7, en tres párrafos nuevos que siguen al del conjunto de ajuste: el perfil común a "
        "los dos tramos (640 px, lotes de ocho, semilla fija, 2.946 y 483 imágenes, punto de "
        "control por mejor precisión media) y el régimen de época de cada uno (10 épocas el "
        "primero; techo de 60 con detención tras 15 sin mejora el segundo, que se detuvo en la 16 "
        "con mejor época 1). Si preferís que viva acá, se mueve tal cual.")
    d.comentario(
        cap, "de la rama comparativa de ajuste fino",
        "Sobre tu comentario «ver si esto corresponde a este documento o al de implementación». "
        "Corresponde a implementación. §17.4 describe cómo está hecho y ya declara el conjunto de "
        "ajuste, su regla de partición y la desviación, así que la configuración del entrenamiento "
        "completa ese párrafo; §17.5 se queda con los resultados y los veredictos. Es la misma "
        "separación que las dos secciones sostienen en todo lo demás. La remisión del párrafo que "
        "cierra 17.5.6 se amplió para nombrarla.")

    st = d.guardar(destino)
    print("\n".join(d.log))
    print(" ", st)
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--origen-17-4", type=Path, default=ORIGEN_174)
    p.add_argument("--origen-17-5", type=Path, default=ORIGEN_175)
    p.add_argument("--destino-17-4", type=Path, default=DESTINO_174)
    p.add_argument("--destino-17-5", type=Path, default=DESTINO_175)
    a = p.parse_args()
    print("=== §17.4 ===")
    pase_17_4(a.origen_17_4, a.destino_17_4)
    print("\n=== §17.5 ===")
    pase_17_5(a.origen_17_5, a.destino_17_5)
    return 0


if __name__ == "__main__":
    sys.exit(main())
