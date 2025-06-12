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
    print("\n\t0 - Salir")

def complementoGrupo(listado):
    ret = []
    dig = {'0','1','2','3','4','5','6','7','8','9'}
    for d in dig:
        res = d
        for c in listado:
            if d in c:
                res = None
                break
        if res is not None:
            ret.append(res)
    return ret

#Funcion de Alta Diversidad Numérica
def esAltaDiversidadNumerica(lista):
    ret = True
    for c in lista:
        if len(c) < 5:
            ret = False
            break
    return ret

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

while True:
    menu()
    op = input("\n\t\tOpción: ")
    match op:
        case "1":
            lista_dni.append(input("Ingrese un dni: "))
            lista_conjuntos.append(set(lista_dni[cantidad_dni]))
            lista_conteo_dni.append(calcularFrecuencia(lista_conjuntos[cantidad_dni], lista_dni[cantidad_dni]))
            lista_sumas_dni.append(calcularSuma(lista_dni[cantidad_dni]))
            cantidad_dni += 1
        case "2":
            for i in lista_dni:
                print(i)
        case "3":
            for i in range(len(lista_dni)):
                print(f"El conjunto de {lista_dni[i]} es {lista_conjuntos[i]}")
        case "4":
            print("¿Que operación desea realizar?")
            print("\t1 - Unión")
            print("\t2 - Intersección")
            print("\t3 - Diferencia")
            print("\t4 - Diferencia Simétrica")
            operacion = input("\n\tOpción: ")
            
            for i in range(len(lista_conjuntos)):
                print(f"{i} - {lista_conjuntos[i]}")
            
            sel1 = input("De la lista anterior ingrese el número del primer conjunto: ")
            sel2 = input("De la lista anterior ingrese el número del segundo conjunto: ")
            
            con1 = lista_conjuntos[int(sel1)]
            con2 = lista_conjuntos[int(sel2)]

            match operacion:
                case "1":
                    print(f"La unión de {con1} y {con2} es {con1.union(con2)}")
                case "2":
                    print(f"La intersección de {con1} y {con2} es: {con1.intersection(con2)}")    
                case "3":
                    print(f"{con1} - {con2} es: {con1.difference(con2)}")
                case "4":
                    print(f"La diferencia simétrica de {con1} y {con2} es: {con1.symmetric_difference(con2)}")


        case "5":
            for i in range(len(lista_dni)):
                print(f"El DNI {lista_dni[i]} tiene:")
                for key, value in lista_conteo_dni[i].items():
                    if value == 1:
                        print(f"\t{value} vez el número {key}")
                    else:
                        print(f"\t{value} veces el número {key}")
            
        case "6":
            for i in range(len(lista_dni)):
                print(f"La suma de los dígitos de {lista_dni[i]} es {lista_sumas_dni[i]}")
   
        case "7":
            for c in complementoGrupo(lista_dni):
                print(f"Grupo sin {c}")
            if esAltaDiversidadNumerica(lista_dni):
                print("El grupo posee una alta diversidad numérica")

            #Grupo Par de Pares
            if parPares(lista_dni):
                print("El grupo es Par y sus conjuntos son Pares. Es un PAR DE PARES!")

        case "0":
            break
    input("Enter para continuar")