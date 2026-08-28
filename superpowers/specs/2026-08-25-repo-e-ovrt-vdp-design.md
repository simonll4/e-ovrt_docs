# Diseño — repositorio público `e-ovrt-vdp` (vitrina del proyecto de tesis)

- **Fecha:** 2026-08-25
- **Estado:** diseño aprobado por secciones en conversación; pendiente de revisión de la
  spec escrita antes de pasar al plan de implementación.
- **Decisor:** el usuario (Simon Llamosas). Autores del trabajo: Carrizo, Matías Lautaro ·
  Guillaumet, Gabriel Agustín · Llamosas, Simon. Tutor: García Mattio, Mariano. IUA
  Córdoba, Facultad de Ingeniería, Ingeniería en Informática, Proyecto Integrador.

## 0. Idea en una línea

Un **repositorio público de documentación**, `e-ovrt-vdp`, que reúne el proyecto entero para
un lector externo: la idea general de la plataforma, su arquitectura con figuras, la
evidencia de lo hecho, el informe final, y el mapa a los cinco repositorios de código. Es
**la única referencia externa que el informe cita**, y sirve para compartir la tesis con
otras personas y mostrar lo que se hizo. `docs/` (este repo) queda **interno** y no se
publica ni se referencia.

## 1. Decisiones que fijan el diseño

| # | Decisión | Elegida | Alternativas descartadas |
|---|---|---|---|
| D1 | Lector primario | **Jurado / lector del informe**, lee en GitHub sin clonar | reproductor de la plataforma; ambos |
| D2 | Qué se lleva de `docs/` | **Nada del andamiaje interno** (bitácora `operacion/`, ADRs, síntesis, kit). Sí el **entregable**: el informe y, por ser parte de él, sus figuras | publicar síntesis reescrita; ADRs curados |
| D3 | Visibilidad | **Todo público**: el paraguas y los 5 repos de código | paraguas público + código privado; todo privado |
| D4 | Forma | **A — repo-vitrina en Markdown puro**, renderizado por GitHub, sin tooling | B — MkDocs + Pages; C — meta-repo con submódulos |
| D5 | Videos | **No se sube ningún video**: ni rodaje, ni derivados del rodaje (V1/V3/VG1/VG1e/lado-a-lado), ni los de internet. Los de internet se **referencian por su URL de origen** | assets de Release; YouTube no listado |
| D6 | Cifras | El paraguas **muestra** cifras, no las produce: cada número enlaza al índice de `e-ovrt_experimental-setup/results/` del que sale | copiar tablas |
| D7 | Git | **Todo el git lo hace el usuario** (remote, push, tags, release). Claude deja el repo local listo y los comandos exactos | — |

De C se rescata una sola cosa: la **tabla de versiones citadas** (repo → tag → commit →
fecha), que da trazabilidad sin submódulos. La estructura de A es compatible con migrar a
B después de la defensa sin reescribir nada.

## 2. Identidad del repositorio

- **Nombre:** `e-ovrt-vdp` (guion medio = nombre de proyecto; los módulos usan
  `e-ovrt_<módulo>`, así el paraguas se distingue a la vista).
- **Cuenta:** `simonll4` (ya aloja 3 de los 5 repos de código y `docs`).
- **Ubicación en disco:** `/home/simonll4/projects/e-ovrt-vdp/`, hermano de los demás.
- **Descripción GitHub:** *Plataforma experimental de detección open-vocabulary en video en
  tiempo real para monitoreo asistivo de riesgos en construcción — Proyecto Integrador,
  Ingeniería en Informática, IUA Córdoba (2026).*
- **Topics:** `open-vocabulary-detection`, `construction-safety`, `grounding-dino`,
  `computer-vision`, `thesis`, `zeromq`, `mqtt`.
- **Idioma:** castellano (el del informe y del jurado). Un párrafo de **abstract en inglés**
  al inicio del README.
- **Licencia (propuesta, decisión de los tres autores):** paraguas **CC BY 4.0** (texto,
  figuras, informe); los 5 repos de código **MIT**, agregada en el mismo pase de
  publicación. Hoy **ningún** repo tiene `LICENSE`.
- **Citación:** `CITATION.cff` con los tres autores, tutor como contribuidor, título del
  informe, institución, año y URL → GitHub muestra "Cite this repository".

## 3. Las cuatro reglas de contenido (`CONTRIBUTING.md`)

1. **Autocontenido hacia afuera.** Ninguna referencia a `docs/` interno, `operacion/NN`,
   `nucleo/`, ADRs (de ninguna serie), IDs `F-xx.x` / `D-xx.x` / `AJ-` / `R-` / `PODA-` /
   `T-FT-`, ni rutas absolutas de la máquina. Sólo se cita: el propio repo, los 5 repos
   públicos, el informe, la bibliografía. Es la misma regla de autocontención que rige el
   informe: para un lector externo, todo eso serían enlaces muertos.
2. **Ninguna cifra sin enlace a `results/`.** Cada número de resultado enlaza al índice de
   `e-ovrt_experimental-setup/results/` del que sale, con `n` y material. El paraguas no es
   fuente de cifras.
3. **Sin binarios pesados en git.** Sí: figuras PNG/SVG (~3,5 MB en total), capturas de
   consola (~200 KB c/u), el PDF del informe (una versión, la entregada). No: videos,
   `.docx` de trabajo, datasets, pesos, `runs/`.
4. **Vocabulario del informe.** CR-01 / CR-02, DBE / EBE, `media.detection.v1`,
   `bus.envelope.v1`, `bench_v3`, limitaciones L1–L8, E-DIR / E-IND / E-HYB, `gdino-tiny-560`
   — los mismos nombres que el informe define para sí, sin sinónimos internos.

Marco de lectura para todo lo que muestre resultados: **los números son EL DATO de una
combinación bajo un protocolo, no un aprobado/fallado**. Un NO-GO pre-registrado (el
fine-tuning) se muestra como resultado, no se esconde. Y **nunca** se argumenta que "OVD
detecta mejor": la tesis es la plataforma y la medición sin entrenar.

## 4. Estructura

```
e-ovrt-vdp/
├── README.md                     ← PORTADA
├── LICENSE                       ← CC BY 4.0
├── CONTRIBUTING.md               ← las 4 reglas (§3)
├── CITATION.cff
├── .gitignore
├── PUBLICAR.md                   ← checklist de publicación PARA EL USUARIO; se borra al publicar
│
├── informe/
│   ├── README.md                 ← qué versión es, fecha, tabla de contenidos del informe
│   └── E-OVRT-VDP-informe.pdf    ← el entregable (entra cuando el maestro cierre)
│
├── plataforma/                   ← "la idea general", 5 documentos de ~1 página
│   ├── 01-problema-y-enfoque.md
│   ├── 02-arquitectura.md
│   ├── 03-flujo-de-una-alerta.md
│   ├── 04-escenarios-dbe-ebe.md
│   └── 05-metodo-experimental.md
│
├── resultados/
│   └── README.md                 ← la respuesta, 8–10 cifras enlazadas, limitaciones L1–L8
│
├── repositorios/
│   └── README.md                 ← ficha por repo + tabla de versiones citadas
│
├── evidencia/
│   ├── figuras/                  ← fig-a…fig-f (PNG 300 dpi + SVG) + scripts/ + README.md
│   ├── consola/                  ← 6–8 capturas PNG de la webconsole + README.md
│   ├── material-de-video.md      ← procedencia del banco de clips (URLs de internet; rodaje no publicado)
│   └── verificacion.md           ← suites verdes por repo, comando + conteo, fecha
│
└── herramientas/
    ├── verificar.py              ← guardián de las 4 reglas (§7)
    └── tests/test_verificar.py
```

Lógica: el lector entra por `README.md` y en un scroll tiene el qué, el resultado en una
línea, la figura de arquitectura y a dónde ir. `plataforma/` es la idea general en cinco
piezas cortas (no un tratado: eso es el informe). `resultados/` es la vitrina de cifras,
nunca fuente. `repositorios/` es el mapa. `evidencia/` es lo que se ve.

Fuera, a propósito: bitácora, ADRs, kit de redacción, versiones intermedias del informe,
datasets, pesos, `runs/`, videos.

## 5. Contenido de cada pieza

La columna "respaldo interno" guía la **redacción** y no aparece en el repo. Todo se
reescribe para un lector externo; nada se copia.

| Pieza | Qué cuenta | Respaldo interno |
|---|---|---|
| `README.md` | Título; abstract EN; la pregunta del trabajo y la **respuesta en una línea** (la detección zero-shot alcanza para sostener CR-01 y no para CR-02; la plataforma alrededor del modelo cambia el resultado más que cualquier elección de modelo o prompt, y esa ganancia sobrevive al tiempo real); figura A; tabla de los 5 repos; "cómo leer este repo"; autores, tutor, institución, año | `sintesis/resultados-y-conclusiones.md` §1; portada del informe (96a) |
| `plataforma/01-problema-y-enfoque.md` | Riesgos en obra y EPP; por qué detección open-vocabulary sin entrenar; las dos condiciones CR-01 (sin casco) / CR-02 (sin chaleco); la hipótesis de plataforma | informe §intro/objetivos; `nucleo/09` |
| `plataforma/02-arquitectura.md` | Tres servicios HTTP config-driven (media `:8080`, control `:8081`, distribución `:8082`), la consola (React + BFF) como cliente de los tres, el bus ZeroMQ PUB/SUB + msgpack, los contratos versionados, el compose integral de 13 servicios con paridad de rutas; **figura A** | `nucleo/14`, `specs/40–45`, §17.3 v1.4 / §17.4 v1.5 |
| `plataforma/03-flujo-de-una-alerta.md` | Detección → evidencia por sujeto (`track_id`) → patrón con persistencia (`confirm_after_ms` 4.000 / 7.000) → confirmación → bus de alertas `:5558` → MQTT QoS 1 con idempotencia; máquina de **5 estados con reapertura a `candidate`**; **figuras E y C** | `nucleo/19`; ADR-011/016/019; README de figuras |
| `plataforma/04-escenarios-dbe-ebe.md` | DBE (offline, acople por archivo JSONL) vs EBE (vivo, acople por bus); **orden de arranque inverso al flujo de datos** (distribución → control → media); hardware real (OAK-D Pro PoE, RTSP); los tramos temporales se citan **por separado, sin sumar percentiles** (`capture_to_host`, G2A, `t_alert-system`, `t_alert-notification`) | docs 37/38/101; `results/realtime/`; `infra/platform/README` |
| `plataforma/05-metodo-experimental.md` | `bench_v3` (6.477 imgs, 3 estratos, reporte por estrato y agregado); banco de clips **47** con GT temporal humano (32 pos / 15 neg, 37 episodios); campañas por pregunta de medición; densidades; fine-tuning como jornada con protocolo pre-registrado | doc 62; `registry/bench_v3.md`; docs 80/113; ADR-017; docs 123/127 |
| `resultados/README.md` | **Por pregunta de medición, nunca por cronología**: (1) selección de modelo — campeón `gdino-tiny-560`, especialista `gdino-base-560`; (2) E-DIR vs E-IND; (3) escena vs sujeto — **G1 0,930**, la mejor del banco, con las mismas detecciones bit a bit; (4) costo del tiempo real — la ganancia de identidad excluye el cero en las 4 densidades; (5) distribución — p95 64,534 ms (n=460); (6) fine-tuning — curva de 3 puntos, NO-GO pre-registrado, causa estructural. Cada cifra con `n`, material y **enlace al índice**. Limitaciones L1–L8. **Figuras B y F** | los 4 índices de `results/`; `operacion/98` para la fuerza de cada afirmación |
| `repositorios/README.md` | Ficha por repo: rol en la cadena, entrada, cómo se corre en 3 líneas, suite de tests, **tag/commit citado**. Nota: son hermanos en disco porque hay rutas relativas cross-repo | READMEs + `CLAUDE.md` de cada repo |
| `evidencia/figuras/README.md` | Qué muestra cada figura, de qué dato sale, cómo se regenera, y las **3 advertencias de lectura**: la distribución es una línea continua · el orden de arranque es inverso al flujo · la máquina tiene 5 estados con reapertura | `informe/figuras/README.md` |
| `evidencia/consola/README.md` | Una línea por captura: qué pantalla es y qué muestra | producción propia |
| `evidencia/material-de-video.md` | Tabla de los 13 clips de internet (id · fuente · **URL**, columna a completar por el usuario = C1); el rodaje descripto (cuántos clips, obra real, GT humano) y declarado **no publicado** | `results/clip_bench/`; doc 113 |
| `evidencia/verificacion.md` | Suites de los 5 repos **corridas el día de la publicación**: comando, conteo, fecha. No se copia ninguna foto vieja (referencia histórica: 2.203 tests al 2026-08-15) | se ejecutan |
| `informe/README.md` | Versión y fecha del PDF; tabla de contenidos del informe; nota de que es el objeto citado | `entregable/00-el-informe-hoy.md` |

## 6. Evidencia: tipo → dónde vive

| Tipo | Dónde | Cómo se produce |
|---|---|---|
| Figuras A–F | `evidencia/figuras/` en git | Copia de `docs/informe/figuras/` (PNG + SVG + 4 generadores + `estilo.py`); README reescrito sin referencias internas. Fig C es PNG solo (no tiene SVG ni generador) |
| Capturas de consola | `evidencia/consola/` en git | Hoy **no existen**. Se levantan consola + `mp-mock` (`EOVRT_MODEL_REF=mock`, sin GPU) y se capturan con chromium headless desde el scratchpad. Pantallas objetivo: preflight de plataforma · lanzamiento de corrida · monitor live · timeline de alertas · comparador de campañas · grabación/recorte de clips |
| Videos | **ninguno en el repo** (D5) | `material-de-video.md` referencia los de internet por URL y describe el rodaje |
| Informe | `informe/*.pdf` en git y adjunto al Release `v1.0` | Lo aporta el usuario cuando cierre el maestro |
| Cifras | ninguna propia | enlaces a `results/` (D6) |

## 7. `herramientas/verificar.py` — el guardián

Script Python sin dependencias externas, con tests (`pytest`), que corre en segundos y sin
red. Se escribe **primero** (TDD) y todo texto pasa por él antes de darse por escrito.

Chequeos:

- **(a) Patrones prohibidos** en todo `.md` del repo (excepto `PUBLICAR.md`):
  `../docs/`, `docs/operacion`, `docs/nucleo`, `docs/decisiones`, `docs/informe`,
  `docs/sintesis`, `docs/specs`, `operacion/\d`, `nucleo/\d`, `ADR-\d`, `\bF-\d`, `\bD-\d`,
  `AJ-\d`, `\bR-\d\d`, `PODA-`, `T-FT-`, `[[PENDIENTE`, `[[FIGURA`, `[[CIFRA`, `/home/`.
  (No se prohíbe `docs/` a secas: `e-ovrt_experimental-setup` tiene una carpeta `docs/`
  pública y legítima de enlazar.)
  Excepción explícita por línea con el marcador `<!-- verificar:permitir -->` (para la
  fila de URLs de C1 mientras esté pendiente).
- **(b) Enlaces relativos** resuelven a un archivo o carpeta existente dentro del repo
  (incluye anclas `#` sólo si el archivo existe; no valida anclas).
- **(c) Filas de cifras enlazadas**: en `resultados/README.md`, toda fila de tabla (no de
  encabezado) que contenga un número decimal con coma, `p95` o `n=` debe contener un
  enlace a `https://github.com/simonll4/e-ovrt_experimental-setup/blob/<ref>/results/…` o
  `…/blob/<ref>/finetuning/…` (las cifras de fine-tuning viven en
  `finetuning/manifests/`, no en `results/`). Los enlaces usan `blob/HEAD/` (rama por
  defecto del repo en GitHub); al congelar, `PUBLICAR.md` los pasa a `blob/informe-2026/`.
- **(d) Figuras referenciadas existen**: toda imagen `![...](ruta)` apunta a un archivo
  existente.

Salida: lista de violaciones `archivo:línea: regla — texto`, exit code 1 si hay alguna.
`--json` para uso en tests. Tests con fixtures sintéticas (repos mínimos en `tmp_path`):
uno por regla en positivo y negativo, más el marcador de excepción.

## 8. Versiones y citación

- **Tags por repo:** el día de la entrega, cada uno de los 5 repos de código recibe el tag
  `informe-2026` sobre el commit que el informe describe. El tag es independiente de la
  rama: **no exige el merge a `main`** (el merge es del usuario y no se ofrece).
- **Release del paraguas:** `v1.0` con el PDF adjunto; la tabla *repo → tag → commit corto →
  fecha* vive en `repositorios/README.md` y se completa en ese momento.
- **Cómo cita el informe al repo:** una sola URL, `https://github.com/simonll4/e-ovrt-vdp`,
  en la sección de entrega/anexos (el informe ya prevé "informe PDF, anexos, repositorio y
  presentación"). Es coherente con la autocontención: referencia externa pública, no
  andamiaje interno. Los repos de código se citan desde el paraguas, no uno a uno.
- **Editar el informe `.docx` queda fuera de alcance**: la nota de dónde va la URL es para
  el usuario.

## 9. Orden de producción

1. **Esqueleto**: carpeta, `git init`, `.gitignore`, `LICENSE` (CC BY 4.0), `CITATION.cff`,
   `CONTRIBUTING.md`, `PUBLICAR.md`.
2. **`herramientas/verificar.py` + tests** (TDD, §7).
3. **Textos**, en este orden: `README.md` → `plataforma/01–05` → `repositorios/README.md` →
   `resultados/README.md` → `evidencia/*.md` → `informe/README.md`. Cada uno pasa
   `verificar.py` antes de darse por escrito. Las cifras de `resultados/` se cotejan contra
   los índices de `results/` (internamente, con `docs/operacion/datos/96-verificar-indices.py`).
4. **Figuras**: copia + README.
5. **Capturas de consola**: consola + mock, chromium headless, 6–8 PNG + README.
6. **`evidencia/verificacion.md`**: correr las suites de los 5 repos y registrar.
7. **`informe/`**: README ahora; el PDF cuando el usuario lo entregue.
8. **Actualizar `CLAUDE.md` del workspace** (archivo raíz, no versionado) con el nuevo hermano
   y su regla de autocontención.

Pasos 1–4 y 7–8 no dependen de nada externo. El 5 exige levantar la consola; el 6, los
venvs de los 5 repos (existen). El PDF (7) depende del cierre del maestro por el usuario.

## 10. `PUBLICAR.md` — checklist para el usuario (se borra al publicar)

1. Decidir licencias con los coautores (propuesta: CC BY 4.0 paraguas, MIT código) y agregar
   `LICENSE` a los 5 repos de código.
2. Barrido de secretos en la historia de los 5 repos antes de hacerlos públicos. Verificado
   el 2026-08-25: `cameras/` nunca fue commiteado; el `infra/platform/.env` histórico de
   experimental-setup sólo contenía `EOVRT_WORKSPACE` y `COMPOSE_PROFILES` (una ruta). Falta
   correr un barrido automático (p. ej. `gitleaks detect`) como constancia.
3. Coherencia: el primer párrafo del `README` de cada repo dice lo mismo que su ficha en
   `repositorios/README.md`.
4. Crear el repo `simonll4/e-ovrt-vdp` en GitHub (público), descripción y topics de §2;
   `git remote add origin …`; push.
5. Hacer públicos los 5 repos de código.
6. Completar C1 (URLs de los clips de internet) en `evidencia/material-de-video.md` y quitar
   el marcador `<!-- verificar:permitir -->`.
7. Cuando cierre el maestro: exportar PDF → `informe/`, actualizar `informe/README.md`.
8. Tags `informe-2026` en los 5 repos; completar la tabla de versiones; Release `v1.0` con
   el PDF.
9. Poner la URL del repo en la sección de entrega del informe.
10. Borrar `PUBLICAR.md`.

## 11. Fuera de alcance (explícito)

- No se edita el informe `.docx`; no se integra §17.3/17.4/17.5 al maestro.
- No se hace merge a `main` en ningún repo, ni se lista como pendiente.
- No se crean repos ni remotes en GitHub; no se pushea.
- No se genera el video V2 ni se publica ningún video.
- No se migra nada de `docs/` que no sea el entregable y sus figuras.
- No se monta MkDocs/Pages (posible después de la defensa; la estructura lo permite).

## 12. Criterios de éxito

- `python3 herramientas/verificar.py` sale en 0 sobre el repo completo (menos la excepción
  marcada de C1).
- Un lector externo que abre el `README.md` entiende en un scroll qué se hizo, cuál fue el
  resultado, cómo es la arquitectura y a dónde ir.
- Toda cifra de `resultados/` tiene `n`, material y enlace a `results/`.
- Las suites de `evidencia/verificacion.md` tienen fecha y comando; ninguna copiada.
- El repo local queda listo para que el usuario ejecute `PUBLICAR.md` sin volver a pedir
  nada a Claude salvo el PDF.
