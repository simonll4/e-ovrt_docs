# Etapa 3 — ajustes al diseño arquitectónico (§17.3)

> **Estado (2026-08-10):** es el **único frente con hoja de trabajo formal y casillas de
> decisión**. Las 26 redlines viven en `material-etapa-3/93-redlines-etapa3.md` (v2,
> 2026-07-12) y **ninguna está aplicada al `.docx`**: las casillas `[ ]` del tablero
> siguen vacías.
>
> **Este documento no reemplaza al 93 ni lo resume "por si acaso": lo enruta.** La ficha
> de cada redline —qué dice hoy, qué debe decir, por qué— está en el 93 y solo ahí. Acá
> está el mapa, el estado y las tres cosas que hay que saber antes de abrirlo.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/90-etapa3-texto-extraido.md` (§17.3.1–§17.3.18) y el `.docx` de Etapa 3 |
| **Las 26 redlines** | **`material-etapa-3/93-redlines-etapa3.md`** ← la hoja de trabajo |
| Texto largo ya redactado | `material-etapa-3/94-secciones-nuevas-etapa3.md` (§1–§9, cubre 9 redlines) |
| El análisis que las originó | `material-etapa-3/91-relevamiento-etapa3-vs-implementacion.md` |
| Material verificado contra código | `material-etapa-3/92-anexo-concrecion-tecnica.md` |
| §17.3.10 (distribución de alertas) | `material-etapa-3/92b-concrecion-distribucion-alertas.md` |

---

## 1. Lo que hay que saber antes de abrir el 93

**Son 26, no 24.** `R-25` y `R-26` se agregaron en la v2 del 2026-07-12, tras auditoría
adversarial. **`R-26` es, según la propia auditoría, "la más valiosa" de todas**
(extensibilidad medida: cuánto cuesta agregar una condición nueva). Un pase que se
detenga en R-24 se pierde justo la mejor.

**La remisión de cifras del 93 está derogada.** El 93 dice "todas las cifras remiten a
la tabla canónica del doc 92 §10". Ese `informe/92` §10 **quedó derogado como fuente de
números el 2026-08-05**. Al transcribir cualquier redline, **las cifras se toman de los
cuatro índices de `e-ovrt_experimental-setup/results/`** (verificables con
`operacion/datos/96-verificar-indices.py`). El 93 ya lleva el banner de esta corrección.

**Numeración de tablas nuevas.** El capítulo cierra en la **Tabla 60**; las tablas nuevas
del doc 94 están numeradas **61 a 67**. Al transcribir hay que verificar que no colisionen
con las que se agreguen en el camino.

---

## 2. El tablero, con lo que cambió desde que se escribió

Prioridad y sección salen del tablero del 93; la última columna es el estado a hoy.

| # | § | Tipo | Pri | Título | Texto listo | Novedad desde 2026-07-12 |
|---|---|---|---|---|---|---|
| R-01 | 17.3.9.2 | CONTRADICE | 🔴 | La estrategia del núcleo es E-IND, no la directa | — | reforzada: E-DIR quedó vetada por precisión (AF-2) |
| R-02 | Tabla 44 | CONTRADICE | 🔴 | El `cooldown` no es parámetro de patrón | — | **atendida por `92b`**, que fija la frontera (ADR-011) |
| R-03 | Tabla 44 / 17.3.6.2 | CONTRADICE | 🔴 | `RunConfig` es un manifiesto + configs por plano | — | |
| R-04 | 17.3.8.3.2 | PRECISA | 🔴 | Granularidad `scene\|subject` + caveat semántico de escena | — | reforzada: G1 (sujeto) terminó siendo **el mejor resultado del banco** |
| R-05 | Tabla 45 / 17.3.6.4 | CONTRADICE | 🔴 | El vocabulario del núcleo es positivo (person/helmet/vest) | — | |
| R-06 | 17.3.11 | CONCRETA | 🔴 | Partir el hedge en dos + tabla de correspondencia | **94 §1** | |
| R-07 | 17.3.11.4 | CONCRETA | 🔴 | Regla de evolución del evento (el pedido del tutor) | **94 §2** | ✎ **08-12: la fila de identidad de sujeto estaba vieja y se corrigió** — ver §3c |
| R-08 | 17.3.8.1 / .4 | CONCRETA | 🟠 | El bus existe y tiene tecnología: ZeroMQ + msgpack | **94 §3** | |
| R-09 | 17.3.5 | CONCRETA | 🟠 | Figura nueva: vista de procesos (dos servicios HTTP) | **94 §4** | es la **FIG-A** del inventario de cierre |
| R-10 | 17.3.13 | CONCRETA | 🟠 | Diccionario de métricas con t0/t1 + criterio de relojes | **94 §5** | cruza con `AJ-2.03` (§17.1) |
| R-11 | 17.3.14 (nueva .6) | PRECISA | 🟠 | Temporalidad de la fuente y el "cero silencioso" | **94 §6** | formalizada en ADR-013 |
| R-12 | cierre (nueva) | EVIDENCIA | 🟠 | Verificación: qué funciona y cómo se midió | **94 §7** | insumo completo: `operacion/97` |
| R-13 | cierre (nueva) | EVIDENCIA | 🟠 | Registro del alcance efectivo y brechas | **94 §8** | ✎ actualizado post ADR-016/017 y `operacion/114`; no usar la tabla preimplementación |
| R-14 | 17.3.8.2 / Tabla 46 | PRECISA | 🟠 | Ventanas efectivas: 4000 / 7000 ms; severidades `high`/`medium` | — | ficha canónica de los valores; cruza con `AJ-2.01` |
| R-15 | 17.3.12.1 | CONCRETA | 🟡 | El repositorio es JSONL append-only, con layout | — | |
| R-16 | 17.3.13.3 | PRECISA | 🟡 | La aplicabilidad es un campo literal (`status` + `cause`) | — | ADR-006/013; cruza con `AJ-2.12` |
| R-17 | 17.3.15 | CONCRETA | 🟡 | Tabla rol → contenedor (Nodo A ≈ EN-1, Nodo B ≈ CPN) | — | |
| R-18 | Tabla 43 (DA-01…13) | PRECISA | 🟡 | Actualizar el estado de las decisiones condicionadas | — | **no confundir con T-81** (ADR → informe), que es otra tabla |
| R-19 | Tabla 50 | ERRATA | 🟡 | `PatternDefinition` es huérfano: falta su fila | — | |
| R-20 | Tabla 57 | PRECISA | 🟡 | Riesgos: los que se materializaron y cómo se mitigaron | — | |
| R-21 | Tablas 58/59 | EVIDENCIA | 🟠 | Backlog: estado real de los 16 ítems | — | **desbloqueada por ADR-015**, y tiene **un punto falso** (ver §3) |
| R-22 | 17.3.14.5 | PRECISA | 🟡 | EBE: la cámara IP real ya se usó; la brecha que queda | — | cruza con `AJ-2.10` |
| R-23 | varias | ERRATA | 🟢 | Figuras sin numerar y vacías, títulos pegados, duplicados | — | |
| R-24 | fuera de 17.3 | PRECISA | 🟡 | Inventario de datasets desactualizado | — | enrutada también desde `AJ-0.05` |
| R-25 | 17.3.11 / 17.3.13 | CONCRETA | 🟠 | Contrato de GT temporal + identidad + los 5 hitos | — | cruza con `AJ-2.09` |
| R-26 | 17.3.17 / 17.3.18 | CONCRETA | 🟠 | **Extensibilidad medida: cuánto cuesta una condición nueva** | **94 §9** | **la más valiosa**; su cifra es la tabla **T-77** |

**Recuento:** 26 redlines — **7 🔴 crítica · 10 🟠 alta · 8 🟡 media · 1 🟢 baja**.
**9 tienen el texto completo ya redactado** en el doc 94 (§1–§9).

---

## 3. Las dos correcciones que ADR-015 dejó pendientes de anotar

ADR-015 (aceptado 2026-08-05) desbloqueó dos redlines que lo estaban esperando, y al
hacerlo dejó dos anotaciones que **hay que aplicar antes de transcribir**:

- **R-13 (registro del alcance efectivo):** la versión inicial quedó superada dos veces.
  `94` §8 ya debe registrar como ejercidos G1, la comparación E-DIR/E-IND/E-HYB, la
  paridad DBE/EBE y la distribución funcional; conserva como límites las métricas MOT,
  las condiciones de nivel 2/3 y las brechas de integración declaradas.
- **R-21 (backlog, Tablas 58/59):** tiene **un punto falso** — dice *"MOT ✗ tracker no
  implementado"*. Lo excluido son las **métricas** MOT (exclusión E-10), **no la
  capacidad**: el tracker existe y la granularidad por sujeto (G1) es el mejor resultado
  del banco.

Ambas anotaciones ya están escritas en el propio 93, en las fichas de R-13 y R-21.

---

## 3b. ✎ 2026-08-11 — la regla de no-anacronismo y las redlines "al cierre"

**La regla** (mapa, regla 5): una etapa temprana no menciona resultados de etapas
posteriores. El §17.3 es Etapa 3 — **recibe correcciones de diseño y decisiones**
(R-01…R-11, R-14…R-19, R-24, R-25: todas son eso), pero **no números de verificación**.
Cuatro redlines quedan tocadas:

- **R-12** ("verificación: qué funciona y cómo se midió") y **R-13** ("registro de lo no
  implementado") fueron concebidas como *secciones nuevas al cierre* del §17.3 — cuando
  §17.4/§17.5 no existían como plan. Hoy existen, y **ese material aterriza en §17.4**
  (así lo enruta el doc de Etapa 4: `AJ-4.10` y `AJ-4.11` usan `94` §7–§8). El §17.3
  queda, a lo sumo, con un puntero de una línea. El texto del `94` §7–§8 sirve igual —
  cambia la sección de destino, no el contenido.
- **R-20** (riesgos que se materializaron) y **R-22** (la cámara IP real ya se usó): la
  parte *retrospectiva* ("cómo resultó") va como **nota fechada o remisión a §17.4**,
  no como prosa del diseño reescrita en pasado profético.

La decisión formal de cada caso queda donde siempre: en la casilla de la redline.

## 3c. ✎ 2026-08-12 — R-07: la fila de identidad de sujeto había envejecido mal

**R-07 es la redline que contesta el punto que el tutor técnico marcó como "muy
importante"**: que el evento de inferencia dé soporte a datos que hoy no están —tracking,
velocidad, dirección, pose, segmentación—. Su texto (doc `94` §2, Tabla 63) declaraba
para identidad de sujeto que *"el componente que lo puebla no está implementado"*. **Era
cierto el 12/07 y es falso desde el 2026-08-04.** El glosario (`13`, entrada `track_id`)
ya llevaba la corrección desde el 08-10; el material de Etapa 3 no la había recibido.

Corregido el 2026-08-12 en `94` §2 y en `92` §4.2 (con recuadro y ruta:línea), y la
corrección **refuerza** la respuesta al tutor en lugar de debilitarla: de las cinco
extensiones que él nombró, **una se recorrió de punta a punta, por configuración y sin
tocar el contrato**, y quedó medida. El reparto entre etapas respeta la regla de
no-anacronismo:

- **§17.3.11.4** (acá): el mecanismo y el estado del contrato, **sin cifra**.
- **§17.4**: la cifra y la comparación pareada (`AJ-4.12`, ampliado el mismo día).

Dos honestidades que viajan con el dato y no se pueden recortar al transcribir: el
`track_id` **no queda en el JSONL del plano de medios** sino en los artefactos del
control, y **lo excluido por E-10 son las métricas MOT, no la capacidad**.

## 4. Cómo se trabaja este frente

El 93 fue escrito para operarse ítem por ítem, con casilla de decisión por redline:

```
DECISIÓN → [ ] acepto   [ ] modifico   [ ] rechazo
```

El orden sugerido está al final del 93 (§*Orden sugerido de trabajo*). El criterio
razonable: **las 7 🔴 primero** (4 son contradicciones, que no son opinables), después
las 🟠 que ya tienen texto en el doc 94 —son transcripción, no redacción—, y al final las
🟡/🟢 de forma.

**El `.docx` no se toca desde el 93.** El 93 produce la instrucción; la edición se hace
en el documento, y la casilla queda como registro de la decisión tomada.

---

## 5. §17.3.10 — el caso especial de la distribución de alertas

`material-etapa-3/92b-concrecion-distribucion-alertas.md` es el diseño completo de esa
subsección, y **`nucleo/19`** es el cierre arquitectónico del ciclo de vida de la alerta
(dónde viven cooldown, supresión y re-notificación — consolida `nucleo/06`, ADR-005,
ADR-011, la spec 45 y el propio `92b`).

**El estatuto lo fija ADR-016 y el estado ejecutado lo fija `operacion/114`.** El módulo
pasó de exclusión a trabajo comprometido y hoy está **funcionalmente implementado**: DBE,
EBE, cooldown, idempotencia, MQTT QoS 1 y reporte consolidado fueron verificados. ✎ **2026-08-14:** las
tres brechas que este párrafo declaraba —vista de webconsole, orquestación y un repo sin
commits— se cerraron el 2026-08-13 (`13c801e`, `42529e2`; repo con `c9903cc` y `1e6d8fa`).

El §17.3.10 describe arquitectura y contratos; las mediciones de verificación del canal no
se convierten automáticamente en resultados de desempeño. El publisher
`control.alert.v1` continúa desactivado por defecto y `AlertEvent` no tiene
`confirmed_at_ms` (detalle corregido por `92b`).

[Enmienda 2026-08-14] §17.3.10 tiene UNA pieza de evidencia en el inventario de cierre:
T-85 (`gobierno/99` §1), la latencia de notificación medida por la campaña del doc 118.

## 6. Fuentes

`material-etapa-3/93` (tablero y las 26 fichas) · `94` (§1–§9, el texto) · `91` (el
relevamiento y el pedido del tutor técnico) · `92` (concreción verificada contra código)
· `92b` (§17.3.10) · `nucleo/19` (ciclo de vida de la alerta) · `gobierno/95` (la
auditoría adversarial que produjo la v2 y agregó R-25/R-26) ·
`decisiones/adr-015-cierre-de-alcance.md` + `adr-016-reapertura-acotada-distribucion.md`.
