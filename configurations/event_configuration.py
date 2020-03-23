import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime
import re


class EventConfiguratation(QWidget):
    def __init__(self, lead_ip):
        super().__init__()
        self.setGeometry(50, 50, 474, 664)
        self.setWindowTitle("Event Configuration")
        self.lead_ip = lead_ip
        self.UI()

    def UI(self):
        # # Creating the label for the window
        self.label = QLabel('Event Configuration')
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        # # Setting the window's font

        self.layout = QVBoxLayout()
        self.event_layout = QWidget()
        self.event_layout.setLayout(QFormLayout())
        self.team_layout = QWidget()
        self.team_layout.setLayout(QFormLayout())
        self.event_layout.layout().addRow(QLabel('Event Configuration', alignment=Qt.AlignLeft,
                                                 font=QFont('MS Shell Dlg 2', 12)))
        self.name = QLineEdit()
        self.description = QLineEdit()
        self.start_date = QDateTimeEdit()
        self.start_date.setCalendarPopup(True)
        self.end_date = QDateTimeEdit()
        self.end_date.setCalendarPopup(True)

        self.event_layout.layout().addRow('Event Name', self.name)
        self.event_layout.layout().addRow('Event Description', self.description)
        self.event_layout.layout().addRow('Event Start Date', self.start_date)
        self.event_layout.layout().addRow('Event End Date', self.end_date)
        self.save_event_button = QPushButton('Save Button')
        self.event_layout.layout().addRow('', self.save_event_button)

        self.save_event_button.clicked.connect(self.configure_event)


        self.team_label = QLabel("Team Configuration")
        self.team_label.setFont(QFont('MS Shell Dlg 2', 12))
        self.team_layout.layout().addRow(QLabel('Team Configuration', alignment=Qt.AlignLeft,
                                                font=QFont('MS Shell Dlg 2', 12)))

        self.lead_ip_address_line_edit = QLineEdit()
        self.team_layout.layout().addRow('Lead IP Address', self.lead_ip_address_line_edit)
        self.established_connections = QLabel('')
        self.team_layout.layout().addRow('Established Connections', self.established_connections)
        self.lead_checkbox = QCheckBox()
        self.team_layout.layout().addRow('Lead', self.lead_checkbox)
        self.connect_button = QPushButton('Connect',clicked=self.validate_credentials)
        self.team_layout.layout().addRow('',self.connect_button)

        self.event_layout.layout().setSpacing(30)
        self.team_layout.layout().setSpacing(30)

        self.layout.addWidget(self.event_layout)
        self.layout.addWidget(self.team_layout)
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

    def configure_event(self):
        valid_name = self.name.text() != ''
        valid_description = self.description.text() != ''
        valid_time_stamp_range = self.start_date.dateTime() < self.end_date.dateTime()
        if valid_name and valid_description and valid_time_stamp_range:
            buttonReply = QMessageBox.question(self, 'PyQt5 message',
                                               "Are you sure this is the correct timestamp range",
                                               QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                               QMessageBox.Cancel)
            if buttonReply == QMessageBox.Yes:
                self.name.setDisabled(True)
                self.description.setDisabled(True)
                self.start_date.setDisabled(True)
                self.end_date.setDisabled(True)
                self.save_event_button.setDisabled(True)
                label = QLabel('Event Configured. You may no longer edit.')
                label.setStyleSheet("QLabel { color: red}")
                self.event_layout.layout().addRow('',label)

            elif buttonReply == QMessageBox.No:
                QMessageBox.information(self, 'No','Please be sure the information entered is correct')

        else:
            if not valid_name:
                QMessageBox.critical(self, 'Name Validation Error', 'Empty Event Name\n'
                                 + 'Please enter a non-empty event name')
            if not valid_description:
                QMessageBox.critical(self, 'Description Validation Error', 'Invalid Description\n'
                                     + 'Please enter a non-empty event description')
            if not valid_time_stamp_range:
                QMessageBox.critical(self, 'Timestamp Validation Error', 'Invalid Timestamp Range\n'
                                     + 'Timestamps must meet either of the following criteria\n' +
                                     '1 - Start date and start time must be less than end date and end time\n' +
                                     '2 - Start date is equal to end date but start time is less than end time')

    def validate_credentials(self):
        result = None
        try:
            result = [0 <= int(x) < 256 for x in re.split('\.', re.match(r'^\d+\.\d+\.\d+\.\d+$', self.lead_ip_address_line_edit.text()).group(0))].count(True) == 4
        except AttributeError:
            result = False

        lead = '127.0.0.1'
        non_lead_analyst = (self.lead_checkbox.isChecked() and self.lead_ip_address_line_edit.text() != lead) \
                           or (not self.lead_checkbox.isChecked() and self.lead_ip_address_line_edit.text() == lead)
        empty_ip = self.lead_ip_address_line_edit.text() == ''

        if non_lead_analyst:
            QMessageBox.critical(self, 'Connection Error',
                                 'Non-Lead attempting to connect as lead\n'
                                 + 'Check lead box if lead IP entered\n'
                                 + 'Uncheck lead box if non-lead IP entered')

        elif empty_ip:
            QMessageBox.critical(self, 'Connection Error',
                                 'IP Address field left empty\n'
                                 + 'Enter a value from 0.0.0.0 to 255.255.255.255')

        elif not result or result is None:
            QMessageBox.critical(self, 'Connection Error',
                                 'IP Address Invalid\n'
                                 + 'Enter a value from 0.0.0.0 to 255.255.255.255')

        else:
            QMessageBox.information(self,'Connection Successful',
                                    f'Connection to server from IP {self.lead_ip_address_line_edit.text()} established !')





