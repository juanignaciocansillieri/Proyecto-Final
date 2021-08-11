from sys import setprofile
from typing import NoReturn
import pymysql
import os
from DB import conexion as c


class usuarios:
    
    def __init__(self,nombre,apellido,dni,tipo,puesto,nacimiento):
        self.nombre=nombre
        self.apellido=apellido
        self.dni= dni
        self.tipo=tipo
        self.alta=1
        self.puesto=puesto
        self.nacimiento=nacimiento
        print("se creo usuario correctamente")


    def alta_usuario(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO usuarios(nombre,apellido,dni,tipo,alta,puesto,nacimiento) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (self.nombre,self.apellido,self.dni,self.tipo,self.alta,self.puesto,self.nacimiento)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
    
    def alta_login(self,contraseña):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO login(dni,contraseña) VALUES (%s,%s)"
            values = (self.dni,contraseña)
            cursor.execute(query, values)
            a.commit()
            print("se registro usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def listar_user(self):
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT dni,nombre,apellido,tipo,nacimiento FROM usuarios"
            cursor.execute(query)
            user = cursor.fetchall()

            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        print(user)
        return user
    
    def buscar_user(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT dni,nombre,apellido,tipo,nacimiento FROM usuarios WHERE dni=%s or nombre=%s or apellido=%s")
        cursor.execute(query, (param, param,param))
        data = cursor.fetchall()
        a.commit()
        return data
        
    def buscar_user_rows(param):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT dni,nombre,apellido,tipo,nacimiento FROM usuarios WHERE dni=%s or nombre=%s or apelldio=%s")
        data = cursor.execute(query, (param, param,param))
        a.commit()
        return data

    def mostrar_user(dni):
        a = c.start_connection()
        cursor = a.cursor()
        query = ("SELECT dni,nombre,apellido,tipo,nacimiento,puesto FROM usuarios WHERE dni=%s")
        cursor.execute(query,dni)
        data = cursor.fetchall()
        a.commit()
        return data

    def mostrar_datos_user_importado(self,dni):
        #a=c.start_connection()
        #cursor=a.cursor()
        #if c.controlador(dni,"usuarios","dni") == 1:
        #self.importar_datos_user(dni)
        try:
            if self.tipo=="1":
                self.tipo="administrador"
            else:
                self.tipo="usuario"     
            print("Nombre: ",self.nombre,"\nApellido: ",self.apellido,"\nDNI: ",dni,"\nFecha de nacimiento: ",self.nacimiento,
            "\nTipo: ",self.tipo,"\nPuesto: ",self.puesto)
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        #c.close_connection(a)
        return 0

    def ab_usuario(dni):
        a=c.start_connection()
        cursor=a.cursor()
        try: 
            query = "UPDATE usuarios set alta= IF(alta = '0', alta + 1, alta-1) WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def importar_datos_user(self,dni):
        a=c.start_connection()
        cursor=a.cursor()

        try:
            query = "SELECT nombre FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            self.nombre=str(b[0][0]) 
            query = "SELECT apellido FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            self.apellido=str(b[0][0])      
            query = "SELECT nacimiento FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            self.nacimiento=str(b[0][0])      
            query = "SELECT tipo FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            self.tipo=str(b[0][0])     
            query = "SELECT puesto FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            self.puesto=str(b[0][0])     
            print("se importo usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_datos_user(dni,nombre,apellido,tipo,puesto,nacimiento):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "UPDATE usuarios SET nombre=%s WHERE dni=%s"
            values = (nombre,dni)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET apellido=%s WHERE dni=%s"
            values = (apellido,dni)
            cursor.execute(query, values)
            a.commit()  
            query = "UPDATE usuarios SET dni=%s WHERE dni=%s"
            values = (dni,dni)
            cursor.execute(query, values)
            a.commit() 
            query = "UPDATE usuarios SET nacimiento=%s WHERE dni=%s"
            values = (nacimiento,dni)
            cursor.execute(query, values)
            a.commit() 
            query = "UPDATE usuarios SET tipo=%s WHERE dni=%s"
            values = (tipo,dni)
            cursor.execute(query, values)
            a.commit()    
            query = "UPDATE usuarios SET puesto=%s WHERE dni=%s"
            values = (puesto,dni)
            cursor.execute(query, values)
            a.commit() 
            print("se modifico  usuario correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

def contar_filas():
    a = c.start_connection()
    cursor = a.cursor()
    query = "SELECT COUNT(*) FROM usuarios"
    cursor.execute(query)
    a.commit()
    b = cursor.fetchall()
    b = str(b[0][0])
    n = int(b)
    c.close_connection(a)
    return n

def listar_user():
        a = c.start_connection()
        cursor = a.cursor()
        try:
            query = "SELECT dni,nombre,apellido,tipo,nacimiento FROM usuarios"
            cursor.execute(query)
            user = cursor.fetchall()

            a.commit()
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)
        return user