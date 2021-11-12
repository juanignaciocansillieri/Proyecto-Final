
import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import ingreso
from ingreso import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import movimientos as m
import lotes as l
import productos as p


class NewIngreso(QMainWindow):

    def __init__(self):
        super(NewIngreso, self).__init__()
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
        self.ui.crearprod_btn.clicked.connect(self.crearIngreso)
        
        

    def crearIngreso(self):
        tipo = False
        cantidad = self.ui.spinBox.value()
        lote = self.ui.motivo_input.text()
        cod = self.ui.codigo_producto_input.text()
        fechaIgreso = self.ui.fecha_date.date().toString("yyyy/MM/dd")
        venc = self.ui.fecha_date_2.date().toString("yyyy/MM/dd")
        codigo = p.productos.mostrar_product(cod)
        loteV = l.lote.verificar(lote)

        if codigo == "":
             QtWidgets.QMessageBox.critical(self, "Error", "Código Inexistente")
        if  loteV == 1:
             QtWidgets.QMessageBox.critical(self, "Error", "Lote Existente")
        else:
            l.lote(cod,cantidad,lote,venc)
            m.movimientos(tipo,cod,cantidad,"Ingreso",fechaIgreso)
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewIngreso()
    window.show()
    sys.exit(app.exec())