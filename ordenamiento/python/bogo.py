from random import shuffle
from permutacion import permutacion # Ejercicio previo
from verificar import verificar # Ejercicio previo

def bogosort(lista):
    while not verificar(lista):
        shuffle(lista)

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")
bogosort(lista)
print(f"Lista ordenada: {lista}.")
