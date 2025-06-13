#Funcion de cálculo de grupo sin tal numero
def complementoGrupo(conjunto1, conjunto2):
    ret = []
    dig = {'0','1','2','3','4','5','6','7','8','9'}
    for d in dig:
        if d not in conjunto1 and d not in conjunto2:
            ret.append(d)
    return ret

#Funcion de Alta Diversidad Numérica
def esAltaDiversidadNumerica(conjunto1, conjunto2):
    if len(conjunto1) >= 5 and len(conjunto2) >= 5:
        return True
    else:
        return False

#Función para expresión lógica Par de Pares
#Se define recibiendo una lista para que tenga sentido la lógica
def parPares(listaConjuntos):
    ret = False
    if len(listaConjuntos) % 2 == 0:
        for l in listaConjuntos:
            if len(l) % 2 == 0:
                ret = True
            else:
                ret = False
                break
    return ret

conteo_dni1 = {}
conteo_dni2 = {}
suma_dni1 = 0
suma_dni2 = 0

#Ingreso de los DNI
dni1 = input("Ingrese el primer dni: ")
dni2 = input("Ingrese el segundo dni: ")

#Generación de conjuntos con los DNI
conjunto_dni1 = set(dni1)
conjunto_dni2 = set(dni2)

print(f"El conjunto de {dni1} es: {conjunto_dni1}")
print(f"El conjunto de {dni2} es: {conjunto_dni2}")

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

#Verificación de expresiones lógicas
#Grupo sin nro
for c in complementoGrupo(conjunto_dni1, conjunto_dni2):
    print(f"Grupo sin {c}")

#Grupo con alta diversidad numérica
if esAltaDiversidadNumerica(conjunto_dni1, conjunto_dni2):
    print("El grupo posee una alta diversidad numérica")

#Grupo Par de Pares
if parPares([conjunto_dni1, conjunto_dni2]):
    print("El grupo es Par y sus conjuntos son Pares. Es un PAR DE PARES!")
