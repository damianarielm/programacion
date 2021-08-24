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
for i in range(1, n + 1):
    factorial *= i

print(f"El factorial es: {factorial}.")
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

# Arreglos

# Punteros

# Otros
