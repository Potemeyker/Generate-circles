import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QPushButton, QVBoxLayout
from PyQt5.QtGui import QColor
from PyQt5.uic import loadUi
import random


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        loadUi('UI.ui', self)

        self.button.clicked.connect(self.generate_circle)

        self.scene = QGraphicsScene(self)
        self.view.setScene(self.scene)

    def generate_circle(self):
        diameter = random.randint(10, 100)
        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setPos(random.randint(0, 400 - diameter), random.randint(0, 400 - diameter))
        circle.setBrush(QColor('yellow'))
        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec_())
