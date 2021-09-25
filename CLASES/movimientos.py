import sys
from sys import setprofile
from typing import NoReturn, ValuesView
import pymysql
import os
sys.path.append("C:\proyecto-final\DB")
import conexion as c

<<<<<<< HEAD:CLASES/movimientos.py
class movimientos:    
    def __init__(self,tipo,codigo,cantidad,motivo,fecha):
=======
class movimientos:
    
    def __init__(self,tipo,codigo,cantidad,descripcion,fecha):
>>>>>>> 3afa557d8b694e05765872b73a184115193a340a:CLASES/moviminetos.py
        self.tipo=tipo
        self.codigo=codigo
        self.cantidad=cantidad
        self.motivo=motivo
        self.fecha=fecha

        print("se creo movimientos correctamente")
        self.alta_movimientos()


    def alta_movimientos(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
<<<<<<< HEAD:CLASES/movimientos.py
            query = "INSERT INTO movimientos(tipo,codigo,cantidad,motivo,fecha) VALUES (%s,%s,%s,%s,%s)"
            values = (self.tipo,self.codigo,self.cantidad,self.motivo,self.fecha)
=======
            query = "INSERT INTO movimientos(tipo,codigo,cantidad,descripcion,fecha) VALUES (%s,%s,%s,%s,%s)"
            values = (self.tipo,self.codigo,self.cantidad,self.descripcion,self.fecha)
>>>>>>> 3afa557d8b694e05765872b73a184115193a340a:CLASES/moviminetos.py
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al movimientos correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)



    def eliminar_movimientos(codigo,fecha):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "DELETE FROM movimientos WHERE codigo=%s and fecha=%s"
            values = (codigo,fecha)
            cursor.execute(query, values)
            a.commit()
            print("se elimino movimientos correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def contar_filas():
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM movimientos"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n
def listar_movimientos():
            a = c.start_connection()
            cursor = a.cursor()
            try:
<<<<<<< HEAD:CLASES/movimientos.py
                query = "SELECT tipo,codigo,cantidad,motivo,fecha FROM movimientos"
=======
                query = "SELECT tipo,codigo,cantidad,descripcion,fecha FROM movimientos"
>>>>>>> 3afa557d8b694e05765872b73a184115193a340a:CLASES/moviminetos.py
                cursor.execute(query)
                area = cursor.fetchall()
                a.commit()
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)
            return area

def mostrar_movimientos(codigo,fecha):
        a = c.start_connection()
        cursor = a.cursor()
<<<<<<< HEAD:CLASES/movimientos.py
        query = ("SELECT tipo,codigo,cantidad,motivo,fecha FROM movimientos WHERE codigo=%s and fecha=%s")
=======
        query = ("SELECT tipo,codigo,cantidad,descripcion,fecha FROM movimientos WHERE codigo=%s and fecha=%s")
>>>>>>> 3afa557d8b694e05765872b73a184115193a340a:CLASES/moviminetos.py
        values=(codigo,fecha)
        cursor.execute(query,values)
        data = cursor.fetchall()
        a.commit()
        return data