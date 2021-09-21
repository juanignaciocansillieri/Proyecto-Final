

import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
#import alojamiento as aloj
import lotes
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c


class productos():
    def __init__(self, codigo, marca, cantidad, descripcion,ubicacion, fechalote, vencimiento,condicion,fragil,foto,peso,largo,ancho,alto):
        self.codigo = codigo
        self.marca = marca
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.ubicacion = ubicacion
        self.foto = foto
        self.fechalote = fechalote
        self.vencimiento = vencimiento
        self.condicion = condicion
        self.fragil = fragil
        self.peso= peso
        self.ancho= ancho
        self.largo= largo
        self.alto= alto
        print("se creo producto correctamente")

    def asignar_ubicacion(self):
        pass

    def alta_producto(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO productos (codigo, marca, descripcion,ubicacion,condicion,fragil,foto,peso,largo,ancho,alto) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (self.codigo, self.marca, self.descripcion, self.ubicacion, self.condicion, self.fragil,self.foto,self.peso,self.largo,self.ancho,self.alto)
            cursor.execute(query, values)
            a.commit()
            lotes.lote(self.codigo,self.cantidad,self.fechalote,self.vencimiento)
            print("se dio alta producto correctamente")

        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    
    def borrar_producto(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("DELETE from productos WHERE codigo =%s")
        cursor.execute(query, codigo)
        print("Se elimino producto correctamente")
        a.commit()


    def modificar_produc(codigov, codigon,marca,descripcion,ubicacion,condicion,fragil,foto,peso,largo,ancho,alto):
        a = c.start_connection()
        cursor = a.cursor()
        query = "SELECT idproductos FROM productos WHERE codigo=%s"
        values = codigov
        cursor.execute(query, values)
        a.commit()
        b = cursor.fetchall()
        idp = str(b[0][0])
        
        try:
            query = "UPDATE productos set codigo=%s WHERE idproductos=%s"
            values = (codigon, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set marca=%s WHERE idproductos=%s"
            values = (marca, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set descripcion=%s WHERE idproductos=%s"
            values = (descripcion, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set foto=%s WHERE idproductos=%s"
            values = (foto, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set condicion=%s WHERE idproductos=%s"
            values = (condicion, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set fragil=%s WHERE idproductos=%s"
            values = (fragil, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set ubicacion=%s WHERE idproductos=%s"
            values = (ubicacion, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set peso=%s WHERE idproductos=%s"
            values = (peso, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set largo=%s WHERE idproductos=%s"
            values = (largo, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set ancho=%s WHERE idproductos=%s"
            values = (ancho, idp)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set alto=%s WHERE idproductos=%s"
            values = (alto, idp)
            cursor.execute(query, values)
            a.commit()

            print("se MODIFICO producto correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


    def buscar_product(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT p.codigo,p.descripcion,p.marca,l.cantidad,l.vencimiento FROM productos p JOIN lote l ON p.codigo=l.idproducto WHERE codigo=%s or descripcion=%s or marca=%s or  cantidad=%s")
        cursor.execute(query, (param, param,param,param))
        data = cursor.fetchall()
        a.commit()
        return data

    def buscar_product_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT p.codigo,p.descripcion,p.marca,l.cantidad,l.vencimiento FROM productos p JOIN lote l ON p.codigo=l.idproducto WHERE codigo=%s or descripcion=%s or marca=%s or  cantidad=%s")
        data = cursor.execute(query, (param, param,param,param))
        a.commit()
        return data

    def mostrar_product(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT p.codigo, p.marca, l.cantidad, p.descripcion,p.ubicacion, l.fechalote, l.vencimiento,p.fragil,p.foto,p.peso,p.largo,p.ancho,p.alto FROM productos p JOIN lote l ON p.codigo = l.idproducto WHERE codigo=%s")
        cursor.execute(query,codigo)
        data = cursor.fetchall()
        a.commit()
        return data



def listar_prod():
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT p.codigo,p.descripcion,p.marca,l.cantidad,l.vencimiento FROM productos p JOIN lote l ON p.codigo=l.idproducto"
        cursor.execute(query)
        productos = cursor.fetchall()
        a.commit()
    except pymysql.err.OperationalError as err:
        productos = ""
        print("Hubo un error:", err)
    c.close_connection(a)
    return productos


def contar_filas():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM productos"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def ver_cod(codigo):
        a=c.start_connection()
        cursor=a.cursor()
        query = "SELECT COUNT(*) FROM productos"
        cursor.execute(query)
        a.commit()
        b = cursor.fetchall()
        b = str(b[0][0])
        n = int(b)
        i=0
        dni="(('"+codigo+"',),)"
        while i<n:
            query = "SELECT codigo FROM productos WHERE idproductos = %s"
            values=i
            cursor.execute(query,values)
            a.commit()
            b = cursor.fetchall()
            b = str(b)
            print (b)
            if b==dni:
                i=n+1
            else:               
                i+=1
        if i==n+1:
            c.close_connection(a)
            # existe
            return 1
        else: 
            c.close_connection(a)
            return 0
