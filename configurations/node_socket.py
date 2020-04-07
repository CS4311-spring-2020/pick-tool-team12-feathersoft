from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


LEFT_TOP = 1
LEFT_MIDDLE = 1.5
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


class Socket():

    def __init__(self, node, index=0, position=LEFT_TOP):
        self.node = node
        self.index = index
        self.position = LEFT_TOP

        self.grSocket = QDMGraphicsSocket(self.node.grNode)
        self.grSocket.setPos(*self.node.getSocketPosition(index,position))



class QDMGraphicsSocket(QGraphicsItem):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.radius = 6
        self._outline_width = 1
        self._color_background = QColor("#FFFF2700")
        self._color_outline = QColor("#FF00")
        self._pen = QPen(self._color_outline)
        self._pen.setWidth(self._outline_width)
        self._brush = QBrush(self._color_background)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):

        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def boundingRect(self):
        return QRectF(
            -self.radius * self._outline_width,
            -self.radius * self._outline_width,
            2 * (self.radius + self._outline_width),
            2 * (self.radius + self._outline_width)
        )

    def mousePressEvent(self, QGraphicsSceneMouseEvent):
        print('i am a socket')


