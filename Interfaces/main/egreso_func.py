
import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import egreso
from egreso import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import movimientos as m
import lotes as l


class NewEgreso(QMainWindow):

    def __init__(self):
        super(NewEgreso, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.ui.crear_egreso.clicked.connect(self.crearEgreso)
        

    def crearEgreso(self):
        tipo = True
        cantidad = self.ui.cantidad.value()
        motivo = self.ui.motivo_input_2.text()
        cod = self.ui.codigo_producto_input_2.text()
        fechaEgreso = self.ui.fecha_egreso.date().toString("yyyy/MM/dd")
        m.movimientos(tipo,cod,cantidad,motivo,fechaEgreso)
        l.lote.fifo(cod,cantidad)
        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewEgreso()
    window.show()
    sys.exit(app.exec())