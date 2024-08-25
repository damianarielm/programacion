[[_TOC_]]

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
