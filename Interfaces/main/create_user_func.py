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
from create_user import Ui_MainWindow

class UsuarioWindow(QMainWindow):

    def __init__(self):
        super(UsuarioWindow, self).__init__()
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

        #self.ui.pushButton.clicked.connect(self.crearProducto)
    
    #CREAR PRODUCTO NUEVO
    def crearProducto(self):   
    
      #RECIBIR VALORES DE LA VENTANA
      codigo = self.ui.codigo_input.text()
      nombre = self.ui.nombre_input.text()
      desc = self.ui.desc_input.text()
      cantidad = self.ui.cantidad_input.text()
      marca = self.ui.marca_input.text()
      venc = self.ui.venc_date.date().toString("yyyy/MM/dd")
      lote = self.ui.lote_input.text()
      fragil = self.ui.fragil_rb.isChecked()
      condicion = self.ui.condicion_cbox.currentText()
      
      if fragil==True:
        fragil="1"
      else:
        fragil="0"
      if condicion=="Refrigerado":
        refri=1
        infla=0
      elif condicion=="Inflamable": 
        refri=0
        infla=1
      else:
        refri=0
        infla=0
      product = pr.productos(codigo,nombre,marca,cantidad,desc,lote,venc,refri,infla,fragil)
      product.alta_producto()
      self.clearInput()
      print(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      #return(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      


    def clearInput(self):
         self.ui.codigo_input.setText("")
         self.ui.nombre_input.setText("")
         self.ui.desc_input.setText("")
         self.ui.cantidad_input.setText("")
         self.ui.marca_input.setText("")
         #self.ui.venc_date.setDate("")
         self.ui.lote_input.setText("")
