import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime


class FilterConfiguration(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 474, 664)
        self.setWindowTitle("Filter Configuration")
        # The filter criteria will read all the filter input from a user to be applied to the entry table.
        self.filter_criteria = dict()
        self.filter_criteria['Keywords'] = set()
        self.filter_criteria['Creator'] = set()
        self.filter_criteria['Event Type'] = set()
        self.filter_criteria['Timestamp'] = [0,0]
        self.ui()

    def ui(self):
        # Creating layout to store widgets
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")

        # Creating and positioning start timestamp
        self.start_timestamp_edit = QDateTimeEdit(self)
        self.start_timestamp_edit.setObjectName(u"startTimestampEdit")
        self.gridLayout.addWidget(self.start_timestamp_edit, 10, 1, 1, 1)

        "Creating a group for the creator buttons so that we don't need an " \
        "event handler for each button" \

        self.creator_button_group = QButtonGroup()

        self.creator_red_button = QRadioButton('Red', self)
        self.creator_red_button.setObjectName(u"redButton1")
        self.creator_red_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.creator_red_button, 3, 1, 1, 1)

        self.creator_blue_button = QRadioButton('Blue', self)
        self.creator_blue_button.setObjectName(u"blueButton1")
        self.creator_blue_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.creator_blue_button, 4, 1, 1, 1)

        self.creator_white_button = QRadioButton('White', self)
        self.creator_white_button.setObjectName(u"whiteButton1")
        self.creator_white_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.creator_white_button, 5, 1, 1, 1)

        self.creator_button_group.addButton(self.creator_red_button)
        self.creator_button_group.addButton(self.creator_blue_button)
        self.creator_button_group.addButton(self.creator_white_button)
        self.creator_button_group.setExclusive(False)


        self.creator_button_group.buttonClicked.connect(self.creator_button_group_clicked)

        self.start_timestamp_label = QLabel('Start Timestamp:', self)
        self.start_timestamp_label.setObjectName(u"startTimestampLabel")
        font = QFont()
        font.setPointSize(16)
        self.start_timestamp_label.setFont(font)
        self.gridLayout.addWidget(self.start_timestamp_label, 10, 0, 1, 1)

        self.end_timestamp_label = QLabel('End Timestamp:', self)
        self.end_timestamp_label.setObjectName(u"endTimestampLabel")
        self.end_timestamp_label.setFont(font)
        self.gridLayout.addWidget(self.end_timestamp_label, 12, 0, 1, 1)

        self.apply_button = QPushButton('Apply Filter', self)
        self.apply_button.setObjectName(u"applyButton")
        self.gridLayout.addWidget(self.apply_button, 13, 0, 1, 1)

        self.apply_button.clicked.connect(self.apply_button_clicked)

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

        self.event_type_button_group = QButtonGroup()

        self.event_red_button = QRadioButton('Red', self)
        self.event_red_button.setObjectName(u"redButton2")
        self.event_red_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.event_red_button, 6, 1, 1, 1)

        self.event_blue_button = QRadioButton('Blue', self)
        self.event_blue_button.setObjectName(u"blueButton2")
        self.event_blue_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.event_blue_button, 7, 1, 1, 1)

        self.event_white_button = QRadioButton('White', self)
        self.event_white_button.setObjectName(u"whiteButton2")
        self.event_white_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.event_white_button, 8, 1, 1, 1)

        self.event_type_button_group.addButton(self.event_red_button)
        self.event_type_button_group.addButton(self.event_blue_button)
        self.event_type_button_group.addButton(self.event_white_button)
        self.event_type_button_group.setExclusive(False)

        self.event_type_button_group.buttonClicked.connect(self.event_type_button_group_clicked)

        self.end_timestamp_edit = QDateTimeEdit(self)
        self.end_timestamp_edit.setObjectName(u"endTimestampEdit")
        self.gridLayout.addWidget(self.end_timestamp_edit, 12, 1, 1, 1)

        self.event_type_label = QLabel('Event Type', self)
        self.event_type_label.setObjectName(u"eventTypeLabel")
        self.event_type_label.setFont(font)
        self.gridLayout.addWidget(self.event_type_label, 6, 0, 1, 1)

        self.creator_label = QLabel('Creator:', self)
        self.creator_label.setObjectName(u"creatorLabel")
        self.creator_label.setFont(font)
        self.gridLayout.addWidget(self.creator_label, 3, 0, 1, 1)
        #self.show()

    # Handling click events for the creator buttons
    def creator_button_group_clicked(self):
        for btn in self.creator_button_group.buttons():
            # If button is selected we want to add it's label to the criteria (e.g. Red, White, Blue)
            if btn.isChecked():
                self.filter_criteria['Creator'].add(btn.text())

            # If user deselects a button we want to remove it from the filter list.
            elif not btn.isChecked() and btn.text() in self.filter_criteria['Creator']:
                self.filter_criteria['Creator'].remove(btn.text())

        print(self.filter_criteria['Creator'])

    # Handling events for the event type button group
    def event_type_button_group_clicked(self):
        for btn in self.event_type_button_group.buttons():
            # If button is selected we want to add it's label to the criteria (e.g. Red, White, Blue)
            if btn.isChecked():
                self.filter_criteria['Event Type'].add(btn.text())

            # If user deselects a button we want to remove it from the filter list.
            elif not btn.isChecked() and btn.text() in self.filter_criteria['Event Type']:
                self.filter_criteria['Event Type'].remove(btn.text())

        print(self.filter_criteria['Event Type'])

    # #Handling apply button event
    def apply_button_clicked(self):
        # Finally add the timestamps to the filter criteria and exit
        self.filter_criteria['Timestamp'][0] = self.start_timestamp_edit.dateTime().currentDateTime().toString()
        self.filter_criteria['Timestamp'][1] = self.end_timestamp_edit.dateTime().currentDateTime().toString()
        # Parse any keywords entered into the search criteria
        self.filter_criteria['Keyword'] = [self.lineEdit.text().split()]
        print(self.filter_criteria)
        self.close()



