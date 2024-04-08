""" Define una función que reciba un número entero n y retorne una lista
con los n primeros números primos."""

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0,5) + 1):
        if num % i == 0:
             return True
    
def primeros_n_primos(n):
    primos = []
    numero = 2
    while len(primos) < n:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

print(primeros_n_primos(5))