# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nueva_area.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(475, 300)
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
        self.frame_3.setGeometry(QtCore.QRect(20, 40, 431, 211))
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
        font.setPointSize(-1)
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
        self.motivo_input = QtWidgets.QLineEdit(self.frame_3)
        self.motivo_input.setGeometry(QtCore.QRect(20, 40, 170, 25))
        self.motivo_input.setMinimumSize(QtCore.QSize(0, 0))
        self.motivo_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.motivo_input.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.motivo_input.setPlaceholderText("")
        self.motivo_input.setObjectName("motivo_input")
        self.crearprod_btn = QtWidgets.QPushButton(self.frame_3)
        self.crearprod_btn.setGeometry(QtCore.QRect(150, 150, 121, 26))
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
        self.label_egr_ing = QtWidgets.QLabel(self.frame_3)
        self.label_egr_ing.setGeometry(QtCore.QRect(20, 10, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_egr_ing.setFont(font)
        self.label_egr_ing.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_egr_ing.setObjectName("label_egr_ing")
        self.label_egr_ing_2 = QtWidgets.QLabel(self.frame_3)
        self.label_egr_ing_2.setGeometry(QtCore.QRect(20, 70, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_egr_ing_2.setFont(font)
        self.label_egr_ing_2.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_egr_ing_2.setObjectName("label_egr_ing_2")
        self.motivo_input_2 = QtWidgets.QLineEdit(self.frame_3)
        self.motivo_input_2.setGeometry(QtCore.QRect(20, 100, 170, 25))
        self.motivo_input_2.setMinimumSize(QtCore.QSize(0, 0))
        self.motivo_input_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.motivo_input_2.setStyleSheet("QLineEdit{\n"
"background-color: #fff;\n"
"border: 0.5px solid #c1c1c1;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"\n"
"}\n"
"")
        self.motivo_input_2.setPlaceholderText("")
        self.motivo_input_2.setObjectName("motivo_input_2")
        self.label_pasillos = QtWidgets.QLabel(self.frame_3)
        self.label_pasillos.setGeometry(QtCore.QRect(220, 10, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_pasillos.setFont(font)
        self.label_pasillos.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_pasillos.setObjectName("label_pasillos")
        self.label_pasillos_2 = QtWidgets.QLabel(self.frame_3)
        self.label_pasillos_2.setGeometry(QtCore.QRect(220, 70, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        self.label_pasillos_2.setFont(font)
        self.label_pasillos_2.setStyleSheet("font-family: Roboto;\n"
"font-size: 14px;\n"
"margin-top:10px;\n"
"margin-left:10px\n"
"\n"
"")
        self.label_pasillos_2.setObjectName("label_pasillos_2")
        self.segmentos_num = QtWidgets.QSpinBox(self.frame_3)
        self.segmentos_num.setGeometry(QtCore.QRect(220, 100, 121, 25))
        self.segmentos_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.segmentos_num.setMinimum(0)
        self.segmentos_num.setMaximum(999)
        self.segmentos_num.setObjectName("segmentos_num")
        self.pasillos_num = QtWidgets.QSpinBox(self.frame_3)
        self.pasillos_num.setGeometry(QtCore.QRect(220, 40, 121, 25))
        self.pasillos_num.setStyleSheet("background-color: #fff;\n"
"border-radius: 3px;\n"
"padding: 4 5px;\n"
"color: rgb(0, 0, 0);\n"
"font-family:Roboto;\n"
"border: none;\n"
"font-size:13px;\n"
"font-weight: 400;\n"
"margin-left: 10px;\n"
"")
        self.pasillos_num.setObjectName("pasillos_num")
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.crearprod_btn.setText(_translate("MainWindow", "Confirmar"))
        self.label_egr_ing.setText(_translate("MainWindow", "Nombre"))
        self.label_egr_ing_2.setText(_translate("MainWindow", "Identifcador"))
        self.label_pasillos.setText(_translate("MainWindow", "Pasilllos"))
        self.label_pasillos_2.setText(_translate("MainWindow", "Segmentos"))
import img_oficiales_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
