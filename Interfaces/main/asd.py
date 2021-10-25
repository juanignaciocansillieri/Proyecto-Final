from PyQt5 import QtCore, QtGui
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

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        def make_frame(text, parent):
            frame = QFrame(parent)
            frame.setFrameStyle(QFrame.StyledPanel)
            layout = QHBoxLayout(frame)
            label = QLabel(text, frame)
            label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(label)
            return frame
        self.splitter = QSplitter(self)
        for text in 'ONE TWO THREE'.split():
            self.splitter.addWidget(make_frame(text, self.splitter))
        self.stack = QStackedLayout()
        self.stack.addWidget(self.splitter)
        self.stack.addWidget(make_frame('FOUR', self))
        self.button = QPushButton('Switch', self)
        self.button.clicked.connect(
            lambda: self.stack.setCurrentIndex(
                int(self.stack.currentIndex() == 0)))
        layout = QVBoxLayout(self)
        layout.addLayout(self.stack)
        layout.addWidget(self.button)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.setGeometry(500, 300, 800, 500)
    window.show()
    sys.exit(app.exec_())