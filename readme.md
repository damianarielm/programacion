[[_TOC_]]

# Secuencial

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

## Fizzbuzz

### Python

```python
for n in range(20):
    if n % 15 == 0:
        print("fizzbuzz")
    elif n % 3 == 0:
        print("fizz")
    elif n % 5 == 0:
        print("buzz")
    else:
        print(n)
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

## Sucesion de Fibonacci

### Python

```python
fa = 1
fb = 1

for i in range(3, 12):
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

# Punteros

# Otros
