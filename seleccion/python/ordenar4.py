n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if n1 > n2: n1, n2 = n2, n1
if n2 > n3: n2, n3 = n3, n2
if n1 > n2: n1, n2 = n2, n1

print(n1, n2, n3)
