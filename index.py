from typing import AbstractSet
import pymysql
from pymysql import connect, err
from pymysql.err import Error
print("hola")

#ELIMINAR TABLA
DROP_TABLE = """DROP TABLE IF EXISTS produc     """ 
#CREAR TABLA
PRODUCTS_TABLE = """CREATE TABLE produc (  
        id int UNSIGNED AUTO_INCREMENT PRIMARY KEY NOT NULL,  
        nombre VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);"""

if __name__ == '__main__':
        try:
                connect = pymysql.connect(host="localhost",port=3306,user="root",password="asd123",database="prueba1")
                print("exitosamente")
                cursor = connect.cursor()       
                cursor.execute(DROP_TABLE)
                cursor.execute(PRODUCTS_TABLE)
        except pymysql.err.OperationalError as err:
                print("hubo un error:" ,err)

        finally:
                cursor.close()
                connect.close()
                print("se cerro la conexión")
                #SIEMPRE CERRAR CUANDO NO SE LO UTILIZA MÁS, ASI LIBERA PROCESOS.


lista = ["h","o","l","a"]
string = " como estas"
hola = "hola"

print(len(lista),len(hola))
for i in lista:
        if(len(lista)==len(hola) +1):
                hola += i
                hola+= string
        else:
                break

print(hola)

print("Soy Nicolás")