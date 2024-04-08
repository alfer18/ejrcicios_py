"""Define una función que tome una lista y retorne la lista sin duplic
ados."""

def eliminar_duplicados(lista):
    return list(set(lista))

print(eliminar_duplicados([1, 1, 2, 3, 3, 4]))
