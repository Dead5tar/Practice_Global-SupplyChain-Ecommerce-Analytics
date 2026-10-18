import pandas as pd

# 1. simulacion de un Dataset Real de Logística y E-commerce (Supply Chain)
data = {
    'order_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    'product_category': ['Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing', 'Home', 'Electronics', 'Clothing'],
    'shipping_days': [5, 2, 10, 3, 8, 12, 4, 1],
    'expected_delivery_days': [4, 3, 7, 5, 6, 10, 5, 2],
    'freight_value': [15.5, 5.0, 22.0, 12.0, 8.5, 30.0, 14.0, 4.0],
    'customer_review_score': [4, 5, 2, 5, 3, 1, 4, 5]
}

df = pd.DataFrame(data)

print("--- DATOS INICIALES DE LOGÍSTICA CARGADOS ---")
print(df.head())

# 2. Ingeniería de Características: Identificar entregas retrasadas
df['is_delayed'] = df['shipping_days'] > df['expected_delivery_days']

print("\n--- ANÁLISIS DE ORDEN Y RETRASOS ---")
print(df[['order_id', 'product_category', 'shipping_days', 'expected_delivery_days', 'is_delayed']])

# 3. Agrupación: Porcentaje de retrasos por categoría de producto
print("\n--- TASA DE RETRASOS POR CATEGORÍA DE PRODUCTO (%) ---")
delay_summary = df.groupby('product_category')['is_delayed'].mean().reset_index()
delay_summary['delay_percentage'] = delay_summary['is_delayed'] * 100
print(delay_summary[['product_category', 'delay_percentage']])

# 4. Análisis de Impacto de Negocio: ¿Cómo afecta el retraso al cliente?
print("\n--- CALIFICACIÓN PROMEDIO DEL CLIENTE SEGÚN SI HUBO RETRASO ---")
review_impact = df.groupby('is_delayed')['customer_review_score'].mean().reset_index()
print(review_impact)