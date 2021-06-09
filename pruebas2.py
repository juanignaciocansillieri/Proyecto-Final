import pruebas as p
#p.crear_vector()

from DB import conexion as c
#a=c.start_connection()
#c.borrar_tabla()
#c.crear_tabla()
#c.contar_filas_tabla()
#c.close_connection()

nombre=input("ingrese el nombre:")
apellido=input("ingrese el apellido:")
tipo=input("ingrese el tipo(1/0):")
puesto=input("ingrese el peusto:")
nacimiento=input("ingrese el fecha de nacimiento:")

from DB import ABM_usuarios as abmuser
#abmuser.crear_usuario(nombre,apellido,tipo,1,puesto,nacimiento)
#abmuser.borrar_usuario(nombre,apellido)
#abmuser.ab_usuario(nombre,apellido)
#abmuser.mostrar_usuario(nombre,apellido)

from CLASES import usuarios as u
u1=u.usuarios(nombre,apellido,tipo,puesto,nacimiento)
u1.alta_usuario()
