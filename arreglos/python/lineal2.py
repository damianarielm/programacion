lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]
print(f"Lista: {lista}.")

buscar = int(input("Ingrese numero a buscar: "))

if buscar in lista:
    print(f"El numero se encuentra en la posicion: {lista.index(buscar)}.")
else:
    print("El numero no se encuentra.")
