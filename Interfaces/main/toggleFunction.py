from PyQt5.sip import enableoverflowchecking
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QMainWindow

from main import *

class UIFunctions(QMainWindow):
    
    def toggleMenu(self, maxWidth, enable):

        if enable:

            #GET WIDTH 
            width = self.ui.slide_bar.width()
            maxExtend = maxWidth
            standard = 0

            #SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            #ANIMACIÓN
        self.animation = QPropertyAnimation(self.ui.slide_bar, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()
   