import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import nuevo_producto_ui
from nuevo_producto_ui import Ui_MainWindow

class ProductWindow(QMainWindow):

    def __init__(self):
        super(ProductWindow, self).__init__()
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
        # Agregar Producto
        self.ui.crearprod_btn.clicked.connect(self.crearProducto)

    
    #CREAR PRODUCTO NUEVO
    def crearProducto(self):   
    
      #RECIBIR VALORES DE LA VENTANA
      codigo = self.ui.codigo_input.text()
      nombre = self.ui.nombre_input.text()
      desc = self.ui.desc_input.text()
      cantidad = self.ui.cantidad_input.text()
      marca = self.ui.marca_input.text()
      venc = self.ui.venc_input.text()
      lote = self.ui.lote_input.text()
      fragil = self.ui.fragil_rb.isChecked()
      condicion = self.ui.condicion_cbox.currentText()
      self.clearInput()
      print(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      return(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      


    def clearInput(self):
         self.ui.codigo_input.setText("")
         self.ui.nombre_input.setText("")
         self.ui.desc_input.setText("")
         self.ui.cantidad_input.setText("")
         self.ui.marca_input.setText("")
         self.ui.venc_input.setText("")
         self.ui.lote_input.setText("")
