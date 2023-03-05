from permutacion import permutacion

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

for n in range(len(lista)):
    for i in range(len(lista) - n - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(f"Lista ordenada: {lista}.")
