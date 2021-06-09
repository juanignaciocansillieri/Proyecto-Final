import pymysql
import os
from DB import conexion as c


class usuarios:
    
    def __init__(self,nombre,apellido,tipo,puesto,nacimiento):
        self.nombre=nombre
        self.apellido=apellido
        self.tipo=tipo
        self.alta=1
        self.puesto=puesto
        self.nacimiento=nacimiento
        print("se creo correctamente")


    def alta_usuario(self):
        a=c.start_connection()
        cursor=a.cursor()
        try:
            query = "INSERT INTO usuarios(nombre,apellido,tipo,alta,puesto,nacimiento) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (self.nombre,self.apellido,self.tipo,self.alta,self.puesto,self.nacimiento)
            cursor.execute(query, values)
            a.commit()
            print("se dio alta correctamente")
        except pymysql.err.OperationalError as err:
            print("Hubo un error:", err)
        c.close_connection(a)