import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime

class TabFormatConfiguration(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 1206, 602)
        self.setWindowTitle("Nodes Configuration In Graphical Format")
        self.UI()

    def UI(self):

        self.treeWidget = QTreeWidget(self)
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QRect(20, 50, 1161, 192))
        self.treeWidget.setAcceptDrops(False)
        self.treeWidget.setObjectName("treeWidget")
        self.headerLabels = ['Node ID', 'Node Name', 'Node Timestamp',
                             'Node Description', 'Log Entry Reference', 'Log Creator', 'Event Type',
                             'Icon Type', 'Source', 'Node Visibility']
        self.treeWidget.setHeaderLabels(self.headerLabels)
        for i in range(len(self.headerLabels)):
            self.treeWidget.resizeColumnToContents(i)

        item = QTreeWidgetItem()
        self.treeWidget.addTopLevelItem(item)
        cb = QCheckBox()
        self.treeWidget.setItemWidget(item,9,cb)
        self.treeWidget.setAlternatingRowColors(True)
        item_0 = QTreeWidgetItem(self.treeWidget)
        item_0 = QTreeWidgetItem(self.treeWidget)
        self.label = QLabel('Nodes Configuration in Tabular Format',self)
        self.label.setGeometry(QRect(20, 30, 231, 16))
        self.label.setObjectName("label")
        self.treeWidget.setHorizontalScrollBar(QScrollBar())
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        #self.show()

