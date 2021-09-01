from random import randint

incognita = str(randint(1000, 10000))
pregunta = ""

while pregunta != incognita:
    pregunta = input("Ingrese un numero de cuatro cifras: ")

    toros = vacas = 0
    for p, i in zip(pregunta, incognita):
        if p == i:
            toros += 1
        elif p in incognita:
            vacas += 1

        print(f"Toros: {toros}, vacas: {vacas}.")

print("Correcto!")
