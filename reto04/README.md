# Reto 4: Formatea un precio

Crea una función para transformar un input en `float` o `int` a un formato familiar para leer un precio de un producto. Devolverá un `string`.

Ten cuidado porque debes aplicar diferentes arreglos. Por ejemplo, mostrar con **una coma en lugar de un punto**, solo mostrar **2 decimales** si existen decimales, **redondear** si hay más de 2 decimales y **quitar decimales si es un número entero** (23.0 pasaría a ser 23).

```python
# Sintaxis: Python 3.9+
def formatear_precio(price: float|int) -> str:
    # Código
    return

formatear_precio(8)
# 8

formatear_precio(1.0)
# 1

formatear_precio(1.5)
# 1,50

formatear_precio(2.03)
# 2,03

formatear_precio(0.4567)
# 0,46
```
