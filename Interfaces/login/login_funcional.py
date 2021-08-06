import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget
from PyQt5.QtCore import QFile,Qt
from login import Ui_MainWindow
sys.path.append("C:\\Users\\Juan Ignacio\\Desktop\\proyecto python\\Interfaces\\main\\")
import main_func as m
sys.path.append("..")
from DB import index as i

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
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
                self.main = m.Main()
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Datos incorrectos")
                self.ui.user_login_input.setText("")
                self.ui.pass_login_input.setText("")
                