import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import splash
import Img.img
from login_funcional import LoginWindow, Ui_MainWindow
import login_funcional as l
sys.path.append("..")
from DB import index as i

counter = 0



class Splash(QMainWindow):
    a = 0

    def __init__(self):
        super(Splash, self).__init__()
        self.ui = splash.Ui_MainWindow()
        self.ui.setupUi(self)
        ######## SACAR BARRA DE TÍTULO#####################
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        ############### ESTILO ################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        ###### INSERTAR CÍRCULO DE PROGRESO##############
        self.circle = CircularProgress()
        self.ui.horizontalLayout_3.addWidget(self.circle)
        ###### CERRAR SPLASH #############
        print(self.circle.timer.duration)
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)

        def timerEvent():
            global time
            self.time = self.time.addSecs(1)
            if str(self.time) == "PyQt5.QtCore.QTime(0, 0, 7)":
                self.close()
                self.login = LoginWindow()
        self.timer.timeout.connect(timerEvent)
        self.timer.start(1000)


class CircularProgress(QWidget):
    counter = 0
    b = 0
    a = 0

    def __init__(self):
        super().__init__()
        # Global
        self.contador = str(0)
        # Record angle
        self.angle = 0
        # This is for drawing, angle is the real angle
        self.drawAngle = self.angle
        # Progress bar width
        self.lineWidth = 18
        # Timeline for animation
        # timer
        self.timer = QTimeLine(7000, self)
        self.timer.setFrameRange(0, 360)
        self.timer.frameChanged.connect(self.progress)
        self.timer.start()
        print(self.drawAngle)

        ######## CREAR LABEL CONTADOR ##########
        self.label = QtWidgets.QLabel(self)
        self.label.move(287, 123)
        self.label.resize(110, 50)
        self.label.setStyleSheet("font-family: roboto;\n""font-weight: lighter;\n"
                                 "color:#FFF;\n"
                                 "font-size: 25px;\n"
                                 "\n"
                                 "background:none")

    def progress(self, frame):
        global counter
        global b
        self.angle = self.counter
        self.drawAngle = frame
        self.update()
        self.counter += 1
        if self.drawAngle == 360:
            self.b = 1
            self.timer.stop()
            self.close()
        if self.counter < 101:
            self.label.setText(str(self.counter) + "%")
        else:
            self.label.setText("100%")
            self.b = 1

    def paintEvent(self, event):
        if self.a == 0:
            # There is a problem here, pyqt5 cannot implicitly convert QRect to QRectF (PySide2 can), so use QRectF directly
            the_rect = QRectF(200, 50, 200, 200)
            # Paintbrush
            painter = QPainter(self)
            painter.setRenderHints(
                QPainter.Antialiasing | QPainter.SmoothPixmapTransform, on=True)
            # Mirror flip, so it is clockwise
            painter.setViewport(self.width(), 0, -self.width(), self.height())

            # path default OddEvenFill, this fills the intersecting part of the two circles
            the_path = QPainterPath()
            the_path.addEllipse(the_rect.adjusted(1, 1, -1, -1))
            the_path.addEllipse(the_rect.adjusted(
                1+self.lineWidth, 1+self.lineWidth, -1-self.lineWidth, -1-self.lineWidth))
            # color inicial
            painter.fillPath(the_path, QColor("#12151a"))

            # Radial gradient (parameters are the center point and the starting angle), by default it is calculated counterclockwise from the right
            the_gradient = QConicalGradient(the_rect.center(), 90)
            the_angle = self.drawAngle/360
            the_gradient.setColorAt(0, QColor(17, 115, 255, 255))
            the_gradient.setColorAt(the_angle, QColor(17, 115, 255, 109))
            if the_angle+0.001 < 1:
                the_gradient.setColorAt(the_angle+0.001, QColor(0, 0, 0, 0))
                painter.fillPath(the_path, the_gradient)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Splash()
    window.show()
    sys.exit(app.exec())
