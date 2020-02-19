import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime
from configurations.filter_configuration import FilterConfiguratation


"""This class will be used to build the UI Window for the Log Entry Configuration"""


class LogEntryConfigurationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1000, 800)
        self.setWindowTitle("Log Entry Configuration")
        self.UI()

    def UI(self):
        # Creating the label for the window
        self.label = QLabel('Log Entry Configuration', self)
        # Setting the window's font
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.move(50,50)

        # Creating the layout that the window will be stored
        self.vbox = QVBoxLayout()
        # Creating the table
        self.table = QTableWidget(self)
        # Setting the amount of columns our table will have
        self.table.setColumnCount(5)
        # Setting the amount of row our table will have
        self.table.setRowCount(20)
        # Setting the headers for each column
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('up_arrow.png'), "List Number"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('up_arrow.png'), "Log Entry Timestamp"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('up_arrow.png'), "Log Entry Event"))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem("Vector"))
        self.table.setHorizontalHeaderItem(4,QTableWidgetItem(""))

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

        # Reading the dummy log
        log = [line.split(' ') for line in open('dummy_log.txt').readlines()]

        for i in range(len(log)):

            # To store non string values in our table cells, we need to create widgets
            # that have a display role formatted for non string values.
            list_value = QTableWidgetItem()
            list_value.setData(Qt.DisplayRole, i)
            time_stamp = QTableWidgetItem()
            time_stamp.setData(Qt.DisplayRole,str(datetime.datetime.utcnow()))
            self.table.setItem(i,0,list_value)
            self.table.setItem(i,1,time_stamp)
            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)
            combobox = QComboBox()
            combobox.addItems(['','1','2','3'])
            tableitem = QTableWidget()
            tableitem.setRowCount(4)
            tableitem.setVerticalHeaderItem(0,QTableWidgetItem('Content'))
            tableitem.setVerticalHeaderItem(1, QTableWidgetItem('Host'))
            tableitem.setVerticalHeaderItem(2, QTableWidgetItem('Source'))
            tableitem.setVerticalHeaderItem(3, QTableWidgetItem('Source Type'))
            self.table.setCellWidget(i,2,tableitem)
            self.table.setCellWidget(i,3,combobox)
            self.table.setItem(i,4,checkbox)

        self.num_clicks = [1,1,1]
        self.table.horizontalHeader().sectionClicked.connect(self.header_clicked)
        self.table.setGeometry(50,100,900, 650)
        self.menuBar = QMenuBar()
        self.menuBar.setMaximumWidth(120)
        self.filter_options = self.menuBar.addMenu('Filter Options')
        self.filter_options.addAction('Filter')
        self.filter_options.triggered[QAction].connect(self.filter_action)
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.menuBar)
        self.vbox.addWidget(self.table)

        self.setLayout(self.vbox)
        #self.show()
        #App = QApplication(sys.argv)
        #sys.exit(App.exec())

    def filter_action(self):
        self.filter = FilterConfiguratation()
        self.filter.show()

    def header_clicked(self):
        col = self.table.currentColumn()

        # items = [self.table.itemAt(i, col).text() for i in range(self.table.rowCount())]
        if col == 0:
            items = [int(item.text()) for item in self.table.selectedItems()]
        else:
            items = [item.text() for item in self.table.selectedItems()]
        valid_col = col <= 2
        if valid_col:
            self.num_clicks[col] += 1
            if self.num_clicks[col] % 2 != 0:
                self.table.horizontalHeaderItem(col).setIcon(QIcon('up_arrow.png'))
                items.sort(reverse=False)
                if col < 2:
                    for row in range(self.table.rowCount()):
                        item = QTableWidgetItem()
                        item.setData(Qt.DisplayRole,items[row])
                        self.table.setItem(row,col,item)

            else:
                if valid_col:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('down_arrow.png'))
                    items.sort(reverse=True)
                    if col < 2:
                        for row in range(self.table.rowCount()):
                            item = QTableWidgetItem()
                            item.setData(Qt.DisplayRole, items[row])
                            self.table.setItem(row, col, item)

        else:
            pass

if __name__ == '__main__':
     App = QApplication(sys.argv)
     window = LogEntryConfigurationWindow()
     window.show()
     sys.exit(App.exec())