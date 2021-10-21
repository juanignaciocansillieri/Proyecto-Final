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
from posiciones_alojamiento_ui import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import area as a

class PosicionAlojamiento(QMainWindow):

    def __init__(self,nombreArea):
        super(PosicionAlojamiento, self).__init__()
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
        #self.ui.modificar_btn.clicked.connect(self.modificar_posicion)
        self.rellenarCampos(nombreArea)
    
    #CREAR POSICIONES ALOJAMIENTO 
    def modificar_posicion(self):   
      #RECIBIR VALORES DE LA VENTANA
      
      columna = self.ui.columna_num.value()
      fila = self.ui.fila_num.value()
      nivel = self.ui.nivel_num.value()
      pasillo = self.ui.comboBox_pasillo.currentText()
      segmento = self.ui.comboBox_segmento.currentText()
      ancho = self.ui.ancho_num.value()
      alto = self.ui.alto_num.value()
      largo = self.ui.largo_num.value()
      a.Area.modificar_area(identv,idenn,nombre,pasillo,segmento,disponibilidad,largo,ancho,alto)

      

    # RELLENAR CAMPOS
    def rellenarCampos(self,id):
        
        posiciones = a.Area.mostrar_area(id)
        atributos = list(posiciones[0])
        pasillos = int(atributos[2])
        segmentos = int(atributos[3])
        i = 1
        j = 1
        while(i<=pasillos):
          self.ui.comboBox_pasillo.addItem('%i' % i)
          i+=1
        while(j<=segmentos):
          self.ui.comboBox_segmento.addItem('%i' % j)
          j+=1
        
        
        self.ui.lineEdit.setText(id)
        """
        self.ui.columna_num.setValue(atributos[0])
        self.ui.fila_num.setValue(atributos[1])
        self.ui.nivel_num.setValue(atributos[3])
        self.ui.ancho_num.setValue(atributos[4])
        self.ui.alto_num.setValue(atributos[5])
        self.ui.largo_num.setValue(atributos[6])
        """
      
