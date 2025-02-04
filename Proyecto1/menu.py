import datetime
from prettytable import PrettyTable

#Se crea una lista para almacenar los experimentos

listaDeExperimentos = [
    ["Experimento 1","14/12/2024","Fisica",[3,8,4,9,2,7]],
]

#Se crea una funcion para agregar un experimento

def agregarExperimento():

    nombre = input("Ingrese el nombre del experimento: ")
    fecha = input("Ingrese la fecha del experimento: ")
    tipo = input("Ingrese el tipo del experimento (Química, Biología, Física): ")

    try:
        datetime.datetime.strptime(fecha, "%d/%m/%Y")
        resultados = list(map(int, input("Ingrese los resultados separados por comas: ").split(",")))
        listaDeExperimentos.append([nombre, fecha, tipo, resultados])
        print("\033[1;32m "+"Experimento agregado con exito"+'\033[0;m')
    except:
        print("\033[1;31m "+"Error: Entrada no valida, intente de nuevo."+'\033[0;m')

#Agregamos la funcion para eliminar un experimento

def eliminarExperimento():
    verExperimentos()
    try:
        indice = int(input("Ingrese el número del experimento a eliminar: ")) -1

        if 0 <= indice < len(listaDeExperimentos):
            listaDeExperimentos.pop(indice)
            print("\033[1;32m "+"Experimento eliminado con exito"+'\033[0;m')
        else:
            print("\033[1;31m "+"Error: Numero no valido."+'\033[0;m')
    except:
        print("\033[1;31m "+"Error: Entrada no valida, intente de nuevo."+'\033[0;m')


#Se crea la funcion para visualizar los experimentos

def verExperimentos():

    tablaExperimentos = PrettyTable()

    tablaExperimentos.field_names = ["Id", "Nombre", "Fecha", "Tipo","Resultados"]
    for i, experimento in enumerate (listaDeExperimentos, start = 1):
        tablaExperimentos.add_row([i, experimento[0], experimento[1], experimento[2],experimento[3]], divider=True)

    if not listaDeExperimentos:
        print("\033[1;33m "+"No existen experimentos registrados."+'\033[0;m')
        return

    print(tablaExperimentos)

#Funcion para realizar los calculos de las estadisticas

def calcularEstadisticas():
    verExperimentos()

    try:
        indice = int(input("Ingrese el número del experimento a calcular: ")) -1

        if 0 <= indice < len(listaDeExperimentos):
            resultados = listaDeExperimentos[indice][3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            print(f"\033[1;32m Las estadisticas del experimento: {listaDeExperimentos[indice][0]}"+'\033[0;m')
            print(f"Promedio: {promedio}, Maximo: {maximo}, Minimo: {minimo}")
        else:
            print("\033[1;31m "+"Error: Numero no valido."+'\033[0;m')
    except:
        print("\033[1;31m "+"Error: Entrada no valida, intente de nuevo."+'\033[0;m')

#Se cre la funcion para hacer la comparacion entre los experimentos
def compararExperimentos():
    verExperimentos()

    try:
        indice = list(map(int, input("Ingrese los indices de los experimentos a comparar separados por comas: ").split(",")))
        comparaciones = []
        for indice in indice:
            if 1 <= indice <= len(listaDeExperimentos):
                resultados = listaDeExperimentos[indice-1][3]
                promedio = sum(resultados) / len(resultados)
                comparaciones.append((listaDeExperimentos[indice-1][0], promedio))
            else:
                print("\033[1;31m "+"Error: Numero no valido."+'\033[0;m')
        comparaciones.sort(key=lambda x: x[1], reverse=True)
        for nombre, promedio in comparaciones:
            print(f"Experimento: {nombre}, Promedio: {promedio}")
    except:
        print("\033[1;31m "+"Error: Entrada no valida, intente de nuevo."+'\033[0;m')


#Se crea la funcion para generar un informe

def generarInforme():
    if not listaDeExperimentos:
        print("\033[1;33m "+"No existen experimentos registrados."+'\033[0;m')
        return
    with open("Informe.txt", "w") as archivo:
        archivo.write("*****INFORME*****\n")
        archivo.write("*****************\n")
        for experimento in listaDeExperimentos:
            resultados = experimento[3]
            promedio = sum(resultados) / len(resultados)
            maximo = max(resultados)
            minimo = min(resultados)
            archivo.write(f"Nombre: {experimento[0]} \n")
            archivo.write(f"Fecha: {experimento[1]}\n")
            archivo.write(f"Tipo: {experimento[2]}\n")
            archivo.write(f"Resultados: {experimento[3]}\n")
            archivo.write(f"Promedio: {promedio}\n")
            archivo.write(f"Maximo: {maximo}\n")
            archivo.write(f"Minimo: {minimo}\n")
            archivo.write("\n")
            archivo.write("*****************\n")
        print("\033[1;32m "+"Informe generado con exito"+'\033[0;m')

#Funcion para mostrar el menú

def mostrarMenu():
    print("****|Menu principal|****")
    print("=====================================")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimentos")
    print("4. Calcular estadisticas")
    print("5. Comparar experimentos")
    print("6. Generar informe")
    print("7. Salir")

#Se crea la funcion principal

def main():
    while True:
        print("=====================================")
        mostrarMenu()
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                agregarExperimento()
            elif opcion == 2:
                verExperimentos()
            elif opcion == 3:
                eliminarExperimento()
            elif opcion == 4:
                calcularEstadisticas()
            elif opcion == 5:
                compararExperimentos()
            elif opcion == 6:
                generarInforme()
            elif opcion == 7:
                print("¡¡Gracias, vuelve pronto!!")
                break

        except:
            print("\033[1;31m "+"Error: Entrada no valida, intente de nuevo."+'\033[0;m')
main()