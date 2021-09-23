import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c
import numpy as np

global area2

class matriz:
    def __init__(self,area,segmento,filas,nivel):
        global area2
        self.area=area
        self.codigo
        self.segmento=segmento
        self.filas=filas
        self.nivel=nivel
        self.disponibilidad=1
        area2=str("matriz"+str(self.area))

        print("se creo matriz correctamente")

    def crear_tabla_area(self):
        global area2
        a=c.start_connection()
        cursor=a.cursor()
        try:
            area2=str("matriz"+str(self.area))
            query = """ CREATE TABLE IF NOT EXISTS %s(
            idmatriz INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
            codigo VARCHAR(20) NOT NULL,
            area VARCHAR(20) NOT NULL,
            segmento VARCHAR(20) NOT NULL,
            fila VARCHAR(20) NOT NULL,
            nivel VARCHAR(20) NOT NULL,
            disponibilidad BINARY(1) NOT NULL
            );"""
            values = (self.area)
            cursor.execute(query, values)
            a.commit()
            print("se cargaron datos de la matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def nombre_tabla(self,area):
        global area2
        area2=str("matriz"+str(area))
        return area2
        

    def formar_matriz(self): #esta se usa cuantas veces se requiera formar la matriz
        self.importar_datos_matriz()
        mz=np.zeros((self.filas,self.nivel)) #acá creo la matriz
        i,j,k = 0,0,0
        while i<self.filas: #acá le doy altura
            while j<self.nivel:
                codigo=str(str(i)+str(j))
                a=c.start_connection()
                cursor=a.cursor()
                try: 
                    query = "UPDATE matriz set codigo=%s WHERE fila=%s and nivel=%s"
                    values = (codigo,i,j,k)
                    cursor.execute(query, values)
                    a.commit()
                except pymysql.err.OperationalError as err:
                    print("Hubo un error:", err)
                c.close_connection(a)
                j=j+1
                
            i=i+1
            j=0
        print("se formo la matriz correctamente")
        return mz

    def crear_matriz(self): #IMPORTANTE ejecutar una sola vez
        mz=np.zeros((self.filas,self.nivel)) #acá creo la matriz
        i,j = 0,0
        while i<self.filas:
            while j<self.nivel:

                codigo=str(str(self.area)+"-"+str(self.segmento)+"-"+str(i)+"-"+str(j))
                self.alta_matriz(codigo,self.area,self.segmento,i,j,self.disponibilidad)
                print(i,j)

                j=j+1
                
            i=i+1
            j=0
        
        print("se dio de alta a la matriz correctamente")
        return mz
        
    

    def alta_datos_matriz(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO datosmatriz(area,segmento,filas,nivel) VALUES (%s,%s,%s,%s)"
            values = (self.area,self.segmento,self.filas,self.columnas)
            cursor.execute(query, values)
            a.commit()
            print("se cargaron datos de la matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


    def alta_matriz(self,codigo,area,segmento,fila,nivel,disponibilidad):
        global area2
        area2=self.nombre_tabla(area)
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO %s (codigo,area,segmento,fila,nivel,disponibilidad) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (area2,codigo,area,segmento,fila,nivel,disponibilidad)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta a la posicion en la matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    

def ab_matriz(area,codigo):
    global area2
    area2=matriz.nombre_tabla(area)
    a=c.start_connection()
    cursor=a.cursor()
    try: 
        query = "UPDATE %s set disponibilidad= IF(disponibilidad = '0', disponibilidad + 1, disponibilidad-1) WHERE codigo=%s"
        values = (area2,codigo)
        cursor.execute(query, values)
        a.commit()
        print("se MODIFICO disponibilidad de posicion correctamente")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)


    def mostrar_datos_matriz():
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT area,segmento,filas,nivel FROM datosmatriz")
        cursor.execute(query)
        data = cursor.fetchall()
        a.commit()
        return data

    def modificar_matriz(self,area,segmento,filas,nivel):
        if self.filas<filas or self.nivel<nivel:
            self.importar_datos_matriz()
            if self.filas==filas:
                dif_filas=0
                self.filas=filas
            else :
                dif_filas=filas-self.filas
                self.filas=filas
            if self.nivel==nivel:
                dif_nivel=0
                self.nivel=nivel
            else :
                dif_nivel=nivel-self.nivel
                self.nivel=nivel
            a=c.start_connection()
            cursor=a.cursor()
            try:
                query = "UPDATE datosmatriz SET filas=%s where area=%s and segmento=%s"
                values = (self.filas,area,segmento)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE datosmatriz SET nivel=%s where area=%s and segmento=%s"
                values = (self.filas,area,segmento)
                cursor.execute(query, values)
                a.commit()
                print("se modificaron datos de la matriz correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)
            self.reajustar_matriz(area,segmento,dif_filas,dif_nivel)
            print("se agregaron posiciones correctamente")
        else:
            print("datos ingresados menores a la matriz actual")
            pass

    def reajustar_matriz(self,area,segmento,dif_filas,dif_nivel):
        global area2
        area2=self.nombre_tabla(area)
        if dif_filas != 0:
            np.insert(self.mz,self.mz.shape[0],np.arange(dif_filas))
        if dif_nivel !=0:
            np.insert(self.mz,self.mz.shape[1],np.arange(dif_nivel))
            i,j = 0,0
            while i<self.filas: 
                while j<self.nivel:
                    codigo=str(str(self.area)+"-"+str(self.segmento)+"-"+str(i)+"-"+str(j))
                    a=c.start_connection()
                    cursor=a.cursor()
                    try: 
                        query = "INSERT INTO %s(codigo,area,segmento,fila,nivel,disponibilidad) VALUES (%s,%s,%s,%s,%s,%s)"
                        values = (area2,codigo,segmento,i,j,1)
                        cursor.execute(query, values)
                        a.commit()
                        print("se dio alta a la posicion en la matriz correctamente")
                    except pymysql.err.OperationalError as err:
                        print("Hubo un error:", err)
                    c.close_connection(a)

                    j=j+1

                i=i+1
                j=0

        
    
    def buscar_matriz(param):
        global area2
        area2= matriz.nombre_tabla(area)
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM %s WHERE codigo=%s")
        cursor.execute(query, (area2,param))
        data = cursor.fetchall()
        a.commit()
        return data

    def buscar_matriz_rows(param):
        global area2
        area2= matriz.nombre_tabla(area)
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM matriz WHERE codigo=%s")
        data = cursor.execute(query, (param, param,param,param))
        a.commit()
        return data

    def mostrar_matriz(codigo,area):
        global area2
        area2= matriz.nombre_tabla(area)
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM %s WHERE codigo=%s")
        cursor.execute(query,area2,codigo)
        data = cursor.fetchall()
        a.commit()
        return data

    
    def listar_matriz(area):
        global area2
        area2= matriz.nombre_tabla(area)
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM %s"
            values= area2
            cursor.execute(query,values)
            productos = cursor.fetchall()

            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        print(productos)
        return productos

    def contar_filas_area(area):
        global area2
        area2= matriz.nombre_tabla(area)
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM %s"
        values= area2
        cursor.execute(query,values)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n








def asignacion_de_posicion():
    a=c.start_connection()
    cursor=a.cursor()
    try:
        query = "SELECT COUNT (*) FROM matriz where disponibilidad = 1"
        #values =
        cursor.execute(query)
        a.commit()
        n=int(cursor.fetchall())
        i=0
        while i<n:
            query = "SELECT codigo FROM matriz WHERE idmatriz = %s and disponibilidad = 1"
            values = i
            cursor.execute(query,values)
            a.commit()
            codigo=cursor.fetchall()
            codigo=str(codigo[0][0])
            if i==n-1 and codigo == "none":
                print("no hay espacios disponibles")
                pass
            else:
                query = "UPDATE matriz SET disponibilidad=0 WHERE codigo=%s"
                values = codigo
                cursor.execute(query,values)
                a.commit()
                return codigo

    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)
