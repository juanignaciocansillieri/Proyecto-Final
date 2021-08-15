# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bm_producto_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(662, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 231))
        self.frame.setStyleSheet("background: #1a1e23;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 20, 221, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cct/Alimento.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #1a1e23;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 620, 288))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 314))
        self.frame_3.setStyleSheet("background: #12151a;\n"
"border-radius: 10px;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(429, 71, 57, 27))
        self.label_19.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(429, 7, 56, 27))
        self.label_20.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame_3)
        self.label_21.setGeometry(QtCore.QRect(429, 199, 154, 27))
        self.label_21.setMaximumSize(QtCore.QSize(154, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.frame_3)
        self.label_22.setGeometry(QtCore.QRect(429, 135, 158, 27))
        self.label_22.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_22.setObjectName("label_22")
        self.fragil_si = QtWidgets.QRadioButton(self.frame_3)
        self.fragil_si.setGeometry(QtCore.QRect(442, 22, 41, 41))
        self.fragil_si.setStyleSheet("QRadioButton{\n"
"border-radius: 3px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"}\n"
"")
        self.fragil_si.setObjectName("fragil_si")
        self.fragil_no = QtWidgets.QRadioButton(self.frame_3)
        self.fragil_no.setGeometry(QtCore.QRect(489, 22, 41, 41))
        self.fragil_no.setStyleSheet("QRadioButton{\n"
"border-radius: 3px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"}\n"
"")
        self.fragil_no.setObjectName("fragil_no")
        self.condicion_cbox = QtWidgets.QComboBox(self.frame_3)
        self.condicion_cbox.setGeometry(QtCore.QRect(439, 104, 161, 25))
        self.condicion_cbox.setStyleSheet("padding:0 5px;\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"color: #fff;\n"
"font-family:Roboto Lt;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"")
        self.condicion_cbox.setMaxVisibleItems(5)
        self.condicion_cbox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.condicion_cbox.setIconSize(QtCore.QSize(16, 0))
        self.condicion_cbox.setDuplicatesEnabled(False)
        self.condicion_cbox.setFrame(False)
        self.condicion_cbox.setObjectName("condicion_cbox")
        self.condicion_cbox.addItem("")
        self.condicion_cbox.addItem("")
        self.condicion_cbox.addItem("")
        self.condicion_cbox.addItem("")
        self.condicion_cbox.addItem("")
        self.condicion_cbox.setItemText(4, "")
        self.subirFoto_btn = QtWidgets.QPushButton(self.frame_3)
        self.subirFoto_btn.setGeometry(QtCore.QRect(440, 232, 157, 25))
        self.subirFoto_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.subirFoto_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subirFoto_btn.setStyleSheet("QPushButton{\n"
"background-color: #b3b3b3;\n"
"border-radius: 7px;\n"
"padding: 4 10px;\n"
"color: #12151a;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 500;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,50);\n"
"color: #fff;\n"
"\n"
"}")
        self.subirFoto_btn.setObjectName("subirFoto_btn")
        self.venc_date = QtWidgets.QDateEdit(self.frame_3)
        self.venc_date.setGeometry(QtCore.QRect(430, 168, 170, 25))
        self.venc_date.setStyleSheet("\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto lt;\n"
"border: none;\n"
"font-size:13px;\n"
"margin-left: 10px;")
        self.venc_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2021, 1, 1), QtCore.QTime(0, 0, 0)))
        self.venc_date.setObjectName("venc_date")
        self.peso_num = QtWidgets.QSpinBox(self.frame_3)
        self.peso_num.setGeometry(QtCore.QRect(20, 230, 170, 25))
        self.peso_num.setStyleSheet("background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.peso_num.setObjectName("peso_num")
        self.cantidad_num = QtWidgets.QSpinBox(self.frame_3)
        self.cantidad_num.setGeometry(QtCore.QRect(229, 168, 170, 25))
        self.cantidad_num.setStyleSheet("background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.cantidad_num.setObjectName("cantidad_num")
        self.ancho_num = QtWidgets.QSpinBox(self.frame_3)
        self.ancho_num.setGeometry(QtCore.QRect(230, 104, 170, 25))
        self.ancho_num.setStyleSheet("background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.ancho_num.setObjectName("ancho_num")
        self.altura_num = QtWidgets.QSpinBox(self.frame_3)
        self.altura_num.setGeometry(QtCore.QRect(230, 40, 170, 25))
        self.altura_num.setStyleSheet("background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.altura_num.setObjectName("altura_num")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(229, 71, 57, 27))
        self.label_8.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_8.setObjectName("label_8")
        self.nombre_input = QtWidgets.QLineEdit(self.frame_3)
        self.nombre_input.setGeometry(QtCore.QRect(20, 104, 170, 25))
        self.nombre_input.setMinimumSize(QtCore.QSize(0, 0))
        self.nombre_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.nombre_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}")
        self.nombre_input.setPlaceholderText("")
        self.nombre_input.setObjectName("nombre_input")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(20, 71, 67, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(229, 7, 56, 27))
        self.label_7.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_7.setObjectName("label_7")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(20, 7, 62, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.codigo_input = QtWidgets.QLineEdit(self.frame_3)
        self.codigo_input.setGeometry(QtCore.QRect(20, 40, 170, 25))
        self.codigo_input.setMinimumSize(QtCore.QSize(0, 0))
        self.codigo_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.codigo_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.codigo_input.setText("")
        self.codigo_input.setPlaceholderText("")
        self.codigo_input.setObjectName("codigo_input")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(229, 199, 154, 27))
        self.label_10.setMaximumSize(QtCore.QSize(154, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_10.setObjectName("label_10")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 199, 51, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.marca_input = QtWidgets.QLineEdit(self.frame_3)
        self.marca_input.setGeometry(QtCore.QRect(20, 168, 170, 25))
        self.marca_input.setMinimumSize(QtCore.QSize(0, 0))
        self.marca_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.marca_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.marca_input.setPlaceholderText("")
        self.marca_input.setObjectName("marca_input")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(20, 135, 57, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(229, 135, 75, 27))
        self.label_9.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"color: #fff;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_9.setObjectName("label_9")
        self.lote_num = QtWidgets.QSpinBox(self.frame_3)
        self.lote_num.setGeometry(QtCore.QRect(230, 230, 170, 25))
        self.lote_num.setStyleSheet("background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.lote_num.setObjectName("lote_num")
        self.crearprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.crearprod_btn.setGeometry(QtCore.QRect(380, 320, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.crearprod_btn.setFont(font)
        self.crearprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crearprod_btn.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.crearprod_btn.setObjectName("crearprod_btn")
        self.crearprod_btn_2 = QtWidgets.QPushButton(self.frame_2)
        self.crearprod_btn_2.setGeometry(QtCore.QRect(520, 320, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.crearprod_btn_2.setFont(font)
        self.crearprod_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crearprod_btn_2.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"font-family:Roboto;\n"
"font-size: 13px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.crearprod_btn_2.setObjectName("crearprod_btn_2")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.condicion_cbox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_19.setText(_translate("MainWindow", "Estado"))
        self.label_20.setText(_translate("MainWindow", "Fragil"))
        self.label_21.setText(_translate("MainWindow", "Imagen"))
        self.label_22.setText(_translate("MainWindow", "Fecha de Vencimiento"))
        self.fragil_si.setText(_translate("MainWindow", "Si"))
        self.fragil_no.setText(_translate("MainWindow", "No"))
        self.condicion_cbox.setCurrentText(_translate("MainWindow", "Ninguna"))
        self.condicion_cbox.setItemText(0, _translate("MainWindow", "Ninguna"))
        self.condicion_cbox.setItemText(1, _translate("MainWindow", "Refrigerado"))
        self.condicion_cbox.setItemText(2, _translate("MainWindow", "Inflamable"))
        self.condicion_cbox.setItemText(3, _translate("MainWindow", "No Perecedero"))
        self.subirFoto_btn.setText(_translate("MainWindow", "Subir Imagen"))
        self.label_8.setText(_translate("MainWindow", "Ancho"))
        self.label_4.setText(_translate("MainWindow", "Nombre"))
        self.label_7.setText(_translate("MainWindow", "Altura"))
        self.label_3.setText(_translate("MainWindow", "Código"))
        self.label_10.setText(_translate("MainWindow", "Lote"))
        self.label_6.setText(_translate("MainWindow", "Peso "))
        self.label_5.setText(_translate("MainWindow", "Marca"))
        self.label_9.setText(_translate("MainWindow", "Cantidad"))
        self.crearprod_btn.setText(_translate("MainWindow", "Modificar Producto"))
        self.crearprod_btn_2.setText(_translate("MainWindow", "Eliminar Producto"))
import img_oficiales_rc