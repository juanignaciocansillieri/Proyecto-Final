import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Interfaces.loading import circularProgress as c, splash
import CLASES
import DB
from Interfaces.login import login_funcional as l

counter = 0


class Splash(QMainWindow):
    a = 0

    def __init__(self):
        super(Splash, self).__init__()
        self.ui = splash.Ui_MainWindow()
        self.ui.setupUi(self)
        ######## SACAR BARRA DE TÍTULO#####################
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        ############### ESTILO ################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        ###### INSERTAR CÍRCULO DE PROGRESO##############
        self.circle = c.CircularProgress()
        self.ui.horizontalLayout_3.addWidget(self.circle)
        ###### CERRAR SPLASH #############
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)

        def timerEvent():
            global time
            self.time = self.time.addSecs(1)
            if str(self.time) == "PyQt5.QtCore.QTime(0, 0, 7)":
<<<<<<< HEAD
                DB.conexion.crear_tabla()
                self.close()

                s = CLASES.usuarios.contar_filas()
                if s == 0:
                    CLASES.usuarios.Usuarios("admin", "admin", "admin", "1", "admin", "2021-01-01", "admin", "Error.png")
                    DB.loginDB.alta_login("admin", "admin")
=======
                conexion.crear_tabla()
                self.close()
                ###
                s=u.ver_dni("admin")
                if s==0:
                    u.usuarios("admin","admin","admin","1","admin","2021-01-01","admin","Error.png")
                    loginDB.alta_login("admin","admin")
>>>>>>> 6107d44b37fb4b2aa509d902e4b00c803bf63ac1

                ###
                self.login = l.LoginWindow()

        self.timer.timeout.connect(timerEvent)
        self.timer.start(1000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Splash()
    window.show()
    sys.exit(app.exec())
