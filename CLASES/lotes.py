import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c

class lote:
    
    def __init__(self,nlote,idproducto,vencimiento):
        self.nlote=nlote
        self.idproducto=idproducto
        self.vencimiento=vencimiento
        print("se creo lote correctamente")
        self.alta_lote()


    def alta_lote(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO lote(nlote,idproducto,vencimiento) VALUES (%s,%s,%s)"
            values = (self.nlote,self.idproducto,self.vencimiento)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al lote correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def eliminar_lote(nlote,idproducto):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "DELETE FROM lote WHERE idproducto=%s and nlote=%s"
            values = (idproducto,nlote)
            cursor.execute(query, values)
            a.commit()
            print("se elimino lote correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def contar_filas():
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM lote"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        c.close_connection(a)
        return n

    def listar_lote(idproducto):
            a = c.start_connection()
            cursor = a.cursor()
            try:
                query = "SELECT nlote,vencimiento FROM lote WHERE idproducto=%s"
                values=idproducto
                cursor.execute(query,values)
                area = cursor.fetchall()
                a.commit()
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)
            return area

    def mostrar_lote(idproducto):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT nlote,vencimiento FROM lote WHERE idproducto=%s")
        cursor.execute(query,idproducto)
        data = cursor.fetchall()
        a.commit()
        return data