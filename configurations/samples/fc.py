import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime


class FilterConfiguratation(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 474, 664)
        self.setWindowTitle("Filter Configuration")
        self.UI()

    def UI(self):
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")

        self.startTimestampEdit = QDateTimeEdit(self)
        self.startTimestampEdit.setObjectName(u"startTimestampEdit")
        self.gridLayout.addWidget(self.startTimestampEdit, 10, 1, 1, 1)

        self.blueButton2 = QRadioButton('Blue',self)
        self.blueButton2.setObjectName(u"blueButton2")
        self.blueButton2.setAutoExclusive(False)
        self.gridLayout.addWidget(self.blueButton2, 7, 1, 1, 1)

        self.redButton1 = QRadioButton('Red',self)
        self.redButton1.setObjectName(u"redButton1")
        self.redButton1.setAutoExclusive(False)
        self.gridLayout.addWidget(self.redButton1, 3, 1, 1, 1)

        self.startTimestampLabel = QLabel('Start Timestamp:',self)
        self.startTimestampLabel.setObjectName(u"startTimestampLabel")
        font = QFont()
        font.setPointSize(16)
        self.startTimestampLabel.setFont(font)
        self.gridLayout.addWidget(self.startTimestampLabel, 10, 0, 1, 1)

        self.blueButton1 = QRadioButton('Blue',self)
        self.blueButton1.setObjectName(u"blueButton1")
        self.blueButton1.setAutoExclusive(False)
        self.gridLayout.addWidget(self.blueButton1, 4, 1, 1, 1)

        self.endTimestampLabel = QLabel('End Timestamp:',self)
        self.endTimestampLabel.setObjectName(u"endTimestampLabel")
        self.endTimestampLabel.setFont(font)
        self.gridLayout.addWidget(self.endTimestampLabel, 12, 0, 1, 1)

        self.applyButton = QPushButton('Apply Filter',self)
        self.applyButton.setObjectName(u"applyButton")
        self.gridLayout.addWidget(self.applyButton, 13, 0, 1, 1)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.filterConfigurationLabel = QLabel('Filter Configuration',self)
        self.filterConfigurationLabel.setObjectName(u"filterConfigurationLabel")
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setWeight(75);
        self.filterConfigurationLabel.setFont(font1)
        self.gridLayout.addWidget(self.filterConfigurationLabel, 0, 0, 1, 1)

        self.whiteButton2 = QRadioButton('White',self)
        self.whiteButton2.setObjectName(u"whiteButton2")
        self.whiteButton2.setAutoExclusive(False)
        self.gridLayout.addWidget(self.whiteButton2, 8, 1, 1, 1)

        self.redButton2 = QRadioButton('Red',self)
        self.redButton2.setObjectName(u"redButton2")
        self.redButton2.setAutoExclusive(False)
        self.gridLayout.addWidget(self.redButton2, 6, 1, 1, 1)

        self.whiteButton1 = QRadioButton('White',self)
        self.whiteButton1.setObjectName(u"whiteButton1")
        self.whiteButton1.setAutoExclusive(False)
        self.gridLayout.addWidget(self.whiteButton1, 5, 1, 1, 1)

        self.endTimestampEdit = QDateTimeEdit(self)
        self.endTimestampEdit.setObjectName(u"endTimestampEdit")
        self.gridLayout.addWidget(self.endTimestampEdit, 12, 1, 1, 1)

        self.eventTypeLabel = QLabel('Event Type',self)
        self.eventTypeLabel.setObjectName(u"eventTypeLabel")
        self.eventTypeLabel.setFont(font)
        self.gridLayout.addWidget(self.eventTypeLabel, 6, 0, 1, 1)

        self.creatorLabel = QLabel('Creator:',self)
        self.creatorLabel.setObjectName(u"creatorLabel")
        self.creatorLabel.setFont(font)
        self.gridLayout.addWidget(self.creatorLabel, 3, 0, 1, 1)
        self.show()

if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = FilterConfiguratation()
    sys.exit(App.exec())