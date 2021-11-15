[[_TOC_]]

## Numeros naturales

### Python

```python
maximo = int(input("Ingrese el maximo: "))

for numero in range(maximo + 1):
    print(numero)
```

## Factores

### Python

```python
n = int(input("Ingrese un numero: "))

for factor in range(1, n + 1):
    if n % factor == 0:
        print(factor)
```

## Binario a decimal

### Python

```python
n = input("Ingrese un numero en binario: ")
decimal = 0

for i, digito in enumerate(n):
    if digito == "1":
        decimal += 2 ** (len(n) - 1 - i)

print(f"El numero en decimal es: {decimal}.")
```

```python
n = input("Ingrese un numero en binario: ")

print(f"El numero en decimal es: {int(n, 2)}.")
```

## Fizzbuzz

Fizz buzz is a group word game for children to teach them about division.
Players take turns to count incrementally, replacing any number divisible by
three with the word "fizz", and any number divisible by five with the word
"buzz".

### Python

```python
maximo = int(input("Ingrese el maximo: "))

for numero in range(1, maximo + 1):
    if numero % 15 == 0: print("fizzbuzz")
    elif numero % 3 == 0: print("fizz")
    elif numero % 5 == 0: print("buzz")
    else: print(numero)
```

```python
maximo = int(input("Ingrese el maximo: "))

for numero in range(1, maximo + 1):
    respuesta = ""
    if numero % 3 == 0: respuesta += "fizz"
    if numero % 5 == 0: respuesta += "buzz"
    print(numero if not respuesta else respuesta)
```

## Sumatoria de naturales

### Python

```python
primero = int(input("Ingrese el primer numero: "))
ultimo = int(input("Ingrese el ultimo numero: "))

suma = 0
for numero in range(primero, ultimo + 1):
    suma += numero

print(f"La suma es: {suma}.")
```

```python
primero = int(input("Ingrese el primer numero: "))
ultimo = int(input("Ingrese el ultimo numero: "))

suma = (primero + ultimo) * (ultimo - primero + 1) / 2

print(f"La suma es: {suma}.")
```

```python
primero = int(input("Ingrese el primer numero: "))
ultimo = int(input("Ingrese el ultimo numero: "))

print(f"La suma es: {sum(range(primero, ultimo + 1))}.")
```

## Factorial

El factorial de un entero positivo n, el factorial de n o n factorial se define
en principio como el producto de todos los números enteros positivos desde 1
(es decir, los números naturales) hasta n.

La operación de factorial aparece en muchas áreas de las matemáticas,
particularmente en combinatoria y análisis matemático. De manera fundamental el
factorial de n representa el número de formas distintas de ordenar n objetos
distintos (elementos sin repetición).

### Python

```python
n = int(input("Ingrese un numero: "))

factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(f"El factorial es: {factorial}.")
```

## Trigo y Ajedrez

Al noroeste de la India (seguramente en el actual Pakistán o Afganistán), había
un poderoso brahmán llamado Rai Bhalit, tan rico y rodeado de tantos placeres
que de ninguno de ellos podía gozar. Ordenó al más inteligente de sus
sirvientes, llamado Sisa, que creara un juego capaz de entretenerle. Pasado
algún tiempo Sisa presentó a su señor el ajedrez, un juego que emulaba la
guerra y que se jugaba en un tablero con sesenta y cuatro casillas,
alternativamente blancas y negras dispuestas en ocho filas y ocho columnas. El
brahmán quedó tan encantado que le permitió escoger su recompensa. Sisa le
dijo: "Señor, soy hombre modesto, y me conformaría con que me paguéis un grano
de trigo por el primer cuadrado, dos por el segundo, cuatro en el tercero, ocho
en el cuarto, etc.". El brahmán, encantado por la modesta petición de Sisa
accedió en seguida, pero su alegría pronto se trocaría en ira cuando se dio
cuenta de que ni con todo el trigo de su país alcanzaría a pagar semejante suma.

### Python

```python
granos = 1
total = 0
for i in range(64):
    total += granos
    granos *= 2

print(f"El total de granos es: {total}.")
```

```python
total = 0
for i in range(64):
    total += 2 ** i

print(f"El total de granos es: {total}.")
```

## Sucesion de Fibonacci

### Python

```python
fa = 1
fb = 1

for i in range(3, 33):
    print(fa)
    fi = fa + fb
    fa, fb = fb, fi
```

```python
phi = (1 + 5**0.5) / 2

for n in range(1, 10):
    print( (phi**n - (1 - phi)**n) // (5**0.5) )
```

## Maximo de 10 numeros

### Python

```python
maximo = int(input("Ingrese un numero: "))

for _ in range(10):
    numero = int(input("Ingrese otro numero: "))

    if numero > maximo: maximo = numero

print(f"El numero mayor es: {maximo}.")
```

```python
maximo = int(input("Ingrese un numero: "))

for _ in range(10):
    maximo = max(maximo, int(input("Ingrese otro numero: ")))

print(f"El numero mayor es: {maximo}.")
```

## Calculo de pi

En matemáticas, la fórmula de Leibniz sirve para el cálculo de π, nombrada así
en honor a Gottfried Leibniz.

Se conoce como producto de Wallis a una expresión utilizada para representar el
valor de π que fue descubierta por John Wallis en 1655.

### Python

```python
iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

pi = 0
for i in range(iteraciones):
    pi += (-1)**i / (2*i + 1)
pi *= 4

print(f"El valor calculado de pi es: {pi}.")
```

```python
iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

pi = 1
for i in range(1, iteraciones + 1):
    pi *= (2*i / (2*i - 1)) * (2*i / (2*i + 1))
pi *= 2

print(f"El valor calculado de pi es: {pi}.")
```

## Calculo de e

El número *e*, conocido en ocasiones como número de Euler o constante de
Napier, fue reconocido y utilizado por primera vez por el matemático escocés
John Napier, quien introdujo el concepto de logaritmo en el cálculo matemático.

Juega un papel importante en el cálculo y en el análisis matemático, en la
definición de la función más importante de la matemática, la función
exponencial, así como *pi*, lo es de la geometría y el número *i*, del
análisis complejo y del álgebra.

### Python

```python
iteraciones = int(input("Ingrese cantidad de iteraciones: "))

e = 1
factorial = 1
for i in range(1, iteraciones):
    e += 1 / factorial
    factorial *= i + 1

print(f"El valor de e es: {e}.")
```

## Numeros palindromos

Un palíndromo, también llamado palíndromo, palíndroma o palindroma, es una
palabra o frase que se lee igual en un sentido que en otro (por ejemplo; Ana,
Anna, Otto). Si se trata de números en lugar de letras, se llama capicúa.

### Python

```python
for n1 in range(1, 10):
    for n2 in range(10):
        for n3 in range(10):
            print(f"{n1}{n2}{n3}{n2}{n1}")
```

## Fichas de domino

El dominó es un juego de mesa en el que se juegan y emplean unas fichas
(baldosas) rectangulares, generalmente blancas por la cara y negras por el
revés, usualmente hay de diferentes colores, aunque existen muchas variantes.
Una de sus caras está dividida por dos cuadrados, cada uno de los cuales está
numerado normalmente mediante disposiciones de puntos como los dados.

### Python

```python
for n1 in range(7):
    for n2 in range(7):
        if n2 >= n1:
            print(f"[{n1}|{n2}]")
```

```python
for n1 in range(7):
    for n2 in range(n1, 7):
        print(f"[{n1}|{n2}]")
```

## Los cofres de Porcia

En *El mercader de Venecia*, de Shakespeare, Porcia tenía tres cofres, dentro
de uno de los cuales estaba el retrato de Porcia. El pretendiente tenía que
elegir uno de los cofres y si tenía suerte (o inteligencia) eligiría el que
tenía el retrato, pudiendo así pedir a Porcia por esposa. En la tapa de cada
cofre había una inscripción para ayudar al pretendiente a elegir sabiamente:

> Cofre 1: El retrato no está en este cofre.

> Cofre 2: El retrato no está aquí.

> Cofre 3: EL retrato no está en el cofre 1.

Porcia explicó al pretendiente que de los tres enunciados, a lo sumo uno era
verdad.

### Python

```python
for retrato in range(1, 3 + 1):
    cofre1 = retrato == 1
    cofre2 = retrato != 2
    cofre3 = retrato != 1

    solo1 = cofre1 and not cofre2 and not cofre3
    solo2 = not cofre1 and cofre2 and not cofre3
    solo3 = not cofre1 and not cofre2 and cofre3
    ninguna = not cofre1 and not cofre2 and not cofre3

    if solo1 or solo2 or solo3 or ninguna:
        print(f"El retrato esta en el cofre {retrato}.")
```

## Problema de Monty Hall

El concursante debe elegir una puerta entre tres (todas cerradas); el premio
consiste en llevarse lo que se encuentra detrás de la elegida. Se sabe con
certeza que tras una de ellas se oculta un automóvil, y tras las otras dos hay
cabras. Una vez que el concursante haya elegido una puerta y comunicado su
elección a los presentes, el presentador, que sabe lo que hay detrás de cada
puerta, abrirá una de las otras dos en la que haya una cabra. A continuación,
le da la opción al concursante de cambiar, si lo desea, de puerta (tiene dos
opciones). ¿Debe el concursante mantener su elección original o escoger la otra
puerta?

### Python

```python
from random import randint

simulaciones = int(input("Ingrese cantidad de simulaciones: "))
cambiando = 0
sincambio = 0

for _ in range(simulaciones):
    auto = randint(1, 3)
    eleccion = randint(1, 3)
    if auto == eleccion: sincambio += 1
    if eleccion != auto: cambiando += 1

print(f"Se ganaron {sincambio} autos sin cambiar de desicion.")
print(f"Se ganaron {cambiando} autos cambiando de desicion.")
```

## Mafia de Cuba

La habana, 29 de diciembre de 1955. Tras una comida organizada para sus
"fieles" secuaces, Don Alessandro comienza a hablar de los "negocios" en
progreso, cuando suena el teléfono de la habitación trasera del restaurante:
el padrino ha sido convocado a la oficina del presidente Batista, por lo que ha
de confiar su preciosa caja de puros a sus secuaces. Pocos saben que ésta tiene
un doble fondo y que bajo una primera capa de cigarros ¡se halla un
compartimento repleto de diamantes!

Cada jugador tendrá que coger la caja, abrirla y optar por traicionar al
padrino y robar algún diamante o seguir siendo un leal y "honesto" mafioso, ser
el chófer, un sicario o incluso un agente del FBI infiltrado (cogiendo la ficha
correspondiente).

Al caer la noche, el padrino recuperará la caja que ha pasado de mano en mano
para descubrir con rabia que sus diamantes han desaparecido.  Tendrá que
recuperar su tesoro sin dejar de castigar a los responsables, a los que
proporcionará unos preciosos zapatos de cemento antes de tirarlos a la bahía.

Tras un acalorado debate el padrino tendrá que tomar unas cuantas decisiones
difíciles... ¿Encontrará, con la ayuda de sus fieles secuaces, todos sus
diamantes? ¿Perderá el respeto de los suyos haciendo acusaciones en falso?
¿Serán los ladrones más astutos que él? ¿o el FBI hará que todos terminen entre
las rejas?

### Python

```python
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
    for _ in range(99): print("")
    if diamantes: print(f"Diamantes: {diamantes}.")
    if leales: print(f"Leales: {leales}.")
    if agentes: print(f"Agentes: {agentes}.")
    if choferes: print(f"Choferes: {choferes}.")

    print("0 - Pasar.")
    if diamantes: print("1 - Robar diamantes.")
    if leales: print("2 - Elegir rol leal.")
    if agentes: print("3 - Elegir rol agente.")
    if choferes: print("4 - Elegir rol chofer.")

    opcion = int(input(f"Jugador {i}, elija una opcion: "))

    if opcion == 1: diamantes -= int(input("Ingrese cantidad de diamantes: "))
    if opcion == 2: leales -= 1
    if opcion == 3: agentes -= 1
    if opcion == 4: choferes -= 1

for _ in range(99): print("")
print(f"Diamantes: {diamantes}.")
print(f"Leales: {leales}.")
print(f"Agentes: {agentes}.")
print(f"Choferes: {choferes}.")
print(f"Comodines: {comodines}.")
print(f"Comienza el juego!")
input("Ingrese enter para borrar la pantalla.")
for _ in range(99): print("")
```
