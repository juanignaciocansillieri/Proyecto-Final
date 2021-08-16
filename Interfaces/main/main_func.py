from numpy import product
from toggleFunction import *
from main import Ui_MainWindow
import os
import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                          QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                         QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from create_user_func import UsuarioWindow
from nuevoProduct_func import ProductWindow
from bm_producto import BMProduct as bm
from bm_producto_ui import Ui_MainWindow as ui_bm
sys.path.append("C:\\proyecto-final\\CLASES\\")
import usuarios as u
import productos as p


# GUI File

# Import Functions


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
        self.ui.btn_toggle.clicked.connect(
            lambda: UIFunctions.toggleMenu(self, 65, True))

        ##                          PAGINAS                                ##

        ########################## PRODUCTOS ##################################

        self.ui.btn_productos.clicked.connect(
            lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_productos))
        self.ui.label_productos.mousePressEvent = self.clickP

        # Listamos productos al iniciar la ventana
        self.listarProductos()

        # Listamos al hacer click en el btn listar
        self.ui.listar_prod_btn.clicked.connect(self.listarProductos)

        # buscamos productos a traves del buscador
        self.ui.buscar_btn.clicked.connect(self.buscarProducto)

        # Abrir Ventana Nuevo producto
        self.ui.nuevo_prod_btn.clicked.connect(self.mostrarNewProduct)

        # Abrir ventana para ver el producto
        self.ui.tableWidget.doubleClicked.connect(self.seleccionarProducto)
        self.ui.tableWidget.doubleClicked.connect(self.mostrarBmProduct)

        # Abrir ventana para bm usuario
        # self.ui.tableWidget.doubleClicked.connect(self.seleccionarusuario)
        # self.ui.tableWidget.doubleClicked.connect(self.mostrarNewUser)

        ############################# DEPOSITO #########################################
        self.ui.btn_depositos.clicked.connect(
            lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_depositos))
        self.ui.label_deposito.mousePressEvent = self.clickD

        ####################### USUARIOS ################################################
        self.ui.btn_usuarios.clicked.connect(
            lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_usuarios))
        self.ui.label_usuarios.mousePressEvent = self.clickU

        # Listamos usuarios al iniciar la ventana
        self.listarUsuarios()
        # buscamos usuarios a traves del buscador
        self.ui.pushButton_usuarios_1.clicked.connect(self.buscarUsuarios)
        # Abrir Ventana Nuevo user
        self.ui.pushButton_usuarios_2.clicked.connect(self.mostrarNewUser)
        # Listamos al hacer click en el btn listar
        self.ui.pushButton_usuarios_3.clicked.connect(self.listarUsuarios)

        # Boton Exit
        self.ui.btn_exit.clicked.connect(self.close)
        # self.ui.label_exit.mousePressEvent(self.close)

    def clickP(self, event):
        return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_productos)

    def clickD(self, event):
        return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_depositos)

    def clickU(self, event):
        return self.ui.Pages_Widget.setCurrentWidget(self.ui.page_usuarios)

    def clickE(self, event):
        return self.close()

    def mostrarNewProduct(self):
        self.newProductWindow = ProductWindow()
        self.newProductWindow.show()

    def mostrarNewUser(self):
        self.newUserWindow = UsuarioWindow()
        self.newUserWindow.show()

    def mostrarBmProduct(self):
        self.newBmProduct = BMProduct()
        self.newBmProduct.show()
        
###############################FUNCIONES PRODUCTOS########################################

    # Listar productos from DB

    def listarProductos(self):
        products = p.listar_prod()
        n = p.contar_filas()
        self.ui.tableWidget.setRowCount(n)
        tableRow = 0
        for row in products:
            self.ui.tableWidget.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(
                tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1

    # Buscar productos a traves del input, por parámetro ingresado

    def buscarProducto(self):
        parametro = self.ui.buscar_input.text()
        products = p.productos.buscar_product(parametro)
        n = p.productos.buscar_product_rows(parametro)
        self.ui.tableWidget.setRowCount(n)
        tableRow = 0
        for row in products:
            self.ui.tableWidget.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget.setItem(
                tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1

    # Seleccionar producto al hacer click y abrir ventana

    def seleccionarProducto(self):
        global productId
        listaProductos = []
        for i in range(0,5):
            listaProductos.append(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),i).text())
        productId = listaProductos[0]
        print(productId)
        
            
 # Seleccionar usuario al hacer click y abrir ventana

    #def seleccionarusuario(self):
     #   global userid
      #  seleccionarusuario = []
       # for i in range(0,5):
        #    seleccionarusuario.append(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(),i).text())
        # userid = seleccionarusuario[0]
        # print(userid)
                    
#def uploadImg(self):
 #       size =(256,256)
 #       self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
  #      if ok:
   #         self.productImg = os.path.basename(self.filename)
    #        img=Image.open(self.filename)
     #       img=img.resize(size)
      #      img.save("img/{0}".format(self.productImg))


###############################FUNCIONES USUARIOS########################################


##Listar Usuarios

    def listarUsuarios(self):
        usuarios = u.listar_user()
        n = u.contar_filas()
        self.ui.tableWidget_2.setRowCount(n)
        tableRow = 0
        for row in usuarios:
            self.ui.tableWidget_2.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_2.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_2.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            if str(row[3]) == "b'1'":
                self.ui.tableWidget_2.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Admin"))
            else:
                self.ui.tableWidget_2.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Usuario"))

            self.ui.tableWidget_2.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1


##Buscar Usuarios

    def buscarUsuarios(self):
       parametro = self.ui.lineEdit_usuarios_1.text()
       products = u.usuarios.buscar_user(parametro)
       n = u.usuarios.buscar_user_rows(parametro)
       self.ui.tableWidget_2.setRowCount(n)
       tableRow = 0
       for row in products:
          self.ui.tableWidget_2.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
          self.ui.tableWidget_2.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
          self.ui.tableWidget_2.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
          if str(row[3])=="b'1'":
             self.ui.tableWidget_2.setItem(tableRow, 3, QtWidgets.QTableWidgetItem("Admin"))
          else:
             self.ui.tableWidget_2.setItem(tableRow, 3, QtWidgets.QTableWidgetItem("Usuario"))
          self.ui.tableWidget_2.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

          tableRow += 1 

   
  # def bm_user(self):
   #    self.ui.btn_depositos.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_depositos))
    #   self.ui.label_deposito.mousePressEvent = self.clickD
class BMProduct(QMainWindow):

    def __init__(self):
        super(BMProduct, self).__init__()
        self.ui = ui_bm()
        self.ui.setupUi(self)
        ############# RECIBIMOS PROPORCIONES DE LA PANTALLA ###########
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        ############## CENTRAMOS LA VENTANA #############
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        self.rellenarCampos()
        self.show()

    def rellenarCampos(self):
        global productId
        producto = p.productos.mostrar_product(productId)
        atributos = list(producto[0])
        print(atributos)
        self.ui.codigo_input.setText(atributos[0])
        self.ui.nombre_input.setText(atributos[1])
        self.ui.marca_input.setText(atributos[2])
        self.ui.venc_date.setDate(atributos[4])
        self.ui.lote_num.setValue(atributos[3])
        #self.ui.peso_num
        #self.ui.ancho_num
        #self.ui.altura_num
        #self.ui.cantidad_num
        #self.ui.condicion_cbox
