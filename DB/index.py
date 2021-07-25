from typing import AbstractSet
import os
import sys
import pymysql
from pymysql import connect, err
import numpy as np
from pymysql import cursors
from pymysql.err import Error
sys.path.append(".")
from DB import db as db


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





# CREAR NUEVO USUARIO - VERIFICAR NÚMERO ENTERO

def crearUser(connect,cursor,codigo, password):
    
    cursor = connect.cursor()
    query = "INSERT INTO usuarios(Codigo,Password) VALUES (%s,%s)"
    values = (codigo, password)
    cursor.execute(query, values)
    connect.commit()
 


def crear_usuario(connect, cursor):
    nombre = input("Ingresa su nombre: ")
    apellido = input("Ingresa su apellido: ")
    while True:
        edad = input("Ingrese edad: ")
        try:
            edad = int(edad)
            query = "INSERT INTO produc(nombre,apellido,edad) VALUES (%s,%s,%s)"
            values = (nombre, apellido, edad)
            cursor.execute(query, values)
            connect.commit()
            return edad
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero.")

# FUNCION LISTA USUARIOS


def listar_usuarios():
    c = db.start_connection()
    cursor = c.cursor()
    u = "USUARIOS: "
    query = "SELECT id,nombre,apellido FROM produc"
    cursor.execute(query)
    # 1
    # for id,nombre,apellido,edad in cursor.fetchall():
    #      print(id,"-", nombre, "-", apellido,"-",edad)
    # 2
    for user in cursor.fetchall():
        u += str(user)

    c.commit()
    db.close_connection(c)
    return(u)

# FUNCION MODIFICAR USUARIOS


def modificar_usuarios(connect, cursor):
    query = "UPDATE produc SET nombre=%s WHERE id=%s"
    values = ("raul", 1)
    cursor.execute(query, values)
    connect.commit()


# FUNCION ELIMINAR USUARIOS
def eliminar_usuarios(connect, cursor):
    query = "DELETE FROM produc WHERE id = %s"
    cursor.execute(query, 2)
    connect.commit()
    # CREAR 1 REGISTRO
    query = "INSERT INTO produc(nombre,apellido,edad) VALUES(%s,%s,%s)"
    values = ("Nicolas", "ajir", 20)
    cursor.execute(query, values)
    print(cursor)
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

    # Modificar registros
    query = "UPDATE produc SET nombre = %s WHERE id = %s"
    values = ("Lautaro", 1)
    cursor.execute(query, values)
    connect.commit()

    # Eliminar registros
    query = "DELETE FROM produc WHERE id = %s"
    cursor.execute(query, 3)
    connect.commit()
    # Ejecutar funciones
    #crear_usuario(connect, cursor)
    #listar_usuarios(connect, cursor)
    #modificar_usuarios(connect, cursor)
    #eliminar_usuarios(connect, cursor)
    
def verificar_usuario(cod,password):
        c = db.start_connection()
        cursor = c.cursor()
        query = "SELECT Codigo,Password FROM usuarios WHERE Codigo= %s AND Password = %s"
        values = (cod,password)
        o = cursor.execute(query,values)
        c.commit()
        db.close_connection(c)
        return (o)  
 
a = verificar_usuario(int("1"),"asd123")
print(a)

def mostrar_usuario(nombre,apellido):
    a=db.start_connection()
    try:
        cursor=a.cursor()
        query = "SELECT * FROM usuarios WHERE Codigo= %s AND Password=%s"
        values = (nombre, apellido)
        cursor.execute(query, values)
        a.commit()
        b=cursor.fetchall()
        b=str(b[0])
        print(b)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    db.close_connection(a)


