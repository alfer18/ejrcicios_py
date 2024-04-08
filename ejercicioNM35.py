""" Define una función que reciba un número entero y retorne True si es
un número primo, de lo contrario retorne False"""

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0,5) + 1):
        if num % i == 0:
            return False
        return True
    
    print(es_primo(15))
    