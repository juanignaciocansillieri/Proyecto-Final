from typing import final
import numpy as np

def sumar():
    print("ingrese el primer numero: ")
    n1=int(input())
    print("ingrese el segundo numero: ")
    n2=int(input())
    suma=n1+n2
    print("la suma es: ",suma)


def crear_vector():
    print("ingrese el tamaño: ")
    n3= int(input())
    v=np.arange(n3)
    i=0
    v1=0
    print(v[:])

    while i<n3:
        print("ingrese el valor para la posicion ", i)
        v1= int(input())
        v[i]=v1
        i=1+i

    
    i=0
    print("vector: ")
    while i<n3:
        print(v[i])
        i=i+1
    
