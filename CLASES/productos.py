

import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
#import alojamiento as aloj
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c


class productos():
    def __init__(self, codigo, nombre, marca, cantidad, descripcion, foto, lote, vencimiento, refrigeracion, inflamable, fragil):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.ubicacion = 1  # aloj.asignacion_de_ubicacion()
        self.foto = foto
        self.lote = lote
        self.vencimiento = vencimiento
        self.refrigeracion = refrigeracion
        self.inflamable = inflamable
        self.fragil = fragil
        print("se creo producto correctamente")

    def asignar_ubicacion(self):
        pass

    def alta_producto(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "INSERT INTO productos (codigo,nombre,marca,cantidad,descripcion,ubicacion,foto,lote,vencimiento,refrigeracion,inflamable,fragil) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (self.codigo, self.nombre, self.marca, self.cantidad, self.descripcion, self.ubicacion,
                      self.foto, self.lote, self.vencimiento, self.refrigeracion, self.inflamable, self.fragil)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta producto correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


    def importar_datos_product(self, codigo):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            self.codigo = codigo
            query = "SELECT nombre FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.nombre = str(b[0][0])
            query = "SELECT marca FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.marca = str(b[0][0])
            query = "SELECT cantidad FROM productosWHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.cantidad = str(b[0][0])
            query = "SELECT descripcion FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.descripcion = str(b[0][0])
            query = "SELECT foto FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.foto = str(b[0][0])
            query = "SELECT lote FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.lote = str(b[0][0])
            query = "SELECT vencimiemto FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            query = "SELECT refrigeracion FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.refrigeracion = str(b[0][0])
            query = "SELECT inflamable FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.inflamable = str(b[0][0])
            query = "SELECT fragil FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.fragil = str(b[0][0])
            query = "SELECT ubicacion FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b = cursor.fetchall()
            self.ubicacion = str(b[0][0])
            print("se importo producto correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)


    def modificar_produc(self, codigo, nombre, marca, cantidad, descripcion, foto, lote, vencimiento, refrigeracion, inflamable, fragil):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "UPDATE productos set codigo=%s WHERE codigo=%s"
            values = (codigo, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set nombre=%s WHERE codigo=%s"
            values = (nombre, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set marca=%s WHERE codigo=%s"
            values = (marca, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set cantidad=%s WHERE codigo=%s"
            values = (cantidad, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set descripcion=%s WHERE codigo=%s"
            values = (descripcion, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set foto=%s WHERE codigo=%s"
            values = (foto, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set lote=%s WHERE codigo=%s"
            values = (lote, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set vemcimiemto=%s WHERE codigo=%s"
            values = (vencimiento, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set refrigeracion=%s WHERE codigo=%s"
            values = (refrigeracion, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set inflamable=%s WHERE codigo=%s"
            values = (inflamable, self.codigo)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE productos set fragil=%s WHERE codigo=%s"
            values = (fragil, self.codigo)
            cursor.execute(query, values)
            a.commit()

            print("se MODIFICO producto correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def agregar_cantidad(self, codigo):
        a = c.start_connection()
        cursor = a.cursor()
        cantidad = input("Ingrese la nueva cantidad: ")
        try:
            query = "UPDATE productos set cantidad=%s WHERE codigo=%s"
            values = (cantidad, codigo)
            cursor.execute(query, values)
            a.commit()

            print("se MODIFICO producto correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def buscar_product(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,nombre,marca,cantidad,vencimiento FROM productos WHERE codigo=%s or nombre=%s or marca=%s or  cantidad=%s")
        cursor.execute(query, (param, param,param,param))
        data = cursor.fetchall()
        a.commit()
        return data

    def buscar_product_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,nombre,marca,cantidad,vencimiento FROM productos WHERE codigo=%s or nombre=%s or marca=%s or  cantidad=%s")
        data = cursor.execute(query, (param, param,param,param))
        a.commit()
        return data

    def mostrar_product(codigo):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT codigo,nombre,marca,cantidad,vencimiento,descripcion,ubicacion,foto,lote,refrigeracion,inflamable,fragil FROM productos WHERE codigo=%s")
        cursor.execute(query,codigo)
        data = cursor.fetchall()
        a.commit()
        return data



def listar_prod():
    a = c.start_connection()
    cursor = a.cursor()
    try:
        query = "SELECT codigo,nombre,marca,cantidad,vencimiento FROM productos"
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
    query = "SELECT COUNT(*) FROM productos"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n
