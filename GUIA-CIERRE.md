# Guía de cierre — tu checklist hasta la defensa

Documento vivo, **sin número** (no forma parte de la serie `operacion/NN-`), pensado para
que lo abras, vayas tachando, y cada ítem te mande al documento con el detalle completo para
ejecutarlo. Última actualización: 2026-07-23.

**Cómo usarlo:** marcá `[x]` a medida que cerrás cada punto. El orden de la lista es el orden
recomendado (hay dependencias reales entre algunos ítems, marcadas donde corresponde). Si en
algún momento perdés el hilo de todo el proyecto, `docs/00-indice.md` es el índice completo y
`docs/operacion/62-plan-maestro-experimentos.md` es el plan metodológico entero.

---

## Ya está todo cerrado (nada que hacer acá)

No hace falta tocar nada de esto — está verificado (auditoría de cierre 2026-07-23), pero si
querés el detalle de cómo se llegó, cada ítem linkea a su doc:

- ✅ **Modelo elegido**: `grounding-dino/gdino-tiny-560`, con criterio pre-registrado y
  confirmado en 2 benchs independientes → `docs/operacion/64-resultados-s1-s2-seleccion-modelos.md`
- ✅ **Bench de imágenes ampliado y congelado**: 6.477 imgs, 3 fuentes → `docs/operacion/66-plan-ampliacion-bench-imagenes.md`
- ✅ **Config del rodaje y del carril live**: prompts congelados, pattern set correcto → `docs/operacion/59-guion-grabacion-bloque-a.md` §9
- ✅ **EBE (corrida live) probada de punta a punta** con el modelo elegido → `docs/operacion/65-l0-ensayo-ebe-tramo1.md`
- ✅ **Plataforma de medición completa** (persistencia, métricas, matching, FAR) → `docs/operacion/62-plan-maestro-experimentos.md` §1-2
- ✅ **Ensayo con cámaras (G2)**: circuito completo probado con la OAK-D real —
  toma A (consola→clip) OK, toma B (live 1:1) con alerta CR-01 real y
  `bus_dropped_events: 0`, claqueta anclada a 222 ms tras corregir la regla del `starting`,
  tiempos de setup medidos (~15 s overhead mecánico/toma live) → `docs/operacion/67-preparacion-rodaje-y-ebe.md` sección G2

---

## Lo que falta — en orden

### 1. [ ] Pasada humana en CVAT — los 14 videos de internet

**Qué es:** corregir el GT preliminar de los videos que ya tenemos descargados. Esto
**desbloquea la Fase T sola**, sin esperar al rodaje — es lo más barato que podés hacer para
destrabar evaluación real.

**Detalle completo (paso a paso, con comandos):**
`docs/operacion/55-como-continuar.md`, **PASO 1** (probar CVAT con el clip que ya está, medio
día) y **PASO 2** (reemplazar el GT preliminar por el tuyo).
Guía técnica de la herramienta: `e-ovrt_datasets/datasets-videos/GUIA-CVAT.md` (cómo levantar
CVAT con Docker, protocolo de corrección) y el complemento conceptual
`e-ovrt_datasets/datasets-videos/docs/etiquetado-cvat.md` (qué significa cada track/atributo).

---

### 2. [ ] Consentimientos + coordinar colegas + EPP físico

**Qué es:** lo administrativo del rodaje — consentimientos firmados **antes** de grabar (no
después), coordinar quién actúa, y tener casco/chaleco reales disponibles para las tomas
"cumplidoras".

**Detalle completo:** `docs/operacion/59-guion-grabacion-bloque-a.md` (el guion entero da el
contexto de qué se graba y por qué).

---

### 3. [ ] Ejecutar el rodaje (día completo, con tus colegas)

**Qué es:** la jornada de grabación en sí — el shot-list completo (P1 a P9), con la config ya
cerrada y las corridas EBE live embebidas.

**Detalle completo — 2 documentos, en este orden:**
1. `docs/operacion/59-guion-grabacion-bloque-a.md` — el guion completo: reglas de oro, las
   plantillas de timeline, escena por escena, hoja de registro por toma, checklist de cierre
   de sesión, y **§9** con las reglas nuevas (regla del `starting`, cantar el evento,
   seguridad de escena).
2. `docs/operacion/67-preparacion-rodaje-y-ebe.md`, sección **G5** — el checklist operativo
   del día (disco, orden de arranque de los servicios, orden EBE, verificaciones por escena).

> Depende de 1 y 2 de esta lista.

---

### 4. [ ] Acta `edir_v1`

**Qué es:** congelar el prompt set `edir_v1` (formulaciones de ausencia directa para CR-01 y
CR-02) para poder correr la comparación E-DIR vs E-IND (Fase D del plan). No bloquea nada
más — las Fases T y P corren sin esto.

**Detalle completo:** `docs/nucleo/04-diseno-comparativo-estrategias-edir-eind.md`, secciones
§8 (criterios de decisión) y §9 (trabajo mínimo para habilitar la comparación).

---

### 5. [ ] GT en CVAT del material del rodaje (después de grabar)

**Qué es:** la misma tarea que el punto 1, pero sobre las tomas del rodaje propio en vez de
los videos de internet. Con equipo de 3, doble anotación en una porción para medir acuerdo.

**Detalle completo:** `docs/operacion/58-plan-cierre-implementacion-experimentacion.md` §B.3.

---

## Después de esto, lo hago yo (sin que haga falta que intervengas)

Con el punto 1 (CVAT internet) ya alcanza para arrancar la Fase T. El resto de la cadena:

**T** (banco temporal) → **P** (validación de la plataforma) → **D** (E-DIR vs E-IND, si ya
está el punto 4) → análisis de errores → reporte de cierre.

Metodología completa de estas fases: `docs/operacion/62-plan-maestro-experimentos.md` §4-8.
Estado y deuda de implementación pendiente (no bloquea nada, la voy tomando en tiempo
libre): mismo doc, §9.

---

## Mapa rápido si te perdiste

| Necesitás | Doc |
|---|---|
| El panorama completo del proyecto de tesis | `docs/operacion/62-plan-maestro-experimentos.md` |
| Por qué elegimos este modelo | `docs/operacion/64-resultados-s1-s2-seleccion-modelos.md` |
| Cómo quedó armado el bench de imágenes | `docs/operacion/66-plan-ampliacion-bench-imagenes.md` |
| Ejecutar el rodaje paso a paso | `docs/operacion/59-guion-grabacion-bloque-a.md` |
| Checklist operativo del día (disco, servicios, EBE) | `docs/operacion/67-preparacion-rodaje-y-ebe.md` |
| Usar CVAT (herramienta y protocolo) | `e-ovrt_datasets/datasets-videos/GUIA-CVAT.md` |
| Cualquier otra cosa / índice completo | `docs/00-indice.md` |
