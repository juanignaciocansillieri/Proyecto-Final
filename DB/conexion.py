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