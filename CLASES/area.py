import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c

class area:
    
    def __init__(self,nombre,identificador):
        self.nombre=nombre
        self.identificador=identificador
        print("se creo area correctamente")
        self.alta_area()


    def alta_area(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO area(nombre,identificador) VALUES (%s,%s)"
            values = (self.nombre,self.identificador)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_area(identv,idenn,nombre):
        a=c.start_connection()
        cursor=a.cursor()
        query = "SELECT idarea FROM area WHERE identificador=%s"
        values =identv
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        ida = str(b[0][0])
        try:
            query = "UPDATE area SET nombre=%s WHERE idarea=%s"
            values = (nombre,ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET identificador=%s WHERE idarea=%s"
            values = (idenn,ida)
            cursor.execute(query, values)
            a.commit()  
            print("se modifico area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def eliminar_area(identificador):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "DELETE FROM area WHERE identificador=%s"
            values = identificador
            cursor.execute(query, values)
            a.commit()
            print("se elimino area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def contar_filas():
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM area"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

    def listar_area():
            a = c.start_connection()
            cursor = a.cursor()
            try:
                query = "SELECT nombre,identificador FROM area"
                cursor.execute(query)
                area = cursor.fetchall()
                a.commit()
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)
            return area

    def mostrar_area(iden):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT nombre,identificador FROM area WHERE identificador=%s")
        cursor.execute(query,iden)
        data = cursor.fetchall()
        a.commit()
        return data
