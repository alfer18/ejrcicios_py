"""Define una función que reciba una lista de números y retorne el seg
undo número más grande de la lista."""

def segundo_maximo(lista):
    return sorted(set(lista), reverse=True)[1]
print(segundo_maximo([12, 42, 13, 46, 38]))
