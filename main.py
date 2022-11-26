import sys

import random
from PyQt5 import uic
from UI import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.drawButton.clicked.connect(self.click)
        self.draw = False

    def click(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            x, y = random.randint(50, 550), random.randint(50, 550)
            radius = random.randint(0, 150)
            painter = QPainter()
            r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            painter.begin(self)
            painter.setPen(QColor(r, g, b))
            painter.setBrush(QColor(r, g, b))
            painter.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
