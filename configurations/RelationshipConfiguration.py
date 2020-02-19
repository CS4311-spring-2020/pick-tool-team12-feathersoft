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
        self.header_labels = ['','Relationship ID', 'Parent', 'Child', 'Label']
        self.treeWidget.setHeaderLabels(self.header_labels)
        item_0 = QTreeWidgetItem(self.treeWidget)
        font = QFont()
        font.setPointSize(17)
        item_0.setFont(2, font)
        item_0 = QTreeWidgetItem(self.treeWidget)
        self.checkBox = QCheckBox(self)
        self.checkBox.setGeometry(QRect(60, 100, 20, 20))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QCheckBox(self)
        self.checkBox_2.setGeometry(QRect(60, 120, 20, 20))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        #self.show()


