import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from configurations.change_configuration import ChangeConfigurationWindow

class VectorDBConfigurationLead(QWidget):
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

        textLead = QLabel('Approval Sync: Pending', self)
        textLead.setFont(QFont('MS Shell Dlg 2', 14))
        textLead.move(30,30)

        approvalText = QLabel('Approval Vector DB Table', self)
        approvalText.setFont(QFont('MS Shell Dlg 2', 12))
        approvalText.move(30,70)

        vbox = QVBoxLayout()
        approvalTable = QTableWidget(self)
        approvalTable.setColumnCount(8)
        approvalTable.setRowCount(20)
        approvalTable.verticalHeader().setVisible(False)
        approvalTable.setHorizontalHeaderItem(7, QTableWidgetItem(""))
        approvalTable.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Source IP"))
        approvalTable.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Request Timestamp"))
        approvalTable.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Vector"))
        approvalTable.setHorizontalHeaderItem(3,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Description"))
        approvalTable.setHorizontalHeaderItem(5,QTableWidgetItem("Graph"))
        approvalTable.setHorizontalHeaderItem(4,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Change Summary"))
        approvalTable.setHorizontalHeaderItem(6,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Sync Status"))


        header = approvalTable.horizontalHeader()
        header.setStretchLastSection(True)
        approvalTable.verticalHeader().setStretchLastSection(True)


        for i in range(approvalTable.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        for i in range(approvalTable.rowCount()):

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

            tableitem_IP = QTableWidgetItem()
            tableitem_IP.setData(Qt.DisplayRole, '127.0.0.1')

            tableitemTimestamp = QTableWidget()
            tableitemTimestamp.setRowCount(4)
            tableitemTimestamp.setVerticalHeaderItem(0, QTableWidgetItem('12: 00 '))
            tableitemTimestamp.setVerticalHeaderItem(1, QTableWidgetItem('12: 10'))
            tableitemTimestamp.setVerticalHeaderItem(2, QTableWidgetItem('12: 20'))
            tableitemTimestamp.setVerticalHeaderItem(3, QTableWidgetItem('12: 30'))

            tableitemDescription = QTableWidgetItem()
            tableitemDescription.setText( 'This text can be changed as presented')

            tableitemSummary = QTableWidgetItem()
            tableitemSummary.setData(Qt.DisplayRole, 'Last Summary')


            approvalTable.setItem(i,0,tableitem_IP)
            approvalTable.setCellWidget(i, 1, tableitemTimestamp)
            approvalTable.setCellWidget(i, 2, tableitemVector)
            approvalTable.setItem(i, 3, tableitemDescription)
            approvalTable.setItem(i, 4, tableitemSummary)
            approvalTable.setCellWidget(i,5,comboboxGraph)
            approvalTable.setCellWidget(i,6,comboboxStatus)
            approvalTable.setItem(i,7,checkbox)


        approvalTable.setGeometry(50,100,900, 400)

        buttonCommit = QPushButton(self)
        buttonCommit.setGeometry(830,60,70,30)
        buttonCommit.setText('Commit')
        vbox.addWidget(textLead)
        vbox.addWidget(approvalTable)
        vbox.addWidget(buttonCommit)


        self.setLayout(vbox)


        #self.show()


# if __name__ == '__main__':
#     App = QApplication(sys.argv)
#     window = VectorDBConfigurationLead()
#     sys.exit(App.exec())