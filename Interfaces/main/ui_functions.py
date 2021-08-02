from PyQt5.sip import enableoverflowchecking
from PyQt5.QtCore import QPropertyAnimation
from PyQt5.QtWidgets import QMainWindow

from main import *

class UIFunctions(QMainWindow):
    
    def toggleMenu(self, maxWidth, enable):
        if enable:

            #GET WIDTH 
            width = self.ui.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 50

            #SET MAX WIDTH
            if width == 50:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            #ANIMACIÓN
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(widthExtended)
        self.animation.start()