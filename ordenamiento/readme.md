[[_TOC_]]

## Generar permutacion

### Python

```python
from random import shuffle

def permutacion(cantidad):
    lista = list(range(cantidad))
    shuffle(lista)
    return lista

cantidad = int(input("Ingrese la cantidad: "))
print(permutacion(cantidad))
```

## Verificar ordenamiento

```python
def verificar(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False

    return True
```

## Ordenamiento de burbuja

La Ordenación de burbuja (Bubble Sort en inglés) es un sencillo algoritmo de
ordenamiento. Funciona revisando cada elemento de la lista que va a ser
ordenada con el siguiente, intercambiándolos de posición si están en el orden
equivocado. Es necesario revisar varias veces toda la lista hasta que no se
necesiten más intercambios, lo cual significa que la lista está ordenada.

### Python

```python
lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

for i in range(len(lista)):
    for j in range(len(lista) - 1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(f"Lista ordenada: {lista}.")
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
lista = [200 ,190, 1200, 1, 2, 4, 55, 1000, 6, 800]

print(f"Lista desordenada: {lista}.")

for i, n in enumerate(lista):
    while i > 0 and lista[i - 1] > n:
        lista[i] = lista[i - 1]
        i -= 1

    lista[i] = n

print(f"Lista ordenada: {lista}.")
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