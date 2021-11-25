[[_TOC_]]

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

```python
n = int(input("Ingrese un numero: "))
print(f"El valor absoluto es {(n*n) ** 0.5}.")
```

```python
n = int(input("Ingrese un numero: "))
print(f"El valor absoluto es {abs(n)}.")
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
else:
    if n == 0:
        print("El numero es cero.")
    else:
        print("El numero es negativo")
```

```python
n = int(input("Ingrese un numero: "))

if n > 0:
    print("El numero es positivo.")
elif n == 0:
    print("El numero es cero.")
else:
    print("El numero es negativo")
```

```python
n = int(input("Ingrese un numero: "))

if n > 0: signo = "positivo"
elif n == 0: signo = "cero"
else: signo = "negativo"

print("El numero es {signo}.")
```

## Piedra, papel o tijera

Piedra, papel o tijera(s) es un juego infantil, un juego de manos en el que
existen tres elementos: la piedra que vence a la tijera rompiéndola, la tijera
que vence al papel cortándolo y el papel que vence a la piedra envolviéndola,
dando lugar a un círculo o ciclo cerrado, que caracteriza al juego. Se utiliza
con mucha frecuencia para decidir quién de dos personas hará algo, tal y como
se hace a veces usando una moneda, o para dirimir algún asunto.

### Python

```python
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
```

```python
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
```

```python
from random import randint

print("1 - Piedra.")
print("2 - Papel.")
print("3 - Tijera.")
jugador = int(input("Elija una opcion: "))

computadora = randint(1, 3)
print(f"Computadora elige: {computadora}.\n")

if computadora == jugador:
    print("Empate.")
elif abs(jugador - computadora) == 1:
    print("Ganaste!" if jugador > computadora else "Perdiste.")
else:
    print("Ganaste!" if jugador < computadora else "Perdiste.")
```

## Arboles de decision

Un árbol de decisión es un modelo de predicción utilizado en diversos ámbitos
que van desde la inteligencia artificial hasta la Economía. Dado un conjunto de
datos se fabrican diagramas de construcciones lógicas, muy similares a los
sistemas de predicción basados en reglas, que sirven para representar y
categorizar una serie de condiciones que ocurren de forma sucesiva, para la
resolución de un problema.

![Titanic](https://upload.wikimedia.org/wikipedia/commons/f/f3/CART_tree_titanic_survivors.png)

### Python

```python
sexo = input("Ingrese sexo (F/M): ")
edad = int(input("Ingrese la edad: "))
hermanos = int(input("Ingrese cantidad de hermanos: "))

if sexo == "M":
    if edad > 9.5:
        if hermanos > 2.5:
            print("El pasajero sobrevivio.")
        else:
            print("El pasajero no sobrevivio.")
    else:
        print("El pasajero no sobrevivio.")
else:
    print("La pasajera sobrevivio.")
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

```python
letra = input("Ingrese una letra minuscula: ")

if letra in "aeiou":
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

if n1 <= n2:
    if n2 <= n3:
        print(n1, n2, n3)
    else:
        if n3 <= n1:
            print(n3, n1, n2)
        else:
            print(n1, n3, n2)
else:
    if n1 <= n3:
        print(n2, n1, n3)
    else:
        if n3 <= n2:
            print(n3, n2, n1)
        else:
            print(n2, n3, n1)
```

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

La desigualdad triangular o desigualdad de Minkowski es un teorema de geometría
euclidiana que establece:

> En todo triángulo la suma de las longitudes de dos lados cualesquiera es
> siempre mayor a la longitud del lado restante.

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

Un año bisiesto se añade para corregir el desfase que existe entre la duración
del año trópico (365,242189 días) y el año calendario de (365 días). Esto
requiere que cada cuatro años se corrija el año calendario por una acumulación
no contabilizada de aproximadamente 1/4 de día por año que equivale a un día
extra.

En el calendario juliano se consideraban bisiestos los años divisibles entre
cuatro, resultando años de 365,25 días. Esto supone un adelanto de unos 11,25
minutos por año respecto al año trópico. Puede no parecer mucho, pero solo en
500 años supondría un desfase de casi cuatro días. Se hacía necesario acortar
el año, y así el calendario gregoriano establece:

> Año bisiesto es el divisible entre 4, **salvo que sea año secular** -último
> de cada siglo, terminado en "00"-, en cuyo caso también ha de ser divisible
> entre 400.

Es decir, se determinan dos grupos de años: los **no seculares** y los
**seculares**. Los primeros han de ser múltiplos de 4, mientras que los
segundos habrán de serlo de 400. De esta manera se eliminan como bisiestos a 3
de cada 4 años seculares. De esta forma, los años 1800 y 1900 pese a ser
divisibles por 4, no lo son por 400, por lo que fueron años comunes. Por su
parte, el año 2000 es divisible tanto por 4 como por 400, por lo tanto sí fue
un año bisiesto.

El ciclo juliano de 4 años da paso a uno gregoriano de 400 en el que hay 97
bisiestos y 303 comunes, resultando años de 365,2425 días. La diferencia con el
año trópico queda ahora reducida a menos de medio minuto por año (26,9 segundos
aproximadamente).

### Python

```python
año = int(input("Ingrese el año: "))

if año%4 == 0:
    if año%100 == 0:
        if año%400 == 0:
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

if año%4 == 0 and (año%100 != 0 or año%400 == 0):
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

```python
primero = int(input("Ingrese el primer numero: "))
segundo = int(input("Ingrese el segundo numero: "))
tercero = int(input("Ingrese el tercer numero: "))
cuarto = int(input("Ingrese el cuarto numero: "))
quinto = int(input("Ingrese el quinto numero: "))
maximo = max(primero, segundo, tercero, cuarto, quinto)

print(f"El mas grande es {maximo}.")
```
