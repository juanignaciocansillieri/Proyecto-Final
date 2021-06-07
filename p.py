from numpy import apply_along_axis
import pymysql
import index as i
import db as db


a = db.start_connection()
i.crear_usuario(a, a.cursor())
db.close_connection(a)