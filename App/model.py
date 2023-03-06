"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 * This program is distributed the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    data_structs = {
        "data": None,
    }

    data_structs["data"] = lt.newList(datastructure="ARRAY_LIST",
                                     cmpfunction=compare)

    return data_structs


# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    d = new_data(data["id"], data["info"])
    lt.addLast(data_structs["data"], d)

    return data_structs


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    data = {'id': 0, "info": ""}
    data["id"] = id
    data["info"] = info

    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    pos_data = lt.isPresent(data_structs["data"], id)
    if pos_data > 0:
        data = lt.getElement(data_structs["data"], pos_data)
        return data
    return None

def sort_crit(a, b):
    if a["Año"] < b["Año"]:
        return True
    elif a["Año"] == b["Año"]:
        return a["Código actividad económica"] < b["Código actividad económica"]
    else:
        return False
    
def convertir(data):
    dicc = {}
    data=data["first"]["info"]["data"]
    data = merg.sort(data, sort_crit)
    data=data["elements"]
    for n in data:
        if n["Año"] not in dicc.keys():
            dicc[n["Año"]] = []
        dicc[n["Año"]].append(n)
    lista_dicc = []
    for i in dicc:
        lista_dicc.append(dicc[i][0])
        lista_dicc.append(dicc[i][1])
        lista_dicc.append(dicc[i][2])
        lista_dicc.append(dicc[i][-3])
        lista_dicc.append(dicc[i][-2])
        lista_dicc.append(dicc[i][-1])
    rta = []
    for i in lista_dicc:
        lista_small = []
        lista_small.append(i["Año"])
        lista_small.append(i["Código actividad económica"])
        lista_small.append(i["Nombre actividad económica"])
        lista_small.append(i["Código sector económico"])
        lista_small.append(i["Nombre sector económico"])
        lista_small.append(i["Código subsector económico"])
        lista_small.append(i["Nombre subsector económico"])
        lista_small.append(i["Total ingresos netos"])
        lista_small.append(i["Total costos y gastos"])
        lista_small.append(i["Total saldo a pagar"])
        lista_small.append(i["Total saldo a favor"])
        rta.append(lista_small)
    return rta

def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs)


def req_1(data):
    """
    Función que soluciona el requerimiento 1
    """
    dicc = {}
    data=data["first"]["info"]["data"]
    data = merg.sort(data, sort_crit)
    data=data["elements"]
    for n in data:
        if n["Año"] not in dicc.keys():
            dicc[n["Año"]] = []
        dicc[n["Año"]].append(n)
    lista_dicc = []
    for año in dicc:
        mayor = 0
        for elemento in dicc[año]:
            if int(elemento["Total saldo a pagar"])>mayor:
                mayor = int(elemento["Total saldo a pagar"])
                mayor_diccionario = elemento
        lista_dicc.append(mayor_diccionario)
    rta = []
    for i in lista_dicc:
        lista_small = []
        lista_small.append(i["Año"])
        lista_small.append(i["Código actividad económica"])
        lista_small.append(i["Nombre actividad económica"])
        lista_small.append(i["Código sector económico"])
        lista_small.append(i["Nombre sector económico"])
        lista_small.append(i["Código subsector económico"])
        lista_small.append(i["Nombre subsector económico"])
        lista_small.append(i["Total ingresos netos"])
        lista_small.append(i["Total costos y gastos"])
        lista_small.append(i["Total saldo a pagar"])
        lista_small.append(i["Total saldo a favor"])
        rta.append(lista_small)
    return rta
    


def req_2(data):
    """
    Función que soluciona el requerimiento 2
    """
    dicc = {}
    data=data["first"]["info"]["data"]
    data = merg.sort(data, sort_crit)
    data=data["elements"]
    for n in data:
        if n["Año"] not in dicc.keys():
            dicc[n["Año"]] = []
        dicc[n["Año"]].append(n)
    lista_dicc = []
    for año in dicc:
        mayor = 0
        for elemento in dicc[año]:
            if int(elemento["Total saldo a favor"])>mayor:
                mayor = int(elemento["Total saldo a favor"])
                mayor_diccionario = (elemento)
        lista_dicc.append(mayor_diccionario)
    rta = []
    for i in lista_dicc:
        lista_small = []
        lista_small.append(i["Año"])
        lista_small.append(i["Código actividad económica"])
        lista_small.append(i["Nombre actividad económica"])
        lista_small.append(i["Código sector económico"])
        lista_small.append(i["Nombre sector económico"])
        lista_small.append(i["Código subsector económico"])
        lista_small.append(i["Nombre subsector económico"])
        lista_small.append(i["Total ingresos netos"])
        lista_small.append(i["Total costos y gastos"])
        lista_small.append(i["Total saldo a pagar"])
        lista_small.append(i["Total saldo a favor"])
        rta.append(lista_small)
    return rta


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs, order):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    if order == "INS":
        lista = ins.sort(data_structs["data"], compare)
    if order == "SE":
        lista = se.sort(data_structs["data"], compare)
    if order == "SHELL":
        lista = sa.sort(data_structs["data"], compare)
    if order == "QUICK":
        lista = quk.sort(data_structs["data"], compare)
    if order == "MERGE":
        lista = merg.sort(data_structs["data"], compare)

# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    if data_1["Año"] > data_2["Año"]:
        return True
    elif data_1["Año"] < data_2["Año"]:
        return False
    elif data_1["Año"] == data_2["Año"]:
        if data_1["Código actividad económica"] > data_2["Código actividad económica"]:
            return True
        elif data_1["Código actividad económica"] < data_2["Código actividad económica"]:
            return False
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["id"] > data_2["id"]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    sa.sort(data_structs["data"], sort_criteria)


def impuestos_agre(data_structs, data):
    
    informacion = infor_impu(data["Año"], data["Código actividad económica"],
                             data["Nombre actividad económica"], data ["Código sector económico"],
                             data["Nombre sector económico"], data["Código subsector económico"],
                             data["Nombre subsector económico"], data ["Total ingresos netos"],
                             data["Total costos y gastos"], data ["Total saldo a pagar"], data["Total saldo a favor"]
        )
    lt.addLast(data_structs["data"], informacion)
    
    return data_structs


def infor_impu(anio, codigo_actividad, nombre_actividad, codigo_sector, nombre_sector, codigo_subsector, nombre_subsector, total_ingresos, total_costos, total_saldo, total_saldo_favor):
    
    tabla_info = {}
    
    tabla_info["Año"]= int(anio)
    tabla_info["Código actividad económica"]= int(codigo_actividad)
    tabla_info["Nombre actividad económica"]=nombre_actividad
    tabla_info["Código sector económico"] = int(codigo_sector)
    tabla_info["Nombre sector económico"] = nombre_sector
    tabla_info["Código subsector económico"]=int(codigo_subsector)
    tabla_info["Nombre subsector económico"]=nombre_subsector
    tabla_info["Total ingresos netos"]= int(total_ingresos)
    tabla_info["Total costos y gastos"]=int(total_costos)
    tabla_info["Total saldo a pagar"]=int(total_saldo)
    tabla_info["Total saldo a favor"]=int(total_saldo_favor)
    return tabla_info
