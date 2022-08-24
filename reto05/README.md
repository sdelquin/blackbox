# Reto 5: Contraseña segura

Crea una función que, a partir de una longitud, genere una contraseña aleatoria con los siguientes requisitos:

- Un carácter, como mínimo, entre la `A` y `Z`. (Mayúsculas)
- Un carácter, como mínimo, entre la `a` y `z`. (Minúsculas)
- Un número, como mínimo, entre el `0` y `9`.
- Un carácter, como mínimo, a partir de: `!@#$%^&\*`.
- No puedes generar contraseñas inferiores a 4.

```python
# Sintaxis: Python 3.9+
def generar_contrasenya(longitud: int) -> str:
    # Código
    return

generar_contrasenya(10)
# j27ugn@F%E

generar_contrasenya(6)
# a&3&zQ

generar_contrasenya(2)
# Xj6^
```
