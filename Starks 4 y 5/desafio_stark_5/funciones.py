import os
import json
from data_stark import *

# PRIMERA PARTE
def leer_archivo(nombre_archivo: str): #1.1
    """
    brief: Lee el contenido de un archivo.
    parametros:
        - nombre_archivo(str): Nombre del archivo a leer.
    return: Contenido del archivo o None si no existe.
    """
    contenido = None
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
    return contenido

def guardar_archivo(nombre_archivo: str, contenido: str):
    """
    brief: Guarda contenido en un archivo.
    parametros:
        - nombre_archivo(str): Nombre del archivo a crear/guardar.
        - contenido(str): Contenido a escribir en el archivo.
    return: True si se guardó correctamente, False si hay un error.
    """
    resultado = True
    archivo = None
    mensaje = ""

    archivo = open(nombre_archivo, 'w', encoding='utf-8')
    archivo.write(contenido)
    archivo.close()
    mensaje = f"Se creó el archivo: {nombre_archivo}"

    if mensaje:
        print(mensaje)
    else:
        print(f"Error al crear el archivo: {nombre_archivo}")
        resultado = False

    return resultado

def generar_csv(nombre_archivo: str, lista_recibida: list): #1.3
    """
    brief: Genera un archivo CSV a partir de una lista.
    parametros:
        - nombre_archivo(str): Nombre del archivo CSV a crear.
        - lista_recibida(list): Lista.
    return: True si se generó el archivo correctamente y no existe, False si hay un error o el archivo ya existe.
    """
    resultado = False  # Inicializamos el resultado como False

    if not lista_recibida:
        print("La lista está vacía.")
    else:
        encabezado = "nombre,identidad,empresa,altura,peso,genero,color_ojos,color_pelo,fuerza,inteligencia\n"
        contenido_csv = encabezado

        for elemento in lista_recibida:
            nombre = elemento.get("nombre", "")
            identidad = elemento.get("identidad", "")
            empresa = elemento.get("empresa", "")
            altura = elemento.get("altura", "")
            peso = elemento.get("peso", "")
            genero = elemento.get("genero", "")
            color_ojos = elemento.get("color_ojos", "")
            color_pelo = elemento.get("color_pelo", "")
            fuerza = elemento.get("fuerza", "")
            inteligencia = elemento.get("inteligencia", "")

            contenido_csv += f"{nombre},{identidad},{empresa},{altura},{peso},{genero},{color_ojos},{color_pelo},{fuerza},{inteligencia}\n"

        if os.path.exists(nombre_archivo):
            print("Este archivo CSV ya existe.")
        else:
            resultado = guardar_archivo(nombre_archivo, contenido_csv)

    return resultado

def leer_csv(nombre_archivo: str): #1.4
    """
    brief: Lee un archivo CSV y devuelve una lista.
    parametros:
        - nombre_archivo(str): Nombre del archivo CSV a leer.
    return: Retorna la lista o False si hay un error.
    """
    contenido = leer_archivo(nombre_archivo)

    if not contenido or not contenido.splitlines():
        print(f"El archivo {nombre_archivo} está vacío o no se pudo leer.")
        lista_recibida = False
    else:
        encabezado, *lineas = contenido.splitlines()
        claves = encabezado.split(',')
        lista_recibida = [{clave: valor for clave, valor in zip(claves, linea.split(','))} for linea in lineas]

    return lista_recibida

def generar_json(nombre_archivo: str, lista_recibida: list, nombre_lista: str): #1.5
    """
    brief: Genera un archivo JSON a partir de una lista.
    parametros:
        - nombre_archivo(str): Nombre del archivo JSON a crear.
        - lista_recibida(list): La lista recibida.
        - nombre_lista(str): Nombre de la lista en el archivo JSON.
    return: True si se generó el archivo correctamente y no existe, False si hay un error o el archivo ya existe.
    """
    retorno = False

    if not lista_recibida:
        print("La lista se encuentra vacía.")
    else:
        datos = {nombre_lista: lista_recibida}

        if os.path.exists(nombre_archivo):
            print("Este archivo JSON ya existe.")
        else:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=4)
                print(f"Se creó el archivo JSON: {nombre_archivo}")
                retorno = True  # Cambiamos el valor de retorno a True si no hay errores

    return retorno

def leer_json(nombre_archivo: str, nombre_lista: str): #1.6
    """
    brief: Lee un archivo JSON y devuelve una lista.
    parametros:
        - nombre_archivo(str): Nombre del archivo JSON a leer.
        - nombre_lista(str): Nombre de la lista en el archivo JSON.
    return: Lista recibida o False si hay un error.
    """
    archivo = None
    try:
        archivo = open(nombre_archivo, 'r', encoding='utf-8')
    except FileNotFoundError:
        if archivo:
            archivo.close()
        print(f"El archivo JSON '{nombre_archivo}' no existe.")
        return False

    contenido = archivo.read()
    archivo.close()

    try:
        datos = json.loads(contenido)
        if nombre_lista in datos:
            return datos[nombre_lista]
        else:
            print(f"La lista '{nombre_lista}' no se encontró en el archivo JSON.")
            return False
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON '{nombre_archivo}': {str(e)}")
        return False

# SEGUNDA PARTE
def ordenar_heroes_ascendente(lista_heroes: list, clave: str):
    """
    brief: Ordena una lista de heroes en orden ascendente por una clave.
    parametros:
        - lista_heroes(list): Lista de heroes.
        - clave(str): Clave por la cual ordenar.
    return: Lista ordenada.
    """
    return sorted(lista_heroes, key=lambda x: float(x[clave]))

def ordenar_heroes_descendente(lista_heroes: list, clave: str):
    """
    brief: Ordena una lista de heroes en orden descendente por una clave.
    parametros:
        - lista_heroes(list): Lista de heroes.
        - clave(str): Clave por la cual ordenar.
    return: Lista ordenada.
    """
    return sorted(lista_heroes, key=lambda x: float(x[clave]), reverse=True)

def ordenar_heroes_por_clave(lista_heroes: list, clave: str, orden: str): # 2.3
    """
    brief: Ordena una lista de heroes por una clave en un orden específico.
    parametros:
        - lista_heroes(list): Lista de heroes.
        - clave(str): Clave por la cual ordenar.
        - orden(str): 'ascendente' o 'descendente'.
    return: Lista ordenada.
    """
    if orden == 'ascendente':
        return ordenar_heroes_ascendente(lista_heroes, clave)
    elif orden == 'descendente':
        return ordenar_heroes_descendente(lista_heroes, clave)
    else:
        print("Opción de orden no válida. Utilice 'asc' o 'desc'.")

def normalizar_datos(lista_recibida: list):
    """
    brief: Normaliza los datos numéricos (flotantes o enteros) en una lista.
    parametros:
        - lista_recibida(list): Lista de superhéroes.
    return: Lista normalizada.
    """
    try:
        for elemento in lista_recibida:
            for clave, valor in elemento.items():
                if valor.replace('.', '', 1).isdigit():
                    if '.' in valor:
                        elemento[clave] = float(valor)
                    else:
                        elemento[clave] = int(valor)
        return lista_recibida
    except Exception:
        print(f"Error al normalizar datos: Los datos ya se encuentran normalizados")
        return None

def listar_heroes_ordenados_por_altura_asc(nombre_archivo: str): #4
    """
    brief: Lista y muestra los heroes ordenados por altura de forma ascendente.
    parametros:
        - nombre_archivo(str): Nombre del archivo CSV a leer.
    """
    if os.path.exists(nombre_archivo):
        lista_heroes_csv = leer_csv(nombre_archivo)
        if lista_heroes_csv:
            lista_ordenada_ascendente = ordenar_heroes_por_clave(lista_heroes_csv, "altura", "ascendente")
            for heroe in lista_ordenada_ascendente:
                print(f"Nombre del heroe: {heroe['nombre']} - Altura: {heroe['altura']}\n")

def listar_heroes_ordenados_por_peso_desc(nombre_archivo: str): #5
    """
    brief: Lista y muestra los heroes ordenados por peso de forma descendente.
    parametros:
        - nombre_archivo(str): Nombre del archivo JSON a leer.
    """
    if os.path.exists(nombre_archivo):
        lista_recibida_json = leer_json(nombre_archivo, "heroes")
        if lista_recibida_json:
            lista_ordenada_descendente = ordenar_heroes_por_clave(lista_recibida_json, "peso", "descendente")
            for heroe in lista_ordenada_descendente:
                print(f"Nombre del heroe: {heroe['nombre']} - Peso: {heroe['peso']}\n")

def ordenar_lista_por_fuerza(lista_recibida: list, orden: str):
    """
    brief: Ordena y muestra la lista de heroes por fuerza en un orden específico.
    parametros:
        - lista_recibida(list): Lista recibida.
        - orden(str): Indica si sera 'ascendente' o 'descendente'.
    """
    if orden == "ascendente":
        lista_ordenada = ordenar_heroes_ascendente(lista_recibida, "fuerza")
    elif orden == "descendente":
        lista_ordenada = ordenar_heroes_descendente(lista_recibida, "fuerza")
    else:
        print("Opción de orden no válida. Utilice 'ascendente' o 'descendente'.")

    for heroe in lista_ordenada:
        print(f"Nombre del heroe: {heroe['nombre']} - Fuerza: {heroe['fuerza']}\n")