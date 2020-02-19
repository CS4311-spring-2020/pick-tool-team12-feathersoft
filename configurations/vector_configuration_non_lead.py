import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class VectorDBConfigurationNonLeadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Vector Database Configuration")
        self.UI()

    def UI(self):
        mainMenu = QMenuBar(self)
        mainMenu.addMenu('File')
        mainMenu.addMenu('Edit')
        mainMenu.addMenu('View')
        mainMenu.addMenu('Search')
        mainMenu.addMenu('Tools')
        mainMenu.addMenu('Help')

        textLead = QLabel('Connection status to lead:', self)
        textLead.setFont(QFont('MS Shell Dlg 2', 14))
        textLead.move(30,30)

        pullText = QLabel('Pulled Vector DB Table', self)
        pullText.setFont(QFont('MS Shell Dlg 2', 12))
        pullText.move(30,70)

        pullText = QLabel('Pushed Vector DB Table', self)
        pullText.setFont(QFont('MS Shell Dlg 2', 12))
        pullText.move(500, 70)

        textStatus = QLabel('Connected', self)
        textStatus.setFont(QFont('MS Shell Dlg 2', 14))
        textStatus.move(300, 30)

        vbox = QVBoxLayout()
        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setRowCount(15)
        table.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('up-down-arrow.png'), "Vector"))
        table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('up-down-arrow.png'), "Description"))
        table.setHorizontalHeaderItem(2,QTableWidgetItem(""))
        table.setHorizontalHeaderItem(3,QTableWidgetItem("Graph"))

        table2 = QTableWidget(self)
        table2.setColumnCount(4)
        table2.setRowCount(15)
        table2.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('up-down-arrow.png'), "Vector"))
        table2.setHorizontalHeaderItem(1, QTableWidgetItem(QIcon('up-down-arrow.png'), "Description"))
        table2.setHorizontalHeaderItem(2, QTableWidgetItem(""))
        table2.setHorizontalHeaderItem(3, QTableWidgetItem("Graph"))

        header = table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        header = table2.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        for i in range(table.rowCount()):
            table.setVerticalHeaderItem(i,QTableWidgetItem(''))
            table2.setVerticalHeaderItem(i,QTableWidgetItem(''))
        log = [line.split(' ') for line in open('example.txt').readlines()]
        for i in range(len(log)):
            table.setItem(i,0,QTableWidgetItem(str(i + 1)))
            table.setItem(i,1,QTableWidgetItem(str(log[i][0])))
            table2.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            table2.setItem(i, 1, QTableWidgetItem(str(log[i][0])))

            checkbox_Push = QTableWidgetItem()
            checkbox_Push.setCheckState(Qt.Unchecked)
            combobox_Push = QComboBox()
            combobox_Push.addItems(['','1','2','3'])

            tableitem_Push = QTableWidget()
            tableitem_Push.setRowCount(4)
            tableitem_Push.setVerticalHeaderItem(0,QTableWidgetItem('Vector 1'))
            tableitem_Push.setVerticalHeaderItem(1, QTableWidgetItem('Vector 2'))
            tableitem_Push.setVerticalHeaderItem(2, QTableWidgetItem('Vector 3'))
            tableitem_Push.setVerticalHeaderItem(3, QTableWidgetItem('Vector 4'))

            tableitem_2_Push = QTableWidget()
            tableitem_2_Push.setRowCount(4)
            tableitem_2_Push.setVerticalHeaderItem(0, QTableWidgetItem('This is the example of text'))
            tableitem_2_Push.setVerticalHeaderItem(1, QTableWidgetItem('This text can be changed as presented'))
            tableitem_2_Push.setVerticalHeaderItem(2, QTableWidgetItem('There are several descriptions of Vectors'))
            tableitem_2_Push.setVerticalHeaderItem(3, QTableWidgetItem('Last description'))

            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            combobox = QComboBox()
            combobox.addItems(['', '1', '2', '3'])

            tableitem = QTableWidget()
            tableitem.setRowCount(4)
            tableitem.setVerticalHeaderItem(0, QTableWidgetItem('Vector 1'))
            tableitem.setVerticalHeaderItem(1, QTableWidgetItem('Vector 2'))
            tableitem.setVerticalHeaderItem(2, QTableWidgetItem('Vector 3'))
            tableitem.setVerticalHeaderItem(3, QTableWidgetItem('Vector 4'))

            tableitem_2 = QTableWidget()
            tableitem_2.setRowCount(4)
            tableitem_2.setVerticalHeaderItem(0, QTableWidgetItem('This is the example of text'))
            tableitem_2.setVerticalHeaderItem(1, QTableWidgetItem('This text can be changed as presented'))
            tableitem_2.setVerticalHeaderItem(2, QTableWidgetItem('There are several descriptions of Vectors'))
            tableitem_2.setVerticalHeaderItem(3, QTableWidgetItem('Last description'))

            table.setCellWidget(i,0,tableitem)
            table.setCellWidget(i, 1, tableitem_2)
            table.setCellWidget(i,3,combobox)
            table.setItem(i,2,checkbox)

            table2.setCellWidget(i, 0, tableitem_Push)
            table2.setCellWidget(i, 1, tableitem_2_Push)
            table2.setCellWidget(i, 3, combobox_Push)
            table2.setItem(i, 2, checkbox_Push)

        table.setGeometry(500,100,400, 300)
        table2.setGeometry(30,100,400, 300)


        buttonPush = QPushButton(self)
        buttonPush.setGeometry(350,65,70,30)
        buttonPush.setText('Pull')

        buttonPull = QPushButton(self)
        buttonPull.setGeometry(820, 65, 70, 30)
        buttonPull.setText('Push')

        vbox.addWidget(table)
        vbox.addWidget(table2)
        vbox.addWidget(buttonPush)
        vbox.addWidget(buttonPull)

        #self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = VectorDBConfigurationNonLeadWindow()
    sys.exit(App.exec())