from DB.conexion import contar_filas_tabla
from CLASES.productos import contar_filas
from _typeshed import Self
import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c

class lote:
    
    def __init__(self,idproducto,cantidad,fechalote,vencimiento):
        self.idproducto=idproducto
        self.cantidad=cantidad
        self.fechalote=fechalote
        self.vencimiento=vencimiento
        print("se creo lote correctamente")
        self.alta_lote()


    def alta_lote(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO lote(idproducto,cantidad,fechalote,vencimiento) VALUES (%s,%s,%s,%s)"
            values = (self.idproducto,self.cantidad,self.fechalote,self.vencimiento)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta al lote correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def eliminar_lote(fechalote,idproducto):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "DELETE FROM lote WHERE idproducto=%s and fechalote=%s"
            values = (idproducto,fechalote)
            cursor.execute(query, values)
            a.commit()
            print("se elimino lote correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_cantidad(idproducto,fechalote,cantidad):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "UPDATE lote set cantidad=%s WHERE idproducto=%s and fechalote=%s"
            values = (cantidad,idproducto,fechalote)
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

    def contar_filas_producto(idproducto):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT COUNT(*) FROM lote WHERE idproducto=%s"
        values=idproducto
        cursor.execute(query,values)
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
                query = "SELECT idproducto,cantidad,fechalote,vencimiento FROM lote WHERE idproducto=%s"
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
        query = ("SELECT idproducto,cantidad,fechalote,vencimiento FROM lote WHERE idproducto=%s")
        cursor.execute(query,idproducto)
        data = cursor.fetchall()
        a.commit()
        return data

    def obtener_cantidades(idproducto):
        cantidad=0
        n=lote.contar_filas_producto(idproducto)
        i=0
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT idlote FROM lote WHERE idproducto=%s ORDER BY cantidad")
        cursor.execute(query,idproducto)
        idlote=cursor.fetchall()
        a.commit()

        while i<n:
            query = ("SELECT cantidad FROM lote WHERE idlote=%s")
            cursor.execute(query,idlote)
            data = cursor.fetchall()
            cantidad=cantidad+data
            a.commit()
            idlote=idlote+1
            i=i+1

        return cantidad

    def fifo(idproducto,cantidad):
        cantidad=0
        n=lote.contar_filas_producto(idproducto)
        i=0
        j=0
        k=0
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT idlote FROM lote WHERE idproducto=%s ORDER BY cantidad")
        cursor.execute(query,idproducto)
        idlote=cursor.fetchall()
        a.commit()

        while i<n:
            query = ("SELECT cantidad FROM lote WHERE idlote=%s ORDER BY vencimiento")
            cursor.execute(query,idproducto)
            data=cursor.fetchall()
            a.commit()
            if data<cantidad:
                query = "UPDATE lote set cantidad=0 WHERE idproducto=%s and cantidad=%s"
                values = (idproducto,data)
                cursor.execute(query, values)
                a.commit()
                cantidad=cantidad-data
                idlote=idlote+1
                i=i+1
            else:
                data2=data-cantidad
                query = "UPDATE lote set cantidad=%s WHERE idproducto=%s and cantidad=%s"
                values = (data2,idproducto,data)
                cursor.execute(query, values)
                a.commit()
                cantidad=cantidad-data
                idlote=idlote+1
                i=n

