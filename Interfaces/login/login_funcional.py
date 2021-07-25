import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QFile
sys.path.append("..")
from login import Ui_MainWindow
from DB import index as i

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.login_btn.clicked.connect(self.verificacion)

    def verificacion(self):
            user = self.ui.user_login_input.text()
            password = self.ui.pass_login_input.text()
            usuario = i.verificar_usuario(user,password)
            if usuario == 1:
                pass
            else:
                QtWidgets.QMessageBox.critical(self, "Error", "Datos incorrectos")
                self.ui.user_login_input.setText("")
                self.ui.pass_login_input.setText("")
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())