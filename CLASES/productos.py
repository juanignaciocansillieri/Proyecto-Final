
import sys
from sys import setprofile
from typing import NoReturn
import pymysql
import os
#import alojamiento as aloj
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c


class productos:
    def __init__(self, codigo, nombre, marca, cantidad, descripcion, foto, lote, vencimiento, refrigeracion, inflamable, fragil):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.ubicacion = 1 #aloj.asignacion_de_ubicacion()
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
            a=c.start_connection()
            cursor=a.cursor()
            try:
                query = "INSERT INTO productos (codigo,nombre,marca,cantidad,descripcion,ubicacion,foto,lote,vencimiento,refrigeracion,inflamable,fragil) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (self.codigo,self.nombre,self.marca,self.cantidad,self.descripcion,self.ubicacion,self.foto,self.lote,self.vencimiento,self.refrigeracion,self.inflamable,self.fragil)
                cursor.execute(query, values)
                a.commit()
                print("se dio alta producto correctamente")
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            c.close_connection(a)

    def importar_datos_product(self,codigo):
            a=c.start_connection()
            cursor=a.cursor()
            if c.controlador(codigo,"productos","codigo") ==1:
                try:
                    self.codigo=codigo
                    query = "SELECT nombre FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.nombre=str(b[0][0]) 
                    query = "SELECT marca FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.marca=str(b[0][0]) 
                    query = "SELECT cantidad FROM productosWHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.cantidad=str(b[0][0]) 
                    query = "SELECT descripcion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.descripcion=str(b[0][0]) 
                    query = "SELECT foto FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.foto=str(b[0][0]) 
                    query = "SELECT lote FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.lote=str(b[0][0]) 
                    query = "SELECT vencimiemto FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.vencimiento=str(b[0][0]) 
                    query = "SELECT refrigeracion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.refrigeracion=str(b[0][0]) 
                    query = "SELECT inflamable FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.inflamable=str(b[0][0]) 
                    query = "SELECT fragil FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.fragil=str(b[0][0])
                    query = "SELECT ubicacion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    self.ubicacion=str(b[0][0])  
                    print("se importo producto correctamente")
                except pymysql.err.OperationalError as err:
                    print("Hubo un error:", err)
            c.close_connection(a)
            
    
    def mostrar_datos_product_importado(self):
        a=c.start_connection()
        cursor=a.cursor()
        #if c.controlador(codigo,"productos","codigo") ==1:
        #self.importar_datos_product(codigo) prefiero usar los 2 comandos por aparte
        try:
            query = "INSERT INTO productos (codigo,nombre,marca,cantidad,descripcion,ubicacion,foto,lote,vencimiento,refrigeracion,inflamable,fragil) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            values = (self.codigo, self.nombre, self.marca, self.cantidad, self.descripcion, self.ubicacion,
                      self.foto, self.lote, self.vencimiento, self.refrigeracion, self.inflamable, self.fragil)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta producto correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        #c.close_connection(a)
        return 0
    

    def mostrar_datos_producto(self,codigo):
        a=c.start_connection()
        cursor=a.cursor()
        if c.controlador(codigo,"productos","codigo") ==1:
        #self.importar_datos_product(codigo) prefiero usar los 2 comandos por aparte
            query= "SELECT nombre FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            nombre=str(b[0][0]) 
            query = "SELECT marca FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            marca=str(b[0][0]) 
            query = "SELECT cantidad FROM productosWHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            cantidad=str(b[0][0]) 
            query = "SELECT descripcion FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            descripcion=str(b[0][0]) 
            query = "SELECT foto FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            foto=str(b[0][0]) 
            query = "SELECT lote FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            lote=str(b[0][0]) 
            query = "SELECT vencimiemto FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            vencimiento=str(b[0][0]) 
            query = "SELECT refrigeracion FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            refrigeracion=str(b[0][0]) 
            query = "SELECT inflamable FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            inflamable=str(b[0][0]) 
            query = "SELECT fragil FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            fragil=str(b[0][0])
            query = "SELECT ubicacion FROM productos WHERE codigo=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            ubicacion=str(b[0][0])  
            try:
                if fragil=="1":
                    fragil="fragil"
                else:
                    fragil="no fragil"
                if refrigeracion=="1":
                    refrigeracion="refrigerado"
                else:
                    refrigeracion="no refrigerado"
                if inflamable=="1":
                    inflamable="inflamable"
                else:
                    inflamable="no inflamable"
                
                print("\ncodigo: ",codigo,"\nnombre: ",nombre,"\nmarca: ",marca,"\ncantidad: ",cantidad,"\ndescripcion: ",descripcion,"\nubicacion: ",ubicacion,"\nfoto: ",foto,"\nlote: ",lote,"\nvencimiento: ",vencimiento,"\nrefrigeracion: ",refrigeracion,"\ninflamable: ",inflamable,"\nfragil: ",fragil)
            except pymysql.err.OperationalError as err:
                print("Hubo un error:", err)
            #c.close_connection(a)
            return 0


    def importar_datos_product(self, codigo):
        a = c.start_connection()
        cursor = a.cursor()
        if c.controlador(codigo, "productos", "codigo") == 1:
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

    """def mostrar_datos_product(self, codigo):
        # a=c.start_connection()
        # cursor=a.cursor()
        # if c.controlador(codigo,"productos","codigo") ==1:
        self.importar_datos_product(codigo)
        try:
            if self.fragil == "1":
                self.fragil = "fragil"
            else:
                self.fragil = "no fragil"
            if self.refrigeracion == "1":
                self.refrigeracion = "refrigerado"
            else:
                self.refrigeracion = "no refrigerado"
            if self.inflamable == "1":
                self.inflamable = "inflamable"
            else:
                self.inflamable = "no inflamable"

            print("\ncodigo: ", self.codigo, "\nnombre: ", self.nombre, "\nmarca: ", self.marca, "\ncantidad: ", self.cantidad, "\ndescripcion: ", self.descripcion, "\nubicacion: ", self.ubicacion,
                  "\nfoto: ", self.foto, "\nlote: ", self.lote, "\nvencimiento: ", self.vencimiento, "\nrefrigeracion: ", self.refrigeracion, "\ninflamable: ", self.inflamable, "\nfragil: ", self.fragil)
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        # c.close_connection(a)
        return 0"""

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
        if c.controlador(codigo, "productos", "codigo") == 1:
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

    


    def buscar_productos(self,codigo):
        try:
            int(codigo)
            tf=True
        except ValueError:
            tf=False
        
        if tf== True:
            a=c.start_connection()
            cursor=a.cursor()
            if c.controlador(codigo,"productos","nombre") ==1:
                try:
                    codigo
                    query = "SELECT nombre FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    nombre=str(b[0][0]) 
                    query = "SELECT marca FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    marca=str(b[0][0]) 
                    query = "SELECT cantidad FROM productosWHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    cantidad=str(b[0][0]) 
                    query = "SELECT descripcion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    descripcion=str(b[0][0]) 
                    query = "SELECT foto FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    foto=str(b[0][0]) 
                    query = "SELECT lote FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    lote=str(b[0][0]) 
                    query = "SELECT vencimiemto FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    vencimiento=str(b[0][0]) 
                    query = "SELECT refrigeracion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    refrigeracion=str(b[0][0]) 
                    query = "SELECT inflamable FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    inflamable=str(b[0][0]) 
                    query = "SELECT fragil FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    fragil=str(b[0][0])
                    query = "SELECT ubicacion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    ubicacion=str(b[0][0])  
                except pymysql.err.OperationalError as err:
                    print("Hubo un error:", err)
            c.close_connection(a)
            self.mostrar_datos_producto(codigo,nombre,marca,cantidad,descripcion,ubicacion,foto,lote,vencimiento,refrigeracion,inflamable,fragil)

        else:
            a=c.start_connection()
            cursor=a.cursor()
            query = "SELECT codigo FROM productos WHERE nombre=%s"
            values = codigo
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            cadena=str(b[0][0])
            a=c.start_connection()
            cursor=a.cursor()
            if c.controlador(codigo,"productos","codigo") ==1:
                try:
                    codigo
                    query = "SELECT nombre FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    nombre=str(b[0][0]) 
                    query = "SELECT marca FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    marca=str(b[0][0]) 
                    query = "SELECT cantidad FROM productosWHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    cantidad=str(b[0][0]) 
                    query = "SELECT descripcion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    descripcion=str(b[0][0]) 
                    query = "SELECT foto FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    foto=str(b[0][0]) 
                    query = "SELECT lote FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    lote=str(b[0][0]) 
                    query = "SELECT vencimiemto FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    vencimiento=str(b[0][0]) 
                    query = "SELECT refrigeracion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    refrigeracion=str(b[0][0]) 
                    query = "SELECT inflamable FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    inflamable=str(b[0][0]) 
                    query = "SELECT fragil FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    fragil=str(b[0][0])
                    query = "SELECT ubicacion FROM productos WHERE codigo=%s"
                    values = codigo
                    cursor.execute(query, values)
                    a.commit()
                    b=cursor.fetchall() 
                    ubicacion=str(b[0][0])  
                except pymysql.err.OperationalError as err:
                    print("Hubo un error:", err)
            c.close_connection(a)
            self.mostrar_datos_producto(codigo,nombre,marca,cantidad,descripcion,ubicacion,foto,lote,vencimiento,refrigeracion,inflamable,fragil)

def listar_prod2():
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

def listar_prod(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT COUNT (*) FROM productos"
            # values =
            cursor.execute(query)
            a.commit()
            n = int(cursor.fetchall())
            i = 0
            ii = 0
            while i < n:
                query = "SELECT codigo FROM productos WHERE idproductos = %s"
                values = i
                cursor.execute(query, values)
                a.commit()
                codigo = cursor.fetchall()
                codigo = str(codigo[0][0])
                self.mostrar_datos_product(codigo)
                i=i+1
                """if self.mostrar_datos_product(codigo) != NoReturn:
                    ii = ii+1
                else:
                    i = i+1"""
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)




                                                           
