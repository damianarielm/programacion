from random import randint

simulaciones = int(input("Ingrese cantidad de simulaciones: "))
cambiando = 0
sincambio = 0

for _ in range(simulaciones):
    auto = randint(1, 3)
    eleccion = randint(1, 3)
    if auto == eleccion: sincambio += 1
    if eleccion != auto: cambiando += 1

print(f"Se ganaron {sincambio} autos sin cambiar de desicion.")
print(f"Se ganaron {cambiando} autos cambiando de desicion.")
