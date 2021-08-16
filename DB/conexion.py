import pymysql
import os

# AXIOMAS Y OBLIGACIONES A LA HORA DE LA CODIFICACION:
# se abre conexion unicamente cuando estamos por usar la base de datos y al finalizar se la cierra
# cada de vez que se usar el cursor, posteriormente se lo cierra
# para la devolucion de datos de cursor se usara fetchall e intantaneamente se lo convertira


def start_connection():  # inicia conexion a db
    h = 'localhost'
    p = 3306
    u = os.environ.get('USER_MYSQL')
    ps = os.environ.get('PASSWORD_MYSQL')
    db = os.environ.get('DB_MYSQL')
    try:
        con = pymysql.Connect(host=h, port=p, user=u, password=ps, database=db)
        print(con, "\nse creo conexion")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
        
    return con


def close_connection(con):  # cierra conexion a db
    try:
        con.close()
        print("se cerro conexion\n",con)
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)


def borrar_tabla():  # borra tablas (posible modificacion futura: ingresar el nombre de la tabla y que la borre)
    # se usa "," para mas de una
    con=start_connection()
    q = "DROP TABLE IF EXISTS productos, usuarios,alojamiento,login,matriz,datosmatriz;"
    try:
        cur = con.cursor()
        cur.execute(q)
        cur.close()
        print("se borro las tablas con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    close_connection(con)

def crear_tabla():  # crea una tabla (al iniciar por primera vez el programa se crearan todas)
    con=start_connection()
    q1 = """CREATE TABLE IF NOT EXISTS usuarios (
    idusuarios INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    apellido VARCHAR(20) NOT NULL,
    dni VARCHAR(20) NOT NULL,
    tipo BINARY(1) NOT NULL,
    alta BINARY(1) NOT NULL,
    puesto VARCHAR(20) NOT NULL,
    nacimiento DATE NOT NULL,
    mail VARCHAR(20) NOT NULL);"""
    q2 = """CREATE TABLE IF NOT EXISTS productos (
    idproductos INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    marca VARCHAR(20) NOT NULL,
    cantidad INT NOT NULL,
    descripcion VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(20) NOT NULL,
    lote INT NOT NULL,
    vencimiento DATE NOT NULL,
    refrigeracion BINARY(1) NOT NULL,
    inflamable BINARY(1) NOT NULL,
    fragil BINARY(1) NOT NULL,
    foto VARCHAR(50) NOT NULL,
    peso INT NOT NULL,
    largo INT NOT NULL,
    ancho INT NOT NULL,
    alto INT NOT NULL);"""
    q3 = """CREATE TABLE IF NOT EXISTS alojamiento (
    idalojamiento INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    largo INT NOT NULL,
    ancho INT NOT NULL,
    alto INT NOT NULL,
    disponibilidad BINARY(1) NOT NULL,
    posicion VARCHAR(20) NOT NULL,
    refrigeracion BINARY(1) NOT NULL,
    limite VARCHAR(20) NOT NULL);"""
    q4 ="""CREATE TABLE IF NOT EXISTS login (
    idlogin INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    dni VARCHAR(20) NOT NULL,
    contraseña VARCHAR(20) NOT NULL);"""
    q5="""CREATE TABLE IF NOT EXISTS datosmatriz (
    filas INT NOT NULL,
    columnas INT NOT NULL,
    altura INT NOT NULL);"""
    q6=""" CREATE TABLE IF NOT EXISTS matriz (
    idmatriz INT UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,
    codigo VARCHAR(20) NOT NULL,
    fila VARCHAR(20) NOT NULL,
    columna VARCHAR(20) NOT NULL,
    altura VARCHAR(20) NOT NULL,
    disponibilidad BINARY(1) NOT NULL);"""

    try:
        cur = con.cursor()
        cur.execute(q1)
        cur.execute(q2)
        cur.execute(q3)
        cur.execute(q4)
        cur.execute(q5)
        cur.execute(q6)
        cur.close()
        print("se creo las tablas con exito")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
    close_connection(con)


def contar_filas_tabla():  # despues hay que poner de que tabla queremos contar
    # cuenta las filas de una tabla especifica
    # (modificacion futura: definir la sentencia de la funcion para que cuente en la tabal donde sea necesario)
    con=start_connection()
    q = "SELECT COUNT(*) from productos;"
    try:
        cur = con.cursor()
        cur.execute(q)
        a = cur.fetchall()  # fetchall hace que el cursor muestre todos las filas
        a = int(a[0][0])  # convierte la tupla del cursor en un entero
        cur.close  # cierra el cursor
        print("hay ", a, "vistas")
    except pymysql.err.OperationalError as err:
        print("Hubo un error:", err)
        # despues tiene que hacer un return
    close_connection(con)

def controlador(con,tabla,columna):
    a=start_connection()
    cursor=a.cursor()
    str(con)
    str(tabla)
    str(columna)
    try:
        query = "SELECT * FROM %s WHERE %s = %s"
        values = (tabla,columna,con)
        cursor.execute(query, values)
        a.commit()
        b=cursor.fetchone()
        control1=str(b)
        if control1 == "None" :#and 
            print("no se encuentra")
            return 0
        else: return 1
            
    except pymysql.err.OperationalError as err:
        print("Ha ocurrido un error", err)
    close_connection(a)