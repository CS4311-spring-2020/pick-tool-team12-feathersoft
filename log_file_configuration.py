import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle("Log File Configuration")
        self.setMaximumSize(800,600)
        self.UI()

    def UI(self):
        mainMenu = QMenuBar(self)
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')

        text = QLabel('Log File Configuration', self)
        text.setFont(QFont('MS Shell Dlg 2', 20))
        text.move(50,50)
        vbox = QVBoxLayout()
        table = QTableWidget(self)
        table.setColumnCount(5)
        table.setRowCount(20)
        table.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('up-down-arrow.png'), "List Number"))
        table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('up-down-arrow.png'), "Log Entry Timestamp"))
        table.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('up-down-arrow.png'), "Log Entry Event"))
        table.setHorizontalHeaderItem(3,QTableWidgetItem("Vector"))
        table.setHorizontalHeaderItem(4,QTableWidgetItem(""))

        header = table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        for i in range(table.rowCount()):
            table.setVerticalHeaderItem(i,QTableWidgetItem(''))
        log = [line.split(' ') for line in open('dummy_log.txt').readlines()]
        print(log[0][1])
        for i in range(len(log)):
            table.setItem(i,0,QTableWidgetItem(str(i + 1)))
            table.setItem(i,1,QTableWidgetItem(str(log[i][0])))
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            combobox = QComboBox()
            combobox.addItems(['','1','2','3'])
            table.setCellWidget(i,3,combobox)
            table.setItem(i,4,checkbox)

        table.setGeometry(50,100,700, 450)
        vbox.addWidget(table)
        #self.setLayout(vbox)
        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())