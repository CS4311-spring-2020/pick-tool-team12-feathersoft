from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QDMGraphicsNode(QGraphicsItem):

    def __init__(self, node, parent=None):
        super().__init__(parent)

        self.node = node
        self.content = self.node.content

        self._title_color = Qt.white
        self._title_font = QFont('Ubuntu', 10)

        self.width = 180
        self.height = 240
        self.title_height = 24
        self.padding = 0.0
        self.edge_size = 10.0

        self._pen_default = QPen(QColor(Qt.red))
        self._pen_selected = QPen(QColor(Qt.blue))

        self.brush_title = QBrush(QColor(Qt.darkGray))
        self.brush_background = QBrush(QColor(Qt.gray))


        self.initTitle()
        self.title = self.node.title

        # init contents
        self.initContents()

        self.initUI()

    def boundingRect(self):
      return QRectF(
          0,
          0,
          2 * self.edge_size + self.width,
          2 * self.edge_size + self.height
      )

    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)
        self.title_item.setPos(self.padding, 0)
        self.title_item.setTextWidth(
            self.width
            - 2 * self.padding
        )

    def initContents(self):
        self.grContent = QGraphicsProxyWidget(self)
        self.content.setGeometry(self.edge_size, self.title_height + self.edge_size,
                                 self.width - 2*self.edge_size, self.height - 2 * self.edge_size - self.title_height)

        self.grContent.setWidget(self.content)

    @property
    def title(self): return self._title
    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self.title)


    def paint(self, QPainter, QStyleOptionGraphicsItem, widget=None):

        # title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0,0,self.width, self.title_height, self.edge_size,self.edge_size)
        path_title.addRect(0,self.title_height-self.edge_size, self.edge_size,self.edge_size)
        path_title.addRect(self.width - self.edge_size,self.title_height-self.edge_size, self.edge_size,self.edge_size)
        QPainter.setPen(Qt.NoPen)
        QPainter.setBrush(self.brush_title)
        QPainter.drawPath(path_title.simplified())


        # content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0,self.title_height, self.width, self.height - self.title_height, self.edge_size, self.edge_size)
        path_content.addRect(0, self.title_height, self.edge_size,self.edge_size)
        path_content.addRect(self.width - self.edge_size, self.title_height, self.edge_size,self.edge_size)
        QPainter.setPen(Qt.NoPen)
        QPainter.setBrush(self.brush_background)
        QPainter.drawPath(path_content.simplified())

        # outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(0,0,self.width,self.height, self.edge_size, self.edge_size)
        QPainter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        QPainter.setBrush(Qt.NoBrush)
        QPainter.drawPath(path_outline.simplified())


class Node():

    def __init__(self, scene, title):
        self.scene = scene

        self.title = title

        self.content = QDMNodeContentWidget()
        self.grNode = QDMGraphicsNode(self)

        self.scene.addNode(self)
        self.scene.grScene.addItem(self.grNode)

        self.grNode.title = title

        self.input = []
        self.output = []


class QDMNodeContentWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)

        self.wdg_label = QLabel('Some Title')
        self.layout.addWidget(self.wdg_label)
        self.layout.addWidget(QTextEdit('foo'))


