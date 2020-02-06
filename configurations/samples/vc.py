import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import os


class VectorConfiguration(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 482, 432)
        self.setWindowTitle("Vector Configuration")
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vectorConfigLabel = QLabel('Vector Configuration',self)
        self.vectorConfigLabel.setObjectName(u"vectorConfigLabel")
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.vectorConfigLabel.setFont(font)

        self.gridLayout.addWidget(self.vectorConfigLabel,0,0,1,2)

        self.editButton = QPushButton('Edit Vector', self)
        self.editButton.setObjectName(u"editButton")

        self.gridLayout.addWidget(self.editButton,7,0,1,1)

        self.addVectorButton = QPushButton('Add Vector',self)
        self.addVectorButton.setObjectName(u"addVectorButton")

        self.gridLayout.addWidget(self.addVectorButton,7,1,1,1)

        self.tableWidget = QTableWidget(self)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem(QIcon('down_arrow.png'),'Vector Name')
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem(QIcon('down_arrow.png'),'Description')
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem('Select')
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem('Vector 1')
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem('Vector 2')
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem('Vector 3')
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem('DOS Attack')
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem('Denial of Service')
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem('MITM')
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem('Man In The Middle')
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem('SQL INJECTION')
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem('SQL Injection')
        self.tableWidget.setItem(2, 1, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget,1,0,6,4)
        self.deleteButton = QPushButton('Delete Vector',self)
        self.gridLayout.addWidget(self.deleteButton,7,2,1,2)
        self.verticalScrollBar = QScrollBar(self)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)
        self.gridLayout.addWidget(self.verticalScrollBar,1,4,6,1)
        self.show()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = VectorConfiguration()
    sys.exit(App.exec())