# Guion de grabación — Bloque A (episodios de alerta, grabación propia)

> ⚠️ **PARA EL DÍA DEL RODAJE, USAR EL DOC 69** (`69-guion-operativo-rodaje.md`): es el
> documento de campo, autocontenido, adaptado al equipo real (3 personas, 2 cascos, 2
> chalecos, 1–2 personas en cuadro) y con la plataforma ya verificada de punta a punta.
> **Este documento 59 queda como la referencia metodológica**: por qué existe cada
> escena, de dónde salen las duraciones y los umbrales, y el registro de las revisiones.
> Ante conflicto operativo, gana el 69.

> **Propósito**: shot-list operativo para la sesión de grabación con el equipo.
> Derivado de `57-validacion-metodologica-externa-duracion-clips.md` (§1–§2, §6.3–§6.4)
> y spec 43 §3.1. Este documento se lleva impreso a la obra/locación: cada toma tiene
> casillas de verificación y marcadores temporales que el operador guiona en voz alta.
>
> **Contexto de banco (2026-07-19)**: el material de internet disponible es casi todo
> obra en cumplimiento de PPE → cubre el pilar negativo (soak, FAR, precisión); la
> única excepción es `4.1.mp4` (un CR-01 espontáneo evaluable, doc 58 §B.2.1 — caso
> duro nocturno, no showcase). Los episodios de alerta guionados (Px) **no existen
> en material público** y se producen con el equipo según este guion. Ver §6 para
> el pilar negativo y §7 para las corridas EBE en vivo.

---

## 1. Reglas de oro (si se rompen, el clip no sirve para medir)

1. **Onset en t≈3–4 s.** El actor arranca SIEMPRE en cumplimiento (casco y chaleco
   puestos) o neutral; la condición de riesgo aparece a los 3–4 s de toma. Si arranca
   ya en infracción, se pierde el onset → TTFD degenera a 0 y el clip queda censurado.
2. **Cola > resolve.** Tras corregir la infracción, seguir filmando **≥ 2–3 s** en
   cumplimiento para capturar el cierre del episodio y descartar alertas tardías.
3. **Toma de 30–35 s** aunque el clip final sea de 20 s: el recorte fino se hace
   después (re-ventaneo con onset en t≈3–4 s). Nunca cortar la cámara "justo".
4. **Los tiempos son del timeline real del video** (spec 43 §3.3: el GT sale del
   video, no del plan). El operador cuenta en voz alta o usa cronómetro visible
   fuera de cuadro para marcar onset y end.
5. **Cada escenario se graba 2–3 veces** variando distancia / luz / oclusión parcial
   (matriz C.2). Cuesta minutos en sesión y multiplica la robustez del banco.

**Vestuario/props**: casco, chaleco reflectante, gorra común (para P9), campera
naranja no reflectante (para P9). Al menos 2 personas para P7/P8 (ideal 3).

---

## 2. Plantillas base (cubren el 90 % del banco)

### Plantilla ALTA — PR-01 sin casco (objetivo 20 s)

```
0–3 s    pre-roll: persona CON casco (baseline, habilita TTFD)
3 s      ONSET: se quita el casco                    ← episodio start_ms≈3000
3–17 s   infracción sostenida (≥14 s)                  (confirma a t≈7 s; alerta
                                                        lenta admisible hasta t≈13 s)
17 s     END: se vuelve a poner el casco             ← episodio end_ms≈17000
17–20 s  cola en cumplimiento (>resolve 2 s)
```

### Plantilla MEDIA — PR-02 sin chaleco (objetivo 30 s)

```
0–4 s    pre-roll: persona CON chaleco
4 s      ONSET: se quita el chaleco                  ← episodio start_ms≈4000
4–26 s   infracción sostenida (≥22 s)                  (confirma a t≈11 s; alerta
                                                        lenta admisible hasta t≈24 s)
26 s     END: se pone el chaleco                     ← episodio end_ms≈26000
26–30 s  cola en cumplimiento (>resolve 3 s)
```

Los demás escenarios son variaciones de estas dos (ver shot-list).

---

## 3. Shot-list — clips de alerta (n objetivo ≈ 12–15 episodios)

Marcar cada toma completada. `[R]` = repetición con variación de captura.

### P1 — CR-01 sin casco (Plantilla ALTA, ~20 s) — mínimo 2 clips

- [ ] **P1-a** — plano medio, buena luz, sin oclusión
- [ ] **P1-b** — mayor distancia o luz desfavorable
- [ ] **P1-c** `[R]` — con oclusión parcial (pasa detrás de un obstáculo durante el evento)

Guion por toma: entra caminando CON casco (3 s) → se lo quita → sostiene ≥14 s
(puede seguir trabajando/caminando) → se lo pone → 3 s más en cuadro. **Cortar cámara
recién a los ~33 s.**

### P2 — CR-02 sin chaleco (Plantilla MEDIA, ~30 s) — **mínimo 3 clips** *(✎ 07-19: era "mínimo 2"; doc 57 §6.8 sube P2 a ×3 — es el denominador más flaco del banco y la toma extra cuesta 2 min)*

- [ ] **P2-a** — plano medio, buena luz
- [ ] **P2-b** — distancia/luz desfavorable
- [ ] **P2-c** `[R]` — oclusión parcial

Guion: entra CON chaleco (4 s) → se lo quita → sostiene ≥22 s → se lo pone →
4 s más. **Cortar a los ~35 s.**

### P4 — Resolución en cuadro (22–25 s) — 1 clip

- [ ] **P4-a**

Guion: plantilla ALTA pero la cola se estira: tras ponerse el casco (t≈13 s),
**permanece en cuadro ≥10 s ya resuelto**. Verifica cierre por resolve y ausencia
de alertas tardías. **Cortar a los ~30 s.**

### P6 — Doble condición (sin casco Y sin chaleco, 25–30 s) — 1 clip

- [ ] **P6-a**

Guion: plantilla MEDIA con dos episodios solapados. Entra con ambos EPP (4 s) →
se quita el casco (onset CR-01) → ~3 s después se quita el chaleco (onset CR-02) →
sostiene ambos → se pone el chaleco → se pone el casco → cola 3–4 s.
Anotar en la hoja los 4 marcadores (2 onsets, 2 ends). **Cortar a los ~35 s.**

### P7 — Multi-persona / cruces (demo G1, 25–30 s) — 2–3 clips

- [ ] **P7-a** — 2 personas: una en cumplimiento todo el clip, la otra sigue plantilla ALTA
- [ ] **P7-b** — 2–3 personas cruzándose entre sí y frente a cámara (~10 s de coreografía
      de cruces) mientras el infractor sostiene el evento ≥8 s
- [ ] **P7-c** `[R]` — variación: el infractor es otro actor / otra prenda

Guion: los cruces deben ocurrir DURANTE el evento (para estresar el tracker), no en
el pre-roll. Cada sujeto infractor sostiene ≥8 s. **Cortar a los ~35 s.**

### P8 — Entrada/salida de cuadro (**30 s mínimo**) — 1 clip *(✎ 07-19: era "26–30 s"; el ep2 arranca en t≈16 s ⇒ floor del gate A1 = 16+10+2+2 = 30 s — a 26–28 s el clip queda marcado `dimensioning_warning`)*

- [ ] **P8-a**

Guion: entra sin casco *ya con pre-roll de 3 s en cumplimiento y onset en cuadro*
→ evento 8 s → **sale de cuadro ≥5 s** (más que resolve: el episodio 1 debe cerrar)
→ re-entra aún sin casco → evento 8 s (episodio 2 nuevo) → se pone el casco →
cola 2–3 s. **Cortar a los ~35 s.** Anotar ambos episodios por separado.

---

## 4. Shot-list — clips de ausencia (P3/P5, ~15 s) y confusables (P9, 18–20 s)

El veredicto de P3/P5 es "NO debe dispararse alerta" (requieren observar ≥1
ventana de confirmación completa post-estímulo). **P9 es distinto (✎ 07-19): SÍ
lleva episodio real** — está en esta sección solo por afinidad de guion.

### P3 — Transitorio no alertable (~15 s) — 1 clip

- [ ] **P3-a**

Guion: entra CON casco (3 s) → se lo quita **solo ~2 s** (sub-umbral: menor que la
ventana de confirmación de 4 s) → se lo pone → permanece en cuadro ≥9 s.
Veredicto: cero alertas. **Cortar a los ~20 s.**

### P5 — Cumplimiento total (15–20 s) — 1 clip (= V3 de la defensa)

- [ ] **P5-a**

Guion: 1–2 personas con EPP completo trabajando normalmente todo el clip.
(Si el material de internet ya aporta esto en abundancia, este clip propio es
opcional pero barato: grabar igual una toma controlada.)

### P9 — Confusables semánticos (**18–20 s**, ✎ 07-19: al ser infracción CR-01 real rige el floor 17 s del gate) — 1–2 clips

- [ ] **P9-a** — persona con **gorra** (no casco) y/o **campera naranja** (no chaleco)
- [ ] **P9-b** `[R]` — casco **en la mano** o colgado, no puesto

Guion: el actor entra con el confusable puesto y permanece ≥12 s. Veredicto según
GT: gorra ≠ casco (debe alertar CR-01 si el patrón lo exige) / la anotación decide.
Alimenta además los argumentos A1–A5 de la defensa (nucleo/09).
**Nota**: revisar también el material de internet en busca de confusables naturales.

---

## 5. Hoja de registro por toma (llenar en el momento)

Copiar esta tabla por cada toma realizada; estos datos son el borrador del GT.

| Campo | Valor |
|---|---|
| ID toma (ej. P1-a-take2) | |
| Fecha / locación / cámara | |
| Onset real (s del timeline) | |
| End real (s del timeline) | |
| Variación de captura (distancia/luz/oclusión) | |
| Incidencias (se rompió regla de oro?, repetir?) | |

---

## 6. Pilar negativo — material de internet (referencia, no se graba)

Registrado acá para que el banco quede completo en un solo documento:

> **✎ 2026-07-19 (más tarde) — actualizado con el lote real (doc 58 §B.2.1):**
> el supuesto "no hay tomas de 5–10 min" quedó viejo — **`6.1.mp4` es una toma
> CONTINUA de 6:10** (0 cortes de escena verificados) y el lote completo suma
> **~16 min** de cumplimiento (14 videos, 20 s–6:10), o sea **el objetivo de
> ≥15 min agregados ya está cumplido**. El régimen de reporte de abajo (FP/min
> agregado + cota superior) queda **ADOPTADO** como la forma canónica de
> presentar FAR — es más honesto que FP/hora extrapolado. La implementación A3
> (`far_per_hour` + `observed_duration_ms` por clip) ya soporta la agregación
> Σ FP / Σ duración; el cambio de unidad es de presentación.

- Los videos de obra real en cumplimiento se usan **enteros, sin recortar**,
  como material soak `negative: true`.
- La métrica FAR se reporta a la escala de la ventana real: **"X FP en N minutos
  de cumplimiento (agregado de K clips)"** + tasa en **FP/min**; el equivalente
  FP/hora solo entre paréntesis y marcado como extrapolación. Con 0 FP observados
  se reporta **cota superior** (regla de ~3/N al 95 %), no "FAR = 0".
- Objetivo de acumulación: **≥ 15–30 min** de tiempo negativo agregado —
  **cumplido con el lote 2026-07-19 (~16 min)**; el soak propio del rodaje suma
  margen.
- **Advertencia del prefiltro (A7, doc 58):** GDINO sobre-marca `bare_head` a la
  distancia de estas cámaras (peor de noche) — se espera FAR **alto** en este
  material, especialmente en los 4 nocturnos. No es un defecto del banco: es el
  resultado de Nivel A que la persistencia de Nivel B debe filtrar, y se reporta
  como tal.

---

## 7. EBE en vivo durante la sesión (doble toma — ver doc 58 §C.5)

Además de grabar, se ejecutan **corridas live** (EBE) con la plataforma real:
producen `t_capture→alert`, `t_compute-budget`, G2A en vivo y salud del bus —
métricas que el banco grabado NO puede dar (ADR-013). **Regla: doble toma** —
la toma grabada va al banco (GT en CVAT); la toma live (misma coreografía) es
una corrida EBE **sin GT**. Escenas live mínimas: **1× P1, 1× P2, 1× P3**.

**El día ANTES (dry-run obligatorio):**
- [ ] Servicios `:8080` + `:8081` arriba; cámara con preset y encuadre verificado
      en la ventana Cámaras (preview)
- [ ] **Grabación verificada con las dos cámaras**: una toma de 60 s con la RTSP y
      otra con la OAK-D desde la ventana Cámaras. Chequear en el sidecar
      `.rec.json`: `measured.fps` cercano al pedido, `measured.resolution` la
      esperada (si sale < 1280 de ancho, el preset apunta al substream del DVR),
      `truncated: false`.
- [ ] **Etapa 0 sobre un master grabado**: `prepare_clip.sh` sobre la toma de
      prueba emite un `info.json` con `n_frames` coherente. **Trampa verificada:
      `--to` es relativo a `--ss` (funciona como duración, NO como punto de corte
      absoluto)**. Ejemplo real (ffmpeg 8.0.1, fuente de 20 s): `--ss 5 --to 8`
      da un clip de **8 s** (240 cuadros a 30 fps), no de 3 s. Para extraer del
      segundo 12 al 32 del master hay que escribir `--ss 12 --to 20` (duración =
      32 − 12 = 20), nunca `--to 32`. Si se escribe mal **no falla**: el clip
      queda más largo y el evento desalineado respecto de las anotaciones. Si
      esto no cierra, el material del rodaje no entra al banco.
- [ ] **Espacio en disco**: ≥ 5 GB libres (la consola lo exige) y destino en el
      filesystem nativo de WSL, nunca bajo `/mnt/c`.
- [ ] Config live con pattern set **`cr01_cr02_v2`** (4000/7000, NO el v1)
- [ ] Modelo **`EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560`** cargado (campeón S2,
      doc 64 — no el `gdino-tiny` a 800); disco libre para `runs/` (checklist completo
      del día: doc 67 G5 — ≥20 GB, servicios desde la raíz de su repo)
- [ ] **Smoke live**: actor se quita el casco ~6 s → alerta CR-01 confirmada a
      ~4 s, `bus_dropped_events = 0`, cierre `run_finished`. Si falla, se
      arregla HOY, no en el rodaje.

**Qué produce cada toma (para que nadie dude por qué se hace dos veces):** la
**toma A grabada** es el material re-corrible — sobre ella corre después TODO lo
offline (banco DBE, GT en CVAT, comparación de modelos, E-DIR vs E-IND, cualquier
prompt set futuro), infinitas veces. La **toma B live** produce las métricas que
SOLO existen en vivo (`t_capture→alert`, G2A live, salud del bus) y no se pueden
regenerar después. Por eso: **si una toma B sale mal, se repite EN EL MOMENTO** —
es la única parte del experimento que no tiene segunda oportunidad.

**Secuencia por escena live (doble toma, orden fijo A→B, verificada en el ensayo
G2 del 2026-07-23 — doc 67):**

*Toma A (grabada):*
- [ ] 1. Grabar desde la ventana Cámaras de la consola. **NADIE actúa hasta que
      la UI salga de `starting`** (la OAK-D tarda ~9 s en conectar) y el operador
      cante "grabando" (regla F-DR6, §9).
- [ ] 2. Coreografía completa del guion: pre-roll en cumplimiento 3–4 s → onset
      cantado → infracción sostenida (≥14 s P1 / ≥22 s P2) → reversión cantada →
      cola ≥3 s. **Cortar cámara recién a ~33 s.**
- [ ] 3. Chequear el sidecar `.rec.json` (`measured.fps`/`resolution` esperados,
      `truncated: false`). El recorte fino (`prepare_clip.sh`) es POST-rodaje,
      no se hace en la sesión.

*Toma B (live, misma coreografía, inmediatamente después):*
- [ ] 4. Disparar control-plane: `POST :8081/api/runs` `{mode: live}` → esperar
      **201 con `subscribed: true`** en el estado (orden NO negociable: control
      SIEMPRE antes que media). Un **409** = ya hay run activo → **reusar** el
      `active_run_id`, no borrarlo. La clave del estado es `control_run_id` y el
      terminal es `succeeded`.
- [ ] 5. Disparar media-plane: `POST :8080/api/runs` con `bus.enabled: true` y
      el prompt set congelado **`cr01_cr02_v2_short`** (vía consola/runner con
      `experiment_id` — el runner hace los dos POST en el orden correcto).
      **Antes de lanzar, revisar que `warmup_frames` NO esté vacío** (poner **20**):
      es un ajuste por-run con default `0`, no viene del preset de cámara, y en
      blanco deja entrar los primeros frames oscuros de la OAK-D (doc 68, trampa 7).
- [ ] 6. **Regla del primer frame (hermana de la del `starting`, aprendida en la
      claqueta fallida del G2): NADIE entra a escena hasta que
      `progress.units_processed > 0`** en `GET :8081/api/runs/{control_run_id}`
      (la OAK-D tarda ~8–9 s en conectar tras el POST; actuar antes = actuar
      para nadie). El operador lo canta ("pipeline vivo").
- [ ] 7. Coreografía idéntica a la toma A (mismos tiempos, mismos cantos).
- [ ] 8. Cortar: `POST :8080/api/runs/{media_run_id}/stop` → esperar terminal en
      AMBOS planos (media `stopped`, control `succeeded`; tarda ~6 s). Overhead
      mecánico total medido de una toma B: **~15 s** + coreografía.
- [ ] 9. **ANTES de desarmar la escena**, verificar en el estado del control:
      `bus_dropped_events = 0` **Y la alerta esperada emitida** (`alerts_count`
      se ve en caliente): P1 → CR-01 a ~4 s del onset; P2 → CR-02 a ~7 s;
      **P3 → NINGUNA alerta** (esa es la demo). Si P2 no alertó → F-G2.1:
      ¿algo con franjas o colores hi-vis en cuadro? → corregir vestuario y
      **repetir la toma B ahora** (es barata; después es imposible).
- [ ] 10. Hoja de registro: `experiment_id`, `media_run_id` + `control_run_id`,
      escena, hora, ¿alertó cuando debía?, incidencias. **NO borrar `runs/`** —
      el JSONL live se re-evalúa offline después (paridad live↔offline con
      contenido real = evidencia citable).

**Opcional (stretch):** 1 escena con **claqueta** (palmada visible a cámara +
anotar la hora exacta) → habilita GT live anclado y la verificación numérica de
`t_alert = TTFD + t_capture→alert` (spec 40 §5.2.2). Si no se puede, se difiere
sin costo.

## 8. Checklist de cierre de la sesión de grabación

- [ ] ≥2 P1, **≥3 P2**, 1 P4, 1 P6, 2–3 P7, 1 P8 completados (n≈12–15 episodios)
- [ ] **Corridas EBE live** (§7): ≥1 P1 + ≥1 P2 + ≥1 P3 con `run_finished` y
      `bus_dropped = 0`; `experiment_id` de cada una en la hoja
- [ ] 1 P3, 1 P5, 1–2 P9 completados
- [ ] **V1 y V2 de la defensa** grabados en la misma sesión (doc 58 §B.1: V1 =
      cadena completa infracción→alerta, el clip demo, 25–30 s, la toma más
      vistosa; V2 = clase nueva por config según guion doc 09, 20–30 s; V3 ≡ P5)
- [ ] **Soak propio opcional** (5–10 min, trípode, obra normal): el lote de
      internet ya cubre FAR (~16 min), pero una toma propia diurna suma margen
      y control
- [ ] Toda toma tiene su hoja de registro con onset/end reales
- [ ] Ninguna toma arranca ya en infracción (regla de oro 1)
- [ ] Todas las tomas tienen cola > resolve (regla de oro 2)
- [ ] Copia de seguridad del material crudo antes de salir de la locación

## 9. Revisión 2026-07-23 (tramo 3 del doc 60 §8, con lo aprendido en dry-run/L0)

Estas reglas ENMIENDAN lo anterior; ante conflicto, gana esta sección.

1. **Config oficial de las corridas (S2/G1 cerrados):** modelo
   `EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560` (campeón, doc 64); prompt set
   **`cr01_cr02_v2_short` CONGELADO** (sha `df81fd48…`); pattern set `cr01_cr02_v2`;
   prefilter EN-2 APAGADO (D-61.2); sin cascada (D-61.1). Presupuesto real medido:
   ~3,3 fps live y g2a ~310 ms con caption de 3 clases (doc 65) — dentro de lo que
   la persistencia 4000/7000 tolera.
2. **Regla dura del `starting` (F-DR6):** NADIE actúa hasta que la UI de grabación
   salga de `starting` (la OAK-D tarda ~9 s en conectar). El operador lo dice en voz
   alta ("grabando") antes de que el actor entre en escena.
3. **Cantar el evento (doc 60 §9):** el actor u operador canta en voz alta el inicio
   y fin de cada infracción actuada ("me saco el casco… casco puesto"). Queda en la
   hoja de registro y desambigua el onset en CVAT.
4. **Seguridad de escena (regla nueva, explícita):** toda infracción se actúa a
   nivel de piso, lejos de bordes, huecos y maquinaria; el EPP real está disponible
   en escena para el estado cumplidor; consentimientos firmados ANTES de la primera
   toma; nadie actúa una infracción real de altura ni de proximidad a equipos.
5. **Trampas operativas del día** (doc 65/67): servicios lanzados DESDE la raíz de
   su repo; orden EBE control-primero (`subscribed:true`); terminal = `succeeded`;
   409 en control = reusar el run activo; Ctrl+Shift+R tras cambios de frontend;
   entrar a la consola por `/`; verificar `bus_dropped_events=0` ANTES de desarmar
   cada escena live; inventario contra §8 antes de liberar a los actores.
