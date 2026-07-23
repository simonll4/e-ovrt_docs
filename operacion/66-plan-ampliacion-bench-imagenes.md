# 66 — Plan de ampliación del bench de imágenes (2026-07-23)

Responde al déficit señalado en el análisis realista post-S2: `bench_obra` es honesto pero
chico (147 imgs; vest n=79, bare_head n=61, violadores CR-01 n=65 ⇒ IC de ±0.12 en recall).
Objetivo: **n≥300 por clase y ≥2 fuentes**, sin sacrificar la honestidad ganada en S0.

## Precondición metodológica (antes de tocar datos): congelar prompts

Regla anti-fuga: **ningún dato que entre al bench puede usarse para calibrar prompts** (sería
overfitting del "modelo" — acá el prompt ES parte del modelo). El set `cr01_cr02_bench_v2`
está fijo desde Sprint 2 y S1 corrió con él; se declara **congelado para evaluación de
bench** antes de incorporar imágenes nuevas. Las corridas de calibración del carril 2 de la
estrategia de prompts usan EXCLUSIVAMENTE material que no esté en ningún bench (p.ej. DEMO
split o el train de CHV no promovido).

## B1 — Promover CSS-train curado (la ganancia grande, misma fuente)

`construction_site_safety/train`: 2.603 imgs con GT completo: Person 9.691, Hardhat 3.362,
**NO-Hardhat 2.318** (→ bare_head + `has_helmet=false`), Safety Vest 3.156, **NO-Safety Vest
3.957** (→ `has_vest=false`, habilita atributos CR-02 que el bench actual casi no tiene).

1. Aplicar la curación S0 (mismas 12 reglas de prefijo + área mínima, script extendido) —
   esperar ~25% de exclusión como en test/val.
2. Auditoría visual muestral (~30 imgs con GT dibujado) ANTES de promover: el train split
   nunca fue mirado a ojo.
3. **Dedup perceptual contra test/val** (política ya declarada en class_mapping.yaml): los
   splits Roboflow salen de los mismos videos ⇒ near-duplicates entre train y test/val
   inflarían el n sin agregar información. Reportar cuántos se excluyen.
4. Convertir con `convert_datasets.py` (ya soporta CSS) + `build_person_gt.py` para extender
   el GT persona-nivel (violadores CR-01 y CR-02 nuevos).
5. Salida: `bench_obra_ext_css` con estrato declarado `fuente=css_train`.

Advertencia declarada: sigue siendo LA MISMA fuente Roboflow — sube n y precisión de los IC,
NO independencia. La independencia la aportan B2/B4.

## B2 — CHV a rol BENCH (segunda fuente, académica)

CHV (ZijianWang, PPE_detection, 1.330 imgs, YOLO): person + helmet(4 colores) + vest. Está
en rol TRAIN, pero **no entrenamos**: reasignarlo a BENCH es legítimo si (a) los prompts ya
están congelados (precondición) y (b) se excluye del carril de calibración.

1. Auditoría S0 muestral (dominio "parcial" según scoring: verificar cuánto es obra real).
2. Sin negativos explícitos ⇒ **aporta AP de person/helmet/vest, NO CR-01/CR-02** (el
   contrato v2 prohíbe derivar bare_head por resta — se respeta).
3. Chequeo de solape contra ppe-dataset rechazado (comparten stems `ppe_XXXX`) y contra CSS.
4. Salida: estrato `fuente=chv` para AP por clase con n independiente.

## B3 — ppe_siabar: decisión post-auditoría (prioridad baja)

1.612 imgs person/helmet/vest, pero el scoring lo marca `dominio_obra_civil: no`. Auditar 20
imgs: si el dominio es genérico-industrial, NO entra al bench de obra (puede servir como
robustez out-of-domain declarada, que es otra pregunta). No gastar más de 30 min.

## B4 — Fuente externa nueva: adoptar SHEL5K (investigación 2026-07-23 cerrada)

Se investigaron 8 candidatos académicos con los criterios de entrada (GT de person + dominio
obra + licencia citable + descarga viva; links y licencias verificados uno a uno):

- **ADOPTAR: SHEL5K** (Otgonbold et al., *Sensors* 2022; Mendeley Data `9rcv8mm682` v4,
  **CC BY 4.0**, descarga directa sin registro, VOC XML). 5.000 imgs / 75.578 labels en 6
  clases que mapean nativo: `person_with_helmet ∪ person_no_helmet` → person (¡con atributo
  has_helmet gratis!), `helmet` → helmet, **`head` → bare_head SIN derivación** — GT nativo
  de nuestra clase más débil, la que más necesita n. No trae vest. Costo: hereda un
  subconjunto no-obra (aulas) del Kaggle original ⇒ **auditoría de dominio S0 obligatoria**
  antes de promover (mismas herramientas de mosaicos).
- **Opcional 2º: CHVG** (Ferdous & Ahsan, *PeerJ CS* 2022; figshare, **CC BY 4.0**, 1.699
  imgs): el único con los 4 conceptos (person body / hardhat / vest / head) en obra real —
  PERO es la extensión de nuestro CHV: exige dedup imagen-a-imagen contra los splits v2 y el
  remanente puede quedar chico. Entra solo si tras dedup aporta n material.
- **Reserva: SH17** (CC BY-NC-SA, 8k imgs, 4 clases, ya tenemos script de descarga legacy) —
  volumen y vest, pero dominio "foto de stock Pexels": no como núcleo del bench.
- **Descartados con evidencia**: SODA (link oficial 404, solo Baidu, sin licencia — una pena:
  el mejor dominio), GDUT-HWD (sin clase person; Baidu-only), SHWD (su "person" son cabezas
  y mezcla aulas — mismo patrón que el ppe-dataset rechazado), Pictor-v3 (sin licencia, 774
  imgs útiles), SFCHD (sin licencia declarada; safety-clothing ≠ vest — reconsiderar si los
  autores licencian: dominio CCTV industrial excelente).

Registro completo del informe: agregarlo a `datasets/registry/` al ejecutar B4.

## B5 — Consolidación: `bench_v3` estratificado y congelado

- Estructura: estratos por fuente (`css_testval`, `css_train`, `chv`, `externo?`) con
  métricas reportables por estrato Y agregadas; n por clase declarado siempre.
- El bench_obra actual (147) queda como **estrato núcleo verificado** — es el único con
  pasada visual completa; el resto entra como "curado por muestreo" hasta pasada humana.
- Congelamiento con manifest + sha256 antes de re-correr campeones (S1 NO se re-corre entero:
  solo `gdino-tiny-560`, `gdino-base-560` y `yoloe-26x` como contraste, sobre el bench ampliado).
- Registro en `datasets/registry/` (mismo patrón que `curation_bench_obra.md`).

## Esfuerzo estimado y orden

B1 (medio día, mayormente automatizable) → B2 (2-3 h) → B5 parcial (re-correr campeones,
~1 h GPU) → B4 si el informe da un ganador (1 día incl. descarga+auditoría) → B3 solo si
sobra tiempo. Con B1+B2 solos: vest pasa de n=79 a ~2.000+, bare_head de 61 a ~1.500+,
violadores CR-01 de 65 a ~1.000+ — los IC bajan de ±0.12 a ±0.03. **El rodaje no se toca ni
se retrasa por esto: es trabajo de Claude en paralelo.**
