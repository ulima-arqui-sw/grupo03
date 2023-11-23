# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 02:23:04 2023

@author: Frank
"""

"""
    ADMINISTRADOR
"""

import sqlite3

# Función para verificar la contraseña
def verificar_contraseña():
    intentos = 3
    while intentos > 0:
        contraseña_ingresada = input("Ingrese la contraseña para acceder: ")
        if contraseña_ingresada == "administrador":  # Reemplaza con tu contraseña deseada
            return True
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")
    return False


# Función para mostrar todos los productos en la base de datos
def mostrar_productos():
    conn = sqlite3.connect('C:/Users/Frank/Desktop/sqlite/bdprueba.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    for producto in productos:
        print(producto)

    conn.close()

# Función para agregar un nuevo producto
def agregar_producto(nombre, precio, stock):
    conn = sqlite3.connect('C:/Users/Frank/Desktop/sqlite/bdprueba.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)', (nombre, precio, stock))

    conn.commit()
    conn.close()

# Función para actualizar el stock de un producto
def actualizar_stock(id_producto, nuevo_stock):
    conn = sqlite3.connect('C:/Users/Frank/Desktop/sqlite/bdprueba.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE productos SET stock = ? WHERE id = ?', (nuevo_stock, id_producto))

    conn.commit()
    conn.close()

# Función para eliminar un producto por su ID
def eliminar_producto(id_producto):
    conn = sqlite3.connect('C:/Users/Frank/Desktop/sqlite/bdprueba.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM productos WHERE id = ?', (id_producto,))

    conn.commit()
    conn.close()



# Ejecución basada en el input del usuario
if verificar_contraseña():
    print("Acceso concedido.")
    while True:
        print("\n¿Qué acción desea realizar?")
        print("1. Mostrar todos los productos")
        print("2. Agregar un nuevo producto")
        print("3. Actualizar el stock de un producto")
        print("4. Eliminar un producto")
        print("5. Salir")

        opcion = input("Ingrese el número de la acción que desea realizar: ")

        if opcion == "1":
            print("Productos existentes:")
            mostrar_productos()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del nuevo producto: ")
            precio = float(input("Ingrese el precio del nuevo producto: "))
            stock = int(input("Ingrese el stock del nuevo producto: "))
            agregar_producto(nombre, precio, stock)
            print("Producto agregado exitosamente.")
        elif opcion == "3":
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
            actualizar_stock(id_producto, nuevo_stock)
            print("Stock actualizado exitosamente.")
        elif opcion == "4":
            id_producto = int(input("Ingrese el ID del producto a eliminar: "))
            eliminar_producto(id_producto)
            print("Producto eliminado exitosamente.")
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
else:
    print("Demasiados intentos incorrectos. Acceso denegado.")

