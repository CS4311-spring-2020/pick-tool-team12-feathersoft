import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class GraphConfiguration(QMainWindow):
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

        self.addToolBar(Qt.RightToolBarArea, graphics_toolbar)
        self.setCentralWidget(NodeEditorWindow())

    def do_nothing(self):
        pass


class NodeEditorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setGeometry(200,200,800,600)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # Create graphics scene
        self.grScene = QGraphicsScene()

        # Create graphics view
        self.view = QGraphicsView(self)
        self.view.setScene(self.grScene)
        self.setWindowTitle('Node Editor')

        self.layout.addWidget(self.view)

        self.show()







if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = GraphConfiguration()
    sys.exit(App.exec())