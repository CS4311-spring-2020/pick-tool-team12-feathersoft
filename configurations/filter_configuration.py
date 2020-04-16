import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import datetime

from PyQt5.QtWidgets import QDateTimeEdit

""" The filter configuration widget is used to collect filter criteria
    from an analyst to apply to a table.
"""


class FilterConfigurationWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 474, 664)
        self.setWindowTitle("Filter Configuration")
        # The filter criteria will read all the filter input from a user to be applied to the entry table.
        self.filter_criteria = dict()
        self.filter_criteria['Keywords'] = set()
        self.filter_criteria['Creator'] = set()
        self.filter_criteria['Event Type'] = set()
        self.filter_criteria['Timestamp'] = [None] * 2
        self.ui()

    # The ui method is used to generate the window
    def ui(self):
        # Creating layout to store widgets
        self.gridLayout = QGridLayout(self)

        # Creating and positioning start timestamp
        self.start_timestamp_edit = QDateTimeEdit(self)
        self.start_timestamp_edit.setCalendarPopup(True)
        self.gridLayout.addWidget(self.start_timestamp_edit, 10, 1, 1, 1)

        "Creating a group for the creator buttons so that we don't need an " \
        "event handler for each button" \

        self.creator_button_group = QButtonGroup()

        self.creator_red_button = QRadioButton('red', self)
        self.gridLayout.addWidget(self.creator_red_button, 3, 1, 1, 1)

        self.creator_blue_button = QRadioButton('blue', self)
        self.gridLayout.addWidget(self.creator_blue_button, 4, 1, 1, 1)

        self.creator_white_button = QRadioButton('white', self)
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
        self.end_timestamp_label.setFont(font)
        self.gridLayout.addWidget(self.end_timestamp_label, 12, 0, 1, 1)

        self.apply_button = QPushButton('Apply Filter', self)
        self.gridLayout.addWidget(self.apply_button, 13, 0, 1, 1)

        self.apply_button.clicked.connect(self.apply_button_clicked)

        self.lineEdit = QLineEdit(self)
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.filterConfigurationLabel = QLabel('Filter Configuration',self)
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setWeight(75);
        self.filterConfigurationLabel.setFont(font1)
        self.gridLayout.addWidget(self.filterConfigurationLabel, 0, 0, 1, 1)

        self.event_type_button_group = QButtonGroup()

        self.event_red_button = QRadioButton('red', self)
        self.event_red_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.event_red_button, 6, 1, 1, 1)

        self.event_blue_button = QRadioButton('blue', self)
        self.event_blue_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.event_blue_button, 7, 1, 1, 1)

        self.event_white_button = QRadioButton('white', self)
        self.event_white_button.setAutoExclusive(False)
        self.gridLayout.addWidget(self.event_white_button, 8, 1, 1, 1)

        self.event_type_button_group.addButton(self.event_red_button)
        self.event_type_button_group.addButton(self.event_blue_button)
        self.event_type_button_group.addButton(self.event_white_button)
        self.event_type_button_group.setExclusive(False)

        self.event_type_button_group.buttonClicked.connect(self.event_type_button_group_clicked)

        self.end_timestamp_edit = QDateTimeEdit(self)
        self.end_timestamp_edit.setCalendarPopup(True)
        self.gridLayout.addWidget(self.end_timestamp_edit, 12, 1, 1, 1)

        self.event_type_label = QLabel('Source Type', self)
        self.event_type_label.setFont(font)
        self.gridLayout.addWidget(self.event_type_label, 6, 0, 1, 1)

        self.creator_label = QLabel('Source:', self)
        self.creator_label.setFont(font)
        self.gridLayout.addWidget(self.creator_label, 3, 0, 1, 1)

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

    # #Handling apply button event
    def apply_button_clicked(self):
        self.filter_criteria["Timestamp"][0] = self.start_timestamp_edit.text()
        self.filter_criteria["Timestamp"][1] = self.end_timestamp_edit.text()
        self.close()