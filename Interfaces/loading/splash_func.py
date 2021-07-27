import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import splash
import Img.img
from circuloProgress import CircularProgress 
sys.path.append("C:\\Users\\Juan Ignacio\\Desktop\\proyecto python\\Interfaces\\login\\")
import login_funcional
class Splash(QMainWindow):
    counter = 0
    def __init__(self):
        super(Splash, self).__init__()
        self.ui = splash.Ui_MainWindow()
        self.ui.setupUi(self)
        self.a = login_funcional.LoginWindow()

        ######## SACAR BARRA DE TÍTULO#####################
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        ############### ESTILO ################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0,0,0,60))
        ###### INSERTAR CÍRCULO DE PROGRESO##############
        self.circle = CircularProgress()        
        self.ui.horizontalLayout_3.addWidget(self.circle)
        
        
        print(self.circle.counter) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Splash()
    window.show()
    sys.exit(app.exec())
