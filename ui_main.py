# 1° COMANDO: C:\Users\nicol\OneDrive\Escritorio\Documentation\Main
# 2° COMANDO: pyuic5 -x "nombre del archivo de qt que es extensión ui" -o "nombre con extensión py"

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);\n"
"")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_top.setStyleSheet("background-color: rgb(18, 21, 26);")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_top)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_izquierda = QtWidgets.QFrame(self.frame)
        self.frame_izquierda.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_izquierda.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_izquierda.setObjectName("frame_izquierda")
        self.horizontalLayout_4.addWidget(self.frame_izquierda)
        self.frame_medio = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.frame_medio.sizePolicy().hasHeightForWidth())
        self.frame_medio.setSizePolicy(sizePolicy)
        self.frame_medio.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_medio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_medio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_medio.setObjectName("frame_medio")
        self.label = QtWidgets.QLabel(self.frame_medio)
        self.label.setGeometry(QtCore.QRect(120, -25, 202, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet("border-image: url(:/cct/Logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.frame_medio)
        self.frame_derecha = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_derecha.sizePolicy().hasHeightForWidth())
        self.frame_derecha.setSizePolicy(sizePolicy)
        self.frame_derecha.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_derecha.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_derecha.setObjectName("frame_derecha")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_derecha)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_derecha)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_interno_izquierdo = QtWidgets.QFrame(self.frame_2)
        self.frame_interno_izquierdo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_interno_izquierdo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_interno_izquierdo.setObjectName("frame_interno_izquierdo")
        self.horizontalLayout_6.addWidget(self.frame_interno_izquierdo)
        self.frame_intern_medio = QtWidgets.QFrame(self.frame_2)
        self.frame_intern_medio.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_intern_medio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_intern_medio.setObjectName("frame_intern_medio")
        self.horizontalLayout_6.addWidget(self.frame_intern_medio)
        self.frame_interno_derecha = QtWidgets.QFrame(self.frame_2)
        self.frame_interno_derecha.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_interno_derecha.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_interno_derecha.setObjectName("frame_interno_derecha")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_interno_derecha)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Btn_minimize = QtWidgets.QPushButton(self.frame_interno_derecha)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_minimize.sizePolicy().hasHeightForWidth())
        self.Btn_minimize.setSizePolicy(sizePolicy)
        self.Btn_minimize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/minimize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_minimize.setIcon(icon)
        self.Btn_minimize.setObjectName("Btn_minimize")
        self.horizontalLayout_7.addWidget(self.Btn_minimize, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Btn_Maximize = QtWidgets.QPushButton(self.frame_interno_derecha)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Maximize.sizePolicy().hasHeightForWidth())
        self.Btn_Maximize.setSizePolicy(sizePolicy)
        self.Btn_Maximize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/maximize.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Maximize.setIcon(icon1)
        self.Btn_Maximize.setObjectName("Btn_Maximize")
        self.horizontalLayout_7.addWidget(self.Btn_Maximize, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.Btn_close = QtWidgets.QPushButton(self.frame_interno_derecha)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_close.sizePolicy().hasHeightForWidth())
        self.Btn_close.setSizePolicy(sizePolicy)
        self.Btn_close.setStyleSheet("border: none;")
        self.Btn_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/cct/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_close.setIcon(icon2)
        self.Btn_close.setIconSize(QtCore.QSize(14, 14))
        self.Btn_close.setObjectName("Btn_close")
        self.horizontalLayout_7.addWidget(self.Btn_close)
        self.horizontalLayout_6.addWidget(self.frame_interno_derecha)
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.horizontalLayout_4.addWidget(self.frame_derecha)
        self.horizontalLayout_3.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: #12151a;")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Btn_Menu_5 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_5.setStyleSheet("border: none;")
        self.Btn_Menu_5.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/cct/Menú.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_5.setIcon(icon3)
        self.Btn_Menu_5.setIconSize(QtCore.QSize(50, 50))
        self.Btn_Menu_5.setObjectName("Btn_Menu_5")
        self.verticalLayout_3.addWidget(self.Btn_Menu_5)
        self.Btn_Menu_4 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_4.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Menu_4.setFont(font)
        self.Btn_Menu_4.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.Btn_Menu_4.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Iconos/Productos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_4.setIcon(icon4)
        self.Btn_Menu_4.setIconSize(QtCore.QSize(60, 60))
        self.Btn_Menu_4.setObjectName("Btn_Menu_4")
        self.verticalLayout_3.addWidget(self.Btn_Menu_4)
        self.Btn_Menu_1 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_1.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Menu_1.setFont(font)
        self.Btn_Menu_1.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: 0px solid;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 170, 255);\n"
"}\n"
"")
        self.Btn_Menu_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/cct/Depósito.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_1.setIcon(icon5)
        self.Btn_Menu_1.setIconSize(QtCore.QSize(60, 60))
        self.Btn_Menu_1.setObjectName("Btn_Menu_1")
        self.verticalLayout_3.addWidget(self.Btn_Menu_1)
        self.Btn_Menu_2 = QtWidgets.QPushButton(self.frame_top_menus)
        self.Btn_Menu_2.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Menu_2.setFont(font)
        self.Btn_Menu_2.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: 0px solid;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_Menu_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("Iconos/Usuarios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_2.setIcon(icon6)
        self.Btn_Menu_2.setIconSize(QtCore.QSize(60, 60))
        self.Btn_Menu_2.setObjectName("Btn_Menu_2")
        self.verticalLayout_3.addWidget(self.Btn_Menu_2)
        self.verticalLayout_2.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.Btn_Menu_3 = QtWidgets.QPushButton(self.frame_left_menu)
        self.Btn_Menu_3.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Btn_Menu_3.setFont(font)
        self.Btn_Menu_3.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.Btn_Menu_3.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/cct/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Btn_Menu_3.setIcon(icon7)
        self.Btn_Menu_3.setIconSize(QtCore.QSize(60, 60))
        self.Btn_Menu_3.setObjectName("Btn_Menu_3")
        self.verticalLayout_2.addWidget(self.Btn_Menu_3)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setStyleSheet("border: none;")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Pages_Widget = QtWidgets.QStackedWidget(self.frame_pages)
        self.Pages_Widget.setStyleSheet("background-color: #1a1e23;\n"
"border: none;")
        self.Pages_Widget.setObjectName("Pages_Widget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.label_productos = QtWidgets.QLabel(self.page_1)
        self.label_productos.setGeometry(QtCore.QRect(140, 60, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_productos.setFont(font)
        self.label_productos.setStyleSheet("background-color: rgb(17, 115, 255);")
        self.label_productos.setObjectName("label_productos")
        self.Pages_Widget.addWidget(self.page_1)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_usuarios = QtWidgets.QLabel(self.page_3)
        self.label_usuarios.setGeometry(QtCore.QRect(90, 70, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_usuarios.setFont(font)
        self.label_usuarios.setStyleSheet("background-color: rgb(17, 115, 255);")
        self.label_usuarios.setObjectName("label_usuarios")
        self.Pages_Widget.addWidget(self.page_3)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_deposito = QtWidgets.QLabel(self.page_2)
        self.label_deposito.setGeometry(QtCore.QRect(150, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_deposito.setFont(font)
        self.label_deposito.setStyleSheet("background-color: rgb(17, 115, 255);")
        self.label_deposito.setObjectName("label_deposito")
        self.Pages_Widget.addWidget(self.page_2)
        self.verticalLayout_4.addWidget(self.Pages_Widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Btn_Menu_1, self.Btn_Menu_2)
        MainWindow.setTabOrder(self.Btn_Menu_2, self.Btn_Menu_3)
        MainWindow.setTabOrder(self.Btn_Menu_3, self.Btn_Menu_5)
        MainWindow.setTabOrder(self.Btn_Menu_5, self.Btn_Menu_4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_productos.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Productos</span></p></body></html>"))
        self.label_usuarios.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Usuarios</span></p></body></html>"))
        self.label_deposito.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Depósito</span></p></body></html>"))
import iconos_provisorios_rc
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())