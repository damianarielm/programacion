from random import randint

print("1 - Piedra.")
print("2 - Papel.")
print("3 - Tijera.")
jugador = int(input("Elija una opcion: "))

computadora = randint(1, 3)
print(f"Computadora elige: {computadora}.\n")

if computadora == jugador:
    print("Empate.")
elif computadora == 1:
    if jugador == 2:
        print("Ganaste!")
    else:
        print("Perdiste.")
elif computadora == 2:
    if jugador == 3:
        print("Ganaste!")
    else:
        print("Perdiste.")
else:
    if jugador == 1:
        print("Ganaste!")
    else:
        print("Perdiste.")
