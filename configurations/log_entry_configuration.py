import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class LogEntryConfigurationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1000, 800)
        self.setWindowTitle("Log File Configuration")
        self.setMaximumSize(1000,800)
        self.UI()

    def UI(self):

        self.label = QLabel('Log File Configuration', self)
        self.label.setFont(QFont('MS Shell Dlg 2', 20))
        self.label.move(50,50)
        self.vbox = QVBoxLayout()
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setRowCount(20)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('up_arrow.png'), "List Number"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('up_arrow.png'), "Log Entry Timestamp"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('up_arrow.png'), "Log Entry Event"))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem("Vector"))
        self.table.setHorizontalHeaderItem(4,QTableWidgetItem(""))
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)


        for i in range(self.table.rowCount()):
            self.table.setVerticalHeaderItem(i,QTableWidgetItem(''))
        log = [line.split(' ') for line in open('dummy_log.txt').readlines()]
        for i in range(len(log)):
            self.table.setItem(i,0,QTableWidgetItem(str(i + 1)))
            self.table.setItem(i,1,QTableWidgetItem(str(log[i][0])))
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

        self.table.clicked.connect(self.header_clicked)
        self.table.setGeometry(50,100,900, 650)
        self.vbox.addWidget(self.table)
        #self.setLayout(vbox)
        self.show()

    def header_clicked(self):
        col = self.table.currentColumn()
        print(col)





if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = LogEntryConfigurationWindow()
    sys.exit(App.exec())