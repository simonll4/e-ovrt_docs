# Borrador — §17.2 Costos asociados (evaluación económica y financiera)

- **Fecha:** 2026-09-11 · **Estado:** borrador v0.1 para revisión del usuario
- **Destino:** reemplaza `[Pendiente]` en §17.2 del maestro. **Título institucional conservado**
  («Costos asociados»); el contenido pedido («Evaluación Económica y Financiera») se anuncia
  en la primera subsección.
- **Tablas:** usa los **cuatro números libres 12–15**. No toca la numeración de ninguna sección cerrada.
- **Respaldo de cifras:** `docs/operacion/datos/costos-proyecto-2026-09-11.csv` (una fila por cifra, con fuente y fecha)
- **Pendientes marcados `[confirmar …]` / `[monto]`:** ver §Notas editoriales al final

---

### 17.2. Costos asociados

#### 17.2.1. Alcance y supuestos de la evaluación económica y financiera

La sección anterior fija qué se mide y con qué infraestructura. Esta sección estima cuánto cuesta esa plataforma experimental, quién la financia y qué ahorros produce, antes de que la sección 17.3 desarrolle su diseño. La evaluación distingue dos magnitudes que conviene no mezclar. El gasto efectivo es el dinero que el proyecto desembolsa. El costo valorizado suma además los recursos que el proyecto usa sin pagarlos, ya sea porque preexisten, porque se prestan o porque los aporta una institución. La segunda magnitud es la que responde a la pregunta de cuánto costaría reproducir el trabajo desde cero, y por eso es la que se reporta como inversión.

Los supuestos de la estimación son cuatro. El horizonte es la duración del proyecto, desde el inicio de la etapa de investigación el 31 de octubre de 2025 hasta la defensa prevista para fines de septiembre de 2026, unas 48 semanas frente a las 42 del cronograma original de la Figura 1. La moneda es el peso argentino, y los valores expresados en dólares se convierten al tipo de cambio oficial minorista de venta del Banco de la Nación Argentina del 10 de septiembre de 2026, de $1.535 por dólar. Los precios de referencia son precios de lista publicados por el fabricante o por su tienda oficial en la fecha indicada en cada tabla, sin fletes ni tributos de importación. Las horas de trabajo se valorizan a la mediana salarial bruta de un desarrollador junior en Argentina según la encuesta de sueldos 2026.01 de Sysarmy, de $1.538.500 mensuales, que sobre una base de 160 horas mensuales equivale a $9.616 por hora.

No se calculan indicadores de rentabilidad como el valor actual neto o la tasa interna de retorno. El producto es un prototipo experimental sin flujo de ingresos, y el objetivo de esta sección es estimar costos e identificar fuentes de financiamiento y ahorros, no proyectar un negocio.

#### 17.2.2. Inversión inicial y equipamiento

La plataforma corre sobre tres nodos cuyas especificaciones detalla el Anexo B. El nodo de procesamiento es una notebook de consumo preexistente, propiedad de uno de los integrantes. El nodo de borde es una cámara Luxonis OAK-D Pro PoE prestada por el tutor. El nodo de entrenamiento es el clúster institucional, que se trata en 17.2.4 por ser un costo de operación y no de inversión. La Tabla 12 reúne el equipamiento con su condición de uso, el gasto que el proyecto afronta y el valor de referencia que permite dimensionar el aporte.

Tabla 12

*Inversión inicial y equipamiento. Gasto efectivo y valor de referencia*

| Ítem | Condición | Gasto efectivo (ARS) | Valor de referencia (ARS) | Fuente del valor de referencia |
|---|---|---|---|---|
| Nodo de procesamiento. Notebook HP Victus 15-fb2024la (Ryzen 5 8645HS, RTX 4060 Laptop 8 GB, SSD 1 TB) | Preexistente, propiedad de un integrante | 0 | 2.719.999 | Tienda oficial HP Argentina, precio con IVA (HP Inc., 2026) |
| Ampliación de memoria a 32 GB DDR5 (2 × 16 GB) | `[confirmar si se adquirió para el proyecto]` | `[confirmar]` | `[confirmar]` | — |
| Nodo de borde. Cámara Luxonis OAK-D Pro PoE (Series 2) | Prestada por el tutor | 0 | 888.765 | Tienda oficial Luxonis, US$ 579 (Luxonis, 2026) |
| Cable Ethernet M12/RJ45 de la cámara | Prestado con la cámara `[confirmar]` | 0 | 38.360 | Tienda oficial Luxonis, US$ 24,99 (Luxonis, 2026) |
| Switch PoE gigabit | Preexistente `[confirmar propietario]` | 0 | No imputado | — |
| Cámara IP RTSP con grabador (DVR) | Preexistente, propiedad de un integrante | 0 | No imputado | Equipo de uso doméstico previo |
| Casco y chaleco reflectivo (utilería del rodaje) | Prestados por Steel Brox S.R.L. | 0 | No imputado | — |
| **Total** | | **0** | **3.647.124** | |

Nota. Los valores de referencia son precios de lista al 10 de septiembre de 2026, convertidos al tipo de cambio oficial minorista de venta del Banco de la Nación Argentina de esa fecha ($1.535 por dólar). No incluyen fletes ni tributos de importación. "No imputado" señala un bien preexistente de uso doméstico o de bajo valor cuyo precio de mercado no altera el orden de magnitud del total.

La inversión efectiva del proyecto en equipamiento es nula. El valor de referencia del equipamiento aportado asciende a $3.647.124, y la notebook representa tres cuartas partes de ese monto. Esta relación anticipa el resultado de 17.2.5. El costo de una unidad mínima de despliegue está dominado por un único equipo de consumo, sin hardware especializado.

#### 17.2.3. Recursos humanos

El equipo lo integran tres estudiantes con una dedicación aproximada de ocho horas semanales cada uno, sostenida a lo largo de todo el proyecto, más la dirección académica del tutor. La Tabla 13 compara las horas previstas por el cronograma original con las efectivamente dedicadas hasta la defensa y las valoriza a la tarifa de referencia declarada en 17.2.1. El trabajo no se remunera. La valorización expresa el costo que tendría el mismo esfuerzo contratado en el mercado, y es el componente dominante del costo total del proyecto.

Tabla 13

*Recursos humanos. Horas previstas, horas ejecutadas y valorización de referencia*

| Recurso | Dedicación | Semanas previstas | Horas previstas | Semanas ejecutadas | Horas ejecutadas | Valorización ejecutada (ARS) |
|---|---|---|---|---|---|---|
| Integrante 1 | 8 h por semana | 42 | 336 | 48 | 384 | 3.692.400 |
| Integrante 2 | 8 h por semana | 42 | 336 | 48 | 384 | 3.692.400 |
| Integrante 3 | 8 h por semana | 42 | 336 | 48 | 384 | 3.692.400 |
| **Subtotal integrantes** | 24 h por semana | 42 | **1.008** | 48 | **1.152** | **11.077.200** |
| Tutoría académica | Reuniones de seguimiento y revisión de entregables | — | — | — | No cuantificada | Aporte institucional en especie |

Nota. Tarifa de referencia de $9.616 por hora, obtenida de la mediana salarial bruta mensual de un desarrollador junior en Argentina ($1.538.500 según la encuesta Sysarmy 2026.01, citada por Teclab, 2026) sobre 160 horas mensuales. Las semanas previstas corresponden al cronograma de la Figura 1 (31 de octubre de 2025 a 21 de agosto de 2026). Las ejecutadas se extienden hasta la defensa prevista para fines de septiembre de 2026. La valorización prevista es de $9.692.550.

La diferencia de 144 horas entre lo previsto y lo ejecutado, un 14 %, se explica por la extensión de la implementación y de la redacción final más allá del cronograma original. La valorización de las horas ejecutadas, $11.077.200, triplica el valor de referencia del equipamiento. En un proyecto de esta naturaleza el costo principal es el trabajo calificado, no el hardware.

#### 17.2.4. Infraestructura, operación y mantenimiento

Los costos de operación del prototipo son bajos por construcción. No hay servidores alquilados ni servicios en la nube. Los tres servicios de la plataforma, el plano de medios, el plano de control y la distribución de alertas, corren en el nodo de procesamiento, en forma nativa o en contenedores. El resguardo de la evidencia experimental usa una cuenta gratuita de Google Drive y el código se aloja en repositorios gratuitos de GitHub. El ajuste fino de modelos, la única tarea que excede la capacidad del equipo local, se ejecuta en el clúster Mendieta del Centro de Computación de Alto Desempeño de la Universidad Nacional de Córdoba, con acceso institucional sin cargo. La Tabla 14 resume las magnitudes de uso registradas y su costo.

Tabla 14

*Infraestructura, operación y mantenimiento. Magnitud de uso registrada y costo*

| Concepto | Magnitud registrada | Gasto efectivo (ARS) | Observación |
|---|---|---|---|
| Cómputo local de inferencia (RTX 4060 Laptop) | 472 corridas registradas entre julio y agosto de 2026, 34,4 h de GPU | 0 | Energía absorbida en el consumo doméstico. A una potencia de 100 a 150 W, equivale a entre 3 y 5 kWh |
| Cómputo en el clúster Mendieta (1 × NVIDIA A30, 10 núcleos por trabajo) | 15 trabajos enviados entre el 13 y el 20 de agosto de 2026, 10 con GPU asignada, 6 completados. 1,2 GPU-h en total, de las cuales 0,94 corresponden a las tres corridas completas de ajuste fino | 0 | Acceso institucional (CCAD-UNC). A precios de alquiler de GPU en nube pública, el equivalente monetario de 1,2 GPU-h es marginal |
| Alquiler de servidores o VPS | Ninguno | 0 | Despliegue local |
| Almacenamiento y control de versiones | 2,6 GB de evidencia no regenerable en Google Drive. Código en GitHub | 0 | Planes gratuitos |
| Licencias de software | Conjunto de herramientas de código abierto de punta a punta | 0 | Ver nota sobre AGPL-3.0 |
| Conjuntos de datos y pesos de modelos | Licencias abiertas con atribución (CC BY 4.0 y equivalentes, Apache-2.0, AGPL-3.0) | 0 | Descarga directa de las fuentes |
| Conectividad a Internet | Uso doméstico de los integrantes | 0 | No discriminada |
| Mantenimiento | Suites de pruebas automatizadas de los cinco repositorios, ejecutadas en el equipo local | 0 | Sin integración continua paga |
| **Total** | | **0** | |

Nota. Las horas de cómputo local provienen de los registros de duración de cada corrida del plano de medios. Las horas de clúster provienen de la contabilidad de Slurm del clúster Mendieta. El único componente del conjunto de herramientas con licencia AGPL-3.0 es la biblioteca de inferencia de los modelos YOLOE, de uso académico libre. Un despliegue comercial derivado exigiría publicar el código bajo la misma licencia o adquirir una licencia empresarial. El modelo campeón, Grounding DINO, se distribuye bajo Apache-2.0 y no impone esa condición.

#### 17.2.5. Financiamiento, ahorros e ingresos

La Tabla 15 consolida las tres tablas anteriores y agrega el único gasto efectivo del proyecto, el traslado a la locación de rodaje, con la fuente de financiamiento de cada componente.

Tabla 15

*Resumen económico del proyecto. Costo valorizado, gasto efectivo y fuentes de financiamiento*

| Componente | Costo valorizado (ARS) | Gasto efectivo (ARS) | Fuente de financiamiento |
|---|---|---|---|
| Recursos humanos (1.152 h, Tabla 13) | 11.077.200 | 0 | Trabajo no remunerado de los integrantes |
| Equipamiento (Tabla 12) | 3.647.124 | 0 | Aporte propio (notebook) y préstamo del tutor (cámara) |
| Infraestructura y operación (Tabla 14) | No imputado | 0 | Aportes en especie de CCAD-UNC, GitHub y Google |
| Movilidad (un traslado a la locación de rodaje) | `[monto]` | `[monto]` | Aporte propio |
| Locación de rodaje y utilería | No imputado | 0 | Préstamo de Steel Brox S.R.L. |
| **Total** | **14.724.324 + `[monto]`** | **`[monto]`** | |

Nota. El costo valorizado suma la valorización de las horas ejecutadas y el valor de referencia del equipamiento aportado. Los componentes "No imputado" son aportes en especie cuyo equivalente monetario no altera el orden de magnitud del total.

El costo valorizado del proyecto es de unos $14,7 millones, de los cuales el 75 % corresponde a las horas de trabajo de los integrantes y el resto al equipamiento aportado. El gasto efectivo se limita al traslado a la locación de rodaje. Ese contraste es la conclusión económica central. El proyecto se financia íntegramente con trabajo propio y con aportes en especie, sin subsidios ni financiamiento externo, y ninguno de esos aportes exige una contraprestación.

**Ingresos esperados.** No los hay ni se proyectan. El producto es una plataforma experimental de medición, no un sistema comercial, y su valor se expresa en la evidencia que produce y en el conocimiento transferible sobre detección de vocabulario abierto en el dominio de la obra.

**Ahorros.** Se identifican tres costos evitados, dos de ellos medidos en el propio proyecto.

1. **Licencias.** El conjunto de herramientas de código abierto elimina el costo de licencias de software de inferencia, de anotación y de despliegue, con la única salvedad sobre AGPL-3.0 señalada en la Tabla 14.
2. **Entrenamiento.** La detección de vocabulario abierto permite operar sin entrenar. Agregar un conjunto de cinco clases que la plataforma nunca había configurado costó un archivo de configuración de 48 líneas y nueve minutos de tiempo de pared, sin anotar datos ni entrenar, y la clase `machinery` alcanzó una AP@0.5 zero-shot de 0,662. En contraste, la rama de ajuste fino consumió 1,2 GPU-h de clúster más el trabajo de preparar datos, entorno y recetas, y no produjo un modelo adoptable. Para el alcance de este trabajo, el costo de entrenar fue un costo sin retorno y el costo de no entrenar fue nulo.
3. **Hardware.** La plataforma completa, con sus tres servicios y la inferencia del modelo campeón, corre en una notebook de consumo. No requiere estación de trabajo ni servidor con GPU de centro de datos.

**Costo de replicación.** Una unidad mínima de despliegue, compuesta por un nodo de procesamiento, una cámara PoE con su cable y un inyector PoE, tiene un costo de referencia de $3.685.484 al tipo de cambio declarado. El software no agrega costo. Tres cuartas partes de ese monto corresponden a la notebook, de modo que el costo de la unidad sigue de cerca al precio de un equipo de consumo con GPU y baja con él.

---

## Notas editoriales (no van al informe)

**Pendientes del usuario (marcados en el texto)**
1. **Ampliación de RAM.** La Tabla B.1 declara 32 GB (2 × 16 GB) y el modelo de fábrica trae 16 GB (2 × 8 GB). Si los módulos se compraron para el proyecto, son gasto efectivo y hay que poner monto y fecha. Si no, borrar la fila.
2. **Cable M12/RJ45** — asumí que vino con la cámara prestada. Confirmar.
3. **Switch PoE** — ¿propio, prestado con la cámara, o de la empresa de alguno de ustedes? Confirmar propietario; el valor queda "No imputado".
4. **`[monto]` del traslado** a Steel Brox (combustible o pasajes). Es el único gasto efectivo del proyecto y aparece tres veces en la Tabla 15.
5. **Tutoría** — quedó como aporte en especie no cuantificado. Si prefieren cuantificarla (p. ej. N reuniones de 1 h más revisión), paso el dato a horas.

**Referencias nuevas a dar de alta en el listado global** (formato APA del informe)
- HP Inc. (2026). *Notebook HP Gaming Victus 15-fb2024la* [Página de producto]. Tienda HP Argentina. https://www.hp.com/ar-es/shop/notebook-gaming-victus-15-fb2024la-a14lsla.html
- Luxonis. (2026). *OAK-D Pro PoE* [Página de producto]. Luxonis Shop. https://shop.luxonis.com/products/oak-d-pro-poe
- Teclab. (2026). *¿Cuánto gana un programador junior en Argentina en 2026?* https://teclab.edu.ar/tecnologia-y-desarrollo/cuanto-gana-un-programador-junior/ (cita la encuesta Sysarmy 2026.01; si se prefiere la fuente primaria: https://sueldos.openqube.io/encuesta-sueldos-2026.01/)
- Tipo de cambio BNA 10/09/2026 ($1.485 compra / $1.535 venta): El Cronista o La Nación de esa fecha, o el histórico del BCRA. Elegir una y citarla.
- Ya existen en el listado y se reutilizan sin alta: *Centro de Computación de Alto Desempeño (2026)* para Mendieta.

**Cifras verificadas en esta jornada (todas en el CSV de respaldo)**
- Mendieta: `sacct -M ivb -u gguillaumet -S 2026-07-01` → 15 jobs, 10 con GPU (Elapsed > 0), 6 COMPLETED; suma 4.302 s = **1,195 GPU-h**; fulls T1 13:08 + T2 17:07 + T2v2 26:10 = 0,94 GPU-h. Todos con `gres/gpu=1, cpu=10`.
- Cómputo local: 472 dirs en `e-ovrt_media-plane/runs/`, 470 con `duration_seconds` → **34,35 h** (jul 2,64 h · ago 31,71 h; 33,98 h Grounding DINO).
- Extensibilidad (AF-4): `results/bench_imagenes/index.md` §4 → 0 entrenamientos, 1 archivo de 48 líneas, 9 min, `machinery` AP@0.5 0,662 (99 cajas GT).
- Semanas: Gantt 31/10/25→21/08/26 = 42,0; real a 30/09/26 = 47,7 ≈ 48.
- HP: AR$ 2.461.538 sin impuestos nacionales; AR$ 2.719.999 con IVA (campo `price` de la página; equivale a IVA 10,5 %).
- Luxonis: US$ 579 (la página hoy; el buscador aún mostraba US$ 549, valor viejo). Cable M12/RJ45 e inyector PoE US$ 24,99 c/u.
- Tarifa: 1.538.500 / 160 = 9.615,625 ARS/h → 384 h = 3.692.400; 1.152 h = 11.077.200; 1.008 h = 9.692.550.

**Reglas verificadas**
- Sin referencias a documentación local. Sin ":" ni ";" en prosa (sólo dentro de tablas). Voz en presente para lo que existe, "se estiman" para las estimaciones. Título institucional conservado.
