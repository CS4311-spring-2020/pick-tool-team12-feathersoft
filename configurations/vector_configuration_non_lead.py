import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class VectorDBConfigurationNonLead(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Vector Database Configuration")
        self.UI()

    def UI(self):
        # mainMenu = QMenuBar(self)
        # mainMenu.addMenu('File')
        # mainMenu.addMenu('Edit')
        # mainMenu.addMenu('View')
        # mainMenu.addMenu('Search')
        # mainMenu.addMenu('Tools')
        # mainMenu.addMenu('Help')

        textLead = QLabel('Connection status to lead:')
        textLead.setFont(QFont('MS Shell Dlg 2', 14))
        textLead.move(30,30)

        pullText = QLabel('Pulled Vector DB Table', self)
        pullText.setFont(QFont('MS Shell Dlg 2', 12))
        pullText.move(30,70)

        pushText = QLabel('Pushed Vector DB Table', self)
        pushText.setFont(QFont('MS Shell Dlg 2', 12))
        pushText.move(500, 70)

        textStatus = QLabel('Connected')
        textStatus.setFont(QFont('MS Shell Dlg 2', 14))
        textStatus.move(300, 30)

        layout = QVBoxLayout()
        
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(15)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Vector"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Description"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem(""))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem("Graph"))

        self.table2 = QTableWidget(self)
        self.table2.setColumnCount(4)
        self.table2.setRowCount(15)
        self.table2.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Vector"))
        self.table2.setHorizontalHeaderItem(1, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Description"))
        self.table2.setHorizontalHeaderItem(2, QTableWidgetItem(""))
        self.table2.setHorizontalHeaderItem(3, QTableWidgetItem("Graph"))

        self.header = self.table.horizontalHeader()
        self.header.setStretchLastSection(True)
        for i in range(self.table.columnCount()):
            self.header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.header2 = self.table2.horizontalHeader()
        self.header2.setStretchLastSection(True)

        self.header2.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.header2.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        for i in range(self.table.rowCount()):

            checkbox_Push = QTableWidgetItem()
            checkbox_Push.setCheckState(Qt.Unchecked)
            combobox_Push = QComboBox()
            combobox_Push.addItems(['','1','2','3'])

            tableitem_Push = QComboBox()
            tableitem_Push.addItems(['', '1', '2', '3'])

            tableitem_2_Push = QTableWidgetItem()
            tableitem_2_Push.setData(Qt.DisplayRole, 'This is the example of text')


            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            combobox = QComboBox()
            combobox.addItems(['', '1', '2', '3'])

            tableitem = QComboBox()
            tableitem.addItems(['', '1', '2', '3'])

            tableitem_2 = QTableWidgetItem()
            tableitem_2.setData(Qt.DisplayRole, 'This is the example of text')


            self.table.setCellWidget(i,0,tableitem)
            self.table.setItem(i, 1, tableitem_2)
            self.table.setCellWidget(i,3,combobox)
            self.table.setItem(i,2,checkbox)

            self.table2.setCellWidget(i, 0, tableitem_Push)
            self.table2.setItem(i, 1, tableitem_2_Push)
            self.table2.setCellWidget(i, 3, combobox_Push)
            self.table2.setItem(i, 2, checkbox_Push)

        # self.table.setGeometry(500,100,400, 300)
        # self.table2.setGeometry(30,100,400, 300)


        buttonPush = QPushButton(self)
        buttonPush.setGeometry(350,65,70,30)
        buttonPush.setText('Push')

        buttonPull = QPushButton(self)
        buttonPull.setGeometry(820, 65, 70, 30)
        buttonPull.setText('Pull')

        buttonCommit = QPushButton(self)
        buttonCommit.setGeometry(820, 30, 70, 30)
        buttonCommit.setText('Commit')

        table1Layout = QVBoxLayout()
        table2Layout = QVBoxLayout()
        table1Layout.addWidget(textLead)
        table1Layout.addWidget(pushText)
        table1Layout.addWidget(self.table)
        button_widget1 = QWidget()
        button_widget1.setLayout(QHBoxLayout())
        button_widget1.layout().addWidget(buttonPush)
        space = QLabel('')

        table1Layout.addWidget(button_widget1)


        table2Layout.addWidget(pullText)
        table2Layout.addWidget(self.table2)

        button_widget2 = QWidget()
        button_widget2.setLayout(QHBoxLayout())
        button_widget2.layout().addWidget(buttonPull)
        button_widget2.layout().addWidget(buttonCommit)
        table2Layout.addWidget(button_widget2)


        layout.addLayout(table1Layout)
        layout.addLayout(table2Layout)
        layout.setSpacing(10)
        self.setLayout(layout)

        #self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = VectorDBConfigurationNonLead()
    sys.exit(App.exec())