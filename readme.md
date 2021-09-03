[[_TOC_]]

# Secuencial

* Constantes importantes
* Operadores aritmeticos
* Calculo de promedio
* Calculo de minutos y segundos
* Calculo de hipotenusa
* Teorema del coseno
* Distancia entre puntos
* Raices y vertice de una parabola
* Intercambio de variables
* Numeros romanos

# Seleccion

* Valor absoluto
* Paridad
* Signo
* Chequeo de vocales
* Ordenar numeros
* Determinacion de signo zodiacal
* Raices de un polinomio de grado 3
* Validacion y clasificacion de triangulos
* Validacion de fecha en año no bisiesto
* Chequeo de año bisiesto
* Maximo de 5 numeros

# Ciclo definido

* Numeros naturales
* Factores
* Codigo Morse
* Binario a decimal
* Fizzbuzz
* Cantidad de vocales
* Sumatoria de naturales
* Factorial
* Trigo y Ajedrez
* Sucesion de Fibonacci
* Maximo de 10 numeros
* Calculo de pi
* Calculo de e
* Numeros palindromos
* Fuerza bruta
* Los cofres de Porcia
* Problema de Monty Hall

# Ciclo indefinido

* Contraseña
* Decimal a binario
* Chequeo de primalidad
* Recaudacion del dia
* Menu
* Conjetura de Collatz
* Algoritmo de Euclides
* Calculadora
* Adivinar un numero
* Simon
* Toros y Vacas

# Arreglos

## Busqueda lineal

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

> El cifrado César recibe su nombre en honor a Julio César, que, según
> Suetonio, lo usó con un desplazamiento de tres espacios para proteger sus
> mensajes importantes de contenido militar:

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

## Spyfall

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

for _ in range(100): print("")
for jugador in jugadores:
    input(f"{jugador}, presiona enter para ver tu rol.")
    if jugador == espia:
        print("Rol: espia.")
    else:
        print(f"Ubicacion: {lugar}.")
    input("Presione enter para borrar la pantalla.")
    for _ in range(100): print("")

print("Lista de lugares:")
print(lugares)
print("\nComienza el juego!")
input("Presiona enter para revelar los roles.")
print(f"\nEspia: {espia}.")
print(f"Lugar: {lugar}.")
```

## Busqueda binaria

### Python

```python
lista = [1, 2, 4, 6, 55, 190, 200, 800, 1000, 12000]

print(f"Lista: {lista}.")
n = int(input("Ingrese numero a buscar: "))

izquierda = 0
derecha = len(lista) - 1

while izquierda <= derecha:
    medio = izquierda + (derecha - izquierda) // 2

    if lista[medio] == n:
        print(f"El elemento se encuentra en la posicion {medio + 1}.")
        derecha = -1
    elif lista[medio] < n:
        izquierda = medio + 1
    else:
        derecha = medio - 1

if derecha != -1: print("El elemento no se encuentra.")
```

## Ordenamiento de burbuja

### Python

```python
lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

for i in range(len(lista)):
    for j in range(0, len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(f"Lista ordenada: {lista}.")
```

## Ordenamiento por insercion

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

## Nim

> The Nimatron is a computer that allows one to play the game Nim. It was
> first presented in April 1940 at the 1939 New York World's Fair purely as a
> form of entertainment. Designed in the winter of 1939 by Edward Condon for
> the sole purpose of entertaining, it is a digital computer composed of
> electromechanical relays which allows the lighting of four lines of seven
> bulbs. Each player can turn off one or more of them in any line, then the
> machine takes a turn, and so on. The last to extinguish a light is the winner.

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

### Python

```python
palabra = input("Ingrese una palabra: ")
respuesta = "_" * len(palabra)
errores = ""

for i in range(100): print("")

while respuesta != palabra and len(errores) < 7:
    for letra in respuesta: print(f"{letra}", end = "")
    print(f"\nErrores: {errores}")
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

# Recursion

## Factorial

### Python

```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Ingrese un numero: "))

print(f"El factorial es: {factorial(n)}.")
```

## Sucesion de Fibonacci

### Python

```python
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(30):
    print(fibonacci(n))
```

## Algoritmo del Campesino Ruso

### Python

```python
def ruso(n1, n2):
    if n2 == 0:
        return 0
    elif n2 == 1:
        return n1
    elif n2 % 2 == 0:
        return 2 * n1 * (n2 // 2)
    else:
        return 2 * n1 * (n2 // 2) + n1

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

print(f"El producto es: {ruso(n1, n2)}.")
```

# Punteros

## strlen

## strcpy

## realloc

## Desbordamiento de buffer

### C

```c
// gcc password.c -fno-stack-protector

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define LEN 10

void main() {
    char password[LEN];
    char input[LEN];

    // Generacion de contraseña aleatoria
    srand(time(NULL));
    for (int i = 0; i < LEN; i++)
        password[i] = rand();

    // Lectura de contraseña por teclado
    printf("Ingrese la contraseña: ");
    scanf("%s", input);

    // Verificacion de contraseña
    if (!strncmp(input, password, LEN))
        printf("Contraseña correcta.\n");
    else
        printf("Contraseña incorrecta.\n");
}
```

# Otros

# Proyectos

## Corrector Ortografico

## Onirim

## Viernes

## Sliding puzzle

## Juego de la vida

## Sokoban

## Orchard

## Deep Space D6

## Cuatro en linea

## Quarto

## Batalla naval

## Reversi

## Oso

## Palm Island

## Shephy

## Zogar's Revenge

## Qwixx

## Sylvion

## Nautilion

## Castellion

## Sagrada

## Quien quiere ser millonario?
