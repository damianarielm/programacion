from random import randint
from time import sleep

simon, jugador = "", ""

while simon == jugador:
    simon += str(randint(1, 4))

    for letra in simon:
        print("\n" * 99)
        print(letra)
        sleep(0.5)
        print("\n" * 99)
        sleep(0.5)


    jugador = input("Repita la secuencia: ")

print(f"Perdiste! La secuencia era: {simon}.")
