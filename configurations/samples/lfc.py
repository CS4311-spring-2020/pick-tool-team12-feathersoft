import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import os


class LogFileConfiguration(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 482, 432)
        self.setWindowTitle("Log File Configuration")
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel('Log File Configuration', self)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(self)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)

        #Setting Headers for Log File Table
        fileNameHeader = QTableWidgetItem('File Name')
        self.tableWidget.setHorizontalHeaderItem(0, fileNameHeader)
        sourceHeader = QTableWidgetItem('Source')
        self.tableWidget.setHorizontalHeaderItem(1, sourceHeader)
        cleansingHeader = QTableWidgetItem('Cleansing Status')
        self.tableWidget.setHorizontalHeaderItem(2, cleansingHeader)
        validationHeader = QTableWidgetItem('Validation Status')
        self.tableWidget.setHorizontalHeaderItem(3, validationHeader)
        ingestionHeader = QTableWidgetItem('Ingestion Status')
        self.tableWidget.setHorizontalHeaderItem(4, ingestionHeader)
        actionReportHeader = QTableWidgetItem('View Enforcement Action Report')
        self.tableWidget.setHorizontalHeaderItem(5, actionReportHeader)

        #Populating Values in Table
        #These are empty headers for the left side column. Maybe we can remove this entirely? No. we cant.
        if (self.tableWidget.rowCount() < 5):
            self.tableWidget.setRowCount(5)
        emptyHeader = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, emptyHeader)
        self.tableWidget.setVerticalHeaderItem(1, emptyHeader)
        self.tableWidget.setVerticalHeaderItem(2, emptyHeader)
        self.tableWidget.setVerticalHeaderItem(3, emptyHeader)
        self.tableWidget.setVerticalHeaderItem(4, emptyHeader)

        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(3, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(4, 4, __qtablewidgetitem36)


        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(680, 55))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        for i in range(self.tableWidget.rowCount()):
            button = QPushButton('View', self)
            button.clicked.connect(self.display)
            self.tableWidget.setCellWidget(i,5,button)

        #self.show()

    def display(self):
        self.w = EnforcementActionReport()
        self.w.show()

class EnforcementActionReport(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 482, 432)
        self.setWindowTitle("Enforcement Action Report")
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)


        #Creating table for enforcement action report window
        self.reportTable = QTableWidget(self)
        if (self.reportTable.columnCount() < 2):
            self.reportTable.setColumnCount(2)

        #Creating headers for columns in table
        lineNumHeader = QTableWidgetItem('Line Number')
        self.reportTable.setHorizontalHeaderItem(0, lineNumHeader)
        errorMsgHeader = QTableWidgetItem('Error Message')
        self.reportTable.setHorizontalHeaderItem(1, errorMsgHeader)


        if (self.reportTable.rowCount() < 3):
            self.reportTable.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.reportTable.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.reportTable.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.reportTable.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.reportTable.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.reportTable.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.reportTable.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.reportTable.setItem(1, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.reportTable.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.reportTable.setItem(2, 1, __qtablewidgetitem10)


        self.reportTable.setObjectName(u"reportTable")
        self.reportTable.setSortingEnabled(True)
        self.reportTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.reportTable.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.reportTable, 1, 0, 1, 4)

        self.enforcementLabel = QLabel('Enforcement Action Report',self)
        self.enforcementLabel.setObjectName(u"enforcementLabel")
        self.enforcementLabel.setFont(font)
        self.gridLayout.addWidget(self.enforcementLabel, 0, 1, 1, 1)

        self.ingestButton = QPushButton('Ingest Despite Errors',self)
        self.ingestButton.setObjectName(u"ingestButton")
        self.gridLayout.addWidget(self.ingestButton, 2, 0, 1, 2)

        self.revalidateButton = QPushButton('Revalidate Files',self)
        self.revalidateButton.setObjectName(u"revalidateButton")
        self.gridLayout.addWidget(self.revalidateButton, 2, 2, 1, 2)

        self.cancelButton = QPushButton('Cancel',self)
        self.cancelButton.setObjectName(u"cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 4, 1, 2)



