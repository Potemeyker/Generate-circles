import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QGraphicsScene, QGraphicsView,
                             QGraphicsEllipseItem)
from PyQt5.QtGui import QColor


class CircleGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Random Circles Generator')
        self.setGeometry(100, 100, 400, 400)

        self.button = QPushButton('Generate Circle', self)
        self.button.clicked.connect(self.generate_circle)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)

        layout = QVBoxLayout(self)
        layout.addWidget(self.button)
        layout.addWidget(self.view)

    def generate_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setPos(random.randint(0, 400 - diameter), random.randint(0, 400 - diameter))
        circle.setBrush(color)

        self.scene.addItem(circle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleGenerator()
    window.show()
    sys.exit(app.exec_())
