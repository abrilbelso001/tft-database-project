import mysql.connector


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",      
        database="tft"
    )


def buscar_composiciones_por_campeon(cursor):
    campeon = input("Introduce el nombre del campeón: ")

    consulta = """
    SELECT c.nombreComposicion, c.tier
    FROM composicion c
    JOIN composicioncampeon cc
        ON c.idComposicion = cc.idComposicion
    JOIN campeon ca
        ON cc.idCampeon = ca.idCampeon
    WHERE ca.nombreCampeon = %s;
    """

    cursor.execute(consulta, (campeon,))
    resultados = cursor.fetchall()

    if resultados:
        print("\nComposiciones encontradas:")
        for nombre, tier in resultados:
            print(f"- {nombre} | Tier: {tier}")
    else:
        print("No se han encontrado composiciones para ese campeón.")


def ver_build_campeon(cursor):
    campeon = input("Introduce el nombre del campeón: ")
    composicion = input("Introduce el nombre de la composición: ")

    consulta = """
    SELECT cci.slotItem, i.nombreItem
    FROM composicion c
    JOIN composicioncampeon cc
        ON c.idComposicion = cc.idComposicion
    JOIN campeon ca
        ON cc.idCampeon = ca.idCampeon
    JOIN composicioncampeonitem cci
        ON cc.idCompCampeon = cci.idCompCampeon
    JOIN item i
        ON cci.idItem = i.idItem
    WHERE ca.nombreCampeon = %s
      AND c.nombreComposicion = %s
    ORDER BY cci.slotItem;
    """

    cursor.execute(consulta, (campeon, composicion))
    resultados = cursor.fetchall()

    if resultados:
        print(f"\nBuild de {campeon} en {composicion}:")
        for slot, item in resultados:
            print(f"Slot {slot}: {item}")
    else:
        print("No se ha encontrado build para ese campeón en esa composición.")


def contar_campeones_por_composicion(cursor):
    consulta = """
    SELECT c.nombreComposicion,
           COUNT(cc.idCampeon) AS numCampeones
    FROM composicion c
    LEFT JOIN composicioncampeon cc
        ON c.idComposicion = cc.idComposicion
    GROUP BY c.idComposicion, c.nombreComposicion
    ORDER BY numCampeones DESC;
    """

    cursor.execute(consulta)
    resultados = cursor.fetchall()

    print("\nNúmero de campeones por composición:")
    for nombre, cantidad in resultados:
        print(f"- {nombre}: {cantidad} campeones")


def menu():
    conexion = conectar()
    cursor = conexion.cursor()

    opcion = ""

    while opcion != "4":
        print("\n--- MENÚ TFT ---")
        print("1. Buscar composiciones donde aparece un campeón")
        print("2. Ver la build de un campeón en una composición")
        print("3. Contar campeones por composición")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            buscar_composiciones_por_campeon(cursor)
        elif opcion == "2":
            ver_build_campeon(cursor)
        elif opcion == "3":
            contar_campeones_por_composicion(cursor)
        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opción no válida.")

    cursor.close()
    conexion.close()


menu()