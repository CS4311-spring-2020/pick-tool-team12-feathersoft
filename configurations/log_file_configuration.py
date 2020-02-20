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

        #Populating Values in Table from dummy file
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        dummy_file = os.path.join(THIS_FOLDER, 'dummyFileConfig.txt')

        dummyFileConfig = [line.split(',') for line in open(dummy_file,'r').readlines()]
        self.tableWidget.setRowCount(len(dummyFileConfig))

        i = 0
        emptyHeader = QTableWidgetItem()
        for line in dummyFileConfig:
                logName,source,cleansedStatus,validatedStatus,ingestedStatus = line[0],line[1],line[2],line[3],line[4]
                self.tableWidget.setVerticalHeaderItem(i,emptyHeader)
                logNameItem = QTableWidgetItem(logName)
                sourceItem = QTableWidgetItem(source)
                cleansedItem = QTableWidgetItem(cleansedStatus)
                validatedItem = QTableWidgetItem(validatedStatus)
                ingestedItem = QTableWidgetItem(ingestedStatus)
                self.tableWidget.setItem(i,0,logNameItem)
                self.tableWidget.setItem(i, 1, sourceItem)
                self.tableWidget.setItem(i,2,cleansedItem)
                self.tableWidget.setItem(i, 3, validatedItem)
                self.tableWidget.setItem(i, 4, ingestedItem)

                i= i+1




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


        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        dummy_file = os.path.join(THIS_FOLDER, 'dummyEnforcementReport.txt')

        dummyEnforcementReport = [line.split(':') for line in open(dummy_file,'r').readlines()]
        self.reportTable.setRowCount(len(dummyEnforcementReport))

        i = 0
        emptyHeader = QTableWidgetItem()
        for line in dummyEnforcementReport:
                lineNum,errorMessage = line[0],line[1]
                self.reportTable.setVerticalHeaderItem(i,emptyHeader)
                lineNumItem = QTableWidgetItem(lineNum)
                errorMessageItem = QTableWidgetItem(errorMessage)
                self.reportTable.setItem(i,0,lineNumItem)
                self.reportTable.setItem(i,1,errorMessageItem)
                i= i+1

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



