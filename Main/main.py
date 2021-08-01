import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import * 

#GUI File
from ui_main import Ui_MainWindow

#Import Functions 
from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    ## Toggle / Burguer menú
    self.ui.Btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

    ## Show main window
    self.show
    ## --> End 


## if __name__ == "__main__":  
##    app = QApplication(sys.argv)
##    window = MainWindow()
##    sys.exit(app.exec_()) 