"""Ejercicio 4: Define una función que tome un número y retorne la suma de sus
dígitos."""

def suma_digitos(n):
    return sum(int(digito) for digito in str(n))

print(suma_digitos(1234))