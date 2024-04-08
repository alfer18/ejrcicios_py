"""Define una función que reciba un número y retorne la suma de sus dí
gitos al cubo."""

def suma_cubos_digitos(n):
    return sum(int(digit)**3 for digit in str(n))
print(suma_cubos_digitos(123))
