import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c
import numpy as np

class matriz:
    def __init__(self,area,segmento,filas,nivel):
        self.area=area
        self.codigo
        self.segmento=segmento
        self.filas=filas
        self.nivel=nivel
        self.disponibilidad=1

        print("se creo matriz correctamente")
        

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

                codigo=str(str(self.area)+str(self.segmento)+str(i)+str(j))
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
            query = "INSERT INTO datosmatriz(codigo,filas,nivel) VALUES (%s,%s,%s)"
            values = (codigo,self.filas,self.columnas)
            cursor.execute(query, values)
            a.commit()
            print("se cargaron datos de la matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    """def alta_datos_matriz_area(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO datosmatrizarea(columnas,altura) VALUES (%s,%s)"
            values = (self.filas,self.columnas)
            cursor.execute(query, values)
            a.commit()
            print("se cargaron datos de la matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)"""

    def alta_matriz(self,codigo,area,segmento,fila,nivel,disponibilidad):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO matriz(codigo,area,segmento,fila,nivel,disponibilidad) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (codigo,area,segmento,fila,nivel,disponibilidad)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta a la posicion en la matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    

    def ab_matriz(self,codigo):
        a=c.start_connection()
        cursor=a.cursor()
        try: 
            query = "UPDATE matriz set disponibilidad= IF(disponibilidad = '0', disponibilidad + 1, disponibilidad-1) WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO disponibilidad de posicion correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


    def mostrar_datos_matriz():
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT filas,columnas,altura FROM datosmatriz")
        cursor.execute(query)
        data = cursor.fetchall()
        a.commit()
        return data

    def modificar_matriz(self,filas,nivel):
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
                query = "UPDATE datosmatriz SET filas=%s"
                values = (self.filas)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE datosmatriz SET nivel=%s"
                values = (self.filas)
                cursor.execute(query, values)
                a.commit()
                print("se modificaron datos de la matriz correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)
            self.reajustar_matriz(dif_filas,dif_nivel)
            print("se agregaron posiciones correctamente")
        else:
            print("datos ingresados menores a la matriz actual")
            pass

    def reajustar_matriz(self,dif_filas,dif_nivel):
        if dif_filas != 0:
            np.insert(self.mz,self.mz.shape[0],np.arange(dif_filas))
        if dif_nivel !=0:
            np.insert(self.mz,self.mz.shape[1],np.arange(dif_nivel))
            i,j = 0,0
            while i<self.filas: 
                while j<self.nivel:
                    codigo=str(str(i)+str(j)+str(k))
                    a=c.start_connection()
                    cursor=a.cursor()
                    try: 
                        query = "INSERT INTO matriz(codigo,area,segmento,fila,nivel,disponibilidad) VALUES (%s,%s,%s,%s,%s,%s)"
                        values = (codigo,i,j,k,1)
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
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM matriz WHERE codigo=%s")
        cursor.execute(query, (param, param,param,param))
        data = cursor.fetchall()
        a.commit()
        return data

    def buscar_matriz_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM matriz WHERE codigo=%s")
        data = cursor.execute(query, (param, param,param,param))
        a.commit()
        return data

    def mostrar_matriz(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM matriz WHERE codigo=%s")
        cursor.execute(query,codigo)
        data = cursor.fetchall()
        a.commit()
        return data

    
    def listar_matriz():
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT codigo,area,segmento,fila,nivel,disponibilidad FROM matriz"
            cursor.execute(query)
            productos = cursor.fetchall()

            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        print(productos)
        return productos

    def contar_filas():
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM matriz"
        cursor.execute(query)
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
