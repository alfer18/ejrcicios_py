"""Ejercicio 7: Define una función que tome una cadena y retorne la cantidad de
letras mayúsculas y minúsculas en la cadena."""

def contar_mayusculas_minusculas(cadena):
    mayusculas = sum(1 for letra in cadena if letra.isupper())
    minusculas = sum(1 for letra in cadena if letra.islower())

print(contar_mayusculas_minusculas("Buenas Noches"))
