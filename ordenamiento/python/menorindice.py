from permutacion import permutacion # Ejercicio previo

def menor_indice(lista):
    menor, indice = lista[0], 0
    for i, x in enumerate(lista):
        if x < menor:
            menor = x
            indice = i

    return indice

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    lista = permutacion(cantidad)
    print(f"La lista es: {lista}.")
    print(f"El indice del menor es: {menor_indice(lista)}.")
