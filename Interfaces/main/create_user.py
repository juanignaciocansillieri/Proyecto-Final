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
        MainWindow.resize(554, 492)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(554, 492))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet(" background-color: #1a1e23;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(80, 90, 431, 311))
        self.frame_3.setStyleSheet("background-color: #12151a;\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame_3)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 20, 391, 281))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 22, 0, 3)
        self.formLayout.setHorizontalSpacing(38)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"color: #fff;\n"
"margin-top:5px")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"color: #fff;\n"
"margin-top:15px")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"color: #fff;\n"
"margin-top:15px")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"color: #fff;\n"
"margin-top:15px")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"color: #fff;\n"
"margin-top:15px")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 28))
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus{\n"
"}")
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_10.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 18px;\n"
"color: #fff;\n"
"margin-top:15px")
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setStyleSheet("\n"
"background-color: #23262b;\n"
"border-radius: 3px;\n"
"padding: 4 10px;\n"
"color: #fff;\n"
"font-family:Roboto;\n"
"margin-top: 3px;\n"
"border: none;\n"
"font-size:15px;\n"
"font-weight: 400;\n"
"margin-top:15px\n"
"\n"
"\n"
"")
        self.comboBox.setMaxVisibleItems(2)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAfterCurrent)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(2, "")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.dateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setStyleSheet("background-color: #23262b;\n"
"border-radius: 10px;\n"
"padding:0 10px;\n"
"color: #b3b3b3;\n"
"font-family:Roboto;\n"
"margin-top: 11px;")
        self.dateEdit.setObjectName("dateEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(140, 0, 311, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("font-family: Roboto;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"color: #fff;\n"
"background:none;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(390, 430, 121, 31))
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
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "APELLIDO:"))
        self.label_3.setText(_translate("MainWindow", "NOMBRE:"))
        self.label_5.setText(_translate("MainWindow", "NACIMIENTO:"))
        self.label_6.setText(_translate("MainWindow", "PUESTO:"))
        self.label_8.setText(_translate("MainWindow", "MAIL:"))
        self.label_10.setText(_translate("MainWindow", "TIPO:"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Admin"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Admin"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Usuario"))
        self.label.setText(_translate("MainWindow", "CREAR NUEVO USUARIO"))
        self.pushButton.setText(_translate("MainWindow", "Crear Usuario"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
