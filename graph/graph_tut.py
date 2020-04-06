from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
class Window(QMainWindow):


    def __init__(self):
        super().__init__()

        self.title = 'Pyqt5 QGraphic View'
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.initUi()

    def initUi(self):

       # Make the scene to draw our widgets on
       self.scene = QGraphicsScene()

       redBrush = QBrush(Qt.red)
       blueBrush = QBrush(Qt.blue)
       blackPen = QPen(Qt.black)

       ellipse = self.scene.addEllipse(10,10, 200, 200, blackPen, redBrush)

       ellipse.setFlag(QGraphicsItem.ItemIsMovable,QGraphicsItem.ItemIsSelectable)
       #pm = QPixmap(os.path.abspath(os.path.abspath('icons/blue_circle.png')))
       #pm = pm.scaled(QSize(128,128))
       #item = QGraphicsPixmapItem()
       #item.setPixmap(pm)
       #item.setFlag(QGraphicsPixmapItem.ItemIsMovable)

       #self.scene.addItem(item)
       self.scene.addItem(TestNode('C:/Users/jayjj/Documents/Spring 2020/Software 2/pick-tool-team12-feathersoft/configurations/icons/folder.png',self.scene))

       self.view = QGraphicsView(self.scene, self)
       self.view.setGeometry(0,0,680,500)
       self.setWindowTitle(self.title)
       self.setGeometry(self.top,self.left,self.width,self.height)
       self.show()


class TestNode(QGraphicsPixmapItem):
    def __init__(self, image,scene):
        super().__init__()
        self.setFlags(QGraphicsPixmapItem.ItemIsMovable)
        self.pixmap = QPixmap(os.path.abspath(image)).scaled(QSize(200,200))
        self.setPixmap(self.pixmap)
        self.scene = scene

        painter = QPainter(self.pixmap)
        painter.setFont(QFont('Arial'))
        painter.drawText(QPoint(100,100),'Hello')

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            pass
        else:
           pass


    def mouseReleaseEvent(self, QMouseEvent):
        painter = QPainter()
        painter.setBrush(QBrush(Qt.black))
        painter.drawLine(self.pos(),QMouseEvent.pos())






if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Window()
    test.show()
    sys.exit(app.exec())