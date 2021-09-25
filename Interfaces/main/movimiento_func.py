
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
sys.path.append("C:\\proyecto-final\\CLASES\\")
import movimientos as m
import lotes as l

a=0
b = True
a = 0
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
        
        self.ui.crearprod_btn.clicked.connect(self.current)

    def current(self):
        global a
        if a == 0:
            a = 1
            self.crearIngreso()
        else: a=1


        self.ui.crearprod_btn.clicked.connect(self.current)

    def current(self):
        global a
        if a == 0:
            a = 1
            self.crearIngreso()
        else: a = 1
        
    def onSelected(self, txtVal):
        global b
        if txtVal == "Egreso":
            print("ates if egreso")
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
                self.ui.crearprod_btn.clicked.connect(self.crearEgreso)



        elif txtVal == "Ingreso":
            print("ates if ingreso")
            if  b == False:
                b = True
                self.ui.spinBox.setGeometry(QtCore.QRect(230, 160, 170, 25))
                self.ui.fecha_date_2.setGeometry(QtCore.QRect(230, 100, 170, 25))
                self.ui.label_fecha_2.setText("Fecha de Vencimiento")
                self.ui.label_motivo.setText("Lote")
                self.ui.crearprod_btn.clicked.connect(self.crearIngreso)

    def crearEgreso(self):
        tipo = True
        cantidad = self.ui.spinBox.value()
        motivo = self.ui.motivo_input.text()
        cod = self.ui.codigo_producto_input.text()
        fechaEgreso = self.ui.fecha_date.date().toString("yyyy/MM/dd")
        m.movimientos(tipo,cod,cantidad,motivo,fechaEgreso)
        l.lote.fifo(cod,cantidad)
        self.close()
        

    def crearIngreso(self):
        print("hola estoy aca")
        tipo = False
        cantidad = self.ui.spinBox.value()
        lote = self.ui.motivo_input.text()
        cod = self.ui.codigo_producto_input.text()
        fechaIgreso = self.ui.fecha_date.date().toString("yyyy/MM/dd")
        venc = self.ui.fecha_date_2.date().toString("yyyy/MM/dd")

        l.lote(cod,cantidad,lote,venc)
        m.movimientos(tipo,cod,cantidad,"Ingreso",fechaIgreso)
        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NewMovimiento()
    window.show()
    sys.exit(app.exec())