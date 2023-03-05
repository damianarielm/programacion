from random import shuffle

def permutacion(cantidad):
    lista = list(range(cantidad))
    shuffle(lista)
    return lista

cantidad = int(input("Ingrese la cantidad: "))
print(permutacion(cantidad))
