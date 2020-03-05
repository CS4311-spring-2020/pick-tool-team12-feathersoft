from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class NodeWidget(QWidget):

    def __init__(self,x,y,color,event):
        self.x = x
        self.y = y
        super().__init__()


    def paintEvent(self, QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(200, 0, 0))
        qp.drawText(20, 20, "Text at fixed coordinates")
        qp.setPen(QPen(Qt.red, 4))
        qp.drawEllipse(QPoint(self.x, self.y), 50, 50)
        qp.end()



