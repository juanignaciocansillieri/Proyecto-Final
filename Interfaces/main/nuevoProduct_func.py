import sys
import os
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import nuevo_producto_ui
from nuevo_producto_ui import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import productos as pr




defaultImg = "Error.png"

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
        self.ui.subirFoto_btn.clicked.connect(self.uploadImg)

    
    #CREAR PRODUCTO NUEVO
    def crearProducto(self):   
    
      #RECIBIR VALORES DE LA VENTANA
      codigo = self.ui.codigo_input.text()
      nombre = self.ui.nombre_input.text()
      desc = self.ui.desc_input.text()
      cantidad = self.ui.cantidad_input.text()
      marca = self.ui.marca_input.text()
      venc = self.ui.venc_date.date().toString("dd/MM/yyyy")
      lote = self.ui.lote_input.text()
      fragil = self.ui.fragil_rb.isChecked()
      condicion = self.ui.condicion_cbox.currentText()
      if codigo=="" or nombre=="" or desc=="" or cantidad=="" or marca=="" or venc=="" or lote==""  :
        QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
        return None

     # if len(codigo)!=8:
      #  QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un dni existente")
       # return None
      
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

      if pr.ver_cod(codigo) == 1:
        QtWidgets.QMessageBox.critical(self, "Error", "Codigo Existente")
        return None
      else:
      
        product = pr.productos(codigo,nombre,marca,cantidad,desc,lote,venc,refri,infla,fragil)
        product.alta_producto()
        self.close()
      self.clearInput()
      
      
      print(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      #return(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      

    def uploadImg(self):
        global defaultImg 
        size=(256,256)
        self.filename,ok = QFileDialog.getOpenFileName(self,"Upload Image","","Image Files (*.jpg *.png)")
        if ok:
            print(self.filename)
            defaultImg = os.path.basename(self.filename)
            print(defaultImg)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\proyecto-final\Interfaces\main\img/{0}".format(defaultImg))

    def clearInput(self):
         self.ui.codigo_input.setText("")
         self.ui.nombre_input.setText("")
         self.ui.desc_input.setText("")
         self.ui.cantidad_input.setText("")
         self.ui.marca_input.setText("")
         #self.ui.venc_date.setDate("")
         self.ui.lote_input.setText("")
