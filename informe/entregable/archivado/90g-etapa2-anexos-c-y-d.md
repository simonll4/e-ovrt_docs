# 90g — Etapa 2: Anexos C y D finales (se anexan al final del documento de la etapa)

> ✎ **2026-09-03 — HISTÓRICO.** Los Anexos C y D ya están pegados y cerrados en la versión final
> (`desarrollando/…v1.15.docx`, Anexo C con C.1–C.3 y Anexo D con D.1–D.3). Este documento conserva
> **la decisión de entonces** sobre qué tablas quedaban y por qué, y **no se actualiza**. Dos
> advertencias al leerlo: (a) toda la numeración de secciones que cita (§17.1.4.4.2, §17.1.5.4.4,
> §17.1.6.2.1, §17.1.6.4.2, §17.1.7.4.x, §17.1.7.8.x, §17.1.7.9…) **cambió** — traducción en
> [`desarrollando/mapa-secciones-17-1-v1-15.md`](../desarrollando/archivado/mapa-secciones-17-1-v1-15.md); (b) la
> "Tabla 31" que menciona como vista vigente de cobertura es hoy la **Tabla 25**. Las notas de las
> tres tablas del Anexo C se reescribieron en la v1.15 (más cortas, sin "Fuente:" y con las
> remisiones vivas), y la Tabla C.2 dejó de estar huérfana: la cita **§17.1.4.2**.

> **Qué es.** El contenido **final y completo** de los Anexos C y D de la Etapa 2, listo para
> pegar. **Decisión del usuario 2026-08-31 (D-P3-8): los anexos viajan AL FINAL del documento de
> trabajo de la etapa** (`…Seccion_17.1_…` → v1.4) — los agrega ChatGPT con la unidad **E2-49**
> del pase 3, y al integrar al maestro el equipo los muda a §19.3/§19.4. Esto supersede la mitad
> "quedan fuera del `.docx`" de D-E2-1; la otra mitad (se corrigen aparte, con constancia) es este
> archivo. Base: los anexos del informe v1.1 (`96e` §19.3/§19.4), que ningún pase había tocado.
> Ejecuta las notas ✎ de **AJ-2.07**, la duplicación verificada **H-8** (`ajustes/09` §4) y la
> decisión **D-P3-5** del pase 3.
>
> **Qué cambió respecto del v1.1:** Anexo C **5 → 3 tablas** · Anexo D **6 → 3 tablas**. Bajas y
> motivos en §1 y §2. Efecto neto sobre el informe: **−7 tablas** (contando las 2 del desarrollo
> que elimina el pase 3).
>
> **⚠ Convenciones al pegar:**
> - Títulos de anexo **sin número** en este documento: *"Anexo C — Prompts, datos, datasets,
>   benchmarks y logística"* y *"Anexo D — Métricas, instrumentación y bitácora experimental"*,
>   con el **mismo estilo de encabezado que el título "17.1. Consolidación metodológica…"** (la
>   numeración 19.3/19.4 es del maestro y se asigna al integrar; un número acá rompería la
>   verificación de numeración del documento).
> - Rótulos según la casa: `**Tabla C.1**` (negrita), título de tabla en itálica, `*Nota.*` en
>   itálica.
> - **Nombres de métrica en las tablas del anexo: texto plano** (t_alert-system, latencia G2A…),
>   como TTFD y SDR. La unificación con los objetos de ecuación del cuerpo queda para el pase de
>   integración (residual ya fichado — mismo caso que el t_alert-system en texto de §17.1.7.2).
> - Guardas de contenido (AJ-2.07 ✎ y R-24): los anexos hablan **sólo de candidatos y
>   retenidos** — nunca de "utilizados" ni del entrenamiento efectivo (eso es §17.4);
>   **`bench_obra` no se introduce** (no es un dataset: es un estrato curado internamente);
>   las licencias, como figuran en el registro.
>
> Las remisiones del cuerpo de §17.1 a estas tablas las actualiza **E2-47** del pase 3
> (C.1 · C.2 · C.3 · D.1 · D.2 · D.3 — cada una queda citada exactamente una vez desde el
> desarrollo).

---

## 1. Anexo C — qué queda, qué cae y por qué

| Tabla v1.1 | Destino | Motivo |
|---|---|---|
| C.1 Catálogo de prompts candidatos | **QUEDA como C.1, sin cambios** | Ancla del anexo: fuente declarada del prompt set (AJ-2.07); §17.1.5.4.4 la cita. |
| C.2 Variables de sensibilidad EBE | **QUEDA como C.2, sin cambios** | Diseño experimental pre-registrado. Estaba huérfana; E2-47 le da la remisión desde §17.1.4.4.2. |
| C.3 Síntesis de cobertura conjunta | **CAE** | Huérfana y **contradice al desarrollo v1.3**: cuenta 7 fuentes para CR-01 incluyendo descartadas y da cobertura "Parcial" a CR-05/CR-06 vía SODA/MOCS, contra la Tabla 31 del desarrollo (4 retenidas, "sin cobertura directa retenida"); su nota cita "la Tabla 27", que hoy es otra tabla. La vista vigente de cobertura es la Tabla 31. |
| C.4 Compatibilidad de formato (9 datasets) | **CAE** | Huérfana; reintroduce los 5 descartados que PODA-12 podó. Para las retenidas: columna "Formato" de la Tabla 26 + la nueva C.3. |
| C.5 Volúmenes estimados (9 datasets) | **SE REESCRIBE como C.3** | Material de planificación de fuentes nunca gestionadas; queda la logística de las 4 retenidas, sin cifras que el registro no respalde. |

### Contenido final del Anexo C (pegar tal cual)

---

**Anexo C — Prompts, datos, datasets, benchmarks y logística**

**Tabla C.1**

*Catálogo de prompts candidatos por condición de riesgo*

| Código | Eje de variación | Prompt candidato (inglés) | Estrategia |
| --- | --- | --- | --- |
| CR-01 | Sintáctica | person without hard hat | Frase nominal con negación explícita |
| CR-01 | Especificidad | construction worker without safety helmet | Términos específicos del dominio |
| CR-01 | Estado observable | person with bare head on construction site | Estado resultante, sin negación directa |
| CR-01 | Template | a photo of a hard hat | Template estándar CLIP para detección de presencia |
| CR-01 | Indirecta | hard hat ; person | Detección separada de entidades; relación evaluada externamente |
| CR-02 | Sintáctica | person without reflective vest | Frase nominal con negación |
| CR-02 | Especificidad | worker without high-visibility vest | Vocabulario técnico de seguridad |
| CR-02 | Descripción visual | person without bright colored safety clothing | Descripción visual del atributo ausente |
| CR-02 | Template | a photo of a reflective safety vest | Template estándar CLIP |
| CR-02 | Indirecta | reflective vest ; person | Detección separada de entidades |
| CR-03 | Sintáctica | person on scaffolding without harness | Contexto espacial + negación |
| CR-03 | Especificidad | worker at height without fall protection equipment | Vocabulario técnico ampliado |
| CR-03 | Descompuesta | person on scaffolding ; safety harness ; fall arrest harness | Detección separada de persona en altura y elementos de protección |
| CR-03 | Estado observable | unprotected worker on elevated platform | Estado resultante sin negación explícita del EPP |
| CR-04 | Sintáctica | unprotected edge with person nearby | Entidad compuesta: borde + persona |
| CR-04 | Especificidad | elevated platform without guardrail near workers | Términos de protección colectiva |
| CR-04 | Descompuesta | platform edge ; guardrail ; safety railing ; person at height | Detección de borde, protección colectiva y persona |
| CR-05 (a) | Entidades maquinaria | excavator ; backhoe loader ; dump truck ; crane ; heavy machinery | Entidades de maquinaria a detectar individualmente |
| CR-05 (b) | Entidades humanas | person ; construction worker ; pedestrian | Entidades humanas a detectar individualmente |
| CR-06 (a) | Entidad persona | person ; worker ; pedestrian | Entidad cuya posición se evalúa contra el polígono |
| CR-06 (b) | Elementos auxiliares | restricted area sign ; caution tape ; warning tape ; barrier ; safety cone | Elementos delimitadores de referencia visual |

*Nota.* Las estrategias "Indirecta" y "Descompuesta" utilizan el separador ";" como notación
analítica para indicar consultas independientes al modelo OVD; su materialización concreta depende
de la sintaxis admitida por cada detector. Las variaciones "Template" utilizan formulaciones tipo
"a photo of a [CLASS]", alineadas con prácticas habituales de uso de modelos visión-lenguaje
preentrenados como CLIP. Para CR-05 y CR-06, al tratarse de condiciones de Nivel 3, no se formulan
prompts integrados sino prompts de entidades componentes; la evaluación de la condición completa se
realiza en el módulo de razonamiento contextual. En particular, los elementos auxiliares de CR-06
no reemplazan la definición externa del polígono de zona restringida, sino que pueden funcionar
como referencias visuales complementarias para experimentos o análisis cualitativo. Fuente:
Elaboración propia basada en los ejes de variación de la Sección 17.1.5.4.2 y en los hallazgos de
Zhou et al. (2022), Du et al. (2022), Gu et al. (2021) y Radford et al. (2021).

**Tabla C.2**

*Variables de sensibilidad candidatas para el Environment-Based Evaluation*

| Variable | Niveles o condiciones retenidas | Uso dentro del protocolo |
| --- | --- | --- |
| Iluminación | Controlada; mixta; natural cuando el entorno lo permita. | Define condición base y barridos univariados de sensibilidad. |
| Resolución de fuente | 1280 × 720 como base; 1920 × 1080 como variante de sensibilidad si la configuración lo permite. | Estima el costo-beneficio entre visibilidad, carga computacional y estabilidad del pipeline. |
| Distancia cámara-sujeto | Rangos a cerrar en instancia de análisis y diseño arquitectónico según campo visual y tamaño aparente; guía inicial: 5-10 m y 10-20 m. | Permite observar el efecto de escala de objeto sin fijar una geometría de cámara antes del diseño del EBE. |
| Oclusión | Baja y media; la oclusión severa no se adopta como obligación de aceptación. | Tensiona la robustez sin convertir la campaña en irreproducible. |
| Tracker | Deshabilitado y habilitado cuando aplique. | Permite medir el aporte del tracking a estabilidad, persistencia y reducción de falsas alarmas. |
| Matriz de prompts | Conjunto acotado de variantes por condición. | Permite seleccionar y congelar el prompt primario antes de las corridas comparativas finales. |
| Composición del vocabulario activo | Configuraciones pequeñas y medianas, explícitamente documentadas. | Permite medir si la cantidad y tipo de consultas activas impacta precisión, latencia o ambas. |

*Nota.* El EBE se organiza de manera secuencial: condición base, barridos de sensibilidad y prueba
de mayor exigencia sobre la mejor configuración retenida. Los niveles consignados son candidatos de
diseño y deberán cerrarse al definir la topología y el espacio físico de prueba.

**Tabla C.3**

*Logística de conversión y acceso de los datasets retenidos*

| Dataset | Formato nativo | Formato de trabajo | Vía de acceso | Observación |
| --- | --- | --- | --- | --- |
| SHEL5K | Pascal VOC | COCO/ODVG y/o YOLO | Mendeley Data | Conversión directa VOC→YOLO; para el pipeline de Grounding DINO, VOC→COCO→ODVG. |
| CHV | Formato nativo a inspeccionar | COCO/ODVG y/o YOLO | Repositorio del autor | Revisar estructura del paquete y términos de uso al descargar; cita obligatoria. |
| construction_site_safety | YOLO (Roboflow) | COCO/ODVG y/o YOLO | Roboflow | Requiere conversión YOLO→COCO→ODVG para el pipeline de Grounding DINO. |
| ppe_siabar | YOLO (Roboflow) | COCO/ODVG y/o YOLO | Roboflow | Requiere conversión YOLO→COCO→ODVG para el pipeline de Grounding DINO. |

*Nota.* La secuencia de gestión —descarga, verificación de integridad, inspección y conversión de
formato, partición conforme a las condiciones metodológicas y transferencia del split de
entrenamiento al nodo de entrenamiento cuando corresponda— se describe en la Sección 17.1.6.4.2.
Los volúmenes y versiones por fuente se consignan en la tabla de datasets retenidos de la Sección
17.1.6.2.1. El esfuerzo de conversión se clasifica como directo (un paso) o en dos pasos
(inspección o normalización previa y conversión al formato de trabajo).

---

## 2. Anexo D — qué queda, qué cae y por qué

| Tabla v1.1 | Destino | Motivo |
|---|---|---|
| D.1 Métricas de detección OVD | **CAE** | Contenido completo en la prosa de §17.1.7.4.1 y la Tabla 34; su único aporte (citas) vive en el primer párrafo de §17.1.7.9. |
| D.2 Métricas MOT | **CAE** | Ídem: prosa de §17.1.7.4.2 + Tabla 34; la unidad de conteo del FP vive en §17.1.7.8.3. |
| D.3 Rendimiento del pipeline | **QUEDA como D.1, sin cambios** | Única con detalle que el desarrollo no lleva (formato de reporte, criterio de estabilidad por métrica). |
| D.4 Umbrales por severidad | **CAE** | ≡ Tabla 35 del desarrollo (**H-8 verificado**); lo que "agrega" ya está en la Tabla 24 y en §17.1.7.7.6. Refina D-E2-1: no queda nada que reducir. |
| D.5 Insumos por familia | **SE REESCRIBE como D.2** | Aporta el mapeo familia→GT→instrumentación→herramientas. **Bug verificado**: la familia "Alerta" aparecía en DOS filas casi idénticas — fusionadas en una. |
| D.6 Bitácora experimental | **QUEDA como D.3, sin cambios** | Estaba huérfana; E2-47 le da la remisión desde §17.1.7.8.4. |

### Contenido final del Anexo D (pegar tal cual)

---

**Anexo D — Métricas, instrumentación y bitácora experimental**

**Tabla D.1**

*Métricas de rendimiento del pipeline y uso de recursos*

| Métrica | Definición operativa | Formato de reporte | Compromiso | Criterio de estabilidad |
| --- | --- | --- | --- | --- |
| FPS efectivos | Cuadros completamente procesados por segundo al final del pipeline. | Media, P50, P95, P99 y variación | Obligatorio | Período de calentamiento previo y corrida sostenida |
| Latencia G2A | Intervalo entre captura o lectura del cuadro y disponibilidad del resultado de inferencia. | ms (P50, P95, P99) | Obligatorio | Timestamps monotónicos |
| Jitter | Variabilidad de la latencia entre cuadros consecutivos. | ms (desv. est. / coef. variación) | Deseable | Reportar junto con G2A |
| Uso de VRAM | Memoria de video ocupada por modelo, tensores y buffers. | MB y % | Obligatorio | Sin crecimiento monótono |
| Utilización GPU | Porcentaje de ocupación de la GPU durante la corrida. | % | Deseable | Registrar media y picos |
| Uso de RAM/CPU | Consumo de memoria del sistema y presión sobre CPU del proceso completo. | MB/GB y %CPU | Deseable | Registrar serie temporal |

*Nota.* G2A = Glass-to-Algorithm. FPS = Frames Per Second. VRAM = Video Random Access Memory. El
reporte obligatorio mínimo incluye FPS efectivos, latencia G2A y uso de VRAM. Cuando sea posible,
conviene registrar además GPU, RAM y CPU con muestreo periódico durante una corrida sostenida.

**Tabla D.2**

*Insumos mínimos requeridos antes de iniciar una campaña de medición*

| Familia de métricas | Ground truth o insumo | Instrumentación mínima | Herramientas o artefactos | Salida mínima |
| --- | --- | --- | --- | --- |
| Detección (AP, P/R) | Bounding boxes y etiquetas por imagen o cuadro. | Export de predicciones por corrida. | pycocotools o conversión COCO equivalente. | AP y P/R por variante, con punto operativo o criterio de reporte explícitamente declarado. |
| Tracking (HOTA, DetA / AssA, IDF1, MOTA, IDSW / Frag) | Boxes y track_id persistente por cuadro. | Export MOT-compatible sobre subset anotado. | TrackEval u otra implementación equivalente. | Métricas MOT sobre subset, con declaración explícita de qué métricas fueron ejecutadas y cuáles no. |
| Pipeline (FPS, latencia G2A, jitter) | No requiere GT semántico. | Timestamps por etapa del pipeline. | Logs internos y scripts de agregación. | P50/P95/P99, promedio y variación. |
| Alerta y patrón (t_alert-system; t_alert-notification si aplica; TTFD; SDR) | Inicio anotado de la condición de riesgo, duración o intervalo temporal del evento, severidad asignada y criterio de activación del patrón. | Logs con timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y disponibilidad, consulta o notificación si aplica. | Motor de evaluación de patrones instrumentado; registro interno de alertas; event log del pipeline; bitácora de corrida; scripts de agregación temporal. | TTFD, SDR y t_alert-system por evento; t_alert-notification sólo si existe trayecto instrumentado; toda métrica sin insumos se declara no aplicable. |
| Recursos (VRAM, GPU, RAM, CPU) | No requiere GT semántico. | Muestreo periódico durante la corrida. | nvidia-smi, psutil u otras herramientas del sistema. | Series temporales y resumen. |
| Fine-tuning | Split train/eval disjunto y baseline zero-shot explícita. | Registro de entrenamiento y evaluación. | Logs de entrenamiento y scripts comparativos. | Deltas y costo de entrenamiento, cuando aplique. |

*Nota.* La ausencia de cualquiera de los insumos requeridos para una familia de métricas debe
declararse antes de planificar la campaña experimental. En particular, no corresponde reemplazar
ground truth inexistente por estimaciones informales ni interpretar logs incompletos como evidencia
suficiente de desempeño. Toda métrica sin insumos mínimos deberá registrarse como no ejecutada o no
aplicable, según corresponda.

**Tabla D.3**

*Campos mínimos recomendados para la bitácora experimental*

| Campo | Contenido mínimo recomendado | Uso en la interpretación |
| --- | --- | --- |
| Identificación | Fecha, nombre de la corrida, responsable y objetivo. | Permite rastrear la prueba. |
| Modelo | Nombre, versión, checkpoint y variante zero-shot o fine-tuned. | Vincula resultados con artefactos concretos. |
| Entrada | Dataset o clip, resolución, FPS de origen y protocolo de video. | Contextualiza comparaciones. |
| Parámetros | Umbral, vocabulario activo, NMS, tracker on/off, ventana de persistencia, criterio de activación/desactivación del patrón e histéresis si aplica. | Hace reproducible la corrida y permite interpretar la confirmación o descarte de patrones. |
| Hardware | CPU, GPU, VRAM, RAM y equipo o nodo utilizado. | Permite interpretar latencia y uso de recursos. |
| Entorno de software | Sistema operativo, versiones de runtime, framework, librerías críticas y herramientas de instrumentación. | Permite reproducir la corrida y contextualizar diferencias de rendimiento o compatibilidad. |
| Temporalidad y logs | Fuente temporal declarada, período de calentamiento, duración efectiva de la corrida, ubicación de logs crudos y artefactos de evaluación. | Permite validar trazabilidad temporal y auditar métricas derivadas del pipeline y de alerta. |
| Eventos de patrón y alerta | Timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y notificación o consulta si aplica; identificador del patrón y regla aplicada. | Permite reconstruir por qué y cuándo una detección se transformó en patrón confirmado y alerta registrada. |
| Resultados | Métricas calculadas, unidades y métricas no ejecutadas. | Consolida la salida cuantitativa. |
| Observaciones | Errores, cuellos de botella y cambios no planificados. | Evita lecturas descontextualizadas. |

*Nota.* Una métrica sin contexto de corrida pierde interpretabilidad y trazabilidad.

---

## 3. Verificación (sobre la v1.4, tras aplicar E2-49)

1. El documento cierra con **dos encabezados sin número** ("Anexo C — …", "Anexo D — …") del
   mismo estilo que el título de §17.1, después de §17.1.11.2.
2. Exactamente **3 tablas C.x** y **3 tablas D.x**, rotuladas `**Tabla C.1**` … `**Tabla D.3**`,
   cada una con su título en itálica y su `*Nota.*`.
3. Cada tabla de anexo aparece citada **exactamente una vez** desde el desarrollo (E2-47) y
   rotulada una vez en el anexo.
4. Cero apariciones de: la síntesis de cobertura vieja ("7" fuentes para CR-01) · la tabla de
   compatibilidad de 9 datasets · los umbrales del anexo (ex-D.4) · las tablas de métricas
   OVD/MOT del anexo (ex-D.1/D.2) · volúmenes de SH17/SODA/MOCS · `bench_obra` · "utilizados".
5. Dos cambios de texto respecto del v1.1 dentro de las tablas conservadas, y sólo esos:
   "por frame" → "por cuadro" en la fila Tracking de D.2 (terminología F5) y
   "(FPS, latencia G2A, jitter)" en la fila Pipeline de D.2 (el nombre iba como objeto de
   ecuación en el maestro; acá va como texto — ver convención del banner).
