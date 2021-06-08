from gui import MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from gui import *
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.saveGeometry(200,200,300,300)

    

def window():
    app=QApplication(sys.argv)
    win=MainWindow()

    win.show()
    sys.exit(app.exec())
window()        