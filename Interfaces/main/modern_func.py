import sys
import os
from typing import get_origin
from PIL import Image
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import nuevo_producto_ui
from modern import Ui_MainWindow
from toggleFunction import UIFunctions
from nuevoProduct_func import ProductWindow
from create_user_func import UsuarioWindow
from create_user_func import UsuarioWindow
from nuevoProduct_func import ProductWindow
from nueva_area import Ui_MainWindow as na
from bm_producto import Ui_MainWindow as ui_bm
from bm_user import Ui_MainWindow as bmu 
from array import array
from nueva_area_func import NewArea
import movimiento_func
from movimiento_func import NewMovimiento
sys.path.append("C:\\proyecto-final\\DB\\")
import loginDB
sys.path.append("C:\\proyecto-final\\CLASES\\")
import usuarios as u
import productos as p
import area as ar
import movimientos as m
import lotes as l



defaultImg = ""
codigoViejo = ""
DNI_Viejo = ""
DNI = ""

class Modern(QMainWindow):

    def __init__(self):
        super(Modern, self).__init__()
        self.ui = Ui_MainWindow()
        self.uii = na()
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

        ##########################   PAGINAS   ##################################
        
    ########################## PRODUCTOS ##################################

        ## Abrir Pagina Productos ##
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage))
        self.ui.products_btn.clicked.connect(self.listarProductos)
        self.ui.products_btn_stock.clicked.connect(self.listarProductos)
        # Abrir Pag Stock
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        self.ui.products_btn_stock.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        # Abrir Pag Movimientos
        self.ui.products_btn_movimiento.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_movimientos))
        # Abrir Pag Lotes
        self.ui.products_btn_lotes.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_lotes))
        #self.ui.btn_movimiento.clicked.connect(self.)
        
        # Listamos productos al iniciar la ventana
        n = 0
        n = p.contar_filas()
        
        if n > 0:
            self.listarProductos()

            # Btn para buscar
        self.ui.btn_buscarP.clicked.connect(self.buscarProducto)  

            # Abrir ventana para ver el producto individual
        self.ui.tableWidget_stock_2.doubleClicked.connect(self.seleccionarProducto)
        self.ui.tableWidget_stock_2.doubleClicked.connect(self.mostrarBmProduct)

            # Abrir ventana para agregar Nuevo producto
        self.ui.product_new_btn.clicked.connect(self.mostrarNewProduct)

        self.aaa = self.mostrarAreas()

            # Abrir ventana para agregar Nuevo movimiento
        self.ui.btn_movimiento.clicked.connect(self.mostrarNewMovimiento)

    ########################## USUARIOS ##################################

        self.ui.user_new_btn.clicked.connect(self.mostrarNewUser)
        self.ui.users_btn.clicked.connect(self.listarUsuarios)
        self.ui.btn_buscarU.clicked.connect(self.buscarUsuarios)  

        
        ## Abrir Pagina Usuarios ##
        self.ui.users_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_usuarios))
        self.ui.users_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage))


            # Abrir ventana para ver el producto individual
        self.ui.tableWidget_usuarios.doubleClicked.connect(self.seleccionarusuario)
        self.ui.tableWidget_usuarios.doubleClicked.connect(self.mostrarBmUser)

    ########################## DEPOSITOS ##################################

        self.ui.deposito_btn.clicked.connect(self.mostrarAreas)
        ## Abrir Pagina Depositos ##
        self.ui.deposito_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito))
        self.ui.deposito_btn.clicked.connect(lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.deposito_subpage))
        self.ui.newArea_btn.clicked.connect(self.mostrarNewArea)

    def mostrarNewProduct(self):
        self.newProductWindow = ProductWindow()
        self.newProductWindow.show()

    def mostrarNewUser(self):
        self.newUserWindow = UsuarioWindow()
        self.newUserWindow.show()

    def mostrarBmProduct(self):
        self.newBmProduct = BMProduct()
        self.newBmProduct.show()
        
    def mostrarBmUser(self):
        self.BM_Usuario = BM_Usuario()
        self.BM_Usuario.show()
        
    def mostrarNewArea(self):
        self.newArea = NewArea()
        self.newArea.show()

    def mostrarNewMovimiento(self):
        self.newMovimiento = NewMovimiento()
        self.newMovimiento.show()
        self.ui.products_btn_movimiento.setFocus()
    

    ## Listar Productos en la tabla
    def listarProductos(self):
        products = p.listar_prod()
        n = p.contar_filas()
        self.ui.tableWidget_stock_2.setRowCount(n)
        tableRow = 0

        for row in products:
                print("row",row)
                self.ui.tableWidget_stock_2.setItem(
                    tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
                self.ui.tableWidget_stock_2.setItem(
                    tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
                self.ui.tableWidget_stock_2.setItem(
                    tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
                self.ui.tableWidget_stock_2.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                self.ui.tableWidget_stock_2.setItem(
                    tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

                tableRow += 1

    ## Listar Movimientos en la tabla
    def listarMovimientos(self):
        movimientos = m.listar_movimientos()
        n = m.contar_filas()
        print(movimientos)
        self.ui.tableWidget_movimientos_2.setRowCount(n)
        tableRow = 0
        for row in movimientos:
            self.ui.tableWidget_movimientos_2.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_movimientos_2.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_movimientos_2.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_movimientos_2.setItem(
                tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_movimientos_2.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.ui.tableWidget_movimientos_2.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[5])))

            tableRow += 1


    ## Listar lotes en la tabla
    def listarMovimientos(self):
        lotes = l.listar_lotes()
        n = l.contar_filas()
        print(lotes)
        self.ui.tableWidget_lotes.setRowCount(n)
        tableRow = 0
        for row in lotes:
            self.ui.tableWidget_lotes.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_lotes.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_lotes.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_lotes.setItem(
                tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_lotes.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1
  # Buscar productos a traves del input, por parámetro ingresado

    def buscarProducto(self):
        parametro = self.ui.buscar_input.text()
        products = p.productos.buscar_product(parametro)
        n = p.productos.buscar_product_rows(parametro)
        self.ui.tableWidget_stock_2.setRowCount(n)
        tableRow = 0
        for row in products:
            self.ui.tableWidget_stock_2.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_stock_2.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_stock_2.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.ui.tableWidget_stock_2.setItem(
                tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.ui.tableWidget_stock_2.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1

   

    def seleccionarProducto(self):
        global productId
        global defaultImg
        listaProductos = []
        for i in range(0,5):
            listaProductos.append(self.ui.tableWidget_stock_2.item(self.ui.tableWidget_stock_2.currentRow(),i).text())
            productId = listaProductos[0]
  

    def agregarAreaCreada(self):

        areas = ar.Area.listar_area()
        n = ar.Area.contar_filas()
        child = self.ui.verticalLayout_7.count()
        if child == n:
            pass
        else:
            
                btn1 = QtWidgets.QPushButton(self.ui.frame_5)
                btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                btn1.setStyleSheet("QPushButton{\n"
            "border:none;\n"
            "font-family: Roboto;\n"
            "border-radius:5px;\n"
            "text-align: center;\n"
            "color: #282830 ;\n"
            "padding:5px;\n"
            "\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: rgba(105, 105, 226, 50);\n"
            "}")
                btn1.setObjectName("btn_{areas[-1][0]}")
                btn1.setText(areas[-1][0])
                self.ui.verticalLayout_7.addWidget(btn1)
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                btn1.setFont(font)

    ## Agregar botones dinamicamente
    def agregarBtnAreas(self):

        areas = ar.Area.listar_area()
        i = 0
        n = ar.Area.contar_filas()
        child = self.ui.verticalLayout_7.count()
        print(",,,,,,,,,,,,,,,,,",child)
        
        for area in areas:
                btn1 = QtWidgets.QPushButton(self.ui.frame_5)
                btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                btn1.setStyleSheet("QPushButton{\n"
            "border:none;\n"
            "font-family: Roboto;\n"
            "border-radius:5px;\n"
            "text-align: center;\n"
            "color: #282830 ;\n"
            "padding:5px;\n"
            "\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "    background-color: rgba(105, 105, 226, 50);\n"
            "}")
                btn1.setObjectName("btn_{area[0]}")
                btn1.setText(area[0])
                self.ui.verticalLayout_7.addWidget(btn1)
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                btn1.setFont(font)
                i+=1


    ## Mostrar Areas graficamente

    def mostrarAreas(self):
        child = self.ui.verticalLayout_7.count()
        areas = ar.Area.listar_area()
        n = ar.Area.contar_filas()
        i = 1
        arr = []

        for a in areas:
                
                frame = QtWidgets.QFrame(self.ui.frame_3)
                frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                frame.setFrameShadow(QtWidgets.QFrame.Raised)
                frame.setObjectName(a[0])
                verticalLayout = QtWidgets.QVBoxLayout(frame)
                verticalLayout.setObjectName("verticalLay{i}")
                verticalLayout.addWidget(frame)
                self.btn = QPushButton(frame)
                self.btn.setText("Ver")
                self.btn.setObjectName('Button%s' % a[0])
                self.btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.btn.setMinimumSize(QtCore.QSize(30,30))
                self.label = QtWidgets.QLabel(frame)
                self.btn.released.connect(self.button_released)

                self.ui.gridLayout.addWidget(frame, 1, i, 1, 1)
                font = QtGui.QFont()
                font.setFamily("Roboto")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.label.setFont(font)
                self.label.setText(a[0])
                self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
                self.label.setStyleSheet("QLabel{\n"  "border:none;\n""}")
                self.label.setMaximumSize(QtCore.QSize(300, 250))
                verticalLayout.addWidget(self.label)
                verticalLayout.addWidget(self.btn)

                if child < n: 
                    if child == n-1:
                        self.agregarAreaCreada()
                    else:
                        self.btn2 = QtWidgets.QPushButton(self.ui.frame_5)
                        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        self.btn2.setStyleSheet("QPushButton{\n"
                    "border:none;\n"
                    "font-family: Roboto;\n"
                    "border-radius:5px;\n"
                    "text-align: center;\n"
                    "color: #282830 ;\n"
                    "padding:5px;\n"
                    "\n"
                    "\n"
                    "}\n"
                    "\n"
                    "QPushButton:hover{\n"
                    "    background-color: rgba(105, 105, 226, 50);\n"
                    "}")
                        self.btn2.setObjectName("Button%s" % a[0])
                        self.btn2.setText(a[0])
                        self.ui.verticalLayout_7.addWidget(self.btn2)
                        font = QtGui.QFont()
                        font.setFamily("Roboto")
                        font.setPointSize(10)
                        font.setBold(True)
                        font.setWeight(75)
                        self.btn2.setFont(font)
                        self.btn2.released.connect(self.button_released)

                        arr.append(self.btn2)
                i+=1
        return(arr)
    
    def button_released(self):

        pp = p.listar_prod()
        atributos = list(pp[0])
        print(atributos[7])
        self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_area)
        productos = p.listar_prod()
        sending_button = self.sender()
        print('%s Clicked!' % str(sending_button.objectName()))

        if str(sending_button.objectName()):
                pass

    def rellenarTabla(self,table):

        areas = ar.Area.listar_area()
        n = ar.Area.contarFilas()
        self.ui.table.setRowCount(n)
        tableRow = 0
        for row in areas:
            self.ui.table.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.table.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.table.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            if str(row[3]) == "b'1'":
                self.ui.table.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Admin"))
            else:
                self.ui.table.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Usuario"))

            self.ui.table.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1
    
                
                


    ## Listar Usuarios en la tabla

    def listarUsuarios(self):
        usuarios = u.listar_user()
        print("usuarios",usuarios)
        n = u.contar_filas()
        self.ui.tableWidget_usuarios.setRowCount(n)
        tableRow = 0
        for row in usuarios:
            self.ui.tableWidget_usuarios.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_usuarios.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_usuarios.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            if str(row[3]) == "1":
                self.ui.tableWidget_usuarios.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Administrador"))
            else:
                self.ui.tableWidget_usuarios.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Usuario"))

            self.ui.tableWidget_usuarios.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1
    
     # Seleccionar usuario al hacer click y abrir ventana

    def seleccionarusuario(self):
        global DNI
        seleccionarusuario = []
        for i in range(0,5):
            seleccionarusuario.append(self.ui.tableWidget_usuarios.item(self.ui.tableWidget_usuarios.currentRow(),i).text())
            DNI = seleccionarusuario[0]    
    
##Buscar Usuarios

    def buscarUsuarios(self):
       parametro = self.ui.lineEdit_3.text()
       products = u.usuarios.buscar_user(parametro)
       n = u.usuarios.buscar_user_rows(parametro)
       self.ui.tableWidget_usuarios.setRowCount(n)
       tableRow = 0
       for row in products:
          self.ui.tableWidget_usuarios.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
          self.ui.tableWidget_usuarios.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
          self.ui.tableWidget_usuarios.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
          if str(row[3])=="b'1'":
             self.ui.tableWidget_usuarios.setItem(tableRow, 3, QtWidgets.QTableWidgetItem("Admin"))
          else:
             self.ui.tableWidget_usuarios.setItem(tableRow, 3, QtWidgets.QTableWidgetItem("Usuario"))
          self.ui.tableWidget_usuarios.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

          tableRow += 1 


# Seleccionar DNI al hacer click y abrir ventana
 
    def SeleccionarDNI(self):
        global DNI
        SeleccionarDNI = []
        for i in range(0,5):
            SeleccionarDNI.append(self.ui.tableWidget_usuarios.item(self.ui.tableWidget_usuarios.currentRow(),i).text())
            DNI = SeleccionarDNI[0]
            print(DNI)
    


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
        #Subir foto btn
        self.ui.subirFoto_btn.clicked.connect(self.uploadImg)

        #Modificar producto btn
        self.ui.modificarprod_btn.clicked.connect(self.modificarProducto)

        #Eliminar producto btn
        self.ui.eliminarprod_btn.clicked.connect(self.borrarProducto)

        self.cbox()
        #Mostrar Ventana
        self.show()

    #Rellenar los campos con los atributos del producto seleccionado
    def rellenarCampos(self):
        global productId
        global codigoViejo
        global defaultImg
        producto = p.productos.mostrar_product(productId)
        atributos = list(producto[0])
        print(atributos)
        self.ui.codigo_input.setText(atributos[0])
        codigoViejo = atributos[0]
        self.ui.descripcion_input.setPlainText(atributos[3])
        self.ui.marca_input.setText(atributos[1])
        self.ui.ubicacion_input.setText(atributos[5])
        self.productImg = self.ui.label
        self.img = QPixmap("C:\proyecto-final\Interfaces\main\img/{0}".format(atributos[8]))
        self.productImg.setPixmap(self.img)
        defaultImg = atributos[8]
        self.ui.estado_cbox.setCurrentText(atributos[13])


        if str(atributos[7]) == "b'1'":
            self.ui.fragil_si.setChecked(1)
        else:
            self.ui.fragil_no.setChecked(1)

        self.ui.peso_num.setValue(atributos[9])
        self.ui.largo_num.setValue(atributos[10])
        self.ui.ancho_num.setValue(atributos[11])
        self.ui.altura_num.setValue(atributos[12])
        
        
    def modificarProducto(self):
        global productId
        global codigoViejo
        global defaultImg
        codigo = self.ui.codigo_input.text()
        descripcion = self.ui.descripcion_input.toPlainText()
        marca = self.ui.marca_input.text()
        ubicacion = self.ui.ubicacion_input.text()
        condicion = self.ui.estado_cbox.currentText()
        if self.ui.fragil_si.isChecked():
            fragil = "1"
        else :
            fragil = "0"

        peso = self.ui.peso_num.value()
        ancho = self.ui.ancho_num.value()
        altura = self.ui.altura_num.value()
        largo = self.ui.largo_num.value()
        foto = defaultImg
        p.productos.modificar_produc(codigoViejo,codigo,marca,descripcion,ubicacion,condicion,fragil,foto,peso,largo,ancho,altura)
        self.close()

    def borrarProducto(self):
        global productId
        qm = QMessageBox

        ret = qm.warning(self,'Esta acción es irreversible', "¿Estás seguro que quieres eliminar el producto?", qm.Yes | qm.No)
        if ret == qm.Yes:
            p.productos.borrar_producto(productId)
            self.close()
        
    def uploadImg(self):
      global defaultImg
      size =(256,256)
      self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
      if ok:
            defaultImg = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\proyecto-final\Interfaces\main\img/{0}".format(defaultImg))

    #def bm_user(self):
     #  self.ui.btn_.clicked.connect(lambda: self.ui.Pages_Widget.setCurrentWidget(self.ui.page_usuarios))
     # self.ui.label_de.mousePressEvent = self.clickD
     

    def cbox(self):
        areas = ar.Area.listar_area()
        for a in areas:
            self.ui.estado_cbox.addItem(a[0])


#############################################################  CLASS BM_USUARIOS ######################################################
 



class BM_Usuario(QMainWindow):

    def __init__(self):
        super(BM_Usuario, self).__init__()
        self.ui = bmu()
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

        #Subir foto btn
        #self.ui.subirFoto_btn.clicked.connect(self.uploadImg)

        #Modificar usuario btn
        self.ui.modificarprod_btn.clicked.connect(self.ModificarUsuario)

        #Eliminar usuario btn
        self.ui.eliminarprod_btn.clicked.connect(self.DarDeBajaUsuario)
        

        #Mostrar Ventana
        self.show()



    #Rellenar los campos con los atributos del producto seleccionado
    def rellenarCampos(self):
        global userid
        global DNI
        global DNI_Viejo
        #global defaultImg        
        usuario = u.usuarios.mostrar_user(DNI)
        print(usuario)
        atributos = list(usuario[0])
        DNI_Viejo = atributos[0]
        self.ui.dni_input.setText(atributos[0])
        self.ui.nombre_input_2.setText(atributos[1])
        self.ui.apellido_input.setText(atributos[2])
        self.ui.nacimiento_date.setDate(atributos[4])
        self.ui.puesto_input.setText(atributos[5])
        self.ui.mail_input.setText(atributos[7])

        
        if  str(atributos[3]) == "1":
            print("admin")
            self.ui.tipo_cb.setCurrentText("Administrador")

        else:
            self.ui.tipo_cb.setCurrentText("Usuario")
        
        """
        CAMBIAR BOTÓN PARA QUE INFORME SI SE DA DE ALTA O NO
        if str(atributos[6]) == "b'1'":
            self.ui.
        else:
            self.ui.fragil_no.setChecked(1)

        self.ui.peso_num.setValue(atributos[12])
        self.ui.ancho_num.setValue(atributos[13])
        self.ui.altura_num.setValue(atributos[14])
        """
        
    def ModificarUsuario(self):
        global DNI_Viejo
        dni = self.ui.dni_input.text()
        nombre = self.ui.nombre_input_2.text()
        apellido = self.ui.apellido_input.text()
        tipo = self.ui.tipo_cb.currentText()
        print("tpi",tipo)
        if tipo == "Administrador": 
            tipo = 1 
        else:
            tipo = 0
        nacimiento = self.ui.nacimiento_date.date().toString("yyyy/MM/dd")
        puesto = self.ui.puesto_input.text()
        mail = self.ui.mail_input.text()
        if self.ui.pass_input.text() != "" or self.ui.pass_rep_input.text != "":
            if self.ui.pass_input.text() == self.ui.pass_rep_input.text():
                u.usuarios.modificar_datos_user(DNI_Viejo,dni,nombre,apellido,tipo,puesto,nacimiento,mail)
                loginDB.cambiar_contrasena(DNI_Viejo,dni,self.ui.pass_input.text())
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Contraseñas diferentes")
                return None
        else:
            u.usuarios.modificar_datos_user(DNI_Viejo,dni,nombre,apellido,tipo,puesto,nacimiento,mail)

        self.close()
        
        

    def DarDeBajaUsuario(self):
        global DNI
        qm = QMessageBox

        ret = qm.warning(self,'Advertencia', "¿Está seguro que quieres dar de baja el usuario?", qm.Yes | qm.No)
        if ret == qm.Yes:
            u.usuarios.ab_usuario(DNI)
            self.close()


    def uploadImg(self):
      global defaultImg
      size =(256,256)
      self.filename,ok =QFileDialog.getOpenFileName(self,'Upload Image','','Image files (*.jpg *.png)')
      if ok:
            defaultImg = os.path.basename(self.filename)
            img=Image.open(self.filename)
            img=img.resize(size)
            img.save("C:\proyecto-final\Interfaces\main\img/{0}".format(defaultImg))


     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Modern()
    window.show()
    sys.exit(app.exec())
