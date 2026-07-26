# 70 — Hallazgo F-RT1: "vest" sobre ropa oscura en pruebas EBE (extiende F-G2.1) — y por qué la plataforma NO falló

**Fecha**: 2026-07-25 (tarde, pruebas exploratorias previas al rodaje)
**Modelo**: `gdino-tiny-560` (campeón S1/S2). **Prompt set de ambas corridas**:
`cr01_cr02_v2_safety_vest` (**NO congelado** — exploratorio; el oficial es
`cr01_cr02_v2_short`, doc 67 G1). **No comparables con el bench.**

Dos corridas analizadas, y la conclusión depende de cuál se mire — la primera versión de
este doc analizó solo `rt-01` y llegó a una conclusión parcialmente equivocada; esta
versión la corrige tras revisar `rt1` frame a frame contra sus previews.

## Corrida A — `rt1` (17:50, la toma del chaleco >10 s fuera): media-only

`run_20260725_175051_dbe_grounding_dino_5be0c9`, 195 frames, 41,7 s. **Lanzada desde
"Nueva corrida" (Composición) → solo plano de medios, sin control-plane.** No hubo
evaluación de patrones en vivo: ninguna alerta podía existir, por construcción.

Coreografía real (verificada en previews): actor con remera negra y casco, **sin ningún
chaleco en escena ~0–9 s** (el verde aparece en manos de la segunda persona ~9 s y queda
puesto ~14 s). Segunda persona sentada con buzo oscuro, de espaldas.

**Nivel detección — el hallazgo del usuario, confirmado y cuantificado (F-RT1):** en los
64 frames de la ventana sin chaleco puesto (0→14 s), **el 100 % tiene ≥1 detección
"vest"** — sobre el buzo oscuro del sentado (`previews/frame_000062`: caja `vest 0.37`
sobre la espalda, sin ningún chaleco real en cuadro), sobre la remera del actor, o sobre
el chaleco en mano ajena. Confianza de los falsos: min 0,33 / mediana 0,53 / max 0,89.
F-G2.1 (doc 67) documentaba sobre-marca en prendas reflectantes/fluo; esto la extiende a
**ropa oscura lisa**. El phrasing `safety vest` no lo evita.

**Nivel plataforma — el matching espacial absorbe el ruido en esta toma:** los falsos caen
mayormente fuera de la banda torso del actor, o el matching bipartito 1:1 los asigna a la
otra persona; el actor queda descubierto en 55/64 frames. **Replay con el motor real y el
pattern set oficial v2** (`diag_rt1_v2_oficial`, reproducible):

- **CR-01 high alerta a t=4,1 s** (evidencia desde frame 0)
- **CR-02 medium alerta a t=8,1 s** (evidencia desde frame 23)

**La plataforma hubiera alertado.** La no-alerta observada en vivo se explica entera por
haber lanzado desde Corridas en vez de Experimentos. Esto además valida en datos reales
el diseño del evaluador (matching bipartito por-persona, A4 del doc 58): la sobre-marca
de vest a ~0,5 **no** basta para suprimir CR-02 cuando el falso no cae en el torso del
sujeto o hay más EPP fantasma que personas que cubrir... en esta toma. No es garantía
general: es un caso favorable documentado, no un teorema.

## Corrida B — `rt-01` (17:58): EBE completo, control adjunto

`run_20260725_175846_dbe_grounding_dino_a06c51` + `control_rt-01_20260725T175846Z_736e69`
(1:1 sano, `bus_dropped_events: 0`). CR-01 alertó en vivo (f646). CR-02 no, por dos causas
reales de esa toma:

1. **Ventana sin chaleco de 2,3 s** (f1206→f1275; a f1296 ya se lo estaba poniendo —
   verificado en previews). CR-02 exige 7,0 s continuos: imposible por diseño de la toma.
2. **El chaleco en la mano cubre espacialmente** (bbox dentro de la banda torso) — trampa
   ya escrita en el doc 69 (regla ⚠️ de P2: chaleco fuera de cuadro).

Acá el falso sobre la remera (0,36–0,46, `previews/frame_001233`) fue un tercer factor,
pero subordinado: con 2,3 s de ventana no alertaba ni con detección perfecta.

## Experimento de umbral (sigue válido)

Distribución en `rt-01` (chaleco puesto 114 frames): min 0,36 / p10 0,59 / mediana 0,81.
Falsos sin chaleco: 0,42–0,46. Replay con `min_absent_class_confidence` 0,25→0,60:
**CR-02 falsa con el chaleco puesto** (los dips de perfil caen bajo 0,60 en 11 % de los
frames y la escena sostiene el episodio). **Las distribuciones se solapan: el umbral de
confianza no separa "puesto" de "alucinado"** con este modelo/cámara/luz. La defensa
contra la sobre-marca no es el umbral: es el matching espacial por-persona (ver Corrida A).

## Síntesis para la tesis

- **F-RT1 (nivel modelo)**: GDINO-tiny-560 con prompt `vest`/`safety vest` marca "chaleco"
  sobre ropa oscura lisa (mediana ~0,5, hasta 0,89) — 100 % de los frames de una ventana
  de 14 s sin chaleco. Límite real del zero-shot, medible y medido.
- **Nivel plataforma**: el evaluador espacial (matching bipartito + banda por-persona)
  demostró en replay absorber ese ruido en la toma disponible: CR-02 a los 8,1 s. El
  argumento de tesis es exactamente este contraste: la condición no vive en el detector,
  vive en el patrón — y eso es lo que la capa de patrones aporta sobre el OVD crudo.
- **Ninguna corrida de hoy tuvo a la vez ventana larga Y control adjunto**: la validación
  live de CR-02 sigue pendiente, con pronóstico favorable (el replay de la Corrida A es
  exactamente el cómputo que haría el motor en vivo, mismos eventos, mismo pattern set).

## Cómo seguir

1. **Repetir como EXPERIMENTO (no corrida)**: `ebe_oakd_live` desde Experimentos, con la
   coreografía P2 del doc 69 (hold ≥ 22 s, chaleco fuera de cuadro). Predicción registrada:
   CR-02 confirma ~7 s tras el inicio del hold. Si no confirma, F-RT1 escala a hallazgo
   bloqueante para la toma B de P2 y se prueba remera lisa (regla "vestuario antes que
   software", doc 69).
2. Error operativo a evitar (dos veces hoy): **"Nueva corrida" = solo media-plane, jamás
   alerta.** Toda prueba de patrones va por Experimentos. (La UI ahora tiene
   "+ Nuevo experimento" al lado de "+ Nueva corrida" — sesión 2026-07-25.)
3. Tomas de tesis: siempre `cr01_cr02_v2_short` (congelado).
4. Anotado sin investigar: `fps_effective` 1,72–1,72 en las corridas de la tarde vs 2,62
   al mediodía.

**Artefactos**: replays diagnósticos (`diag_rt1_v2_oficial`, `diag_rt01_vestconf06`) en el
scratchpad de la sesión; corridas en `e-ovrt_media-plane/runs/` y
`e-ovrt_control-plane/runs/` con los ids citados; previews clave:
`rt1/previews/frame_000062` (vest sobre buzo oscuro, sin chaleco en escena),
`rt-01/previews/frame_001233` (doble vest: mano + remera).

---

## Adenda (2026-07-25, noche — tras las corridas P2 oficiales con set congelado)

1. **La magnitud de F-RT1 es mayor que la medida acá.** En la P2 final del día
   (`run_20260725_201145...0eb1fd`, prompt set congelado `cr01_cr02_v2_short`), el
   falso sobre la remera negra lisa llegó a **`vest 0.73`** (preview `frame_000670`,
   verificado visualmente: remera negra, sin ningún chaleco en escena). El rango
   0,36–0,46 de este doc era de la toma exploratoria; el techo real observado es 0,73.
   Consecuencia: la vía del umbral queda **doblemente** descartada — ya no hay margen
   ni teórico (los falsos superan al p10 de "puesto" = 0,59).
2. **La predicción del §"Cómo seguir" punto 1 se cumplió por la negativa**: la
   repetición como experimento con hold correcto y chaleco fuera de cuadro NO
   confirmó CR-02 (2 corridas P2, 0 alertas; solo 4 frames de evidencia en 83 con
   sujeto). F-RT1 escala a **hallazgo confirmado de supresión de CR-02 live** con
   este modelo/cámara/vestuario. Detalle completo y hallazgo hermano **F-RT2** (la
   detección intermitente de YOLOE corrompe la ventana temporal — el modo de falla
   opuesto): **doc 71 §2**.
