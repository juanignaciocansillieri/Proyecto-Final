from sys import setprofile
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
        print("se creo correctamente")


    def alta_usuario(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO usuarios(nombre,apellido,dni,tipo,alta,puesto,nacimiento) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (self.nombre,self.apellido,self.dni,self.tipo,self.alta,self.puesto,self.nacimiento)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta correctamente")
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
            print("se registro correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def mostrar_datos_user(self,dni):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "SELECT nombre FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() #fetchall llama a la tupla
            nombre=str(b[0][0])      #al ser "[0]" elmina un solo parentesis, dos "[0] elimina los 2"
            query = "SELECT apellido FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            apellido=str(b[0][0])      
            query = "SELECT nacimiento FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            nacimiento=str(b[0][0])      
            query = "SELECT tipo FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            tipo=str(b[0][0])     
            if tipo=="1":
                tipo="administrador"
            else:
                tipo="usuario"
            query = "SELECT puesto FROM usuarios WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            b=cursor.fetchall() 
            puesto=str(b[0][0])     
            print("Nombre: ",nombre,"\nApellido: ",apellido,"\nDNI: ",dni,"\nFecha de nacimiento: ",nacimiento,
            "\nTipo: ",tipo,"\nPuesto: ",puesto)
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def ab_usuario(self,dni):
        a=c.start_connection()
        try:
            cursor=a.cursor()
            query = "UPDATE usuarios set alta= IF(alta = '0', alta + 1, alta-1) WHERE dni=%s"
            values = dni
            cursor.execute(query, values)
            a.commit()
            print("se MODIFICO correctamente")
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
            print("se importo correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)

    def modificar_datos_user(self,nombre,apellido,dni,tipo,puesto,nacimiento):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "UPDATE usuarios SET nombre=%s WHERE dni=%s"
            values = (nombre,self.dni)
            cursor.execute(query, values)
            a.commit()
            query = "UPDATE usuarios SET apellido=%s WHERE dni=%s"
            values = (apellido,self.dni)
            cursor.execute(query, values)
            a.commit()  
            query = "UPDATE usuarios SET dni=%s WHERE dni=%s"
            values = (dni,self.dni)
            cursor.execute(query, values)
            a.commit() 
            query = "UPDATE usuarios SET nacimiento=%s WHERE dni=%s"
            values = (nacimiento,self.dni)
            cursor.execute(query, values)
            a.commit() 
            query = "UPDATE usuarios SET tipo=%s WHERE dni=%s"
            values = (tipo,self.dni)
            cursor.execute(query, values)
            a.commit()    
            query = "UPDATE usuarios SET puesto=%s WHERE dni=%s"
            values = (puesto,self.dni)
            cursor.execute(query, values)
            a.commit() 
            print("se modifico correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)