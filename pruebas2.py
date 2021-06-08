import pruebas as p
#p.crear_vector()

from DB import conexion as c
a=c.start_connection()
c.borrar_tabla(a)
#c.crear_tabla(a)
#c.contar_filas_tabla(a)
#c.close_connection(a)

nombre=input("ingrese el nombre:")
apellido=input("ingrese el apellido:")
#tipo=input("ingrese el tipo(1/0):")
#puesto=input("ingrese el peusto:")
#nacimiento=input("ingrese el fecha de nacimiento:")

from DB import ABM_usuarios as abmuser
#abmuser.crear_usuario(nombre,apellido,tipo,1,puesto,nacimiento)
#abmuser.borrar_usuario(nombre,apellido)
#abmuser.ab_usuario(nombre,apellido)