import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
import numpy as np
import matriz as mz
import area as ar
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c

class alojamiento:
    def __init__(self,largo,ancho,alto,area,pasillo,segmento,filas,nivel,limite,columna):
        self.columna = columna
        self.largo=largo
        self.ancho=ancho
        self.alto=alto
        self.area=area
        self.segmento=segmento
        self.filas=filas
        self.columna=columna
        self.nivel=nivel
        self.volumen=self.largo*self.ancho*self.alto
        self.disponibilidad=0 #0 disponible 1 tiene algo 2 esta lleno
        iden=ar.Area.mostrar_identificador(area)
        iden=str(iden[0][0])
        self.posicion=str(str(iden)+"-"+str(pasillo)+"-"+str(self.segmento)+"-"+str(filas)+"-"+str(columna)+"-"+str(nivel))
        self.pasillo=pasillo
        self.limite=limite
        self.codigo= str(str(iden)+"-"+str(pasillo)+"-"+str(self.segmento)+"-"+str(filas)+"-"+str(columna)+"-"+str(nivel))
        self.alta_alojamiento()
        print("se creo alojamiento correctamente")


    def alta_alojamiento(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO alojamiento(codigo,largo,ancho,alto,volumen,disponibilidad,posicion,pasillo,limite,columna) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (self.codigo,self.largo,self.ancho,self.alto,self.volumen,self.disponibilidad,self.posicion,self.pasillo,self.limite,self.columna)
            cursor.execute(query, values)
            a.commit()
            mz.ab_matriz(self.area,self.codigo)
            print("se dio alta alojamiento correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
    
    def ab_alojamiento(self,codigo):
        a=c.start_connection()
        cursor=a.cursor()
        try: 
            query = "UPDATE alojaminto set disponibilidad= IF(disponibilidad = '0', disponibilidad + 1, disponibilidad-1) WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO alojamiento correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


        
    def modificar_alojamiento(self,codigo,largo,ancho,alto,disponibilidad,posicion,pasillo,limite,columna):
            a=c.start_connection()
            cursor=a.cursor()
            try:
                query = "UPDATE alojamiento set largo=%s WHERE codigo=%s"
                values = (largo,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set ancho=%s WHERE codigo=%s"
                values = (ancho,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set alto=%s WHERE codigo=%s"
                values = (alto,codigo)
                cursor.execute(query, values)
                a.commit()
                volumen=largo*ancho*alto
                query = "UPDATE alojamiento set volumen=%s WHERE codigo=%s"
                values = (volumen,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set disponibilidad=%s WHERE codigo=%s"
                values = (disponibilidad,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set posicion=%s WHERE codigo=%s"
                values = (posicion,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set pasillo=%s WHERE codigo=%s"
                values = (pasillo,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set limite=%s WHERE codigo=%s"
                values = (limite,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set columna=%s WHERE codigo=%s"
                values = (columna,codigo)
                cursor.execute(query, values)
                a.commit()
                print("se MODIFICO alojamiento correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)



    def buscar_aloj(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,largo,ancho,alto,volumen,pasillo,segmento,disponibilidad,posicion,limite,columna FROM alojamiento WHERE codigo=%s")
        cursor.execute(query, (param, param,param,param))
        data = cursor.fetchall()
        a.commit()
        return data

    def buscar_aloj_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,largo,ancho,alto,volumen,pasillo,segmento,disponibilidad,posicion,limite,columna FROM alojamiento WHERE codigo=%s")
        data = cursor.execute(query, param)
        a.commit()
        return data

    def mostrar_aloj(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,largo,ancho,alto,volumen,pasillo,alojamiento,disponibilidad,posicion,limite,columna FROM alojamiento WHERE codigo=%s")
        cursor.execute(query,codigo)
        data = cursor.fetchall()
        a.commit()
        return data

    
    def listar_alojamiento():
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT codigo,largo,ancho,alto,volumen,pasillo,alojamiento,disponibilidad,posicion,limite,columna FROM alojamiento"
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
        query = "SELECT COUNT(*) FROM alojamiento"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

    def listar_alojamiento_disponibles_area(area):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT codigo,largo,ancho,alto,volumen,pasillo,alojamiento,disponibilidad,posicion,limite FROM alojamiento WHERE disponibilidad=0 and area=%s"
            cursor.execute(query,area)
            productos = cursor.fetchall()

            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        print(productos)
        return productos

    def contar_filas_disponibles_area(area):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM alojamiento where disponibilidad=0 and area=%s"
        cursor.execute(query,area)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

def ver_codigo(codigo):
        a=c.start_connection()
        cursor=a.cursor()
        query = "SELECT COUNT(*) FROM alojamiento"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        i=0
        codigo="(('"+codigo+"',),)"
        while i<n:
            query = "SELECT codigo FROM alojamiento WHERE idalojamiento = %s"
            values=i
            cursor.execute(query,values)
            a.commit()
            b = cursor.fetchall()
            b = str(b)
            print (b)
            if b==codigo:
                i=n+1
            else:               
                i+=1
        if i==n+1:
            c.close_connection(a)
            #codigo existe
            return 1
        else: 
            c.close_connection(a)
            return 0


"""
def asignacion_de_ubicacion():
    a=c.start_connection()
    cursor=a.cursor()
    try:
        query = "SELECT COUNT (*) FROM alojamiento where disponibilidad = %s"
        values = 1
        cursor.execute(query,values)
        a.commit()
        n=int(cursor.fetchall())
        i=0
        ii=0
        while i<n:
            query = "SELECT codigo FROM alojamiento WHERE idmatriz = %s and disponibilidad = 1"
            values = ii
            cursor.execute(query,values)
            a.commit()
            codigo=cursor.fetchall()
            codigo=str(codigo[0][0])
            if i==n-1 and codigo == "none":
                print("no hay alojamiento disponibles")
                pass
            else: 
                query = "UPDATE alojamiento SET disponibilidad=0 WHERE codigo=%s"
                values = codigo
                cursor.execute(query,values)
                a.commit()
                return codigo        
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    c.close_connection(a)
        """