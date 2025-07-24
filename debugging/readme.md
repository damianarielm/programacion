[[_TOC_]]

## Longitud

### Python

```python
palabra = input("Ingrese una palabra: ")

for indice in len(palabra):
    print("La letra", palabra[indice], "se encuentre en la posicion", indice)
```

```python
palabra = input("Ingrese una palabra: ")

for indice in range(len(palabra - 1)):
    print("La letra", palabra[indice], "se encuentre en la posicion", indice)
```

## Contador

### Python

```python
positivos = negativos = 0
numero = 1

while numero != 0:
    numero = int(input("Ingrese un numero (0 para salir): "))
    if numero > 0:
        positivos =+ 1
    elif numero < 0:
        negativos =+ 1

print("La cantidad de numeros positivos es:", positivos)
print("La cantidad de numeros negativos es:", negativos)
```

## Combustible

### Python

```python
def alcance(tanque, rendimiento):
    return tanque * rendimiento

rendimiento = 1 # Kilometros por litro
tanque = input("Ingrese cantidad de combustible en litros: ")
distancia = input("Ingrese distancia a recorrer: ")

if alcance(tanque, rendimiento) >= distancia:
    print("No es necesario cargar combustible.")
else:
    print("Debe cargar mas combustible para viajar.")
```

## Divisores

### Python

```python
numero = int(input("Ingrese un numero: "))

print("Los divisores son:")
for divisor in (1, numero + 1):
    if numero % divisor == 0:
        print(divisor)
```

## Division

### C

```c
#include <stdio.h>

int main() {
    int dividendo, divisor;

    printf("Ingrese un divisor distinto de 0: ");
    scanf("%d", &divisor);

    if (divisor != 0)
        printf("Ingrese un dividendo: ");
        scanf("%d", &dividendo);
        printf("%d / %d = %d.\n", dividendo, divisor, dividendo / divisor);
}
```
## Positivo

### C

```c
#include <stdio.h>

int main() {
    int numero;
    printf("Ingrese un numero: ");
    scanf("%d", &numero);

    if (numero = 0)
        puts("El numero es 0.");
    else if (numero > 0)
        puts("El numero es positivo");
    else
        puts("El numero es negativo");
}
```

## Ordenar numeros

### C

```c
#include <stdio.h>

int main() {
    int numero1, numero2, numero3;

    printf("Ingrese un numero: ");
    scanf("%d", &numero1);
    printf("Ingrese otro numero: ");
    scanf("%d", &numero2);
    printf("Ingrese otro numero: ");
    scanf("%d", &numero3);

    if (numero1 < numero2 < numero3)
        printf("%d < %d < %d.\n", numero1, numero2, numero3);
    else if (numero1 < numero3 < numero2)
        printf("%d < %d < %d.\n", numero1, numero3, numero2);
    else if (numero2 < numero1 < numero3)
        printf("%d < %d < %d.\n", numero2, numero1, numero3);
    else if (numero2 < numero3 < numero1)
        printf("%d < %d < %d.\n", numero2, numero3, numero1);
    else if (numero3 < numero1 < numero2)
        printf("%d < %d < %d.\n", numero3, numero1, numero2);
    else
        printf("%d < %d < %d.\n", numero3, numero2, numero1);
}
```
