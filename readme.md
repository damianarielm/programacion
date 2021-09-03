[[_TOC_]]

# Secuencial

* Constantes importantes
* Operadores aritmeticos
* Calculo de promedio
* Calculo de minutos y segundos
* Calculo de hipotenusa
* Teorema del coseno
* Distancia entre puntos
* Raices y vertice de una parabola
* Intercambio de variables
* Numeros romanos

# Seleccion

* Valor absoluto
* Paridad
* Signo
* Chequeo de vocales
* Ordenar numeros
* Determinacion de signo zodiacal
* Raices de un polinomio de grado 3
* Validacion y clasificacion de triangulos
* Validacion de fecha en año no bisiesto
* Chequeo de año bisiesto
* Maximo de 5 numeros

# Ciclo definido

* Numeros naturales
* Factores
* Codigo Morse
* Binario a decimal
* Fizzbuzz
* Cantidad de vocales
* Sumatoria de naturales
* Factorial
* Trigo y Ajedrez
* Sucesion de Fibonacci
* Maximo de 10 numeros
* Calculo de pi
* Calculo de e
* Numeros palindromos
* Fuerza bruta
* Los cofres de Porcia
* Problema de Monty Hall

# Ciclo indefinido

* Contraseña
* Decimal a binario
* Chequeo de primalidad
* Recaudacion del dia
* Menu
* Conjetura de Collatz
* Algoritmo de Euclides
* Calculadora
* Adivinar un numero
* Simon
* Toros y Vacas

# Arreglos

* Busqueda lineal
* Cadena reversa
* Cifrado Cesar
* Spyfall
* Busqueda binaria
* Ordenamiento de burbuja
* Ordenamiento por insercion
* Ta-Te-Ti
* Nim
* Torres de Hanoi
* Ahorcado
* Memoria

# Recursion

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

# Punteros

## strlen

## strcpy

## realloc

## Desbordamiento de buffer

### C

```c
// gcc password.c -fno-stack-protector

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

#define LEN 10

void main() {
    char password[LEN];
    char input[LEN];

    // Generacion de contraseña aleatoria
    srand(time(NULL));
    for (int i = 0; i < LEN; i++)
        password[i] = rand();

    // Lectura de contraseña por teclado
    printf("Ingrese la contraseña: ");
    scanf("%s", input);

    // Verificacion de contraseña
    if (!strncmp(input, password, LEN))
        printf("Contraseña correcta.\n");
    else
        printf("Contraseña incorrecta.\n");
}
```

# Otros

# Proyectos

## Corrector Ortografico

## Onirim

## Viernes

## Sliding puzzle

## Juego de la vida

## Sokoban

## Orchard

## Deep Space D6

## Cuatro en linea

## Quarto

## Batalla naval

## Reversi

## Oso

## Palm Island

## Shephy

## Zogar's Revenge

## Qwixx

## Sylvion

## Nautilion

## Castellion

## Sagrada

## Quien quiere ser millonario?
