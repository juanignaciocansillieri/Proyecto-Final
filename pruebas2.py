import pruebas as p
#p.crear_vector()
import sys
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as c
#a=c.start_connection()
#c.borrar_tabla()
c.crear_tabla()
#c.contar_filas_tabla()
#c.close_connection()

#nombre=input("ingrese el nombre:")
#apellido=input("ingrese el apellido:")
#dni=input("ingrese el dni:")
#tipo=input("ingrese el tipo(1/0):")
#puesto=input("ingrese el peusto:")
#nacimiento=input("ingrese el fecha de nacimiento:")

from DB import loginDB as log
sys.path.append("C:\\proyecto-final\\CLASES\\")
import usuarios as us

import productos as pr
import alojamiento as al
import matriz as mz

"""
aa=us.usuarios("alex","arraya","123",1,"gerente","1999/05/14")
aa.alta_usuario()
aa.alta_login("asd")
bb=us.usuarios("juan","cansillieri","456",1,"productor","1999/07/20")
bb.alta_usuario()
bb.alta_login("zxc")
cc=us.usuarios("nicolas","rija","789",0,"asistente","1999/04/26")
cc.alta_usuario()
cc.alta_login("qwe")
"""

dd=pr.productos("123","leche","serenisima","10","clasica","...","147","2021/07/25",1,0,0)
dd.alta_producto()
ee=pr.productos("456","harina","harina","100","0000","...","258","2021/09/10",0,0,0)
dd.alta_producto()
ff=pr.productos("789","fideos","gallo","50","integral","...","369","2021/08/05",0,0,0)
ff.alta_producto()


lista=pr.listar_prod2()
print(lista)


#gg=mz.matriz(3,3,3)



#al.generacion_posicion("12 1 5")

#from DB import ABM_usuarios as abmuser
#abmuser.crear_usuario(nombre,apellido,tipo,1,puesto,nacimiento)
#abmuser.borrar_usuario(nombre,apellido)
#abmuser.ab_usuario(nombre,apellido)
#abmuser.mostrar_usuario(nombre="alex",apellido="arraya")
#abmuser.mostrar2__usuario(nombre="alex",apellido="arraya")

#from CLASES import usuarios as u
#u1=u.usuarios(nombre,apellido,dni,tipo,puesto,nacimiento)
#u1.alta_usuario()

#from DB import login as log
#log.log_in(132,132)


""" aa=15
bb=16
cc=20
union=str(aa)+str(bb)+str(cc)
print(union)"""


