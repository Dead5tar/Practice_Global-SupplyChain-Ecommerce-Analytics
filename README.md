# A Global Supply Chain & E-Commerce Analytics (Python & Pandas)

## A Resumen del Proyecto
Este proyecto analiza datos de logística y comercio electrónico utilizando **Python y Pandas** para evaluar la eficiencia en la cadena de suministro (*Supply Chain*). El objetivo principal es identificar retrasos en los envíos, analizar los costos de flete y medir el impacto directo de los incumplimientos logísticos en la satisfacción y calificación del cliente (*Customer Review Score*).

### A Tecnologías Utilizadas
* **Python**: Lenguaje de programación para la manipulación y procesamiento de datos.
* **Pandas**: Creación de DataFrames, filtrado condicional, ingeniería de características (*Feature Engineering*) y agregaciones estadísticas.
* **Business Intelligence (Logística):** Enfoque analítico orientado a la optimización de entregas y la experiencia del cliente.

### A ¿Qué hace el script (`supply_chain_analysis.py`)?
1. **Simulación de Datos Logísticos:** Carga un conjunto de datos tabulares con variables críticas de e-commerce (categoría de productos, días de envío reales vs. estimados, valor de flete y calificación).
2. **Ingeniería de Características (`Feature Engineering`):** Crea de forma automatizada una columna lógica (`is_delayed`) para aislar los pedidos que sufrieron retrasos.
3. **Agregación de Retrasos por Categoría:** Calcula el porcentaje exacto de retrasos por cada categoría de producto mediante operaciones de agrupación.
4. **Análisis de Impacto en el Cliente:** Cruza las métricas logísticas con las calificaciones de los usuarios para demostrar el costo en la reputación del negocio ante fallas operativas.

### A Hallazgos Clave y Aplicación de Negocio
* **Corrosión de la Experiencia del Usuario:** Se evidencia analíticamente que cada retraso en la entrega impacta de forma directa y negativa la calificación promedio otorgada por el consumidor final.
* **Cuellos de Botella por Categoria:** El análisis permite a los gerentes de logística identificar qué líneas de productos sufren más desviaciones en los plazos estimados, facilitando la renegociación con proveedores o transportistas.

### A Cómo ejecutar el proyecto
1. Asegúrate de tener Python y la librería Pandas instalados:
   ```bash
   pip install pandas