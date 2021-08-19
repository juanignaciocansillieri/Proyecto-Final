import pymysql
import os
import conexion as c

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
        password=str(b)
        #contraseña=str(contraseña)
        print(password,b)
        if password == "None":
            print("no se encontro el dni indicado")
            return 2
        else:
            password=str(b[0])
            if contraseña == password:
                print("se inicio sesion correctamente")
                return 1
            else: 
                print("contraseña incorrecta")
                return 3

    except pymysql.err.OperationalError as err:
        print("Ha ocurrido un error", err)
    c.close_connection(a)

def cambiar_conrasena(dniv,dni,password):
    a=c.start_connection()
    cursor=a.cursor()
    query = "SELECT idlogin FROM login WHERE dni=%s"
    values = dniv
    cursor.execute(query, values)
    a.commit()
    b = cursor.fetchall()
    idl = str(b[0][0])
    print (idl,dniv,dni,password)
    try:
        cursor=a.cursor()
        query = "UPDATE login SET contraseña=%s WHERE idlogin= %s"
        values = (password,idl)
        cursor.execute(query, values)
        cursor=a.cursor()
        query = "UPDATE login SET dni=%s WHERE idlogin= %s"
        values = (dni,idl)
        cursor.execute(query, values)
        print("Contraseña cambiada exitosamente")
        a.commit()
    except pymysql.err.OperationalError as err:
        print("Ha ocurrido un error", err)
    c.close_connection(a)