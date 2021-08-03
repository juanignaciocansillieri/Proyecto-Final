import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDesktopWidget
from PyQt5.QtCore import QFile,Qt


class Functions():
        def centrarPantalla(self):
############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
            qtRectangle = self.frameGeometry()
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle.moveCenter(centerPoint)
            self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
            centerPoint = QDesktopWidget().availableGeometry().center()
            qtRectangle.moveCenter(centerPoint)
            self.move(qtRectangle.topLeft())