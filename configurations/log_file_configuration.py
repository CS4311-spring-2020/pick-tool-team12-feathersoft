import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import os

"""
    The log file configuration will be used to display the various log files ingested into the system as well as their
    enforcement action reports.
"""


class LogFileConfigurationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 482, 432)
        self.setWindowTitle("Log File Configuration")
        self.er_reports = list()
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel('Log File Configuration', self)
        self.label.setObjectName(u"label")
        self.label.setFont(QFont('MS Shell Dlg 2', 12))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.table = QTableWidget(self)

        self.table.setColumnCount(6)
        #Setting Headers for Log File Table
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('icons/up_arrow.png'),'File Name'))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Source'))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Cleansing Status'))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Validation Status'))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Ingestion Status'))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem(QIcon(''), 'Enforcement Action Report'))

        emptyHeader = QTableWidgetItem()
        self.table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.table.setGridStyle(Qt.SolidLine)
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setProperty("showSortIndicator", False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.header = self.table.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(True)
        self.table.verticalHeader().setProperty("showSortIndicator", True)
        self.table.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 1)

        self.table.horizontalHeader().sectionClicked.connect(self.header_clicked)
        self.slot_clicks = [1] * self.table.columnCount()

    def display(self):
        sender = self.sender()
        index = self.table.indexAt(sender.pos()).row()
        self.e = EnforcementActionReport()
        self.e.populate_table(self.er_reports[index])
        self.e.show()

    def populate_table(self,log_files):
        self.table.setRowCount(len(log_files))
        for i in range(len(log_files)):
                logNameItem = QTableWidgetItem(log_files[i].get_name.split('/')[-1])
                sourceItem = QTableWidgetItem(str(log_files[i].get_name))
                cleansedItem = QTableWidgetItem(str(log_files[i].get_cleansing_status))
                validatedItem = QTableWidgetItem(str(log_files[i].get_validation_status))
                ingestedItem = QTableWidgetItem(str(log_files[i].get_ingestion_status))
                self.table.setItem(i, 0, logNameItem)
                self.table.setItem(i, 1, sourceItem)
                self.table.setItem(i, 2, cleansedItem)
                self.table.setItem(i, 3, validatedItem)
                self.table.setItem(i, 4, ingestedItem)
                self.table.setCellWidget(i, 5, QPushButton('View'))
                self.table.cellWidget(i,5).clicked.connect(self.display)

    def header_clicked(self):
        if not self.table.rowCount() == 0:
            col = self.table.currentColumn()
            items = [item.text() for item in self.table.selectedItems()]
            valid_col = col < 5
            if valid_col:
                self.slot_clicks[col] += 1
                if self.slot_clicks[col] % 2 != 0:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/up_arrow.png'))
                    self.table.sortByColumn(col,Qt.AscendingOrder)
                else:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/down_arrow.png'))
                    self.table.sortByColumn(col, Qt.DescendingOrder)


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


        # Creating table for enforcement action report window
        self.reportTable = QTableWidget(0,2,self)

        # Creating headers for columns in table

        lineNumHeader = QTableWidgetItem('Line Number')
        self.reportTable.setHorizontalHeaderItem(0, lineNumHeader)
        errorMsgHeader = QTableWidgetItem('Error Message')
        self.reportTable.setHorizontalHeaderItem(1, errorMsgHeader)

        emptyHeader = QTableWidgetItem()
        self.reportTable.horizontalHeader().setStretchLastSection(True)
        self.reportTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

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
        self.setLayout(self.gridLayout)

    def populate_table(self,er_report):
        rows = [(key, er_report[key]) for key in er_report.keys() if er_report[key] != []]
        self.reportTable.setRowCount(len(rows))
        i = 0
        for i in range(len(rows)):
            key,report = rows[i]
            indexes = ''.join(str(i) + ' ' for i in report)
            self.reportTable.setItem(i,0,QTableWidgetItem(indexes))
            self.reportTable.setItem(i,1,QTableWidgetItem(key))
            i += 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogFileConfigurationWindow()
    sys.exit(app.exec())



