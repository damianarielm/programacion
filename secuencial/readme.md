[[_TOC_]]

## Constantes importantes

### Python

```python
print("El valor de pi es aproximadamente: 3.14159265359")
print("El valor de e es aproximadamente: 2.71828182846")
print("El valor de phi es aproximadamente: 1.618033988")
print("El valor de g es aproximadamente: 9.80665")
print("El valor de c es aproximadamente: 299792458")
```

```python
pi = 3.14159265359
e = 2.71828182846
phi = 1.618033988
g = 9.80665
c = 299792458

print(f"El valor de pi es aproximadamente: {pi}")
print(f"El valor de e es aproximadamente: {e}")
print(f"El valor de phi es aproximadamente: {phi}")
print(f"El valor de g es aproximadamente: {g}")
print(f"El valor de c es aproximadamente: {c}")
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

```python
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese otro numero: "))

print(f"La suma es {n1 + n2}.")
print(f"La resta es {n1 - n2}.")
print(f"El producto es {n1 * n2}.")
print(f"La division es {n1 / n1}.")
print(f"El resto de la division es {n1 % n2}.")
print(f"La division entera es {n1 // n2}.")
print(f"La potencia es {n1 ** n2}.")
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
n = int(input("Ingrese exponente: "))

e = (1 + 1/n) ** n

print(f"El numero e es aproximadamente: {e}.")
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

```python
promedio  = int(input("Ingrese un numero: ")) / 5
promedio += int(input("Ingrese otro numero: ")) / 5
promedio += int(input("Ingrese otro numero: ")) / 5
promedio += int(input("Ingrese otro numero: ")) / 5
promedio += int(input("Ingrese otro numero: ")) / 5

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

En matemáticas, el teorema de Pitágoras es una relación fundamental en
geometría euclidiana entre los tres lados de un triángulo rectángulo. Afirma
que el área del cuadrado cuyo lado es la hipotenusa (el lado opuesto al ángulo
recto) es igual a la suma de las áreas de los cuadrados de los otros dos lados.

### Python

```python
a = int(input("Ingrese el valor de un cateto: "))
b = int(input("Ingrese el valor del otro cateto: "))

hipotenusa = (a*a + b*b) ** 0.5

print(f"El valor de la hipotenusa es {hipotenusa}.")
```

## Teorema del coseno

El teorema del coseno es una generalización del teorema de Pitágoras en los
triángulos rectángulos en trigonometría.

El teorema relaciona un lado de un triángulo cualquiera con los otros dos y con
el coseno del ángulo formado por estos dos lados.

### Python

```python
from math import cos

a = int(input("Ingrese el valor de un lado: "))
b = int(input("Ingrese el valor de otro lado: "))
g = float(input("Ingrese el angulo que conforman, en radianes: "))

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

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

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

print(f"Despues del intercambio el valor de a es {a}, y el de b es {b}.")
```

```python
a = int(input("Ingrese el valor de la variable a: "))
b = int(input("Ingrese el valor de la variable b: "))

a, b = b, a

print(f"Despues del intercambio el valor de a es {a}, y el de b es {b}.")
```

## Numeros romanos

La numeración romana es un sistema de numeración que se desarrolló en la
Antigua Roma y se utilizó en todo el Imperio romano, manteniéndose con
posterioridad a su desaparición y todavía utilizado en algunos ámbitos.

Está basado en la numeración etrusca, la cual, a diferencia de la numeración
decimal que está basada en un sistema posicional, se basa en un sistema aditivo
(cada signo representa un valor que se va sumando al anterior).

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

print(f"El numero en decimal es: {romanos}.")
```
