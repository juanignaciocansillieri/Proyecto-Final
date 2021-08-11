# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1134, 543)
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 500))
        self.centralwidget.setObjectName("centralwidget")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setGeometry(QtCore.QRect(0, 0, 1133, 45))
        self.Top_Bar.setMinimumSize(QtCore.QSize(0, 45))
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 45))
        self.Top_Bar.setStyleSheet("background-color: #12151a;\n"
"")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.Top_Bar)
        self.label.setMinimumSize(QtCore.QSize(0, 45))
        self.label.setMaximumSize(QtCore.QSize(200, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/cct/logo-18.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setGeometry(QtCore.QRect(0, 45, 1133, 497))
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(50, 16777215))
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
        self.btn_toggle = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_toggle.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btn_toggle.setFont(font)
        self.btn_toggle.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_toggle.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: none;\n"
"border-radius:10px;\n"
"padding:0 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #23262b;\n"
"}\n"
"\n"
"\n"
"QPushButton:focus {\n"
"background-color: #23262b;\n"
"}")
        self.btn_toggle.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cct/Menú.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QtCore.QSize(50, 50))
        self.btn_toggle.setObjectName("btn_toggle")
        self.verticalLayout_3.addWidget(self.btn_toggle)
        self.btn_productos = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_productos.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_productos.setFont(font)
        self.btn_productos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_productos.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: none;\n"
"border-radius:10px;\n"
"padding:0 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #23262b;\n"
"}\n"
"\n"
"\n"
"QPushButton:focus {\n"
"background-color: #23262b;\n"
"}")
        self.btn_productos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cct/Productos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_productos.setIcon(icon1)
        self.btn_productos.setIconSize(QtCore.QSize(60, 60))
        self.btn_productos.setObjectName("btn_productos")
        self.verticalLayout_3.addWidget(self.btn_productos)
        self.btn_depositos = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_depositos.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_depositos.setFont(font)
        self.btn_depositos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_depositos.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: none;\n"
"border-radius:10px;\n"
"padding:0 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #23262b;\n"
"}\n"
"\n"
"\n"
"QPushButton:focus {\n"
"background-color: #23262b;\n"
"}")
        self.btn_depositos.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/cct/Deposito.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_depositos.setIcon(icon2)
        self.btn_depositos.setIconSize(QtCore.QSize(60, 60))
        self.btn_depositos.setObjectName("btn_depositos")
        self.verticalLayout_3.addWidget(self.btn_depositos)
        self.btn_usuarios = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_usuarios.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_usuarios.setFont(font)
        self.btn_usuarios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_usuarios.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: none;\n"
"border-radius:10px;\n"
"padding:0 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #23262b;\n"
"}\n"
"\n"
"\n"
"QPushButton:focus {\n"
"background-color: #23262b;\n"
"}")
        self.btn_usuarios.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/cct/Usuarios.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_usuarios.setIcon(icon3)
        self.btn_usuarios.setIconSize(QtCore.QSize(60, 60))
        self.btn_usuarios.setObjectName("btn_usuarios")
        self.verticalLayout_3.addWidget(self.btn_usuarios)
        self.verticalLayout_2.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.btn_exit = QtWidgets.QPushButton(self.frame_left_menu)
        self.btn_exit.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet("QPushButton {\n"
"color: #b3b3b3;\n"
"background-color: #12151a;\n"
"border: none;\n"
"border-radius:10px;\n"
"padding:0 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #23262b;\n"
"}\n"
"\n"
"\n"
"QPushButton:focus {\n"
"background-color: #23262b;\n"
"}")
        self.btn_exit.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/cct/Exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon4)
        self.btn_exit.setIconSize(QtCore.QSize(60, 60))
        self.btn_exit.setObjectName("btn_exit")
        self.verticalLayout_2.addWidget(self.btn_exit)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.slide_bar = QtWidgets.QFrame(self.Content)
        self.slide_bar.setMinimumSize(QtCore.QSize(80, 741))
        self.slide_bar.setMaximumSize(QtCore.QSize(0, 750))
        self.slide_bar.setStyleSheet("background-color: #12151a;")
        self.slide_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_bar.setObjectName("slide_bar")
        self.label_inicio = QtWidgets.QLabel(self.slide_bar)
        self.label_inicio.setGeometry(QtCore.QRect(0, 1, 51, 50))
        self.label_inicio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_inicio.setStyleSheet("QLabel {\n"
"color: #fff;\n"
"font-weight:bold;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}")
        self.label_inicio.setObjectName("label_inicio")
        self.label_deposito = QtWidgets.QLabel(self.slide_bar)
        self.label_deposito.setGeometry(QtCore.QRect(0, 130, 71, 31))
        self.label_deposito.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_deposito.setStyleSheet("color:#fff;\n"
"font-family:Roboto")
        self.label_deposito.setObjectName("label_deposito")
        self.label_productos = QtWidgets.QLabel(self.slide_bar)
        self.label_productos.setGeometry(QtCore.QRect(0, 65, 71, 31))
        self.label_productos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_productos.setStyleSheet("QLabel {\n"
"color: #fff\n"
"\n"
"}\n"
"\n"
"")
        self.label_productos.setObjectName("label_productos")
        self.label_usuarios = QtWidgets.QLabel(self.slide_bar)
        self.label_usuarios.setGeometry(QtCore.QRect(0, 186, 71, 31))
        self.label_usuarios.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_usuarios.setStyleSheet("color:#fff;\n"
"font-family:Roboto")
        self.label_usuarios.setObjectName("label_usuarios")
        self.label_exit = QtWidgets.QLabel(self.slide_bar)
        self.label_exit.setGeometry(QtCore.QRect(0, 693, 101, 31))
        self.label_exit.setStyleSheet("QLabel {\n"
"color: #fff;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"QLabel:hover {\n"
"background-color: #23262b;\n"
"}")
        self.label_exit.setObjectName("label_exit")
        self.label_exit_2 = QtWidgets.QLabel(self.slide_bar)
        self.label_exit_2.setGeometry(QtCore.QRect(0, 451, 71, 31))
        self.label_exit_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_exit_2.setStyleSheet("color:#fff;\n"
"font-family:Roboto")
        self.label_exit_2.setObjectName("label_exit_2")
        self.horizontalLayout_2.addWidget(self.slide_bar)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setMaximumSize(QtCore.QSize(16777215, 16777215))
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
        self.page_productos = QtWidgets.QWidget()
        self.page_productos.setObjectName("page_productos")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_productos)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.page_productos)
        self.frame.setMinimumSize(QtCore.QSize(0, 503))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(900, 65))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setMinimumSize(QtCore.QSize(990, 50))
        self.groupBox.setMaximumSize(QtCore.QSize(0, 70))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.buscar_input = QtWidgets.QLineEdit(self.groupBox)
        self.buscar_input.setGeometry(QtCore.QRect(43, 21, 771, 25))
        self.buscar_input.setStyleSheet("QLineEdit{\n"
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
        self.buscar_input.setText("")
        self.buscar_input.setObjectName("buscar_input")
        self.buscar_btn = QtWidgets.QPushButton(self.groupBox)
        self.buscar_btn.setGeometry(QtCore.QRect(841, 21, 81, 25))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.buscar_btn.setFont(font)
        self.buscar_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buscar_btn.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"font-family:Roboto;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.buscar_btn.setObjectName("buscar_btn")
        self.verticalLayout_6.addWidget(self.groupBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setMinimumSize(QtCore.QSize(900, 328))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 500))
        self.tableWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"color:#fff;\n"
"font-size: 20px;\n"
"border-style: none;\n"
"margin-left: 0px;\n"
"margin-top:15px\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #12151a;\n"
"    color:#fff;\n"
"    font-size: 12pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #23262b;\n"
"    border-right: 1px solid #23262b;\n"
"    font-family:Roboto;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border-top: 1px solid #23262b;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"\n"
"    border-left: 1px solid #23262b;\n"
"}")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(176)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setMinimumSectionSize(23)
        self.verticalLayout_5.addWidget(self.tableWidget, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 66))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 75))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 53))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.nuevo_prod_btn = QtWidgets.QPushButton(self.frame_4)
        self.nuevo_prod_btn.setGeometry(QtCore.QRect(690, 27, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.nuevo_prod_btn.setFont(font)
        self.nuevo_prod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nuevo_prod_btn.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.nuevo_prod_btn.setObjectName("nuevo_prod_btn")
        self.listar_prod_btn = QtWidgets.QPushButton(self.frame_4)
        self.listar_prod_btn.setGeometry(QtCore.QRect(820, 27, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setItalic(False)
        self.listar_prod_btn.setFont(font)
        self.listar_prod_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.listar_prod_btn.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.listar_prod_btn.setObjectName("listar_prod_btn")
        self.verticalLayout_7.addWidget(self.frame_4, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.frame)
        self.Pages_Widget.addWidget(self.page_productos)
        self.page_depositos = QtWidgets.QWidget()
        self.page_depositos.setObjectName("page_depositos")
        self.label_3 = QtWidgets.QLabel(self.page_depositos)
        self.label_3.setGeometry(QtCore.QRect(120, 170, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(17, 115, 255);")
        self.label_3.setObjectName("label_3")
        self.Pages_Widget.addWidget(self.page_depositos)
        self.page_usuarios = QtWidgets.QWidget()
        self.page_usuarios.setObjectName("page_usuarios")
        self.frame_usuarios = QtWidgets.QFrame(self.page_usuarios)
        self.frame_usuarios.setGeometry(QtCore.QRect(-10, 0, 1081, 503))
        self.frame_usuarios.setMinimumSize(QtCore.QSize(0, 503))
        self.frame_usuarios.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_usuarios.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_usuarios.setObjectName("frame_usuarios")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_usuarios)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_usuarios_1 = QtWidgets.QFrame(self.frame_usuarios)
        self.frame_usuarios_1.setMinimumSize(QtCore.QSize(900, 65))
        self.frame_usuarios_1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_usuarios_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_usuarios_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_usuarios_1.setObjectName("frame_usuarios_1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_usuarios_1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_usuarios_1 = QtWidgets.QGroupBox(self.frame_usuarios_1)
        self.groupBox_usuarios_1.setMinimumSize(QtCore.QSize(1941, 50))
        self.groupBox_usuarios_1.setMaximumSize(QtCore.QSize(0, 70))
        self.groupBox_usuarios_1.setTitle("")
        self.groupBox_usuarios_1.setObjectName("groupBox_usuarios_1")
        self.lineEdit_usuarios_1 = QtWidgets.QLineEdit(self.groupBox_usuarios_1)
        self.lineEdit_usuarios_1.setGeometry(QtCore.QRect(43, 21, 771, 25))
        self.lineEdit_usuarios_1.setStyleSheet("QLineEdit{\n"
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
        self.lineEdit_usuarios_1.setText("")
        self.lineEdit_usuarios_1.setObjectName("lineEdit_usuarios_1")
        self.pushButton_usuarios_1 = QtWidgets.QPushButton(self.groupBox_usuarios_1)
        self.pushButton_usuarios_1.setGeometry(QtCore.QRect(841, 21, 81, 25))
        self.pushButton_usuarios_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_usuarios_1.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"font-family:Roboto;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.pushButton_usuarios_1.setObjectName("pushButton_usuarios_1")
        self.verticalLayout_9.addWidget(self.groupBox_usuarios_1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_8.addWidget(self.frame_usuarios_1, 0, QtCore.Qt.AlignTop)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_usuarios)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(980, 300))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(801, 500))
        self.tableWidget_2.setStyleSheet("QTableWidget{\n"
"color:#fff;\n"
"font-size: 20px;\n"
"border-style: none;\n"
"margin-left: 55px;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #12151a;\n"
"    color:#fff;\n"
"    font-size: 12pt;\n"
"    border-style: none;\n"
"    border-bottom: 1px solid #23262b;\n"
"    border-right: 1px solid #23262b;\n"
"    font-family:Roboto;\n"
"\n"
"\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"\n"
"    border-top: 1px solid #23262b;\n"
"}\n"
"\n"
"QHeaderView::section:vertical\n"
"{\n"
"\n"
"    border-left: 1px solid #23262b;\n"
"}")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(176)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.verticalLayout_8.addWidget(self.tableWidget_2)
        self.frame_usuarios_3 = QtWidgets.QFrame(self.frame_usuarios)
        self.frame_usuarios_3.setMinimumSize(QtCore.QSize(0, 53))
        self.frame_usuarios_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_usuarios_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_usuarios_3.setObjectName("frame_usuarios_3")
        self.pushButton_usuarios_2 = QtWidgets.QPushButton(self.frame_usuarios_3)
        self.pushButton_usuarios_2.setGeometry(QtCore.QRect(470, 10, 111, 31))
        self.pushButton_usuarios_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_usuarios_2.setStyleSheet("QPushButton{\n"
"background-color: #1173ff;\n"
"color: #fff;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #45a9f0;\n"
"}")
        self.pushButton_usuarios_2.setObjectName("pushButton_usuarios_2")
        self.verticalLayout_8.addWidget(self.frame_usuarios_3)
        self.Pages_Widget.addWidget(self.page_usuarios)
        self.verticalLayout_4.addWidget(self.Pages_Widget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Pages_Widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_depositos, self.btn_usuarios)
        MainWindow.setTabOrder(self.btn_usuarios, self.btn_exit)
        MainWindow.setTabOrder(self.btn_exit, self.btn_toggle)
        MainWindow.setTabOrder(self.btn_toggle, self.btn_productos)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_inicio.setText(_translate("MainWindow", " Inicio"))
        self.label_deposito.setText(_translate("MainWindow", " Depósito"))
        self.label_productos.setText(_translate("MainWindow", " Productos"))
        self.label_usuarios.setText(_translate("MainWindow", " Usuarios"))
        self.label_exit.setText(_translate("MainWindow", "Exit"))
        self.label_exit_2.setText(_translate("MainWindow", " Salir"))
        self.buscar_input.setPlaceholderText(_translate("MainWindow", "Buscar un producto"))
        self.buscar_btn.setText(_translate("MainWindow", "Buscar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Código"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Marca"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Fecha de Vencimiento"))
        self.nuevo_prod_btn.setText(_translate("MainWindow", "Nuevo Pruducto"))
        self.listar_prod_btn.setText(_translate("MainWindow", "Listar Productos"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">Depósito</span></p></body></html>"))
        self.lineEdit_usuarios_1.setPlaceholderText(_translate("MainWindow", "Buscar un usuario"))
        self.pushButton_usuarios_1.setText(_translate("MainWindow", "Buscar"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fecha de Nacimiento"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Tipo"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Puesto"))
        self.pushButton_usuarios_2.setText(_translate("MainWindow", "Crear nuevo usuario"))
import img.img


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
