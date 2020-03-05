import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime

class RelationshipConfiguration(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 919, 667)
        self.setWindowTitle("Relationship Configuration")
        self.UI()

    def UI(self):
        self.label = QLabel(self)
        self.label.setGeometry(QRect(40, 30, 211, 16))
        self.label.setObjectName("label")
        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setGeometry(QRect(30, 80, 601, 311))
        self.treeWidget.setObjectName("treeWidget")
        self.header_labels = ['Display','Relationship ID', 'Parent', 'Child', 'Label']
        self.treeWidget.setHeaderLabels(self.header_labels)

        # hardcoded
        dummy1 = ["", "1", "node1", "node3", "attack1"];
        dummy2 = ["", "2", "node2", "node4", "attack2"];
        for row in range(2):
            rowItem = QTreeWidgetItem(self.treeWidget)

            for column in range(len(self.header_labels)):
                if column == 0:
                    cb = QCheckBox()
                    self.treeWidget.setItemWidget(rowItem, 0, cb)
                else:
                    if row == 0:
                        rowItem.setText(column, dummy1[column])
                    else:
                        rowItem.setText(column, dummy2[column])

        for i in range(len(self.header_labels)):
            self.treeWidget.resizeColumnToContents(i)
        self.treeWidget.setAlternatingRowColors(True)
        self.label = QLabel('Relationship Configuration', self)
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.setGeometry(QRect(20, 30, 231, 16))
        self.label.setObjectName("label")
        #self.show()


