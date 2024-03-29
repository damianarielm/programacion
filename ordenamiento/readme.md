[[_TOC_]]

## Generar permutacion

### Python

```python
from random import shuffle

def permutacion(cantidad):
    lista = list(range(cantidad))
    shuffle(lista)
    return lista

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    print(permutacion(cantidad))
```

## Verificar ordenamiento

### Python

```python
def esta_ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False

    return True
```

## Bogo Sort

### Python

```python
from random import shuffle
from permutacion import permutacion # Ejercicio previo
from verificar import esta_ordenada # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

while not esta_ordenada(lista):
    shuffle(lista)

print(f"Lista ordenada: {lista}.")
```

## Permutation Sort

### Python

```python
from itertools import permutations
from verificar import esta_ordenada # Ejercicio previo
from permutacion import permutacion # Ejercicio previo

def permutation_sort(lista):
    for permutacion in permutations(lista):
        if esta_ordenada(permutacion):
            return permutacion

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")
print(f"Lista ordenada: {permutation_sort(lista)}.")
```

## Menor Indice

### Python

```python
from permutacion import permutacion # Ejercicio previo

def menor_indice(lista):
    menor, indice = lista[0], 0
    for i, x in enumerate(lista):
        if x < menor:
            menor = x
            indice = i

    return indice

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    lista = permutacion(cantidad)
    print(f"La lista es: {lista}.")
    print(f"El indice del menor es: {menor_indice(lista)}.")
```

## Ordenamiento por seleccion

### Python

```python
from menorindice import menor_indice # Ejercicio previo
from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

for i in range(len(lista) - 1):
    m = menor_indice(lista[i:]) + i
    lista[i], lista[m] = lista[m], lista[i]

print(f"Lista ordenada: {lista}.")
```

## Ordenamiento de burbuja

La Ordenación de burbuja (Bubble Sort en inglés) es un sencillo algoritmo de
ordenamiento. Funciona revisando cada elemento de la lista que va a ser
ordenada con el siguiente, intercambiándolos de posición si están en el orden
equivocado. Es necesario revisar varias veces toda la lista hasta que no se
necesiten más intercambios, lo cual significa que la lista está ordenada.

### Python

```python
from permutacion import permutacion

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

for _ in range(len(lista)):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(f"Lista ordenada: {lista}.")
```

```python
from permutacion import permutacion

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

for n in range(len(lista)):
    for i in range(len(lista) - n - 1):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]

print(f"Lista ordenada: {lista}.")
```

```python
from permutacion import permutacion

def burbuja(lista):
    for n in range(len(lista)):
        intercambios = False

        for i in range(len(lista) - n - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambios = True

        if not intercambios:
            return lista

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")
print(f"Lista ordenada: {burbuja(lista)}.")
```

## Insertar en orden

### Python

```python
def insertar_en_orden(lista, numero):
    for i in range(len(lista)): # Recorremos la lista...
        if numero < lista[i]: # ...buscando un lugar en el medio.
            return lista[:i] + [numero] + lista[i:]

    return lista + [elemento]   # Si no lo encontramos, va al final.

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    lista = list(range(cantidad))

    numero = float(input("Ingrese numero a agregar: "))
    lista = insertar_en_orden(lista, numero)

    print(f"Lista: {lista}.")
```

```python
def insertar_en_orden(lista, numero):
    mitad = len(lista) // 2

    if len(lista) == 0:
        return [numero]
    if len(lista) == 1:
        return [numero] + lista if numero < lista[0] else lista + [numero]
    elif numero <= lista[mitad]:
        return insertar_en_orden(lista[:mitad], numero) + lista[mitad:]
    else:
        return lista[:mitad] + insertar_en_orden(lista[mitad:], numero)

if __name__ == "__main__":
    cantidad = int(input("Ingrese la cantidad: "))
    lista = list(range(cantidad))

    numero = float(input("Ingrese numero a agregar: "))
    lista = insertar_en_orden(lista, numero)

    print(f"Lista: {lista}.")
```

## Ordenamiento por insercion

El ordenamiento por inserción (insertion sort en inglés) es una manera muy
natural de ordenar para un ser humano, y puede usarse fácilmente para ordenar
un mazo de cartas numeradas en forma arbitraria.

Inicialmente se tiene un solo elemento, que obviamente es un conjunto ordenado.
Después, cuando hay *k* elementos ordenados de menor a mayor, se toma el
elemento *k+1* y se compara con todos los elementos ya ordenados, deteniéndose
cuando se encuentra un elemento menor (todos los elementos mayores han sido
desplazados una posición a la derecha) o cuando ya no se encuentran elementos
(todos los elementos fueron desplazados y este es el más pequeño). En este
punto se inserta el elemento *k+1* debiendo desplazarse los demás elementos.

### Python

```python
from permutacion import permutacion # Ejercicio previo
from insertar2 import insertar_en_orden # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

for i in range(len(lista)):
    lista = insertar_en_orden(lista[:i], lista[i]) + lista[i + 1:]

print(f"Lista ordenada: {lista}.")
```

## Quick Sort

El ordenamiento rápido (quicksort en inglés) es un algoritmo de ordenacion
creado por el científico británico en computación C. A. R. Hoare.

### Python

```python
from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [ n for n in lista[1:] if n < pivote ]
        mayores = [ n for n in lista[1:] if n > pivote ]
        return quick_sort(menores) + [ pivote ] + quick_sort(mayores)

print(f"Lista ordenada: {quick_sort(lista)}.")
```

```python
from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        if lista[0] <= lista[1] <= lista[-1]: pivote = lista[1]
        elif lista[0] <= lista[-1] <= lista[0]: pivote = lista[-1]
        else: pivote = lista[0]

        menores = [ n for n in lista if n < pivote ]
        mayores = [ n for n in lista if n > pivote ]
        return quick_sort(menores) + [ pivote ] + quick_sort(mayores)

print(f"Lista ordenada: {quick_sort(lista)}.")
```

```python
from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        if lista[0] <= lista[1] <= lista[-1]: pivote = lista[1]
        elif lista[0] <= lista[-1] <= lista[0]: pivote = lista[-1]
        else: pivote = lista[0]

        menores = [ n for n in lista if n < pivote ]
        pivotes = [ n for n in lista if n == pivote ]
        mayores = [ n for n in lista if n > pivote ]
        return quick_sort(menores) + pivotes + quick_sort(mayores)

print(f"Lista ordenada: {quick_sort(lista)}.")
```

## Combinar listas ordendas

### Python

```python
def merge(lista1, lista2):
    if not lista1:
        return lista2
    elif not lista2:
        return lista1
    elif lista1[0] < lista2[0]:
        return [ lista1[0] ] + merge(lista1[1:], lista2)
    else:
        return [ lista2[0] ] + merge(lista1, lista2[1:])
```

## Merge Sort

El algoritmo de ordenamiento por mezcla (merge sort en inglés) es un algoritmo
de ordenamiento externo estable basado en la técnica divide y vencerás.

Fue desarrollado en 1945 por John Von Neumann.

### Python

```python
from combinar import merge # Ejercicio previo
from permutacion import permutacion # Ejercicio previo

cantidad = int(input("Ingrese la cantidad: "))
lista = permutacion(cantidad)
print(f"Lista desordenada: {lista}.")

def merge_sort(lista):
    if len(lista) <= 1: return lista

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    return merge(merge_sort(izquierda), merge_sort(derecha))

print(f"Lista ordenada: {merge_sort(lista)}.")
```
