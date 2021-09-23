import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from numpy import pi
import splash
import Img.img
import circularProgress as c
sys.path.append("C:\\proyecto-final\\DB\\")
import conexion as conexion
sys.path.append("C:\\proyecto-final\\Interfaces\\login\\")
import login_funcional as l
sys.path.append("C:\\proyecto-final\\Interfaces\\main\\")
import main_func as m


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
        print(self.circle.timer.duration)
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)

        def timerEvent():
            global time
            self.time = self.time.addSecs(1)
            if str(self.time) == "PyQt5.QtCore.QTime(0, 0, 1)":
                self.close()
                conexion.crear_tabla()
                #self.login = l.LoginWindow()
                self.m = m.Main(1)
        self.timer.timeout.connect(timerEvent)
        self.timer.start(1000)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Splash()
    window.show()
    sys.exit(app.exec())