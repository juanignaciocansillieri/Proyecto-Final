import pruebas as p
#p.crear_vector()

from DB import conexion as c
a=c.start_connection()
c.borrar_tabla(a)
#c.crear_tabla(a)
#c.contar_filas_tabla(a)
c.close_connection(a)