import sys
from sys import setprofile
from typing import NoReturn, ValuesView
import pymysql
import os
sys.path.append("C:\proyecto-final\DB")
import conexion as c

class movimientos:    
    def __init__(self,tipo,codigo,cantidad,motivo,fecha):
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
            query = "INSERT INTO movimientos(tipo,codigo,cantidad,motivo,fecha) VALUES (%s,%s,%s,%s,%s)"
            values = (self.tipo,self.codigo,self.cantidad,self.motivo,self.fecha)
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
                query = "SELECT tipo,codigo,cantidad,motivo,fecha FROM movimientos"
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
        query = ("SELECT tipo,codigo,cantidad,motivo,fecha FROM movimientos WHERE codigo=%s and fecha=%s")
        values=(codigo,fecha)
        cursor.execute(query,values)
        data = cursor.fetchall()
        a.commit()
        return data