import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime


class GraphFormatConfiguration(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 919, 667)
        self.setWindowTitle("Nodes Configuration In Graphical Format")
        self.UI()
    def UI(self):

        self.label = QLabel('Nodes Configuration in graphical format',self)
        self.label.setGeometry(QRect(20, 10, 251, 16))
        self.label.setObjectName("label")
        self.groupBox = QGroupBox('Configuration',self)
        self.groupBox.setGeometry(QRect(30, 50, 321, 151))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QLabel('Interval Units',self.groupBox)
        self.label_3.setGeometry(QRect(30, 100, 131, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QRect(130, 100, 104, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("New Item")
        self.comboBox_2.addItem("New Item")
        self.comboBox_2.addItem("New Item")
        self.comboBox_2.addItem("New Item")
        self.comboBox_2.addItem("New Item")
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setGeometry(QRect(160, 60, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("New Item")
        self.comboBox.addItem("New Item")
        self.comboBox.addItem("New Item")
        self.comboBox.addItem("New Item")
        self.comboBox.addItem("New Item")
        self.label_2 = QLabel('Timeline Orientation',self.groupBox)
        self.label_2.setGeometry(QRect(30, 60, 131, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QGroupBox(self)
        self.groupBox_2.setGeometry(QRect(30, 220, 871, 381))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QGroupBox('Zoom',self.groupBox_2)
        self.groupBox_3.setGeometry(QRect(660, 320, 171, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton = QPushButton('In',self.groupBox_3)
        self.pushButton.setGeometry(QRect(10, 20, 71, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton('Out',self.groupBox_3)
        self.pushButton_2.setGeometry(QRect(100, 20, 71, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.graph = QGraphicsView(self.groupBox_2)
        self.graph.setGeometry(QRect(10, 40, 411, 281))
        self.graph.setObjectName("graph")
        self.graph_2 = QGraphicsView(self.groupBox_2)
        self.graph_2.setGeometry(QRect(440, 40, 411, 281))
        self.graph_2.setObjectName("graph_2")
        self.label_4 = QLabel('Interval',self.groupBox_2)
        self.label_4.setGeometry(QRect(180, 20, 60, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalSlider = QSlider(self.groupBox_2)
        self.horizontalSlider.setGeometry(QRect(80, 350, 381, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_5 = QLabel('Timeline',self.groupBox_2)
        self.label_5.setGeometry(QRect(10, 350, 60, 16))
        self.label_5.setObjectName("label_5")
        self.groupBox.raise_()
        self.label.raise_()
        self.groupBox_2.raise_()




