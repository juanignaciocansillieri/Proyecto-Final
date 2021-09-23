# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nuevo_producto_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #fff;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(30, 30, 611, 321))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(240, 242, 255);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_cantidad = QtWidgets.QLabel(self.frame_3)
        self.label_cantidad.setGeometry(QtCore.QRect(420, 10, 158, 27))
        self.label_cantidad.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_cantidad.setFont(font)
        self.label_cantidad.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_cantidad.setObjectName("label_cantidad")
        self.label_ancho = QtWidgets.QLabel(self.frame_3)
        self.label_ancho.setGeometry(QtCore.QRect(229, 70, 90, 27))
        self.label_ancho.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_ancho.setFont(font)
        self.label_ancho.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #000;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_ancho.setObjectName("label_ancho")
        self.label_ubicacion = QtWidgets.QLabel(self.frame_3)
        self.label_ubicacion.setGeometry(QtCore.QRect(20, 70, 91, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_ubicacion.setFont(font)
        self.label_ubicacion.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_ubicacion.setObjectName("label_ubicacion")
        self.label_altura = QtWidgets.QLabel(self.frame_3)
        self.label_altura.setGeometry(QtCore.QRect(229, 10, 90, 27))
        self.label_altura.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_altura.setFont(font)
        self.label_altura.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_altura.setObjectName("label_altura")
        self.label_codigo = QtWidgets.QLabel(self.frame_3)
        self.label_codigo.setGeometry(QtCore.QRect(20, 10, 101, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_codigo.setFont(font)
        self.label_codigo.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_codigo.setObjectName("label_codigo")
        self.codigo_input = QtWidgets.QLineEdit(self.frame_3)
        self.codigo_input.setGeometry(QtCore.QRect(20, 40, 170, 25))
        self.codigo_input.setMinimumSize(QtCore.QSize(0, 0))
        self.codigo_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.codigo_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.codigo_input.setText("")
        self.codigo_input.setPlaceholderText("")
        self.codigo_input.setObjectName("codigo_input")
        self.label_lote = QtWidgets.QLabel(self.frame_3)
        self.label_lote.setGeometry(QtCore.QRect(230, 250, 154, 27))
        self.label_lote.setMaximumSize(QtCore.QSize(154, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_lote.setFont(font)
        self.label_lote.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_lote.setObjectName("label_lote")
        self.label_peso = QtWidgets.QLabel(self.frame_3)
        self.label_peso.setGeometry(QtCore.QRect(230, 190, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_peso.setFont(font)
        self.label_peso.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_peso.setObjectName("label_peso")
        self.label_marca = QtWidgets.QLabel(self.frame_3)
        self.label_marca.setGeometry(QtCore.QRect(20, 190, 100, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_marca.setFont(font)
        self.label_marca.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_marca.setObjectName("label_marca")
        self.label_largo = QtWidgets.QLabel(self.frame_3)
        self.label_largo.setGeometry(QtCore.QRect(229, 130, 90, 27))
        self.label_largo.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_largo.setFont(font)
        self.label_largo.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_largo.setObjectName("label_largo")
        self.lote_input = QtWidgets.QLineEdit(self.frame_3)
        self.lote_input.setGeometry(QtCore.QRect(230, 280, 170, 25))
        self.lote_input.setMinimumSize(QtCore.QSize(0, 0))
        self.lote_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lote_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #e9e9;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.lote_input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lote_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lote_input.setPlaceholderText("")
        self.lote_input.setObjectName("lote_input")
        self.peso_num = QtWidgets.QSpinBox(self.frame_3)
        self.peso_num.setGeometry(QtCore.QRect(230, 220, 170, 25))
        self.peso_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.peso_num.setMinimum(0)
        self.peso_num.setMaximum(9999)
        self.peso_num.setObjectName("peso_num")
        self.altura_num = QtWidgets.QSpinBox(self.frame_3)
        self.altura_num.setGeometry(QtCore.QRect(230, 40, 170, 25))
        self.altura_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.altura_num.setMinimum(0)
        self.altura_num.setMaximum(9999)
        self.altura_num.setObjectName("altura_num")
        self.ancho_num = QtWidgets.QSpinBox(self.frame_3)
        self.ancho_num.setGeometry(QtCore.QRect(230, 100, 170, 25))
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
        self.ancho_num.setMaximum(9999)
        self.ancho_num.setObjectName("ancho_num")
        self.largo_num = QtWidgets.QSpinBox(self.frame_3)
        self.largo_num.setGeometry(QtCore.QRect(230, 160, 170, 25))
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
        self.cantidad_num = QtWidgets.QSpinBox(self.frame_3)
        self.cantidad_num.setGeometry(QtCore.QRect(420, 40, 170, 25))
        self.cantidad_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.cantidad_num.setMinimum(0)
        self.cantidad_num.setMaximum(9999)
        self.cantidad_num.setObjectName("cantidad_num")
        self.label_fragil = QtWidgets.QLabel(self.frame_3)
        self.label_fragil.setGeometry(QtCore.QRect(420, 70, 90, 27))
        self.label_fragil.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_fragil.setFont(font)
        self.label_fragil.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_fragil.setObjectName("label_fragil")
        self.fragil_si = QtWidgets.QRadioButton(self.frame_3)
        self.fragil_si.setGeometry(QtCore.QRect(430, 100, 31, 21))
        self.fragil_si.setIconSize(QtCore.QSize(30, 30))
        self.fragil_si.setObjectName("fragil_si")
        self.fragil_no = QtWidgets.QRadioButton(self.frame_3)
        self.fragil_no.setGeometry(QtCore.QRect(460, 100, 31, 21))
        self.fragil_no.setIconSize(QtCore.QSize(30, 30))
        self.fragil_no.setObjectName("fragil_no")
        self.label_area = QtWidgets.QLabel(self.frame_3)
        self.label_area.setGeometry(QtCore.QRect(420, 130, 90, 27))
        self.label_area.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_area.setFont(font)
        self.label_area.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_area.setObjectName("label_area")
        self.area_comboBox = QtWidgets.QComboBox(self.frame_3)
        self.area_comboBox.setGeometry(QtCore.QRect(420, 160, 170, 22))
        self.area_comboBox.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.area_comboBox.setObjectName("area_comboBox")
        self.label_vencimiento = QtWidgets.QLabel(self.frame_3)
        self.label_vencimiento.setGeometry(QtCore.QRect(20, 250, 151, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_vencimiento.setFont(font)
        self.label_vencimiento.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_vencimiento.setObjectName("label_vencimiento")
        self.venc_date = QtWidgets.QDateEdit(self.frame_3)
        self.venc_date.setGeometry(QtCore.QRect(20, 280, 170, 25))
        self.venc_date.setStyleSheet("\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #000;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"")
        self.venc_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.venc_date.setObjectName("venc_date")
        self.marca_input = QtWidgets.QLineEdit(self.frame_3)
        self.marca_input.setGeometry(QtCore.QRect(20, 220, 170, 25))
        self.marca_input.setMinimumSize(QtCore.QSize(0, 0))
        self.marca_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.marca_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.marca_input.setPlaceholderText("")
        self.marca_input.setObjectName("marca_input")
        self.label_ubicacion_2 = QtWidgets.QLabel(self.frame_3)
        self.label_ubicacion_2.setGeometry(QtCore.QRect(420, 190, 91, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_ubicacion_2.setFont(font)
        self.label_ubicacion_2.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_ubicacion_2.setObjectName("label_ubicacion_2")
        self.ubicacion_input = QtWidgets.QLineEdit(self.frame_3)
        self.ubicacion_input.setGeometry(QtCore.QRect(420, 220, 170, 25))
        self.ubicacion_input.setMinimumSize(QtCore.QSize(0, 0))
        self.ubicacion_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.ubicacion_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.ubicacion_input.setPlaceholderText("")
        self.ubicacion_input.setObjectName("ubicacion_input")
        self.descripcion_input = QtWidgets.QLineEdit(self.frame_3)
        self.descripcion_input.setGeometry(QtCore.QRect(20, 100, 170, 75))
        self.descripcion_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.descripcion_input.setObjectName("descripcion_input")
        self.subirFoto_btn = QtWidgets.QPushButton(self.frame_3)
        self.subirFoto_btn.setGeometry(QtCore.QRect(435, 280, 150, 25))
        self.subirFoto_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.subirFoto_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subirFoto_btn.setStyleSheet("QPushButton{\n"
"background-color: rgba(71, 71, 103,180);\n"
"border-radius: 7px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 500;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(71, 71, 103);\n"
"color: #fff;\n"
"\n"
"}")
        self.subirFoto_btn.setObjectName("subirFoto_btn")
        self.crearprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.crearprod_btn.setGeometry(QtCore.QRect(460, 360, 150, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.crearprod_btn.setFont(font)
        self.crearprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crearprod_btn.setStyleSheet("QPushButton{\n"
"background-color: rgba(71, 71, 103);\n"
"color: #fff;\n"
"border-radius:5px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(71, 71, 103,180);\n"
"}")
        self.crearprod_btn.setObjectName("crearprod_btn")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_cantidad.setText(_translate("MainWindow", "Cantidad"))
        self.label_ancho.setText(_translate("MainWindow", "Ancho (cm)"))
        self.label_ubicacion.setText(_translate("MainWindow", "Descripción"))
        self.label_altura.setText(_translate("MainWindow", "Altura (cm)"))
        self.label_codigo.setText(_translate("MainWindow", "Código"))
        self.label_lote.setText(_translate("MainWindow", "Lote"))
        self.label_peso.setText(_translate("MainWindow", "Peso (g)"))
        self.label_marca.setText(_translate("MainWindow", "Marca"))
        self.label_largo.setText(_translate("MainWindow", "Largo (cm)"))
        self.label_fragil.setText(_translate("MainWindow", "Frágil"))
        self.fragil_si.setText(_translate("MainWindow", "SI"))
        self.fragil_no.setText(_translate("MainWindow", "NO"))
        self.label_area.setText(_translate("MainWindow", "Área"))
        self.label_vencimiento.setText(_translate("MainWindow", "Fecha De Vencimiento"))
        self.label_ubicacion_2.setText(_translate("MainWindow", "Ubicación"))
        self.subirFoto_btn.setText(_translate("MainWindow", "Subir Imagen"))
        self.crearprod_btn.setText(_translate("MainWindow", "Crear producto"))
import img_oficiales_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())