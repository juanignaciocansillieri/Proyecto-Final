# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 640)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(749, 800))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 640))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 640))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(400, 640))
        self.frame.setMaximumSize(QtCore.QSize(400, 640))
        self.frame.setStyleSheet(" background-color: #1a1e23;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(20, 10, 400, 640))
        self.frame_3.setMinimumSize(QtCore.QSize(400, 640))
        self.frame_3.setMaximumSize(QtCore.QSize(400, 640))
        self.frame_3.setStyleSheet("background-color: #12151a;\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, -20, 351, 591))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 22, 0, 3)
        self.formLayout.setHorizontalSpacing(38)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:5px")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.nombre_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.nombre_input.setMinimumSize(QtCore.QSize(0, 10))
        self.nombre_input.setMaximumSize(QtCore.QSize(300, 20))
        self.nombre_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.nombre_input.setPlaceholderText("")
        self.nombre_input.setObjectName("nombre_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.nombre_input)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.nac_date = QtWidgets.QDateEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nac_date.sizePolicy().hasHeightForWidth())
        self.nac_date.setSizePolicy(sizePolicy)
        self.nac_date.setStyleSheet("background-color: #23262b;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-size:15;\n"
"font-family:Roboto;\n"
"margin-top: 3 px;")
        self.nac_date.setObjectName("nac_date")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.nac_date)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px;")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.puesto_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.puesto_input.setMinimumSize(QtCore.QSize(0, 10))
        self.puesto_input.setMaximumSize(QtCore.QSize(300, 20))
        self.puesto_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.puesto_input.setPlaceholderText("")
        self.puesto_input.setObjectName("puesto_input")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.puesto_input)
        self.mail_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.mail_input.setMinimumSize(QtCore.QSize(0, 10))
        self.mail_input.setMaximumSize(QtCore.QSize(300, 20))
        self.mail_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}\n"
"")
        self.mail_input.setPlaceholderText("")
        self.mail_input.setObjectName("mail_input")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.mail_input)
        self.pass_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_input.setMinimumSize(QtCore.QSize(0, 10))
        self.pass_input.setMaximumSize(QtCore.QSize(300, 20))
        self.pass_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.pass_input.setPlaceholderText("")
        self.pass_input.setObjectName("pass_input")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.pass_input)
        self.pass_input_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_input_2.setMinimumSize(QtCore.QSize(0, 10))
        self.pass_input_2.setMaximumSize(QtCore.QSize(300, 20))
        self.pass_input_2.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.pass_input_2.setPlaceholderText("")
        self.pass_input_2.setObjectName("pass_input_2")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.SpanningRole, self.pass_input_2)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.apellido_input = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.apellido_input.setMinimumSize(QtCore.QSize(0, 10))
        self.apellido_input.setMaximumSize(QtCore.QSize(300, 20))
        self.apellido_input.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.apellido_input.setPlaceholderText("")
        self.apellido_input.setObjectName("apellido_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.apellido_input)
        self.tipo_cb = QtWidgets.QComboBox(self.formLayoutWidget)
        self.tipo_cb.setStyleSheet("\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 0px;\n"
"border: none;\n"
"font-size:13;\n"
"font-weight: 400;\n"
"margin-top:5px\n"
"\n"
"\n"
"")
        self.tipo_cb.setMaxVisibleItems(2)
        self.tipo_cb.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.tipo_cb.setDuplicatesEnabled(False)
        self.tipo_cb.setFrame(True)
        self.tipo_cb.setObjectName("tipo_cb")
        self.tipo_cb.addItem("")
        self.tipo_cb.addItem("")
        self.tipo_cb.addItem("")
        self.tipo_cb.setItemText(2, "")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.LabelRole, self.tipo_cb)
        self.pass_input_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_input_3.setMinimumSize(QtCore.QSize(0, 10))
        self.pass_input_3.setMaximumSize(QtCore.QSize(300, 20))
        self.pass_input_3.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.pass_input_3.setPlaceholderText("")
        self.pass_input_3.setObjectName("pass_input_3")
        self.formLayout.setWidget(20, QtWidgets.QFormLayout.SpanningRole, self.pass_input_3)
        self.pass_input_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_input_4.setMinimumSize(QtCore.QSize(0, 10))
        self.pass_input_4.setMaximumSize(QtCore.QSize(300, 20))
        self.pass_input_4.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.pass_input_4.setPlaceholderText("")
        self.pass_input_4.setObjectName("pass_input_4")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.SpanningRole, self.pass_input_4)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_11.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_9.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_12.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"color: #fff;\n"
"margin-top:20px")
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(120, 590, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"font-family:Roboto;\n"
"font-size: 14px\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tipo_cb.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "APELLIDO:"))
        self.label_3.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_5.setText(_translate("MainWindow", "NACIMIENTO:"))
        self.label_6.setText(_translate("MainWindow", "PUESTO:"))
        self.label_10.setText(_translate("MainWindow", "TIPO:"))
        self.label_8.setText(_translate("MainWindow", "DNI:"))
        self.tipo_cb.setCurrentText(_translate("MainWindow", "Admin"))
        self.tipo_cb.setItemText(0, _translate("MainWindow", "Admin"))
        self.tipo_cb.setItemText(1, _translate("MainWindow", "Usuario"))
        self.label_7.setText(_translate("MainWindow", "CONTRASEÑA:"))
        self.label_11.setText(_translate("MainWindow", "MAIL:"))
        self.label_9.setText(_translate("MainWindow", "REPETIR CONTRASEÑA:"))
        self.label_12.setText(_translate("MainWindow", "REPETIR MAIL:"))
        self.pushButton.setText(_translate("MainWindow", "Crear Usuario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
