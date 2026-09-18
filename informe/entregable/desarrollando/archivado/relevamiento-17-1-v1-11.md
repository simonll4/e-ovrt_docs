# Relevamiento crítico de §17.1 v1.11 (2026-09-03)

> ✅ **CERRADO el 2026-09-03 — §17.1 quedó en la v1.15, aceptada y limpia.** Este documento es la
> constancia completa del ciclo v1.10 → v1.15 (relevamiento de la v1.11, cotejo de la
> contra-evaluación de GPT, actas §H a §L de las versiones v1.12, v1.13 y v1.14) y **ya no se
> edita**. La reescritura del tramo final y el cierre están en
> [`analisis-17-1-8-anexos.md`](analisis-17-1-8-anexos.md) §8. Documento vigente de la etapa:
> `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.15.docx`.

> **Qué es.** Relevamiento completo de `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.11.docx`
> contra la v1.10 aceptada, medido sobre el `.docx` real (extracción propia de `document.xml`,
> diff por oración con umbral de similitud 0,8, cotejo de citas por apellido+año, conteo de
> ecuaciones OMML, comentarios, saltos de sección y referencias cruzadas). Nada de lo que sigue
> se infiere: todo se midió. Cotejo cruzado con `archivado/analisis-poda-17-1.md`,
> `justificacion-extension-17-1.md`, `validacion-reestructuracion-17-1-5.md`, los textos
> extraídos de §17.3/§17.4/§17.5 (`90*.md`), §15/16 v1.1 y el registro de datasets
> (`e-ovrt_datasets/datasets/registry/`).
>
> **Veredicto:** la v1.11 es una reestructuración **buena en dirección y a medio cerrar**. §17.1.6
> queda mejor que en la v1.10 con pérdidas menores; §17.1.7 gana rigor conceptual (unidad episodio,
> dominios de reloj, hitos en vez de sumas) pero **pierde tres piezas que la tesis no puede
> perder** (niveles de compromiso, modelo aditivo del presupuesto, criterios de factibilidad) y
> deja **cinco defectos mecánicos** (Anexo D huérfano y contradictorio, tres referencias colgantes,
> una fila truncada, dos huecos nuevos de numeración de tablas). No aceptar tal cual; sí aceptar la
> estructura y reparar. Tres decisiones quedan para el usuario (§F).

## A. Medición v1.10 → v1.11

| Magnitud | v1.10 | v1.11 | Nota |
|---|---:|---:|---|
| Palabras (prosa + tablas, conteo propio) | 19.504 | 15.297 | −21,6 % (el acta anterior contaba 21.779 con otro método; usar el relativo) |
| Títulos | 83 | 44 | nivel 5: **35 → 0**; nivel 4: 32 → 29; nivel 3: 12 → 11 |
| Tablas | 24 | 22 | caen **31** y **32**; huecos 18/19 (previo) y ahora 31/32 |
| Ecuaciones OMML | 76 | **4** | 72 desaparecen; 74 de ellas vivían en §17.1.7 |
| Comentarios | 1 | 3 | dos nuevos, firmados por el colega en el archivo (ver §E) |
| Saltos de sección (apaisadas) | 45 (24) | 38 (22) | coherente con las 2 tablas menos |
| Marcas de revisión | 0 | 0 | — |
| Citas (apellido, año) | 30 | 30 | **cero bajas, cero altas** — regla del pase 5 cumplida |
| Marcadores `[[PENDIENTE]]` | 0 | **3** | nuevos, en §17.1.6.2 (×2) y §17.1.6.4 |
| Párrafo de cuerpo con estilo Heading | 1 (§17.1.4.2) | 0 | **A-3 resuelto** |

Bloques **byte-idénticos en texto**: §17.1, 17.1.1, 17.1.2, 17.1.3, 17.1.8, 17.1.9, 17.1.10,
17.1.11, Anexo C y Anexo D (0 oraciones caídas, 0 nuevas). §17.1.5: 9 caídas / 8 nuevas
(metadiscurso de handoff, ver §D). Los dos bloques reescritos son **§17.1.6** (164 → 117
oraciones+filas; 127 caídas / 85 nuevas) y **§17.1.7** (246 → 179; 234 caídas / 168 nuevas).

## B. §17.1.6 Estrategia de datos — 19 títulos → 5, −42 % · veredicto: ✅ aceptar con 4 reparaciones

**Mapa.** `.1.1–.1.3` → **17.1.6.1 Alcance y criterios** (P-E1-03/08, dos categorías, exclusiones,
Tabla 22 C1–C7) · `.2.1–.2.8` → **17.1.6.2 Fuentes, cobertura y brechas** (Tabla 23 retenidas
**fusionada con la aptitud FT/eval de la vieja Tabla 26**, Tabla 24 no retenidas, **Tabla 25
cobertura por CR nueva**) · `.2.4 + .2.7` → **17.1.6.3 Roles y partición** (regla de asignación
exclusiva, 500–2.000, Tabla 26 condiciones) · `.3 + .3.1 + .3.2` → **17.1.6.4 Benchmarks
seguimiento** (Tabla 27 MOT17/OVT-B) · `.4.1 + .4.2 + .5` → **17.1.6.5 Licencias, ética y
logística**.

**Lo que se conserva y está bien:** todo el pre-registro protegido por D-E2-6 (MOT17/OVT-B con
función, métricas y límite de interpretación), los siete criterios, las siete condiciones de
partición, el rango 500–2.000, la escalera de datos complementarios para CR-03/04 (curación →
anotación acotada → EBE), la brecha CR-03…06, la regla de licencia "no se transfiere por
inferencia", la logística hacia el TN Mendieta. La **Tabla 25 (cobertura por CR y consecuencia
metodológica)** es una ganancia neta: reemplaza tres párrafos sueltos por una lectura única.
La prosa nueva no tiene dos puntos ni punto y coma (regla del usuario).

**Lo que cayó y conviene evaluar:**

| # | Pérdida | Peso | Recomendación |
|---|---|---|---|
| B-1 | Lista nominal de corpus de preentrenamiento excluidos (Visual Genome, LVIS, Objects365, Open Images) — queda "corpus generalistas empleados para preentrenar". LVIS sí está en §16 (18 menciones); los otros tres desaparecen del informe. | bajo | opcional: una frase entre paréntesis |
| B-2 | Frase de las condiciones fuera de alcance (calzado, guantes, gafas, pasillos obstruidos) "no integran el alcance experimental de la Etapa 2" | bajo-medio | restaurar una frase en 17.1.6.1: es la única defensa ante "¿por qué no evaluaron X?" dentro de esta sección (17.1.2.1 la cubre en parte) |
| B-3 | Expansión de acrónimos MOTA/IDF1/HOTA/TETA/LocA/ClsA/AssA (nota de la vieja Tabla 27). TETA/LocA/ClsA/AssA **no aparecen en §15/16**: hoy sólo viven en la Tabla 27 sin definir | medio | restaurar la nota de acrónimos bajo Tabla 27 |
| B-4 | "La instancia de análisis y diseño arquitectónico verifica manualmente los términos efectivos de cada fuente antes de descargar…" → v1.11 lo dice en pasiva ("se verifican") sin responsable | bajo | aceptar |

**Defectos mecánicos en §17.1.6:**
- **Tabla 26, fila "Deduplicación cruzada": truncada** — termina en coma ("…se verifican duplicados y casi duplicados,"). Falta el remate (v1.10: "…especialmente entre datasets de PPE web-mined o crowd-sourced que podrían compartir fuentes de origen").
- **Tres `[[PENDIENTE]]` nuevos.** Dos se responden hoy desde el registro del repo, sin salir a buscar nada:
  `construction_site_safety` = Roboflow Universe **v27**, descargado 2026-06-18 · `ppe_siabar` = Roboflow Universe **v1**, 2026-06-18 (`download_log.md`, `datasets_metadata.yaml`) · SH17 = CC BY-NC-SA **4.0** (verificada en README) · Pictor-PPE = "Verificar / Bloqueado" · Construction-PPE = AGPL-3.0 con `LICENSE` en la descarga · MOCS = CC BY 4.0 **declarada por el uploader de la copia Roboflow**, original sin verificar · CHV = grant informal + cita, sin SPDX (`license_registry.md`). El tercero (referencias primarias y licencias de MOT17/OVT-B) sí exige bibliografía: MOT17 CC BY-NC-SA 3.0 y OVT-B Apache-2.0 ya están en la tabla; faltan las entradas de Referencias.
  ⚠ Ojo con la voz del documento (D-P3-9): §17.1 es el protocolo de Etapa 2; consignar "v27 / 2026-06-18" es dato de implementación. Cabe como nota de tabla ("versión efectivamente gestionada: …") o remitir a §17.4.
- **Anexo C, nota de la Tabla C.3, referencia a `17.1.6.4.2` y `17.1.6.2.1`**: ambas secciones ya no existen → deben pasar a 17.1.6.5 y 17.1.6.2.

**Decisión consumida de hecho:** la fusión de la vieja Tabla 26 (aptitud FT/eval) dentro de la
Tabla 23 era **PODA-C** en `analisis-poda-17-1.md` §5 ("requiere reabrir decisiones firmadas";
D-P5-3 recomendaba NO). Se hizo. Es defendible (la columna "Papel posible" conserva la
información), pero hay que firmarla (§F, D-3).

## C. §17.1.7 Framework de métricas — 28 títulos → 6, −43 %, 74 → 2 ecuaciones · veredicto: ⚠ aceptar la estructura, restaurar tres piezas

**Mapa.** `.1.1` → **17.1.7.1 Propósito, alcance y aplicabilidad** (P-E1-06/01, tres niveles,
**cuatro estados de una métrica**) · `.2 + .3.1` → **17.1.7.2 Niveles y jerarquía** (Tabla 28
nueva: nivel × unidad × métricas × condición × lectura) · `.4.1–.4.3 + .5.1–.5.4 + .8.3` →
**17.1.7.3 Métricas y reglas de lectura** · `.6` → **17.1.7.4 Comparación zero-shot vs
ajustada** (Tabla 29 vieja pasa a prosa) · `.2 + .7.x` → **17.1.7.5 Presupuesto temporal**
(2 ecuaciones nuevas, Tabla 29 tramos, Tabla 30 = vieja Tabla 32, rangos 35–250 ms conservados)
· `.8.1 + .8.2 + .8.4 + .9` → **17.1.7.6 Instrumentación, aplicabilidad y reporte**.

### C.1 Lo que la v1.11 mejora (conservar)

1. **La unidad del nivel de alerta es el episodio anotado**, con material negativo tratado por
   conteo de FP y FAR/hora derivada, y re-alerta ≠ FP. Esto alinea §17.1 con el término "evento
   de percepción" (E3), con el clip bench (32/15/47) y con ADR-011 (`re_alerts` no son FP).
2. **Dominios de reloj**: "no se restan marcas monotónicas de procesos distintos"; correlación por
   marca de fuente o identificador. Mejor que el "timestamps monotónicos" de la v1.10.
3. **t_alert-system(e) = τ_confirmación(e) − τ_inicio(e)** y **t_alert-notification(a) =
   τ_canal(a) − τ_disponibilidad(a)** definidas como diferencia de hitos, con la regla "los
   percentiles agregados no se suman". Recoge exactamente las trampas de instrumento de
   `operacion/96` (F-96) y `101` (F-101.8).
4. **Tabla 29 separa `capture_to_host` (captura → dequeue) del G2A instrumentado (dequeue →
   fin de inferencia)** y dice que G2A "no equivale a sensor → algoritmo cuando la captura queda
   fuera". Es F-101.8 escrito como regla. Ver §F D-2 sobre el anacronismo.
5. **Cuatro estados explícitos por métrica** (calculada / aplicable no calculada / no aplicable /
   no interpretable) y "un valor ausente nunca se reemplaza por cero". Más limpio que la v1.10.
6. Las reglas de lectura que sostienen §17.5 sobreviven: reporte por estrato con denominador,
   SDR sólo a cadencia igual, latencia de alerta sólo sobre episodios comunes, negativos fuera
   de P/R/F1, unidad del FP declarada antes de medir ΔFP_tracking, warm-up y P50/P95/P99.

### C.2 Lo que la tesis pierde y hay que restaurar

| # | Pérdida | Por qué importa | Cómo restaurar (mínimo) |
|---|---|---|---|
| **C-1** | **Niveles de compromiso (obligatorio / deseable / conceptual)** y **jerarquía primario / secundario / transversal** (viejas .3.1, .3.2, Tabla 31). Desaparecen las definiciones, pero el vocabulario **sigue usándose**: Tabla 33 ("métrica obligatoria", "métricas primarias calculadas"), Anexo D Tabla D.1 (columna "Compromiso" con Obligatorio/Deseable), §17.1.11.1 ("núcleo obligatorio"), §17.1.9.1. | Es la **matriz de aplicación condicionada**: el dispositivo de honestidad por el cual §17.5 declara "prescripto y no ejercido" sin que parezca omisión. `analisis-poda` §6.3 lo marcó como no cortable; `justificacion-extension` §2.3 lo mismo. Hoy "obligatoria" en Tabla 33 no significa nada dentro del documento. | Un párrafo en 17.1.7.1 con las tres definiciones y la frase "la pertenencia al nivel primario expresa prioridad interpretativa, no aplicabilidad automática". ~90 palabras. |
| **C-2** | **Modelo aditivo del presupuesto** (las 4 ecuaciones de .7.1: t_G2A = t_cap + t_transp + t_pre + t_inf; t_alert-system ≈ t_evidencia + t_G2A + t_tracking + t_razonamiento; t_alert-notification ≈ t_alert-system + t_notif; t_evidencia como ventana funcional) y la **vieja Tabla 30** (componente ↔ tramo ↔ compromiso). | Es la respuesta literal a **P-E1-01** ("operacionaliza el presupuesto mediante descomposición en componentes medibles"). Sin ella, el "35 a 250 ms" de 17.1.7.5 aparece sin fórmula que diga qué se suma; y §17.1.11.2 sigue prometiendo "la instrumentación de t_G2A y t_alert-system". La v1.11 tiene razón en que t_alert es diferencia de hitos, **no suma** — por eso el modelo aditivo debe volver **rotulado como modelo orientativo de plausibilidad**, que es exactamente el uso que le daba .7.7.4. La Tabla 29 nueva es mejor que la vieja Tabla 30 y debe quedarse. | Reponer las 2 primeras ecuaciones (t_G2A y t_alert-system) antes del párrafo "Con el perfil de hardware de referencia…", con una frase: "El modelo es aditivo y orientativo; sirve para instrumentar y estimar plausibilidad, no reemplaza la medición por hitos". ~60 palabras + 2 OMML. |
| **C-3** | **Cinco criterios de factibilidad** para que una métrica sea obligatoria (necesidad operativa, GT verificable, módulo existente, instrumentación suficiente, costo compatible) (vieja .3.3). | Es la regla con la que el jurado puede auditar por qué una métrica quedó "no aplicable" y no "omitida". La v1.11 enumera casos (17.1.7.6 §4) pero no el criterio general. | Una oración en 17.1.7.1. ~45 palabras. |
| C-4 | Puente aritmético entre Tabla 29 y Tabla 30: "persistencia orientativa de 2 a 4 s + 35–250 ms de cómputo ⇒ objetivo de 3 a 5 s para severidad crítica" y la **cláusula de recalibración** "si el hardware difiere (modelos más pesados, resolución > 640 px, transporte con más latencia), los umbrales se recalibran antes de operar como criterio de aceptación". | La primera es la única verificación de coherencia interna entre rangos y umbrales. La segunda es la que §17.5 necesita cuando el campeón resulta un transformer (GDINO-tiny) a 560 px: la nota de la Tabla 30 la cubre a medias ("deben calibrarse con la cadencia efectiva…"). | Una oración cada una. |
| C-5 | "La selección de checkpoints no debe hacerse sobre el conjunto de evaluación" y "horas-persona" en el costo del ajuste. | Anti-leakage explícito para T1/T2 (`best_epoch=1` se eligió sobre validación interna). Tabla 26 dice "selección de hiperparámetros", que no es lo mismo. | Añadir "ni selección de checkpoints" en Tabla 26 fila "Congelamiento previo". |
| C-6 | Tríada nominal G2A / **Glass-to-Alert** / glass-to-glass (vieja .2). | Glass-to-Alert no se usa en ningún otro documento del informe (0 en §15/16, §17.3, §17.4, §17.5); Glass-to-Algorithm sí está en §16 (3). Pérdida nula para la coherencia cruzada. | Nada. |
| C-7 | Ejemplos de latencia por modelo (YOLOE-v8-S 3,3 ms, G-DINO 1.5 Edge 13,3 ms, …) y la aclaración "YOLO-World es referencia comparativa, no candidato". | Las citas (Cheng 2024, Wang 2025) se conservan agrupadas. Era PODA-B (re-argumentación → remite a §15/16). | Nada. |

### C.3 Defectos mecánicos en §17.1.7 / Anexo D

- **Anexo D quedó huérfano.** En la v1.10 el cuerpo remitía a D.1 (.4.3), D.2 (.8.1) y D.3 (.8.4).
  En la v1.11 **ninguna sección del desarrollo cita Tabla D.1, D.2 ni D.3** ("Anexo D" 4 → 1, la
  del propio título). Tres tablas de 898 palabras sin punto de entrada.
- **Anexo D contradice la Tabla 29 nueva.** Tabla D.1 define "Latencia G2A: intervalo entre
  captura o lectura del cuadro y disponibilidad del resultado de inferencia" con criterio
  "timestamps monotónicos"; la Tabla 29 dice "G2A instrumentado: dequeue → fin de inferencia" y
  §17.1.7.5 prohíbe restar monotónicos entre dominios. Hay que alinear D.1 con la definición que
  se elija (§F D-2).
- **Huecos de numeración**: 18/19 (rama GPT, abierto) y ahora **31/32**. La Tabla 30 nueva es la
  vieja 32; la 31 (jerarquía) cae con C-1. Si se restaura C-1 como tabla, ocupa el 31.
- `§17.1.3.3` remite a la **Sección 17.1.4.4**, que no existe (defecto heredado de la rama GPT,
  sigue abierto).

## D. §17.1.4 y §17.1.5 — cambios menores

- **§17.1.4.2**: el párrafo "La relación entre ambos escenarios no es de reemplazo…" vuelve a ser
  cuerpo (con la Tabla 17 detrás). **A-3 resuelto.** Ningún texto perdido.
- **§17.1.5**: 9 oraciones caídas, 8 nuevas. Siete son metadiscurso de handoff ("corresponde a la
  instancia de análisis y diseño arquitectónico", "de realizarse, esas pruebas corresponden a la
  validación experimental") — coherente con el pase 4. Dos merecen mirada:
  - "La severidad … **ni define por sí misma los umbrales computacionales** de activación,
    distancia, persistencia o latencia" (pase 6, desacople normativo) → la v1.11 conserva sólo
    "no constituye una calificación normativa". La segunda mitad la recupera parcialmente
    17.1.7.3 ("la severidad funciona como estrato de lectura y no como métrica"). Aceptable.
  - "las formulaciones finalistas deben quedar seleccionadas y congeladas mediante un **acta**
    previa a la evaluación comparativa" → cae; la palabra "acta" pasa de 1 a 0 en el documento.
    La regla sobrevive en la Fase 5 de 17.1.5.4 ("Selección y congelamiento"), así que el
    pre-registro del freeze (07-28) sigue teniendo referente. Aceptable.
- El párrafo introductorio de 17.1.5 pierde "Los valores numéricos que se fijan son decisiones de
  protocolo dentro de rangos orientativos, y su calibración empírica corresponde al framework…".
  Aceptable: 17.1.7.3 y la nota de la Tabla 30 lo dicen.

## E. Comentarios y marcas

- Comentario 0 (colega, sobre 17.1.4, "Acomode esta sección…"): intacto.
- **Nuevos**: comentario 1 sobre el título de **17.1.5** ("Repasar") y comentario 2 sobre el título
  de **17.1.6** ("Validar, sobre todo la lista de pendientes y los datasets"). Ambos figuran en el
  archivo con autoría del colega. Regla vigente (`feedback_no_tocar_comentarios_docx`): se
  informan como estado y viajan; no los toco.
- Los 26 comentarios perdidos de la rama GPT (A-1) siguen perdidos; la v1.8 sigue siendo la
  fuente de recuperación.

## F. Decisiones para el usuario

- **D-1 — Guardarraíl 2.** El pase 1–2 firmó "§17.1.5 y §17.1.7 no se comprimen", y `analisis-poda`
  §4.8 listó como intocables la estimación de latencia, el protocolo FT, las reglas .8.1/.8.3 y
  los umbrales. La v1.11 comprime §17.1.7 un 43 %. Lo intocable **sobrevive en sustancia**
  (rangos, umbrales, FT, reglas de lectura) salvo C-1/C-2/C-3. Propuesta: **derogar el
  guardarraíl 2 para §17.1.7 con la condición de restaurar C-1, C-2 y C-3**, y dejar constancia.
- **D-2 — G2A desde el dequeue en §17.1.** La Tabla 29 escribe F-101.8 (hallazgo del 08-05,
  posterior a la Etapa 2) como regla del protocolo. Es coherente con la decisión de que "el
  informe debe decirlo", pero §17.1 es el protocolo *ex ante* y §17.5 reporta "prescripto vs
  ejercido". Dos salidas: (a) aceptar la regla en §17.1 y **alinear Tabla D.1** (y no presentar
  luego en §17.5 la separación capture_to_host/G2A como hallazgo, sino como cumplimiento); o
  (b) volver en Tabla 29 a "captura o lectura → resultado" y dejar el refinamiento del dequeue a
  §17.4/§17.5 como hallazgo F-101.8. Recomiendo **(a)**: la regla es correcta y está redactada
  como regla ("cuando no existe una marca confiable de captura, el informe comienza en el primer
  hito instrumentado"), pero la firma es tuya.
- **D-3 — Fusión de la aptitud FT/eval en la Tabla 23** (PODA-C consumida). Firmar o revertir.
  Recomiendo firmar.

## G. Plan de reparación propuesto (si se acepta la estructura)

Sobre `document.xml` byte a byte, mismo instrumento que `aplicar_1715.py`, sin tocar comentarios
ni saltos de sección:

1. 17.1.7.1: párrafo de niveles de compromiso + criterios de factibilidad (C-1, C-3).
2. 17.1.7.5: dos ecuaciones OMML del modelo aditivo rotuladas como orientativas + frase puente
   2–4 s / 3–5 s + cláusula de recalibración (C-2, C-4). Las OMML se transplantan de la v1.10.
3. 17.1.7.3 o 17.1.7.6: remisión a Tabla D.2 (insumos por familia) y Tabla D.3 (bitácora); 17.1.7.3
   remisión a Tabla D.1 (rendimiento). Alinear la fila "Latencia G2A" de D.1 según D-2.
4. Tabla 26: completar la fila "Deduplicación cruzada"; añadir "ni selección de checkpoints" (C-5).
5. Anexo C nota C.3: `17.1.6.4.2 → 17.1.6.5`, `17.1.6.2.1 → 17.1.6.2`. §17.1.3.3: `17.1.4.4 → 17.1.4.2`.
6. Tabla 27: nota de acrónimos (B-3). 17.1.6.1: frase de condiciones fuera de alcance (B-2).
7. Resolver los tres `[[PENDIENTE]]` con el registro (versiones/fechas como nota de tabla, o remitir
   a §17.4) y agregar las dos referencias MOT17/OVT-B al listado.
8. Renumerar tablas 33–35 → 31–33 y C/D quedan; o dejar los huecos y resolverlos en la integración
   junto con 18/19 (recomendado: en la integración, de una sola vez).

Después: re-medir (verificador OK, 30 citas, 6 ecuaciones, 3 comentarios), archivar la v1.10,
y **recién entonces** re-extraer `90f`, regenerar el kit y mover la nota D-E2-2 del generador
(hoy apunta a 17.1.5.4.2 y a 17.1.7.x que ya no existen: `generar_project_kit.py` l. 318/516/517).

## H. Acta de aplicación (2026-09-03) — v1.11 → v1.12 (sugerencias sin aceptar)

**Decisiones del usuario sobre §B:** B-1 no · **B-2 sí** · B-3 no · B-4 no · los defectos mecánicos
de §17.1.6 (fila truncada de la Tabla 26, los tres `[[PENDIENTE]]`, la nota de la Tabla C.3) quedan
**pendientes para el final**. Todo lo demás (§C.2 C-1…C-5, §C.3 salvo los huecos de numeración,
§F D-1/D-2(a)/D-3) se toma tal como se recomendó.

**Qué se aplicó**, como cambios controlados (autor `Claude`, fecha 2026-09-03), sobre una copia:
`E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.12 (sugerencias sin aceptar).docx`. La v1.11
no se modificó.

| # | Sitio | Cambio | Marca |
|---|---|---|---|
| E1 | 17.1.7.1, entre el párrafo de los tres niveles y el de los cuatro estados | **C-1** niveles de compromiso (obligatorio / deseable / conceptual) + jerarquía primario / secundario / transversal · **C-3** cinco criterios de factibilidad | 2 párrafos insertados |
| E2 | 17.1.7.5, entre "El tramo computacional reúne…" y "Con el perfil de hardware…" | **C-2** modelo aditivo orientativo: párrafo de encuadre + `t_G2A = t_preprocesamiento + t_inferencia` + `t_alert-system ≈ t_evidencia + t_captura-host + t_G2A + t_tracking + t_razonamiento` + párrafo que mapea los símbolos a los tramos de la Tabla 29 y declara que la estimación 35–250 ms es la suma de todos los términos salvo t_evidencia. **La ecuación de t_G2A ya no incluye captura ni transporte**, porque la Tabla 29 define G2A desde el dequeue (D-2a); ese tramo entra como t_captura-host sólo si hay marca de captura confiable | 2 párrafos + 2 ecuaciones OMML insertados (estructura transplantada de la v1.10, párrafos 556/557) |
| E2b | 17.1.7.5, final del párrafo previo a la Tabla 30 (lleva el `sectPr` portrait: sólo se agregaron runs, ningún párrafo) | **C-4** puente 2–4 s + cómputo ⇒ 3–5 s (cita la ventana de 17.1.5.2) · plausibilidad de 5–10 y 10–20 s · cláusula de recalibración si el hardware difiere del perfil | runs insertados |
| E3 | Tabla 26, fila "Congelamiento previo" | **C-5** "…selección de hiperparámetros, **selección de checkpoints** ni aumento de datos" | run insertado |
| E4 | 17.1.7.3 (viabilidad) · 17.1.7.6 §1 (registro) · 17.1.7.6 §4 (aplicabilidad) | remisiones a **Tabla D.1**, **Tabla D.3** y **Tabla D.2** del Anexo D — el anexo deja de estar huérfano | 3 runs insertados |
| E5 | Anexo D, Tabla D.1, fila "Latencia G2A" | **D-2(a)** definición "Intervalo entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia. La captura y el transporte hasta el dequeue se informan aparte como capture_to_host." · criterio "Timestamps monotónicos" → "Hitos y dominio de reloj declarados" | 2 del + 2 ins |
| E6 | 17.1.3.3 | "Sección 17.1.4.4" → "Sección 17.1.4.2" | 1 del + 1 ins |
| E7 | 17.1.6.1 §2, al final | **B-2** condiciones fuera del catálogo (calzado, guantes, gafas, pasillos) remiten a 17.1.5.1 | run insertado |

**Medición v1.12:** 906 párrafos (+6) · 21 `w:ins` (6 son marcas de párrafo insertado) · 3 `w:del` ·
ids 9001–9024 únicos · **6 ecuaciones** · 22 tablas · 38 saltos de sección · 3 comentarios intactos ·
las otras 17 partes del zip **idénticas byte a byte** · prosa nueva con **0 dos puntos y 0 punto y
coma** (aserción en el instrumento). **Rechazar todo reproduce la v1.11 exactamente** (897/897
párrafos con texto iguales); **aceptar todo** produce sólo las 13 diferencias de la tabla.
Instrumento: `herramientas/aplicar_v112_17_1.py` (copia del de scratchpad; lee los OMML de la v1.10).

**Queda para después (no es de este pase):** aceptar o rechazar las sugerencias en Word → la
v1.12 limpia · los mecánicos de §17.1.6 (fila truncada · `[[PENDIENTE]]` × 3 · nota C.3 →
17.1.6.5 / 17.1.6.2) · huecos 18/19 y 31/32 en la integración · archivar v1.10 y v1.11 · re-extraer
`90f`, regenerar el kit y mover la nota D-E2-2 del generador · A-1 (26 comentarios de la v1.8).

## I. Cotejo de la contra-evaluación de GPT (2026-09-03) — qué se verificó y qué no resiste

GPT devolvió una evaluación del relevamiento con un paquete propio de reparaciones. Se cotejó cada
afirmación fáctica contra los archivos. Resultado: **el criterio editorial es bueno en tres puntos y
debe adoptarse; cuatro premisas son falsas o están vencidas, y una instrucción revierte una decisión
firmada.**

### I.1 Afirmaciones de GPT que NO resisten el cotejo

| GPT dice | Lo que dicen los archivos | Consecuencia |
|---|---|---|
| §4: "el paquete activo exige un marcador espejo AAIP en §17.1.11.1 … se perdió … debe recuperarse" | **D-E1-11 fue CERRADA por el usuario el 2026-09-01**: el informe no adjudica la inscripción; el párrafo y los **dos** marcadores se borran; el lado §17.1 se aplicó en v1.7→v1.8 (`cierre-d-e1-11-aaip.md`; kit `01-etapa-1-activa.md` l. 66 y 264: "el espejo de §17.1 ya está borrado"). GPT leyó los tramos históricos del mismo kit (l. 855–1244) que aún dicen "debe viajar". | **No restaurar el marcador.** Hacerlo revierte una decisión firmada y planta la pregunta del jurado sin respuesta. La v1.11 tiene 0 "AAIP": está bien. |
| §1.3: remisiones a "la tabla de métricas de detección", "la tabla de métricas MOT" y "la de rendimiento e instrumentación" | Esas tablas **cayeron en el pase 3 (E2-47)**: `90g` l. 136–137 "D.1 Métricas de detección OVD CAE · D.2 Métricas MOT CAE · D.3 Rendimiento QUEDA como D.1". Hoy el Anexo D es **D.1 rendimiento · D.2 insumos por familia · D.3 bitácora** (verificado en el `.docx`). | El plan de remisiones de GPT apunta a un anexo que ya no existe. Las tres remisiones aplicadas en E4 (D.1 desde viabilidad, D.2 desde aplicabilidad, D.3 desde registro) son las correctas y cumplen la regla E2-47 "cada tabla citada exactamente una vez". **Hallazgo nuevo:** la **Tabla C.2 está citada 0 veces desde el cuerpo** en v1.10 y v1.11 — viola E2-47 desde antes de la v1.11. |
| §3.5: "muchas ecuaciones de la versión anterior eran definiciones estándar de precision, recall, F1, AP y métricas MOT" | Las 76 OMML de la v1.10 eran: 29× `t_alert-system`, 12× `t_alert-notification`, 23 símbolos de componentes, 3× `ΔFP_tracking`, 3× `t_G2A` y **3 ecuaciones** de descomposición. **Ninguna** definía precision, recall, F1, AP ni métricas MOT. | Premisa falsa. Además el relevamiento pidió restaurar **2** ecuaciones, no "decenas": el argumento responde a una posición que nadie sostuvo. |
| §3.2: "calzado, guantes, gafas … ya se tratan al justificar el catálogo en §17.1.2 y §17.1.5" | En la v1.11: **guantes 0 · gafas 0 · calzado 2** (sólo como ejemplo de detalle irresoluble en 17.1.5.1). En §15/16 v1.1: **0 · 0 · 0**. La única frase del informe que excluía guantes y gafas era la de §17.1.6 v1.10, que cayó. | La conclusión de GPT (no repetir) descansa en una premisa falsa. El contenido de B-2 tiene que existir en algún lugar; su ubicación (17.1.6.1 como se aplicó en E7, o 17.1.5.1 junto al ejemplo de calzado, que es donde GPT lo supone) es decisión del usuario. |
| §3.7: "el paquete ya registró que el guardarraíl fue enmendado" | Cierto a medias: **D-P3-1 (2026-08-31)** enmendó el guardrail 2 "**para este pase**" (pase 3) con la condición "**prohibido tocar definiciones, umbrales, reglas o contenido de tablas**". | GPT tiene razón en que no hace falta texto nuevo ni firmar D-1. Pero la enmienda que cita protege precisamente lo que C-1 y C-3 restauran (definiciones). La constancia de la compresión de la v1.11 ya está en §H. |
| §2.5: "no tomaría el resumen de Fable como sustituto del registro o de la fuente oficial" | Los datos del relevamiento **salen del registro** (`download_log.md` con sha256 y fecha, `license_registry.md`, `datasets_metadata.yaml`), que es la fuente verificada del proyecto. GPT no sabía que existe. | Coincidencia de fondo (versión = inventario; fecha = ejecución → §17.4), ya escrita en §B. Pendiente por decisión del usuario. |

### I.2 Criterios editoriales de GPT que SÍ conviene adoptar (corrigen la propuesta del relevamiento)

1. **Símbolos (C-2).** Reusar `t_alert-system` en una suma orientativa después de definirlo como
   diferencia de hitos confunde dos objetos. Razón válida. Corrección: notación separada de
   presupuesto (`B_…` para estimaciones de ingeniería, `W_evidencia` para la espera funcional) o
   una sola oración con la Tabla 29. **Ojo:** el modelo `B` que GPT escribe **omite captura y
   transporte**, así que suma 25–200 ms y no reproduce los 35–250 ms del propio párrafo (que
   incluyen 10–50 ms de `capture_to_host`). Si se adopta, el término `B_captura-host` entra
   condicionado a marca de captura confiable, igual que en E2.
2. **Jerarquía (C-1).** Conservar obligatorio / deseable / conceptual; **no** restaurar
   primario / secundario / transversal (la Tabla 28 ya es la columna vertebral). Razón válida.
   **Dependencia que GPT no vio:** la Tabla 33 dice "métricas primarias calculadas" → debe pasar a
   "métricas obligatorias calculadas". Y el párrafo que GPT propone lleva **punto y coma**: viola la
   regla de prosa nueva del usuario; hay que reescribirlo.
3. **Puente aritmético (C-4).** 2–4 s + 35–250 ms = 2,035–4,25 s, no 3–5 s. La frase de la v1.10 y
   de E2b decía "coherente", no "igual", pero la lectura cualitativa de GPT ("compatible con la
   ventana y con margen para procesamiento y variabilidad") es más honesta. Adoptar. La cláusula de
   recalibración queda (ambos coinciden).

### I.3 Donde GPT y el relevamiento coinciden (sin novedad)

Fila truncada · referencias cruzadas · alineación de G2A en D.1 (E5 ya lo hace; "es D.1" está
verificado en el archivo) · checkpoints (E3) · factibilidad en una oración (C-3) · C-6/C-7 no ·
B-1 no · B-4 no · D-3 sin reabrir · renumerar 33–35 → 31–33 (opción válida; el hueco 18/19 sigue
hasta la integración) · MOT17/OVT-B sólo con entrada bibliográfica verificada.

### I.4 Conflictos con decisiones ya tomadas por el usuario

- **B-2**: usuario sí · GPT no (con premisa falsa). El usuario decide ubicación, no existencia.
- **B-3**: usuario no · GPT sí. TETA / LocA / ClsA / AssA no están definidas en ningún documento
  del informe (§15/16: 0). El relevamiento y GPT coinciden; la decisión sigue siendo del usuario.

### I.5 Efecto sobre la v1.12 (sugerencias sin aceptar)

Si se adoptan I.2: **E1** se recorta (caen las oraciones de primario / secundario / transversal;
se agrega la edición "primarias → obligatorias" en la Tabla 33), **E2** se reescribe con notación
`B`/`W` incluyendo `B_captura-host` condicional (o se reduce a una oración), **E2b** cambia el
puente aritmético por la formulación cualitativa. **E3, E4, E5, E6 y E7 no cambian.** Se puede
regenerar la v1.12 con el mismo instrumento en cuanto el usuario fije I.2 y I.4.

## J. Acta de aplicación (2026-09-03) — v1.13 (sugerencias sin aceptar), reemplaza a la v1.12

**Mandato del usuario:** aplicar como sugerencias, partiendo de la v1.12, las tres correcciones
editoriales de GPT (§I.2), mantener lo ya ajustado, y decidir B-2 y B-3 "según lo que tenga más
sentido y coherencia". La v1.12 no había sido modificada (mismo tamaño y hora de creación), así que
la v1.13 se generó desde la v1.11 con el conjunto revisado: **rechazar todo devuelve la v1.11
exacta** (897/897 párrafos). Archivo:
`E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.13 (sugerencias sin aceptar).docx`.
Instrumento: `herramientas/aplicar_v113_17_1.py`. La v1.12 queda superada.

**Decisiones tomadas por coherencia:**
- **B-2 → sí, pero en 17.1.5.1 y no en 17.1.6.1.** El contenido no existe en ningún otro lugar
  del informe (guantes y gafas: 0 en v1.11 y en §15/16), así que no puede caer. Pero su casa es la
  delimitación del catálogo, donde 17.1.5.1 ya enuncia el criterio de exclusión con el ejemplo del
  calzado. Se extendió esa frase (guantes y gafas como detalle irresoluble) y se agregó una oración
  para las condiciones de escena (pasillos obstruidos, materiales inestables). La inserción en
  17.1.6.1 de la v1.12 se retiró: habría repetido lo mismo dos secciones más adelante.
- **B-3 → sí.** TETA, LocA, ClsA y AssA no están definidas en ningún documento del informe; una tabla
  con acrónimos que el lector no puede resolver es un defecto de coherencia, no una preferencia. Una
  oración en la nota de la Tabla 27, antes del marcador `[[PENDIENTE]]`, que no se tocó.

| # | Sitio | Cambio respecto de la v1.12 |
|---|---|---|
| E1' | 17.1.7.1, **después** del párrafo de los cuatro estados | Un solo párrafo: niveles de compromiso (obligatorio / deseable / conceptual) independientes del estado de aplicabilidad + criterio de exigibilidad en una oración. **Cae la jerarquía primario / secundario / transversal** (GPT §2.1). |
| T33 | Tabla 33, fila Baseline DBE | "métricas primarias calculadas" → "métricas **obligatorias** calculadas" (dependencia que GPT no vio). Ninguna otra mención a "métricas primarias" en el documento. |
| E2' | 17.1.7.5 | Notación propia (GPT §2.2): `B_procesamiento ≈ B_captura-host + B_preprocesamiento + B_inferencia + B_identidad + B_reglas` y `B_alerta ≈ W_evidencia + B_procesamiento`. `B_captura-host` condicionado a marca confiable (sin él, el modelo no reproduce los 35–250 ms). `t_alert-system` **no aparece en ninguna suma**; el párrafo lo dice explícitamente. |
| E2b' | 17.1.7.5, párrafo previo a la Tabla 30 | Compatibilidad cualitativa objetivo ↔ ventana de 17.1.5.2 con margen para procesamiento y variabilidad (GPT §2.4) + cláusula de recalibración por modelo, resolución, cadencia o transporte. **Sin** el puente 2–4 s + 35–250 ms. |
| E3–E6 | Tabla 26 · remisiones D.1/D.2/D.3 · Tabla D.1 "Latencia G2A" · 17.1.3.3 | Sin cambios respecto de la v1.12. |
| E7 | 17.1.6.1 | **Retirado** (va a 17.1.5.1 como B-2'). |
| B-2' | 17.1.5.1, frase "Quedan fuera las condiciones…" | Dos inserciones (ver arriba). |
| B-3 | Tabla 27, nota | Expansión de TETA / LocA / ClsA / AssA antes del `[[PENDIENTE]]`. |

**Medición v1.13:** 905 párrafos (+5) · 22 `w:ins` (5 marcas de párrafo insertado) · 4 `w:del` ·
ids 9101–9126 únicos · 6 ecuaciones · 22 tablas · 38 saltos de sección · 3 comentarios intactos ·
17 partes del zip idénticas byte a byte · 0 dos puntos y 0 punto y coma en la prosa nueva ·
aceptar todo produce exactamente las 17 diferencias de la tabla (16 comprobaciones automáticas en
verde, incluidas "sin `t_alert-system ≈`", "sin nivel primario/secundario", "D.1/D.2/D.3 citadas
una vez").

**Sigue pendiente:** aceptar en Word → v1.13 limpia · mecánicos de §17.1.6 (fila truncada, los
tres `[[PENDIENTE]]`, nota C.3) · **Tabla C.2 sin cita desde el cuerpo** (hallazgo §I.1, previo a
la v1.11) · renumeración 33–35 → 31–33 y hueco 18/19 en la integración · archivar v1.10/v1.11/v1.12
· re-extraer `90f`, kit y nota D-E2-2 del generador · A-1.

## K. Opinión sobre el presupuesto de latencia (v1.13, §17.1.7.5) — cotejo con §17.1.5.2, el pattern set y lo medido

**Veredicto:** el presupuesto tiene sentido y es coherente en su lógica interna y con la escalera de
severidades. Sus costuras están en tres lugares: la relación explícita entre `B_alerta`,
`t_alert-system` y la latencia vidrio→alerta (hay un tramo que ninguna métrica cubre), dos columnas
de la Tabla 30 (SDR como piso; "rango" donde debería decir "máximo") y dos números que el resto de la
tesis usa distinto (50–250 ms del instrumento vs 35–250 ms del protocolo; captura 10–50 ms vs
~200 ms medidos). Nada de eso obliga a retocar el protocolo ex ante; sí obliga a que §17.5 lo
reporte contra él con las palabras correctas.

**Lo que cierra (verificado):**
- Aritmética: 10–50 + 5–20 + 15–150 + 5–20 + <10 = **35–250 ms** ✓.
- Escalera: ventanas de §17.1.5.2 (crítica 2–4 s · alta 3–5 · media 5–10) → objetivos de la Tabla 30
  (3–5 · 5–10 · 10–20) con margen creciente (+1 · +2 a 5 · +5 a 10 s) ✓. Valores de protocolo
  4.000/7.000 ms dentro de sus ventanas ✓ (= `confirm_after_ms` del pattern set oficial; resolve
  2.000/3.000 = histéresis declarada) ✓.
- Empíricamente consistente: `t_alert` medido CR-01 5.236–5.327 ms (ventana 4 s) y CR-02 8.572 ms
  (ventana 7 s) ⇒ TTFD + cola ≈ 1,2–1,6 s, dentro de "TTFD < 3 s alta / < 10 s media" ✓.
- Tabla 29 ↔ modelo B/W: ventana funcional = primera evidencia aceptada → confirmación; evaluación de
  patrón mide cómputo y no la espera ✓. `t_alert-notification` p95 64,5 ms como tramo separado ✓.

**Costuras, por importancia:**
1. **Tres marcos temporales sin puente explícito.** `t_alert-system(e)` va del inicio anotado al
   **timestamp de fuente del cuadro confirmante**; `B_alerta` va de la **primera evidencia** a la
   **alerta disponible** (wall-clock). Difieren al inicio por TTFD y al final por la cola del cuadro
   confirmante (`capture_to_host` + `t_G2A` + evaluación ≈ 0,25–1,1 s en vivo). Ese tramo de cierre
   no lo cubre ninguna métrica: `t_alert-notification` arranca en la publicación. Falta una oración
   (o una fila en la Tabla 29, "cierre de alerta"): vidrio→alerta ≈ TTFD + W_evidencia +
   B_procesamiento; `t_alert-system` ≈ TTFD + W, sin la cola, que se reporta con `capture_to_host` y
   `t_G2A`. Es la generalización de F-101.8 (el inventario ya lo dice: "vidrio→alerta =
   capture_to_host + G2A + política").
2. **SDR como "referencia mínima" por severidad (≥ 0,50 / 0,60 / 0,70).** La confirmación es una
   ventana sostenida con histéresis, no exige proporción: CR-02 llegó a recall 1,000 con **SDR
   0,281**. Y el propio §17.1.7.3 dice que SDR sólo se compara a cadencia igual (F-96.6: sube al bajar
   la densidad). Un piso fijo por severidad es un criterio que el motor no implementa y que la
   cadencia desestabiliza. Mejor "SDR esperada (descriptiva)" o sacar la columna; SDR ya vive como
   evidencia de estabilidad en §17.1.7.3.
3. **"Rango objetivo orientativo" vs "máximo".** La v1.10 decía "máximo orientativo". Con "rango",
   el CR-02 medido (8,6 s) queda **fuera por rápido** del 10–20 s. Una palabra.
4. **Realismo de las bandas frente a la plataforma.** Captura+transporte 10–50 ms (LAN/RTSP de
   literatura) vs `capture_to_host` **202–217 ms** en el rodaje (169 humo · 1,6 s degradado);
   inferencia 15–150 ms vs `inf p50` **432–567 ms** del campeón (G2A p95 630–890) y 112–118 ms de
   YOLOE (225–249). El protocolo es honesto como banda ex ante, pero conviene explicitar su supuesto
   ("detectores de la familia eficiente; una arquitectura transformer a 560 px puede excederla y la
   desviación se reporta") para que §17.5 lea la tensión calidad↔latencia como hallazgo y no como
   incumplimiento. La cláusula de recalibración de E2b' ayuda.
5. **Dos números para "el presupuesto".** Doc 39, `inventario-de-metricas` y el índice de
   `results/realtime` verifican G2A contra **50–250 ms** (`p95_within_budget`); §17.1 dice
   **35–250** para el tramo previo a la acumulación (que incluye captura). Además el G2A
   instrumentado de la Tabla 29 (dequeue → fin de inferencia) debería compararse con
   pre+inf = 20–170 ms, no con 50–250. Reconciliar en la integración (§17.4/§17.5 deben mapear su
   50–250 a la descomposición de §17.1).
6. **TTFD < 1 s para crítica vs cadencia live** (1,16–4,42 fps ⇒ período 0,23–0,86 s + G2A 0,6–0,9 s).
   Inalcanzable con el campeón en vivo; latente porque el núcleo no tiene patrones críticos.

**Si se quiere cerrar con sugerencias mínimas (v1.14):** (a) oración-puente de 1 en 17.1.7.5 tras
`B_alerta` [+ fila "Cierre de alerta" en Tabla 29]; (b) Tabla 30: encabezado "Máximo orientativo" y
columna SDR a "SDR esperada" o fuera; (c) oración de supuesto de familia eficiente junto al
35–250; (d) nota para la integración: 50–250 ↔ 35–250.

## L. Acta de aplicación (2026-09-03) — v1.14 (sugerencias sin aceptar), reemplaza a la v1.13

**Mandato:** de los cuatro toques de §K, el usuario aceptó aplicar los dos que cierran agujeros sin
mover umbrales pre-registrados (§K a y b-encabezado); se dejan a propósito el piso de SDR (sería
retocar el protocolo después de ver el 0,281), el supuesto de familia eficiente (ya está dicho como
"modelos orientados a inferencia eficiente"; la tensión nace en §17.5) y el 50–250 ↔ 35–250 (va a la
integración). Archivo: `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.14 (sugerencias sin
aceptar).docx`; instrumento `herramientas/aplicar_v114_17_1.py` (parte de la v1.11, como los
anteriores). La v1.13 queda superada.

| # | Sitio | Cambio respecto de la v1.13 |
|---|---|---|
| P-1 | 17.1.7.5, párrafo que mapea los símbolos del modelo B/W (inserción E2') | Dos oraciones nuevas antes de la frase de cierre: "La latencia vidrio a alerta de un episodio se aproxima entonces a la suma de TTFD y B_alerta. t_alert-system, medida entre hitos del reloj de la fuente, comprende la reacción perceptiva inicial y la ventana funcional, pero no la cola de procesamiento del cuadro que confirma, que se informa por separado mediante capture_to_host y t_G2A." — cierra la costura §K.1 (tres marcos temporales sin puente). |
| T30 | Tabla 30, encabezado de la 2.ª columna | "Rango objetivo orientativo de t_alert-system" → "**Máximo** orientativo de t_alert-system" (1 del + 1 ins). Restaura la semántica de la v1.10; evita leer el 8,6 s de CR-02 como fuera de objetivo por rápido (§K.3). |
| resto | E1', T33, E2', E2b', E3–E6, B-2', B-3 | Idénticos a la v1.13. |

**Medición v1.14:** 905 párrafos (+5) · 23 `w:ins` · 5 `w:del` · ids 9201–9228 únicos · 6 ecuaciones ·
22 tablas · 38 saltos de sección · 3 comentarios intactos · 17 partes del zip idénticas byte a byte ·
**rechazar todo == v1.11** · aceptar todo difiere de aceptar-todo-v1.13 exactamente en los 2
párrafos de la tabla · prosa nueva sin dos puntos ni punto y coma.

**Sigue pendiente (sin cambios):** aceptar en Word → v1.14 limpia · mecánicos de §17.1.6 · Tabla C.2
sin cita desde el cuerpo · renumeración y huecos en la integración · reconciliar 50–250 (doc 39,
inventario, `results/realtime`) con 35–250 (§17.1) en §17.4/§17.5 · archivar v1.10–v1.13 ·
re-extraer `90f`/kit · A-1.
