import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChangeConfigurationWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(650, 300, 600, 400)
        self.setWindowTitle('Change Configuration')
        self.setMaximumSize(600, 400)
        self.ui()

    def ui(self):
        label = QLabel('CHANGE LIST', self)
        label.move(50, 70)
        text_area = QTextEdit(self)
        text_area.setFixedWidth(500)
        text_area.move(50,100)
        undo_btn = QPushButton('UNDO', self)
        undo_btn.move(50, 330)
        commit_btn = QPushButton('COMMIT', self)
        commit_btn.move(450,330)
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = ChangeConfigurationWindow()
    sys.exit(App.exec())