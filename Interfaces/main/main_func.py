import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import * 
from nuevoProduct_func import ProductWindow
sys.path.append(".")
from CLASES import productos as p

#GUI File
from main import Ui_MainWindow

#Import Functions 
from toggleFunction import *

class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.show()

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
        ###################### ABRIR/CERRAR BARRA LATERAL #########################
        self.ui.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 65, True))

        ## PAGINAS ##

        # PRODUCTOS 
        self.ui.btn_productos.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_productos))
        self.ui.label_productos.mousePressEvent = self.clickP
        #Listamos productos al iniciar la ventana
        self.listarProductos()
        #Listamos al hacer click en el btn listar
        self.ui.listar_prod_btn.clicked.connect(self.listarProductos)

        #buscamos productos a traves del buscador
        self.ui.buscar_btn.clicked.connect(self.buscarProducto)
        

        #Abrir Ventana Nuevo producto
        self.ui.nuevo_prod_btn.clicked.connect(self.mostrarNewProduct)
       
        


        # DEPOSITO 
        self.ui.btn_depositos.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_depositos))
        self.ui.label_deposito.mousePressEvent = self.clickD
        # Usuarios 
        self.ui.btn_usuarios.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_usuarios))
        self.ui.label_usuarios.mousePressEvent = self.clickU
        # Boton Exit
        self.ui.btn_exit.clicked.connect(self.close)
        #self.ui.label_exit.mousePressEvent(self.close)
        
    def clickP(self,event): 
       return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_productos)
        
    def clickD(self,event): 
       return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_depositos)
        
    def clickU(self,event): 
       return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_usuarios)
    def clickE(self,event): 
       return self.close()



    def mostrarNewProduct(self):
         self.newProductWindow = ProductWindow()
         self.newProductWindow.show()
        


   #Listar productos from DB

    def listarProductos(self):
       products = p.listar_prod()
       n=p.contar_filas()
       self.ui.tableWidget.setRowCount(n)
       tableRow = 0
       for row in products:
          self.ui.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
          self.ui.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
          self.ui.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
          self.ui.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
          self.ui.tableWidget.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

          tableRow += 1 


    #Buscar productos a traves del input, por parámetro ingresado
    def buscarProducto(self):
       parametro = self.ui.buscar_input.text()
       products = p.productos.buscar_product(parametro)
       n = p.productos.buscar_product_rows(parametro)
       self.ui.tableWidget.setRowCount(n)
       tableRow = 0
       for row in products:
          self.ui.tableWidget.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
          self.ui.tableWidget.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
          self.ui.tableWidget.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
          self.ui.tableWidget.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
          self.ui.tableWidget.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

          tableRow += 1 


      
