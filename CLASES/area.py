import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c

class Area:
    #HOlA
    def __init__(self,nombre,identificador,pasillos,segmentos,longitud,ancho,alto):
        self.nombre=nombre
        self.identificador=identificador
        self.pasillos=pasillos
        self.segmentos=segmentos
        self.longitud=longitud
        self.ancho=ancho
        self.alto=alto
        self.disponibilidad=0
        print("se creo area correctamente")
        self.alta_area()


    def alta_area(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO area(nombre,identificador,pasillos,segmentos,longitud,ancho,alto,disponibilidad) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (self.nombre,self.identificador,self.pasillos,self.segmentos,self.disponibilidad,self.longitud,self.ancho,self.alto)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_area(nombrev,nombren,iden,pasillos,segmentos,disponibilidad,longitud,ancho,alto):
        a=c.start_connection()
        cursor=a.cursor()
        query = "SELECT idarea FROM area WHERE nombre=%s"
        values =nombrev
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        ida = str(b[0][0])
        try:
            query = "UPDATE area SET nombre=%s WHERE idarea=%s"
            values = (nombren,ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET identificador=%s WHERE idarea=%s"
            values = (iden,ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET pasillos=%s WHERE idarea=%s"
            values = (pasillos,ida)
            cursor.execute(query, values)
            a.commit() 
            query = "UPDATE area SET segmentos=%s WHERE idarea=%s"
            values = (segmentos,ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET disponibilidad=%s WHERE idarea=%s"
            values = (disponibilidad,ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET longitud=%s WHERE idarea=%s"
            values = (longitud,ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET ancho=%s WHERE idarea=%s"
            values = (ancho,ida)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE area SET alto=%s WHERE idarea=%s"
            values = (alto,ida)
            cursor.execute(query, values)
            a.commit()   
            print("se modifico area correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def eliminar_area(nombre):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "DELETE FROM area WHERE nombre=%s"
            values = nombre
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
                query = "SELECT nombre,identificador,pasillos,segmentos,disponibilidad FROM area"
                cursor.execute(query)
                area = cursor.fetchall()
                a.commit()
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)
            return area

    def mostrar_identificador(nombre):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT nombre FROM area WHERE identificador=%s")
        cursor.execute(query,nombre)
        data = cursor.fetchall()
        a.commit()
        return data

    def mostrar_area(nombre):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT nombre,identificador,pasillos,segmentos,disponibilidad,longitud,ancho,alto FROM area WHERE nombre=%s")
        cursor.execute(query,nombre)
        data = cursor.fetchall()
        a.commit()
        return data