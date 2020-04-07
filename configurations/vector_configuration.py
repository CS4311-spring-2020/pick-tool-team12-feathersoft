import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import os


class VectorConfiguration(QWidget):


    vector_added = pyqtSignal()
    vector_deleted = pyqtSignal()
    vector_selected = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 482, 432)
        self.setWindowTitle("Vector Configuration")
        self.selected_vectors = set()
        self.UI()



    def UI(self):
        self.main_layout = QGridLayout(self)
        self.button_layout = QWidget()
        self.button_layout.setLayout(QHBoxLayout())

        self.main_layout.addWidget(QLabel('Vector Configuration', alignment=Qt.AlignLeft,
                                                font=QFont('MS Shell Dlg 2', 12)))



        self.editButton = QPushButton('Edit Vector', clicked=self.edit_vector)
        self.addVectorButton = QPushButton('Add Vector',clicked=self.add_vector)
        self.deleteButton = QPushButton('Delete Vector',clicked=self.delete_vector)

        self.button_layout.layout().addWidget(self.editButton)
        self.button_layout.layout().addWidget(self.addVectorButton)
        self.button_layout.layout().addWidget(self.deleteButton)


        self.table = QTableWidget(0, 3, self)
        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.button_layout)
        # self.table.verticalHeader().setVisible(False)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Vector Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Vector Description"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem(QIcon('icons/unchecked'), ""))

        self.slot_clicks = [1] * self.table.columnCount()

        for i in range(self.table.rowCount()):
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            checkbox.clicked.connect(self.update_vector_db)
            self.table.setCellWidget(i,0,QTextEdit())
            self.table.setCellWidget(i,1,QTextEdit())
            self.table.setCellWidget(i, 2, checkbox)


        self.table.horizontalHeader().sectionClicked.connect(self.header_clicked)
        self.table.horizontalHeader().setProperty("showSortIndicator", False)
        self.header = self.table.horizontalHeader()
        #self.header.setStretchLastSection(True)


        for i in range(self.table.columnCount()):
           self.header.setSectionResizeMode(i, QHeaderView.Stretch)


        self.setLayout(self.main_layout)

    def update_vector_db(self):
        self.vector_selected.emit()

    def header_clicked(self):
        if self.table.rowCount() > 0:
            col = self.table.currentColumn()
            self.slot_clicks[col] += 1
            if col == 2:
                if self.slot_clicks[col] % 2 == 0:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/checked.png'))
                    for row in range(self.table.rowCount()):
                        self.table.cellWidget(row, col).setCheckState(Qt.Checked)
                        if self.table.item(row, 0) and self.table.item(row, 1):
                            self.vector_selected.emit()
                else:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/unchecked.png'))
                    for row in range(self.table.rowCount()):
                        self.table.cellWidget(row, col).setCheckState(Qt.Unchecked)

            else:
                items = [item.text() for item in self.table.selectedItems()]
            valid_col = col < 2
            if valid_col:
                if self.slot_clicks[col] % 2 != 0:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/up_arrow.png'))
                    self.table.sortByColumn(col,Qt.AscendingOrder)

                else:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/down_arrow.png'))
                    self.table.sortByColumn(col, Qt.DescendingOrder)

    def delete_vector(self):
        selected = self.table.selectedItems()
        for select in selected:
            row = self.table.indexFromItem(select).row()
            for j in range(self.table.columnCount()):
                self.table.takeItem(row,j)
            self.table.removeRow(row)

        self.vector_deleted.emit()

    def add_vector(self):
        row_index = self.table.rowCount() + 1
        self.table.setRowCount(row_index)

        for i in range(row_index):
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            checkbox.clicked.connect(self.update_vector_db)
            self.table.setCellWidget(self.table.rowCount()-1, 2, checkbox)
        self.vector_added.emit()

    def edit_vector(self):
        if self.table.selectedItems():
            self.editor = VectorEdit(self.table.currentRow(),self.table)
            self.editor.show()


class VectorEdit(QWidget):
    def __init__(self,row,table):
        super().__init__()
        self.row = row
        self.vc_table = table
        #self.selected = selected
        self.setGeometry(100,100,400,100)
        self.setFixedWidth(400)
        self.setFixedHeight(100)
        self.initUI()

    def initUI(self):

        self.layout = QFormLayout()
        self.name = QLineEdit()
        self.desc = QLineEdit()
        self.layout.addRow('Vector Name', self.name)
        self.layout.addRow('Vector Description', self.desc)
        self.layout.addRow('', QPushButton('Submit', clicked=self.submitted))
        self.setLayout(self.layout)


    def submitted(self):
        if self.vc_table.selectedItems():
            for item in self.vc_table.selectedItems():
                self.vc_table.takeItem(item.row(),0)
                self.vc_table.takeItem(item.row(),1)
                self.vc_table.setItem(item.row(),0,QTableWidgetItem(self.name.text() if self.name.text() !='' else " "))
                self.vc_table.setItem(item.row(),1,QTableWidgetItem(self.desc.text() if self.name.text() !='' else " "))
        self.close()








