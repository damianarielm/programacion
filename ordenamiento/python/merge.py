from combinar import merge # Ejercicio previo
from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

def merge_sort(lista):
    if len(lista) <= 1: return lista

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    return merge(merge_sort(izquierda), merge_sort(derecha))

print(f"Lista ordenada: {merge_sort(lista)}.")
