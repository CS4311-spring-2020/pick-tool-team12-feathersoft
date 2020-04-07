import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from configurations.node_scene import *
from configurations.node_graphics_scene import *
from configurations.node_graphics_view import QDMGraphicsView
from configurations.graph_node import *



class GraphConfigurationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 850, 600)
        self.setWindowTitle("Graph Configuration")
        self.UI()

    def UI(self):
        graphics_toolbar = QToolBar('PMR')
        graphics_toolbar.addAction('Add Node', self.do_nothing)
        graphics_toolbar.addAction('Delete Node', self.do_nothing)
        graphics_toolbar.addAction('Edit Node', self.do_nothing)
        graphics_toolbar.addAction('Set Node Color',self.do_nothing)
        self.window = NodeEditorWindow()
        self.addToolBar(Qt.RightToolBarArea, graphics_toolbar)
        self.setCentralWidget(self.window)

    def do_nothing(self):
        pass


class NodeEditorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()



    def initUI(self):
        self.setGeometry(200,200,800,600)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # Create graphics scene
        self.scene = Scene()

        # Creating the tablular view
        self.table = QTableWidget(0,10,self)
        #self.table.setFixedWidth(850)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node ID"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node Name"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node Timestamp"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node Description"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Log Entry Reference"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Log Creator'))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem('Event Type'))
        self.table.setHorizontalHeaderItem(7, QTableWidgetItem(QIcon('icon/unchecked.png'), "Icon Type"))
        self.table.setHorizontalHeaderItem(8, QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Source'))
        self.table.setHorizontalHeaderItem(9, QTableWidgetItem('Node Visibility'))
        self.header = self.table.horizontalHeader()
        for i in range(self.table.columnCount()):
            self.header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        # Creating the Graphical View
        self.layout.addWidget(self.table,1)
        self.view = QDMGraphicsView(self.scene.grScene,self)
        # self.view.setScene(self.scene)
        self.setWindowTitle('Node Editor')

        #self.scene.addNode(Node(self.scene,'title',[1,2,3],[1]))
        node = Node(self.scene, 'Node', icon='icons/red_circle.png', inputs=[1] * 30, outputs=[1] * 30)


        self.layout.addWidget(self.view,1)

        self.setWindowTitle('Graph View')
        self.setLayout(self.layout)

        #self.addDebugContent()

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        newAct = contextMenu.addAction("Add Node", self.addNode)
        openAct = contextMenu.addAction("Open")
        quitAct = contextMenu.addAction("Quit")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            self.close()

    def addNode(self):
        node = Node(self.scene, 'Node', icon='icons/red_circle.png', inputs=[1] * 30,outputs=[1] * 30)
        node.setPosition(100,200)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button == Qt.RightButton:
            self.contextMenuEvent(QMouseEvent)


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = GraphConfigurationWindow()
    sys.exit(App.exec())