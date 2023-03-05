from random import shuffle

def permutacion(cantidad):
    lista = list(range(cantidad))
    shuffle(lista)
    return lista

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    print(permutacion(cantidad))
