from random import shuffle
from permutacion import permutacion # Ejercicio previo
from verificar import esta_ordenada # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

while not esta_ordenada(lista):
    shuffle(lista)

print(f"Lista ordenada: {lista}.")
