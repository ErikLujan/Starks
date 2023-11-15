from funciones import *

datos_normalizados = False

# Menu Principal del programa
while True:
    print("-----------------------------------------------------------------------------------------------------------------------------------\nOpciones: \n")
    print("1-Normalizar datos")
    print("2-Generar CSV")
    print("3-Listar héroes del archivo CSV ordenados por altura ASC")
    print("4-Generar JSON")
    print("5-Listar héroes del archivo JSON ordenados por peso DESC")
    print("6-Ordenar Lista por fuerza")
    print("7-Salir\n-----------------------------------------------------------------------------------------------------------------------------------")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        lista_personajes_normalizada = normalizar_datos(lista_personajes)
        if lista_personajes_normalizada is not None:
            lista_personajes = lista_personajes_normalizada
            datos_normalizados = True
            print("-----------------------------------------------------------------------------------------------------------------------------------\nDatos normalizados con éxito.\n-----------------------------------------------------------------------------------------------------------------------------------")
    elif opcion == "2" and datos_normalizados:
        generar_csv("desafio_stark_5/lista_heroes.csv", lista_personajes)
    elif opcion == "3" and datos_normalizados:
        listar_heroes_ordenados_por_altura_asc("desafio_stark_5/lista_heroes.csv")
    elif opcion == "4" and datos_normalizados:
        generar_json("desafio_stark_5/lista_heroes.json", lista_personajes, "heroes")
    elif opcion == "5" and datos_normalizados:
        listar_heroes_ordenados_por_peso_desc("desafio_stark_5/lista_heroes.json")
    elif opcion == "6" and datos_normalizados:
        orden = input("-----------------------------------------------------------------------------------------------------------------------------------\n¿Deseas ordenar la lista por fuerza de manera ascendente (ascendente) o descendente (descendente)?\n-----------------------------------------------------------------------------------------------------------------------------------\nOrden elegido: ")
        ordenar_lista_por_fuerza(lista_personajes, orden)
    elif opcion == "7":
        print("Saliste del menu.")
        break
    else:
        print("Opción no válida o datos sin normalizar. Intente nuevamente y asegurese de tener los datos normalizados.")