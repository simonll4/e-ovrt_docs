#!/usr/bin/env python3
"""Generate the minimal ChatGPT Project kit from canonical report sources."""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


class KitError(RuntimeError):
    """Raised when a source cannot be composed without ambiguity."""


@dataclass(frozen=True)
class SourceSlice:
    path: str
    start_heading: str | None = None
    end_heading: str | None = None
    note: str = ""


MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
EXTERNAL_TARGET_RE = re.compile(r"^(?:https?://|mailto:)", re.IGNORECASE)
GENERATED_DATE_RE = re.compile(r"^> Generado el (\d{4}-\d{2}-\d{2})\.", re.MULTILINE)

BASE_MAX_BYTES = 500 * 1024
STAGE_MAX_BYTES = 750 * 1024
STAGE_FILENAME_RE = re.compile(r"^01-etapa-[0-6]-activa\.md$")


def stage_filename(stage: int) -> str:
    """Nombre de archivo propio de cada etapa: no se pisan entre si."""

    return f"01-etapa-{stage}-activa.md"

BASE_SOURCES = (
    SourceSlice("GUIA-REDACTORES.md"),
    SourceSlice("13-glosario-y-convenciones-de-lectura.md"),
    SourceSlice("informe/ajustes/08-manual-de-aplicacion.md"),
    SourceSlice("sintesis/resultados-y-conclusiones.md"),
    SourceSlice(
        "decisiones/estado-de-implementacion-adrs.md",
        end_heading="## 1. Detalle por ADR",
        note="encuadre y tabla resumen vigentes; el detalle historico queda fuera",
    ),
    SourceSlice("nucleo/10-registro-alcance-y-exclusiones.md"),
    SourceSlice("nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md"),
    SourceSlice(
        "operacion/114-relevamiento-distribucion-alertas.md",
        end_heading="## 1. Veredicto en una línea",
        note="banners de actualizacion vigentes; el cuerpo inferior es la foto inicial",
    ),
    SourceSlice(
        "informe/ajustes/gobierno/99-materiales-de-cierre.md",
        start_heading="## 4. Limitaciones y ADRs",
        end_heading="### 4.2 ADRs: dos series que se confunden",
        note="lista vigente de limitaciones L1-L8; la cronologia de ADRs queda fuera",
    ),
    SourceSlice(
        "../e-ovrt_experimental-setup/results/index.md",
        end_heading="## Limitaciones declaradas",
        note="argumento y reglas de lectura; L1-L8 se incorporan desde gobierno/99",
    ),
    SourceSlice(
        "../e-ovrt_experimental-setup/results/index.md",
        start_heading="## Verificación de estos índices",
        note="verificacion, licencias y procedencia; omite el rotulo historico de L1",
    ),
    SourceSlice("../e-ovrt_experimental-setup/results/bench_imagenes/index.md"),
    SourceSlice("../e-ovrt_experimental-setup/results/bench_nivel_a/index.md"),
    SourceSlice("../e-ovrt_experimental-setup/results/clip_bench/index.md"),
    SourceSlice("../e-ovrt_experimental-setup/results/realtime/index.md"),
)

STAGE_SOURCES: dict[int, tuple[SourceSlice, ...]] = {
    0: (
        SourceSlice(
            "informe/entregable/96a-informe-v11-frontmatter-intro-objetivos-plan.md",
            start_heading="## 11. Glosario, Listado de Símbolos y Convenciones",
            note="texto vigente de las secciones 11 a 14",
        ),
        SourceSlice(
            "informe/ajustes/00-mapa-de-ajustes.md",
            start_heading="## 4. Etapa 0 — ajustes transversales del frontmatter (§11–§14)",
            end_heading="## 5. Tablero global",
            note="ajustes AJ-0.01 a AJ-0.07",
        ),
    ),
    1: (
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-1.md",
            note="pase 1 de alineacion de la etapa 1 (2026-08-27): YA APLICADO Y VERIFICADO en el"
            " documento de trabajo - NO volver a aplicarlo. Sus comentarios E1-01 a E1-12 y sus"
            " decisiones D-E1-1 a D-E1-6 siguen rigiendo como criterio de lectura; su seccion 1"
            " (la plataforma efectivamente construida) sigue siendo el blanco de la alineacion y"
            " NO se cita en el informe",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-2.md",
            note="pase 2 (2026-08-27): revision de la primera iteracion y E1-13 a E1-23. YA APLICADO"
            " Y VERIFICADO (su seccion 6) salvo tres RESIDUALES que SI son trabajo pendiente:"
            " R1 (una fila de la Tabla 4 sin sostener en prosa), R2 (formato de la ficha de"
            " Florence-2) y R3 (delta de referencias: altas Kumar 2022, Lee 2023, OASIS 2019,"
            " Ultralytics 2026; Luxonis lleva letra s. f.-b; bajas de PODA-18). Sus decisiones"
            " D-E1-7 (la Tabla A.1 se conserva y corrige: PODA-17 invertida) y D-E1-8 rigen",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-5.md",
            note="pase 5 (2026-08-27/28): **YA APLICADO Y VERIFICADO** - NO volver a aplicarlo. Fue el"
            " pase de formato y terminologia (F1-F6); la entrega de GPT llego con cambios controlados y"
            " cumplio los seis. Su seccion de verificacion registra ademas E1-57 (una capacidad no"
            " implementada descrita como el sistema, corregida) y E1-58 (formato roto en mitad de"
            " palabra heredado del pase 3, reparado). **Con esto la ETAPA 1 queda CERRADA.**",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-4.md",
            note="pase 4 (2026-08-27): **YA APLICADO Y VERIFICADO** - E1-52 y E1-53 se repararon de forma"
            " deterministica sobre el .docx (estilos de encabezado trasplantados de hermanas sanas y"
            " renumeracion 16.7.6 a 16.7.3), con prueba de no-regresion: el texto quedo identico."
            " **El CONTENIDO de la etapa 1 esta CERRADO; el unico trabajo activo es el pase 5 (formato"
            " y terminologia).** Su seccion 0"
            " certifica que entro el pase 3 completo y su seccion 2 fija el flujo obligatorio:"
            " **se trabaja dentro del Project, NO sobre Drive**",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-3.md",
            note="pase 3 (2026-08-27): **YA APLICADO Y VERIFICADO** (constancia en la seccion 0 del"
            " pase 4) - NO volver a aplicarlo. Fue el relevamiento que AJ-1.16 declaraba pendiente:"
            " cubrio la seccion 16 y el Anexo A, que nunca habian recibido pase. Sus comentarios"
            " E1-24 a E1-51 y sus decisiones D-E1-9 a D-E1-12 siguen rigiendo como criterio de"
            " lectura -en particular la inversion de la poda 17 y las enmiendas a las podas 06, 07"
            " y 11-. **D-E1-11 sigue ABIERTA y es del equipo**: la aplicabilidad de la inscripcion"
            " ante la AAIP, hoy marcada en el texto con un [[PENDIENTE]] que debe viajar",
        ),
        SourceSlice(
            "informe/entregable/90d-etapa1-texto-extraido.md",
            note="TEXTO BASE FINAL DE LA ETAPA 1 - **el DESARROLLO: seccion 15 y seccion 16**,"
            " extraido de 'E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx', con los **cinco pases YA APLICADOS Y"
            " VERIFICADOS**, los 16 AJ-1.xx resueltos, las podas 01-11 aplicadas, formato y"
            " terminologia unificados (el verificador da OK). **SUPERA al 96c y al 96d** del informe"
            " v1.1, que por eso ya no forman parte de este paquete. **El entregable de la etapa es SOLO"
            " el desarrollo**: el Anexo A y el listado de referencias salieron del documento por"
            " decision del usuario -los arma el equipo- y quedaron en `90e`. **La etapa esta CERRADA:"
            " no queda trabajo de contenido, formato ni terminologia** sobre este texto; no cambiar una"
            " palabra de fondo. Lo unico abierto de fondo es D-E1-11, que decide el equipo y viaja"
            " como [[PENDIENTE]]",
        ),
        SourceSlice(
            "informe/entregable/90e-etapa1-anexo-a-y-referencias.md",
            note="Anexo A y listado de Referencias, ya corregidos en los cuatro pases pero FUERA del entregable de la etapa: el Anexo A pertenece a la seccion 19 y las referencias son globales del informe, y los arma el equipo. Se conserva porque **el cuerpo de la seccion 15 cita la Tabla A.1 y la 15.3.3 cita la Tabla A.2**: si esas tablas no llegan a la seccion 19, quedan dos remisiones colgadas. NO se redacta desde aca",
        ),
        SourceSlice(
            "informe/ajustes/01-etapa-1-fundamentacion-teorica.md",
            note="tablero ORIGINAL AJ-1.01 a AJ-1.16 (2026-08-10), con el relevamiento que dio"
            " origen a la etapa y las cifras de vara con su marca de confianza. **Los 16 estan"
            " RESUELTOS** -AJ-1.04 y AJ-1.05 por eliminacion de las fichas, AJ-1.09 en el Anexo A,"
            " AJ-1.16 por el pase 3-. Se conserva como historia y como fuente de las cifras: NO es"
            " una lista de tareas",
        ),
        SourceSlice(
            "informe/entregable/borradores/vara-15.md",
            note="borrador historico (2026-08-16) de la vara del 15: YA INTEGRADO al texto base"
            " (AJ-1.01/1.02/1.13 estan aplicados). Material de consulta para las cifras y sus marcas"
            " de confianza, NO redactar desde aca",
        ),
        SourceSlice(
            "informe/ajustes/07-critica-extension-y-poda.md",
            end_heading="## 3. §15 Estado del Arte (21.575 palabras)",
            note="encuadre de la crítica de extension: la regla de gobierno (no hay limite de"
            " extension y no se poda por cuota, se poda por APORTE) y los cinco criterios C1 a C5"
            " que cada PODA cita por su sigla. Sin esto, las fichas de poda no se pueden leer",
        ),
        SourceSlice(
            "informe/ajustes/07-critica-extension-y-poda.md",
            start_heading="## 3. §15 Estado del Arte (21.575 palabras)",
            end_heading="## 5. §17.1 Consolidación Metodológica (32.222 palabras)",
            note="podas 01 a 11 aplicables a las secciones 15 y 16: YA APLICADAS Y VERIFICADAS (etapa 1"
            " CERRADA 2026-08-28) - se conservan solo como criterio de lectura, NO reaplicar."
            " Dos enmiendas del pase de alineacion: la poda 04 se aplica CON la excepcion E1-10"
            " (el parrafo de RTSP/RTP y la seccion 15.4.3 completa se conservan) y la poda 03 CON"
            " el matiz E1-08 (las metricas MOT se comprimen, no se eliminan)",
        ),
        SourceSlice(
            "informe/ajustes/07-critica-extension-y-poda.md",
            start_heading="## 7. §18, §19 y Referencias (12.339 palabras)",
            note="de este bloque, a la etapa 1 le tocan la poda 17 (Anexo A, que es su tercera"
            " pieza: decision D-E1-4) y la poda 18 (Referencias, que se poda sola al caer secciones"
            " y con el pase de AJ-1.10); las demas son de otras etapas. Incluye ademas el tablero"
            " completo y, sobre todo, los GUARDRAILS: su punto 1 protege 16.2 y 16.3 —el corazon"
            " conceptual de la tesis— de las podas 05 a 11, y su punto 6 fija que las adiciones de"
            " vara mandan sobre las podas (la poda les hace lugar, no compite con ellas)",
        ),
        SourceSlice("sintesis/fundamentos-teoricos.md"),
    ),
    2: (
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-2.md",
            note="EL PASE DE LA ETAPA 2 (2026-08-28): comentarios E2-01..E2-26 y decisiones D-E2-1..9."
            " **YA APLICADO Y VERIFICADO** en el documento de trabajo v1.3 (misma jornada; constancia en"
            " `correcciones-etapa-2-pase-2.md`) - **NO volver a aplicarlo**. Sigue rigiendo como criterio"
            " de lectura y manda sobre las fichas AJ-2.xx donde las precisa o corrige",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-2-pase-2.md",
            note="pase 2 de la etapa 2 (2026-08-28, noche): la VERIFICACION de la entrega v1.2 y el cierre en"
            " v1.3 - estado por unidad E2, los tres arreglos de forma E2-27..E2-29, los residuales que NO se"
            " corrigen, el delta de referencias (13 bajas) y lo que queda fuera del .docx (90g y handoffs)",
        ),
        SourceSlice(
            "informe/entregable/90f-etapa2-texto-extraido.md",
            note="TEXTO BASE VIGENTE de la seccion 17.1: extraido del documento de trabajo"
            " `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx` (2026-08-28), con el pase"
            " E2-01..E2-26 y el pase de formato F1-F6 **YA APLICADOS Y VERIFICADOS** (28.534 palabras,"
            " 118 titulos, verificador OK). No cambiar una palabra de fondo sin un pase nuevo explicito."
            " El 96b (v1.1 sin correcciones) queda como foto historica fuera del paquete. Las ecuaciones"
            " de Word aparecen como ⟦ECUACIÓN⟧: no son erratas",
        ),
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística",
            end_heading="## Referencias",
            note="Anexos C y D del informe v1.1 (texto vigente). Por D-E2-1 NO van en el .docx de la etapa:"
            " se corrigen aparte (AJ-2.07, duplicaciones de ajustes/09) y quedan en 90g para la seccion 19",
        ),
        SourceSlice(
            "operacion/130-relevamiento-plataforma-pre-etapa-2.md",
            start_heading="## 4. Protocolo §17.1 vs lo construido — la tabla que alimenta el pase de la Etapa 2",
            end_heading="## 7. Qué cambió en el set a partir de este relevamiento (misma jornada, 2026-08-28)",
            note="relevamiento de la plataforma del 2026-08-28: la tabla prescripcion -> CUMPLIDA/PARCIAL/NO"
            " EJERCIDA/DESVIADA por subseccion de 17.1 (lo que se declara en 17.4/17.5 y lo que se ajusta"
            " como protocolo en 17.1) y las decisiones D-E2 firmadas",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md",
            start_heading="## E. Hechos verificados en este pase — NO \"corregir\" estos valores",
            end_heading="## F. Mapa comentario → unidad — los 29 hilos, ninguno sin destino",
            note="hechos del pase 3 que dependen de la etapa 2: CPN/EN/TN y las siglas t_alert-system/TTFD/SDR"
            " NACEN en 17.1 (17.3 las usa sin redefinir) - no moverlas ni renombrarlas",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md",
            start_heading="## I. Diferidos y dependencias inversas",
            note="dependencias inversas hacia la etapa 2: C-1 (bautismo E-DIR/E-IND/E-HYB, ahora firmado por"
            " D-E2-2), el solape 17.3.3.1/17.3.3.2 y la anomalia de la sigla OMML en 17.1.7.5.1",
        ),
        SourceSlice("informe/ajustes/02-etapa-2-consolidacion-metodologica.md"),
        SourceSlice(
            "informe/ajustes/07-critica-extension-y-poda.md",
            start_heading="## 5. §17.1 Consolidación Metodológica (32.222 palabras)",
            end_heading="## 6. §17.3 Diseño arquitectónico (24.389 palabras)",
            note="podas 12 a 14 aplicables a la seccion 17.1",
        ),
    ),
    3: (
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4.md",
            note="pase de cierre 1 (2026-08-19): YA APLICADO - NO volver a aplicarlo; sus decisiones D1-D4 y la regla de autocontención SIGUEN RIGIENDO. Excepcion (✎ 2026-08-28, D-E2-2): el bautismo E-DIR/E-IND/E-HYB de D3/C-1 no quedo en §17.1 en su momento (E3-42 lo hizo nacer en §17.3.6.4); la etapa 2 lo aplica ahora en §17.1.5.4.2 y §17.3.6.4 debera recortar su glosa a una remision (dependencia inversa, pase 3 §I)",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-pase-2.md",
            note="pase de cierre 2 (2026-08-20): YA APLICADO Y VERIFICADO en el documento de trabajo (2026-08-23) - NO volver a aplicarlo; sus decisiones D-P2-1..6 siguen rigiendo como criterio de lectura",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md",
            note="pase de cierre 3 (2026-08-22): YA APLICADO Y VERIFICADO en el documento de trabajo (2026-08-23) - NO volver a aplicarlo; enmendo a E3-22 y E4-22, y su seccion D fija las restricciones de la etapa 5. Sus decisiones D-P3-1..6 siguen rigiendo",
        ),
        SourceSlice(
            "informe/entregable/90-etapa3-texto-extraido.md",
            note="TEXTO BASE VIGENTE de la seccion 17.3: extraido del documento de trabajo v1.4 (2026-08-23), con los tres pases YA aplicados y verificados. Es el texto sobre el que se revisa y se sigue trabajando",
        ),
        SourceSlice("informe/ajustes/03-etapa-3-diseno-arquitectonico.md"),
        SourceSlice("informe/ajustes/material-etapa-3/92-anexo-concrecion-tecnica.md"),
        SourceSlice("informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md"),
        SourceSlice("informe/ajustes/material-etapa-3/93-redlines-etapa3.md"),
        SourceSlice("informe/ajustes/material-etapa-3/94-secciones-nuevas-etapa3.md"),
        SourceSlice(
            "informe/ajustes/07-critica-extension-y-poda.md",
            start_heading="## 6. §17.3 Diseño arquitectónico (24.389 palabras)",
            end_heading="## 7. §18, §19 y Referencias (12.339 palabras)",
            note="podas 15 y 16 aplicables a la seccion 17.3",
        ),
    ),
    4: (
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4.md",
            note="pase de cierre 1 (2026-08-19): YA APLICADO - NO volver a aplicarlo; sus decisiones D1-D4 y la regla de autocontención SIGUEN RIGIENDO. Excepcion (✎ 2026-08-28, D-E2-2): el bautismo E-DIR/E-IND/E-HYB de D3/C-1 no quedo en §17.1 en su momento (E3-42 lo hizo nacer en §17.3.6.4); la etapa 2 lo aplica ahora en §17.1.5.4.2 y §17.3.6.4 debera recortar su glosa a una remision (dependencia inversa, pase 3 §I)",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-pase-2.md",
            note="pase de cierre 2 (2026-08-20): YA APLICADO Y VERIFICADO en el documento de trabajo (2026-08-23) - NO volver a aplicarlo; sus decisiones D-P2-1..6 siguen rigiendo como criterio de lectura",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md",
            note="pase de cierre 3 (2026-08-22): YA APLICADO Y VERIFICADO en el documento de trabajo (2026-08-23) - NO volver a aplicarlo; enmendo a E3-22 y E4-22, y su seccion D fija las restricciones de la etapa 5. Sus decisiones D-P3-1..6 siguen rigiendo",
        ),
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 17.4. Implementación del prototipo experimental",
            end_heading="### 17.5. Evaluación y validación del prototipo",
            note="placeholder vigente de la seccion 17.4",
        ),
        SourceSlice("informe/ajustes/04-etapa-4-implementacion.md"),
        SourceSlice(
            "informe/entregable/90b-etapa4-texto-extraido.md",
            note="TEXTO BASE VIGENTE de la seccion 17.4: extraido del documento de trabajo v1.6 (re-extraido 2026-08-28), con los tres pases YA aplicados y verificados. Es el texto sobre el que se revisa y se sigue trabajando. Pendiente detectado por operacion/130 R-01: su parrafo sobre el orden de disparo con distribucion debe decir control -> distribucion -> medios",
        ),
        SourceSlice(
            "informe/entregable/borradores/17-4.md",
            note="borrador historico (2026-08-20), ANTERIOR a los pases 2 y 3 y ya superado por el documento de trabajo v1.6: material de consulta, NO redactar desde aca",
        ),
        SourceSlice("informe/ajustes/material-etapa-3/92-anexo-concrecion-tecnica.md"),
        SourceSlice("informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md"),
        SourceSlice(
            "operacion/130-relevamiento-plataforma-pre-etapa-2.md",
            end_heading="## 5. Set documental — auditoría documento contra documento",
            note="FOTO VIGENTE de la plataforma (2026-08-28): estado de los seis repos, hechos citables por"
            " modulo con ruta:linea en datos/130-…, divergencias doc<->codigo y la tabla protocolo 17.1 vs"
            " construido. Manda sobre operacion/97 en todo lo que difieran",
        ),
        SourceSlice(
            "operacion/97-relevamiento-plataforma-2026-08-05.md",
            note="FOTO HISTORICA del 2026-08-05, SUPERADA por operacion/130: decia 4 repos, dos servicios HTTP y"
            " distribucion no implementada. Solo para trazabilidad; no citar su estado",
        ),
        SourceSlice("nucleo/14-mapa-de-la-cadena.md"),
        SourceSlice("nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md"),
    ),
    5: (
        SourceSlice(
            "informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md",
            note="pase de cierre 3 (2026-08-22): su seccion D fija las restricciones que rigen la redaccion de la etapa 5",
        ),
        SourceSlice(
            "informe/ajustes/09-pase-de-tablas-y-lectura-de-cierre.md",
            note="revision de cierre (2026-08-21/22): su seccion 2 es el plan de tablas del 17.5 (7 quedan, 6 a prosa, 3 al Anexo D, 1 fuera) y sus hallazgos de la seccion 3 estan RESUELTOS",
        ),
        SourceSlice(
            "informe/entregable/90c-etapa5-texto-extraido.md",
            note="TEXTO BASE VIGENTE de la seccion 17.5: extraido del documento de trabajo v1.3 (2026-08-23), redactado bajo D-P3-6 y verificado (185 cifras, cero inventadas, cero marcadores de cifra). Es el texto sobre el que se revisa y se sigue trabajando",
        ),
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 17.5. Evaluación y validación del prototipo",
            end_heading="### 17.6. Documentación técnica, repositorio y evidencias de cierre",
            note="placeholder de la seccion 17.5 en el maestro: sigue vacio porque el documento de trabajo todavia no se integro",
        ),
        SourceSlice("informe/ajustes/05-etapa-5-evaluacion-y-validacion.md"),
        SourceSlice(
            "informe/entregable/borradores/vara-15.md",
            note="la vara de literatura: sin ella no se puede escribir en tres tiempos",
        ),
        SourceSlice(
            "informe/ajustes/gobierno/99-materiales-de-cierre.md",
            start_heading="## 1. Inventario de figuras y tablas, con su artefacto de origen",
            end_heading="## 2. Anexo de reproducibilidad",
            note="figuras y tablas aplicables a resultados",
        ),
    ),
    6: (
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 17.6. Documentación técnica, repositorio y evidencias de cierre",
            note="secciones 17.6, 18, 19 y referencias vigentes",
        ),
        SourceSlice("informe/ajustes/06-etapa-6-documentacion-y-cierre.md"),
        SourceSlice(
            "informe/ajustes/07-critica-extension-y-poda.md",
            start_heading="## 7. §18, §19 y Referencias (12.339 palabras)",
            note="podas 17 y 18, tablero y guardrails aplicables al cierre",
        ),
        SourceSlice(
            "informe/ajustes/gobierno/99-materiales-de-cierre.md",
            start_heading="## 2. Anexo de reproducibilidad",
            end_heading="## 6. Lo que este armado encontró, y qué hay que decidir",
            note="reproducibilidad, licencias, limitaciones y mecanismos",
        ),
    ),
}

STAGE_CONTRACTS: dict[int, tuple[str, ...]] = {
    1: (
        "**Restriccion propia de esta etapa: el estado del arte tiene que quedar alineado"
        " con la plataforma que efectivamente se construyo.** Un modelo, metodo o protocolo"
        " se desarrolla si tiene rol en el trabajo; y todo resultado que el informe reporte"
        " mas adelante necesita aca su **vara** (cifra publicada) o su **brecha** declarada."
        " Ese es el criterio que ordena tanto las adiciones como las podas.",
        "La seccion 1 del pase de alineacion describe la plataforma construida. Es el blanco"
        " de la alineacion y **no se cita**: en las secciones 15 y 16 no entra ningun numero"
        " propio, ningun experimento y ninguna eleccion de diseno del proyecto.",
        "Estado del trabajo (✎ 2026-08-27, cierre): **el CONTENIDO de la etapa 1 esta CERRADO.**"
        " Los pases 1, 2 y 3 estan APLICADOS Y VERIFICADOS sobre las tres piezas -seccion 15,"
        " seccion 16 y Anexo A-, los 16 `AJ-1.xx` estan resueltos y las podas 01-11 aplicadas."
        " **NO reaplicar nada de eso, ni volver a redactar.**",
        "**ETAPA 1 CERRADA (✎ 2026-08-28): los cinco pases estan aplicados y verificados.** Documento"
        " final: `E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx` (secciones 15 y 16). **No hay trabajo pendiente"
        " de redaccion, formato ni terminologia.** Si este paquete se abre para otra cosa, no rehacer"
        " nada de lo hecho; cualquier cambio sobre la etapa 1 requiere un pase nuevo, explicito.",
        "**El entregable de la etapa es SOLO el desarrollo (secciones 15 y 16).** Sin Anexo A, sin"
        " Anexo B y sin listado de Referencias: los arma el equipo. El Anexo A y las referencias ya"
        " corregidos estan en `90e` para la seccion 19, porque el cuerpo cita las Tablas A.1 y A.2.",
        "**No se trabaja sobre Drive ni editando el documento en la nube.** El texto vigente"
        " completo de la etapa esta en este paquete (`90d`: secciones 15 y 16),"
        " asi que ir a buscar el documento afuera es innecesario y ademas lo daña: los dos"
        " defectos que quedan aparecieron exactamente asi. El detalle del circuito de entrega"
        " esta en la seccion 'Como se trabaja y como se entrega' del contexto base y en la"
        " seccion 2 del pase 4.",
        "Queda **una decision del equipo, no del redactor**: D-E1-11, la aplicabilidad de la"
        " inscripcion ante la AAIP al contexto experimental. Esta correctamente marcada en el"
        " texto con `[[PENDIENTE: ...]]` y **ese marcador debe viajar**: no se completa con una"
        " estimacion ni se borra.",
    ),
    2: (
        "**Restriccion propia de esta etapa: §17.1 se corrige COMO PROTOCOLO** (regla de"
        " no-anacronismo, mapa regla 5). Entran decisiones, definiciones, criterios y valores de"
        " configuracion elegidos dentro de rangos declarados; **NO entran resultados medidos ni"
        " estados de implementacion**: eso se declara en §17.4/§17.5. Lo que el protocolo"
        " prescribio y no se ejercio (templates de prompt, vocabulario aislado-vs-completo cruzado,"
        " espanol, doble anotacion/kappa, MOT17/OVT-B y metricas MOT, NVDEC) **NO se borra ni se"
        " 'corrige' en §17.1**: queda como protocolo y §17.5 lo reporta como no ejercido.",
        "**Texto base = `90f` = §17.1 v1.3 (28.534 palabras, 118 titulos, Tablas 16–38), con el pase"
        " `correcciones-etapa-2.md` (E2-01..E2-26: las 12 fichas AJ-2.xx, la AJ-2.13, las podas 12–14 y"
        " los handoffs de las etapas 1 y 3) y el pase de formato F1–F6 YA APLICADOS Y VERIFICADOS el"
        " 2026-08-28. **La seccion esta CERRADA en contenido; no reaplicar nada.** Lo que queda de la"
        " etapa es externo al .docx: `90g` (Anexos C y D) y los handoffs hacia 17.3/17.4/17.5. **Guardrails:** §17.1.5 y §17.1.7 no se comprimen (no hay"
        " 'segunda vuelta'); los nombres de metrica que se ven vacios o como ⟦ECUACIÓN⟧ son"
        " objetos de ecuacion de Word, NO erratas; CPN/EN/TN y las siglas t_alert-system/TTFD/SDR"
        " nacen aca y §17.3/§17.4 las usan — no renombrar.",
        "**Decisiones firmadas (2026-08-28):** D-E2-1 el .docx es SOLO §17.1 (Anexos C y D aparte, en"
        " 90g) · D-E2-2 los codigos E-DIR/E-IND/E-HYB se bautizan en §17.1.5.4.2 y §17.3.6.4 recorta su"
        " glosa a una remision · D-E2-5 el nivel intermedio 'estado observable por persona' se declara"
        " en §17.1.7.3.1 (AJ-2.13) · D-E2-6 MOT17/OVT-B y metricas MOT intactos con ⊘ explicito ·"
        " D-E2-3 la regla 're-alerta ≠ FP' va en §17.1.7.8.3 · D-E2-4 los 4.000/7.000 ms entran como"
        " decision dentro del rango de la Tabla 24, sin la palabra 'efectivos' · D-E2-7 marcador"
        " espejo de la AAIP en §17.1.11 · D-E2-8 PODA-14 solo recorta §17.1.4.",
        "**Formato:** el documento hereda del maestro un defecto que el pase corrige: §17.1.1 esta en"
        " estilo Heading 2 (el nivel de §17.1) con tabulador tras el numero — debe ser Heading 3 con"
        " espacio, como sus hermanas §17.1.2…§17.1.12. La remision a 'la seccion 16.7.6' es hoy"
        " §16.7.3. Verificacion: `verificar_entregable.py <entrega.docx> --seccion 17.1`.",
    ),
}

STAGE_DESCRIPTIONS = {
    0: "Etapa 0: secciones 11 a 14 y ajustes transversales",
    1: "Etapa 1: secciones 15 y 16 (CERRADA 2026-08-28; el Anexo A corregido vive en 90e)",
    2: "Etapa 2: seccion 17.1 (los Anexos C y D se corrigen aparte, D-E2-1)",
    3: "Etapa 3: seccion 17.3, diseno arquitectonico",
    4: "Etapa 4: seccion 17.4, implementacion del prototipo",
    5: "Etapa 5: seccion 17.5, evaluacion y validacion",
    6: "Etapa 6: secciones 17.6, 18 y 19",
}

BASE_PREAMBLE = """
## Que esta CERRADO y que esta ABIERTO (leer antes de redactar)

Lo **cerrado** se escribe como hecho, en pasado y sin condicionales: ya fue ejecutado y
verificado, y dejarlo como duda seria falsear el estado del trabajo. Lo **abierto** no se
escribe: se deja un marcador visible para que lo complete quien tiene el dato.

**CERRADO — se afirma:**

1. Distribucion de alertas: implementada, verificada e integrada (vista de webconsole,
   orquestacion y repositorio versionado, 2026-08-13). Su estatuto es trabajo comprometido
   con estado declarado a la entrega; los canales adicionales siguen fuera de alcance.
2. Identidad de sujeto: implementada y medida. Lo excluido son las metricas MOT.
3. Comparacion de estrategias de deteccion: ejecutada (la directa fue vetada por
   precision y la hibrida por disyuncion fue ejecutada y refutada).
4. Referencia temporal del banco: anotacion **humana** y congelada; se reporta como
   resultado, no como verificacion preliminar.
5. Rama de ajuste fino (E-04): **JORNADA COMPLETA en sus tres tramos, cerrada con
   veredictos pre-registrados** — T1 NO-GO (2026-08-17) · T2 NO-GO (2026-08-21) · T3
   cerrado con causa tecnica. Se escribe como **curva de capacidad de tres puntos** y
   como hallazgo, no fracaso. T1: rescata `bare_head` del cero (AP50 0,0000 -> 0,0455)
   pero falta 0,0045 al umbral y rompe la retencion de `person` (-11,62 %, tope 10 %).
   T2 (SGD explicito, D-FT-16): la ganancia PASA (`bare_head` -> 0,0909, el doble de T1)
   pero colapsa en entrenamiento (early stop 16/60, mejor epoca = 1) y **fallan las dos
   retenciones** (in-domain: `person` -49,7 %; open-vocabulary: COCO -71,3 %).
   **F-127.1: el fallo es ESTRUCTURAL (2.946 imagenes vs 10,35M parametros), no de
   capacidad.** Margenes y expectativas firmados ANTES de cada evaluacion, sin
   renegociar; ningun checkpoint se adopto; no hay mas brazos contra `bench_v3`.
   **Trampa de cita: T1 gana por recall CR-01, T2 por AP — no hay "mejor tuned" de
   metrica unica.** Va en tabla propia, por estrato, nunca mezclada con el nucleo
   zero-shot.
6. **Plataforma relevada de punta a punta el 2026-08-28** (`operacion/130`, seis repos, solo
   lectura): lo estructural coincide con los docs; las 26 cifras de los cuatro indices verifican
   (EXIT 0); `bench_v3` reproduce byte a byte. Lo que 130 corrigio manda sobre cualquier foto
   anterior (en particular sobre `operacion/97`).
7. **Etapa 1 del informe CERRADA** (2026-08-28): §15 + §16 en su documento v1.0, verificador OK.

**ABIERTO — no se afirma; se marca:**

1. **Procedencia de origen del lote de obra real** (direccion y fecha de acceso por
   clip): pendiente. No bloquea redactar; si bloquea cerrar la version final.
2. **Insercion de las figuras en el `.docx`.** Las seis figuras estan **PRODUCIDAS**
   desde el 2026-08-21 (PNG 300 dpi + SVG en `informe/figuras/`: vista de procesos,
   maquina de estados, calidad frente a densidad, alerta superpuesta, frontera de
   juzgabilidad, mas la FIG-D preexistente), pero **pegarlas en el documento sigue
   pendiente**: en el texto se referencian con `[[FIGURA: cual]]` y no se describe una
   figura como presente mientras la seccion no la tenga insertada.
3. **La integracion al documento maestro.** ✎ 2026-08-28: cada seccion se trabaja **en su
   propio documento** en `entregable/desarrollando/`; lo que queda al final es
   **integrarlas al maestro**, que todavia tiene §17.3/§17.4 en su version previa y §17.5 vacia. Estado:
   **Etapa 1 CERRADA** (`E-OVRT-VDP_Secciones_15_y_16_…_v1.0.docx`, cinco pases aplicados y
   verificados; texto base `90d`; solo D-E1-11 abierta) · **§17.3 v1.4 · §17.4 v1.6 · §17.5 v1.3**
   con sus tres pases APLICADOS Y VERIFICADOS (textos base `90` / `90b` / `90c`) · **§17.1 v1.3
   (Etapa 2) con el pase E2 y el de formato APLICADOS Y VERIFICADOS** el 2026-08-28 (texto base
   `90f`; quedan `90g` —Anexos C y D— y los handoffs hacia 17.3/17.4/17.5) · §17.6, §18 y §19
   sin redactar. El texto base vigente de cada etapa es SIEMPRE su extraccion
   (`90d`/`90f`/`90`/`90b`/`90c`), nunca el placeholder del maestro, los borradores ni las fotos
   `96x` del informe v1.1 (superadas para §15, §16 y §17.1).
4. **D-E1-11 — inscripcion ante la AAIP**: decision del EQUIPO, marcada con `[[PENDIENTE]]`
   en §16.6.2.2 y con marcador espejo en §17.1.11 (D-E2-7); viaja hasta que el equipo la resuelva.

### Convencion de marcadores (obligatoria)

Todo hueco se deja con doble corchete, de modo que sea localizable con una busqueda:

- `[[PENDIENTE: que falta · de que depende]]`
- `[[CIFRA: que cifra hace falta · de que indice saldria]]`
- `[[FIGURA: cual]]`

Reglas: nunca completar un marcador con una estimacion, un valor probable ni una
redaccion evasiva; nunca borrarlo para que el texto "fluya"; el marcador viaja hasta el
entregable y recien lo remueve quien aporta el dato. Un capitulo con marcadores visibles
es honesto; un capitulo que rellena huecos es indefendible.

## Como se trabaja y como se entrega (obligatorio, ✎ 2026-08-27)

**No se trabaja sobre una unidad de Drive conectada, ni editando el documento en su nube.**
Se trabaja **dentro del Project**, con estos archivos de knowledge como unica fuente: el
paquete de la etapa activa **ya contiene el texto vigente completo** de la seccion que se
esta corrigiendo (la extraccion `90`/`90b`/`90c`/`90d`/`90f` segun la etapa). No hace falta ir a
buscar el documento a ningun lado, y hacerlo empeora el resultado.

*Por que la regla existe.* En la entrega del 2026-08-27 el contenido salio bien pero
**cinco encabezados numerados contiguos perdieron su estilo de titulo** (`16.5.3`, `16.5.4`,
`16.5.5`, `16.6`, `16.6.1`): se ven como titulos y no lo son, asi que desaparecen del indice
automatico y de la numeracion de campos. El defecto aparecio al editar via Drive y no se ve
leyendo el texto. Ese ida y vuelta tambien pierde los cambios controlados.

**Forma de la entrega**, por seccion y no del documento completo:

1. Un `.docx` armado **sobre una COPIA del DOCX base** de formato, nunca sobrescribiendolo.
2. **Cada titulo con su estilo de encabezado real** (`Heading 2/3/4/5`), jamas texto en
   negrita imitando un titulo. Si se elimina una subseccion, **renumerar sus hermanas**: un
   salto (por ejemplo `16.7.1`, `16.7.2`, `16.7.6`) se ve en el indice.
3. **Con cambios controlados activados**, o en su defecto con el bloque de trazabilidad por
   unidad que piden las instrucciones del Project (diagnostico · texto propuesto ·
   trazabilidad · pendientes).
4. Sin markdown crudo pegado (`###`, `|---|`, cercos de codigo) y sin identificadores
   internos: `AJ-`, `R-`, `PODA-`, `E1-`/`E3-`/`E4-`, lineas `SHA-256`, cabeceras
   `> Seleccion:`. **Excepcion**: los codigos `P-E1-xx` de las preguntas rectoras SI son
   parte del informe.
5. Los marcadores `[[PENDIENTE: …]]` / `[[CIFRA: …]]` / `[[FIGURA: …]]` **viajan**: no se
   completan con estimaciones ni se borran.
6. **Delta de referencias explicito**: altas completas en APA 7 con DOI/URL, y bajas de lo
   que dejo de citarse. Si una obra queda citada solo desde la nota de una tabla, decirlo.

**Verificacion mecanica antes de dar una entrega por buena** (la corre el equipo, es parte
del circuito y no un extra): `python3 herramientas/verificar_entregable.py <entrega.docx>
--seccion <N>` (p. ej. `--seccion 15 --seccion 16`, o `--seccion 17.1`). Falla con titulos sin estilo, huecos de numeracion, fugas de
andamiaje, markdown crudo y citas sin entrada en referencias; e informa las referencias
huerfanas, la misma autoria con años distintos y si faltan los cambios controlados.

## Estado vigente que manda sobre el resto

- Banco temporal: **47 clips = 32 positivos + 15 negativos, con 37 episodios**. Los 34
  clips corresponden solo al Bloque A del rodaje.
- **FAR/hora se mide y se reporta**, pero la exposicion disponible no permite sostener
  una cota operativa; siempre se cita el conteo, la duracion observada y la tasa derivada.
- **G1/identidad de sujeto esta implementada y medida**. Las metricas MOT siguen fuera
  de alcance; no debe confundirse la exclusion de esas metricas con la capacidad.
- La distribucion de alertas esta **funcionalmente implementada**: los seis criterios de
  spec 45 quedaron verificados, incluido reporte y broker MQTT real. La vista de
  webconsole y la orquestacion integral se cerraron el 2026-08-13 y el repo
  `e-ovrt_alert-distribution` ya tiene historia propia. **Si aporta cifra citable**:
  `t_alert-notification` **p95 = 64,534 ms (n = 460)** entregas live, y en regimen
  sostenido **p95 = 102,025 ms (n = 104)**; mide `bus de alertas -> PUBACK MQTT`, nunca
  sensor -> notificacion (`operacion/118`).
- E-04/fine-tuning: **jornada COMPLETA y CERRADA en sus tres tramos** (✎ 2026-08-22) —
  T1 NO-GO (`operacion/123`) · T2 NO-GO (`operacion/127`) · T3 cerrado con causa tecnica
  (`operacion/117` §2, sin baseline MM-GDINO geometricamente sana el delta es
  ininterpretable), **jamas "por falta de tiempo"** (ADR-017). Ningun checkpoint se
  adopto; no hay mas brazos contra `bench_v3` (reabrir exige pre-registracion nueva,
  acta `operacion/128` §5). Reglas de cita que siguen mandando: las cifras de la rama
  van SIEMPRE en tablas propias, por estrato, jamas fundidas con el nucleo zero-shot;
  la secuencia se cuenta completa y en orden (baseline una sola vez -> margenes D-FT-12
  firmados ANTES -> veredicto T1 -> enmienda D-FT-14 DESPUES del veredicto -> margenes
  D-FT-15 pre-firmados con expectativas -> corrida y veredicto T2) porque **la
  transparencia de la secuencia ES el argumento**; T1 gana por recall CR-01 y T2 por AP
  (no hay "mejor tuned" de metrica unica); el gate de latencia de T1 no se midio y se
  dice explicito (F-123.1); F-120.1: las latencias del run de la baseline no se citan.
  Baseline YOLOE-26s (doc 120, una sola corrida sobre `bench_v3`): `bare_head` AP50
  0,000 (6.181 GT / 10 det), recall CR-01 agregado 0,0002, retencion a proteger person
  0,7843 / helmet 0,6286 / vest 0,2642. En §17.4 la fila de la Tabla 68 la fija E4-27
  (pase 3); en §17.5, el bloque ✎ 2026-08-22 de AJ-5.13.
- **Acoples vigentes (ADR-020, 2026-08-18):** los patrones de acople son DOS, no tres.
  **(a) HTTP config-driven en los TRES modulos** de la plataforma: medios `:8080`,
  control `:8081` y **distribucion `:8082`** (`eovrt-distribute serve`), con la
  webconsole y el runner como clientes de los tres — ninguno consume el bus.
  **(b) bus ZeroMQ PUB/SUB + msgpack** para el dato: detecciones `:5557`
  (medios->control), alertas `:5558` (control->distribucion).
  **NO escribir "BFF-subproceso" ni contar un tercer patron.** El subproceso del
  distribuidor sigue en el codigo como **fallback operativo**
  (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`) — implementado y probado, pero
  es un detalle de operacion, no arquitectura, y no va al informe. Tampoco escribir
  "el modulo es una CLI y no un servicio": es servicio, y ademas conserva su CLI
  para el camino offline (igual que el control-plane).
  *(Historia del numero, solo para quien la necesite — ningun documento anterior al
  2026-08-18 describe el estado vigente de arriba: ADR-018 (2026-08-15) declaro que
  "la plataforma tiene TRES patrones de acople, no dos", con el tercero siendo
  **BFF-subproceso** porque el modulo de distribucion, que es CLI y no servicio,
  no tenia otra forma de acoplarse. ADR-019 (2026-08-17/18) le dio servicio HTTP
  propio al distribuidor sin cambiar el conteo — seguian siendo tres. **ADR-020**,
  el mismo dia, derogo a ADR-018 e invirtio el default: HTTP paso a ser el acople
  normal, el subproceso bajo a fallback, y volvieron a ser DOS.)*
- **Orden de arranque de una corrida live CON distribucion (✎ 2026-08-28, `operacion/130`
  R-01 — corrige a FIG-A, al CLAUDE.md raiz y a la nota de 128 §4, que decian lo contrario):**
  el runner lanza **control → distribucion → medios**: primero `POST :8081/api/runs`
  (`mode: live`, con `alert_bus.enabled` y `wait_for_subscriber_ms ≥ 10 s`), despues
  `POST :8082/api/runs` (necesita el `control_run_id`) y por ultimo `POST :8080/api/runs`. La
  no-perdida en el bus de alertas la garantiza el **handshake XPUB del publicador** (el control
  espera la suscripcion del distribuidor hasta 10 s), no el orden literal. **NO escribir
  "distribucion primero" ni "orden inverso al flujo de datos".** §17.4 v1.6 todavia lo dice
  (pendiente de la etapa 4).
- **Campeon y sus umbrales (✎ 2026-08-28, `operacion/130` R-04/R-11):** citar siempre el par
  completo `gdino-tiny-560` = 560 px · `box_threshold` **0,30** · `text_threshold` 0,25 · NMS
  IoU 0,50 · fp16. **`gdino-tiny` (800 px) corrio a 0,35**: la comparacion "560 no degrada mAP
  respecto de 800" esta confundida con el umbral en el par tiny (el par base si esta a 0,30 en
  ambos: 0,453 vs 0,401); el −24 % de latencia no depende del umbral. El **n=5.313** del recall
  CR-01 (S1/S2) es el del GT del 2026-07-23; con el GT vigente (29-jul) el denominador es 5.308
  y la medicion no se repitio: citarlo fechado. `effective_config.yaml` imprime tambien los
  campos inertes de la otra familia (`confidence_threshold 0,25` en GDINO; `box_threshold 0,35`
  en YOLOE): **GDINO usa `box`+`text`+`iou`; YOLOE usa `confidence`+`iou`**. El campo
  `run.scenario` **no clasifica** DBE/EBE (siempre dice `DBE`): se distingue por `source_type` +
  `bus.enabled`.
- **Motor de patrones (✎ 2026-08-28, `operacion/130` R-07):** **cinco** estados
  `inactive → candidate → confirmed → sustained → resolved`, alerta solo al entrar a
  `confirmed`, reapertura `resolved → candidate`; `cr01_cr02_v2` = CR-01 `high` 4.000/2.000 ms,
  CR-02 `medium` 7.000/3.000 ms, **sin cooldown** (la capacidad existe en el codigo, desactivada);
  la persistencia se implementa como **duracion desde la primera evidencia con tolerancia a
  huecos**, no como proporcion de frames positivos. Hitos persistidos 4 de 5 (la notificacion es
  del distribuidor). Causa two-node = `clock_skew` (no `cross_node_monotonic_clock`).
- **Fine-tuning y datos (✎ 2026-08-28, `operacion/130` R-02/R-03):** el entrenamiento efectivo
  (`finetuning_v1`, T1/T2) uso `construction_site_safety` 2.203 + `ppe_siabar` 743 = **2.946
  train / 483 val** y **EXCLUYO `chv`** por anti-leakage (el 100 % de `chv` es estrato del banco);
  "css + chv + ppe_siabar" es el rol TRAIN **historico** (`train_v2`, archivado 08-15) y NO se
  escribe como lo entrenado. El protocolo (Tabla 28 de §17.1) acotaba el split a 500–2.000
  imagenes: **2.946 es una desviacion que se declara** (100 % de linajes elegibles tras dedup y
  exclusion del banco; F-127.1 muestra que aun asi es insuficiente). Los checkpoints ajustados
  **solo se evaluaron en DBE-imagenes**, nunca en clips ni EBE (ΔSDR/Δt_alert/ΔTTFD no existen).
  De los 9 datasets de la Tabla 26 de §17.1 solo SHEL5K y CHV se usaron (como fuentes del banco);
  css y ppe_siabar, los que se entrenaron, no figuran en esa tabla.
- **G2A y la cadena temporal (✎ 2026-08-28, `operacion/130` R-17):** el G2A medido va del
  **dequeue** (el proceso ya leyo el frame) al **fin de la inferencia**; el tramo sensor→dequeue
  (`capture_to_host`, 202–217 ms) existe **solo para OAK-D** — para RTSP ese tramo **no se midio**
  (no "se suma", falta). NVDEC no se uso (decodificacion por software). El SO real es Linux/WSL2,
  no Windows 11 como decia el protocolo.
- **La containerizacion SI se puede mencionar en el informe** (✎ 2026-08-18, precision del
  usuario). ✎ 2026-08-28 (`operacion/130` R-09): **esta DEFINIDA y validada por configuracion**
  desde el 2026-08-19/20 — Dockerfiles en los tres repos de servicio y `infra/platform/` con el
  compose de 13 servicios y paridad de rutas; lo que sigue **pendiente y diferido a post-entrega
  es el build y el smoke integral** (nunca se corrieron). Su razon de ser es la
  **reproducibilidad** (que un tercero levante la plataforma en otra maquina), y su documentacion
  operativa vive en los repositorios, no en la tesis. **Como escribirla:** "definida y validada
  por configuracion; despliegue no verificado", como trabajo comprometido con su causa, en el
  cierre (§17.6/§18) y en el camino de reproducibilidad (§19). **Como NO escribirla:** ni
  "diferida" (ya esta escrita), ni en presente como capacidad desplegada, ni con instrucciones
  de despliegue — el informe no es un manual. *Describir el compromiso y su fundamento es correcto; describir un despliegue
  que no corrio es falso.*
- **Metricas de `report.json`**: `t_alert-system` es **citable** (esta en el diccionario de
  la spec 40 §5.1 y siempre debio figurar; dejo de estar clavada en `not_applicable`).
  `precision_alertas` / `recall_alertas` / `F1_alertas` **existen pero NO son citables**:
  duplican cifras que ya se reportan via `evaluate-alerts` con denominadores por estrato.
  **La citabilidad esta materializada**: `t_alert-system` ES la columna `t_alert` del
  clip bench (campo `t_alert_system_ms` de cada `metrics.json`) — citable por campana y
  por condicion, nunca promediada entre campanas. ✎ 2026-08-28 (`operacion/130` R-05): esa
  cifra es un **PROMEDIO por campana** — `evaluate-alerts` no produce percentiles ni persiste
  latencias por episodio; los **P50/P95/P99** existen solo para el tramo de plataforma
  (`summary.json` de medios y control: G2A, `processing_ms`, `ttfa_internal`) y para
  `t_alert-notification` (`metrics.json` de la campana 118). Decirlo cuando se cite. Y
  `t_alert-system` cierra en el **reloj de fuente del frame que confirmo** (`alert.timestamp_ms`),
  no en el registro interno monotónico. NO confundir con `t_alert-notification`
  (bus→PUBACK, la campana de distribucion): son tramos con relojes distintos y **los
  percentiles no se suman entre tramos** — la cadena temporal completa se cita POR TRAMOS
  segun la tabla de `results/index.md`.
- Las cifras se toman del índice raíz `results/index.md` (limitaciones L1–L8 y procedencia)
  más los 4 índices canónicos (`bench_imagenes`, `bench_nivel_a`, `clip_bench`,
  `realtime`), incluidos en la sección de resultados operativa. Ante una contradiccion,
  manda este estado, luego el banner mas reciente de la fuente y finalmente su cuerpo
  historico.
""".strip()


def _resolve_source(path: str, repo_root: Path) -> Path:
    source = (repo_root / path).resolve()
    if not source.is_file():
        raise KitError(f"Fuente inexistente: {path} (resuelta como {source})")
    return source


def _find_heading(lines: list[str], heading: str, source: Path, start: int = 0) -> int:
    for index in range(start, len(lines)):
        if lines[index].rstrip("\r\n") == heading:
            return index
    raise KitError(f"Encabezado {heading!r} no encontrado en {source}")


def extract_source(spec: SourceSlice, repo_root: Path) -> tuple[str, Path, str]:
    """Read a complete source or an exact heading-bounded slice."""

    source = _resolve_source(spec.path, repo_root)
    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    start = _find_heading(lines, spec.start_heading, source) if spec.start_heading else 0
    end = (
        _find_heading(lines, spec.end_heading, source, start + 1)
        if spec.end_heading
        else len(lines)
    )
    text = "".join(lines[start:end])
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    return text, source, digest


def _canonical_path(path: Path, workspace_root: Path) -> str:
    try:
        return path.resolve().relative_to(workspace_root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def rewrite_relative_links(text: str, source_path: Path, workspace_root: Path) -> str:
    """Replace local Markdown links with canonical source-path references."""

    def canonical_target(raw_target: str) -> str | None:
        target = raw_target.strip().strip("<>")
        if EXTERNAL_TARGET_RE.match(target):
            return None
        if target.startswith("#"):
            return target

        path_part, separator, fragment = target.partition("#")
        resolved = (source_path.parent / path_part).resolve()
        canonical = _canonical_path(resolved, workspace_root)
        return f"{canonical}#{fragment}" if separator else canonical

    def replace_image(match: re.Match[str]) -> str:
        label, raw_target = match.groups()
        canonical = canonical_target(raw_target)
        if canonical is None:
            return match.group(0)
        description = label or "imagen"
        return f"{description} (recurso fuente: `{canonical}`)"

    def replace_link(match: re.Match[str]) -> str:
        label, raw_target = match.groups()
        canonical = canonical_target(raw_target)
        if canonical is None:
            return match.group(0)
        if canonical.startswith("#"):
            return f"{label} (seccion: `{canonical}`)"
        return f"{label} (fuente: `{canonical}`)"

    without_local_images = MARKDOWN_IMAGE_RE.sub(replace_image, text)
    return MARKDOWN_LINK_RE.sub(replace_link, without_local_images)


def render_document(
    title: str,
    purpose: str,
    specs: tuple[SourceSlice, ...],
    repo_root: Path,
    *,
    preamble: str = "",
    generated_on: str | None = None,
) -> str:
    """Render source slices into one provenance-preserving Markdown document."""

    workspace_root = repo_root.parent
    generated_on = generated_on or date.today().isoformat()
    chunks = [
        f"# {title}\n\n",
        f"> Generado el {generated_on}. {purpose}\n\n",
    ]
    if preamble:
        chunks.extend([preamble.rstrip(), "\n\n"])
    for spec in specs:
        text, source, digest = extract_source(spec, repo_root)
        canonical = _canonical_path(source, workspace_root)
        selection = spec.note or (
            f"desde {spec.start_heading!r} hasta antes de {spec.end_heading!r}"
            if spec.start_heading or spec.end_heading
            else "documento completo"
        )
        chunks.extend(
            [
                "---\n\n",
                f"## Fuente: `{canonical}`\n\n",
                f"> SHA-256 del bloque: `{digest}`  \n",
                f"> Seleccion: {selection}.\n\n",
                rewrite_relative_links(text, source, workspace_root).rstrip(),
                "\n\n",
            ]
        )
    return "".join(chunks)


def build_outputs(
    repo_root: Path,
    stage: int,
    *,
    generated_on: str | None = None,
) -> dict[Path, str]:
    """Build the two and only two files uploaded to ChatGPT knowledge."""

    if stage not in STAGE_SOURCES:
        raise KitError(f"Etapa invalida: {stage}; opciones: 0, 1, 2, 3, 4, 5, 6")

    kit_dir = repo_root / "informe/project-kit"
    base = render_document(
        "E-OVRT-VDP - contexto base para redaccion",
        "Archivo estable del knowledge; se usa junto al paquete de la etapa activa.",
        BASE_SOURCES,
        repo_root,
        preamble=BASE_PREAMBLE,
        generated_on=generated_on,
    )
    stage_preamble = BASE_PREAMBLE + "\n\n" + "\n".join(
        [
            "## Contrato de uso",
            "",
            f"- **Etapa activa:** {stage} - {STAGE_DESCRIPTIONS[stage]}.",
            "- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.",
            "- No se trasladan resultados propios hacia secciones cronologicamente anteriores.",
            f"- Nombre propio de esta etapa ({stage_filename(stage)}): regenerarla no pisa"
            " el paquete de ninguna otra etapa.",
            *(f"- {bullet}" for bullet in STAGE_CONTRACTS.get(stage, ())),
        ]
    )
    active_stage = render_document(
        f"E-OVRT-VDP - paquete de etapa {stage}",
        STAGE_DESCRIPTIONS[stage] + ".",
        STAGE_SOURCES[stage],
        repo_root,
        preamble=stage_preamble,
        generated_on=generated_on,
    )
    return {
        kit_dir / "00-contexto-base.md": base,
        kit_dir / stage_filename(stage): active_stage,
    }


def _relative_markdown_targets(text: str) -> list[str]:
    targets: list[str] = []
    for regex in (MARKDOWN_IMAGE_RE, MARKDOWN_LINK_RE):
        for match in regex.finditer(text):
            target = match.group(2).strip().strip("<>")
            if not EXTERNAL_TARGET_RE.match(target):
                targets.append(target)
    return targets


def check_outputs(outputs: dict[Path, str]) -> list[str]:
    """Return all integrity errors without modifying the generated files."""

    errors: list[str] = []
    names = {path.name for path in outputs}
    if "00-contexto-base.md" not in names:
        errors.append("falta 00-contexto-base.md en el knowledge generado")
    stage_names = names - {"00-contexto-base.md"}
    if not stage_names:
        errors.append("no se genero ningun archivo de etapa")
    for name in sorted(stage_names):
        if not STAGE_FILENAME_RE.match(name):
            errors.append(f"nombre de archivo de etapa invalido: {name}")

    for path, expected in outputs.items():
        if not path.is_file():
            errors.append(f"falta el archivo generado: {path}")
        elif path.read_text(encoding="utf-8") != expected:
            errors.append(f"archivo desactualizado: {path}")

        size = len(expected.encode("utf-8"))
        limit = BASE_MAX_BYTES if path.name == "00-contexto-base.md" else STAGE_MAX_BYTES
        if size > limit:
            errors.append(f"{path.name} pesa {size} bytes y supera el limite de {limit}")
        if "SHA-256 del bloque:" not in expected:
            errors.append(f"{path.name} no contiene cabeceras de procedencia")
        relative_targets = _relative_markdown_targets(expected)
        if relative_targets:
            errors.append(
                f"{path.name} conserva enlaces Markdown relativos: "
                + ", ".join(relative_targets[:5])
            )
    return errors


def _existing_generation_date(repo_root: Path) -> str | None:
    base_path = repo_root / "informe/project-kit/00-contexto-base.md"
    if not base_path.is_file():
        return None
    match = GENERATED_DATE_RE.search(base_path.read_text(encoding="utf-8"))
    return match.group(1) if match else None


def write_outputs(outputs: dict[Path, str]) -> None:
    for path, content in outputs.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(path)


def _etapa_value(raw: str) -> int | str:
    if raw.strip().lower() in {"all", "todas"}:
        return "all"
    try:
        value = int(raw)
    except ValueError as error:
        raise argparse.ArgumentTypeError(f"etapa invalida: {raw!r}") from error
    if value not in range(7):
        raise argparse.ArgumentTypeError(f"etapa invalida: {raw!r}; opciones: 0-6, all")
    return value


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--etapa",
        type=_etapa_value,
        default=1,
        help="0-6 para una sola etapa, o 'all' para regenerar las siete a la vez",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="verifica frescura e integridad sin escribir archivos",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parents[1]
    generated_on = _existing_generation_date(repo_root) if args.check else date.today().isoformat()
    stages = list(range(7)) if args.etapa == "all" else [args.etapa]
    try:
        outputs: dict[Path, str] = {}
        for stage in stages:
            outputs.update(build_outputs(repo_root, stage, generated_on=generated_on))
    except KitError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if args.check:
        errors = check_outputs(outputs)
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        print(f"OK: kit vigente para etapa(s) {args.etapa}; {len(outputs)} archivos de knowledge")
        return 0

    write_outputs(outputs)
    for path, content in outputs.items():
        print(f"GENERADO: {path.relative_to(repo_root)} ({len(content.encode('utf-8'))} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
