"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
assert cf
import traceback
from tabulate import tabulate
import model
#from tabulate import tabulate

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("10- Obtener dato dado un ID")
    print("0- Salir")


def load_data(control, file):
    """
    Carga los datos
    """
    data = controller.load_data(control, file)
    return data


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = controller.get_data(control, id)
    print("El dato con el ID", id, "es:", data)


def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    return(controller.req_1(control))
     
def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    return controller.req_2(control)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    print(controller.req_3(control))

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    print(controller.req_4(control))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    print(controller.req_5(control))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(controller.req_6(control))


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    print(controller.req_7(control))

def tipo_de_datos():
    lista = int(input("Ingresa el tipo de lista:\n1.Arreglo\n2.Lista encadenada\n"))
    
    if lista == 1:
        dato = "ARRAY_LIST"
    elif lista == 2:
        dato = "SINGLE_LINKED"
    else:
        print("opcion invalida")

    controlador = new_controller(dato)
    return controlador

def tamano():
    porcentaje = int(input("Ingresa el proctenaje:\n1.0.50%\n2. 5%\n3. 10%\n4. 20%\n5. 30%\n6. 50%\n7. 80%\n8. 100%\n"))
    
    if porcentaje == 1:
        dato = "small"
    if porcentaje == 2:
        dato = "5pct"
    if porcentaje == 3:
        dato = "10pct"
    if porcentaje == 4:
        dato = "20pct"
    if porcentaje == 5:
        dato = "30pct"
    if porcentaje == 6:
        dato = "50pct"
    if porcentaje == 7:
        dato = "80pct"
    if porcentaje == 8:
        dato = "large"

    ruta = f"/Salida_agregados_renta_juridicos_AG-{dato}.csv"
    return ruta

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    tipo = tipo_de_datos()
    size = tamano()
    data = controller.cargainpu(tipo, size)
        
    ordenamiento = int(input(f"Que tipo de ordenamiento deseas hacer?\n1.Insertion\n2.Selection\n3.Shell\n4.Quick\n5.Merge"))
    if ordenamiento == 1:
        order = "INS"
    if ordenamiento == 2:
        order = "SE"
    if ordenamiento == 3:
        order = "SHELL"
    if ordenamiento == 4:
        order = "QUICK"
    if ordenamiento == 5:
        order = "MERGE"


    datos = controller.req_8(tipo, order)
    print("El tamaño de la muestra es: ", data)
    print("El tiempo de ejecución del programa fue: ", datos[1]) 
# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                file = "/Salida_agregados_renta_juridicos_AG-small.csv"
                data, tamanodata = load_data(control["model"], file)
                print(tamanodata)
                # esta separando numeros de las ultimas columnas con coma en los miles
                intformats = [
                    "","","","","","","",",",",",",",","
                    ]
                datos = controller.convertir(data)
                datos_tabulados = tabulate(datos, tablefmt="grid", headers=["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], maxheadercolwidths=8, maxcolwidths=8,intfmt= intformats)
                print(datos_tabulados)
            elif int(inputs) == 2:
                datos = print_req_1(data)
                intformats = [
                    "","","","","","","",",",",",",",","
                    ]
                datos_tabulados = tabulate(datos, tablefmt="grid", headers=["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], maxheadercolwidths=8, maxcolwidths=8,intfmt= intformats)
                print(datos_tabulados)
                
            elif int(inputs) == 3:
                datos = print_req_2(data)
                intformats = [
                    "","","","","","","",",",",",",",","
                    ]
                datos_tabulados = tabulate(datos, tablefmt="grid", headers=["Año", "Código actividad económica", "Nombre actividad económica", "Código sector económico", "Nombre sector económico", "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"], maxheadercolwidths=8, maxcolwidths=8,intfmt= intformats)
                print(datos_tabulados)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 10:
                id = input("Ingrese un id: ")
                print_data(control, id)

            elif int(inputs) == 0:
                working = (False)
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except ValueError:
            print("Ingrese una opción válida.\n")
            traceback.print_exc()
    sys.exit(0)
