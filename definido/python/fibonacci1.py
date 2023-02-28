cantidad = int(input("Ingrese la cantidad de numeros: "))

fa = 1
fb = 1

for i in range(3, cantidad + 3):
    print(fa)
    fi = fa + fb
    fa, fb = fb, fi
