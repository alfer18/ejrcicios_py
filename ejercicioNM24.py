"""Define una función que tome un número y retorne un diccionario con
la tabla de multiplicar de ese número del 1 al 10."""

def tabla_de_multiplicar(numero):
    return {i: numero * i in range(1, 11)}
   
print(tabla_de_multiplicar(2))
