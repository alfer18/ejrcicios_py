"""Ejercicio 6:  Define una función que tome una lista y un número n, y retorne los
primeros n elementos de la lista."""

def primeros_n_elementos(lista, n):
    return lista[:n]

print(primeros_n_elementos([1, 2, 3, 4], 3))
