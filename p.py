from PyQt5.QtCore import QPluginLoader
from numpy import apply_along_axis
import pymysql
import index as i
import db as db
from gui import *
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

class Listar():
    def __init__(self):
        super(Listar, self).__init__()
        self.ui = QPluginLoader().load("gui.ui")

if __name__ == "__main__":

        a = db.start_connection()
        i.listar_usuarios(a, a.cursor())
        a = db.start_connection()
        u = i.listar_usuarios(a, a.cursor())
        db.close_connection(a)
