from funciones import *

def menu_principal(lista_heroes: list):
    """
    brief: Muestra un menú principal y permite al usuario seleccionar diferentes opciones para interactuar con la lista de héroes.
    parametros:
        - lista_heroes (list): Una lista de diccionarios que contienen la información de los héroes.
    """
    datos_normalizados = False

    while True:
        print("-----------------------------------------------------------------------------------------------------------------------------------\n---- MENÚ PRINCIPAL ----")
        print("1 - Imprimir la lista de nombres junto con sus iniciales")
        print("2 - Imprimir la lista de nombres y el código del mismo")
        print("3 - Normalizar datos")
        print("4 - Imprimir índice de nombres")
        print("5 - Navegar fichas")
        print("6 - Salir \n-----------------------------------------------------------------------------------------------------------------------------------")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            nombre_con_iniciales = stark_imprimir_nombres_con_iniciales(lista_heroes)
            print(nombre_con_iniciales)
        elif opcion == "2":
            codigos_generados = stark_generar_codigos_heroes(lista_heroes)
            print(codigos_generados)
        elif opcion == "3":
            stark_normalizar_datos(lista_heroes)
            datos_normalizados = True  # Actualizamos la variable de normalización
        elif opcion == "4" and datos_normalizados:
            stark_imprimir_indice_nombre(lista_heroes)
        elif opcion == "5" and datos_normalizados:
            stark_navegar_fichas(lista_heroes)
        elif opcion == "6":
            print("Saliste del Menú")
            break
        else:
            print("Opción inválida o No se encuentra normalizada, asegurese de elegir una opcion valida/normalizada.")

menu_principal(lista_personajes)