from sys import setprofile
import pymysql
import os
from DB import conexion as c
import numpy as np

class alojamiento:
    def __init__(self,dimensiones,refrigeracion,limite):
        #self.codigo=#autogeneracion de codigo
        self.dimensiones=dimensiones
        self.disponibilidad=1
        self.posicion=self.generacion_posicion
        self.refrigeracion=refrigeracion
        self.limite=limite
        print("se creo alojamiento correctamente")

    def generacion_codigo(self):
        pass

    def generacion_posicion(self):
        posicion=self.codigo.split()
        posicion="pasillo: ",posicion[0],", fila: ",posicion[1],", altura: ",posicion[2]
        posicion=str(posicion)
        return posicion


    def alta_alojamiento(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO alojamiento(codigo,dimensiones,disponibilidad,posicion,refrigeracion,limite) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (self.codigo,self.dimensiones,self.disponibilidad,self.posicion,self.refrigeracion,self.limite)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta alojamiento correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
    
    def ab_alojamiento(self,codigo):
        a=c.start_connection()
        cursor=a.cursor()
        if c.controlador(codigo,"alojamiento","codigo") == 1:
            try: 
                query = "UPDATE alojaminto set disponibilidad= IF(disponibilidad = '0', disponibilidad + 1, disponibilidad-1) WHERE codigo=%s"
                values = codigo
                cursor.execute(query, values)
                a.commit()
                print("se MODIFICO alojamiento correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
        c.close_connection(a)

    def importar_datos_alojamiento(self,codigo):
            a=c.start_connection()
            cursor=a.cursor()
            if c.controlador(codigo,"alojaminto","codigo") ==1:
                try:
                    self.codigo=codigo
                    query = "SELECT dimensiones FROM alojamiento WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.nombre=str(b[0][0]) 
                    query = "SELECT disponibilidad FROM alojamiento WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.marca=str(b[0][0]) 
                    query = "SELECT posicion FROM alojamiento WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.cantidad=str(b[0][0]) 
                    query = "SELECT refrijeracion FROM alojamiento WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.descripcion=str(b[0][0]) 
                    query = "SELECT limite FROM alojamiento WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.foto=str(b[0][0]) 
                    print("se importo alojamiento correctamente")
                except pymysql.err.OperationalError as err:
                    print("Hubo un error:", err)
            c.close_connection(a)

    def mostrar_datos_alojamiento(self,codigo):
        #a=c.start_connection()
        #cursor=a.cursor()
        self.importar_datos_alojamiento(codigo)
        try:
            if self.disponibilidad=="1":
                self.disponibilidad="disponible"
            else:
                self.disponibilidad="no disponible"
            if self.refrigeracion=="1":
                self.refrigeracion="refrigerado"
            else:
                self.refrigeracion="no refrigerado"
            print("\ncodigo: ",self.codigo,"\ndimensiones: ",self.dimensiones,"\nsiponibilidad: ",self.disponibilidad,"\nposicion: ",self.posicion,"\nrefrigeracion: ",self.refrigeracion,"\nlimite: ",self.limite)
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        #c.close_connection(a)
        return 0
        
    def modificar_alojamiento(self,codigo,dimensiones,refrigeracion,limite):
            a=c.start_connection()
            cursor=a.cursor()
            try:
                query = "UPDATE alojamiento set dimensiones=%s WHERE codigo=%s"
                values = (dimensiones,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set refrigeracion=%s WHERE codigo=%s"
                values = (refrigeracion,codigo)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE alojamiento set limite=%s WHERE codigo=%s"
                values = (limite,codigo)
                cursor.execute(query, values)
                a.commit()
                print("se MODIFICO alojamiento correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)

    def listar_alojamiento(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "SELECT COUNT (*) FROM alojamiento"
            #values =
            cursor.execute(query)
            a.commit()
            n=int(cursor.fetchall())
            i=0
            ii=0
            while i<n:
                query = "SELECT codigo FROM productos WHERE idproductos = %s"
                values = ii
                cursor.execute(query,values)
                a.commit()
                codigo=cursor.fetchall()
                codigo=str(codigo[0][0])
                if self.mostrar_datos_alojamiento(codigo) != pymysql.NULL:
                    ii=ii+1
                else:
                    i=i+1
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        