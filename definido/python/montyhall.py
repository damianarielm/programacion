from random import randint

simulaciones = int(input("Ingrese cantidad de simulaciones: "))
cambiando = 0
sincambio = 0

for s in range(simulaciones):
    auto = randint(1, 3)
    eleccion = randint(1, 3)
    if auto == eleccion: cambiando += 1
    if eleccion != auto: sincambio += 1

print(f"Se ganaron {cambiando} autos sin cambiar de desicion.")
print(f"Se ganaron {sincambio} autos cambiando de desicion.")
