import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from pymongo import MongoClient

from configurations.custom_widgets import CheckableComboBox


class VectorDBConfigurationNonLead(QWidget):

    _push_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Vector Database Configuration")
        self.UI()
        self.vectors = []
        self.cluster = \
            MongoClient(
                "mongodb+srv://Feathersoft:stevenroach@cluster0-700yf.mongodb.net/test?retryWrites=true&w=majority")

        # Defining our DB
        self.db = self.cluster["vector_db_test"]
        self.collection = self.db["vdb_test"]

    def UI(self):
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
        
        self.table = QTableWidget(0,4,self)
        self.table.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Vector"))
        self.table.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Description"))
        self.table.setHorizontalHeaderItem(2,QTableWidgetItem(""))
        self.table.setHorizontalHeaderItem(3,QTableWidgetItem("Graph"))

        self.table2 = QTableWidget(0,4,self)
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



        buttonPush = QPushButton(self,clicked=self.pushed)
        buttonPush.setGeometry(350,65,70,30)
        buttonPush.setText('Push')



        buttonPull = QPushButton(self,clicked=self.pull)
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

    def pushed(self):
        self._push_signal.emit()

    def pull(self):
        self.results = self.collection.find()
        j = 0

        self.results = list(self.results)
        self.table2.setRowCount(len(self.results))

        for i in range(self.table2.rowCount()):
            self.table2.setItem(i, 0, QTableWidgetItem(self.results[i]['_name']))
            self.table2.setItem(i, 1, QTableWidgetItem(self.results[i]['_desc']))
            self.table2.setItem(i, 3, QTableWidgetItem(self.results[i]['_graph']))




