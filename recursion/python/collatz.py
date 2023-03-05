def collatz(numero):
    print(numero)
    if numero != 1:
        collatz(numero // 2 if numero%2 == 0 else 3*numero + 1)

numero = int(input("Ingrese un numero: "))
collatz(numero)
