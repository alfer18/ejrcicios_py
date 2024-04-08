"""Define una función que reciba un número y retorne su representación
en binario.
"""
def a_binario(n):
    return bin(n).replace("0b","")
print(a_binario(4))
