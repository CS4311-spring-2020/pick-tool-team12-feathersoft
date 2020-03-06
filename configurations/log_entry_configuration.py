import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import os
import time
from configurations.filter_configuration import FilterConfiguration


"""This class will be used to build the UI Window for the Log Entry Configuration"""


class LogEntryConfiguration(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1000, 800)
        self.setWindowTitle("Log Entry Configuration")
        self.filter = FilterConfiguration()
        self.logs = [line.split(' ') for line in open('testlog.txt').readlines()]
        self.UI()

    def UI(self):
        # Creating the label for the window
        self.label = QLabel('Log Entry Configuration', self)
        # Setting the window's font
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.move(50,50)

        # Creating the layout that the window will be stored
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        # Creating the table
        self.table = QTableWidget(self)
        # Setting the amount of columns our table will have
        self.table.setColumnCount(8)
        # Setting the amount of row our table will have
        # Reading the dummy self.logs

        self.table.setRowCount(len(self.logs))
        # Setting the headers for each column
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('icons/up_arrow.png'), "List Number"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Log Entry Timestamp"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Log Entry Content"))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Host"))
        self.table.setHorizontalHeaderItem(4,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Source"))
        self.table.setHorizontalHeaderItem(5,QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Source type'))
        self.table.setHorizontalHeaderItem(6,QTableWidgetItem('Vector'))
        self.table.setHorizontalHeaderItem(7,QTableWidgetItem(QIcon('icon/unchecked.png'), "Select"))


        # Resizing the column headers to resize dynamically to the size of their contents
        self.header = self.table.horizontalHeader()
        for i in range(self.table.columnCount()):
            self.header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setProperty("showSortIndicator", False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setProperty("showSortIndicator", False)
        self.table.verticalHeader().setStretchLastSection(True)

        # Hiding the row labels in the table
        self.table.verticalHeader().setVisible(False)
        dummy = ['SQL Injection', 'Blue Team', 'Red Team', 'NULL']
        for i in range(len(self.logs)):
            # To store non string values in our table cells, we need to create widgets
            # that have a display role formatted for non string values.
            list_value = QTableWidgetItem()
            list_value.setData(Qt.DisplayRole, self.logs[i][0])
            time_stamp = QTableWidgetItem()
            time_stamp.setData(Qt.DisplayRole,self.logs[i][1])
            self.table.setItem(i,0,list_value)
            self.table.setItem(i,1,time_stamp)
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            combobox = QComboBox()
            combobox.addItems(['','1','2','3'])

            self.table.setItem(i,2,QTableWidgetItem(self.logs[i][2]))
            self.table.setItem(i,3, QTableWidgetItem(self.logs[i][3]))
            self.table.setItem(i,4, QTableWidgetItem(self.logs[i][4]))
            self.table.setItem(i,5, QTableWidgetItem(self.logs[i][5]))
            self.table.setCellWidget(i,6,combobox)
            self.table.setItem(i,7,checkbox)

        self.num_clicks = [1,1,1,1,1,1,1,1]
        self.table.horizontalHeader().sectionClicked.connect(self.header_clicked)
        self.table.setGeometry(50,100,900, 650)
        menuBar = QMenuBar(self)
        self.filter_options = menuBar.addMenu('Filter Options')
        self.fa = QAction('Filter')
        self.fa.setShortcut('Ctrl+F')
        self.filter_options.addAction(self.fa)
        self.filter_options.triggered[QAction].connect(self.filter_action)
        self.grid.addWidget(menuBar)
        self.grid.addWidget(self.label)
        self.grid.addWidget(self.table)


    def filter_action(self):
        self.filter.show()
        self.filter.closeEvent = self.apply_filter

    def apply_filter(self, event):
        criteria = self.filter.filter_criteria
        filtered_logs = []


    def header_clicked(self):

        col = self.table.currentColumn()
        # self.num_clicks[col] += 1
        # if self.num_clicks[col] % 2 != 0:
        #     self.table.sortByColumn(col,Qt.AscendingOrder)
        # else:
        #     self.table.sortByColumn(col,Qt.DescendingOrder)
        # items = [self.table.itemAt(i, col).text() for i in range(self.table.rowCount())]
        if col == 0:
            items = [int(item.text()) for item in self.table.selectedItems()]
        elif col == 7:
            self.num_clicks[col] += 1
            if self.num_clicks[col] % 2 == 0:
                self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/intermediate.png'))
                for row in range(self.table.rowCount()):
                    self.table.item(row,7).setCheckState(True)

            else:
                self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/unchecked.png'))
                for row in range(self.table.rowCount()):
                    self.table.item(row,7).setCheckState(False)
        else:
            items = [item.text() for item in self.table.selectedItems()]
        valid_col = col < 6
        if valid_col:
            self.num_clicks[col] += 1
            if self.num_clicks[col] % 2 != 0:
                self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/up_arrow.png'))
                items.sort(reverse=False)

            else:
                self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/down_arrow.png'))
                items.sort(reverse=True)

            for row in range(self.table.rowCount()):
                item = QTableWidgetItem()
                item.setData(Qt.DisplayRole, items[row])
                self.table.setItem(row, col, item)

if __name__ == '__main__':
     App = QApplication(sys.argv)
     window = LogEntryConfiguration()
     window.show()
     sys.exit(App.exec())