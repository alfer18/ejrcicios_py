"""Ejercicio 5: Define una función que tome una cadena y cuente el número de
vocales en la cadena."""

def contar_vocales(cadena):
    return sum(1 for letra in cadena if letra.lower() in 'aeiou')
print(contar_vocales('Buenos dias'))