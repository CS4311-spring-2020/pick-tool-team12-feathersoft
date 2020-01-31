import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QWidget):


    def __init__(self):
        super().__init__()
        self.setGeometry(650,300, 600,400)
        self.setWindowTitle('Export Configuration')
        self.setMaximumSize(600,400)
        self.UI()

    def UI(self):
        label = QLabel('EXPORT FORMAT',self)
        label.move(100,75)
        combobox = QComboBox(self)
        combobox.setFixedWidth(400)
        combobox.move(100,100)
        combobox.addItems(['', '.CSV', '.DOCX', '.TXT'])
        btn = QPushButton('Export',self)
        btn.move(480,330)
        self.show()




if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())