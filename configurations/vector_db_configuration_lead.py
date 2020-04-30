from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pymongo import MongoClient

# A cluster is the machine that holds our database


class VectorDBConfigurationLead(QWidget):
    """

    """
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 900, 700)
        self.setWindowTitle("Vector Database Configuration Lead")
        self.UI()
        self.load_commits()

    def UI(self):
        """

        :return:
        """
        textLead = QLabel('Approval Sync: Pending', self)
        textLead.setFont(QFont('MS Shell Dlg 2', 14))
        textLead.move(30,30)

        approvalText = QLabel('Approval Vector DB Table', self)
        approvalText.setFont(QFont('MS Shell Dlg 2', 12))
        approvalText.move(30,70)

        vbox = QVBoxLayout()
        self.approvalTable = QTableWidget(self)
        self.approvalTable.setColumnCount(8)
        self.approvalTable.setHorizontalHeaderItem(7, QTableWidgetItem(""))
        self.approvalTable.setHorizontalHeaderItem(0,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Source IP"))
        self.approvalTable.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Request Timestamp"))
        self.approvalTable.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Vector"))
        self.approvalTable.setHorizontalHeaderItem(3,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Description"))
        self.approvalTable.setHorizontalHeaderItem(5,QTableWidgetItem("Graph"))
        self.approvalTable.setHorizontalHeaderItem(4,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Change Summary"))
        self.approvalTable.setHorizontalHeaderItem(6,QTableWidgetItem(QIcon('icons/up_arrow.png'), "Sync Status"))

        self.cluster = \
            MongoClient(
                "mongodb+srv://Feathersoft:stevenroach@cluster0-700yf.mongodb.net/test?retryWrites=true&w=majority")

        # Defining our DB
        self.db = self.cluster["test"]
        self.collection = self.db["test"]
        header = self.approvalTable.horizontalHeader()
        header.setStretchLastSection(True)

        for i in range(self.approvalTable.columnCount()):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.approvalTable.setGeometry(50,100,900, 400)

        buttonCommit = QPushButton(self,clicked=self.commit_to_database)
        buttonCommit.setGeometry(830,60,70,30)
        buttonCommit.setText('Commit')
        vbox.addWidget(textLead)
        vbox.addWidget(self.approvalTable)
        vbox.addWidget(buttonCommit)
        self.setLayout(vbox)

    def load_commits(self):
        """

        :return:
        """
        self.results = list(self.collection.find())
        self.approvalTable.setRowCount(len(self.results))

        for i in range(self.approvalTable.rowCount()):
            self.approvalTable.setItem(i, 0, QTableWidgetItem(self.results[i]['_ip_address']))
            self.approvalTable.setItem(i, 1, QTableWidgetItem(self.results[i]["_time_stamp"]))
            self.approvalTable.setItem(i, 2, QTableWidgetItem(self.results[i]['_name']))
            self.approvalTable.setItem(i, 3, QTableWidgetItem(self.results[i]['_desc']))
            self.approvalTable.setItem(i, 4, QTableWidgetItem(self.results[i]['_commit']))
            self.approvalTable.setItem(i, 5, QTableWidgetItem(self.results[i]['_graph']))
            self.approvalTable.setItem(i, 6, QTableWidgetItem(self.results[i]['_status']))

    def commit_to_database(self):
        """

        :return:
        """
        self.db = self.cluster["vector_db_test"]
        self.collection = self.db["vdb_test"]

        model = self.approvalTable.selectionModel()
        selected_rows = model.selectedRows()
        try:
            for row in selected_rows:
                result = self.results[row.row()]
                entry = {"_ip_address": result['_ip_address'], "_time_stamp": result['_time_stamp'], "_name":
                result['_name'], "_desc": result['_desc'],"_commit": result['_commit'],
                         "_graph": result['_graph'], "_status": result['_status']}
                self.collection.insert_one(entry)

        except KeyError:
            pass

        except ConnectionError:
            pass





