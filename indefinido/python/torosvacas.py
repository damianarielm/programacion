from random import randint

incognita = str(randint(1000, 10000))
intento = ""

while intento != incognita:
    intento = input("Ingrese un numero de cuatro cifras: ")

    toros = vacas = 0
    for p, i in zip(intento, incognita):
        if p == i:
            toros += 1
        elif p in incognita:
            vacas += 1

        print(f"Toros: {toros}, vacas: {vacas}.")

print("Correcto!")
