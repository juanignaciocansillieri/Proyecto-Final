import pymysql
import os

#AXIOMAS Y OBLIGACIONES A LA HORA DE LA CODIFICACION:
#se abre conexion unicamente cunado estamos por usar la base de datos y al finalizar se la cierra
#cada de vez que se usar el cursor, posteriormente se lo cierra
#para la devolucion de datos de cursor se usara fetchall e intantaneamente se lo convertira 

def start_connection(): #inicia conexcion a db
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
 
def close_connection(con):  #cierra conexcion a db
    try:
        con.close()
        print("se cerro conexion\n",con)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)

def borrar_tabla(con):  #borra tablas (posible modificacion futura: ingresar el nombre de la tabla y que la borre)
    q="DROP TABLE IF EXISTS produc;" #se usa "," para mas de una
    try:
        cur=con.cursor()
        cur.execute(q)
        cur.close()
        print("se borro con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)

def crear_tabla(con):   #crea una tabla (al iniciar por primera vez el programa se crearan todas)
    q="CREATE TABLE IF NOT EXISTS produc(id int UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL, nombre VARCHAR(30) NOT NULL,apellido VARCHAR(30) NOT NULL,edad int(2) NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"
    try:
        cur=con.cursor()
        cur.execute(q)
        cur.close()
        print("se creo con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:",err)

def contar_filas_tabla(con):
    #cuenta las filas de una tabla especifica
    #(modificacion futura: definir la sentencia de la funcion para que cuente en la tabal donde sea necesario)
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