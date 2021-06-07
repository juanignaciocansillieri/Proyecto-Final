import pruebas as p
#p.crear_vector()

from DB import conexion as c
a=c.start_connection()
c.borrar_db(a)
#c.crear_db(a)
c.close_connection(a)