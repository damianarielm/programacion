[[_TOC_]]

# Secuencial

## Constantes importantes

### Python

```python
print("El valor de pi es aproximadamente: 3.14159265359")
print("El valor de e es aproximadamente: 2.71828182846")
print("El valor de phi es aproximadamente: 1.618033988")
print("El valor de g es aproximadamente: 9.80665")
print("El valor de c es aproximadamente: 299792458")
```

## Operadores aritmeticos

### Python

```python
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2
resto = n1 % n2
entera = n1 // n2
potencia = n1 ** n2

print(f"La suma es {suma}.")
print(f"La resta es {resta}.")
print(f"El producto es {producto}.")
print(f"La division es {division}.")
print(f"El resto de la division es {resto}.")
print(f"La division entera es {entera}.")
print(f"La potencia es {potencia}.")
```

## Calculo de promedio

### Python

```python
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))
n3 = int(input("Ingrese otro numero: "))
n4 = int(input("Ingrese otro numero: "))
n5 = int(input("Ingrese otro numero: "))

promedio = (n1 + n2 + n3 + n4 + n5) / 5

print(f"El promedio es: {promedio}.")
```

## Calculo de minutos y segundos

### Python

```python
horas = int(input("Ingrese una cantidad de horas: "))

minutos = horas * 60
segundos = minutos * 60

print(f"La cantidad equivale a {minutos} minutos o {segundos} segundos.")
```

## Calculo de hipotenusa

### Python

```python
a = int(input("Ingrese el valor de un cateto: "))
b = int(input("Ingrese el valor del otro cateto: "))

hipotenusa = (a*a + b*b) ** 0.5

print(f"El valor de la hipotenusa es {hipotenusa}.")
```

## Teorema del coseno

### Python

```python
from math import cos

a = int(input("Ingrese el valor de un lado: "))
b = int(input("Ingrese el valor de un lado: "))
g = float(input("Ingrese el angulo que conforman en radianes: "))

c = (a*a + b*b + 2*a*b*cos(g)) ** 0.5

print(f"El lado restante vale {c}.")
```

## Distancia entre puntos

### Python

```python
x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"La distancia es: {distancia}.")
```

## Raices y vertice de una parabola

### Python

```python
a = int(input("Ingrese coeficiente principal: "))
b = int(input("Ingrese coeficiente lineal: "))
c = int(input("Ingrese termino independiente: "))

x1 = (-b + (b*b - 4*a*c) ** 0.5) / (2*a)
x2 = (-b - (b*b - 4*a*c) ** 0.5) / (2*a)
xv = -b / (2*a)
yv = a*xv*xv + b*xv + c

print(f"Las raices son {x1} y {x2}.")
print(f"El vertice es ({xv}, {yv}).")
```

## Intercambio de variables

### Python

```python
a = int(input("Ingrese el valor de la variable a: "))
b = int(input("Ingrese el valor de la variable b: "))

t = b
b = a
a = t

print(f"El valor de a es {a}, y el de b es {b}.")
```

```python
a = int(input("Ingrese el valor de la variable a: "))
b = int(input("Ingrese el valor de la variable b: "))

a, b = b, a

print(f"El valor de a es {a}, y el de b es {b}.")
```

## Numeros romanos

### Python

```python
n = int(input("Ingrese un numero menor a 4000: "))
romanos = ""

romanos, n = romanos + "M" * (n // 1000), n % 1000
romanos, n = romanos + "CM" * (n // 900), n % 900
romanos, n = romanos + "D" * (n // 500), n % 500
romanos, n = romanos + "CD" * (n // 400), n % 400
romanos, n = romanos + "C" * (n // 100), n % 100
romanos, n = romanos + "XC" * (n // 90), n % 90
romanos, n = romanos + "L" * (n // 50), n % 50
romanos, n = romanos + "XL" * (n // 40), n % 40
romanos, n = romanos + "X" * (n // 10), n % 10
romanos, n = romanos + "IX" * (n // 9), n % 9
romanos, n = romanos + "V" * (n // 5), n % 5
romanos, n = romanos + "IV" * (n // 4), n % 4
romanos, n = romanos + "I" * (n // 1), n % 1

print(romanos)
```

# Seleccion

## Valor absoluto

### Python

```python
n = int(input("Ingrese un numero: "))

if n >= 0:
    print(f"El valor absoluto es {n}.")
else:
    print(f"El valor absoluto es {-n}.")
```

```python
n = int(input("Ingrese un numero: "))
print(f"El valor absoluto es {a if n >= 0 else -n}.")
```

## Paridad

### Python

```python
n = int(input("Ingrese un numero: "))

if n % 2 == 0:
    print("El numero es par.")
else:
    print("El numero es impar.")
```

```python
n = int(input("Ingrese un numero: "))

if n / 2 == n // 2:
    print("El numero es par.")
else:
    print("El numero es impar.")
```

## Signo

### Python

```python
n = int(input("Ingrese un numero: "))

if n > 0:
    print("El numero es positivo.")
elif n == 0:
    print("El numero es cero.")
else:
    print("El numero es negativo")
```

## Chequeo de vocales

### Python

```python
letra = input("Ingrese una letra minuscula: ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("La letra es una vocal.")
else:
    print("La letra es una consonante.")
```

## Ordenar numeros

### Python

```python
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if n1 < n2 < n3: print(n1, n2, n3)
if n1 < n3 < n2: print(n1, n3, n2)
if n2 < n1 < n3: print(n2, n1, n3)
if n2 < n3 < n1: print(n2, n3, n1)
if n3 < n1 < n2: print(n3, n1, n2)
if n3 < n2 < n1: print(n3, n2, n1)
```

```python
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if n1 > n2: n1, n2 = n2, n1
if n2 > n3: n2, n3 = n3, n2
if n1 > n2: n1, n2 = n2, n1

print(n1, n2, n3)
```

## Determinacion de signo zodiacal

### Python

```python
dia = int(input("Ingrese el dia: "))
mes = int(input("Ingrese el mes: "))

if mes == 1:
    signo = "Capricornio" if dia < 20 else "Acuario"
elif mes == 2:
    signo = "Acuario" if dia < 19 else "Piscis"
elif mes == 3:
    signo = "Piscis" if dia < 21 else "Aries"
elif mes == 4:
    signo = "Aries" if dia < 20 else "Tauro"
elif mes == 5:
    signo = "Tauro" if dia < 21 else "Geminis"
elif mes == 6:
    signo = "Geminis" if dia < 21 else "Cancer"
elif mes == 7:
    signo = "Cancer" if dia < 23 else "Leo"
elif mes == 8:
    signo = "Leo" if dia < 23 else "Virgo"
elif mes == 9:
    signo = "Virgo" if dia < 23 else "Libra"
elif mes == 10:
    signo = "Libra" if dia < 23 else "Escorpio"
elif mes == 11:
    signo = "Escorpio" if dia < 22 else "Sagitario"
elif mes == 12:
    signo = "Sagitario" if dia < 22 else "Capricornio"

print(f"El signo es: {signo}.")
```

## Raices de un polinomio de grado 3

### Python

```python
from math import pi, cos, acos

a = int(input("Ingrese el coeficiente principal: "))
b = int(input("Ingrese el coeficiente cuadratico: "))
c = int(input("Ingrese el coeficiente lineal: "))
d = int(input("Ingrese el termino independiente: "))

p = (3*a*c - b*b) / (3*a*a)
q = (2*b*b*b - 9*a*b*c + 27*a*a*d) / (27*a*a*a)
t = acos( ((3*q) / (2*p)) * ((-3 / p)**0.5) )

z1 = 2 * ((-p/ 3)**0.5) * cos( (t + 2*0*pi) / 3 )
z2 = 2 * ((-p/ 3)**0.5) * cos( (t + 2*1*pi) / 3 )
z3 = 2 * ((-p/ 3)**0.5) * cos( (t + 2*2*pi) / 3 )

if q > 0:
    z1 *= -1
    z2 *= -1
    z3 *= -1

x1 = z1 - b / (3*a)
x2 = z2 - b / (3*a)
x3 = z3 - b / (3*a)

print(f"Las raices son {x1}, {x2} y {x3}.")
```

## Validacion y clasificacion de triangulos

### Python

```python
l1 = int(input("Ingrese el primer lado: "))
l2 = int(input("Ingrese el segundo lado: "))
l3 = int(input("Ingrese el tercer lado: "))

if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 = l1:
    print("No es un triangulo.")
else:
    if l1 == l2 == l3:
        print("Es un triangulo equilatero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Es un triangulo isoceles.")
    else:
        print("Es un triangulo escaleno.")
```

## Validacion de fecha en año no bisiesto

### Python

```python
mes = int(input("Ingrese el mes: "))

if 1 <= mes <= 12:
    dia = int(input("Ingrese el dia: "))

    if dia < 1 or dia > 31:
        print("Dia invalido.")
    else:
        if mes == 2 and dia > 28:
            print("Fecha invalida.")
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
            print("Fecha invalida.")
        else:
            print("Fecha valida.")
else:
    print("Mes invalido.")
```

## Chequeo de año bisiesto

### Python

```python
año = int(input("Ingrese el año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año es bisiesto.")
        else
            print("El año no es bisiesto.")
    else:
        print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
```

```python
año = int(input("Ingrese el año: "))

if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    print("El año es bisiesto.")
else
    print("El año es no bisiesto.")
```

## Maximo de 5 numeros

### Python

```python
maximo = int(input("Ingrese el primer numero: "))

segundo = int(input("Ingrese el segundo numero: "))
if segundo > maximo: maximo = segundo

tercero = int(input("Ingrese el tercer numero: "))
if tercero > maximo: maximo = tercero

cuarto = int(input("Ingrese el cuarto numero: "))
if cuarto > maximo: maximo = cuarto

quinto = int(input("Ingrese el quinto numero: "))
if quinto > maximo: maximo = quinto

print(f"El mas grande es {maximo}.")
```

# Ciclo definido

## Numeros naturales

### Python

```python
for n in range(100):
    print(n)
```

## Factores

### Python

```python
n = int(input("Ingrese un numero: "))

for factor in range(1, n + 1):
    if n % factor == 0:
        print(factor)
```

## Codigo Morse

> En 1837, Samuel Morse y Alfred Vail estaban trabajando en un sistema de
> telégrafo eléctrico. Decidieron usar un método por el cual cada símbolo era
> transmitido de forma individual como una combinación de rayas y puntos, es
> decir, señales telegráficas que se diferencian en el tiempo de duración de la
> señal activa. Morse desarrolló una primera versión de su código en 1837 para
> enviar números, que luego se debían convertir en mensajes completos usando un
> libro de claves. Este código fue expandido por Vail en 1841 para incluir
> letras y otros signos de puntuación, creando así el código actual. Morse
> reconoció la idoneidad de este sistema y lo patentó junto con el telégrafo
> eléctrico. Fue conocido como American Morse Code y utilizado en la primera
> transmisión por telégrafo.

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

## Fizzbuzz

### Python

```python
for n in range(20):
    if n % 15 == 0: print("fizzbuzz")
    elif n % 3 == 0: print("fizz")
    elif n % 5 == 0: print("buzz")
    else: print(n)
```

## Cantidad de vocales

### Python

```python
texto = input("Ingrese un texto: ")

vocales = 0
for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "u":
        vocales += 1

print(f"La cantidad de vocales es: {vocales}.")
```

## Suma de naturales

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

## Factorial

### Python

```python
n = int(input("Ingrese un numero: "))

factorial = 1
for i in range(2, n + 1):
    factorial *= i

print(f"El factorial es: {factorial}.")
```

## Trigo y Ajedrez

> Al noroeste de la India (seguramente en el actual Pakistán o Afganistán),
> había un poderoso brahmán llamado Rai Bhalit, tan rico y rodeado de tantos
> placeres que de ninguno de ellos podía gozar. Ordenó al más inteligente de
> sus sirvientes, llamado Sisa, que creara un juego capaz de entretenerle.
> Pasado algún tiempo Sisa presentó a su señor el ajedrez, un juego que
> emulaba la guerra y que se jugaba en un tablero con sesenta y cuatro
> casillas, alternativamente blancas y negras dispuestas en ocho filas y ocho
> columnas. El brahmán quedó tan encantado que le permitió escoger su
> recompensa. Sisa le dijo: "Señor, soy hombre modesto, y me conformaría con
> que me paguéis un grano de trigo por el primer cuadrado, dos por el segundo,
> cuatro en el tercero, ocho en el cuarto, etc.". El brahmán, encantado por la
> modesta petición de Sisa accedió en seguida, pero su alegría pronto se
> trocaría en ira cuando se dio cuenta de que ni con todo el trigo de su país
> alcanzaría a pagar semejante suma.

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

for i in range(10):
    n = int(input("Ingrese otro numero: "))

    if n > maximo: maximo = n

print(f"El numero mayor es: {maximo}.")
```

## Calculo de pi

### Python

```python
iteraciones = int(input("Ingrese la cantidad de iteraciones: "))

pi = 0
for i in range(iteraciones):
    pi += (-1)**i / (2*i + 1)
pi *= 4

print(f"El valor calculado de pi es: {pi}.")
```

## Calculo de e

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

### Python

```python
for n1 in range(1, 10):
    for n2 in range(10):
        for n3 in range(10):
            print(f"{n1}{n2}{n3}{n2}{n1}")
```

## Fuerza bruta

### Python

```python
alfabeto = "abcdefghijklmnopqrstuvwxyz"

for l1 in alfabeto:
    for l2 in alfabeto:
        for l3 in alfabeto:
            for l4 in alfabeto:
                print(l1 + l2 + l3 + l4)
```

## Los cofres de Porcia

> En *El mercader de Venecia*, de Shakespeare, Porcia tenía tres cofres, dentro
> de uno de los cuales estaba el retrato de Porcia. El pretendiente tenía que
> elegir uno de los cofres y si tenía suerte (o inteligencia) eligiría el que
> tenía el retrato, pudiendo así pedir a Porcia por esposa. En la tapa de cada
> cofre había una inscripción para ayudar al pretendiente a elegir sabiamente:

> Cofre 1: El retrato no está en este cofre.

> Cofre 2: El retrato no está aquí.

> Cofre 3: EL retrato no está en el cofre 1.

> Porcia explicó al pretendiente que de los tres enunciados, a lo sumo uno era
> verdad.

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

> El concursante debe elegir una puerta entre tres (todas cerradas); el premio
> consiste en llevarse lo que se encuentra detrás de la elegida. Se sabe con
> certeza que tras una de ellas se oculta un automóvil, y tras las otras dos
> hay cabras. Una vez que el concursante haya elegido una puerta y comunicado
> su elección a los presentes, el presentador, que sabe lo que hay detrás de
> cada puerta, abrirá una de las otras dos en la que haya una cabra. A
> continuación, le da la opción al concursante de cambiar, si lo desea, de
> puerta (tiene dos opciones). ¿Debe el concursante mantener su elección
> original o escoger la otra puerta?

### Python

```python
from random import randint

simulaciones = int(input("Ingrese cantidad de simulaciones: "))
cambiando = 0
sincambio = 0

for s in range(simulaciones):
    auto = randint(1, 3)
    eleccion = randint(1, 3)
    if auto == eleccion: cambiando += 1
    if eleccion != auto: sincambio += 1

print(f"Se ganaron {cambiando} autos sin cambiar de desicion.")
print(f"Se ganaron {sincambio} autos cambiando de desicion.")
```

# Ciclo indefinido

## Contraseña

### Python

```python
contraseña = "abc123"
intento = ""

while intento != contraseña:
    intento = input("Ingrese una contraseña: ")

print("Contraseña correcta.")
```

## Decimal a binario

### Python

```python
n = int(input("Ingrese un numero positivo: "))
binario = ""

while n >= 1:
    binario = str(n % 2) + binario
    n //= 2

print(f"El numero en binario es: {binario}.")
```

## Chequeo de primalidad

### Python

```python
n = int(input("Ingrese un numero mayor a 1: "))
factor = 2
primo = True

while n >= 4 and factor <= int(n ** 0.5) + 1 and primo:
    if n % factor == 0: primo = False
    else: factor += 1

print(f"El numero{' no' if not primo else ''} es primo.")
```

## Recaudacion del dia

### Python

```python
venta = -1
total = 0

while venta != 0:
    venta = int(input("Ingrese el valor de la venta (0 para salir): "))
    total += venta

print(f"El total de ventas es: {total}.")
```

## Menu

### Python

```python
opcion = ""
while opcion != "0":
    print("Menu principal")
    print("1 - Menu secundario")
    print("2 - Menu terciario")
    print("0 - Salir")
    opcion = input("Ingrese una opcion: ")
    print("")

    if opcion == "1":
        while opcion != "0":
            print("Menu secundario")
            print("1 - Opcion 1")
            print("2 - Opcion 2")
            print("0 - Volver")
            opcion = input("Ingrese una opcion: ")
            print("")
        opcion = ""
    elif opcion == "2":
        while opcion != "0":
            print("Menu terciario")
            print("1 - Opcion 1")
            print("2 - Opcion 2")
            print("0 - Volver")
            opcion = input("Ingrese una opcion: ")
            print("")
        opcion = ""
```

## Conjetura de Collatz

### Python

```python
n = int(input("Ingrese un numero: "))

while n != 1:
if n % 2 == 0:
n //= 2
else:
n = 3*n + 1

print(n)
```

## Algoritmo de Euclides

### Python

```
ra = int(input("Ingrese un numero: "))
rb = int(input("Ingrese otro numero: "))

while ra % rb != 0:
    ra, rb = rb, ra % rb

print(f"El MCD es: {rb}.")
```

## Calculadora

### Python

```python
numero = int(input("Ingrese un numero: "))
operador = input("Ingrese operador: ")
resultado = numero

while operador != "=":
    anterior = operador
    numero = int(input("Ingrese un numero: "))
    operador = input("Ingrese operador: ")

    if anterior == "+": resultado += numero
    if anterior == "-": resultado -= numero
    if anterior == "*": resultado *= numero
    if anterior == "/": resultado /= numero

print(f"Resultado: {resultado}.")
```

## Adivinar un numero

### Python

```python
from random import randint

incognita = randint(1, 100)
pregunta = -1

while incognita != pregunta:
    pregunta = int(input("Ingrese un numero: "))

    if incognita > pregunta:
        print("El numero es mas grande.")
    elif incognita < pregunta:
        print("El numero es mas chico.")

print("Correcto!")
```

## Simon

> Simon es un juego electrónico creado por Ralph Baer y Howard J. Morrison en
> 1978. Tuvo un gran éxito durante los 80.

> El juego de forma aleatoria va iluminando los cuadrantes de colores, y a la
> vez que se ilumina cada cuadrante emite un sonido propio. Después de esperar,
> el usuario debe ir introduciendo la secuencia mostrada en el orden correcto,
> ayudándose de su memoria visual y sonora. Si lo consigue, este responderá con
> una secuencia más larga, y así sucesivamente.

### Python

```python
from random import randint
from time import sleep

simon = jugador = ""

while simon == jugador:
    simon += str(randint(1, 4))

    for letra in simon:
        print(letra, end = "", flush = True)
        sleep(0.5)

    for i in range(100):
        print("")

    jugador = input("Repita la secuencia: ")
```

## Toros y Vacas

### Python

```python
from random import randint

incognita = str(randint(1000, 10000))
pregunta = ""

while pregunta != incognita:
    pregunta = input("Ingrese un numero de cuatro cifras: ")

    toros = vacas = 0
    for p, i in zip(pregunta, incognita):
        if p == i:
            toros += 1
        elif p in incognita:
            vacas += 1

        print(f"Toros: {toros}, vacas: {vacas}.")

print("Correcto!")
```

# Arreglos

## Cadena reversa

### Python

```
texto = input("Ingrese un texto: ")

reversa = ""
for indice in range(len(texto) - 1, -1, -1):
    reversa += texto[indice]

print(f"La cadena reversa es: {reversa}.")
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
juego = True

while juego:
    for fila in tablero: print(fila)

    if 0 < tablero[0][0] == tablero[0][1] == tablero[0][2]: juego = False
    if 0 < tablero[1][0] == tablero[1][1] == tablero[2][2]: juego = False
    if 0 < tablero[2][0] == tablero[2][1] == tablero[2][2]: juego = False
    if 0 < tablero[0][0] == tablero[1][0] == tablero[2][0]: juego = False
    if 0 < tablero[0][1] == tablero[1][1] == tablero[2][1]: juego = False
    if 0 < tablero[0][2] == tablero[1][2] == tablero[2][2]: juego = False
    if 0 < tablero[0][0] == tablero[1][1] == tablero[2][2]: juego = False
    if 0 < tablero[0][2] == tablero[1][1] == tablero[2][0]: juego = False
    if 0 not in tablero[0] + tablero[1] + tablero[2]: juego = False

    if juego:
        print(f"Turno: jugador {turno + 1}")
        fila = int(input("Ingrese fila: ")) - 1
        columna = int(input("Ingrese columna: ")) - 1

        if 0 <= fila <= 2 and 0 <= columna <= 2:
            if not tablero[fila][columna]:
                tablero[fila][columna] = turno + 1
                turno = (turno + 1) % 2
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

while "".join(montones):
    print(f"1: {montones[0]}")
    print(f"2: {montones[1]}")
    print(f"3: {montones[2]}")

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
    print(f"Torre 1: {torres[0]}.")
    print(f"Torre 2: {torres[1]}.")
    print(f"Torre 3: {torres[2]}.\n")

    origen = int(input("Ingrese torre de origen: ")) - 1
    destino = int(input("Ingrese torre de destino: ")) - 1

    if origen < 4 and destino < 4 and torres[origen]:
        if not torres[destino] or torres[origen][-1] < torres[destino][-1]:
            torres[destino] += [torres[origen].pop()]
```

## Ahorcado

### Python

```python
palabra = input("Ingrese una palabra: ")
respuesta = "_" * len(palabra)
errores = ""

for i in range(100): print("")

while respuesta != palabra and len(errores) < 7:
    print(" ".join(respuesta))
    print(f"Errores: {errores}")
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
