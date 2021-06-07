import pymysql
import os

def start_connection():
    h='localhost'
    p=3306
    u=os.environ.get('USER_MYSQL')
    ps=os.environ.get('PASSWORD_MYSQL')
    db=os.environ.get('DB_MYSQL')
    try: 
        con= pymysql.Connect(host=h,port=p,user=u,password=ps,database=db)
        print(con,"conectado")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)
    
    return con
 
def close_connection(con):
    try:
        con.close()
        print("se cerro conexion",con)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)

def borrar_tabla(con):
    q="DROP TABLE IF EXISTS produc;"
    try:
        cur=con.cursor()
        cur.execute(q)
        cur.close()
        print("se borro con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)

def crear_tabla(con):
    q="CREATE TABLE IF NOT EXISTS produc(id int UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL, nombre VARCHAR(30) NOT NULL,apellido VARCHAR(30) NOT NULL,edad int(2) NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    try:
        cur=con.cursor()
        cur.execute(q)
        cur.close()
        print("se creo con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)

def contar_filas_tabla(con):
    q="SELECT COUNT(*) from produc;"
    try:
        cur=con.cursor()
        cur.execute(q)
        a=cur.fetchall()    #fetchall hace que el cursor muestre todos las filas
        a=int(a[0][0])      #convierte la tupla del cursor en un entero
        cur.close           #cierra el cursor
        print("hay ",a,"vistas")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)