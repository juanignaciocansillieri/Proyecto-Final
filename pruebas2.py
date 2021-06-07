import pruebas as p
#p.crear_vector()

from DB import conexion as c
a=c.start_connection()
c.close_connection(a)