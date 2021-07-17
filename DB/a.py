from typing import AbstractSet
import os
import pymysql
from pymysql import connect, err
import numpy as np
from pymysql import cursors
from pymysql.err import Error
import db as db


def verificar_usuario(codigo, password):
    c = db.start_connection()
    cursor = c.cursor()
    query = "select Codigo, Password from usuarios where Codigo = %s AND Password = %s' "
    values = (codigo, password)
    cursor.execute(query,values)
    c.commit()
    db.close_connection(c)

# CREAR NUEVO USUARIO - VERIFICAR NÚMERO ENTERO
verificar_usuario("1","asd123")