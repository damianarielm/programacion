[[_TOC_]]

# Secuencial

## Calculo de minutos y segundos

### Python

```python
h = int(input("Ingrese una cantidad de horas: "))

m = h * 60
s = m * 60

print(f"La cantidad equivale a {m} minutos o {s} segundos.")
```

## Calculo de hipotenusa

### Python

```python
a = int(input("Ingrese el valor de un cateto: "))
b = int(input("Ingrese el valor del otro cateto: "))

h = (a*a + b*b) ** 0.5

print(f"El valor de la hipotenusa es {h}.")
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
a = int(input("Ingrese un numero: "))

if a >= 0:
    print(f"El valor absoluto es {a}.")
else:
    print(f"El valor absoluto es {-a}.")
```

## Signo

### Python

```python
a = int(input("Ingrese un numero: "))

if a > 0:
    print("El numero es positivo.")
elif a == 0:
    print("El numero es cero.")
else:
    print("El numero es negativo")
```

## Maximo de 5 numeros

### Python

```python
m = int(input("Ingrese el primer numero: "))

s = int(input("Ingrese el segundo numero: "))
if s > m: m = s

t = int(input("Ingrese el tercer numero: "))
if t > m: m = t

c = int(input("Ingrese el cuarto numero: "))
if c > m: m = c

q = int(input("Ingrese el quinto numero: "))
if q > m: m = q

print(f"El mas grande es {m}.")
```

# Ciclo definido

# Ciclo indefinido

# Arreglos

# Punteros

# Otros
