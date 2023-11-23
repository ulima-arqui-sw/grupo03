# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 23:49:30 2023

@author: Frank
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 02:23:04 2023

@author: Frank
"""

"""
    CLIENTE
"""

import sqlite3


# Función para mostrar todos los productos en la base de datos
def mostrar_productos():
    conn = sqlite3.connect('C:/Users/Frank/Desktop/sqlite/bdprueba.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    for producto in productos:
        print(producto)

    conn.close()

# Ejecución basada en el input del usuario
while True:
    print("\n¿Qué acción desea realizar?")
    print("1. Mostrar todos los productos")
    print("2. Salir")

    opcion = input("Ingrese el número de la acción que desea realizar: ")

    if opcion == "1":
        print("Productos existentes:")
        mostrar_productos()

    elif opcion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")

