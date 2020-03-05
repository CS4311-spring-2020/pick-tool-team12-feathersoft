from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class GraphView(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(50,50,1000,800)
        self.prompt = PositionPrompt()
        self.palette = GraphPalette()
        self.nodes = set()
        self.relationships = set()
        self.pos = None
        self.x = None
        self.y = None
        self.text = ""
        self.UI()

    def UI(self):
        self.menuBar = self.menuBar()
        self.addNode = self.menuBar.addMenu('Add Node')
        self.addNode.addAction(QIcon('red_circle.png'), 'Red Node')
        self.addNode.addAction(QIcon('blue_circle.png'), 'Blue Node')
        self.addNode.addAction(QIcon('white_circle.png'), 'White Node')
        self.addRelationship = self.menuBar.addMenu('Add Relationship')
        self.addRelationship = self.addRelationship.addAction(QIcon('relationship.png'), 'Relationship')
        self.deleteNode = self.menuBar.addMenu('Delete Node')
        self.deleteRelationship = self.menuBar.addMenu('Delete Relationship')
        self.editNode = self.menuBar.addMenu('Edit Node')
        self.editRelationship = self.menuBar.addMenu('Edit Relationship')
        self.export = self.menuBar.addMenu('Export')

        self.canvas = QPixmap(900,700)

        self.addNode.triggered[QAction].connect(self.node_prompt)
        self.prompt.draw_button.clicked.connect(self.draw_nodes)
        # self.show()

    def node_prompt(self,action):
        self.prompt.show()
        if self.text is not None: self.text = str(action.text())

    def paintEvent(self, event):

        if self.x is not None and self.y is not None:
            newnode = NodeWidget(25, QPoint(self.x, self.y), self.find_color(self.text))
            self.nodes.add(newnode)

        if self.pos is not None:
            self.nodes.add(NodeWidget(25,self.pos,Qt.red))

        for node in self.nodes:
            node.paint(QPainter(self))

        self.prompt.x_coordinate_line.clear()
        self.prompt.y_coordinate_line.clear()


    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.pos = QMouseEvent.pos()
            print(self.pos)
            self.update()

    def draw_nodes(self):
        self.x = int(self.prompt.x_coordinate_line.displayText())
        self.y = int(self.prompt.y_coordinate_line.displayText())
        self.update()
        self.prompt.close()

    def find_color(self, input):
        if input is not None:
            if 'Red' in input:
                return Qt.red
            elif 'Blue' in input:
                return Qt.blue
            else:
                return Qt.white



class GraphPalette(QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(100,200)

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red,Qt.SolidPattern))
        painter.drawEllipse(20,20,25,25)

        painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.drawEllipse(20, 80, 25, 25)

        painter.setPen(QPen(Qt.white, 2, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.drawEllipse(20, 140, 25, 25)


class PositionPrompt(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(400,300,310,300)
        self.layout = QVBoxLayout()
        self.setWindowTitle('Select Position')
        self.x_coordinate_label = QLabel('X Pos:',self)
        self.x_coordinate_label.move(10,80)
        self.x_coordinate_line = QLineEdit(self)
        self.x_coordinate_line.setFixedWidth(200)
        self.x_coordinate_line.move(50,80)
        self.y_coordinate_label = QLabel('Y Pos:',self)
        self.y_coordinate_line = QLineEdit(self)
        self.y_coordinate_line.setFixedWidth(200)
        self.y_coordinate_line.move(50, 150)
        self.y_coordinate_label.move(10,150)
        self.draw_button = QPushButton('Draw Node',self)
        self.draw_button.move(100, 250)
        self.layout.addWidget(self.x_coordinate_line)
        self.layout.addWidget(self.y_coordinate_line)
        self.layout.addWidget(self.draw_button)


class Shape(QGraphicsItem):
    def __init__(self, length, position, color, parent=None):
        super().__init__()
        self.color = color
        self.position = position
        self.length = length

    def paint(self, painter):
        pass




class NodeWidget(Shape):

    def __init__(self, length, position, color):
        super().__init__(length,position,color)
        #self.setMouseTracking(True)


    def paint(self, painter):
        if not painter.isActive():
            return
        painter.save()
        painter.setPen(QPen(self.color, 4, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        x, y = self.position.x(), self.position.y()
        painter.drawEllipse(x, y, self.length, self.length)
        painter.restore()

    # def mousePressEvent(self, QMouseEvent):
    #     if QMouseEvent.button() == Qt.ArrowCursor:
    #         print('hello')










if __name__ == '__main__':
     App = QApplication(sys.argv)
     window = GraphView()
     window.show()
     sys.exit(App.exec())