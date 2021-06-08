import pymysql
import os
from DB import conexion as c

def crear_usuario(nombre,apellido,tipo,alta,puesto,nacimiento):
    a=c.start_connection()
    try:
        cursor=a.cursor()
        query = "INSERT INTO usuarios(nombre,apellido,tipo,alta,puesto,nacimiento) VALUES (%s,%s,%s,%s,%s,%s)"
        values = (nombre, apellido, tipo,alta, puesto, nacimiento)
        cursor.execute(query, values)
        a.commit()
        print("se creo correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def borrar_usuario(nombre,apellido):
    a=c.start_connection()
    try:
        cursor=a.cursor()
        query = "DELETE usuarios WHERE nombre= %s AND apellido=%s"
        values = (nombre, apellido)
        cursor.execute(query, values)
        a.commit()
        print("se borro correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def ab_usuario(nombre,apellido):
    a=c.start_connection()
    try:
        cursor=a.cursor()
        query = "UPDATE usuarios set alta= IF(alta = '0', alta + 1, alta-1) WHERE nombre= %s AND apellido=%s"
        values = (nombre, apellido)
        cursor.execute(query, values)
        a.commit()
        print("se MODIFICO correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)

def mostrar_usuario(nombre,apellido):
    a=c.start_connection()
    try:
        cursor=a.cursor()
        query = "SELECT * FROM usuarios WHERE nombre= %s AND apellido=%s"
        values = (nombre, apellido)
        cursor.execute(query, values)
        a.commit()
        b=cursor.fetchall()
        b=str(b[0])
        print(b)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)