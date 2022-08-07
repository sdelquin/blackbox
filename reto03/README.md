# Reto 3: Ocultado números sensibles

Crea una función que oculte los números de una tarjeta de crédito, salvo los 3 últimos dígitos. Deberías recibir siempre 16 dígitos y puede ser `string` o `int`.

Si la longitud no es válida, devolverás un `False`.

Algunos parámetros esperados.

```python
1234567890123456
"1234567890123456"
"1234 5678 9012 3456"
```

En todos los casos anteriores devolveremos:

```python
"xxxxxxxxxxxxx456"
```

La siguiente estructura puede servirte de prototipo.

```python
# Sintaxis: Python 3.9+
def ocultar_numeros(numeros: str|int, char_hide: str = "x") -> str:
    # Código
    return ""
```
