from random import randint

incognita = randint(1, 100)
pregunta = -1

while incognita != pregunta:
    pregunta = int(input("Ingrese un numero: "))

    if incognita > pregunta:
        print("El numero es mas grande.")
    elif incognita < pregunta:
        print("El numero es mas chico.")

print("Correcto!")
