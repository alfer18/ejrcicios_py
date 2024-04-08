"""* Define una función que tome una cadena y retorne un diccionario con
la cantidad de apariciones de cada caracter en la cadena."""

def contar_caracteres(cadena):
    return {caracter: cadena.count(caracter) for caracter in cadena}

print(contar_caracteres("buenos dias Ana"))
