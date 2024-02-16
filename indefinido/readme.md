[[_TOC_]]

## Contraseña

### Python

```python
contraseña = "abc123"
intento = ""

while intento != contraseña:
    intento = input("Ingrese una contraseña: ")

print("Contraseña correcta.")
```

## Suma digital

### Python

```python
n = int(input("Ingrese un numero: "))

suma = 0
while n != 0:
    suma += n % 10
    n //= 10

print(f"La suma de los digitos es: {suma}.")
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

```python
n = int(input("Ingrese un numero positivo: "))

print(f"El numero en binario es: {n:b}.")
```

## Chequeo de primalidad

En matemáticas, un número primo es un número natural mayor que 1 que tiene
únicamente dos divisores positivos distintos: él mismo y el 1. El número 1, por
convenio, no se considera ni primo ni compuesto.

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
    if n%2 == 0:
        n //= 2
    else:
        n = 3*n + 1

    print(n)
```

```python
n = int(input("Ingrese un numero: "))

while n != 1:
    n = n // 2 if n%2 == 0 else 3*n + 1

    print(n)
```

## Algoritmo de Euclides

El algoritmo de Euclides es un método antiguo y eficiente para calcular el
máximo común divisor (MCD). Fue originalmente descrito por Euclides en su obra
Elementos.

### Python

```python
ra = int(input("Ingrese un numero: "))
rb = int(input("Ingrese otro numero: "))

while ra%rb != 0:
    ra, rb = rb, ra % rb

print(f"El MCD es: {rb}.")
```

## Raiz digital

### Python

``` python
n = raiz = int(input("Ingrese un numero: "))

while n > 9:
    raiz = 0
    while n != 0:
        raiz += n % 10
        n //= 10
    n = raiz

print(f"La raiz digital es: {raiz}.")
```

```python
n = int(input("Ingrese un numero: "))

raiz = (n - 1) % 9 + 1 if n else 0

print(f"La raiz digital es: {raiz}.")
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
intento = -1

while incognita != intento:
    intento = int(input("Ingrese un numero: "))

    if incognita > intento:
        print("El numero es mas grande.")
    elif incognita < intento:
        print("El numero es mas chico.")

print("Correcto!")
```

## Toros y Vacas

### Python

```python
from random import randint

incognita = str(randint(1000, 10000))
intento = ""

while intento != incognita:
    intento = input("Ingrese un numero de cuatro cifras: ")

    toros = vacas = 0
    for p, i in zip(intento, incognita):
        if p == i:
            toros += 1
        elif p in incognita:
            vacas += 1

        print(f"Toros: {toros}, vacas: {vacas}.")

print("Correcto!")
```
