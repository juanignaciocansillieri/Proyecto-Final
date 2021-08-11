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
sys.path.append("C:\\proyecto-final\\CLASES\\")
import usuarios as us

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

        self.ui.pushButton.clicked.connect(self.crearUser)
    
    #CREAR PRODUCTO NUEVO
    def crearUser(self):   
    
      #RECIBIR VALORES DE LA VENTANA
      apellido = self.ui.apellido_input.text()
      nom = self.ui.nombre_input.text()
      dni = self.ui.mail_input.text()
      nacimiento = self.ui.nac_date.date().toString("yyyy/MM/dd")
      puesto = self.ui.puesto_input.text()
      tipo = self.ui.tipo_cb.currentText()
      contraseña = self.ui.pass_input.text()

      
      if tipo=="Admin":
        tipo="1"
      else:
        tipo="0"

      user = us.usuarios(nom,apellido,dni,tipo,puesto,nacimiento)
      user.alta_usuario()
      user.alta_login(contraseña)
      self.clearInput()
      #return(codigo,nombre,desc,cantidad,marca,venc,condicion,lote,fragil)
      


    def clearInput(self):
         self.ui.apellido_input.setText("")
         self.ui.nombre_input.setText("")
         self.ui.mail_input.setText("")
         self.ui.puesto_input.setText("")
         self.ui.pass_input.setText("")
