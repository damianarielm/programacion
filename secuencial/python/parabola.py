a = int(input("Ingrese coeficiente principal: "))
b = int(input("Ingrese coeficiente lineal: "))
c = int(input("Ingrese termino independiente: "))

x1 = (-b + (b*b - 4*a*c) ** 0.5) / (2*a)
x2 = (-b - (b*b - 4*a*c) ** 0.5) / (2*a)
xv = -b / (2*a)
yv = a*xv*xv + b*xv + c

print(f"Las raices son {x1} y {x2}.")
print(f"El vertice es ({xv}, {yv}).")
