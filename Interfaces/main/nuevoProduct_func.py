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
import area as a
import lotes as l
import alojamiento as p
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
        self.cbox()

    
    #CREAR PRODUCTO NUEVO
    def crearProducto(self):   
      global defaultImg
      #RECIBIR VALORES DE LA VENTANA
      codigo = self.ui.codigo_input.text()
      descripcion = self.ui.descripcion_input.toPlainText()
      cantidad = self.ui.cantidad_num.value()
      marca = self.ui.marca_input.text()
      venc = self.ui.venc_date.date().toString("yyyy/MM/dd")
      lote = self.ui.lote_input.text()
      ubicacion = self.ui.ubicacion_input.text()
      imagen = defaultImg
      if self.ui.fragil_si.isChecked():
        fragil = "1"
      else :
        fragil = "0"

      condicion = self.ui.area_comboBox.currentText()

  

      peso = self.ui.peso_num.value()
      ancho = self.ui.ancho_num.value()
      altura = self.ui.altura_num.value()
      largo = self.ui.largo_num.value()

    
      if codigo==""  or descripcion=="" or cantidad=="" or marca=="" or venc=="" or lote=="" or peso=="" or ancho=="" or largo=="" or altura=="":
        QtWidgets.QMessageBox.critical(self, "Error", "Ingrese todos los datos")
        return None

     # if len(codigo)!=8:
      #  QtWidgets.QMessageBox.critical(self, "Error", "Ingrese un dni existente")
       # return None
      
      
      if pr.ver_cod(codigo) == 1:
        QtWidgets.QMessageBox.critical(self, "Error", "Codigo Existente")
        return None
      else:
        pr.productos(codigo,marca,cantidad,descripcion,ubicacion,lote,venc,condicion,fragil,defaultImg,peso,largo,ancho,altura)


        self.close()
      
      

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
            print(defaultImg)

    def clearInput(self):
         self.ui.codigo_input.setText("")
         self.ui.descripcion_input.setText("")
         self.ui.cantidad_num.setValue("")
         self.ui.lote_input.setText("")
         self.ui.peso_num.setValue("")
         self.ui.ancho_num.setValue("")
         self.ui.largo_num.setValue("")
         self.ui.altura_num.setValue("")
         self.ui.marca_input.setText("")
         self.ui.venc_date.setDate("")
         self.ui.descripcion_input.setText("")
         #self.ui.area_comboBox.setCompleter("")
         self.ui.ubicacion_input.setText("")


    def cbox(self):
        areas = a.Area.listar_area()
        for ar in areas:
            self.ui.area_comboBox.addItem(ar[0])
        areaSeleccionada = self.ui.area_comboBox.currentText()
        posiciones = p.alojamiento.listar_alojamiento_disponibles_area(areaSeleccionada)
        for pos in posiciones:
          self.ui.posicion_comboBox.addItem(pos[0])

        self.ui.area_comboBox.currentIndexChanged.connect(self.clearCombo)
        self.ui.area_comboBox.currentIndexChanged.connect(self.updateCombo)

    def updateCombo(self):
      areaSeleccionada = self.ui.area_comboBox.currentText()
      posiciones = p.alojamiento.listar_alojamiento_disponibles_area(areaSeleccionada)
      for pos in posiciones:
        self.ui.posicion_comboBox.addItem(pos[0])

    def clearCombo(self):
      self.ui.posicion_comboBox.clear()
  