from permutacion import permutacion # Ejercicio previo
from insertar2 import insertar_en_orden # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

for i in range(len(lista)):
    lista = insertar_en_orden(lista[:i], lista[i]) + lista[i + 1:]

print(f"Lista ordenada: {lista}.")
