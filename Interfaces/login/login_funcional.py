import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget
from PyQt5.QtCore import QFile,Qt
sys.path.append("C:\\Users\\Alex\\Desktop\\Nueva carpeta (2)\\Interfaces\\login\\")
from login import Ui_MainWindow
#sys.path.append("C:\\Users\\Juan Ignacio\\Desktop\\proyecto python\\Interfaces\\main\\")
sys.path.append("C:\\Users\\Alex\\Desktop\\Nueva carpeta (2)\\Interfaces\\main\\")
import main_func as m
#sys.path.append("C:\\Users\\Juan Ignacio\\Desktop\\proyecto python\\DB\\")
sys.path.append("C:\\Users\\Alex\\Desktop\\Nueva carpeta (2)\\DB\\")
import loginDB as l

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
            usuario = l.log_in(user,password)
            
            if usuario==1:
                #inicia
                self.main = m.Main()
                self.close()
            if usuario==2:
                #no se encuentra dni
                QtWidgets.QMessageBox.critical(self, "Error", "DNI Incorrecto")
                self.ui.user_login_input.setText("")
                self.ui.pass_login_input.setText("")
            if usuario==3:
                #contraseña incorrecta
                QtWidgets.QMessageBox.critical(self, "Error", "Contraseña Incorrecta")
                self.ui.pass_login_input.setText("")
