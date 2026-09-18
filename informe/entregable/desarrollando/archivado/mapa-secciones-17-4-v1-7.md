# Mapa de secciones de §17.4 — de la v1.6 a la v1.7

> **Para qué sirve.** El pase 4 ([`correcciones-etapa-4-pase-4.md`](correcciones-etapa-4-pase-4.md),
> 2026-09-04) llevó §17.4 de **16 títulos a 9** y renumeró sus subsecciones. Las actas anteriores
> (**E4-01…E4-31**), las fichas `AJ-4.x` de `ajustes/04`, la tabla de alineación cruzada del pase 3
> y la extracción `entregable/90b` citan la numeración vieja. **Nada de eso se reescribe**: se lee
> con este mapa al lado, igual que se hizo con §17.1 y con §17.3.
>
> Estado: la v1.7 se entregó **con sugerencias sin aceptar**. Mientras el usuario no las acepte, el
> documento vigente sigue siendo la v1.6 y `90b-etapa4-texto-extraido.md` no se regenera.
>
> §17.5 **no necesita mapa**: sus subsecciones conservan número y título, y sólo desapareció la
> 17.5.8. Sus tablas sí cambiaron de número, y eso está en la §3 de acá.

---

## 1. Estructura de la v1.7

| # | Sección | Tablas | Figura |
|---|---|---|---|
| 17.4 | Implementación del prototipo experimental | — | — |
| 17.4.1 | Componentes construidos y cadena de datos | — | 4.5 |
| 17.4.2 | Correspondencia y contratos materializados | 56 | — |
| 17.4.3 | Servicios, gobierno por configuración y acople | 57 | — |
| 17.4.4 | Configuración efectiva y catálogo de modelos | — | — |
| 17.4.5 | Artefactos y trazabilidad por corrida | 58 | — |
| 17.4.6 | Banco temporal y referencia humana de evaluación | — | — |
| 17.4.7 | Verificación, alcance efectivo y brechas | 59 | — |
| 17.4.8 | Extensibilidad y costo de extensión | 60 | — |

Nueve títulos, todos de nivel 3 salvo el del capítulo. **Cero títulos de nivel 4.**

---

## 2. Traducción, de la numeración vieja a la nueva

| Vieja (v1.6) | Nueva (v1.7) | Nota |
|---|---|---|
| 17.4 Implementación del prototipo experimental | **17.4** | entrada de dos párrafos a uno |
| 17.4.1 Componentes construidos y cadena de datos | **17.4.1** | las propiedades de servicio migran a 17.4.3 |
| 17.4.2 Correspondencia entre el diseño y los artefactos implementados | **17.4.2** | retitulada, absorbe la 17.4.3 |
| 17.4.3 Contratos de datos materializados | **17.4.2** | fundida, sin título propio |
| 17.4.4 Interfaces de servicio y gobierno por configuración | **17.4.3** | retitulada, absorbe la 17.4.5 |
| 17.4.5 Patrones de acople y caminos experimentales | **17.4.3** | fundida, sin título propio |
| 17.4.6 Configuración efectiva y catálogo de modelos | **17.4.4** | ⚠ es la que §17.3 citaba por número |
| 17.4.7 Artefactos y trazabilidad por corrida | **17.4.5** | recibe el detalle del ledger (E4-31) |
| 17.4.8 Construcción del banco temporal y de la referencia humana de evaluación | **17.4.6** | retitulada, sin títulos de nivel 4 |
| **17.4.8.1** Adquisición y conformación del material audiovisual | **17.4.6** | entradilla «Adquisición del material» |
| **17.4.8.2** Preparación y segmentación temporal de los clips | **17.4.6** | entradilla «Segmentación temporal» |
| **17.4.8.3** Preanotación asistida y revisión humana en CVAT | **17.4.6** | entradilla «Preanotación y revisión humana» |
| **17.4.8.4** Derivación, validación, promoción y congelamiento | **17.4.6** | entradilla «Derivación y congelamiento» |
| 17.4.9 Verificación técnica de la implementación | **17.4.7** | retitulada, absorbe la 17.4.10 |
| 17.4.10 Alcance efectivo, límites y brechas | **17.4.7** | fundida, sin título propio |
| 17.4.11 Extensibilidad implementada y costo de extensión | **17.4.8** | retitulada, recibe la evolución aditiva |

---

## 3. Tablas y figura

### §17.4

| Vieja | Nueva | Sección | Estado |
|---|---|---|---|
| 56 Correspondencia entre contratos y materialización | **56** | 17.4.2 | sin cambios |
| 57 Interfaces principales de los servicios | **57** | 17.4.3 | cuatro celdas reescritas |
| 58 Artefactos persistidos por componente | **58** | 17.4.5 | sin cambios |
| 59 Evidencia de verificación técnica | **59** | 17.4.7 | cinco celdas acortadas |
| **60** Capacidades ejercidas, exclusiones y brechas | — | — | **pasa a prosa** (D-C, comentario 6) |
| 61 Puntos de extensión y costo técnico | **60** | 17.4.8 | renumerada, dos celdas reescritas |

| Vieja | Nueva | Sección | Estado |
|---|---|---|---|
| Figura 4.7 Vista de procesos y patrones de acople | **Figura 4.5** | 17.4.1 | renumerada y citada en prosa |

⚠ La imagen embebida **no es** la producida el 2026-08-28 en `informe/figuras/`. La embebida deja a
la distribución fuera del orden de arranque; la producida lo dibuja completo. La nota del pase ya
describe el orden correcto, de modo que al reemplazar la imagen todo coincide. Pegarla es trabajo
del usuario.

### §17.5

| Vieja | Nueva | Sección | Estado |
|---|---|---|---|
| 62 Resultados de percepción por combinación | **61** | 17.5.2 | renumerada |
| 63 Resultados de estado por persona | **62** | 17.5.3 | renumerada, dos celdas traducidas |
| 64 Alerta por episodio en el bloque de rodaje | **63** | 17.5.4 | renumerada, absorbe los denominadores |
| **65** Falsos positivos en el estrato de obra real | — | — | **pasa a prosa** (D-I) |
| 66 Camino en vivo por densidad, integridad y tramo | **64** | 17.5.5 | renumerada, celda restaurada y presupuesto remitido |
| 67 Curva de capacidad del ajuste fino | **65** | 17.5.6 | renumerada |

Con §17.4 cerrando en la Tabla 60 y §17.5 arrancando en la 61, el capítulo queda contiguo, que es
lo que el pase 3 §G había previsto. **El hueco 53–55 que dejó §17.3** al bajar de 17 a 14 tablas
sigue abierto y lo resuelve la integración.

---

## 4. Dónde quedó cada cosa que las actas viejas nombran

| Concepto | Casa en la v1.7 |
|---|---|
| Correspondencia diseño → artefacto (AJ-4.02, E4-05) | **17.4.2**, Tabla 56 |
| Los cinco contratos y el evento persistido (AJ-4.03, E4-28, comentario 0) | **17.4.2** |
| Identificador determinista de la alerta y sus tres consecuencias | **17.4.2**, en dos párrafos |
| Servicios HTTP config-driven (AJ-4.04, E4-03, E4-06) | **17.4.3**, Tabla 57 |
| Orden de arranque real y garantía del publicador (H2-01) | **17.4.3**, una sola vez |
| Dos caminos de acople DBE y EBE (AJ-4.05, E4-07) | **17.4.3** |
| Valores efectivos del núcleo y del perfil operativo (AJ-4.07, E4-11, E4-12, E4-26) | **17.4.4** |
| Layout de artefactos y árbol del repositorio (AJ-4.08, E4-13, E4-29) | **17.4.5**, Tabla 58 |
| Detalle operativo del ledger (E4-31) | **17.4.5** |
| Construcción del banco temporal (AJ-4.09, E4-14, E4-19) | **17.4.6**, cuatro entradillas |
| Verificación técnica y su cifra fechada (AJ-4.10, E4-21) | **17.4.7**, Tabla 59 |
| Capacidades, exclusiones y brechas (AJ-4.11, E4-16, E4-17, E4-22, E4-27) | **17.4.7**, en prosa por estatuto |
| Desviación del rango de entrenamiento (H2-02) | **17.4.7** |
| Puntos de extensión y costo medido (AJ-4.12, R-26) | **17.4.8**, Tabla 60 |
| Evolución aditiva del contrato e identidad de sujeto | **17.4.8** |
| Marcador de procedencia del lote (C1) | **17.4.6**, intacto |
