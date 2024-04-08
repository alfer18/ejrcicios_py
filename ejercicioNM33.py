""" Escribe una función que reciba una lista de tuplas y retorne una lista
ordenada basada en el último elemento de cada tupla."""

def ordenar_por_ultimo_elemento(tuplas):
    return sorted(tuplas, key=lamba x: x[-1])

print(ordenar_por_ultimo_elemento([(1, 2), (3, 2), (4, 5)]))

