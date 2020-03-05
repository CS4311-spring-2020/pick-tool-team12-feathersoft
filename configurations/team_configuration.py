import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime


class TeamConfiguratation(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 560, 664)
        self.setWindowTitle("Team Configuration")
        self.UI()

    def UI(self):
        self.label = QLabel('Team Configuration', self)
        self.label.move(160, 70)
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.setObjectName("label")
        self.checkBox = QCheckBox('Lead',self)
        self.checkBox.setGeometry(QRect(10, 280, 381, 41))

        self.label_2 = QLabel('Lead IP Address',self)

        self.label_2.setGeometry(QRect(6, 120, 101, 41))

        self.label_3 = QLabel('connections to',self)
        self.label_3.setGeometry(QRect(10, 220, 101, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QPushButton('Connect',self)
        self.pushButton.setGeometry(QRect(130, 350, 261, 81))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(130, 120, 261, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QTextEdit(self)
        self.textEdit_2.setGeometry(QRect(130, 200, 261, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QLabel('no. established',self)
        self.label_4.setGeometry(QRect(10, 200, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel('lead ip',self)
        self.label_5.setGeometry(QRect(10, 240, 101, 16))
        self.label_5.setObjectName("label_5")

        #self.show()

