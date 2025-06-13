from datetime import datetime
from itertools import product

# Funcion para saber si un año es bisiesto
def bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Ingreso de los dos años de nacimiento
anio1 = int(input("Ingresa el primer año de nacimiento: "))
anio2 = int(input("Ingresa el segundo año de nacimiento: "))

anios_nacimiento = [anio1, anio2]

# Suma de años pares e impares
pares = 0
impares = 0

for anio in anios_nacimiento:
    if anio % 2 == 0:
        pares += 1
    else:
        impares += 1

print()
print(f"Años pares: {pares}")
print(f"Años impares: {impares}")
print()

# Flag para saber si son de la generacion Z
if anio1 > 2000 and anio2 > 2000:
    print("Es un Grupo Z")

# Flag para saber si hay un año bisiesto
if bisiesto(anio1) or bisiesto(anio2):
    print("Tenemos un año especial")

# Calculo edad
anio_actual = datetime.now().year
edades = [anio_actual - anio for anio in anios_nacimiento]

# Producto cartesiano (años y edades)
producto = list(product(anios_nacimiento, edades))

print("\nProducto cartesiano entre años y edades:")
for par in producto:
    print(par)