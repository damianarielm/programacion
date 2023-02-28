jugadores = int(input("Ingrese la cantidad de jugadores: "))
diamantes = int(input("Ingrese entre 10 y 15 diamantes: "))

if jugadores == 6:  leales, agentes, choferes, comodines = 1, 1, 1, 0
if jugadores == 7:  leales, agentes, choferes, comodines = 2, 1, 1, 0
if jugadores == 8:  leales, agentes, choferes, comodines = 3, 1, 1, 1
if jugadores == 9:  leales, agentes, choferes, comodines = 4, 1, 1, 1
if jugadores == 10: leales, agentes, choferes, comodines = 4, 2, 1, 1
if jugadores == 11: leales, agentes, choferes, comodines = 4, 2, 2, 2
if jugadores == 12: leales, agentes, choferes, comodines = 5, 2, 2, 2

print("1 - Ninguno.")
print("2 - Leal.")
print("3 - Agente.")
print("4 - Chofer.")
opcion = int(input("Jugador 2, elija rol a eliminar: "))
if opcion == 2: leales -= 1
if opcion == 3: agentes -= 1
if opcion == 4: choferes -= 1

for i in range(2, jugadores + 1):
    if diamantes: print(f"Diamantes: {diamantes}.")
    if leales: print(f"Leales: {leales}.")
    if agentes: print(f"Agentes: {agentes}.")
    if choferes: print(f"Choferes: {choferes}.")

    if diamantes: print("1 - Robar diamantes.")
    if leales: print("2 - Elegir rol leal.")
    if agentes: print("3 - Elegir rol agente.")
    if choferes: print("4 - Elegir rol chofer.")
    if diamantes + leales + agentes + choferes == 0 or i == jugadores:
        print("5 - Elegir rol pillo.")

    opcion = int(input(f"Jugador {i}, elija una opcion: "))
    if opcion == 1: diamantes -= int(input("Ingrese cantidad de diamantes: "))
    if opcion == 2: leales -= 1
    if opcion == 3: agentes -= 1
    if opcion == 4: choferes -= 1

    print("\n" * 99)

print(f"Diamantes: {diamantes}.")
print(f"Leales: {leales}.")
print(f"Agentes: {agentes}.")
print(f"Choferes: {choferes}.")
print(f"Comodines: {comodines}.")
print(f"Comienza el juego!")
