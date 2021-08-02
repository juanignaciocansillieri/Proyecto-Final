import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import * 

#GUI File
from main import Ui_MainWindow

#Import Functions 
from toggleFunction import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()


        ###################### ABRIR/CERRAR BARRA LATERAL #########################
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 100, True))

        ## PAGINAS ##

        # PRODUCTOS 
        self.ui.btn_productos.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_productos))
        self.ui.label_productos.mousePressEvent = self.clickP
        # DEPOSITO 
        self.ui.btn_depositos.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_depositos))
        self.ui.label_deposito.mousePressEvent = self.clickD
        # Usuarios 
        self.ui.btn_usuarios.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_usuarios))
        self.ui.label_usuarios.mousePressEvent = self.clickU
        # Boton Exit
        self.ui.btn_exit.clicked.connect(self.close)
        
    def clickP(self,event): 
       return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_productos)
        
    def clickD(self,event): 
       return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_depositos)
        
    def clickU(self,event): 
       return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_usuarios)


    

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_()) 