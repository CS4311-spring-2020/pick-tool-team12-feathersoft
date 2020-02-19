import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from configurations.change_configuration import ChangeConfigurationWindow

class VectorDBConfigurationLeadWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 900, 700)
        self.setWindowTitle("Vector Database Configuration Lead")
        self.UI()

    def UI(self):
        # self.mainMenu = QMenuBar(self)
        # self.mainMenu.addMenu('File')
        # self.mainMenu.addMenu('Edit')
        # self.mainMenu.addMenu('View')
        # self.mainMenu.addMenu('Search')
        # self.mainMenu.addMenu('Tools')
        # self.mainMenu.addMenu('Help')

        textLead = QLabel('Approval Sync:', self)
        textLead.setFont(QFont('MS Shell Dlg 2', 14))
        textLead.move(30,30)

        approvalText = QLabel('Approval Vector DB Table', self)
        approvalText.setFont(QFont('MS Shell Dlg 2', 12))
        approvalText.move(30,70)

        vbox = QVBoxLayout()
        approvalTable = QTableWidget(self)
        approvalTable.setColumnCount(8)
        approvalTable.setRowCount(15)
        approvalTable.verticalHeader().setVisible(False)
        approvalTable.setHorizontalHeaderItem(7, QTableWidgetItem(""))
        approvalTable.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('up-down-arrow.png'), "Source IP"))
        approvalTable.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('up-down-arrow.png'), "Request Timestamp"))
        approvalTable.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('up-down-arrow.png'), "Vector"))
        approvalTable.setHorizontalHeaderItem(3,QTableWidgetItem(QIcon('up-down-arrow.png'), "Description"))
        approvalTable.setHorizontalHeaderItem(5,QTableWidgetItem("Graph"))
        approvalTable.setHorizontalHeaderItem(4,QTableWidgetItem(QIcon('up-down-arrow.png'), "Change Summary"))
        approvalTable.setHorizontalHeaderItem(6,QTableWidgetItem(QIcon('up-down-arrow.png'), "Sync Status"))


        header = approvalTable.horizontalHeader()
        for i in range(approvalTable.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        for i in range(approvalTable.rowCount()):
            approvalTable.setVerticalHeaderItem(i,QTableWidgetItem(''))
        log = [line.split(' ') for line in open('example.txt').readlines()]
        for i in range(len(log)):
            approvalTable.setItem(i,0,QTableWidgetItem(str(i + 1)))
            approvalTable.setItem(i,1,QTableWidgetItem(str(log[i][0])))

            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)

            comboboxStatus = QComboBox()
            comboboxStatus.addItems(['','Complete','Pending'])

            comboboxGraph = QComboBox()
            comboboxGraph.addItems(['', '1', '2'])

            tableitemVector = QTableWidget()
            tableitemVector.setRowCount(4)
            tableitemVector.setVerticalHeaderItem(0,QTableWidgetItem('Vector 1'))
            tableitemVector.setVerticalHeaderItem(1, QTableWidgetItem('Vector 2'))
            tableitemVector.setVerticalHeaderItem(2, QTableWidgetItem('Vector 3'))
            tableitemVector.setVerticalHeaderItem(3, QTableWidgetItem('Vector 4'))

            tableitem_IP = QTableWidget()
            tableitem_IP.setRowCount(4)
            tableitem_IP.setVerticalHeaderItem(0, QTableWidgetItem('80808451515'))
            tableitem_IP.setVerticalHeaderItem(1, QTableWidgetItem('55066519595'))
            tableitem_IP.setVerticalHeaderItem(2, QTableWidgetItem('18520215885'))
            tableitem_IP.setVerticalHeaderItem(3, QTableWidgetItem('11111111111'))

            tableitemTimestamp = QTableWidget()
            tableitemTimestamp.setRowCount(4)
            tableitemTimestamp.setVerticalHeaderItem(0, QTableWidgetItem('12: 00 '))
            tableitemTimestamp.setVerticalHeaderItem(1, QTableWidgetItem('12: 10'))
            tableitemTimestamp.setVerticalHeaderItem(2, QTableWidgetItem('12: 20'))
            tableitemTimestamp.setVerticalHeaderItem(3, QTableWidgetItem('12: 30'))

            tableitemDescription = QTableWidget()
            tableitemDescription.setRowCount(4)
            tableitemDescription.setVerticalHeaderItem(0, QTableWidgetItem('This is the example of text'))
            tableitemDescription.setVerticalHeaderItem(1, QTableWidgetItem('This text can be changed as presented'))
            tableitemDescription.setVerticalHeaderItem(2, QTableWidgetItem('There are several descriptions of Vectors'))
            tableitemDescription.setVerticalHeaderItem(3, QTableWidgetItem('Last description'))

            tableitemSummary = QTableWidget()
            tableitemSummary.setRowCount(4)
            tableitemSummary.setVerticalHeaderItem(0, QTableWidgetItem('This is the example of text'))
            tableitemSummary.setVerticalHeaderItem(1, QTableWidgetItem('This text can be changed as presented'))
            tableitemSummary.setVerticalHeaderItem(2, QTableWidgetItem('There are several summaries'))
            tableitemSummary.setVerticalHeaderItem(3, QTableWidgetItem('Last Summary'))

            approvalTable.setCellWidget(i,0,tableitem_IP)
            approvalTable.setCellWidget(i, 1, tableitemTimestamp)
            approvalTable.setCellWidget(i, 2, tableitemVector)
            approvalTable.setCellWidget(i, 3, tableitemDescription)
            approvalTable.setCellWidget(i, 4, tableitemSummary)
            approvalTable.setCellWidget(i,5,comboboxGraph)
            approvalTable.setCellWidget(i,6,comboboxStatus)
            approvalTable.setItem(i,7,checkbox)


        approvalTable.setGeometry(50,100,700, 400)

        buttonCommit = QPushButton(self)
        buttonCommit.setGeometry(670,60,70,30)
        buttonCommit.setText('Commit')
        ccw = ChangeConfigurationWindow()
        vbox.addWidget(textLead)
        vbox.addWidget(approvalTable)
        vbox.addWidget(buttonCommit)
        self.ccw = ChangeConfigurationWindow()
        vbox.addWidget(self.ccw)
        self.setLayout(vbox)


        #self.show()


# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#     window = VectorDBConfigurationLeadWindow()
#     sys.exit(App.exec())