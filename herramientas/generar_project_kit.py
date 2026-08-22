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
        SourceSlice("informe/entregable/96c-informe-v11-estado-del-arte.md"),
        SourceSlice("informe/entregable/96d-informe-v11-marco-teorico.md"),
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario",
            end_heading="### 19.2. Anexo B - Infraestructura, nodos y parámetros experimentales",
            note="Anexo A vigente",
        ),
        SourceSlice("informe/ajustes/01-etapa-1-fundamentacion-teorica.md"),
        SourceSlice(
            "informe/entregable/borradores/vara-15.md",
            note="borrador listo para integrar: la vara del 15 (AJ-1.01/1.02/1.13)",
        ),
        SourceSlice(
            "informe/ajustes/07-critica-extension-y-poda.md",
            start_heading="## 3. §15 Estado del Arte (21.575 palabras)",
            end_heading="## 5. §17.1 Consolidación Metodológica (32.222 palabras)",
            note="podas 01 a 11 aplicables a las secciones 15 y 16",
        ),
        SourceSlice("sintesis/fundamentos-teoricos.md"),
    ),
    2: (
        SourceSlice("informe/entregable/96b-informe-v11-17-1-consolidacion-metodologica.md"),
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística",
            end_heading="## Referencias",
            note="Anexos C y D vigentes",
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
            note="pase de cierre 1 (2026-08-19): sus decisiones D1-D4 y la regla de autocontención SIGUEN RIGIENDO",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/correcciones-etapa-3-4-pase-2.md",
            note="pase de cierre 2 (2026-08-20): continua la numeracion del pase 1 y manda sobre el resto del material de esta etapa",
        ),
        SourceSlice("informe/entregable/90-etapa3-texto-extraido.md"),
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
            note="pase de cierre 1 (2026-08-19): sus decisiones D1-D4 y la regla de autocontención SIGUEN RIGIENDO",
        ),
        SourceSlice(
            "informe/entregable/desarrollando/correcciones-etapa-3-4-pase-2.md",
            note="pase de cierre 2 (2026-08-20): continua la numeracion del pase 1 y manda sobre el resto del material de esta etapa",
        ),
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 17.4. Implementación del prototipo experimental",
            end_heading="### 17.5. Evaluación y validación del prototipo",
            note="placeholder vigente de la seccion 17.4",
        ),
        SourceSlice("informe/ajustes/04-etapa-4-implementacion.md"),
        SourceSlice(
            "informe/entregable/borradores/17-4.md",
            note="borrador completo de la seccion 17.4, listo para revision",
        ),
        SourceSlice("informe/ajustes/material-etapa-3/92-anexo-concrecion-tecnica.md"),
        SourceSlice("informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md"),
        SourceSlice("operacion/97-relevamiento-plataforma-2026-08-05.md"),
        SourceSlice("nucleo/14-mapa-de-la-cadena.md"),
        SourceSlice("nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md"),
    ),
    5: (
        SourceSlice(
            "informe/entregable/96e-informe-v11-cierre-anexos-referencias.md",
            start_heading="### 17.5. Evaluación y validación del prototipo",
            end_heading="### 17.6. Documentación técnica, repositorio y evidencias de cierre",
            note="placeholder vigente de la seccion 17.5",
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

STAGE_DESCRIPTIONS = {
    0: "Etapa 0: secciones 11 a 14 y ajustes transversales",
    1: "Etapa 1: secciones 15 y 16, y Anexo A",
    2: "Etapa 2: seccion 17.1 y Anexos C y D",
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
5. Rama de ajuste fino, **brazo T1: CERRADO con veredicto NO-GO** (2026-08-17). Los
   margenes se firmaron **antes** de la linea base, la corrida se ejecuto una vez y se
   evaluo una vez, y **el checkpoint ajustado no se adopta como modelo de servicio**.
   Tiene cifra medida y se escribe como **hallazgo, no como fracaso**: el ajuste rescata
   `bare_head` del cero absoluto (AP50 0,0000 -> 0,0455) pero **no alcanza el umbral**
   (faltaron 0,0045) y **rompe la retencion de `person`** (-11,62 %, tope 10 %). Va en
   tabla propia, por estrato, nunca mezclada con el nucleo zero-shot.

**ABIERTO — no se afirma; se marca:**

1. **Resultado del brazo T2**: no existe. T2 se reabrio como tier **exploratorio** por
   enmienda posterior al NO-GO (D-FT-14) y esta **enviado y en cola, sin empezar**; sus
   margenes ya estan firmados por adelantado (D-FT-15). No hay ninguna cifra de ese
   checkpoint y no la habra hasta que corra y se evalue: esa subseccion queda reservada
   con marcador. **T1 ya no es un hueco**: tiene resultado y se afirma (ver CERRADO 5).
2. **Cinco figuras sin producir** (vista de procesos, maquina de estados del motor,
   calidad frente a densidad, cuadro con alerta superpuesta y frontera de juzgabilidad).
   Se mencionan en el texto con marcador; no se describen como si existieran.
3. **Procedencia de origen del lote de obra real** (direccion y fecha de acceso por
   clip): pendiente. No bloquea redactar; si bloquea cerrar la version final.

### Convencion de marcadores (obligatoria)

Todo hueco se deja con doble corchete, de modo que sea localizable con una busqueda:

- `[[PENDIENTE: que falta · de que depende]]`
- `[[CIFRA: que cifra hace falta · de que indice saldria]]`
- `[[FIGURA: cual]]`

Reglas: nunca completar un marcador con una estimacion, un valor probable ni una
redaccion evasiva; nunca borrarlo para que el texto "fluya"; el marcador viaja hasta el
entregable y recien lo remueve quien aporta el dato. Un capitulo con marcadores visibles
es honesto; un capitulo que rellena huecos es indefendible.

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
- E-04/fine-tuning es una **rama comparativa separada y en curso**. F-100.1 esta
  resuelta. `1166583` cerro freeze/smoke tecnico con 12 tensores/3.096 parametros y
  optimizer 12/12; dual gate, serving real y **procedencia T-FT-023 (cerrada el
  2026-08-13, snapshot tar `639e60df...`)** estan verdes. **El 2026-08-15 el usuario firmo
  D-FT-08 (contrato de serving), D-FT-12 (objetivo y margenes go/no-go, firmada ANTES de
  la baseline) y D-FT-13 (derogacion de la sonda `machinery` solo para T1)**, T-FT-005
  quedo `done` y **no queda ninguna decision humana pendiente**. La misma jornada se
  cerraron **T-FT-031** (comando de evaluacion congelado + enforcement canonico v2 en
  config + catalogo finetuned) y **T-FT-032**: la **baseline YOLOE-26s corrio UNA vez
  sobre las 6.477 imagenes de `bench_v3`** (doc 120) — `bare_head` AP50 **0,000**
  (6.181 GT / 10 detecciones), recall CR-01 0,0167/0,0000 por fuente y **0,0002
  agregado**; retencion a proteger person 0,7843 / helmet 0,6286 / vest 0,2642. Estas
  cifras son **de la rama comparativa**: van SIEMPRE en tablas propias, por estrato, y
  NO se promueven a `results/` hasta cerrar la jornada; **no hay cifra del checkpoint
  ajustado** (no existe todavia) ✎ *superado el 2026-08-17: el checkpoint T1 SI tiene
  cifra — ver la enmienda al pie de esta vineta; el que sigue sin cifra es T2*.
  F-120.1: las latencias de ese run NO se citan (cambio
  de energia en curso); el gate de latencia se mide pareado aparte.
  **✎ 2026-08-15 (noche) — T1 full ENVIADO: T-FT-043 esta CERRADA.** La autorizacion se
  emitio y verifico en el cluster con sus 7 gates, el ensayo `--test-only` paso, y el
  `RUN` quedo **encolado como job `1167640`** (1 GPU / 10 CPU / 60 GB / 2 h). Al encolar
  figuraba en espera, con inicio estimado por el planificador el 2026-08-17; una
  estimacion del planificador **no es reserva ni promesa**, y el envio **no es un
  resultado**. Lo que sigue abierto es la corrida en si y, despues, la promocion del
  checkpoint por hash, su evaluacion unica y el veredicto go/no-go contra los margenes ya
  firmados. **Hasta que eso ocurra no existe ninguna cifra del modelo ajustado**: la
  subseccion correspondiente se deja con `[[PENDIENTE: ...]]`, jamas con un valor
  estimado ni con una redaccion que sugiera que la comparacion ya se hizo.
  La sonda de clase nueva (`machinery`) quedo **derogada para T1 y reasignada a T2/T3**
  por D-FT-13; en T2/T3, de vocabulario abierto, sigue siendo exigible.
  **✎ 2026-08-17 — la jornada T1 CERRO: veredicto NO-GO.** El job `1167640` corrio el
  16/08, el checkpoint se promovio por hash y se evaluo **una sola vez** contra
  `bench_v3`: `bare_head` AP50 **0,0000 -> 0,0455** (gate A pedia >= 0,05: **faltaron
  0,0045**) y la retencion de `person` cayo **0,7843 -> 0,6932 (-11,62 %, tope 10 %)**.
  **El checkpoint no se adopta.** Los margenes (D-FT-12) estaban firmados desde el 15/08,
  antes de la baseline, y **no se renegociaron**: eso es lo que hace al resultado
  defendible. La cifra **existe y es citable**, en tabla propia por estrato; el gate de
  latencia **no se midio** y se dice explicito (F-123.1), no se omite.
  **La misma jornada, DESPUES del veredicto, el usuario firmo la enmienda D-FT-14**: T2
  se reabre como tier **exploratorio** —para separar si el fallo fue de capacidad o
  estructural—, no como reintento de T1, y **T3 queda cerrado como trabajo futuro con
  causa tecnica** (sin baseline MM-GDINO geometricamente sana el delta es
  ininterpretable), **jamas por "falta de tiempo"**. **D-FT-15** fijo los margenes de T2
  **antes de todo resultado T2**, con la retencion de vocabulario abierto sobre COCO
  val2017 congelada en mAP50 **0,434676 => umbral NO-GO 0,391208**, y con la expectativa
  **pre-registrada** de que T2 tambien de NO-GO. **T2 esta enviado y en cola, sin
  empezar**: no tiene ni una cifra. Al redactar, la secuencia se cuenta completa y en ese
  orden —veredicto, enmienda posterior, margenes firmados por adelantado—: **la
  transparencia de la secuencia ES el argumento**, y suavizarla la destruye.
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
- **La containerizacion SI se puede mencionar en el informe** (✎ 2026-08-18, precision del
  usuario — antes esto se leia como "no mencionarla"). Esta **diferida con causa**
  (ADR-019 §4): se va a hacer **despues** de cerrar la redaccion, su razon de ser es la
  **reproducibilidad** de la plataforma —que un tercero pueda levantarla en otra maquina—
  y **no** cerrar el informe, y su **documentacion operativa vive en los repositorios**
  (`infra/`, READMEs), no en la tesis. **Como escribirla:** como **trabajo comprometido
  con su causa**, en el cierre (§17.6/§18) y en el camino de reproducibilidad (§19).
  **Como NO escribirla:** en presente, como capacidad existente, o con instrucciones de
  despliegue — el informe no es un manual. La frase que gobierna: *describir el compromiso
  y su fundamento es correcto; describir un despliegue que no corrio es falso.*
- **Metricas de `report.json`**: `t_alert-system` es **citable** (esta en el diccionario de
  la spec 40 §5.1 y siempre debio figurar; dejo de estar clavada en `not_applicable`).
  `precision_alertas` / `recall_alertas` / `F1_alertas` **existen pero NO son citables**:
  duplican cifras que ya se reportan via `evaluate-alerts` con denominadores por estrato.
  **La citabilidad esta materializada**: `t_alert-system` ES la columna `t_alert` del
  clip bench (campo `t_alert_system_ms` de cada `metrics.json`) — citable por campana y
  por condicion, nunca promediada entre campanas. NO confundir con `t_alert-notification`
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
