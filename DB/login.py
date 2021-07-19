import pymysql
import os
from DB import conexion as c

def log_in (dni,contraseña):
    print(dni,contraseña)
    a=c.start_connection()
    cursor=a.cursor()
    try:
        cursor=a.cursor()
        query = "SELECT contraseña FROM login WHERE dni= %s"
        values = dni
        cursor.execute(query, values)
        a.commit()
        b=cursor.fetchone()
        password=str(b[0])
        contraseña=str(contraseña)
        print(password,b)
        if password == "None":
            print("no se encontro el dni indicado")
        else:
            if contraseña == password:
                print("se inicio sesion conrractamente")
                #aca iria el comando para pasar a la ventana correspondiente
            else: 
                print("contraseña incorrecta")

    except pymysql.err.OperationalError as err:
        print("Ha ocurrido un error", err)
    c.close_connection(a)