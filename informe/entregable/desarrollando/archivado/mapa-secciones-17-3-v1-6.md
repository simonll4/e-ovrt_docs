# Mapa de secciones de §17.3 — de la v1.4/v1.5 a la v1.6

> **Para qué sirve.** El pase 4 (`correcciones-etapa-3-pase-4.md`, 2026-09-03) redujo §17.3 de
> **61 títulos a 30** y renumeró todas sus subsecciones. Las actas anteriores (**E3-01…E3-42**),
> las **26 redlines** `R-01…R-26` de `ajustes/material-etapa-3/93`, el material `91`, `92`, `92b`,
> `94` y la extracción `entregable/90` citan la numeración vieja. **Nada de eso se reescribe**: se
> lee con este mapa al lado, igual que se hizo con §17.1 en `mapa-secciones-17-1-v1-15.md`.
>
> Estado (✎ 2026-09-04): el usuario aceptó la v1.6 y, más tarde, el pase de la Etapa 4 obligó a
> corregir una remisión cruzada. El documento vigente es
> **`desarrollando/E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.7.docx`** (limpio, 0 marcas, 4
> comentarios abiertos), idéntico a la v1.6 salvo un token: la remisión de §17.3.6.1 pasa de
> «sección 17.4.6» a **«sección 17.4.4»**, porque §17.4 renumeró sus subsecciones.
> `90-etapa3-texto-extraido.md` se regeneró desde la v1.7 (regla D-C) y el kit también. La v1.5, la
> v1.6 y las dos entregas con sugerencias están en `archivado/`.
>
> **La estructura y la numeración de subsecciones de este mapa no cambian entre la v1.6 y la v1.7.**

---

## 1. Estructura de la v1.6

| Nueva | Título |
|---|---|
| **17.3.1** | Propósito y pregunta rectora |
| **17.3.2** | Alcance, capacidades y decisiones arquitectónicas |
| 17.3.2.1 | Capacidades arquitectónicas requeridas |
| 17.3.2.2 | Requisitos no funcionales de referencia |
| 17.3.2.3 | Decisiones arquitectónicas y principios de lectura |
| **17.3.3** | Vista general y patrones de acople |
| **17.3.4** | Configuración experimental, vocabulario y estrategia del núcleo |
| 17.3.4.1 | Configuración de corrida como artefacto de reproducibilidad |
| 17.3.4.2 | Diseño de prompts y vocabulario activo |
| 17.3.4.3 | Vocabulario y estrategia del núcleo validable |
| 17.3.4.4 | Reglas de comparabilidad entre configuraciones |
| **17.3.5** | Diseño conceptual del plano de medios |
| 17.3.5.1 | Flujo operativo del Pipeline de Medios |
| 17.3.5.2 | Capacidades opcionales y degradación segura |
| **17.3.6** | Diseño conceptual del plano de control |
| 17.3.6.1 | Máquina de estados y ciclo del episodio |
| 17.3.6.2 | Motor de evaluación y definición de patrón |
| 17.3.6.3 | Transporte, persistencia y trazabilidad experimental |
| 17.3.6.4 | Cadena de traducción entre condición, evidencia, patrón y alerta |
| **17.3.7** | Distribución de alertas confirmadas |
| **17.3.8** | Contratos, trazabilidad y evidencia visual |
| 17.3.8.1 | Contratos mínimos e interfaces |
| 17.3.8.2 | Repositorio de hechos y reconstrucción experimental |
| 17.3.8.3 | Política de evidencia visual mínima |
| **17.3.9** | Observabilidad y aplicabilidad de métricas |
| **17.3.10** | Escenarios experimentales y topología de referencia |
| 17.3.10.1 | Equivalencia arquitectónica y alcance de EBE |
| 17.3.10.2 | Naturaleza temporal de la fuente y aplicabilidad |
| 17.3.10.3 | Roles funcionales y unidades desplegables de referencia |
| **17.3.11** | Riesgos, plan de materialización y cierre |

---

## 2. Traducción, de la numeración vieja a la nueva

| Vieja (v1.4 / v1.5) | Nueva (v1.6) | Nota |
|---|---|---|
| 17.3.1 Introducción y propósito | **17.3.1** | reescrita alrededor de la pregunta rectora |
| 17.3.2 Insumos metodológicos y decisiones derivadas | **17.3.1** | fundida; su idea rectora es el primer párrafo |
| 17.3.3 Alcance, requisitos y decisiones iniciales | **17.3.2** | |
| 17.3.3.1 Alcance del núcleo y extensiones | **17.3.2** (entrada) | fundida, sin título propio |
| 17.3.3.2 Capacidades arquitectónicas requeridas | **17.3.2.1** | Tabla 39 |
| 17.3.3.3 Requisitos no funcionales de referencia | **17.3.2.2** | Tabla 40 |
| 17.3.3.4 Decisiones arquitectónicas iniciales | **17.3.2.3** | Tabla 41 |
| 17.3.4 Principios arquitectónicos adoptados | **17.3.2.3** | es la entrada de la Tabla 41 |
| 17.3.5 Vista general de la arquitectura | **17.3.3** | única casa de los dos patrones de acople |
| 17.3.6 Configuración experimental y diseño de prompts | **17.3.4** | |
| 17.3.6.1 Función arquitectónica de la configuración | **17.3.4** (entrada) | fundida |
| 17.3.6.2 Configuración de corrida como artefacto | **17.3.4.1** | Tabla 42 |
| 17.3.6.3 Diseño de prompts y vocabulario activo | **17.3.4.2** | remite a §17.1.5.3 |
| 17.3.6.4 Diseño inicial de prompts para el catálogo | **17.3.4.3** | Tabla 43, reducida |
| 17.3.6.5 Reglas de comparabilidad | **17.3.4.4** | |
| 17.3.7 Diseño conceptual del plano de medios | **17.3.5** | |
| 17.3.7.1 Flujo operativo del Pipeline de Medios | **17.3.5.1** | absorbe 17.3.7.2 y 17.3.7.3 |
| 17.3.7.2 Criterios de diseño del plano de medios | **17.3.5.1** | sin título propio |
| 17.3.7.3 Control de ritmo según tipo de fuente | **17.3.5.1** | dentro de la etapa de control de ritmo |
| 17.3.7.4 Capacidades opcionales sin desplazar el núcleo | **17.3.5.2** | casa de *fail-open* |
| 17.3.8 Diseño conceptual del plano de control | **17.3.6** | |
| 17.3.8.1 Flujo lógico y responsabilidades | **17.3.6** (entrada) | fundida |
| 17.3.8.2 Evaluación de patrones y máquina de estados | **17.3.6.1** | Figura 4.3 |
| 17.3.8.3 Motor de evaluación de patrones de riesgo | **17.3.6.2** | absorbe sus cuatro nietos |
| **17.3.8.3.1** Patrón de riesgo como unidad evaluable | **17.3.6.2** | los siete elementos, íntegros |
| **17.3.8.3.2** Memoria temporal y ciclo de evaluación | **17.3.6.2** y **17.3.6.1** | el ciclo sube a la máquina de estados |
| **17.3.8.3.3** Evaluación según niveles de complejidad | **17.3.6.2** | Tabla 44 |
| **17.3.8.3.4** Salidas, episodios y trazabilidad | **17.3.6.2** | |
| 17.3.8.4 Transporte, persistencia y trazabilidad | **17.3.6.3** | |
| 17.3.9 Integración condición → estrategia → patrón → alerta | **17.3.6.4** | queda sólo la cadena y su figura |
| 17.3.9.1 Cadena de traducción arquitectónica | **17.3.6.4** | Figura 4.4 |
| 17.3.9.2 Estrategia adoptada para el núcleo validable | **17.3.4.3** | E-IND se muda a su sección dueña |
| 17.3.9.3 Comparabilidad entre estrategias | **17.3.4.4** | fundida |
| 17.3.10 Distribución de alertas confirmadas | **17.3.7** | sin subsecciones |
| 17.3.10.1 Función arquitectónica de la distribución | **17.3.7** | |
| 17.3.10.2 Consumidores, canales y ciclo de vida | **17.3.7** | Tabla 45 |
| 17.3.10.3 Política, medición y límites de interpretación | **17.3.7** | el detalle del ledger baja a §17.4 |
| 17.3.11 Contratos e interfaces internas | **17.3.8** | |
| 17.3.11.1 Fronteras informacionales de intercambio | **17.3.8** (entrada) | reducida a una oración |
| 17.3.11.2 Contratos mínimos e interfaces | **17.3.8.1** | Tabla 46 |
| 17.3.11.3 Criterios de evolución durante la implementación | **17.3.8.1** | fundida |
| 17.3.12 Trazabilidad y minimización de evidencia visual | **17.3.8.2** y **17.3.8.3** | |
| 17.3.12.1 Repositorio de eventos | **17.3.8.2** | |
| 17.3.12.2 Hechos persistibles mínimos | **17.3.8.2** | la Tabla 47 pasa a prosa |
| 17.3.12.3 Política de evidencia visual mínima | **17.3.8.3** | única casa de la minimización |
| 17.3.13 Observabilidad e instrumentación de métricas | **17.3.9** | sin subsecciones |
| 17.3.13.1 Materialización arquitectónica de las métricas | **17.3.9** | Tabla 47 (antes 48) |
| 17.3.13.2 Definiciones operacionales y criterio de relojes | **17.3.9** | la Tabla 49 se elimina |
| 17.3.13.3 Señales observables y estados de aplicabilidad | **17.3.9** | Tabla 48 (antes 50) |
| 17.3.13.4 Registro de resultados por corrida | **17.3.9** | |
| 17.3.14 Escenarios experimentales DBE y EBE | **17.3.10** | |
| 17.3.14.1 DBE como escenario de estabilización | **17.3.10** (entrada) | fundida |
| 17.3.14.2 EBE como escenario de fuente en vivo | **17.3.10** (entrada) | fundida |
| 17.3.14.3 Equivalencia arquitectónica entre escenarios | **17.3.10.1** | |
| 17.3.14.4 Comparación arquitectónica entre DBE y EBE | **17.3.10.1** | la Tabla 51 se elimina |
| 17.3.14.5 Alcance arquitectónico de EBE | **17.3.10.1** | Tabla 49 (antes 52) |
| 17.3.14.6 Naturaleza temporal de la fuente | **17.3.10.2** | |
| 17.3.15 Roles funcionales y unidades desplegables | **17.3.10.3** | Tabla 50 (antes 53) |
| 17.3.16 Riesgos arquitectónicos y mitigaciones | **17.3.11** | Tabla 51 (antes 54) |
| 17.3.17 Plan de materialización y criterios de avance | **17.3.11** | Tabla 52 (antes 55) |
| 17.3.18 Cierre del diseño arquitectónico | **17.3.11** | conservado corto |

---

## 3. Tablas

Catorce tablas, numeradas **39–52** de forma contigua. Cada una se cita **exactamente una vez** en
prosa, cosa que en la v1.5 no ocurría con once de las diecisiete.

| Vieja | Nueva | Sección | Estado |
|---|---|---|---|
| 39 | **39** | 17.3.2.1 | sin cambios |
| 40 | **40** | 17.3.2.2 | sin cambios; ahora citada en prosa |
| 41 | **41** | 17.3.2.3 | dos celdas acortadas (DA-03, DA-11) |
| 42 | **42** | 17.3.4.1 | una celda acortada (política de distribución) |
| 43 | **43** | 17.3.4.3 | **8 filas fuera** (CR-03…CR-06 → Anexo C); leyenda nueva |
| 44 | **44** | 17.3.6.2 | columna de evidencia acortada; nota remite a §17.1.5.2 |
| 45 | **45** | 17.3.7 | sin cambios |
| 46 | **46** | 17.3.8.1 | sin cambios; ahora citada en prosa |
| **47** | — | — | **eliminada** (hechos persistibles → prosa de 17.3.8.2) |
| 48 | **47** | 17.3.9 | nota ampliada con el hito inicial del plano de medios |
| **49** | — | — | **eliminada** (diccionario de métricas → §17.1.7.3/17.1.7.5 y Anexo D) |
| 50 | **48** | 17.3.9 | sin cambios; ahora citada en prosa |
| **51** | — | — | **eliminada** (DBE/EBE → Tabla 17 de §17.1) |
| 52 | **49** | 17.3.10.1 | sin cambios; ahora citada en prosa |
| 53 | **50** | 17.3.10.3 | sin cambios; ahora citada en prosa |
| 54 | **51** | 17.3.11 | sin cambios |
| 55 | **52** | 17.3.11 | sin cambios |

---

## 4. Figuras

Cuatro figuras, todas citadas en prosa. En la v1.5 ninguna lo estaba.

| Vieja | Nueva | Sección | Estado |
|---|---|---|---|
| 4.1 Vista conceptual | **4.1** | 17.3.3 | sin cambios |
| 4.2 Flujo del Pipeline de Medios | **4.2** | 17.3.5 | sin cambios |
| **4.3** Flujo del plano de control | — | — | **eliminada** (tres cajas, sin información propia) |
| 4.4 Máquina de estados | **4.3** | 17.3.6.1 | renumerada |
| 4.5 Cadena de traducción | **4.4** | 17.3.6.4 | renumerada |
| **4.6** Roles CPN, EN y TN | — | — | **eliminada** (repite la Tabla 50) |

⚠ La imagen embebida de la máquina de estados **no es** la FIG-E producida el 2026-08-21 en
`informe/figuras/`: no dibuja la reapertura a `candidate`. Pegarla es trabajo de la integración.

---

## 5. Dónde quedó cada cosa que las actas viejas nombran

| Concepto | Casa en la v1.6 |
|---|---|
| Códigos E-DIR / E-IND / E-HYB (E3-42) | remisión a **§17.1.5.3**; la adopción de E-IND, en **17.3.4.3** |
| *fail-open* (enmienda a E3-28) | definido en **17.3.5.2**; nombrado sin re-explicar en 17.3.2, 17.3.10.1 y 17.3.11 |
| Ledger de entregas y política de distribución (E3-29) | **17.3.7**; el detalle operativo baja a §17.4 (handoff E4-31) |
| Los cinco estados del motor (E3-08 / FIG-E) | **17.3.6.1** |
| Definición de patrón, siete elementos | **17.3.6.2** |
| Contratos versionados (D-P2-5) | **17.3.8.1** |
| Minimización de evidencia visual | **17.3.8.3** |
| Estados de aplicabilidad y causas | **17.3.9** |
| Cero silencioso sobre fuente no temporal | **17.3.10.2** |
| Roles CPN / EN / TN | **17.3.10.3**, con remisión a §17.1.4.1 |
| Extensibilidad en tres clases (R-26) | **17.3.11** |
