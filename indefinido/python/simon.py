from random import randint
from time import sleep

simon, jugador = "", ""

while simon == jugador:
    simon += str(randint(1, 4))

    for letra in simon:
        for _ in range(100): print("")
        print(letra)
        sleep(0.5)
        for _ in range(100): print("")
        sleep(0.5)


    jugador = input("Repita la secuencia: ")

print(f"Perdiste! La secuencia era: {simon}.")
