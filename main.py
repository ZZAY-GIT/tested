import sys

import random
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
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
            painter.begin(self)
            painter.setPen(QPen(Qt.yellow, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            painter.drawEllipse(x, y, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
