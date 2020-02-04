import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 850, 600)
        self.setWindowTitle("Graph Configuration")
        self.UI()

    def UI(self):

        mainImage = QLabel(self)
        mainImage.setPixmap(QPixmap('attackGraph.png'))
        mainImage.setGeometry(340,30,555,555)

        combobox = QComboBox(self)
        combobox.addItems(['Vectors:', '1', '2', '3'])
        combobox.setGeometry(250, 20, 70, 30)


        textWindow = QTextEdit(self)
        textWindow.setVerticalScrollBar(QScrollBar())
        textWindow.setGeometry(20,50,300,500)
        textWindow.setFontPointSize(12)
        textWindow.setText('This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.'
                           'This is an example description of the current vector selected. The description will repeat to show the vertical scroll bar.')

        mainMenu = QMenuBar(self)
        mainMenu.addMenu('Add node')
        mainMenu.addMenu('Add relationship')
        mainMenu.addMenu('Delete node')
        mainMenu.addMenu('Delete relationship')
        mainMenu.addMenu('Edit node')
        mainMenu.addMenu('Edit relationship')

        iconTitle = QLabel('Description:', self)
        iconTitle.setFont(QFont('MS Shell Dlg 2', 12))
        iconTitle.move(20,30)

        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())