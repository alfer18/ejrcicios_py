"""Define una función que tome dos listas y retorne la lista de elemen
tos que no están en ambas listas."""

def elementos_no_comunes(lista1, lista2):
    return list(set(lista1) ^ set(lista2))
print(elementos_no_comunes([1, 2, 3, 4], [3, 4, 5]))
