from typing import AbstractSet
import os
import pymysql
from pymysql import connect, err
from pymysql.err import Error

# ELIMINAR TABLA
DROP_TABLE = """DROP TABLE IF EXISTS produc"""
# CREAR TABLA
PRODUCTS_TABLE = """CREATE TABLE produc (  
        id int UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,  
        nombre VARCHAR(30) NOT NULL,
        apellido VARCHAR(30) NOT NULL,
        edad int(2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""

users = [
    ("Angel", "Andrade", 22),
    ("Ignacio", "Atim", 21),
    ("Perez", "Raid", 21)
]

def crear_usuario(connect,cursor):
    nombre = input("Ingresa su nombre: ")
    apellido = input("Ingresa su apellido: ")
    while True:
        edad = input("Ingrese edad: ")
        try:
            edad = int(edad)
            query= "INSERT INTO produc(nombre,apellido,edad) VALUES (%s,%s,%s)"
            values = (nombre, apellido,edad)
            cursor.execute(query,values)
            connect.commit()
            return edad
        except ValueError:
            print ("ATENCIÓN: Debe ingresar un número entero.")





if __name__ == '__main__':
    try:
        connect = pymysql.Connect(
            host="localhost",
            port=3306,
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('PASSWORD_MYSQL'),
            database=os.environ.get('DB_MYSQL'))

        with connect.cursor() as cursor:
            # Eliminar tabla
            cursor.execute(DROP_TABLE)
            # Agregar tabla
            cursor.execute(PRODUCTS_TABLE)

            # CREAR 1 REGISTRO
            query = "INSERT INTO produc(nombre,apellido,edad) VALUES(%s,%s,%s)"
            values = ("Nicolas", "ajir", 20)
            cursor.execute(query, values)

            # CREAR MÚLTIPLES REGISTROS
            query = "INSERT INTO produc(nombre,apellido,edad) VALUES(%s,%s,%s)"
            # 1° forma

            # for user in users:
            #   cursor.execute(query,user)

            # 2° forma
            cursor.executemany(query, users)
            connect.commit()  # siempre utilizar commit para confirmar

            # Obtener registros
            query = "SELECT id,nombre,apellido,edad FROM produc WHERE id < 3"
            nmro_usuarios = cursor.execute(query)
            # devuelve cantidad de usuarios en la consulta
            print(nmro_usuarios)

            for user in cursor.fetchall():
                print(user)
                # Muestra c/u

            #Modificar registros
            query = "UPDATE produc SET nombre = %s WHERE id = %s"
            values = ("Lautaro", 1)
            cursor.execute(query, values)
            connect.commit()

            #Eliminar registros
            query = "DELETE FROM produc WHERE nombre = %s"
            cursor.execute(query,"Perez")
            connect.commit()

            crear_usuario(connect,cursor)

    except pymysql.err.OperationalError as err:
        print("hubo un error:", err)

    finally:
        connect.close()
        print("se cerro la conexión con éxito")
        # SIEMPRE CERRAR CUANDO NO SE LO UTILIZA MÁS, ASI LIBERA PROCESOS.
