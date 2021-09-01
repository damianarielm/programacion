n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el tercer numero: "))

if n1 <= n2:
    if n2 <= n3:
        print(n1, n2, n3)
    else:
        if n3 <= n1:
            print(n3, n1, n2)
        else:
            print(n1, n3, n2)
else:
    if n1 <= n3:
        print(n2, n1, n3)
    else:
        if n3 <= n2:
            print(n3, n2, n1)
        else:
            print(n2, n3, n1)
