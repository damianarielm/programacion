from itertools import permutations
from verificar import esta_ordenada # Ejercicio previo
from permutacion import permutacion # Ejercicio previo

def permutation_sort(lista):
    for permutacion in permutations(lista):
        if esta_ordenada(permutacion):
            return permutacion

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")
print(f"Lista ordenada: {permutation_sort(lista)}.")
