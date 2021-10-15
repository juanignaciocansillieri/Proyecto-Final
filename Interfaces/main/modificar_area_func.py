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
from modificar_area import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import area as a

class NewArea(QMainWindow):

    def __init__(self):
        super(NewArea, self).__init__()
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
        ## self.ui.crearprod_btn.clicked.connect(self.crearArea)
        self.ui.modificar_btn.clicked.connect(self.modificar_area)

    
    #CREAR PRODUCTO NUEVO
    def modificar_area(self):   
      #RECIBIR VALORES DE LA VENTANA
      IdArea = self.ui.IdArea_input.text()
      nombre = self.ui.nombre_input.text()
      longitud = self.ui.longitud_num.value()
      identificador = self.ui.identificador_input.text()
      disponibilad = self.ui.identificador_input.text()
      alto = self.ui.alto_num.value()
      pasillos = self.ui.pasillos_num.value()
      segmentos = self.ui.segmentos_num.value()
      ancho = self.ui.ancho_num.value()
      self.close()
     
      
      

     
      
