from random import randint

minimo = int(input("Ingrese el valor minimo: "))
maximo = int(input("Ingrese el valor maximo: "))
sorteo = randint(minimo, maximo)

print(f"El numero sorteado fue: {sorteo}.")
