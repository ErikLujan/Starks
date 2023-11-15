from data_stark import lista_personajes
import re

def extraer_iniciales(nombre_heroe: str) -> str: #1.1
    """
    brief: extrae las iniciales de un nombre de héroe y las devuelve en mayúsculas.
    parametros: nombre_heroe nombre_limpio iniciales
    return: iniciales
    """
    if not nombre_heroe:
        retorno = "N/A"
    nombre_limpio = re.sub(r'\bthe\b', '', nombre_heroe, flags=re.IGNORECASE)
    nombre_limpio = nombre_limpio.replace('-', ' ')
    iniciales = re.findall(r'\b\w', nombre_limpio, re.IGNORECASE)
    retorno = '.'.join(iniciales).upper() + '.'
    return retorno

def obtener_dato_formato(dato: str): #1.2
    """
    brief: Convierte un dato en formato de cadena a un formato específico.
    parametros:
        - dato (str): El dato que se desea convertir.
    return: El dato convertido en el formato especificado.
    """
    if type(dato) != str:
        resultado = False
    else:
        dato = dato.lower()
        resultado = re.sub(" ", "_", dato)
        return resultado

def stark_imprimir_nombre_con_iniciales(dic: dict):  # 1.3
    """
    brief: Retorna el nombre de un héroe junto con sus iniciales.
    parametros:
        - dic (dict): Un diccionario que contiene la información del héroe.
    return: El nombre con las iniciales si se pudo obtener correctamente, de lo contrario None.
    """
    if type(dic) == dict and "nombre" in dic.keys():
        return f"{dic['nombre']} ({extraer_iniciales(dic['nombre'])})"
    else:
        return None

def stark_imprimir_nombres_con_iniciales(lista_heroes: list):  # 1.1
    """
    brief: Imprime la lista de nombres junto con las iniciales de los héroes.
    parametros:
        - lista_heroes (list): Una lista de diccionarios que contienen la información de los héroes.
    return: Una cadena que contiene los nombres de los héroes junto con sus iniciales.
    """
    cadena_generada = ""
    for dic in lista_heroes:
        if type(dic) == dict and "nombre" in dic.keys():
            cadena_generada += f"{dic['nombre']} ({extraer_iniciales(dic['nombre'])})\n"

    return cadena_generada

def generar_codigo_heroe(dic: dict, id: int):  # 2.1
    """
    brief: Genera un código único para un héroe.
    parametros:
        - dic (dict): Un diccionario que contiene la información del héroe.
        - id (int): El identificador único del héroe.
    return: El código generado para el héroe.
    """

    if dic['genero'] not in ["M", "F", "NB"] or dic['genero'] == "":
        return "N/A"
    else:
        if dic['genero'] == "M":
            primer_numero = 1
        elif dic['genero'] == "F":
            primer_numero = 2
        else:  # Si el género es NB
            primer_numero = 0
        
        id_str = str(id).zfill(7)

        codigo = f"{dic['genero']} - {primer_numero}{id_str}"
        return codigo

def stark_generar_codigos_heroes(lista_heroes: list):  # 2.2
    """
    brief: Genera y muestra los códigos de los héroes de una lista.
    parametros:
        - lista_heroes (list): Una lista de diccionarios que contienen la información de los héroes.
    return: Una cadena que contiene los nombres de los héroes junto con sus códigos.
    """
    cadena_generada = ""
    for personaje in range(len(lista_heroes)):
        if type(lista_heroes[personaje]) == dict and len(lista_heroes) > 0:
            nombre_con_iniciales = stark_imprimir_nombre_con_iniciales(lista_heroes[personaje])
            codigo = generar_codigo_heroe(lista_heroes[personaje], personaje + 1)
            cadena_generada += f"{nombre_con_iniciales} | {codigo}\n"
    return cadena_generada

def sanitizar_entero(num_str: str) -> int: #3.1
    """
    brief: Sanitiza un string y la convierte en un número entero válido.
    parametros:
        - num_str (str): El string que se desea sanitizar.
    return: El número entero sanitizado.
    """
    if type(num_str) is not str:
        num_str = str(num_str)

    num_str = num_str.strip()
    resultado = -1

    if num_str.isdigit():
        numero = int(num_str)
        if numero >= 0:
            resultado = numero
        else:
            resultado = -2
    else:
        resultado = -3

    return resultado

def sanitizar_flotante(numero_str: str) -> float:
    """
    brief: Sanitiza un string y lo convierte en un número de punto flotante válido.
    parametros:
        - numero_str (str): El string que se desea sanitizar.
    return: El número de punto flotante sanitizado.
    """
    if type(numero_str) is not str:
        return -1
    
    numero_str = numero_str.strip()
    resultado = -1
    
    if numero_str.replace('.', '', 1).isdigit() and not numero_str.startswith('-'):
        try:
            resultado = float(numero_str)
        except ValueError:
            resultado = sanitizar_entero(numero_str)
    
    if resultado < 0:
        resultado = -2
    
    return resultado

def sanitizar_string(valor_str: str, valor_por_defecto: str = '-') -> str: #3.3
    """
    brief: Sanitiza un string y la devuelve en minúsculas.
    parametros:
        - valor_str (str): El string que se desea sanitizar.
        - valor_por_defecto (str): El valor por defecto que se utilizará si el string no es válido.
    return: El string sanitizada en minúsculas.
    """
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()

    resultado = valor_por_defecto.lower()

    if valor_str.replace(" ", "").replace("/", "").isalpha():
        valor_str = valor_str.replace("/", " ")
        if valor_str != "":
            resultado = valor_str.lower()
    elif any(char.isdigit() for char in valor_str):
        resultado = "N/A"

    return resultado

def sanitizar_dato(heroe: dict, clave: str, tipo_dato: str): #3.4
    """
    brief: Sanitiza un dato específico de un héroe.
    parametros:
        - heroe (dict): Un diccionario que contiene la información del héroe.
        - clave (str): La clave del dato que se desea sanitizar.
        - tipo_dato (str): El tipo de dato que se desea sanitizar.
    """
    if clave in heroe:
        valor = heroe[clave]
        if tipo_dato == 'string':
            heroe[clave] = sanitizar_string(valor)
        elif tipo_dato == 'entero':
            heroe[clave] = sanitizar_entero(valor)
        elif tipo_dato == 'flotante':
            heroe[clave] = sanitizar_flotante(valor)

def stark_normalizar_datos(lista: list): #3.5
    """
    brief: Normaliza los datos de los héroes en una lista.
    parametros:
        - lista (list): Una lista de diccionarios que contienen la información de los héroes.
    """
    if not lista:
        print("Error: Lista de héroes vacía")
        return
    
    for heroe in lista:
        sanitizar_dato(heroe, 'altura', 'flotante')
        sanitizar_dato(heroe, 'peso', 'flotante')
        sanitizar_dato(heroe, 'color_ojos', 'string')
        sanitizar_dato(heroe, 'color_pelo', 'string')
        sanitizar_dato(heroe, 'fuerza', 'entero')
        sanitizar_dato(heroe, 'inteligencia', 'entero')
    
    print("Datos normalizados")

def stark_imprimir_indice_nombre(lista_heroes: list): #4.1
    """
    brief: Imprime el índice y el nombre de los héroes en una lista.
    parametros:
        - lista_heroes (list): Una lista de diccionarios que contienen la información de los héroes.
    """
    for elemento in lista_heroes:
        nombre = elemento['nombre']
        palabras = re.findall(r'\b(?!the\b)\w+\b', nombre, flags=re.IGNORECASE)
        nombre_limpio = '-'.join(palabras)
        print(nombre_limpio)

def generar_separador(patron: str, largo: int, imprimir=True):
    """
    brief: Genera un separador utilizando un patrón y un largo específico.
    parametros:
        - patron (str): El patrón utilizado para generar el separador.
        - largo (int): La longitud del separador.
        - imprimir (bool): Un indicador de si se debe imprimir el separador generado.
    return: El separador generado.
    """
    if len(patron) < 1 or len(patron) > 2 or type(largo) != int or largo < 1 or largo > 235:
        separador = 'N/A'
    else:
        separador = patron * largo
        if imprimir:
            print(separador)
    
    return separador

def generar_encabezado(titulo: str): #5.2
    """
    brief: Genera un encabezado utilizando un título específico.
    parametros:
        - titulo (str): El título utilizado para generar el encabezado.
    return: El encabezado generado.
    """
    separador = generar_separador("*", 131, imprimir=False)
    titulo_mayusculas = titulo.upper()
    encabezado = f"{separador}\n{titulo_mayusculas}\n{separador}"
    return encabezado

def imprimir_ficha_heroe(heroe: dict, lista_heroes: list):  # 5.3
    """
    brief: Imprime la ficha de un héroe.
    parametros:
        - heroe (dict): Un diccionario que contiene la información del héroe.
        - lista_heroes (list): Una lista de diccionarios que contienen la información de los héroes.
    """
    separador_principal = generar_encabezado("PRINCIPAL")
    separador_fisico = generar_encabezado("FISICO")
    separador_señas_particulares = generar_encabezado("SEÑAS PARTICULARES")
    
    print(separador_principal)
    iniciales = extraer_iniciales(heroe['nombre'])
    print(f"NOMBRE DEL HÉROE: {heroe['nombre']} ({iniciales})")
    print(f"IDENTIDAD SECRETA: {heroe['identidad']}")
    print(f"CONSULTORA: {heroe['empresa']}")
    
    codigo_heroe = stark_generar_codigos_heroes(lista_heroes).split('\n')[lista_heroes.index(heroe)].split('|')[1].strip()
    print(f"CÓDIGO DE HÉROE: {codigo_heroe}")
    
    print(separador_fisico)
    print(f"ALTURA: {heroe['altura']:.2f} cm")
    print(f"PESO: {heroe['peso']:.2f} kg")
    print(f"FUERZA: {heroe['fuerza']} N")
    print(f"GENERO: {heroe['genero']}")
    
    print(separador_señas_particulares)
    print(f"COLOR DE OJOS: {heroe['color_ojos']}")
    print(f"COLOR DE PELO: {heroe['color_pelo']}")

def stark_navegar_fichas(lista_heroes: list): #5.5
    """
    brief: Permite navegar y mostrar las fichas de los héroes en una lista.
    parametros:
        - lista_heroes (list): Una lista de diccionarios que contienen la información de los héroes.
    """
    indice_actual = 0
    cantidad_heroes = len(lista_heroes)
    
    while True:
        imprimir_ficha_heroe(lista_heroes[indice_actual], lista_heroes)
        opcion = input("-----------------------------------------------------------------------------------------------------------------------------------\nIngrese una de las siguientes opciones:\n--- \n[1] Ir a la izquierda \n--- \n[2] Ir a la derecha \n--- \n[3] Salir \n----------------------------------------------------------------------------------------------------------------------------------- \nOpcion Ingresada: ")

        if opcion == "1":
            indice_actual = (indice_actual - 1) % cantidad_heroes
        elif opcion == "2":
            indice_actual = (indice_actual + 1) % cantidad_heroes
        elif opcion == "3":
            print("Has salido")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")