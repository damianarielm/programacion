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
