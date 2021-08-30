import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import new
from new import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import productos as p

class New(QMainWindow):

    def __init__(self):
        super(New, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.toggle_btn.clicked.connect( lambda: self.toggle(130,True))
        self.ui.products_btn.clicked.connect(self.prrint)
        self.listarProductos()


    def toggle(self, maxWidth, enable):

        if enable:

            #GET WIDTH 
            width = self.ui.left_frame.width()
            maxExtend = maxWidth
            standard = 0

            #SET MAX WIDTH
            if width == 50:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            #ANIMACIÓN
        self.animation = QPropertyAnimation(self.ui.left_frame, b"minimumWidth")
        self.animation.setDuration(300)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()

    def listarProductos(self):
        products = p.listar_prod()
        n = p.contar_filas()
        self.ui.tableWidget.setRowCount(n)
        tableRow = 0
        for row in products:
            self.ui.tableWidget.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(
                tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = New()
    window.show()
    sys.exit(app.exec())