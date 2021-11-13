from random import randint

incognita = randint(1, 100)
intento = -1

while incognita != intento:
    intento = int(input("Ingrese un numero: "))

    if incognita > intento:
        print("El numero es mas grande.")
    elif incognita < intento:
        print("El numero es mas chico.")

print("Correcto!")
