from random import choice

lugares  = ["avion", "banco", "barco pirata", "carpa de circo", "catedral"]
lugares += ["ejercito de cruzadas", "embajada", "escuela", "estacion espacial"]
lugares += ["estacion polar", "estacion de policia", "estacion de servicios"]
lugares += ["estudio de peliculas", "fiesta de trabajo", "hospital", "hotel"]
lugares += ["playa", "restaurant", "submarino", "supermercado", "teatro"]
lugares += ["spa", "transatlantico", "tren de pasajeros", "universidad"]

lugar = choice(lugares)
cantidad = int(input("Ingrese cantidad de jugadores: "))

jugadores = []
for i in range(cantidad):
    jugadores += [input(f"Jugador {i + 1} ingrese su nombre: ")]

espia = choice(jugadores)

for jugador in jugadores:
    input(f"\n{jugador}, presiona enter para ver tu rol.")
    if jugador == espia:
        print("Rol: espia.")
    else:
        print(f"Ubicacion: {lugar}.")
    input("Presione enter para borrar la pantalla.")
    for _ in range(100): print("")

print(f"Lista de lugares: {lugares}.")
print("\nComienza el juego!")
input("Presiona enter para revelar los roles.")
print(f"\nEspia: {espia}.")
print(f"Lugar: {lugar}.")
