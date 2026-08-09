# Resumen para el equipo — duraciones de los clips y qué métricas podemos medir

> ## ✎ HISTÓRICO — RESUMEN PRE-RODAJE (banner agregado 2026-08-06)
>
> Foto del 2026-07-20, **anterior al rodaje** (2026-07-25): su §8 ("estado del
> material") y §9 ("qué sigue") describen en futuro cosas ya ejecutadas — el rodaje
> se hizo, el GT del banco está `gt_ready` (34 clips, doc 80) y el tramo experimental
> está completo (docs 92/98). No usar como estado; para el presente, entrar por
> `00-indice.md` o `operacion/95`.

**Fecha:** 2026-07-20 · **Fuentes:** docs/operacion/57 (metodología), 58 (plan de cierre), 59 (guion de grabación).
Este documento es un resumen de lectura. La fuente de verdad sigue siendo 57/58/59.

---

## 1. La idea central

La duración de un clip no es un detalle de producción: **determina qué métricas se pueden
calcular con él**. Un clip corto no da un resultado "peor", da un resultado *inválido* —
por ejemplo un TTFD de 0 ms que es un artefacto del recorte, o un "no alertó" que en realidad
es "el clip se terminó antes de que la alerta pudiera ocurrir".

Por eso el banco de video está **estratificado por duración**, no grabado a una duración única.

## 2. Las dos constantes que mandan

El motor confirma una alerta solo si la condición persiste:

| Patrón | Condición | Persistencia | Resolve | Target de alerta |
|---|---|---|---|---|
| **CR-01** (alto) | persona sin casco | **4 s** | 2 s | 5–10 s |
| **CR-02** (medio) | persona sin chaleco | **7 s** | 3 s | 10–20 s |

De ahí sale la fórmula de dimensionamiento:

```
duración = pre-roll (≥3-4 s) + evento + cola (≥ resolve + 2 s)
```

Y la **restricción dura** ("censura temporal"): el clip tiene que ser lo bastante largo para
que una *alerta lenta pero válida* quepa adentro. Si no, no podemos distinguir
"alertó a los 18 s (pasa)" de "no alertó nunca (falla)".

- CR-01 necesita `onset + 10 s` dentro del clip → **≥ 14–15 s**
- CR-02 necesita `onset + 20 s` dentro del clip → **≥ 23–24 s**

**Regla de grabación:** el evento nunca arranca en t=0. El onset va en t≈3–4 s.
Se graban tomas de ~30–35 s y se recortan al presupuesto de cada escenario.

## 3. Duraciones decididas por escenario

**La duración óptima es bimodal:**
- **~15 s** para los clips cuyo veredicto es *ausencia de alerta* (P3, P5).
- **~25–30 s** para los clips cuyo veredicto es una *alerta medida* (P1 entra en 20 s).
- **5–10 min** para el/los clips **soak** — el único material que da denominador para FAR.

| Escenario | Qué es | Duración |
|---|---|---|
| P1 | CR-01 persistente | **18–20 s** |
| P2 | CR-02 persistente (×3 tomas) | **25–30 s** |
| P3 | transitorio sub-umbral, NO debe alertar | **15 s** |
| P4 | resolución del episodio | **22–25 s** |
| P5 | cumplimiento total (negativo) | **15–20 s** |
| P6 | doble condición | **25–30 s** |
| P7 | multi-persona | **25–30 s** |
| P8 | entrada/salida (2 episodios) | **≥30 s** |
| P9 | confusables (gorra, campera naranja) | **18–20 s** |

Banco total ≈ **21–25 clips**: 13 guionados (Bloque A) + 2 de defensa (V1, V2) + 5–8 de relleno
+ 1–2 soak. Objetivo ~8–10 episodios evaluables por patrón; piso de seguridad n≥8.
Más de ~25 clips no cambia ninguna conclusión y duplica el trabajo de anotación.

### Dos reglas duras
1. **No concatenar clips cortos** para fabricar uno largo: el corte de escena crea onsets
   artificiales y rompe la semántica del episodio.
2. **P2, P4, P6 y P8 no se rellenan con material corto de internet.** Si faltan, se graban.

### Gate automático (A1, ya implementado)
`derive_clip_gt.py` computa, por episodio, el piso de duración y emite
`dimensioning_warnings` en el GT. **Avisa, no bloquea** — queda auditado.

---

## 4. Qué mide cada tipo de clip

| Métrica | Qué necesita | Piso |
|---|---|---|
| **Recall** de episodios | que la alerta quepa | CR-01: onset+10 s · CR-02: onset+20 s |
| **Precision / FP** | tiempo sin evento (cola + soak) | cola ≥ resolve+2 s |
| **TTFD** (onset→1ª detección) | **pre-roll real** | ≥3 s de pre-roll |
| **SDR** (detección sostenida) | evento largo | ≥8 s (CR-01) / ≥12 s (CR-02) |
| **t_alert-system** | que la alerta más lenta quepa | igual que recall |
| **FAR/hora** | volumen de tiempo en cumplimiento | **soak de 5–10 min** |

## 5. Los dos niveles del reporte

La frontera es la identidad de spec 40:

```
t_alert-system  =  TTFD  +  t_capture→alert
                 (DETECCIÓN)   (PLATAFORMA)
```

**Nivel A — rendimiento del modelo OVD** (¿el modelo *ve* la condición?)
AP@0.5 por clase, recall espacial, **TTFD**, **SDR**, G2A/FPS/drops.
Se usa para comparar modelos y estrategias de prompt, con la plataforma congelada.
→ P9 (confusables) es Nivel A: mide recall bajo estrés semántico, no falsos positivos.

**Nivel B — comportamiento de alertado de la plataforma** (¿alerta cuando debe y calla cuando debe?)
Recall de episodios, precision + **FAR/hora**, P3/P5 en cero alertas, **t_alert-system**,
t_capture→alert. Se valida con el modelo ganador de Nivel A ya fijo.

**Por qué importa la separación:** si alguien objeta "el modelo detecta mal" (sabemos que
`bare_head` es débil), la respuesta es: *eso es Nivel A, está medido y declarado; la tesis
se juzga en Nivel B*.

**Régimen de reporte:** percentiles P50/P95/P99 solo para métricas por-frame.
Todo lo por-episodio (TTFD, SDR, Nivel B) va como **mediana + rango + muestra completa**,
con **n declarado por métrica** — con n≈10 un P95 es el máximo disfrazado.

---

## 6. Qué queda INVIABLE o censurado, y por qué

### 6.1 Censura por duración (`metric_censored`, ya implementado)
Un episodio demasiado corto para que el veredicto sea concluyente **sale del denominador**
de esa métrica, en vez de contarse como fallo. El reporte lo declara:
*"t_alert PR-02: n=X episodios evaluables (clips ≥29 s)"*.

### 6.2 Métricas que requieren corrida **live** (no salen de video grabado)
`t_capture→alert`, `t_compute-budget`, G2A live y `bus_dropped_events` usan reloj wallclock;
en replay sobre archivo quedan `not_interpretable`. Además el ancla wallclock↔media
**sigue sin resolver**.

**Solución: protocolo dual-take** (se ejecuta en la misma jornada de rodaje)
- **Toma A grabada** → banco DBE → CVAT → TTFD / SDR / t_alert / recall **con GT**.
- **Toma B live** (misma coreografía) → corrida EBE 1:1 → t_capture→alert / G2A / bus **sin GT**.

Cada plano mide lo suyo y nadie necesita el ancla. Mínimo: 1× P1, 1× P2, 1× P3 en live.
*Trampa operativa:* primero se dispara el control-plane (`POST :8081/api/runs`, mode live) y
**después** el media-plane con `bus.enabled: true` — PUB/SUB pierde todo lo anterior a la suscripción.

### 6.3 Métricas excluidas con causa
- **`t_alert-notification`** → requiere spec 45 (MQTT), que va para lo último.
- **`ΔFP_tracker`** → solo aplica a labs con tracker; en la plataforma G0 se excluye.
- **TTFA interna** → diagnóstico, no se reporta como resultado.
- **`t_alert-system` NO sirve para comparar modelos**: está dominada por la constante de
  persistencia (4000/7000 ms), idéntica entre corridas — aplasta la diferencia real.
  Por eso el criterio de desempate de D1 se cambió a **TTFD**.

### 6.4 Artefactos conocidos
- `video16_clip10`: TTFD = 0 ms es artefacto de recorte (el episodio empieza en t=0).
- Los videos viejos de 12 s en `raw/` **ya son clips cortados**, no hay original más largo
  para re-ventanear. Mantienen rol diagnóstico/negativo, nunca P2/P4/P6/P8.
- `bare_head` sobre-marca a distancia (prefiltro GDINO: 8/10 tracks de noche). El prefiltro
  **no puede auto-certificar negativos** → verificación humana. Esa sobre-marca no se descarta:
  es insumo directo de FAR/hora.

---

## 7. El principio que gobierna el cierre (doc 57 §7.6)

> **El núcleo validable se cierra con las métricas que el material efectivamente cubra —
> la cobertura decide el conjunto final de métricas reportadas, no al revés.**

1. **Ninguna métrica bloquea el cierre.** La que no tenga material se reporta con su estado
   y su causa; jamás detiene la entrega ni se fabrica.
2. **La dirección es material → métrica.** Primero se releva qué se pudo grabar; recién
   entonces se fija qué entra al reporte y con qué n.
3. **La prioridad de adquisición se ordena por métricas desbloqueadas por unidad de esfuerzo.**
   Hoy: (a) tomas P2 largas, (b) footage soak. Un clip que no desbloquea nada nuevo no se prioriza.
4. **El reporte declara la cobertura como resultado, no como disculpa.**

---

## 8. Estado del material (lote de internet, 14 videos)

1080p/30fps, ~15.9 min totales, obra real, cámara fija, 0 cortes de escena verificados.

**Cubre:**
- ✅ **Soak / FAR-hora** — `6.1` de 6:10 min continuos. Era la métrica que estaba en cero.
- ✅ Negativos largos / precision — ~16 min agregados (objetivo ≥15 min, cumplido).
- ✅ 1 positivo real externo evaluable: **`4.1`** (19.1 s, onset en t≈6 s, evento ~11 s) →
  **primer clip del banco con TTFD real, no artefacto**. Es un caso *duro*, no un showcase:
  de noche esperamos recall alto y precision baja.
- ✅ Diversidad de escena: 10 diurnos + 4 nocturnos; fachada, excavación, estructura en altura,
  vial, demolición.

**No cubre (sale solo del rodaje propio):**
- ❌ Todos los positivos guionados P1–P9. **P2 es el crítico** — es el denominador más flaco.
- ❌ Banda de distancia cercana 5–10 m (todo el lote es cámara elevada).
- ❌ Confusables P9.

**Decisión asociada:** no sumar más cortos de 12 s por volumen. Para precision/FAR lo que
cuenta es el tiempo observado, y un clip de 12 s aporta 0.2 min pagando overhead fijo de
registro y verificación. Solo se agregan cortos que llenen un hueco de escena identificado.

**Pendiente:** registrar los 14 videos en `license_registry.md` y `download_log.md`.

---

## 9. Qué sigue

1. `prepare` + `derive` de `4.1` (primer TTFD real) y del soak `6.1`.
2. Licencias + consentimientos Ley 25.326 (**bloqueante legal antes de grabar**) y guion impreso.
3. Dry-run EBE el día previo (smoke live de 1 min).
4. Jornada de rodaje: ~15 escenas × 2 tomas + soak + las 3 corridas EBE live.
5. Post-rodaje: 2–3 tardes de anotación en CVAT. **La pasada humana reemplaza todo el GT
   preliminar actual**, incluido `cb_b01_p7`.
6. Experimentación C.1→C.4.

Spec 45 (MQTT) y EBE-desde-clip quedan después: no bloquean el cierre.
