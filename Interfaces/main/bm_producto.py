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
        MainWindow.resize(678, 578)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 209))
        self.frame.setStyleSheet("background: #fff;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 10, 231, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cct/Alimento.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setStyleSheet("background: #fff;\n"
                                   "")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 641, 291))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 400))
        self.frame_3.setStyleSheet("border-radius: 10px;\n"
                                   "background-color: rgb(240, 242, 255);\n"
                                   "")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.estado_label = QtWidgets.QLabel(self.frame_3)
        self.estado_label.setGeometry(QtCore.QRect(429, 80, 57, 27))
        self.estado_label.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.estado_label.setFont(font)
        self.estado_label.setStyleSheet("font-family: Roboto;\n"
                                        "font-size: 14px;\n"
                                        "margin-top:10px;\n"
                                        "margin-left:10px\n"
                                        "\n"
                                        "")
        self.estado_label.setObjectName("estado_label")
        self.fragil_label = QtWidgets.QLabel(self.frame_3)
        self.fragil_label.setGeometry(QtCore.QRect(429, 20, 56, 27))
        self.fragil_label.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.fragil_label.setFont(font)
        self.fragil_label.setStyleSheet("font-family: Roboto;\n"
                                        "font-size: 14px;\n"
                                        "margin-top:10px;\n"
                                        "margin-left:10px\n"
                                        "\n"
                                        "")
        self.fragil_label.setObjectName("fragil_label")
        self.fragil_si = QtWidgets.QRadioButton(self.frame_3)
        self.fragil_si.setGeometry(QtCore.QRect(442, 40, 41, 31))
        self.fragil_si.setStyleSheet("QRadioButton{\n"
                                     "border-radius: 3px;\n"
                                     "font-family: Roboto;\n"
                                     "font-size: 12px;\n"
                                     "border: none;\n"
                                     "font-weight: 400;\n"
                                     "margin-top:15px\n"
                                     "}\n"
                                     "")
        self.fragil_si.setObjectName("fragil_si")
        self.fragil_no = QtWidgets.QRadioButton(self.frame_3)
        self.fragil_no.setGeometry(QtCore.QRect(489, 40, 41, 31))
        self.fragil_no.setStyleSheet("QRadioButton{\n"
                                     "border-radius: 3px;\n"
                                     "font-family: Roboto;\n"
                                     "font-size: 12px;\n"
                                     "border: none;\n"
                                     "font-weight: 400;\n"
                                     "margin-top:15px\n"
                                     "}\n"
                                     "")
        self.fragil_no.setObjectName("fragil_no")
        self.estado_cbox = QtWidgets.QComboBox(self.frame_3)
        self.estado_cbox.setGeometry(QtCore.QRect(429, 110, 171, 25))
        self.estado_cbox.setStyleSheet("background-color: #fff;\n"
                                       "border-radius: 3px;\n"
                                       "padding: 4 5px;\n"
                                       "color: rgb(0, 0, 0);\n"
                                       "font-family:Roboto;\n"
                                       "border: none;\n"
                                       "font-size:13px;\n"
                                       "font-weight: 400;\n"
                                       "margin-left: 10px;\n"
                                       "")
        self.estado_cbox.setCurrentText("")
        self.estado_cbox.setMaxVisibleItems(10)
        self.estado_cbox.setMaxCount(10)
        self.estado_cbox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.estado_cbox.setIconSize(QtCore.QSize(16, 0))
        self.estado_cbox.setDuplicatesEnabled(False)
        self.estado_cbox.setFrame(False)
        self.estado_cbox.setObjectName("estado_cbox")
        self.subirFoto_btn = QtWidgets.QPushButton(self.frame_3)
        self.subirFoto_btn.setGeometry(QtCore.QRect(440, 230, 160, 25))
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
                                         "background-color: rgba(179,179,179,110);\n"
                                         "\n"
                                         "\n"
                                         "}")
        self.subirFoto_btn.setObjectName("subirFoto_btn")
        self.peso_num = QtWidgets.QSpinBox(self.frame_3)
        self.peso_num.setGeometry(QtCore.QRect(230, 230, 170, 25))
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
        self.peso_num.setMaximum(9999)
        self.peso_num.setObjectName("peso_num")
        self.largo_num = QtWidgets.QSpinBox(self.frame_3)
        self.largo_num.setGeometry(QtCore.QRect(230, 170, 170, 25))
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
        self.largo_num.setMaximum(9999)
        self.largo_num.setObjectName("largo_num")
        self.ancho_num = QtWidgets.QSpinBox(self.frame_3)
        self.ancho_num.setGeometry(QtCore.QRect(230, 110, 170, 25))
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
        self.ancho_num.setMaximum(9999)
        self.ancho_num.setObjectName("ancho_num")
        self.altura_num = QtWidgets.QSpinBox(self.frame_3)
        self.altura_num.setGeometry(QtCore.QRect(230, 50, 170, 25))
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
        self.altura_num.setMaximum(9999)
        self.altura_num.setObjectName("altura_num")
        self.ancho_label = QtWidgets.QLabel(self.frame_3)
        self.ancho_label.setGeometry(QtCore.QRect(229, 80, 90, 27))
        self.ancho_label.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.ancho_label.setFont(font)
        self.ancho_label.setStyleSheet("font-family: Roboto;\n"
                                       "font-size: 14px;\n"
                                       "margin-top:10px;\n"
                                       "margin-left:10px\n"
                                       "\n"
                                       "")
        self.ancho_label.setObjectName("ancho_label")
        self.altura_label = QtWidgets.QLabel(self.frame_3)
        self.altura_label.setGeometry(QtCore.QRect(229, 20, 90, 27))
        self.altura_label.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.altura_label.setFont(font)
        self.altura_label.setStyleSheet("font-family: Roboto;\n"
                                        "font-size: 14px;\n"
                                        "margin-top:10px;\n"
                                        "margin-left:10px\n"
                                        "\n"
                                        "")
        self.altura_label.setObjectName("altura_label")
        self.codigo_label = QtWidgets.QLabel(self.frame_3)
        self.codigo_label.setGeometry(QtCore.QRect(20, 20, 62, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.codigo_label.setFont(font)
        self.codigo_label.setStyleSheet("font-family: Roboto;\n"
                                        "font-size: 14px;\n"
                                        "margin-top:10px;\n"
                                        "margin-left:10px\n"
                                        "\n"
                                        "")
        self.codigo_label.setObjectName("codigo_label")
        self.codigo_input = QtWidgets.QLineEdit(self.frame_3)
        self.codigo_input.setGeometry(QtCore.QRect(20, 50, 170, 25))
        self.codigo_input.setMinimumSize(QtCore.QSize(0, 0))
        self.codigo_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.codigo_input.setStyleSheet("QLineEdit{\n"
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
                                        "}")
        self.codigo_input.setText("")
        self.codigo_input.setPlaceholderText("")
        self.codigo_input.setObjectName("codigo_input")
        self.peso_label = QtWidgets.QLabel(self.frame_3)
        self.peso_label.setGeometry(QtCore.QRect(229, 200, 71, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.peso_label.setFont(font)
        self.peso_label.setStyleSheet("font-family: Roboto;\n"
                                      "font-size: 14px;\n"
                                      "margin-top:10px;\n"
                                      "margin-left:10px\n"
                                      "\n"
                                      "")
        self.peso_label.setObjectName("peso_label")
        self.marca_input = QtWidgets.QLineEdit(self.frame_3)
        self.marca_input.setGeometry(QtCore.QRect(20, 230, 170, 25))
        self.marca_input.setMinimumSize(QtCore.QSize(0, 0))
        self.marca_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.marca_input.setStyleSheet("QLineEdit{\n"
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
                                       "}")
        self.marca_input.setPlaceholderText("")
        self.marca_input.setObjectName("marca_input")
        self.marca_label = QtWidgets.QLabel(self.frame_3)
        self.marca_label.setGeometry(QtCore.QRect(20, 200, 57, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.marca_label.setFont(font)
        self.marca_label.setStyleSheet("font-family: Roboto;\n"
                                       "font-size: 14px;\n"
                                       "margin-top:10px;\n"
                                       "margin-left:10px\n"
                                       "\n"
                                       "")
        self.marca_label.setObjectName("marca_label")
        self.largo_label = QtWidgets.QLabel(self.frame_3)
        self.largo_label.setGeometry(QtCore.QRect(229, 140, 90, 27))
        self.largo_label.setMaximumSize(QtCore.QSize(90, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.largo_label.setFont(font)
        self.largo_label.setStyleSheet("font-family: Roboto;\n"
                                       "font-size: 14px;\n"
                                       "margin-top:10px;\n"
                                       "margin-left:10px\n"
                                       "\n"
                                       "")
        self.largo_label.setObjectName("largo_label")
        self.descripcion_input = QtWidgets.QTextEdit(self.frame_3)
        self.descripcion_input.setGeometry(QtCore.QRect(20, 110, 170, 85))
        self.descripcion_input.setStyleSheet("background-color: #fff;\n"
                                             "border: 0.5px solid #c1c1c1;\n"
                                             "border-radius: 3px;\n"
                                             "padding: 4 5px;\n"
                                             "color: #e9e9;\n"
                                             "font-family:Roboto;\n"
                                             "font-size:13px;\n"
                                             "font-weight: 400;\n"
                                             "margin-left: 10px;\n"
                                             "")
        self.descripcion_input.setObjectName("descripcion_input")
        self.descripcion_label = QtWidgets.QLabel(self.frame_3)
        self.descripcion_label.setGeometry(QtCore.QRect(20, 80, 99, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.descripcion_label.setFont(font)
        self.descripcion_label.setStyleSheet("font-family: Roboto;\n"
                                             "font-size: 14px;\n"
                                             "margin-top:10px;\n"
                                             "margin-left:10px\n"
                                             "\n"
                                             "")
        self.descripcion_label.setObjectName("descripcion_label")
        self.ubicacion_label = QtWidgets.QLabel(self.frame_3)
        self.ubicacion_label.setGeometry(QtCore.QRect(429, 140, 84, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.ubicacion_label.setFont(font)
        self.ubicacion_label.setStyleSheet("font-family: Roboto;\n"
                                           "font-size: 14px;\n"
                                           "margin-top:10px;\n"
                                           "margin-left:10px\n"
                                           "\n"
                                           "")
        self.ubicacion_label.setObjectName("ubicacion_label")
        self.ubicacion_cbox = QtWidgets.QComboBox(self.frame_3)
        self.ubicacion_cbox.setGeometry(QtCore.QRect(430, 180, 171, 25))
        self.ubicacion_cbox.setStyleSheet("background-color: #fff;\n"
                                          "border-radius: 3px;\n"
                                          "padding: 4 5px;\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "font-family:Roboto;\n"
                                          "border: none;\n"
                                          "font-size:13px;\n"
                                          "font-weight: 400;\n"
                                          "margin-left: 10px;\n"
                                          "")
        self.ubicacion_cbox.setCurrentText("")
        self.ubicacion_cbox.setMaxVisibleItems(10)
        self.ubicacion_cbox.setMaxCount(10)
        self.ubicacion_cbox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.ubicacion_cbox.setIconSize(QtCore.QSize(16, 0))
        self.ubicacion_cbox.setDuplicatesEnabled(False)
        self.ubicacion_cbox.setFrame(False)
        self.ubicacion_cbox.setObjectName("ubicacion_cbox")
        self.modificarprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.modificarprod_btn.setGeometry(QtCore.QRect(380, 320, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.modificarprod_btn.setFont(font)
        self.modificarprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modificarprod_btn.setStyleSheet("QPushButton{\n"
                                             "background-color: rgb(71, 71, 103);\n"
                                             "\n"
                                             "color: #fff;\n"
                                             "border-radius:10px;\n"
                                             "font-family:Roboto;\n"
                                             "font-size: 13px\n"
                                             "\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "background-color: rgba(71, 71, 103,180);\n"
                                             "\n"
                                             "}")
        self.modificarprod_btn.setObjectName("modificarprod_btn")
        self.eliminarprod_btn = QtWidgets.QPushButton(self.frame_2)
        self.eliminarprod_btn.setGeometry(QtCore.QRect(520, 320, 121, 26))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.eliminarprod_btn.setFont(font)
        self.eliminarprod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eliminarprod_btn.setStyleSheet("QPushButton{\n"
                                            "background-color: rgb(71, 71, 103);\n"
                                            "\n"
                                            "color: #fff;\n"
                                            "border-radius:10px;\n"
                                            "font-family:Roboto;\n"
                                            "font-size: 13px\n"
                                            "\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "background-color: rgba(71, 71, 103,180);\n"
                                            "\n"
                                            "}")
        self.eliminarprod_btn.setObjectName("eliminarprod_btn")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.estado_cbox.setCurrentIndex(-1)
        self.ubicacion_cbox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Producto"))
        self.estado_label.setText(_translate("MainWindow", "??rea"))
        self.fragil_label.setText(_translate("MainWindow", "Fragil"))
        self.fragil_si.setText(_translate("MainWindow", "Si"))
        self.fragil_no.setText(_translate("MainWindow", "No"))
        self.subirFoto_btn.setText(_translate("MainWindow", "Actualizar Imagen"))
        self.ancho_label.setText(_translate("MainWindow", "Ancho (cm)"))
        self.altura_label.setText(_translate("MainWindow", "Altura (cm)"))
        self.codigo_label.setText(_translate("MainWindow", "C??digo"))
        self.peso_label.setText(_translate("MainWindow", "Peso (gr)"))
        self.marca_label.setText(_translate("MainWindow", "Marca"))
        self.largo_label.setText(_translate("MainWindow", "Largo (cm)"))
        self.descripcion_label.setText(_translate("MainWindow", "Descripci??n"))
        self.ubicacion_label.setText(_translate("MainWindow", "Ubicaci??n"))
        self.modificarprod_btn.setText(_translate("MainWindow", "Modificar Producto"))
        self.eliminarprod_btn.setText(_translate("MainWindow", "Eliminar Producto"))
from Interfaces.main import img_oficiales_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
