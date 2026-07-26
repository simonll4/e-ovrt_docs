# 69 — Guion operativo del rodaje (documento de campo)

**Fecha:** 2026-07-25. **Para:** equipo de 3 personas, 2 cascos, 2 chalecos.
**Cómo se usa:** se lee de arriba hacia abajo, en orden, tachando casillas. No hace
falta abrir ningún otro documento durante la jornada.

> Este documento **reemplaza al doc 59 para el día del rodaje**. El 59 sigue siendo la
> referencia metodológica (por qué cada escena existe, cómo se derivan las duraciones);
> este es el que se lleva a la obra. Toda la plataforma que se menciona acá está
> **verificada de punta a punta el 2026-07-25**: red, dos cámaras, grabación, corrida
> live y alertas reales.

> ✅ **RODAJE EJECUTADO el 2026-07-25.** 35/35 tomas sanas, shot-list completo salvo
> P7-c (única no grabada), subset DVR ampliado a 9 tomas. Los checkboxes del §6 quedan
> tildados con el resultado de cada toma B. **El relevamiento crítico completo del día
> —material, corridas EBE, bugs arreglados, límites de realtime— es el doc 71.**
> El análisis de resultados realtime (GDINO vs YOLOE) está EN REVISIÓN por el usuario;
> las conclusiones de esa parte no están cerradas todavía.

---

## 1. Los tres roles (definir ANTES de empezar)

Son 3 personas y los roles **no rotan durante una escena**:

| Rol | Quién | Qué hace |
|---|---|---|
| **OPERADOR** | (definir) | Maneja la consola. **Nunca entra en cuadro.** Canta los estados en voz alta, llena la hoja de registro, verifica antes de desarmar. |
| **ACTOR A** | (definir) | El infractor principal en casi todas las escenas. |
| **ACTOR B** | (definir) | El cumplidor / segundo cuerpo en las escenas de 2 personas. En las escenas de 1 persona, **se aparta fuera de cuadro**. |

> **Regla dura: en cuadro hay 1 o 2 personas, nunca más, nunca de casualidad.**
> Antes de cada toma el OPERADOR dice **"cuadro limpio"** y confirma en el preview que
> no haya nadie de fondo. Una persona accidental en el fondo mete un sujeto sin GT y
> ensucia la escena para siempre: la toma hay que repetirla.

---

## 2. Inventario que hay que tener a mano

- [ ] **2 cascos**
- [ ] **2 chalecos reflectantes**
- [ ] Notebook + cargador, switch PoE, 2 cables de red
- [ ] OAK-D + su cable PoE
- [ ] (Opcional, para P9) **gorra común** y **campera naranja no reflectante**
- [ ] Cronómetro visible fuera de cuadro (o celular)
- [ ] **Consentimientos firmados** — antes de la primera toma, no después
- [ ] Esta guía impresa o en una segunda pantalla

**Con 2 cascos y 2 chalecos alcanza para todo el shot-list.** El punto más ajustado es
P5 y P7-a, que usan los 4 elementos a la vez. En ninguna escena hacen falta 3 juegos.

---

## 3. Arranque de la plataforma (una vez, al llegar — ~10 min)

### 3.1 Red — no hay nada que configurar

Las dos cámaras tienen **IP fija link-local**, elegida a propósito para que funcione sin
router y sin tocar la configuración de la notebook:

| Cámara | IP |
|---|---|
| OAK-D Pro PoE | **169.254.31.137** |
| DVR RTSP (EZVIZ) | **169.254.31.140** |

- [ ] Conectar: notebook → **switch PoE** → las dos cámaras
- [ ] Esperar unos segundos a que Windows le dé IP sola a la Ethernet (`169.254.x.x`)
- [ ] **Bajar las VPN** (NordVPN, WireGuard, ZeroTier) — pueden capturar rutas
- [ ] Verificar en la terminal:
      `ping 169.254.31.137` y `ping 169.254.31.140`

> **No hay que fijar IPs, ni apagar el Wi-Fi, ni usar permisos de administrador.**
> El Wi-Fi puede quedar prendido dando internet en paralelo.
> **Si un ping falla, reintentar** antes de tocar nada: la interfaz tarda en levantar y
> da falsos negativos.

### 3.2 Servicios — cada uno desde la raíz de SU repo

Tres terminales. **Si se lanzan desde otra carpeta, los artefactos se escriben en el
lugar equivocado** (ya pasó, y costó recuperar un run del banco).

- [ ] **Terminal 1 — media-plane**
      ```bash
      cd ~/projects/e-ovrt_media-plane
      EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve
      ```
- [ ] **Terminal 2 — control-plane**
      ```bash
      cd ~/projects/e-ovrt_control-plane
      .venv/bin/eovrt-control serve --port 8081
      ```
- [ ] **Terminal 3 — consola**
      ```bash
      cd ~/projects/e-ovrt_experimental-setup/webconsole/backend
      .venv/bin/uvicorn eovrt_webconsole.app:create_app --factory --port 8090
      ```

- [ ] Abrir **http://localhost:8090/** — entrar por la raíz `/`, los enlaces directos dan 404
- [ ] Verificar que el **preflight** de la consola esté en verde (si un plano está caído,
      el botón *Lanzar* aparece deshabilitado con el motivo a la vista)

### 3.3 Encuadre y prueba de humo

- [ ] En la ventana **Cámaras**, abrir el **preview** de la OAK-D y ajustar el encuadre
      — es la cámara principal de todo el shot-list (§6.0)
- [ ] **Dejar el DVR ya apuntado a la misma escena**, aunque no se use hasta el subset de
      comparación (§6.0). Verificar su encuadre con el preview **ahora**, no cuando haya
      que filmar contra reloj
- [ ] **Cerrar el preview** antes de grabar o correr — preview y run son excluyentes (da 409)
- [ ] Grabar **una toma de prueba de 30 s** y revisar el sidecar `.rec.json`:
      `resolution` 1920×1080, `truncated: false`
- [ ] **Borrar la toma de prueba** para que no se mezcle con el material real

> **Las dos cámaras no graban a la vez** (§6.0): grabación y corrida en vivo son
> secuenciales, y solo hay una grabación activa por vez. Encuadrar las dos ahora
> evita tener que reacomodar el set en el medio de la jornada.

> **Luz:** con poca luz la OAK-D alarga la exposición y el pipeline baja a ~1,6 fps
> (contra ~3,3 con buena luz). Las alertas igual salen, pero el margen se achica.
> **Si la escena está oscura, iluminarla antes que tocar cualquier umbral.**

---

## 4. Las 5 reglas de oro (si se rompen, la toma no sirve)

1. **Arrancar SIEMPRE en cumplimiento.** El actor entra con el EPP puesto y la
   infracción aparece a los **3–4 s**. Si entra ya en infracción, se pierde el arranque
   y la toma no se puede medir.
2. **Cola al final ≥ 3 s.** Después de corregir la infracción, seguir filmando en
   cumplimiento. Nunca cortar la cámara "justo".
3. **Grabar de más.** Aunque la escena dure 20 s, **cortar recién a los ~33 s**.
   El recorte fino se hace después, tranquilos.
4. **Cantar todo en voz alta.** El actor dice *"me saco el casco"* / *"casco puesto"*.
   Sirve para **sincronizar al equipo en el set** — que el OPERADOR sepa cuándo arranca
   y termina la infracción para anotarla, y que los actores no se desfasen.
   ⚠️ **El canto NO queda grabado.** Ver la nota de abajo.
5. **Cuadro limpio.** 1 o 2 personas, nadie más, nadie de fondo.

> **Las cámaras no graban audio — regla verificada el 2026-07-25 sobre 25 clips: los 25
> son video puro, sin pista de audio.** Ni la OAK-D ni el DVR RTSP capturan sonido.
>
> Por eso **el GT no se puede anotar desde el audio**: los segundos de inicio y fin de
> cada infracción salen **únicamente de la hoja de registro (§8) y de la inspección
> visual posterior**. Esto vuelve la hoja de registro **crítica, no opcional** — sobre
> todo en **P6** (4 momentos) y **P8** (2 episodios), que son las escenas con más
> transiciones que anotar.
>
> Si hace falta un ancla temporal visible, usar la **claqueta** (§10): una palmada
> visible a cámara al inicio de la toma.

**Seguridad, no negociable:** toda infracción se actúa **a nivel de piso**, lejos de
bordes, huecos y maquinaria. Nadie actúa una infracción real de altura ni cerca de
equipos. El EPP real está en escena para el estado cumplidor.

---

## 5. Cómo se hace cada escena

Cada escena se graba **dos veces, siempre en este orden**:

- **TOMA A (grabada)** → es el material que queda. Se puede re-analizar infinitas veces.
- **TOMA B (en vivo)** → mide cosas que solo existen en vivo y **no se pueden regenerar**.
  Por eso, si una toma B sale mal, **se repite en el momento**.

**Solo 3 escenas necesitan toma B: P1, P2 y P3.** Las demás son solo toma A.

### 5.1 TOMA A — grabada (todas las escenas)

- [ ] 1. OPERADOR: en la consola, ventana **Cámaras** → elegir escenario y variante →
      **Grabar**
- [ ] 2. **Nadie actúa hasta que el OPERADOR cante "GRABANDO"** — la OAK-D tarda ~9 s en
      conectar y el estado pasa por `starting`. Actuar antes es actuar para nadie.
- [ ] 3. Coreografía completa (ver §6), con los cantos
- [ ] 4. Cortar a los ~33 s
- [ ] 5. Revisar el sidecar: `resolution` correcta, `truncated: false`

### 5.2 TOMA B — en vivo (solo P1, P2, P3)

El orden **no es negociable**: primero el control-plane, después el media-plane. Al
revés se pierden los primeros eventos **sin que nada dé error**.

- [ ] 6. Lanzar desde **Experimentos → `Lanzar experimento`**, eligiendo el manifiesto
      de la escena (`ebe_p1_live`, `ebe_p2_live`, `ebe_p3_live`). Chequear que los dos
      chips digan **`media listo`** y **`control listo`**.

      > ⛔ **NO usar "Nueva corrida"** (pantalla Composición). Esa pantalla lanza
      > **solo el plano de medios**: su payload no lleva el campo `bus`, así que el
      > control-plane nunca recibe los eventos y **la toma sale sin ninguna alerta,
      > sin que nada dé error**. Verificado el 2026-07-25: costó dos pruebas antes de
      > detectarse (doc 70). Solo el camino de Experimentos dispara los dos planos en
      > el orden correcto (control primero, con `SubscriptionNotConfirmed` como guard).

      El `warmup_frames: 20` y el prompt set congelado **ya vienen en el manifiesto**
      — no hay campo que completar ni que recordar. El nombre de la corrida sale del
      slug, así que cada toma queda autoidentificada en los artefactos de ambos planos.
      Si hace falta una escena nueva: **`+ Nuevo experimento`** en el sidebar → basado
      en `ebe_oakd_live` → cambiar solo el nombre → **Crear** (no lanza; se lanza aparte).
- [ ] 7. **Nadie entra en escena hasta que el OPERADOR cante "PIPELINE VIVO"** — cuando
      las unidades procesadas pasan de 0 (tarda ~11 s). Actuar antes es actuar para nadie.
- [ ] 8. Misma coreografía que la toma A, mismos tiempos, mismos cantos
- [ ] 9. Cortar la corrida: pill `●` del sidebar → pantalla del run → **`■ Detener`**.
      Se corta **el media**; el control cierra solo, 1:1, al recibir `run_finished`.
      Esperar a que **los dos planos** queden en estado terminal (tarda ~2–6 s).
      **No intentar frenar el control por su lado** — la corrida live no es cancelable
      por API; si se mata primero, el media queda publicando al vacío.
- [ ] 10. **ANTES de desarmar la escena, verificar DOS cosas** (§7)

---

## 6. Shot-list — ordenado para cambiarse de ropa lo menos posible

Total: **~15 tomas A con la OAK-D + 3 tomas de comparación con el DVR + 3 tomas B**.
Calculá ~5 min por escena con su repetición.

### 6.0 Qué cámara usa cada toma — leer antes de empezar

**Restricción dura: las dos cámaras NO pueden grabar a la vez.** El sistema toma una
grabación por vez, y además **grabar y correr en vivo son secuenciales** (si se intenta,
la consola responde *"el media-plane está ocupado: grabar y correr son secuenciales"*).

> Consecuencia práctica: **una toma = una cámara**. Filmar una escena "con las dos" es
> filmarla **dos veces seguidas**, con dos actuaciones distintas. No son dos ángulos del
> mismo momento.

**La política del rodaje:**

| Qué | Cámara | Por qué |
|---|---|---|
| **Todo el shot-list (toma A)** | **OAK-D** | Es la que tiene el encuadre y el preview armados en §3.3. Una sola fuente para todo el material base. |
| **Subset de comparación: P1-a, P2-a, P5-a** | **DVR RTSP** | Se **re-filman esas 3 escenas** con el DVR. Cubre CR-01, CR-02 y el control de no-alerta en una segunda fuente. |
| **Las 3 tomas B (P1, P2, P3)** | **OAK-D** | Material **no regenerable**: las 3 con la misma cámara para que sean comparables entre sí, sin meter una variable extra. |

**Solo estas 3 escenas se filman con las dos cámaras: P1, P2 y P5.** Todas las demás
(P3, P4, P6, P7, P8, P9) van **solo con la OAK-D**. Las casillas del DVR están puestas
dentro de cada escena en el shot-list, marcadas con 📹.

**Cuándo se filma cada toma del DVR: inmediatamente después de las tomas OAK-D de esa
misma escena**, no al final de la jornada. El vestuario, la luz y el encuadre ya están
puestos, y no hay que cambiar nada de hardware — las dos cámaras están conectadas y
encuadradas desde §3.3, solo se elige el otro preset en la consola. Dejarlo para el final
obligaría a rearmar tres vestuarios distintos.

- [ ] Anotar **siempre la cámara** en la hoja de registro (§8).
- [ ] Al ID de toma del subset DVR, agregarle el sufijo: `P1-a-dvr`, `P2-a-dvr`,
      `P5-a-dvr`. Sin eso, después no se distinguen de las de la OAK-D.

> **Si el rodaje viene atrasado, el subset del DVR es lo primero que se recorta** — la
> decisión se toma **en el momento de cada escena**, salteando esa casilla 📹 y siguiendo.
> El shot-list completo con la OAK-D y las 3 tomas B tienen prioridad, porque el subset
> del DVR **se puede filmar otro día con el mismo guion**: justamente porque no depende
> de que sea la misma actuación, no se pierde nada al posponerlo.
>
> **Si sobra tiempo al final de la jornada**, ampliar el subset del DVR — P3-a y P7-a son
> los siguientes más valiosos.

#### 6.0.1 Por qué dos cámaras — y qué NO prueba el subset

Vale la pena tener esto claro **antes** de gastar 15–20 min de jornada en el subset, y
sobre todo antes de escribir conclusiones con ese material.

**Lo que el subset del DVR sí compra:**

1. **La respuesta a la pregunta de defensa más previsible.** *"¿Esto anda solo con tu
   cámara cara, o con las que ya hay en una obra?"* El DVR EZVIZ es hardware de vigilancia
   común. Tres clips donde CR-01 y CR-02 se confirman sobre un DVR comodity responden eso
   sin tener que argumentar nada. Es seguro barato.
2. **Las dos cámaras sostienen argumentos distintos, no el mismo.** Esta es la razón más
   fuerte:
   - La **OAK-D** sostiene la historia de **arquitectura EBE**: el prefiltro on-device
     (EN-2), el Nodo A edge, el descarte antes de la GPU. El DVR no puede mostrar nada de
     eso — es una cámara tonta que escupe RTSP.
   - El **DVR** sostiene la historia de **despliegue**: "la plataforma se acopla a lo que
     ya está instalado, no hace falta comprar hardware".

   Con una sola cámara, uno de los dos argumentos se queda sin material propio.
3. **Valor diagnóstico.** Si una escena falla en una cámara y anda en la otra, ya se sabe
   que el problema es de captura (fps, exposición, encuadre) y no del modelo ni del motor
   de patrones. Con una sola fuente, un fallo queda ambiguo.

**Lo que el subset del DVR NO prueba — importante al redactar:**

- **No es una comparación controlada de sensores.** Las dos tomas no son simultáneas:
  difieren en la cámara **y** en la actuación, la luz de ese minuto y el encuadre exacto.
  Si `P1-a` sale distinto de `P1-a-dvr`, **la diferencia no se le puede atribuir al
  sensor** — está confundida con todo lo demás.
- **No hay poder estadístico.** Con 3 escenas pareadas no se sostiene ninguna afirmación
  cuantitativa del tipo *"mAP 0.44 en OAK-D contra 0.39 en DVR"*.
- **No es equivalente a la estratificación del banco de imágenes.** En `bench_v3` los
  estratos son muestras independientes de la misma tarea; acá son dos actuaciones
  distintas. La analogía no aguanta el peso de una conclusión de robustez.

> **Cómo se puede escribir el resultado del subset, y hasta dónde:**
> ✅ *"La condición se confirmó también sobre una fuente RTSP comodity."*
> ❌ *"El sistema es robusto al sensor"* / *"la fuente A rinde mejor que la B"*.
>
> Es **evidencia de existencia**, no medición.

### BLOQUE 1 — Actor A solo, con chaleco, jugando con el casco

*Vestuario de base: **ACTOR A con casco + chaleco puestos**. **ACTOR B fuera de cuadro**
en las 4 escenas de este bloque (se aparta, no pasa por el fondo). El **chaleco queda
puesto todo el clip** — la única variable es el casco, o su confusable en P9.*

#### P1 — Sin casco (la escena principal) — **3 tomas + 1 toma B**

- [x] **P1-a** — plano medio, buena luz — *OAK-D*
- [x] **P1-b** — más lejos, o con luz peor — *OAK-D*
- [x] **P1-c** — pasando por detrás de algo durante el evento (oclusión parcial) — *OAK-D*
- [x] **`P1-a-dvr`** — 📹 **repetir P1-a con el DVR**, misma coreografía y mismo vestuario
      (subset de comparación, §6.0 / §6.0.1) — *grabada como `P1-a-take5` (sufijo `-dvr`
      NO usado: la cámara se distingue por el sidecar; además hay DVR extra de P1-b y
      P1-c ×2, ver doc 71 §1)*
- [x] **P1 — TOMA B en vivo** (sobre P1-a) — *OAK-D* — **✓ CR-01 confirmó en las 4
      corridas del día (deltas 4.1–4.3 s sobre umbral 4.0). Detalle: doc 71 §2.2.**

**Qué hace ACTOR A, segundo a segundo** (ACTOR B: fuera de cuadro todo el clip):

| t | ACTOR A |
|---|---|
| 0–3 s | Entra en cuadro **con casco y chaleco puestos**. Camina, trabaja, se mueve normal. |
| 3 s | Canta **"ME SACO EL CASCO"** y se lo saca. Lo deja en la mano o lo apoya — que se vea claro que **no está en la cabeza**. |
| 3–17 s | **Sostiene 14 s sin casco**, chaleco puesto. Camina, trabaja, se mueve. **No se tapa la cabeza con las manos ni con un objeto** (salvo en P1-c, ver abajo). |
| 17 s | Canta **"CASCO PUESTO"** y se lo pone. |
| 17–20 s | Sigue **3 s más en cuadro** con el casco puesto (la cola de la regla 2). |
| 20–33 s | Sigue trabajando normal. **No cortar todavía** — se graba de más (regla 3). |
| ~33 s | El OPERADOR corta. |

> **En vivo debe alertar CR-01 a los ~4 s del onset** (o sea, alrededor del segundo 7
> del clip: 3 s de entrada + 4 s de confirmación).
>
> **P1-c — la oclusión parcial, cómo se ejecuta:** todo igual que arriba, pero **durante
> el hold sin casco** (entre los 3 y los 17 s) ACTOR A camina detrás de un objeto que ya
> esté en el encuadre —mesa alta, caño, estantería, el marco de una puerta— de modo que
> le tape el cuerpo o la cabeza durante **2–4 s**, y sigue caminando hasta quedar visible
> de nuevo. **No se saca ni se pone nada mientras está tapado.**
>
> **ACTOR A no sale del plano general de cámara en ningún momento.** Eso es exactamente
> lo que separa esta toma de P8: acá el detector tiene que **recuperar el tracking**
> después de una oclusión breve; si el actor desaparece del cuadro entero, esa señal no
> se mide y la toma se convierte en una copia de P8.
>
> Antes de rodar P1-c: elegir el objeto y **caminar el recorrido una vez sin cámara**,
> para confirmar dónde tapa y cuántos segundos dura.

#### P3 — Transitorio corto, NO debe alertar — **1 toma + 1 toma B**

- [x] **P3-a**
- [x] **P3 — TOMA B en vivo** — **✓ silencio correcto: el candidato CR-01 del
      transitorio de 2 s nunca confirmó (f309→f412, resolved). 2/2 en el día
      (también con YOLOE). Detalle: doc 71 §2.2–2.3.**

**Qué hace ACTOR A** (ACTOR B: fuera de cuadro todo el clip):

| t | ACTOR A |
|---|---|
| 0–3 s | Entra en cuadro **con casco y chaleco puestos**, trabajando normal. |
| 3 s | Canta **"ME SACO EL CASCO"** y se lo saca. |
| 3–5 s | **Solo 2 s sin casco.** Este es el corazón de la escena: **cronometrar**, no estimar a ojo. |
| 5 s | Canta **"CASCO PUESTO"** y se lo pone. |
| 5–14 s | Sigue **9 s en cuadro** con casco, trabajando normal. |
| ~20 s | El OPERADOR corta. |

> **En vivo NO debe alertar. Esa es toda la gracia de la escena**: 2 s de infracción
> están por debajo de los 4 s que CR-01 necesita para confirmar.
> Si alertó igual → **anotarlo como hallazgo y NO repetir**: es un dato real (§7).

#### P4 — Se resuelve y sigue en cuadro — **1 toma**

- [x] **P4-a**

**Qué hace ACTOR A** (ACTOR B: fuera de cuadro todo el clip):

| t | ACTOR A |
|---|---|
| 0–3 s | Entra **con casco y chaleco puestos**, trabajando normal. |
| 3 s | Canta **"ME SACO EL CASCO"** y se lo saca. |
| 3–17 s | Sostiene **14 s sin casco**, chaleco puesto (igual que P1). |
| 17 s | Canta **"CASCO PUESTO"** y se lo pone. |
| 17–27 s | **Se queda 10 s más en cuadro**, trabajando normal, con el casco puesto. **Acá está la diferencia con P1** (que solo tiene 3 s de cola): se mide que la alerta cierre y que la persona se siga siguiendo en estado cumplidor. |
| ~30 s | El OPERADOR corta. |

#### P9 — Confusables — **1–2 tomas**

- [x] **P9-a** — con **gorra** en vez de casco (y/o campera naranja en vez de chaleco)
- [x] **P9-b** — con el **casco en la mano** o colgado, no puesto

**Qué hace ACTOR A** (ACTOR B: fuera de cuadro todo el clip):

| t | ACTOR A |
|---|---|
| 0 s | Entra en cuadro **ya con el confusable puesto** (ver variantes abajo). |
| 0–12 s | Trabaja normal, quieto o caminando, **≥12 s en cuadro**. **No se saca ni se pone nada — el clip es un solo estado, sin transición.** |
| ~20 s | El OPERADOR corta. |

- **P9-a** — ACTOR A entra con **gorra común** en la cabeza (no casco) + chaleco puesto.
  Si además hay campera naranja no reflectante, puede usarla **en vez del chaleco**
  (esa campera lo reemplaza por todo el clip).
- **P9-b** — ACTOR A entra con el **casco en la mano, colgado del brazo o del cinturón**
  — bien visible en cuadro, pero **no puesto en la cabeza** — y el **chaleco real puesto**.

> **P9 es la única escena que arranca ya en infracción** — es la excepción consciente a
> la regla 1, porque acá no hay transición que medir: se mide si el modelo confunde el
> confusable con EPP real.
> Si no hay gorra ni campera naranja disponible, **hacer solo P9-b**.

### BLOQUE 2 — Actor A solo, con casco, jugando con el chaleco

*Vestuario de base: **ACTOR A con casco + chaleco puestos**. **ACTOR B fuera de cuadro**.
El **casco queda puesto todo el clip** — la única variable es el chaleco.*

#### P2 — Sin chaleco — **3 tomas + 1 toma B**

- [x] **P2-a** — plano medio, buena luz — *OAK-D*
- [x] **P2-b** — más lejos o luz peor — *OAK-D*
- [x] **P2-c** — con oclusión parcial — *OAK-D*
- [x] **`P2-a-dvr`** — 📹 **repetir P2-a con el DVR**, misma coreografía y mismo vestuario
      (subset de comparación, §6.0 / §6.0.1) — *grabada como `P2-a-take2` (cámara en el
      sidecar, sin sufijo)*
- [x] **P2 — TOMA B en vivo** (sobre P2-a) — *OAK-D* — **✗ ejecutada 2 veces, SIN alerta
      CR-02: F-RT1 (sobre-marca `vest` 0.25–0.5 sobre el torso descubierto) abortó los
      episodios a ~4.5 s de los 7 requeridos. Anotado como resultado del modelo, NO se
      repite (regla del §7 aplicada al revés: acá el dato es la supresión). La única
      CR-02 live legítima del día fue la de las 15:47 con el chaleco fuera de cuadro.
      Detalle: doc 71 §2.2 y doc 70.**

**Qué hace ACTOR A, segundo a segundo** (ACTOR B: fuera de cuadro todo el clip):

| t | ACTOR A |
|---|---|
| 0–4 s | Entra en cuadro **con casco y chaleco puestos**, trabajando normal. |
| 4 s | Canta **"ME SACO EL CHALECO"** y se lo saca. **Lo deja FUERA de cuadro** — no colgado del brazo, no apoyado a la vista, no en una silla que se vea. Ver la advertencia de abajo. |
| 4–26 s | **Sostiene 22 s sin chaleco**, casco puesto. Camina, trabaja, se mueve. |
| 26 s | Canta **"CHALECO PUESTO"** y se lo pone. |
| 26–30 s | Sigue **4 s más en cuadro** con el chaleco puesto (cola). |
| 30–35 s | Sigue trabajando normal. **No cortar todavía.** |
| ~35 s | El OPERADOR corta. |

> **En vivo debe alertar CR-02 a los ~7 s del onset** (o sea, alrededor del segundo 11
> del clip: 4 s de entrada + 7 s de confirmación).
>
> **P2-c — la oclusión parcial, cómo se ejecuta:** misma lógica que P1-c. Durante el
> hold sin chaleco (entre los 4 y los 26 s), ACTOR A pasa **2–4 s** detrás de un objeto
> ya presente en el encuadre y vuelve a quedar visible, **sin salir del plano general de
> cámara** y sin sacarse ni ponerse nada mientras está tapado. No confundir con una
> salida de cuadro: eso es P8.
>
> ⚠️ **Si P2 no alerta en vivo, mirar el vestuario ANTES que el software.** El modelo
> **sobre-marca "chaleco"**: cualquier prenda con franjas reflectantes o color
> fluorescente que quede en cuadro —incluido **el chaleco que el actor se acaba de
> sacar**— puede hacerle creer que el chaleco sigue puesto. Sacar esa prenda del cuadro
> y **repetir la toma B ahí mismo**.

### BLOQUE 3 — Actor A solo, las dos infracciones y la salida de cuadro

*Vestuario de base: **ACTOR A con casco + chaleco puestos**. **ACTOR B fuera de cuadro**.
En P6 se saca los dos elementos; en P8 solo el casco.*

#### P6 — Las dos infracciones a la vez — **1 toma**

- [x] **P6-a**

**Qué hace ACTOR A, segundo a segundo** (ACTOR B: fuera de cuadro todo el clip):

| t | ACTOR A |
|---|---|
| 0–4 s | Entra en cuadro **con casco y chaleco puestos**, trabajando normal. |
| 4 s | Canta **"ME SACO EL CASCO"** y se lo saca. ← **momento 1** |
| 7 s | **3 s después**, canta **"ME SACO EL CHALECO"** y se lo saca. Lo deja **fuera de cuadro** (misma trampa que P2). ← **momento 2** |
| 7–24 s | **Sostiene las dos infracciones ~17 s** (mínimo 15 s: CR-02 necesita 7 s para confirmar y hay que dejar holgura). Camina, trabaja. |
| 24 s | Canta **"CHALECO PUESTO"** y se lo pone. ← **momento 3** |
| 27 s | Canta **"CASCO PUESTO"** y se lo pone. ← **momento 4** |
| 27–31 s | Sigue **4 s más en cuadro** con todo puesto (cola). |
| ~35 s | El OPERADOR corta. |

> **Anotar los 4 momentos** en la hoja de registro: 2 de inicio y 2 de fin.
> Las infracciones **se escalonan a propósito** (3 s de diferencia al salir, 3 s al
> volver): así se puede ver si el sistema las distingue como dos condiciones separadas
> en vez de una sola.

#### P8 — Sale y vuelve a entrar — **1 toma**

- [x] **P8-a**

**Qué hace ACTOR A, segundo a segundo** (ACTOR B: fuera de cuadro todo el clip):

| t | ACTOR A |
|---|---|
| 0–3 s | Entra en cuadro **con casco y chaleco puestos**, trabajando normal. |
| 3 s | Canta **"ME SACO EL CASCO"** y se lo saca. **← empieza el episodio 1** |
| 3–11 s | **8 s en cuadro sin casco**, chaleco puesto. |
| 11 s | Canta **"SALGO DE CUADRO"** y **sale del encuadre por completo** — no queda ni un brazo, ni una pierna, ni una sombra suya en el plano. |
| 11–16 s | **≥5 s fuera de cuadro.** **No se pone el casco afuera** — vuelve igual que salió. El cuadro queda vacío. |
| 16 s | Canta **"VUELVO"** y entra de nuevo, **todavía sin casco**. **← empieza el episodio 2** |
| 16–24 s | **8 s más en cuadro sin casco.** |
| 24 s | Canta **"CASCO PUESTO"** y se lo pone. |
| 24–27 s | Sigue **3 s más en cuadro** (cola). |
| ~35 s | El OPERADOR corta. |

> **El chaleco queda puesto todo el clip** — la única variable es el casco.
>
> **Son dos episodios distintos: anotarlos por separado** en la hoja de registro (dos
> pares de inicio/fin, no uno solo). Lo que se mide es si el sistema los separa en dos
> o los pega en uno.
>
> **No confundir P8 con la oclusión de P1-c / P2-c.** Son dos señales distintas y
> ninguna reemplaza a la otra:
>
> | | P8 | P1-c / P2-c |
> |---|---|---|
> | Qué hace el actor | **Sale del plano por completo** ≥5 s | Queda tapado por un objeto 2–4 s, **sin salir del plano** |
> | Qué se mide | Segmentación en dos episodios | Recuperación del tracking tras oclusión |

### BLOQUE 4 — Los dos actores en cuadro

*Vestuario de base: **los 4 elementos en uso** — ACTOR A con casco + chaleco, ACTOR B con
casco + chaleco. Acá **los dos están en cuadro**. El **chaleco queda puesto en ambos todo
el clip** en las 4 tomas del bloque — lo único que varía es **quién se saca el casco**.*

#### P5 — Todo en regla (el clip de "no alerta") — **1 toma**

- [x] **P5-a** — *OAK-D*
- [x] **`P5-a-dvr`** — 📹 **repetir P5-a con el DVR**, mismo vestuario (subset de
      comparación, §6.0 / §6.0.1)

**Qué hacen los dos actores:**

| t | ACTOR A | ACTOR B |
|---|---|---|
| 0–20 s | Entra **con casco y chaleco puestos**. Trabaja normal junto a ACTOR B: caminar, mover cosas, señalar, conversar. | Entra **con casco y chaleco puestos**. Trabaja normal junto a ACTOR A. |
| | **No se saca nada. No canta nada** — no hay transición que anotar. | **No se saca nada. No canta nada.** |
| ~30 s | El OPERADOR corta (la acción son 15–20 s, pero se graba de más). | |

> Este es el clip de control: **no debe alertar nunca, en ningún momento**.
> Si alerta, es un falso positivo y vale como hallazgo — anotarlo, no repetir la toma.

#### P7 — Dos personas, una infringe — **2–3 tomas**

- [x] **P7-a** — ACTOR B cumple todo el clip; ACTOR A hace la coreografía de P1
- [x] **P7-b** — los dos **se cruzan entre sí y frente a cámara** (~10 s de cruces)
      mientras ACTOR A sostiene la infracción ≥8 s
- [ ] **P7-c** — igual que P7-a pero **cambiando quién infringe**: ahora ACTOR B se
      saca el casco y ACTOR A cumple — **NO GRABADA (2026-07-25): única toma del
      shot-list que quedó afuera. Era la opcional de menor prioridad del bloque;
      P7-a/P7-b la cubren parcialmente. Si se re-arma la escena, es la primera
      candidata.**

**P7-a — ACTOR A infringe, ACTOR B cumple:**

| t | ACTOR A (infractor) | ACTOR B (cumplidor) |
|---|---|---|
| 0–3 s | Entra **con casco y chaleco puestos**, trabajando normal. | Entra **con casco y chaleco puestos**. |
| 3 s | Canta **"ME SACO EL CASCO"** y se lo saca. | Sigue trabajando normal, **sin tocarse el EPP**. |
| 3–17 s | **Sostiene 14 s sin casco**, chaleco puesto. Trabaja, camina. | **Permanece en cuadro con casco y chaleco puestos todo el clip.** Trabaja normal cerca de ACTOR A. |
| 17 s | Canta **"CASCO PUESTO"** y se lo pone. | Sigue igual. |
| 17–20 s | 3 s de cola con todo puesto. | Sigue igual. |
| ~35 s | El OPERADOR corta. | |

> Lo que se mide: que el sistema **le atribuya la infracción a la persona correcta** y no
> alerte por ACTOR B, que cumple todo el tiempo.

**P7-b — igual que P7-a, pero con cruces:**

Misma coreografía que P7-a, con un agregado: durante el hold sin casco (los 14 s), los
dos actores **se cruzan entre sí y pasan frente a cámara** durante ~10 s — se tapan
mutuamente, se pasan por delante y por detrás, intercambian posiciones.

- **Los cruces tienen que pasar DURANTE la infracción, no antes ni después.**
- ACTOR A tiene que sostener la infracción **≥8 s** mientras ocurren los cruces.
- ACTOR B **nunca se saca nada**: cruza con casco y chaleco puestos.

> Lo que se mide: que el sistema no **intercambie las identidades** cuando los cuerpos se
> tapan entre sí — es decir, que la infracción no "salte" de ACTOR A a ACTOR B en un cruce.

**P7-c — los roles al revés:**

Idéntica a P7-a, pero **cambia quién infringe**:

| t | ACTOR A (ahora cumple) | ACTOR B (ahora infringe) |
|---|---|---|
| 0–3 s | Entra **con casco y chaleco puestos**. | Entra **con casco y chaleco puestos**. |
| 3 s | Sigue trabajando normal, **sin tocarse el EPP**. | Canta **"ME SACO EL CASCO"** y se lo saca. |
| 3–17 s | **Permanece en cuadro con casco y chaleco puestos todo el clip.** | **Sostiene 14 s sin casco**, chaleco puesto. |
| 17 s | Sigue igual. | Canta **"CASCO PUESTO"** y se lo pone. |
| 17–20 s | Sigue igual. | 3 s de cola con todo puesto. |
| ~35 s | El OPERADOR corta. | |

> Lo que se mide: lo mismo que P7-a, pero descartando que el resultado dependa de **cuál
> de los dos cuerpos** es el infractor (ropa, altura, posición en el cuadro).

---

## 7. Antes de desarmar cada escena live — DOS verificaciones

No es una, son **dos**. Si falta cualquiera, la toma B se repite ahora.

- [ ] **`bus_dropped_events = 0`** en el estado del control-plane
- [ ] **La alerta esperada se emitió**:

| Escena | Qué tiene que pasar |
|---|---|
| **P1** | alerta **CR-01** a ~4 s del onset |
| **P2** | alerta **CR-02** a ~7 s del onset |
| **P3** | **ninguna alerta** |

> **Dónde mirarlo:** `/experiments/<experiment_id>`, card **Alertas**. ⚠️ Esa vista
> **carga los datos una sola vez al montar y no se refresca** — el polling solo mueve
> el badge de estado. Si la abriste antes de que terminara, vas a ver "Sin alertas."
> aunque hayan saltado: **recargar la página** una vez que ambos planos estén terminales.
> El `bus_dropped_events` sale del summary del control-plane.

> Si P2 no alertó → revisar franjas o colores fluorescentes en cuadro → repetir la toma B.
> **Sospechoso nuevo (F-RT1, doc 70): la ropa oscura lisa también se marca como "chaleco"**
> (mediana ~0.5, picos de 0.89) — usar remera lisa sin estampa grande y el chaleco
> literalmente fuera del encuadre.
> Si P3 alertó → anotarlo como hallazgo, **no repetir**: es un dato real.

---

## 8. Hoja de registro (una por toma)

| Campo | Valor |
|---|---|
| ID de toma (ej. `P1-a-take1`; subset DVR: `P1-a-dvr`) | |
| Hora | |
| **Cámara** (OAK-D / DVR) — **nunca dejarlo vacío** (§6.0) | |
| Segundo en que empieza la infracción | |
| Segundo en que termina | |
| (P6/P8: los 4 momentos / los 2 episodios) | |
| Variación (distancia / luz / oclusión) | |
| **Solo toma B:** `media_run_id` | |
| **Solo toma B:** `control_run_id` | |
| **Solo toma B:** ¿alertó cuando debía? | |
| Incidencias / ¿hay que repetirla? | |

> **No borrar la carpeta `runs/`.** Todo lo que queda grabado ahí se vuelve a analizar
> después; es la evidencia.

---

## 9. Si algo falla — soluciones rápidas

| Síntoma | Qué hacer |
|---|---|
| **"ya hay una grabación activa"** y no deja grabar | Apretar **Detener** en la consola. Si quedó un archivo de 0 bytes, borrarlo antes de repetir. |
| **La grabación falla con un mensaje raro** que menciona `DeprecationWarning` | Ese mensaje **no dice la causa real**. Casi siempre es la **cámara desconectada o sin PoE**: revisar cable y `ping 169.254.31.137`. |
| **La cámara no responde al ping** | Reintentar 2–3 veces antes de tocar nada. Verificar que el switch PoE tenga corriente y que el LED del puerto esté encendido. |
| **El DVR "perdió" su IP** | Tiene **Wi-Fi y Ethernet con configuración separada**. La IP que importa es la de **Ethernet** (`169.254.31.140`); si se edita la otra pantalla, parece que revirtió pero no. |
| **El control-plane dice 409 al lanzar** | Ya hay una corrida abierta: **reusarla**, no borrarla. Disparar solo el media-plane contra esa. |
| **La corrida live quedó colgada y no arranca otra** | No se puede cancelar por API. O se reusa (fila anterior), o se espera **5 minutos** a que cierre sola, o se reinicia el control-plane. **En rodaje: reusar.** |
| **El botón Lanzar está deshabilitado** | Un plano está caído. El motivo aparece en pantalla: levantar ese servicio y recargar. |
| **Cambié algo y la consola no lo muestra** | `Ctrl+Shift+R` en el navegador. |
| **Windows ve la cámara pero la consola no** | `wsl --shutdown` en PowerShell, reabrir la terminal y **volver a levantar los tres servicios**. |
| **El video sale con menos de 1280 de ancho** | El preset está apuntando al substream del DVR. Avisar y seguir con la OAK-D. |

---

## 10. Cierre de la jornada — antes de que se vaya nadie

- [ ] **3 P1**, **3 P2**, 1 P3, 1 P4, 1 P6, 1 P8, 2–3 P7, 1 P5, 1–2 P9 — todas con la **OAK-D**
- [ ] **Subset de comparación con el DVR**: `P1-a-dvr`, `P2-a-dvr`, `P5-a-dvr` (§6.0).
      **Es lo primero que se recorta si falta tiempo** (se puede filmar otro día con el
      mismo guion), y lo primero que se amplía si sobra. Qué prueba y qué no: §6.0.1.
- [ ] **Las 3 tomas B** (P1, P2, P3) con `bus_dropped_events = 0` y sus IDs anotados
- [ ] **Toda toma tiene anotada la cámara** con la que se filmó — sin eso no se pueden
      reportar los resultados por fuente
- [ ] Toda toma tiene su hoja de registro con los segundos anotados
- [ ] **Ninguna toma arranca ya en infracción** (regla 1)
- [ ] **Todas tienen cola al final** (regla 2)
- [ ] Revisar que ninguna toma tenga gente de más en el fondo
- [ ] **Copia de seguridad del material crudo antes de salir de la locación**
- [ ] Recién ahí, liberar a los actores

### Opcional si sobra tiempo y ganas

- [ ] **Soak**: 5–10 min de cámara fija sobre actividad normal en cumplimiento
- [ ] **Claqueta**: una escena con una palmada visible a cámara, anotando la hora exacta
- [ ] **V1 de la defensa**: la toma más vistosa de la cadena infracción → alerta

---

## 11. Datos de referencia (por si hay que confirmar algo)

| | |
|---|---|
| Modelo | `grounding-dino/gdino-tiny-560` |
| Prompt set | `cr01_cr02_v2_short` (congelado) |
| Pattern set | `cr01_cr02_v2` — **nunca el v1** |
| Consola | http://localhost:8090/ |
| Servicios | media `:8080`, control `:8081`, consola `:8090` |
| OAK-D | `169.254.31.137` — conecta en ~9 s, primer frame a ~11 s |
| DVR RTSP | `169.254.31.140` — 1920×1080, ~18 fps |
| Videos grabados | `e-ovrt_datasets/datasets-videos/raw/` |
| Corridas live | `e-ovrt_media-plane/runs/` y `e-ovrt_control-plane/runs/` |
| CR-01 (sin casco) | confirma a los **4 s** |
| CR-02 (sin chaleco) | confirma a los **7 s** |
