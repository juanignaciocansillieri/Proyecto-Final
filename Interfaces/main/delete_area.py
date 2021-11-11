import sys
import os
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import create_user
from delete_area_ui import Ui_MainWindow
sys.path.append("C:\\proyecto-final\\CLASES\\")
import area as a

nombreViejo = ""
class BorrarArea(QMainWindow):

    def __init__(self):
        super(BorrarArea, self).__init__()
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
        self.ui.modificar_btn.clicked.connect(lambda: self.eliminarArea())
        self.rellenarCampo()


    def eliminarArea(self):

        area = self.ui.comboBox.currentText()
        qm = QMessageBox

        ret = qm.warning(self,'Esta acción es irreversible', "¿Estás seguro que quieres eliminar ésta área ?", qm.Yes | qm.No)
        if ret == qm.Yes:
         a.Area.eliminar_area(area)
         self.close()

    def rellenarCampo(self):
        areas = a.Area.listar_area()
        for area in areas:
            self.ui.comboBox.addItem(area[0])
        self.close()
