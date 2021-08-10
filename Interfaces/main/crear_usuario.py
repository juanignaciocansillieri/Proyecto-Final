# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crear_usuario.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 600)
        MainWindow.setStyleSheet("background-color: rgb(26, 30, 35);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_principal = QtWidgets.QFrame(self.centralwidget)
        self.frame_principal.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_principal.setObjectName("frame_principal")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_principal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.frame_principal)
        self.frame.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-family:Roboto;\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"border: 1px solid rgb(75, 75, 75);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_1 = QtWidgets.QFrame(self.frame)
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.label_titulo = QtWidgets.QLabel(self.frame_1)
        self.label_titulo.setGeometry(QtCore.QRect(290, -10, 131, 31))
        self.label_titulo.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_titulo.setObjectName("label_titulo")
        self.label_nombre = QtWidgets.QLabel(self.frame_1)
        self.label_nombre.setGeometry(QtCore.QRect(0, 60, 140, 20))
        self.label_nombre.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_nombre.setLineWidth(1)
        self.label_nombre.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_nombre.setIndent(0)
        self.label_nombre.setObjectName("label_nombre")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.frame_1)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(120, 60, 220, 20))
        self.lineEdit_nombre.setText("")
        self.lineEdit_nombre.setCursorPosition(0)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.verticalLayout_2.addWidget(self.frame_1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_apellido = QtWidgets.QLabel(self.frame_2)
        self.label_apellido.setGeometry(QtCore.QRect(0, 10, 130, 20))
        self.label_apellido.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_apellido.setLineWidth(1)
        self.label_apellido.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_apellido.setIndent(0)
        self.label_apellido.setObjectName("label_apellido")
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_apellido.setGeometry(QtCore.QRect(120, 10, 220, 20))
        self.lineEdit_apellido.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_apellido.setText("")
        self.lineEdit_apellido.setCursorPosition(0)
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.label_tipo = QtWidgets.QLabel(self.frame_2)
        self.label_tipo.setGeometry(QtCore.QRect(10, 50, 140, 20))
        self.label_tipo.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_tipo.setLineWidth(1)
        self.label_tipo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_tipo.setIndent(0)
        self.label_tipo.setObjectName("label_tipo")
        self.comboBox_tipo = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_tipo.setGeometry(QtCore.QRect(120, 50, 110, 22))
        self.comboBox_tipo.setStyleSheet("background-color: #23262b;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-family:Roboto;\n"
"")
        self.comboBox_tipo.setObjectName("comboBox_tipo")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_nacimiento = QtWidgets.QLabel(self.frame_3)
        self.label_nacimiento.setGeometry(QtCore.QRect(-10, 0, 130, 20))
        self.label_nacimiento.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_nacimiento.setLineWidth(1)
        self.label_nacimiento.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_nacimiento.setIndent(0)
        self.label_nacimiento.setObjectName("label_nacimiento")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_3)
        self.dateEdit.setGeometry(QtCore.QRect(120, 0, 110, 22))
        self.dateEdit.setStyleSheet("background-color: #23262b;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-family:Roboto;\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.label_nacimiento_2 = QtWidgets.QLabel(self.frame_3)
        self.label_nacimiento_2.setGeometry(QtCore.QRect(10, 40, 130, 20))
        self.label_nacimiento_2.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_nacimiento_2.setLineWidth(1)
        self.label_nacimiento_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_nacimiento_2.setIndent(0)
        self.label_nacimiento_2.setObjectName("label_nacimiento_2")
        self.lineEdit_apellido_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_apellido_2.setGeometry(QtCore.QRect(120, 40, 220, 20))
        self.lineEdit_apellido_2.setText("")
        self.lineEdit_apellido_2.setCursorPosition(0)
        self.lineEdit_apellido_2.setObjectName("lineEdit_apellido_2")
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_vivnm = QtWidgets.QFrame(self.frame)
        self.frame_vivnm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_vivnm.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_vivnm.setObjectName("frame_vivnm")
        self.verticalLayout_2.addWidget(self.frame_vivnm)
        self.frame_TRES = QtWidgets.QFrame(self.frame)
        self.frame_TRES.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_TRES.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_TRES.setObjectName("frame_TRES")
        self.verticalLayout_2.addWidget(self.frame_TRES)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_principal)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CREAR USUARIO</span></p></body></html>"))
        self.label_nombre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NOMBRE:</span></p></body></html>"))
        self.lineEdit_nombre.setPlaceholderText(_translate("MainWindow", "Escribir..."))
        self.label_apellido.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">APELLIDO:</span></p></body></html>"))
        self.lineEdit_apellido.setPlaceholderText(_translate("MainWindow", "Escribir..."))
        self.label_tipo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TIPO:</span></p></body></html>"))
        self.comboBox_tipo.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_tipo.setItemText(1, _translate("MainWindow", "User"))
        self.label_nacimiento.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NACIMIENTO:</span></p></body></html>"))
        self.label_nacimiento_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PUESTO:</span></p></body></html>"))
        self.lineEdit_apellido_2.setPlaceholderText(_translate("MainWindow", "Escribir..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())