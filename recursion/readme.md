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

## Quick Sort

El ordenamiento rápido (quicksort en inglés) es un algoritmo de ordenacion
creado por el científico británico en computación C. A. R. Hoare.

### Python

```python
lista = [200, 190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

def ordenar(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [ n for n in lista[1:] if n < pivote ]
        mayores = [ n for n in lista[1:] if n >= pivote ]
        return ordenar(menores) + [ pivote ] + ordenar(mayores)

print(f"Lista ordenada: {ordenar(lista)}.")
```

## Merge Sort

El algoritmo de ordenamiento por mezcla (merge sort en inglés) es un algoritmo
de ordenamiento externo estable basado en la técnica divide y vencerás.

Fue desarrollado en 1945 por John Von Neumann.

### Python

```python
lista = [200, 190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

def merge(lista1, lista2):
    if not lista1:
        return lista2
    elif not lista2:
        return lista1
    elif lista1[0] < lista2[0]:
        return [ lista1[0] ] + merge(lista1[1:], lista2)
    else:
        return [ lista2[0] ] + merge(lista1, lista2[1:])

def ordenar(lista):
    if len(lista) <= 1:
        return lista
    else:
        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]
        return merge(ordenar(izquierda), ordenar(derecha))

print(f"Lista ordenada: {ordenar(lista)}.")
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
