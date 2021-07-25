import sys
from typing import Counter
from PyQt5 import QtCore
 # If it is pyqt5 use the following import
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
 
class CircularProgress(QWidget):
    counter = 0
    def __init__(self):
        super().__init__()  
                #Global
                 # Record angle
        self.angle=0
                 # This is for drawing, angle is the real angle
        self.drawAngle=self.angle
                 # Progress bar width
        self.lineWidth=18
                 # Timeline for animation
                #timer
        self.timer = QTimeLine(5000,self)
        self.timer.setFrameRange(0,360)
        self.timer.frameChanged.connect(self.progress)
        self.timer.start()
        

    def progress(self,frame):
        global counter
        self.angle = self.counter
        self.drawAngle = frame
        self.update()
        self.counter += 1
        if self.counter > 101:
            self.timer.stop()
 
    def paintEvent(self,event):
                 # There is a problem here, pyqt5 cannot implicitly convert QRect to QRectF (PySide2 can), so use QRectF directly
        the_rect=QRectF(100,100,200,200)
        if the_rect.isNull():
            return
                 # Paintbrush
        painter=QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing|QPainter.SmoothPixmapTransform,on=True)
                 # Mirror flip, so it is clockwise
        painter.setViewport(self.width(),0,-self.width(),self.height())
 
                 # path default OddEvenFill, this fills the intersecting part of the two circles
        the_path=QPainterPath()
        the_path.addEllipse(the_rect.adjusted(1,1,-1,-1))
        the_path.addEllipse(the_rect.adjusted( 
            1+self.lineWidth,1+self.lineWidth,-1-self.lineWidth,-1-self.lineWidth))
             #color inicial
        painter.fillPath(the_path,QColor(255,255,255,0))
 
                 # Radial gradient (parameters are the center point and the starting angle), by default it is calculated counterclockwise from the right
        the_gradient=QConicalGradient(the_rect.center(),90)
        the_angle=self.drawAngle/360
        the_gradient.setColorAt(0,QColor(17, 115, 255, 255))
        the_gradient.setColorAt(the_angle,QColor(17, 115, 255, 109))
        if the_angle+0.001<1:
            the_gradient.setColorAt(the_angle+0.001,QColor(0,0,0,0))
        painter.fillPath(the_path,the_gradient)
 
 
 
if __name__=="__main__":
    app=QApplication(sys.argv)
    w=CircularProgress()
    w.setWindowTitle("Gong Jianbo 1992")
    w.resize(400,400)
    w.show()
    sys.exit(app.exec_())