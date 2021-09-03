import sys
import os
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
from bm_producto import BMProduct as bm
from bm_producto_ui import Ui_MainWindow as ui_bm
from bm_user import Ui_MainWindow as bmu 

sys.path.append("C:\\proyecto-final\\CLASES\\")
import productos as pr
sys.path.append("C:\\proyecto-final\\CLASES\\")
import usuarios as u
import productos as p



defaultImg = ""
codigoViejo = ""
DNI_Viejo = ""
DNI = ""

class Modern(QMainWindow):

    def __init__(self):
        super(Modern, self).__init__()
        self.ui = Ui_MainWindow()
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
        ###################### ABRIR/CERRAR BARRA LATERAL #########################
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        self.ui.products_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.product_subpage))

        self.ui.users_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_usuarios))
        self.ui.users_btn.clicked.connect(
            lambda: self.ui.stackedWidget_3.setCurrentWidget(self.ui.user_subpage))
        self.ui.users_btn.clicked.connect(self.listarUsuarios)

        self.ui.deposito_btn.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_deposito))

        self.ui.products_btn_stock.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_stock))
        self.ui.products_btn_movimiento.clicked.connect(lambda: self.ui.stackedWidget_main.setCurrentWidget(self.ui.page_movimientos))

        self.ui.product_new_btn.clicked.connect(self.mostrarNewProduct)
        self.ui.user_new_btn.clicked.connect(self.mostrarNewUser)
    
        # Listamos productos al iniciar la ventana
        self.listarProductos(self.ui.tableWidget_stock_2)

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
        self.BM_Usuario = BM_Usuario ()
        self.BM_Usuario.show()
        
    def listarUsuarios(self):
        usuarios = u.listar_user()
        n = u.contar_filas()
        self.ui.tableWidget_3.setRowCount(n)
        tableRow = 0
        for row in usuarios:
            self.ui.tableWidget_3.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.ui.tableWidget_3.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.ui.tableWidget_3.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            if str(row[3]) == "b'1'":
                self.ui.tableWidget_3.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Admin"))
            else:
                self.ui.tableWidget_3.setItem(
                    tableRow, 3, QtWidgets.QTableWidgetItem("Usuario"))

            self.ui.tableWidget_3.setItem(
                tableRow, 4, QtWidgets.QTableWidgetItem(str(row[4])))

            tableRow += 1

    def listarProductos(self,tablewidget):
        products = p.listar_prod()
        n = p.contar_filas()
        tablewidget.setRowCount(n)
        tableRow = 0
        for row in products:
            tablewidget.setItem(
                tableRow, 0, QtWidgets.QTableWidgetItem(row[0]))
            tablewidget.setItem(
                tableRow, 1, QtWidgets.QTableWidgetItem(row[1]))
            tablewidget.setItem(
                tableRow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablewidget.setItem(
                tableRow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            tablewidget.setItem(
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
        self.ui.nombre_input.setText(atributos[1])
        self.ui.marca_input.setText(atributos[2])
        self.ui.venc_date.setDate(atributos[4])
        self.ui.cantidad_num.setValue(atributos[3])
        self.ui.descripcion_input.setText(atributos[5])
        self.ui.ubicacion_input.setText(atributos[6])
        self.productImg = self.ui.label
        self.img = QPixmap("C:\proyecto-final\Interfaces\main\img/{0}".format(atributos[7]))
        self.productImg.setPixmap(self.img)
        defaultImg = atributos[7]
        self.ui.lote_num.setValue(atributos[8])
        
        if  str(atributos[9]) == "b'1'":
            print("1")
            self.ui.condicion_cbox.setCurrentText("Refrigerado")

        elif str(atributos[10]) == "b'1'":
            print("1")
            self.ui.condicion_cbox.setCurrentText("Inflamable")
        else:
            self.ui.condicion_cbox.setCurrentText("Ninguna")
        
        if str(atributos[11]) == "b'1'":
            self.ui.fragil_si.setChecked(1)
        else:
            self.ui.fragil_no.setChecked(1)

        self.ui.peso_num.setValue(atributos[12])
        self.ui.largo_num.setValue(atributos[13])
        self.ui.ancho_num.setValue(atributos[14])
        self.ui.altura_num.setValue(atributos[15])
        
    def modificarProducto(self):
        global codigoViejo
        global defaultImg
        codigo = self.ui.codigo_input.text()
        nombre = self.ui.nombre_input.text()
        descripcion = self.ui.descripcion_input.toPlainText()
        cantidad = self.ui.cantidad_num.value()
        marca = self.ui.marca_input.text()
        ubicacion = self.ui.ubicacion_input.text()
        venc = self.ui.venc_date.date().toString("yyyy/MM/dd")
        lote = self.ui.lote_num.value()
        if self.ui.fragil_si.isChecked():
            fragil = "1"
        else :
            fragil = "0"

        condicion = self.ui.condicion_cbox.currentText()

        if condicion=="Refrigerado":
            refri=1
            infla=0
        elif condicion=="Inflamable": 
            refri=0
            infla=1
        else:
            refri=0
            infla=0

        peso = self.ui.peso_num.value()
        ancho = self.ui.ancho_num.value()
        altura = self.ui.altura_num.value()
        largo = self.ui.largo_num.value()
        foto = defaultImg
        print(lote,largo,ubicacion)
        p.productos.modificar_produc(codigoViejo,codigo,nombre,marca,cantidad,ubicacion,descripcion,lote,venc,refri,infla,fragil,foto,peso,largo,ancho,altura)
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
        self.ui.pushButton_modificar_usuario.clicked.connect(self.ModificarUsuario)

        #Eliminar usuario btn
        self.ui.pushButton_eliminar_usuario.clicked.connect(self.DarDeBajaUsuario)
        

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
        self.ui.nombre_input.setText(atributos[1])
        self.ui.apellido_input.setText(atributos[2])
        self.ui.nacimiento_date.setDate(atributos[4])
        self.ui.puesto_input.setText(atributos[5])
        self.ui.mail_input.setText(atributos[7])

        
        if  str(atributos[3]) == "b'1'":
            
            self.ui.tipo_cb.setCurrentText("Admin")

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
        nombre = self.ui.nombre_input.text()
        apellido = self.ui.apellido_input.text()
        tipo = self.ui.tipo_cb.currentText()
        if tipo == "admin": 
            tipo = 1 
        else:
            tipo = 0
        nacimiento = self.ui.nacimiento_date.date().toString("yyyy/MM/dd")
        puesto = self.ui.puesto_input.text()
        mail = self.ui.mail_input.text()
        if self.ui.pass_input.text() != "" or self.ui.pass_rep_input.text != "":
            if self.ui.pass_input.text() == self.ui.pass_rep_input.text():
                u.usuarios.modificar_datos_user(DNI_Viejo,dni,nombre,apellido,tipo,puesto,nacimiento,mail)
                login.cambiar_conrasena(DNI_Viejo,dni,self.ui.pass_input.text())
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


  
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Modern()
    window.show()
    sys.exit(app.exec())