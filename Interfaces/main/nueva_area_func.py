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
from nueva_area import Ui_MainWindow
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
        self.ui.crearprod_btn.clicked.connect(self.crearArea)

    
    #CREAR PRODUCTO NUEVO
    def crearArea(self):   
      #RECIBIR VALORES DE LA VENTANA
      nom = self.ui.motivo_input.text()
      ide = self.ui.motivo_input_2.text()
      pasillo = self.ui.segmentos_num.value()
      segmento = self.ui.pasillos_num.value()
      area = a.Area(nom,ide,pasillo,segmento) 
      longitud = self.ui.longitud_num.value()
      ancho = self.ui.ancho_num.value()
      alto = self.ui.alto_num.value()
      self.close()
     
      
      

     
      
