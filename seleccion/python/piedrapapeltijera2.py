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
    print("Ganaste!" if jugador == 2 else "Perdiste.")
elif computadora == 2:
    print("Ganaste!" if jugador == 3 else "Perdiste.")
else:
    print("Ganaste!" if jugador == 1 else "Perdiste.")
