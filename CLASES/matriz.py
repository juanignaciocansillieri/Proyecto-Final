from sys import setprofile
from typing import NoReturn
import pymysql
import os
from DB import conexion as c
import numpy as np

class matriz:
    def __init__(self,filas,columnas,altura):
        self.filas=filas
        self.columnas=columnas
        self.altura=altura
        self.mz=self.crear_matriz()
        self.alta_datos_matriz()

        print("se creo matriz correctamente")
        

    def formar_matriz(self): #esta se usa cuantas veces se requiera formar la matriz
        self.importar_datos_matriz()
        mz=np.zeros((self.filas,self.columnas,self.altura)) #acá creo la matriz
        i,j,k = 0,0,0
        while i<self.filas: #acá le doy altura
            while j<self.columnas:
                while k<self.altura:
                    codigo=str(str(i)+str(j)+str(k))
                    a=c.start_connection()
                    cursor=a.cursor()
                    try: 
                        query = "UPDATE matriz set codigo=%s WHERE fila=%s and columna=%s and altura=%s"
                        values = (codigo,i,j,k)
                        cursor.execute(query, values)
                        a.commit()
                    except pymysql.err.OperationalError as err:
                        print("Hubo un error:", err)
                    c.close_connection(a)
                    k=k+1
                j=j+1
                k=0
            i=i+1
            j=0
        print("se formo la matriz correctamente")
        return mz

    def crear_matriz(self): #IMPORTANTE ejecutar una sola vez
        mz=np.zeros((self.filas,self.columnas,self.altura)) #acá creo la matriz
        i,j,k = 0,0,0
        while i<self.filas:
            while j<self.columnas:
                while k<self.altura:
                    codigo=str(str(i)+str(j)+str(k))
                    self.alta_matriz(codigo,i,j,k)
                    print(i,j,k)
                    k=k+1  
                j=j+1
                k=0
            i=i+1
            j=0
        
        print("se dio de alta a la matriz correctamente")
        return mz
        
    

    def alta_datos_matriz(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO datosmatriz(filas,columnas,altura) VALUES (%s,%s,%s)"
            values = (self.filas,self.columnas,self.altura)
            cursor.execute(query, values)
            a.commit()
            print("se cargaron datos de la matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def alta_matriz(self,codigo,fila,columna,altura):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO matriz(codigo,fila,columna,altura,disponibilidad) VALUES (%s,%s,%s,%s,%s)"
            values = (codigo,fila,columna,altura,1)
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

    def importar_datos_matriz(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "SELECT filas FROM datosmatriz"
            cursor.execute(query)
            a.commit()
            b=cursor.fetchall() 
            self.filas=int(b[0][0]) 
            query = "SELECT columnas FROM matriz"
            cursor.execute(query)
            a.commit()
            b=cursor.fetchall() 
            self.columnas=int(b[0][0])      
            query = "SELECT altura FROM matriz WHERE codigo=%s"
            cursor.execute(query)
            a.commit()
            b=cursor.fetchall() 
            self.altura=int(b[0][0])       
            self.mz=self.formar_matriz()
            print("se importo posicion de matriz correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_matriz(self,filas,columnas,altura):
        if self.filas<filas or self.columnas<columnas or self.altura<altura:
            self.importar_datos_matriz()
            if self.filas==filas:
                dif_filas=0
                self.filas=filas
            else :
                dif_filas=filas-self.filas
                self.filas=filas
            if self.columnas==columnas:
                dif_columnas=0
                self.columnas=columnas
            else :
                dif_columnas=columnas-self.columnas
                self.columnas=columnas
            if self.altura==altura:
                dif_altura=0
                self.altura=altura
            else :
                dif_filas=altura-self.altura
                self.altura=altura
            a=c.start_connection()
            cursor=a.cursor()
            try:
                query = "UPDATE datosmatriz SET filas=%s"
                values = (self.filas)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE datosmatriz SET columnas=%s"
                values = (self.filas)
                cursor.execute(query, values)
                a.commit()
                query = "UPDATE datosmatriz SET altura=%s"
                values = (self.filas)
                cursor.execute(query, values)
                a.commit()
                print("se modificaron datos de la matriz correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)
            self.reajustar_matriz(dif_filas,dif_columnas,dif_altura)
            print("se agregaron posiciones correctamente")
        else:
            print("datos ingresados menores a la matriz actual")
            pass

    def reajustar_matriz(self,dif_filas,dif_columnas,dif_altura):
        if dif_filas != 0:
            np.insert(self.mz,self.mz.shape[0],np.arange(dif_filas))
        if dif_columnas !=0:
            np.insert(self.mz,self.mz.shape[1],np.arange(dif_columnas))
        if dif_altura!=0:
            np.insert(self.mz,self.mz.shape[2],np.arange(dif_altura))
            i,j,k = 0,0,0
            while i<self.filas: 
                while j<self.columnas:
                    while k<self.altura:
                        codigo=str(str(i)+str(j)+str(k))
                        a=c.start_connection()
                        cursor=a.cursor()
                        try: 
                            query = "INSERT INTO matriz(codigo,fila,altura,columna,disponibilidad) VALUES (%s,%s,%s,%s,%s)"
                            values = (codigo,i,j,k,1)
                            cursor.execute(query, values)
                            a.commit()
                            print("se dio alta a la posicion en la matriz correctamente")
                        except pymysql.err.OperationalError as err:
                            print("Hubo un error:", err)
                        c.close_connection(a)
                        k=k+1
                    j=j+1
                    k=0
                i=i+1
                j=0

    def mostrar_datos_ubicaciones(self,codigo):
        self.importar_datos_alojamiento(codigo)
        try:
            
            
            a=c.start_connection()
            cursor=a.cursor()
            if c.controlador(codigo,"matriz","codigo") ==1:
                query = "SELECT codigo FROM matriz WHERE codigo=%s"
                values = codigo
                cursor.execute(query, values)
                a.commit()
                b=cursor.fetchall() 
                codigo=str(b[0][0]) 
                query = "SELECT fila FROM matriz WHERE codigo=%s"
                values = codigo
                cursor.execute(query, values)
                a.commit()
                b=cursor.fetchall() 
                fila=str(b[0][0])
                query = "SELECT fila FROM matriz WHERE codigo=%s"
                values = codigo
                cursor.execute(query, values)
                a.commit()
                b=cursor.fetchall() 
                columna=str(b[0][0])
                query = "SELECT fila FROM matriz WHERE codigo=%s"
                values = codigo
                cursor.execute(query, values)
                a.commit()
                b=cursor.fetchall() 
                altura=str(b[0][0])
                query = "SELECT fila FROM matriz WHERE codigo=%s"
                values = codigo
                cursor.execute(query, values)
                a.commit()
                b=cursor.fetchall() 
                disponibilidad=str(b[0][0])
                if disponibilidad=="1":
                    disponibilidad="disponible"
                else:
                    disponibilidad="no disponible"



            print("\ncodigo: ",self.codigo,"\nfila: ",fila,"\ncolumna: ",columna,"\naltura: ",altura,"\ndisponibilidad: ",disponibilidad)
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        #c.close_connection(a)
        return 0
        
    def listar_matriz(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "SELECT COUNT (*) FROM matriz"
            #values =
            cursor.execute(query)
            a.commit()
            n=int(cursor.fetchall())
            i=0
            ii=0
            while i<n:
                query = "SELECT codigo FROM matriz WHERE idproductos = %s"
                values = ii
                cursor.execute(query,values)
                a.commit()
                codigo=cursor.fetchall()
                codigo=str(codigo[0][0])
                if self.mostrar_datos_matriz(codigo) != pymysql.NULL:
                    ii=ii+1
                else:
                    i=i+1
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)








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