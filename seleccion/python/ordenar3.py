n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

minimo = min(n1, n2, n3)
maximo = max(n1, n2, n3)

print(minimo)

if minimo < n1 < maximo:
    print(n1)
elif minimo < n2 < maximo:
    print(n2)
else:
    print(n3)

print(maximo)
