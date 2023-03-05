from permutacion import permutacion

def burbuja(lista):
    for n in range(len(lista)):
        intercambios = False

        for i in range(len(lista) - n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambios = True

        if not intercambios:
            return lista

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")
print(f"Lista ordenada: {burbuja(lista)}.")
