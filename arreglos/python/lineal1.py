lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]
print(f"Lista: {lista}.")

buscar = int(input("Ingrese numero a buscar: "))

indice = -1
for i, numero in enumerate(lista):
    if numero == buscar:
        indice = i

if indice == -1:
    print("El numero no se encuentra.")
else:
    print(f"El numero se encuentra en la posicion: {indice}.")
