from random import shuffle

cartas = [ "If another player hands you food or drink, you may take their role card.", # Glutton
           "If you are the only player to clean up a game, you may take any other player's role card.", # Maid
           "If another player takes a picture of you, you may take their role card.", # Model
           "If another player hands you money, you may take their role card.", # Cheapskate
           "If another player sits in your seat, you may take their role card.", # King
           "If another player comments about the number of times you rolled dice off the table, you may take their role card.", # Klutz
           "If another player threatens to 'flip the table', you make take their role card.", # Clown
           "If another player refuses to play a game that at least two people want to play, you may take their role card.", # Critic
           "If you catch something thrown by another player, you may take their role card.", # Sport
           "If another player hands you a rulebook, you may take their role.", # Bookworm
           "If another player makes a phone call, you may take their role card.", # Busybody
           "If you successfully convince the group to play the same game twice in a row, you may take any player's role card.", # Old dog
           "If incorrectly called out, reveal yourself and keep this card as a point. You also gain the accuser's role card.", # Shadow
           "If you get someone to start playing music or change the existing music, you may take their role card.", # Maestro
           "If you can convince the group to play a game with a house rule, you may take any other player's role card.", # Crafter
           "If you get someone to give you a high five, you may take their role card.", # Frat boy
           "If you come in last place for two games in a row, you may take any other player's role card.", # Sore loser
           "If you win two games in a row, you may take any other player's role card.", # Champ
           "If you teach the group to play a new game, you may take any other player's role card." ] # Teacher
shuffle(cartas)

jugadores = int(input("Ingrese cantidad de jugadores: "))
nombres = []
for n in range(jugadores):
    nombres += [ input(f"Ingrese nombre del jugador {n + 1}: ") ]
    input(f"{cartas[n]}\nPresiona enter para continuar.")
    print("\n" * 99)

opcion = ""
while opcion != 0:
    print("\n0: Salir")
    for i, nombre in enumerate(nombres):
        print(f"{i + 1}: {nombre}.")

    opcion = int(input("Revelar rol: "))
    if opcion > 0:
        print(cartas[opcion - 1]) # 43
