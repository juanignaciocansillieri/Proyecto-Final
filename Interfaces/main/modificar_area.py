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
from modificar_area_ui import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import area as a

nombreViejo = ""
class ModificarArea(QMainWindow):

    def __init__(self,id):
        super(ModificarArea, self).__init__()
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
        self.rellenarCampos(id)
        self.ui.modificar_btn.clicked.connect(lambda: self.modificarArea(id))
        
    
    #CREAR PRODUCTO NUEVO
    def modificarArea(self,id):   
      nombre = id
      #RECIBIR VALORES DE LA VENTANA
      identificador = self.ui.identificador_input.text()
      longitud = self.ui.largo_num.value()
      pasillos = self.ui.pasillo_num.value()
      segmentos = self.ui.segmento_num.value()
      ancho = self.ui.ancho_num.value()
      alto = self.ui.alto_num.value()
      a.Area.modificar_area(nombre,identificador,pasillos,segmentos,longitud,ancho,alto)
      self.close()
      return(nombre)
      
    def rellenarCampos(self,id):
        areas = a.Area.mostrar_area(id)
        print("area",id)
        atributos = list(areas[0])
        self.ui.nombre_input.setText(atributos[0])
        self.ui.identificador_input.setText(atributos[1])
        self.ui.pasillo_num.setValue(int(atributos[2]))
        self.ui.segmento_num.setValue(int(atributos[3]))
        self.ui.largo_num.setValue(int(atributos[4]))
        self.ui.ancho_num.setValue(int(atributos[5]))
        self.ui.alto_num.setValue(int(atributos[6]))
        
    
