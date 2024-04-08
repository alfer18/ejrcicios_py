""" Define una función que tome una cadena y determine si es un
palíndromo."""
def es_palindromo(cadena):
    return cadena == cadena[::-1]
print(es_palindromo("radar"))
