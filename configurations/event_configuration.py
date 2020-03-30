import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime
import re
import os
import socket
from configurations.splunk_client import SplunkIntegrator
from configurations.rwo.significant_log_entry import SignificantLogEntry
from configurations.rwo.log_file import LogFile


class EventConfiguratation(QWidget):

    configured = pyqtSignal(bool)
    ingestion_complete = pyqtSignal(list)
    logs_ingested = pyqtSignal(list)

    def __init__(self, lead_ip,parent=QMainWindow):
        super().__init__()
        self.setGeometry(50, 50, 474, 664)
        self.setWindowTitle("Event Configuration")
        self.lead_ip = lead_ip
        self.time_stamp_validated = False
        self.ip_validated = False
        self.root_structure_validated = False
        self.splunk_client = SplunkIntegrator('192.168.1.138',8089,'feathersoft','Feathersoft','stevenroach')
        self.logs = []
        self.files = []


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
        self.directory_configuration_layout = QWidget()
        self.directory_configuration_layout.setLayout(QFormLayout())

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

        self.save_event_button.clicked.connect(self.validate_timestamp)


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


        # dc layout

        self.directory_configuration_layout.layout().addRow(QLabel('Directory Configuration', alignment=Qt.AlignLeft,
                                                                   font=QFont('MS Shell Dlg 2', 12)))
        self.root_directory_layout = QWidget()
        self.root_directory_layout.setLayout(QHBoxLayout())
        self.root_directory_edit = QLineEdit()
        self.root_directory_button = QPushButton(self, clicked=self.open_file, icon=QIcon('icons/folder.png'))
        self.root_directory_layout.layout().addWidget(self.root_directory_edit)
        self.root_directory_layout.layout().addWidget(self.root_directory_button)


        self.red_directory_layout = QWidget()
        self.red_directory_layout.setLayout(QHBoxLayout())
        self.red_directory_edit = QLineEdit()
        self.red_directory_button = QPushButton(self, clicked=self.open_file, icon=QIcon('icons/folder.png'))
        self.red_directory_layout.layout().addWidget(self.red_directory_edit)
        self.red_directory_layout.layout().addWidget(self.red_directory_button)

        self.blue_directory_layout = QWidget()
        self.blue_directory_layout.setLayout(QHBoxLayout())
        self.blue_directory_edit = QLineEdit()
        self.blue_directory_button = QPushButton(self, clicked=self.open_file, icon=QIcon('icons/folder.png'))
        self.blue_directory_layout.layout().addWidget(self.blue_directory_edit)
        self.blue_directory_layout.layout().addWidget(self.blue_directory_button)

        self.white_directory_layout = QWidget()
        self.white_directory_layout.setLayout(QHBoxLayout())
        self.white_directory_edit = QLineEdit()
        self.white_directory_button = QPushButton(self, clicked=self.open_file, icon=QIcon('icons/folder.png'))
        self.white_directory_layout.layout().addWidget(self.white_directory_edit)
        self.white_directory_layout.layout().addWidget(self.white_directory_button)

        self.directory_configuration_layout.layout().addRow('Root Directory', self.root_directory_layout)
        self.directory_configuration_layout.layout().addRow('Red Team Folder', self.red_directory_layout)
        self.directory_configuration_layout.layout().addRow('Blue Team Folder', self.blue_directory_layout)
        self.directory_configuration_layout.layout().addRow('White Team Folder', self.white_directory_layout)
        self.directory_configuration_layout.layout().addRow('', QPushButton('Ingest', clicked=self.validate_root_structure))


        self.layout.addWidget(self.event_layout)
        self.layout.addWidget(self.team_layout)
        self.layout.addWidget(self.directory_configuration_layout)
        self.setLayout(self.layout)

    def validate_timestamp(self):
        valid_name = self.name.text() != ''
        valid_description = self.description.text() != ''
        valid_time_stamp_range = self.start_date.dateTime() < self.end_date.dateTime()
        if valid_name and valid_description and valid_time_stamp_range:
            buttonReply = QMessageBox.question(self, 'PyQt5 message',
                                               "Are you sure this is the correct timestamp range",
                                               QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                               QMessageBox.Cancel)
            if buttonReply == QMessageBox.Yes:
                label = QLabel('Event Timestamp Validated ✔.')
                label.setStyleSheet("QLabel { color: green}")
                if not self.time_stamp_validated:
                    self.event_layout.layout().addRow('',label)
                self.time_stamp_validated = True

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
        if not self.ip_validated:
            if self.lead_ip_address_line_edit.isEnabled():
                result = None
                try:
                    result = [0 <= int(x) < 256 for x in re.split('\.', re.match(r'^\d+\.\d+\.\d+\.\d+$', self.lead_ip_address_line_edit.text()).group(0))].count(True) == 4
                except AttributeError:
                    result = False

                non_lead_analyst = (self.lead_checkbox.isChecked() and self.lead_ip_address_line_edit.text() != self.lead_ip
                                    or self.lead_checkbox.isChecked() and socket.gethostbyname(socket.gethostname()) != self.lead_ip) \
                                   or(self.lead_ip_address_line_edit.text() != self.lead_ip and not self.lead_checkbox.isChecked())

                empty_ip = self.lead_ip_address_line_edit.text() == ''

                if non_lead_analyst:
                    QMessageBox.critical(self, 'Connection Error',
                                         f'Non-Lead {socket.gethostbyname(socket.gethostname())} attempting to connect as lead\n'
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
                    if not self.ip_validated:
                        label = QLabel('Lead IP Validated ✔.')
                        label.setStyleSheet("QLabel { color: green}")
                        self.team_layout.layout().addRow('', label)
                    self.lead_ip_address_line_edit.setEnabled(False)

                    self.ip_validated = True

    def open_file(self):
        file = str(QFileDialog.getExistingDirectory(QFileDialog(), "Select Directory",
                                                    directory=os.path.realpath(os.getcwd())))
        if self.sender() == self.root_directory_button:
            self.root_directory_edit.setText(file)

        elif self.sender() == self.red_directory_button:
            self.red_directory_edit.setText(file)

        elif self.sender() == self.blue_directory_button:
            self.blue_directory_edit.setText(file)

        else:
            self.white_directory_edit.setText(file)

    def validate_root_structure(self):
        if self.root_directory_edit.text() != '':
            num_folders = len(os.listdir(self.root_directory_edit.text()))
            if num_folders < 3:
                QMessageBox.critical(self,"Root Directory Structure Error",
                                     f"Root Directory currently has {num_folders} folders")
            else:
                buttonReply = QMessageBox.question(self, 'PyQt5 message',
                                                   "Begin Ingestion?",
                                                   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                                   QMessageBox.Cancel)

                if not self.root_structure_validated:
                    label = QLabel('Root Structure Validated ✔.')
                    label.setStyleSheet("QLabel { color: green}")
                    self.directory_configuration_layout.layout().addRow('', label)

                self.root_structure_validated = True

                if buttonReply == QMessageBox.Yes:

                    toolbar_unlocked = self.time_stamp_validated and self.ip_validated and self.root_structure_validated
                    self.configured.emit(toolbar_unlocked)
                    self.begin_ingestion(count=1000)

    def begin_ingestion(self,count):
        # for filepath, folder, dir in os.walk(self.root_directory_edit.text()):
        #     for file in dir:
        #
        #         path = os.path.join(filepath,file)
        #         self.files.append(path)

        self.files.append(os.path.abspath('android.txt'))
        for file in self.files:
            log_file = LogFile()
            log_file.cleansing_status = self.splunk_client.cleanse_file(file)
            validated = self.splunk_client.validate_file(file, self.start_date.text(), self.end_date.text())
            if validated is dict():log_file.validation_status = False
            else:log_file.validation_status = validated

            acknowledged = log_file.validation_status and log_file.cleansing_status
            if acknowledged:
                log_file.acknowledgement_status = True
                if self.splunk_client.upload_file(file,'main'):
                    log_file.ingestion_status = True
                else:
                    log_file.ingestion_status = False

            self.logs.append(log_file)



                #self.splunk_client.upload_file(path=path, index='main')

        self.splunk_client.download_log_files(count=count)
        self.ingestion_complete.emit(self.splunk_client.entries)
        self.logs_ingested.emit(self.logs)








