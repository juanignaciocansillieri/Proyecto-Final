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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("\n"
"background-color: #1a1e23;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-family:Roboto;\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_titulo = QtWidgets.QLabel(self.frame)
        self.label_titulo.setGeometry(QtCore.QRect(330, 10, 171, 31))
        self.label_titulo.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_titulo.setObjectName("label_titulo")
        self.label_nombre = QtWidgets.QLabel(self.frame)
        self.label_nombre.setGeometry(QtCore.QRect(36, 70, 140, 20))
        self.label_nombre.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_nombre.setLineWidth(1)
        self.label_nombre.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_nombre.setIndent(0)
        self.label_nombre.setObjectName("label_nombre")
        self.label_apellido = QtWidgets.QLabel(self.frame)
        self.label_apellido.setGeometry(QtCore.QRect(20, 120, 164, 20))
        self.label_apellido.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_apellido.setLineWidth(1)
        self.label_apellido.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_apellido.setIndent(0)
        self.label_apellido.setObjectName("label_apellido")
        self.label_tipo = QtWidgets.QLabel(self.frame)
        self.label_tipo.setGeometry(QtCore.QRect(49, 170, 140, 20))
        self.label_tipo.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_tipo.setLineWidth(1)
        self.label_tipo.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_tipo.setIndent(0)
        self.label_tipo.setObjectName("label_tipo")
        self.label_nacimiento = QtWidgets.QLabel(self.frame)
        self.label_nacimiento.setGeometry(QtCore.QRect(27, 220, 130, 20))
        self.label_nacimiento.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_nacimiento.setLineWidth(1)
        self.label_nacimiento.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_nacimiento.setIndent(0)
        self.label_nacimiento.setObjectName("label_nacimiento")
        self.label_nacimiento_2 = QtWidgets.QLabel(self.frame)
        self.label_nacimiento_2.setGeometry(QtCore.QRect(41, 270, 130, 20))
        self.label_nacimiento_2.setStyleSheet("color: rgb(230, 230, 230);\n"
"font: 15pt \"Roboto\";")
        self.label_nacimiento_2.setLineWidth(1)
        self.label_nacimiento_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_nacimiento_2.setIndent(0)
        self.label_nacimiento_2.setObjectName("label_nacimiento_2")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(165, 70, 220, 20))
        self.lineEdit_nombre.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_nombre.setText("")
        self.lineEdit_nombre.setCursorPosition(0)
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_apellido.setGeometry(QtCore.QRect(160, 120, 220, 20))
        self.lineEdit_apellido.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_apellido.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_apellido.setText("")
        self.lineEdit_apellido.setCursorPosition(0)
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.comboBox_tipo = QtWidgets.QComboBox(self.frame)
        self.comboBox_tipo.setGeometry(QtCore.QRect(160, 170, 120, 22))
        self.comboBox_tipo.setStyleSheet("background-color: #23262b;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-family:Roboto;\n"
"")
        self.comboBox_tipo.setObjectName("comboBox_tipo")
        self.comboBox_tipo.addItem("")
        self.comboBox_tipo.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(160, 220, 110, 22))
        self.dateEdit.setStyleSheet("background-color: #23262b;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-family:Roboto;\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.lineEdit_apellido_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_apellido_2.setGeometry(QtCore.QRect(160, 270, 220, 20))
        self.lineEdit_apellido_2.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_apellido_2.setText("")
        self.lineEdit_apellido_2.setCursorPosition(0)
        self.lineEdit_apellido_2.setObjectName("lineEdit_apellido_2")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titulo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">CREAR USUARIO</span></p></body></html>"))
        self.label_nombre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NOMBRE:</span></p></body></html>"))
        self.label_apellido.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">APELLIDO:</span></p></body></html>"))
        self.label_tipo.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">TIPO:</span></p></body></html>"))
        self.label_nacimiento.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NACIMIENTO:</span></p></body></html>"))
        self.label_nacimiento_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">PUESTO:</span></p></body></html>"))
        self.lineEdit_nombre.setPlaceholderText(_translate("MainWindow", "Escribir..."))
        self.lineEdit_apellido.setPlaceholderText(_translate("MainWindow", "Escribir..."))
        self.comboBox_tipo.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox_tipo.setItemText(1, _translate("MainWindow", "User"))
        self.lineEdit_apellido_2.setPlaceholderText(_translate("MainWindow", "Escribir..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
