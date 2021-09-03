[[_TOC_]]

## Numeros naturales

### Python

```python
maximo = int(input("Ingrese el maximo: "))

for numero in range(maximo + 1):
    print(numero)
```

## Factores

### Python

```python
n = int(input("Ingrese un numero: "))

for factor in range(1, n + 1):
    if n % factor == 0:
        print(factor)
```

## Codigo Morse

> En 1837, Samuel Morse y Alfred Vail estaban trabajando en un sistema de
> telégrafo eléctrico. Decidieron usar un método por el cual cada símbolo era
> transmitido de forma individual como una combinación de rayas y puntos, es
> decir, señales telegráficas que se diferencian en el tiempo de duración de la
> señal activa. Morse desarrolló una primera versión de su código en 1837 para
> enviar números, que luego se debían convertir en mensajes completos usando un
> libro de claves. Este código fue expandido por Vail en 1841 para incluir
> letras y otros signos de puntuación, creando así el código actual. Morse
> reconoció la idoneidad de este sistema y lo patentó junto con el telégrafo
> eléctrico. Fue conocido como American Morse Code y utilizado en la primera
> transmisión por telégrafo.

### Python

```python
texto = input("Ingrese texto: ")
codigo = ""

for letra in texto:
    if letra == "a": codigo += ".- "
    elif letra == "b": codigo += "-... "
    elif letra == "c": codigo += "-.-. "
    elif letra == "d": codigo += "-.. "
    elif letra == "e": codigo += ". "
    elif letra == "f": codigo += "..-. "
    elif letra == "g": codigo += "--. "
    elif letra == "h": codigo += ".... "
    elif letra == "i": codigo += ".. "
    elif letra == "j": codigo += ".--- "
    elif letra == "k": codigo += "-.- "
    elif letra == "l": codigo += ".-.. "
    elif letra == "m": codigo += "-- "
    elif letra == "n": codigo += "-. "
    elif letra == "o": codigo += "--- "
    elif letra == "p": codigo += ".--. "
    elif letra == "q": codigo += "--.- "
    elif letra == "r": codigo += ".-. "
    elif letra == "s": codigo += "... "
    elif letra == "t": codigo += "- "
    elif letra == "u": codigo += "..- "
    elif letra == "v": codigo += "...- "
    elif letra == "w": codigo += ".-- "
    elif letra == "x": codigo += "-..- "
    elif letra == "y": codigo += "-.-- "
    elif letra == "z": codigo += "--.. "
    else: codigo += letra

print(f"El cifrado es: {codigo}")
```

## Binario a decimal

### Python

```python
n = input("Ingrese un numero en binario: ")
decimal = 0

for i, digito in enumerate(n):
    if digito == "1":
        decimal += 2 ** (len(n) - 1 - i)

print(f"El numero en decimal es: {decimal}.")
```

## Fizzbuzz

### Python

```python
maximo = int(input("Ingrese el maximo: "))

for numero in range(maximo + 1):
    if numero % 15 == 0: print("fizzbuzz")
    elif numero % 3 == 0: print("fizz")
    elif numero % 5 == 0: print("buzz")
    else: print(numero)
```

## Cantidad de vocales

### Python

```python
texto = input("Ingrese un texto: ")

vocales = 0
for letra in texto:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        vocales += 1

print(f"La cantidad de vocales es: {vocales}.")
```

## Sumatoria de naturales

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

## Trigo y Ajedrez

> Al noroeste de la India (seguramente en el actual Pakistán o Afganistán),
> había un poderoso brahmán llamado Rai Bhalit, tan rico y rodeado de tantos
> placeres que de ninguno de ellos podía gozar. Ordenó al más inteligente de
> sus sirvientes, llamado Sisa, que creara un juego capaz de entretenerle.
> Pasado algún tiempo Sisa presentó a su señor el ajedrez, un juego que
> emulaba la guerra y que se jugaba en un tablero con sesenta y cuatro
> casillas, alternativamente blancas y negras dispuestas en ocho filas y ocho
> columnas. El brahmán quedó tan encantado que le permitió escoger su
> recompensa. Sisa le dijo: "Señor, soy hombre modesto, y me conformaría con
> que me paguéis un grano de trigo por el primer cuadrado, dos por el segundo,
> cuatro en el tercero, ocho en el cuarto, etc.". El brahmán, encantado por la
> modesta petición de Sisa accedió en seguida, pero su alegría pronto se
> trocaría en ira cuando se dio cuenta de que ni con todo el trigo de su país
> alcanzaría a pagar semejante suma.

### Python

```python
granos = 1
total = 0
for i in range(64):
    total += granos
    granos *= 2

print(f"El total de granos es: {total}.")
```

```python
total = 0
for i in range(64):
    total += 2 ** i

print(f"El total de granos es: {total}.")
```

## Sucesion de Fibonacci

### Python

```python
fa = 1
fb = 1

for i in range(3, 33):
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

for _ in range(10):
    numero = int(input("Ingrese otro numero: "))

    if numero > maximo: maximo = numero

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

## Los cofres de Porcia

> En *El mercader de Venecia*, de Shakespeare, Porcia tenía tres cofres, dentro
> de uno de los cuales estaba el retrato de Porcia. El pretendiente tenía que
> elegir uno de los cofres y si tenía suerte (o inteligencia) eligiría el que
> tenía el retrato, pudiendo así pedir a Porcia por esposa. En la tapa de cada
> cofre había una inscripción para ayudar al pretendiente a elegir sabiamente:

> Cofre 1: El retrato no está en este cofre.

> Cofre 2: El retrato no está aquí.

> Cofre 3: EL retrato no está en el cofre 1.

> Porcia explicó al pretendiente que de los tres enunciados, a lo sumo uno era
> verdad.

### Python

```python
for retrato in range(1, 3 + 1):
    cofre1 = retrato == 1
    cofre2 = retrato != 2
    cofre3 = retrato != 1

    solo1 = cofre1 and not cofre2 and not cofre3
    solo2 = not cofre1 and cofre2 and not cofre3
    solo3 = not cofre1 and not cofre2 and cofre3
    ninguna = not cofre1 and not cofre2 and not cofre3

    if solo1 or solo2 or solo3 or ninguna:
        print(f"El retrato esta en el cofre {retrato}.")
```

## Problema de Monty Hall

> El concursante debe elegir una puerta entre tres (todas cerradas); el premio
> consiste en llevarse lo que se encuentra detrás de la elegida. Se sabe con
> certeza que tras una de ellas se oculta un automóvil, y tras las otras dos
> hay cabras. Una vez que el concursante haya elegido una puerta y comunicado
> su elección a los presentes, el presentador, que sabe lo que hay detrás de
> cada puerta, abrirá una de las otras dos en la que haya una cabra. A
> continuación, le da la opción al concursante de cambiar, si lo desea, de
> puerta (tiene dos opciones). ¿Debe el concursante mantener su elección
> original o escoger la otra puerta?

### Python

```python
from random import randint

simulaciones = int(input("Ingrese cantidad de simulaciones: "))
cambiando = 0
sincambio = 0

for s in range(simulaciones):
    auto = randint(1, 3)
    eleccion = randint(1, 3)
    if auto == eleccion: cambiando += 1
    if eleccion != auto: sincambio += 1

print(f"Se ganaron {cambiando} autos sin cambiar de desicion.")
print(f"Se ganaron {sincambio} autos cambiando de desicion.")
```
