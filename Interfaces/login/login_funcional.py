import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget
from PyQt5.QtCore import QFile,Qt
sys.path.append("..")
from login import Ui_MainWindow
from Funciones import functions
from DB import index as i

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Centrar Pantalla
        self.funciones = functions.Functions()
        self.funciones.centrarPantallas()
        ### BOTON INGRESAR ####
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.login_btn.clicked.connect(self.verificacion)

        ## MOSTRAR ##
        self.show()

### VERIFICAR DATOS INGRESADOS LA DB ####
    def verificacion(self):
            user = self.ui.user_login_input.text()
            password = self.ui.pass_login_input.text()
            usuario = i.verificar_usuario(user,password)
            if usuario == 1:
                self.close()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Datos incorrectos")
                self.ui.user_login_input.setText("")
                self.ui.pass_login_input.setText("")
                