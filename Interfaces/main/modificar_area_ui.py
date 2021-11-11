# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificar_area.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 329)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 551, 330))
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #fff;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(50, 30, 391, 271))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(240, 242, 255);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 62, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.modificar_btn = QtWidgets.QPushButton(self.frame_3)
        self.modificar_btn.setGeometry(QtCore.QRect(230, 230, 111, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.modificar_btn.setFont(font)
        self.modificar_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificar_btn.setStyleSheet("QPushButton{\n"
"background-color: rgb(71, 71, 103);\n"
"color: #fff;\n"
"border-radius:5px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(71, 71, 103,180);\n"
"}")
        self.modificar_btn.setObjectName("modificar_btn")
        self.label_Area = QtWidgets.QLabel(self.frame_3)
        self.label_Area.setGeometry(QtCore.QRect(20, 10, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_Area.setFont(font)
        self.label_Area.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_Area.setObjectName("label_Area")
        self.label_pasillo = QtWidgets.QLabel(self.frame_3)
        self.label_pasillo.setGeometry(QtCore.QRect(20, 200, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_pasillo.setFont(font)
        self.label_pasillo.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_pasillo.setObjectName("label_pasillo")
        self.label_segmento = QtWidgets.QLabel(self.frame_3)
        self.label_segmento.setGeometry(QtCore.QRect(220, 10, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_segmento.setFont(font)
        self.label_segmento.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_segmento.setObjectName("label_segmento")
        self.label_alto = QtWidgets.QLabel(self.frame_3)
        self.label_alto.setGeometry(QtCore.QRect(220, 130, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_alto.setFont(font)
        self.label_alto.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_alto.setObjectName("label_alto")
        self.label_ancho = QtWidgets.QLabel(self.frame_3)
        self.label_ancho.setGeometry(QtCore.QRect(220, 70, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_ancho.setFont(font)
        self.label_ancho.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_ancho.setObjectName("label_ancho")
        self.alto_num = QtWidgets.QSpinBox(self.frame_3)
        self.alto_num.setGeometry(QtCore.QRect(220, 160, 121, 25))
        self.alto_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.alto_num.setMinimum(0)
        self.alto_num.setMaximum(999)
        self.alto_num.setObjectName("alto_num")
        self.ancho_num = QtWidgets.QSpinBox(self.frame_3)
        self.ancho_num.setGeometry(QtCore.QRect(220, 100, 121, 25))
        self.ancho_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.ancho_num.setMinimum(0)
        self.ancho_num.setMaximum(999)
        self.ancho_num.setObjectName("ancho_num")
        self.label_longitud = QtWidgets.QLabel(self.frame_3)
        self.label_longitud.setGeometry(QtCore.QRect(20, 130, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_longitud.setFont(font)
        self.label_longitud.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_longitud.setObjectName("label_longitud")
        self.largo_num = QtWidgets.QSpinBox(self.frame_3)
        self.largo_num.setGeometry(QtCore.QRect(20, 160, 121, 25))
        self.largo_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.largo_num.setMinimum(0)
        self.largo_num.setMaximum(999)
        self.largo_num.setObjectName("largo_num")
        self.nombre_input = QtWidgets.QLineEdit(self.frame_3)
        self.nombre_input.setGeometry(QtCore.QRect(20, 40, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        font.setBold(True)
        font.setWeight(75)
        self.nombre_input.setFont(font)
        self.nombre_input.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"margin-left: 10px;\n"
"")
        self.nombre_input.setReadOnly(True)
        self.nombre_input.setObjectName("nombre_input")
        self.segmento_num = QtWidgets.QSpinBox(self.frame_3)
        self.segmento_num.setGeometry(QtCore.QRect(220, 40, 121, 25))
        self.segmento_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.segmento_num.setMinimum(0)
        self.segmento_num.setMaximum(999)
        self.segmento_num.setObjectName("segmento_num")
        self.pasillo_num = QtWidgets.QSpinBox(self.frame_3)
        self.pasillo_num.setGeometry(QtCore.QRect(20, 230, 121, 25))
        self.pasillo_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.pasillo_num.setMinimum(0)
        self.pasillo_num.setMaximum(999)
        self.pasillo_num.setObjectName("pasillo_num")
        self.identificador_input = QtWidgets.QLineEdit(self.frame_3)
        self.identificador_input.setGeometry(QtCore.QRect(20, 100, 121, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.identificador_input.setFont(font)
        self.identificador_input.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"margin-left: 10px;\n"
"")
        self.identificador_input.setText("")
        self.identificador_input.setReadOnly(False)
        self.identificador_input.setObjectName("identificador_input")
        self.label_Area_2 = QtWidgets.QLabel(self.frame_3)
        self.label_Area_2.setGeometry(QtCore.QRect(20, 70, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(1)
        self.label_Area_2.setFont(font)
        self.label_Area_2.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_Area_2.setObjectName("label_Area_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Modificar", "Modificar"))
        self.modificar_btn.setText(_translate("MainWindow", "Modificar"))
        self.label_Area.setText(_translate("MainWindow", "Nombre"))
        self.label_pasillo.setText(_translate("MainWindow", "Pasillos"))
        self.label_segmento.setText(_translate("MainWindow", "Segmentos"))
        self.label_alto.setText(_translate("MainWindow", "Alto"))
        self.label_ancho.setText(_translate("MainWindow", "Ancho"))
        self.label_longitud.setText(_translate("MainWindow", "Longitud"))
        self.label_Area_2.setText(_translate("MainWindow", "Identificador"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
