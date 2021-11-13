[[_TOC_]]

## Cantidad de vocales

### Python

```python
texto = input("Ingrese un texto: ")

vocales = 0
for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales += 1

print(f"La cantidad de vocales es: {vocales}.")
```

```python
texto = input("Ingrese un texto: ")

vocales = 0
for letra in texto:
    if letra in "aeiou":
        vocales += 1

print(f"La cantidad de vocales es: {vocales}.")
```

```python
texto = input("Ingrese un texto: ")

vocales  = texto.count("a")
vocales += texto.count("e")
vocales += texto.count("i")
vocales += texto.count("o")
vocales += texto.count("u")

print(f"La cantidad de vocales es: {vocales}.")
```

## Codigo Morse

En 1837, Samuel Morse y Alfred Vail estaban trabajando en un sistema de
telégrafo eléctrico. Decidieron usar un método por el cual cada símbolo era
transmitido de forma individual como una combinación de rayas y puntos, es
decir, señales telegráficas que se diferencian en el tiempo de duración de la
señal activa. Morse desarrolló una primera versión de su código en 1837 para
enviar números, que luego se debían convertir en mensajes completos usando un
libro de claves. Este código fue expandido por Vail en 1841 para incluir
letras y otros signos de puntuación, creando así el código actual. Morse
reconoció la idoneidad de este sistema y lo patentó junto con el telégrafo
eléctrico. Fue conocido como American Morse Code y utilizado en la primera
transmisión por telégrafo.

### Python

```python
texto = input("Ingrese texto: ")
codigo = ""

for letra in texto:
    if letra == "a": codigo += ".- "
    elif letra == "b": codigo += "-... "
    elif letra == "c": codigo += "-.-. "
    elif letra == "d": codigo += "-.. "
    elif letra == "e": codigo += ". "
    elif letra == "f": codigo += "..-. "
    elif letra == "g": codigo += "--. "
    elif letra == "h": codigo += ".... "
    elif letra == "i": codigo += ".. "
    elif letra == "j": codigo += ".--- "
    elif letra == "k": codigo += "-.- "
    elif letra == "l": codigo += ".-.. "
    elif letra == "m": codigo += "-- "
    elif letra == "n": codigo += "-. "
    elif letra == "o": codigo += "--- "
    elif letra == "p": codigo += ".--. "
    elif letra == "q": codigo += "--.- "
    elif letra == "r": codigo += ".-. "
    elif letra == "s": codigo += "... "
    elif letra == "t": codigo += "- "
    elif letra == "u": codigo += "..- "
    elif letra == "v": codigo += "...- "
    elif letra == "w": codigo += ".-- "
    elif letra == "x": codigo += "-..- "
    elif letra == "y": codigo += "-.-- "
    elif letra == "z": codigo += "--.. "
    else: codigo += letra

print(f"El cifrado es: {codigo}")
```

```python
texto = input("Ingrese texto: ")

texto = texto.replace("a", ".- ")
texto = texto.replace("b", "-... ")
texto = texto.replace("c", "-.-. ")
texto = texto.replace("d", "-.. ")
texto = texto.replace("e", ". ")
texto = texto.replace("f", "..-. ")
texto = texto.replace("g", "--. ")
texto = texto.replace("h", ".... ")
texto = texto.replace("i", ".. ")
texto = texto.replace("j", ".--- ")
texto = texto.replace("k", "-.- ")
texto = texto.replace("l", ".-.. ")
texto = texto.replace("m", "-- ")
texto = texto.replace("n", "-. ")
texto = texto.replace("o", "--- ")
texto = texto.replace("p", ".--. ")
texto = texto.replace("q", "--.- ")
texto = texto.replace("r", ".-. ")
texto = texto.replace("s", "... ")
texto = texto.replace("t", "- ")
texto = texto.replace("u", "..- ")
texto = texto.replace("v", "...- ")
texto = texto.replace("w", ".-- ")
texto = texto.replace("x", "-..- ")
texto = texto.replace("y", "-.-- ")
texto = texto.replace("z", "--.. ")

print(f"El cifrado es: {texto}")
```

## Fuerza bruta

En criptografía, se denomina ataque de fuerza bruta a la forma de recuperar una
clave probando todas las combinaciones posibles hasta encontrar aquella que
permite el acceso.

### Python

```python
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for l1 in alfabeto:
    for l2 in alfabeto:
        for l3 in alfabeto:
            for l4 in alfabeto:
                print(l1 + l2 + l3 + l4)
```

## Busqueda lineal

En informática, la búsqueda lineal o la búsqueda secuencial es un método para
encontrar un valor objetivo dentro de una lista.Ésta comprueba secuencialmente
cada elemento de la lista para el valor objetivo hasta que es encontrado o
hasta que todos los elementos hayan sido comparados.

### Python

```python
lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]
print(f"Lista: {lista}.")

buscar = int(input("Ingrese numero a buscar: "))

indice = -1
for i, numero in enumerate(lista):
    if numero == buscar:
        indice = i

if indice == -1:
    print("El numero no se encuentra.")
else:
    print(f"El numero se encuentra en la posicion: {indice}.")
```

```python
lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]
print(f"Lista: {lista}.")

buscar = int(input("Ingrese numero a buscar: "))

if buscar in lista:
    print(f"El numero se encuentra en la posicion: {lista.index(buscar)}.")
else:
    print("El numero no se encuentra.")
```

## Cadena reversa

### Python

```python
texto = input("Ingrese un texto: ")

print("La cadena reversa es:", end = " ")
for indice in range(len(texto)):
    print(f"{texto[len(texto) - 1 - indice]}", end = "")
```

```
texto = input("Ingrese un texto: ")

print("La cadena reversa es:", end = " ")
for indice in range(len(texto) - 1, -1, -1):
    print(f"{texto[indice]}", end = "")
```

```python
texto = input("Ingrese un texto: ")

print("La cadena reversa es:", end = " ")
for indice in range(1, len(texto) + 1):
    print(f"{texto[-indice]}", end = "")
```

```python
texto = input("Ingrese un texto: ")
print(f"La cadena reversa es: {texto[::-1]}.")
```

## Cifrado Cesar

El cifrado César recibe su nombre en honor a Julio César, que, según Suetonio,
lo usó con un desplazamiento de tres espacios para proteger sus mensajes
importantes de contenido militar:

> "Si tenía que decir algo confidencial, lo escribía usando el cifrado, esto
> es, cambiando el orden de las letras del alfabeto, para que ni una palabra
> pudiera entenderse. Si alguien quiere decodificarlo, y entender su
> significado, debe sustituir la cuarta letra del alfabeto, es decir, la D por
> la A, y así con las demás."

### Python

```python
alfabeto = "abcdefghijklmnopqrstuvwxyz"

texto = input("Ingrese un texto: ")
desplazamiento = int(input("Ingrese desplazamiento: "))
cifrado = ""

for letra in texto:
    indice = (alfabeto.index(letra) + desplazamiento) % len(alfabeto)
    cifrado += alfabeto[indice]

print(f"El texto cifrado es: {cifrado}.")
```

## Pretense

It's board game night! Players are dealt roles and have the entire night to
complete their secret objective. By the end of the night, the truth will come
out.

*Pretense* is a game night social metagame, essentially a game that you play
DURING other games. You have a secret role and a secret objective, and if you
accomplish it, you gain a point AND you steal someone's role. With that role
you can try to gain more points and more roles. The game plays from 2-12 and is
great on a good-sized game night with about 5-6 people.

### Python

```python
from random import shuffle

cartas = [ "If another player hands you food or drink, you may take their role card.", # Glutton
           "If you are the only player to clean up a game, you may take any other player's role card.", # Maid
           "If another player takes a picture of you, you may take their role card.", # Model
           "If another player hands you money, you may take their role card.", # Cheapskate
           "If another player sits in your seat, you may take their role card." # King
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
    nombre = input(f"Ingrese nombre del jugador {n + 1}: ")
    nombres += [ nombre ]

for i, nombre in enumerate(nombres):
    input(f"\n{nombre} presiona enter para revelar tu rol.")
    input(f"{cartas[i]}\nPresiona enter para continuar.")
    for _ in range(100): print("")

opcion = ""
while opcion != 0:
    print("\n0: Salir")
    for i, nombre in enumerate(nombres):
        print(f"{i + 1}: {nombre}.")

    opcion = int(input("Revelar rol: "))
    if opcion > 0:
        print(cartas[opcion - 1])
```

## Spyfall

Spyfall is played over several rounds, and at the start of each round all
players receive cards showing the same location — a casino, a traveling circus,
a pirate ship, or even a space station — except that one player receives a card
that says "Spy" instead of the location. Players then start asking each other
questions — "Why are you dressed so strangely?" or "When was the last time we
got a payday?" or anything else you can come up with — trying to guess who
among them is the spy. The spy doesn't know where he is, so he has to listen
carefully. When it's his time to answer, he'd better create a good story!

At any time during a round, one player may accuse another of being a spy. If
all other players agree with the accusation, the round ends and the accused
player has to reveal his identity. If the spy is uncovered, all other players
score points. However, the spy can himself end a round by announcing that he
understands what the secret location is; if his guess is correct, only the spy
scores points.

### Python

```python
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
```

## Busqueda binaria

En ciencias de la computación y matemáticas, la búsqueda binaria, también
conocida como búsqueda de intervalo medio o búsqueda logarítmica, es un
algoritmo de búsqueda que encuentra la posición de un valor en un array
ordenado. Compara el valor con el elemento en el medio del array, si no son
iguales, la mitad en la cual el valor no puede estar es eliminada y la búsqueda
continúa en la mitad restante hasta que el valor se encuentre.

### Python

```python
lista = [1, 2, 4, 6, 55, 190, 200, 800, 1000, 12000]

print(f"Lista: {lista}.")
buscar = int(input("Ingrese numero a buscar: "))

izquierda = 0
derecha = len(lista) - 1

while izquierda <= derecha:
    medio = izquierda + (derecha - izquierda) // 2

    if lista[medio] == buscar:
        print(f"El elemento se encuentra en la posicion {medio + 1}.")
        derecha = -1
    elif lista[medio] < buscar:
        izquierda = medio + 1
    else:
        derecha = medio - 1

if derecha != -1: print("El elemento no se encuentra.")
```

## Ordenamiento de burbuja

La Ordenación de burbuja (Bubble Sort en inglés) es un sencillo algoritmo de
ordenamiento. Funciona revisando cada elemento de la lista que va a ser
ordenada con el siguiente, intercambiándolos de posición si están en el orden
equivocado. Es necesario revisar varias veces toda la lista hasta que no se
necesiten más intercambios, lo cual significa que la lista está ordenada.

### Python

```python
lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(f"Lista ordenada: {lista}.")
```

## Ordenamiento por insercion

El ordenamiento por inserción (insertion sort en inglés) es una manera muy
natural de ordenar para un ser humano, y puede usarse fácilmente para ordenar
un mazo de cartas numeradas en forma arbitraria.

Inicialmente se tiene un solo elemento, que obviamente es un conjunto ordenado.
Después, cuando hay *k* elementos ordenados de menor a mayor, se toma el
elemento *k+1* y se compara con todos los elementos ya ordenados, deteniéndose
cuando se encuentra un elemento menor (todos los elementos mayores han sido
desplazados una posición a la derecha) o cuando ya no se encuentran elementos
(todos los elementos fueron desplazados y este es el más pequeño). En este
punto se inserta el elemento *k+1* debiendo desplazarse los demás elementos.

### Python

```python
lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

for i, n in enumerate(lista):
    while i > 0 and lista[i - 1] > n:
        lista[i] = lista[i - 1]
        i -= 1

    lista[i] = n

print(f"Lista ordenada: {lista}.")
```

## Ta-Te-Ti

El tres en línea, es un juego de lápiz y papel entre dos jugadores: O y X, que
marcan los espacios de un tablero de 3×3 alternadamente.

Cada jugador solo debe colocar su símbolo una vez por turno y no debe ser sobre
una casilla ya jugada. En caso de que el jugador haga trampa el ganador será el
otro. Se debe conseguir realizar una línea recta o diagonal por símbolo.

### Python

```python
tablero = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
turno = 0
fin = False

for fila in tablero: print(fila)
while not fin:
    print(f"Turno: jugador {turno + 1}")
    fila = int(input("Ingrese fila: ")) - 1
    columna = int(input("Ingrese columna: ")) - 1

    if not tablero[fila][columna]:
        tablero[fila][columna] = turno + 1
        turno = (turno + 1) % 2

    for fila in tablero: print(fila)

    if 0 < tablero[0][0] == tablero[0][1] == tablero[0][2]: fin = True
    if 0 < tablero[1][0] == tablero[1][1] == tablero[2][2]: fin = True
    if 0 < tablero[2][0] == tablero[2][1] == tablero[2][2]: fin = True
    if 0 < tablero[0][0] == tablero[1][0] == tablero[2][0]: fin = True
    if 0 < tablero[0][1] == tablero[1][1] == tablero[2][1]: fin = True
    if 0 < tablero[0][2] == tablero[1][2] == tablero[2][2]: fin = True
    if 0 < tablero[0][0] == tablero[1][1] == tablero[2][2]: fin = True
    if 0 < tablero[0][2] == tablero[1][1] == tablero[2][0]: fin = True
    if 0 not in tablero[0] + tablero[1] + tablero[2]: fin = True
```

## Juego del 15

The 15 puzzle (also called Gem Puzzle, Boss Puzzle, Game of Fifteen, Mystic
Square and many others) is a sliding puzzle having 15 square tiles numbered
1–15 in a frame that is 4 tiles high and 4 tiles wide, leaving one unoccupied
tile position. Tiles in the same row or column of the open position can be
moved by sliding them horizontally or vertically, respectively. The goal of the
puzzle is to place the tiles in numerical order.

### Python

```python
tablero = [ [1, 2, 0, 3], [9, 8, 4, 7], [6, 5, 11, 12], [13, 10, 14, 15] ]
final = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0] ]

while tablero != final:
    for fila in tablero:
        for elemento in fila:
            print(f"{elemento:02d}", end = " ")
        print("")

    print("\n8 - Arriba.")
    print("4 - Izquierda.")
    print("6 - Derecha.")
    print("2 - Abajo.")
    movimiento = int(input("Ingrese un movimiento: "))

    for i, fila in enumerate(tablero):
        for j, elemento in enumerate(fila):
            if elemento == 0:
                x, y = i, j

    if movimiento == 8:
        tablero[x][y], tablero[x - 1][y] = tablero[x - 1][y], tablero[x][y]
    elif movimiento == 2:
        tablero[x][y], tablero[x + 1][y] = tablero[x + 1][y], tablero[x][y]
    elif movimiento == 4:
        tablero[x][y], tablero[x][y - 1] = tablero[x][y - 1], tablero[x][y]
    else:
        tablero[x][y], tablero[x][y + 1] = tablero[x][y + 1], tablero[x][y]

print("Ganaste!")
```

## Babylon

The game consists of twelve tiles in four colors, and the tiles are scattered
on the table at the start of play, creating twelve stacks that are each one
tile high. On a turn, you take one stack and place it on another stack that is
either (a) the same height or (b) topped by a tile of the same color. Stacks
cannot be divided. Players take turns until one player cannot make a move; that
player loses the game and the other player wins.

### Python

```python
pilas = ["♥"] * 3 + ["♦"] * 3 + ["♣"] * 3 + ["♠"] * 3

turno = 0
fin = False
while not fin:
    for i, pila in enumerate(pilas): print(f"{i}: {pila}")

    print(f"Turno jugador {turno + 1}.")
    origen = pilas[int(input("Ingrese pila de origen: "))]
    destino = pilas[int(input("Ingrese pila de destino: "))]

    if origen[-1] == destino[-1] or len(origen) == len(destino):
        pilas += [destino + origen]
        pilas.remove(origen)
        pilas.remove(destino)
    else:
        print("Movimiento invalido.")
        fin = True

    turno = (turno + 1) % 2

print(f"Gana el jugador {turno + 1}.")
```

## Nim

The Nimatron is a computer that allows one to play the game Nim. It was first
presented in April 1940 at the 1939 New York World's Fair purely as a form of
entertainment. Designed in the winter of 1939 by Edward Condon for the sole
purpose of entertaining, it is a digital computer composed of electromechanical
relays which allows the lighting of four lines of seven bulbs. Each player can
turn off one or more of them in any line, then the machine takes a turn, and so
on. The last to extinguish a light is the winner.

### Python

```python
montones =  ["*" * int(input("Ingrese cantidad del primer monton: "))]
montones += ["*" * int(input("Ingrese cantidad del segundo monton: "))]
montones += ["*" * int(input("Ingrese cantidad del tercer monton: "))]

turno = 0

while montones[0] or montones[1] or montones[2]:
    for i in range(len(montones)):
        print(f"{i + 1}: {montones[i]}")

    monton = int(input(f"Jugador {turno + 1}, elija un monton: ")) - 1

    if 0 <= monton <= 2 and montones[monton]:
        cantidad = int(input("Ingrese cantidad: "))

        if 0 < cantidad <= len(montones[monton]):
            montones[monton] = "*" * (len(montones[monton]) - cantidad)
            turno = (turno + 1) % 2
```

## Torres de Hanoi

> N. Claus de Siam vio en el gran templo de Benarés, debajo de una cúpula que
> marca el centro del mundo, tres varillas de diamante embutidas en una base
> de bronce, de la altura de 1 codo (unos 45 cm) y el grosor del cuerpo de una
> abeja. Sobre una de las varillas Dios ensartó, en el comienzo de los
> tiempos, 64 discos de oro puro; el mayor de todos apoyado sobre el bronce y
> los demás, cada vez más pequeños, apilados hasta el final de la varilla. Es
> la torre sagrada de Brahma. Día y noche los sacerdotes se turnan sobre las
> gradas del altar para trasladar la torre de la primera varilla a la tercera,
> respetando las antedichas reglas impuestas por Brahma. Cuando se complete la
> tarea la torre y los brahmanes colapsarán y acaecerá el fin del mundo.

### Python

```python
discos = int(input("Ingrese numero de discos: "))

torres = [ list(range(discos))[::-1], [], [] ]

while len(torres[2]) != discos:
    for i in range(len(torres)):
        print(f"Torre {i + 1}: {torres[i]}.")

    origen = int(input("Ingrese torre de origen: ")) - 1
    destino = int(input("Ingrese torre de destino: ")) - 1

    if origen < 4 and destino < 4 and torres[origen]:
        if not torres[destino] or torres[origen][-1] < torres[destino][-1]:
            torres[destino] += [ torres[origen].pop() ]

print("Ganaste!")
```

## Ahorcado

El ahorcado (también llamado colgado) es un juego de adivinanzas de lápiz y
papel para dos o más jugadores. Un jugador piensa en una palabra, frase u
oración y el otro trata de adivinarla según lo que sugiere por letras o dentro
de un cierto número de oportunidades.

### Python

```python
palabra = input("Ingrese una palabra: ")
respuesta = "_" * len(palabra)
errores = ""

for i in range(100): print("")

while respuesta != palabra and len(errores) < 7:
    print(respuesta)
    print(f"Errores: {errores}.")
    intento = input("Ingrese una letra: ")

    for i, letra in enumerate(palabra):
        if intento == letra:
            respuesta = respuesta[0:i] + intento + respuesta[i + 1:]

    if intento not in palabra: errores += intento

print(f"La palabra era: {palabra}.")
```

## Memoria

### Python

```python
from random import shuffle

dorso = "██"
valores = "A234567890JQK"
palos = "♥♤♢♧"
rojos = "♥♢"
coincidencias = 0

mazo = []
for valor in valores:
    for palo in palos:
        mazo += [valor + palo]
shuffle(mazo)

matriz = []
for i in range(len(palos)):
    matriz += [ mazo[len(valores) * i:len(valores) * (i+1)] ]

juego = []
for _ in palos:
    juego += [[dorso] * len(valores)]

while coincidencias < len(mazo) / 2:
    print("  1   2   3   4   5   6   7   8   9   10  11  12  13")
    for i, fila in enumerate(juego):
        print(f"{i + 1}", end = "")
        for elemento in fila:
            print(f" {elemento} ", end = "")
        print("\n")

    fila1 = int(input("Ingrese una fila: ")) - 1
    columna1 = int(input("Ingrese una columna: ")) - 1
    carta1 = matriz[fila1][columna1]
    print(f"\n{carta1}\n")

    fila2 = int(input("Ingrese una fila: ")) - 1
    columna2 = int(input("Ingrese una columna: ")) - 1
    carta2 = matriz[fila2][columna2]
    print(f"\n{carta2}\n")

    ambosRojos = carta1[1] in rojos and carta2[1] in rojos
    ambosNegros = carta1[1] not in rojos and carta2[1] not in rojos
    if carta1[0] == carta2[0] and (ambosRojos or ambosNegros):
        juego[fila1][columna1] = carta1
        juego[fila2][columna2] = carta2
        coincidencias += 1

print("Ganaste!")
```

## Quarto

Quarto! has a 4×4 board and 16 pieces. Each piece has four dichotomous
attributes – color, height, shape, and bold – so each piece is either white or
yellow, tall or short, square or cross, and bold or not. The object is to place
the fourth piece in a row in which all four pieces have at least one attribute
in common. The twist is that your opponent gets to choose the piece you place
on the board each turn.

### Python

```python
from colorama import Fore, Style

def mostrarTablero(tablero):
    print("\nTablero:")
    for fila in tablero:
        print(*[elemento[0] for elemento in fila])
    print("")

tablero = [ [" "] * 4 for _ in range(4) ]
piezas  = [ ("o" + Style.RESET_ALL, 0, 0, 0, 0) ]
piezas += [ (Style.BRIGHT + "o" + Style.RESET_ALL, 0, 0, 0, 1) ]
piezas += [ (Fore.YELLOW + "o" + Style.RESET_ALL, 0, 0, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "o" + Style.RESET_ALL, 0, 0, 1, 1) ]
piezas += [ ("O" + Style.RESET_ALL, 0, 1, 0, 0) ]
piezas += [ (Style.BRIGHT + "O" + Style.RESET_ALL, 0, 1, 0, 1) ]
piezas += [ (Fore.YELLOW + "O" + Style.RESET_ALL, 0, 1, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "O" + Style.RESET_ALL, 0, 1, 1, 1) ]
piezas += [ ("x" + Style.RESET_ALL, 1, 0, 0, 0) ]
piezas += [ (Style.BRIGHT + "x" + Style.RESET_ALL, 1, 0, 0, 1) ]
piezas += [ (Fore.YELLOW + "x" + Style.RESET_ALL, 1, 0, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "x" + Style.RESET_ALL, 1, 0, 1, 1) ]
piezas += [ ("X" + Style.RESET_ALL, 1, 1, 0, 0) ]
piezas += [ (Style.BRIGHT + "X" + Style.RESET_ALL, 1, 1, 0, 1) ]
piezas += [ (Fore.YELLOW + "X" + Style.RESET_ALL, 1, 1, 1, 0) ]
piezas += [ (Style.BRIGHT + Fore.YELLOW + "X" + Style.RESET_ALL, 1, 1, 1, 1) ]

jugador = ganador = 0
while not ganador:
    mostrarTablero(tablero)
    for i, pieza in enumerate(piezas): print(f"{i}: {pieza[0]}")
    pieza = input(f"\nJugador {jugador+1} elija una pieza para su oponente: ")
    pieza = piezas.pop(int(pieza))

    jugador = (jugador + 1) % 2
    fila = int(input(f"\nJugador {jugador+1} ingrese fila: ")) - 1
    columna = int(input(f"Jugador {jugador+1} ingrese columna: ")) - 1
    tablero[fila][columna] = pieza

    d1 = [ tablero[0][0], tablero[1][1], tablero[2][2], tablero[3][3] ]
    d2 = [ tablero[0][3], tablero[1][2], tablero[2][1], tablero[3][0] ]
    for posibilidad in tablero + list(zip(*tablero)) + [d1, d2]:
        if " " not in posibilidad:
            for i in range(1, 5):
                if all(pieza[i] == posibilidad[0][i] for pieza in posibilidad):
                    ganador = jugador + 1

mostrarTablero(tablero)
print(f"Jugador {ganador} ha ganado!")
```
