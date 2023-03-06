from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [ n for n in lista if n < pivote ]
        mayores = [ n for n in lista if n > pivote ]
        return quick_sort(menores) + [ pivote ] + quick_sort(mayores)

print(f"Lista ordenada: {quick_sort(lista)}.")
