import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget
from PyQt5.QtCore import QFile,Qt
from login import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\DB\\")
import loginDB as l
import conexion as con
sys.path.append("C:\\proyecto-final\\CLASES\\")
import usuarios as u
sys.path.append("C:\\proyecto-final\\Interfaces\\main\\")
import modern_func as m

admin_user=True

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
            global admin_user
            user = self.ui.user_login_input.text()
            password = self.ui.pass_login_input.text()
            usuario = l.log_in(user,password)

            if user=="admin" and password=="admin":
                con.crear_tabla()
                self.main = m.Modern(1)
                self.close()

            if usuario==1:
                #inicia
                admin_user=u.ver_tipo(user)
                con.crear_tabla()
                self.close()
                self.main = m.Modern(admin_user)
            if usuario==2:
                #no se encuentra dni
                if user == "admin":
                    pass
                else:
                    QtWidgets.QMessageBox.critical(self, "Error", "DNI Incorrecto")
                    self.ui.user_login_input.setText("")
                    self.ui.pass_login_input.setText("")
            if usuario==3:
                #contraseña incorrecta
                QtWidgets.QMessageBox.critical(self, "Error", "Contraseña Incorrecta")
                self.ui.pass_login_input.setText("")
