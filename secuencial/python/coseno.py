from math import cos

a = int(input("Ingrese el valor de un lado: "))
b = int(input("Ingrese el valor de otro lado: "))
g = float(input("Ingrese el angulo que conforman, en radianes: "))

c = (a*a + b*b + 2*a*b*cos(g)) ** 0.5

print(f"El lado restante vale {c}.")
