lista = [1, 2, 4, 6, 55, 190, 200, 800, 1000, 12000]

print(f"Lista: {lista}.")
n = int(input("Ingrese numero a buscar: "))

izquierda = 0
derecha = len(lista) - 1

while izquierda <= derecha:
    medio = izquierda + (derecha - izquierda) // 2

    if lista[medio] == n:
        print(f"El elemento se encuentra en la posicion {medio + 1}.")
        derecha = -1
    elif lista[medio] < n:
        izquierda = medio + 1
    else:
        derecha = medio - 1

if derecha != -1: print("El elemento no se encuentra.")
