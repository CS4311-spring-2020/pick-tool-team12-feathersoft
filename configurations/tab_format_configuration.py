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
        #hardcoded
        dummy1 = ["1", "attack1", "2020-02-20 02:00:35.552164", "Lorem ipsum dolor sit amet",
                  "dir/logs/log1.txt", "Jhonny Rogers", "attack", "red-icon.png", "Red Team"];
        dummy2 = ["2", "attack2", "2019-03-06 05:00:45.552169", "consectetur adipiscing elit",
                  "dir/logs/log2.txt", "Jon", "attack", "blue-icon.png", "Red Team"];
        for row in range(2):
            rowItem = QTreeWidgetItem(self.treeWidget)

            for column in range(len(self.headerLabels)):
                if column == 9:
                    cb = QCheckBox()
                    self.treeWidget.setItemWidget(rowItem,9,cb)
                else:
                    if row == 0:
                        rowItem.setText(column, dummy1[column])
                    else:
                        rowItem.setText(column, dummy2[column])

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

