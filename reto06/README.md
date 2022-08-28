# Reto 6: Desfragmentando el disco

La información tiende a desfragmentarse paulatinamente en un disco según pasa el tiempo. En los discos duros mecánicos, o HDD, afecta negativamente al tener que recorrer más distancia para leer o escribir los mismos datos. Incluso tiende a acortar su vida útil al desgastar más sus partes. En los discos SSD no es importante al no existir piezas mecánicas.

Por ello vamos a crear una función que nos ayude a acercar, u ordenar, toda la información del disco. Los datos serán representados por una lista enlazada. Cada nodo estará formado por: id, texto y id del siguiente nodo.

```python
disco = ((4, "Unicornio", 2), (3, "Pegasus", 6), (1, "Dragón", 3), (5, "Griffin", 4), (2, "Minotaur", 1), (6, "Quimera", 5))

# Sintaxis: Python 3.9+
def desfragmentar_disco(disco: tuple[int]) -> tuple[int]:
    # Código
    return

desfragmentar_disco(disco)
# ((1, "Dragón", 3), (3, "Pegasus", 6), (6, "Quimera", 5), (5, "Griffin", 4), (4, "Unicornio", 2), (2, "Minotaur", 1))
```
