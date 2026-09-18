# Pase de la Etapa 6 — §17.6, §18 y §19 · v1.2 → v1.3

> **Entregado el 2026-09-12 como SUGERENCIAS Y COMENTARIOS.** Nada en limpio: rechazar todas
> las sugerencias devuelve la v1.2 exacta (verificado).
> Guion: [`herramientas/pase_etapa6_v13.py`](../../../../herramientas/archivado/pase_etapa6_v13.py) ·
> Documento: `E-OVRT-VDP_Etapa_6_Secciones_17.6_18_19_v1.3 (sugerencias sin aceptar).docx` ·
> Lectura previa, hilo por hilo: `analisis-comentarios-etapa6-v1.2-2026-09-12.md`.

Punto de partida: la v1.2 que bajaste de Google Docs (sha `45157574…`; todas las sugerencias de
la v1.1 aceptadas, sin la lista de Referencias, 14 hilos de comentarios tuyos). Las siete
decisiones que tomaste sobre el análisis gobiernan este pase.

---

## 1. Los 14 hilos, uno por uno

| Hilo | Dónde | Qué se hizo |
|---|---|---|
| H01 repos | 17.6.1 | Una oración al final del ¶1: los cinco repos son públicos y se reúnen en el **repositorio de documentación** `https://github.com/simonll4/e-ovrt-vdp`, «vía de acceso a todo el material que este informe identifica». Se cita una sola vez; los cinco no se citan uno por uno. La URL va inline porque es un punto de acceso; si preferís APA estricto se quita de ahí y queda sólo en la entrada de referencias (§3). |
| H02/H03 «¿qué suma?» | 17.6.3 ¶3–4 | Fundidos en **un** párrafo concreto: qué recalcula cada comprobación automática (cifras contra artefactos: 26 cifras sobre 17 campañas; organización del material de video), el banco reproducido byte a byte, la relectura determinista, y el límite (no sustituye repetir la inferencia en otro equipo). Si igual no te convence, rechazás y se borra: nada depende de él. |
| H04 dockerizado | 17.6.4 ¶2 · 18.6 · Anexo E | **Desarrollado en afirmativo, sin declarar pendientes** (decisión del usuario: el build y el arranque integral son tarea interna del equipo, no estado del informe). El párrafo describe lo que existe: los cuatro archivos de construcción, la composición de trece servicios con redes, volúmenes, comprobaciones de salud y dependencias, el arranque diferido de las instancias de inferencia, la paridad de rutas y la resolución por nombre de servicio. **No afirma una portabilidad medida sobre un tercer equipo**, porque eso sería un resultado. Arrastre: el camino «Portabilidad» de §18.6 pasa a **«Despliegue permanente en obra»** (una instalación en producción, no una deuda), y el «Alcance» del Anexo E convierte el empaquetado en la **respuesta** a la pregunta de entorno en vez de en una salvedad. |
| H05 archivos y Drive | 17.6.4 ¶3 · Anexo E ¶1 · Anexo F ¶1 | El **punto de entrada único**: el informe remite al repositorio de documentación; el material audiovisual «se conserva con acceso autorizado y se solicita a los autores por esa misma vía». La URL de la carpeta de Drive **no** va en el informe: va en el repositorio, en la sección «Material audiovisual y evidencia cruda: acceso autorizado», cuando la armes. |
| H06 hipótesis literal | 18.1 | Párrafo nuevo tras el ¶1: las dos consultas de ejemplo de §12.3 («persona sin casco», «persona sin chaleco reflectivo») se transformaron en alertas evaluables, con los dos matices: no como negación literal (descartada por precisión) sino como ausencia sobre una persona detectada; CR-01 sostenida en los tres niveles, CR-02 con la clasificación por persona abierta. |
| H07 F1 vs AP | 18.1 ¶2 · 18.2 ¶1 | Oración al final del ¶2: el AP compara detectores sobre imágenes y vive en §17.5.2; la alerta por episodio es una decisión binaria y se mide con precisión/recall/F1, fijado en §17.1.7. En 18.2 ¶1 se citan las cifras: 0,503 vs 0,474 en el núcleo, 0,551 vs 0,525 en el banco completo. |
| H08 `machinery` | 18.2 | Dicho: clase ajena al núcleo, maquinaria de obra, agregada por configuración para el piloto de extensibilidad, AP50 0,662 sobre 99 cajas; `vehicle` fue la segunda palabra probada y el modelo la resolvió sobre la misma maquinaria. |
| H09 «me perdí» | 18.3 ¶5 | Reescrito: dice de entrada que es **otro nivel** (estado por persona, cuadro a cuadro, sin motor temporal), sobre 17 clips de obra real, F1 0,031 / 0,018, y por qué cayó (precisión < 0,02: predicciones sobre personas cuyo estado el anotador no podía determinar). |
| H10 presupuesto | 18.4 ¶1 | Con cifra: §17.1.7 estimó **hasta 250 ms por unidad**; medido 630–890 ms p95, **2,5 a 3,6 veces**; la plataforma sin detector resolvió el tramo en 31,8 ms p95, así que el exceso es del modelo. No se agregó YOLOE en vivo (entra en presupuesto pero no reconoce la condición) porque esa cifra no está en §17.5. |
| H11 30 fps | 18.4 ¶3 | Dicho antes de la serie: 30 fps es la cadencia completa del material grabado, evaluado en diferido; el vivo entregó 1,16–4,42 fps; el remuestreo cubre esa franja. |
| H12 §18.5 | 18.5 | Seis párrafos → **cuatro**: qué fue la rama (con los **tres tramos numerados y definidos una vez**), qué pasó en cada uno, qué significa, cierre. 535 → 457 palabras. Todas las cifras y veredictos conservados (Tabla 66, §17.5.6); salió la oración sobre la latencia no medida (ya está en 17.5.7). Absorbe la regresión «No implica» → «no implican». |
| H13 continuidades | 18.6 ¶4–5 · 18.3 ¶1 | **Dos párrafos, con el encuadre del diseño y no del traspaso.** No dicen «queda una base para que otro siga», sino que **la plataforma se diseñó para el catálogo completo y se validó sobre su núcleo obligatorio**, que es la afirmación fuerte y la que el informe ya sostiene con su propio vocabulario: 17.1 retiene seis condiciones en tres niveles, llama a CR-01 y CR-02 «núcleo obligatorio de validación» y a las demás «extensiones condicionadas»; 17.3 separa capacidades de «núcleo» de las «complementarias previstas» y declara que el motor admite el catálogo completo de patrones. Las dos frases que ordenan el bloque: **el recorte fue de la validación, no del diseño**, y **lo que falta es evidencia, no arquitectura**. Las versiones con seis caminos desarrollados y con lista quedaron descartadas por extensión. **Dos ambigüedades corregidas en el camino:** decía «el tracker está implementado» sin dejar claro si existía, y ahora la identidad temporal figura como **implementada y medida** (17.5.7: «la exclusión no alcanzó a la capacidad de identidad temporal, que sí fue implementada y medida por su efecto sobre la alerta»), con las métricas de seguimiento multiobjeto como lo único ausente, por falta de identidades anotadas; y §18.3 ¶1 llamaba «evaluación MOT del tracker» a esa misma ausencia, que ahora se nombra como en 17.5.7. «Tracker» queda sólo en dos tablas de anexos heredados. El párrafo del aporte final queda último, sin cambios. |
| H14 Anexo E | 19.5 | Sin nombres de archivo ni comandos. Tabla E.1: dos celdas sin `.json`/`clip_gt.v2`. **Tabla E.2: sólo las dos huellas completas** (banco de imágenes `4557024e…a4462`, manifiesto del banco temporal `3f14f50a…01a75`; ambas verificadas hoy contra disco); las siete abreviadas se van. La prosa: ocho párrafos → **seis pasos con entrada en negrita** (banco de imágenes · banco temporal · relectura y evaluación · agregación · repetición en vivo · alcance). 1.181 → 1.068 palabras. |

## 2. Efecto en el tamaño

| Bloque | v1.2 | v1.3 | Δ |
|---|---:|---:|---:|
| §17.6 | 1.130 | 1.281 | +151 |
| §18.1 | 324 | 472 | +148 |
| §18.2 | 494 | 546 | +52 |
| §18.3 | 532 | 566 | +34 |
| §18.4 | 375 | 449 | +74 |
| §18.5 | 526 | 448 | −78 |
| §18.6 | 563 | 578 | +15 |
| Anexo E | 1.170 | 1.073 | −97 |
| Anexo F | 833 | 881 | +48 |
| **Total (sin Referencias)** | **10.497** | **10.844** | **+347 (+3,3 %)** |

Crece donde pediste claridad —la hipótesis literal, el presupuesto con su cifra, el empaquetado
desarrollado en afirmativo— y baja donde pediste legibilidad: §18.5 y el Anexo E. Las continuidades
de §18.6 quedaron en la extensión que tenían, con otro contenido.

## 3. Entrada de referencias (para la integración)

La v1.2 no trae la lista, así que la alta va acá y se pega al integrar, en su lugar alfabético:

> Carrizo, M. L., Guillaumet, G. A., y Llamosas, S. (2026). *E-OVRT-VDP: Plataforma experimental de
> detección open-vocabulary en video en tiempo real para monitoreo asistivo de riesgos en
> construcción* [Repositorio de documentación]. GitHub. https://github.com/simonll4/e-ovrt-vdp

Cita en el cuerpo: «(Carrizo, Guillaumet y Llamosas, 2026)», una vez, en 17.6.1.

## 4. Compuertas

| Compuerta | Resultado |
|---|---|
| Rechazar todas las sugerencias devuelve la v1.2 | ✅ texto idéntico (64.154 caracteres), 18 tablas, 735 párrafos |
| Integridad OPC del paquete | ✅ íntegro |
| Anclas de comentario | ✅ los 15 previos conservados; 16 nuevos: uno por hilo (H02/H03 comparten el suyo; H14 lleva tres) más el del arrastre de vocabulario en §18.3 |
| `verificar_entregable.py` | 3 fallas, **las tres conocidas y falsas**: «§17 arranca en 6» (esperable en un `.docx` por sección) y las dos huellas SHA-256 completas de la Tabla E.2, que el verificador confunde con andamiaje del kit (falso positivo ya anotado el 09-09; hay que aflojarle el patrón) |
| Extracción de la vista aceptada | ✅ sin nombres de archivo ni comandos en el Anexo E; sin `**` literales |

## 5. Lo que se hizo FUERA del documento hoy, para que la cita al repositorio no mienta

| Qué | Estado |
|---|---|
| **Ramas por defecto en GitHub.** Los enlaces del repositorio de documentación usan `blob/HEAD/` y las ramas `main` de los repos de código estaban en junio/julio, sin `results/`. Cambiadas a la rama de trabajo: `e-ovrt_experimental-setup` → `feature/webconsole-adopcion-front-design`, `e-ovrt_media-plane` → `feature/inference-service`. | ✅ hecho; los 15 enlaces a cifras del repositorio resuelven (verificado por API) |
| `e-ovrt_datasets` y `e-ovrt_control-plane` (dueño: Pandulc) | ⚠ **no tengo permiso**: siguen en `main` (junio). Mientras tanto el mapa de artefactos enlaza por nombre de rama (`feature/datasets-v2-setup`, `feature/control-service`), y los 10 enlaces resuelven. Cuando Pandulc cambie la rama por defecto (o se congele con el tag) se pasan a `HEAD`/tag. |
| **`evidencia/mapa-de-artefactos.md`** (nuevo en el repositorio de documentación) | Para cada material de la Tabla E.1: qué archivo es, en qué repo y ruta, con enlace; las dos huellas completas; y la sección §4 «Material con acceso autorizado» donde va el enlace a la carpeta de evidencia. |
| `README.md` del repositorio | Dos filas nuevas en «Cómo leer» y la sección «Material audiovisual y evidencia cruda: acceso autorizado» (enlace «se publica al cierre de la entrega; el acceso se solicita a los autores»). |
| `evidencia/material-de-video.md`, `repositorios/README.md`, `PUBLICAR.md` | Puntero al acceso autorizado; rama de trabajo vigente de `experimental-setup`; paso 4 del checklist anotado. |
| Guardián del repositorio | ✅ `verificar.py`: 0 violaciones · 43 tests · 34 enlaces a GitHub comprobados, 0 rotos |

Nada de esto está commiteado: los archivos del repositorio de documentación quedan modificados en
el árbol para que los revises antes de publicar.

## 6. Lo que queda para vos

1. **Revisar la v1.3 en Google Docs** (sugerencias + 15 comentarios). Cada comentario dice qué hilo
   responde y qué rechazar si no te convence.
2. **La carpeta de evidencia con acceso autorizado** (Drive), al final: cuando exista, el enlace va
   en `README.md` §«Material audiovisual…» y en `evidencia/mapa-de-artefactos.md` §4 del repositorio
   de documentación. El informe no cambia.
3. **Pandulc**: cambiar la rama por defecto de `e-ovrt_datasets` y `e-ovrt_control-plane` a la de
   trabajo, o congelar con el tag `informe-2026` (paso 8 de `PUBLICAR.md`).
4. **C1** sigue abierto (URL + fecha de acceso de los 13 videos del lote): el `[[PENDIENTE]]` del
   Anexo F viaja.
5. Al integrar: la entrada de referencias de §3 y aflojar el patrón del verificador para las huellas.
