#Cambiar según la cantidad de integrantes
def menu():
    print("Bienvenido. Elija una opción")
    print("\t1 - Ingresar DNI nuevo")
    print("\t2 - Ver los DNI ingresados")
    print("\t3 - Ver los conjuntos")
    print("\t4 - Realizar operaciones")
    print("\t5 - Mostrar las frecuencias")
    print("\t6 - Mostrar las sumas de sus dígitos")
    print("\t7 - Verificar condiciones especiales")

def calcularFrecuencia(conjunto, dni):
    dictAux = {}
    for c in conjunto:
        dictAux[c] = dni.count(c)
    return dictAux

def calcularSuma(dni):
    suma = 0
    for c in dni:
        suma += int(c)
    return suma

cantidad_dni = 0
lista_dni = []
lista_conteo_dni = []
lista_sumas_dni = []
lista_conjuntos = []

menu()
while True:
    op = input("Opción: ")
    match op:
        case "1":
            lista_dni.append(input("Ingrese un dni: "))
            lista_conjuntos.append(set(lista_dni[cantidad_dni]))
            lista_conteo_dni.append(calcularFrecuencia(lista_conjuntos[cantidad_dni], lista_dni[cantidad_dni]))
            lista_sumas_dni.append(lista_dni[cantidad_dni])
            cantidad_dni += 1
        case "2":
            for i in lista_dni:
                print(i)
        case "3":
            for i in range(len(lista_dni)):
                print(f"El conjunto de {lista_dni[i]} es {lista_conjuntos[i]}")
        case "4":
            for i in lista_dni:
                print()
        case "5":
            pass
        case "6":
            pass
#inicializar diccionarios de conteo y listas de suma
for i in range(CANTIDAD_DNI):
    lista_conteo_dni.append({})
    lista_sumas_dni.append(0)

#Ingreso de los DNI
#for i in range(CANTIDAD_DNI):
#    lista_dni.append(input("Ingrese el primer dni: "))


#Generación de conjuntos con los DNI
for i in range(CANTIDAD_DNI):
    lista_conjuntos.append(set(lista_dni[i]))

for i in range(CANTIDAD_DNI):
    print(f"El conjunto de {lista_dni[i]} es: {lista_conjuntos[i]}")
#print(f"El conjunto de {dni2} es: {conjunto_dni2}")

#Cálculo y visualización de operaciones.
#Union
print(f"La unión de estos es: {conjunto_dni1.union(conjunto_dni2)}")
#Intersección
print(f"La intersección entre estos es: {conjunto_dni1.intersection(conjunto_dni2)}")
#Diferencias
print(f"La diferencia del primer dni por el segundo dni es: {conjunto_dni1.difference(conjunto_dni2)}")
print(f"La diferencia del segundo dni por el primer dni es: {conjunto_dni2.difference(conjunto_dni1)}")
#Diferencia Simétrica
print(f"La diferencia simétrica de los conjuntos es: {conjunto_dni1.symmetric_difference(conjunto_dni2)}")

#Conteo de frecuencia de cada dígito
for c in conjunto_dni1:
    conteo_dni1[c] = dni1.count(c)

#Conteo de frecuencia de cada dígito
for c in conjunto_dni2:
    conteo_dni2[c] = dni2.count(c)

#Muestra de la frecuencia de cada dígito.
print(f"El DNI {dni1} tiene: ")
for key, value in conteo_dni1.items():
    print(f"\t{value} vez el número {key}")

#Muestra de la frecuencia de cada dígito.
print(f"El DNI {dni2} tiene: ")
for key, value in conteo_dni2.items():
    print(f"\t{value} vez el número {key}")


#Suma de los digitos de cada dni y resultado.
for c in dni1:
    suma_dni1 += int(c)
print(f"La suma de los dígitos de {dni1} es: {suma_dni1}")

for c in dni2:
    suma_dni2 += int(c)
print(f"La suma de los dígitos de {dni2} es: {suma_dni2}")

