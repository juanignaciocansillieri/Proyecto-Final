import pymysql
from pymysql import connect, err
from pymysql.err import Error
import os

def start_connection():

    try:
        connect = pymysql.Connect(
        host="localhost",
        port=3306,
        user=os.environ.get('USER_MYSQL'),
        password=os.environ.get('PASSWORD_MYSQL'),
        database=os.environ.get('DB_MYSQL'))
        print(connect)
    except pymysql.err.OperationalError as err:
        print("hubo un error:", err)
    return(connect)

def close_connection(connect):
    connect.close()
    print("se cerro la conexión con éxito")



    
      
