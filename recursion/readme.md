[[_TOC_]]

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

## Torres de Hanoi

N. Claus de Siam vio en el gran templo de Benarés, debajo de una cúpula que
marca el centro del mundo, tres varillas de diamante embutidas en una base
de bronce, de la altura de 1 codo (unos 45 cm) y el grosor del cuerpo de una
abeja. Sobre una de las varillas Dios ensartó, en el comienzo de los
tiempos, 64 discos de oro puro; el mayor de todos apoyado sobre el bronce y
los demás, cada vez más pequeños, apilados hasta el final de la varilla. Es
la torre sagrada de Brahma. Día y noche los sacerdotes se turnan sobre las
gradas del altar para trasladar la torre de la primera varilla a la tercera,
respetando las antedichas reglas impuestas por Brahma. Cuando se complete la
tarea la torre y los brahmanes colapsarán y acaecerá el fin del mundo.

### Python

```python
def mover(altura, origen, destino, auxiliar):
    if altura >= 1:
        mover(altura - 1, origen, auxiliar, destino)
        print(origen, "->", destino)
        mover(altura - 1, auxiliar, destino, origen)

discos = int(input("Ingrese numero de discos: "))
mover(discos, 1, 3, 2)
```
