import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import create_user
from bm_producto_ui import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import productos as p

class BMProduct(QMainWindow):

    def __init__(self):
        super(BMProduct, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.rellenarCampos()
        self.show()




    def rellenarCampos(self):
        producto = p.productos.mostrar_product(productId)
        atributos = list(producto[0])
        atributos[0] = self.ui.codigo_input
        atributos[1] = self.ui.nombre_input
        atributos[2] = self.ui.marca_input
        atributos[3] = self.ui.venc_date
        atributos[4] = self.ui.lote_input
        #atributos[3] = self.ui.peso_num
        #atributos[4] = self.ui.ancho_num
        #atributos[5] = self.ui.altura_num
        #atributos[6] = self.ui.cantidad_num
        #atributos[8] = self.ui.condicion_cbox
