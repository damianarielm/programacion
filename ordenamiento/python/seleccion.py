from menorindice import menor_indice # Ejercicio previo
from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

for i in range(len(lista) - 1):
    m = menor_indice(lista[i:]) + i
    lista[i], lista[m] = lista[m], lista[i]

print(f"Lista ordenada: {lista}.")
