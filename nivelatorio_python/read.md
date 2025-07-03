# Sistema de Gestión de Librerías

Este es un **sistema de gestión de inventario y ventas basado en consola** para una librería nacional, desarrollado en **Python**. Permite gestionar productos, registrar y analizar ventas, y generar informes detallados con control de stock, validaciones y gestión de descuentos.

---

## Características

### 1. Gestión de Inventario
- Añadir, actualizar, eliminar y listar libros.
- Cada producto incluye: `título`, `autor`, `categoría`, `precio` y `stock`.

### 2. Módulo de Ventas
- Registrar nuevas ventas seleccionando productos, cantidad, cliente y descuento opcional.
- Actualizar el stock automáticamente.
- Validar si hay suficiente stock antes de procesar una venta.

### 3. Informes
- Los 3 productos más vendidos.
- Ventas netas totales agrupadas por autor.
- Ingresos brutos y netos (con y sin descuentos).

### 4. Validaciones
- Garantiza que todas las entradas sean válidas (números positivos, campos obligatorios).
- Impide ventas si el stock es insuficiente.
- Gestión de errores mediante `try-except`.

### 5. Diseño modular
- Toda la lógica se divide en funciones reutilizables.
- Utiliza diccionarios y listas para almacenar y gestionar datos.
- Las funciones utilizan parámetros, valores de retorno y expresiones lambda para los informes.

---

## Estructura de datos

### Productos
Almacenados en un diccionario como:
```python
products = {
"P001": {
"title": "Título del libro",
"author": "Nombre del autor",
"category": "Género",
"price": 19.99,
"stock": 5
},
...
}

