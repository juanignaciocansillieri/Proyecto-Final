import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import movimiento_ui
from movimiento_ui import Ui_MainWindow

b = True

class NewMovimiento(QMainWindow):

    def __init__(self):
        super(NewMovimiento, self).__init__()
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
        self.ui.egr_ing_cb.activated[str].connect(self.onSelected)
        self.lote = QtWidgets.QLineEdit(self.ui.frame_3)

    def onSelected(self, txtVal):
        global b
        if txtVal == "Egreso":
            if  b:
                b = False
                self.ui.spinBox.setGeometry(QtCore.QRect(230, 160, 170, 25))
                self.ui.fecha_date_2.setGeometry(QtCore.QRect(230, 100, 0, 0))
                self.ui.label_fecha_2.setText("")
                self.ui.label_fecha.setText("Fecha de Egreso")
                self.ui.label_cantidad.setText("Cantidad")
                self.ui.label_motivo.setText("Motivo")
                self.lote.setGeometry(QtCore.QRect(230, 100, 0, 0))
                self.lote.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")

        if txtVal == "Ingreso":
            if  b == False:
                b = True
                self.ui.spinBox.setGeometry(QtCore.QRect(230, 160, 170, 25))
                self.ui.fecha_date_2.setGeometry(QtCore.QRect(230, 100, 170, 25))
                self.ui.label_fecha_2.setText("Fecha de Vencimiento")
                self.ui.label_motivo.setText("Lote")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewMovimiento()
    window.show()
    sys.exit(app.exec())