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
from configurations.rwo.event_configuration import EventConfiguration


class EventConfigurationWindow(QWidget):

    """ The Event Configuration class is a UI Window that accepts all necessary input to
        to create an event and ingest and provide log files and entries to the rest of the configurations.
    """

    """
        Initially the UI is blocked until an event is successfully configured. Each of these signals will be emitted
        to the Main UI.
    """

    # This signal tells the UI when to unlock the toolbar.
    configured = pyqtSignal(bool)
    # This signal tells the UI to populate the log entries table after ingestion.
    ingestion_complete = pyqtSignal(bool)
    # This signal tells the UI to populate the log file table after ingestion.
    logs_ingested = pyqtSignal(bool)
    # This signal tells the UI to populate the enforcement action reports for the log file table after ingestion.
    reports_generated = pyqtSignal(bool)

    def __init__(self, parent=QMainWindow):

        """
        :param parent: The parent of this window.
        """
        super().__init__()
        self.setGeometry(50, 50, 474, 664)
        self.setWindowTitle("Event Configuration")
        self.time_stamp_validated = False
        self.ip_validated = False
        self.root_structure_validated = False
        self.logs = []
        self.files = set()
        self.splunk_port = ''
        self.splunk_index = ''
        self.splunk_username = ''
        self.splunk_password = ''
        self.UI()

    def UI(self):
        # # Creating the label for the window
        self.label = QLabel('Event Configuration')
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        # # Setting the window's font

        # Setting the layout for the window.
        self.layout = QVBoxLayout()
        self.event_layout = QWidget()
        self.event_layout.setLayout(QFormLayout())
        self.team_layout = QWidget()
        self.team_layout.setLayout(QFormLayout())

        # Adding the main label
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
        self.lead_ip_address_line_edit.setObjectName('Lead')
        self.server_port_line_edit = QLineEdit()
        self.splunk_index_line_edit = QLineEdit()
        self.splunk_username_line_edit = QLineEdit()
        self.splunk_password_line_edit = QLineEdit()
        self.splunk_password_line_edit.setEchoMode(QLineEdit.Password)

        self.team_layout.layout().addRow('Lead IP Address', self.lead_ip_address_line_edit)
        self.team_layout.layout().addRow('Server Port', self.server_port_line_edit)
        self.team_layout.layout().addRow('Splunk Index', self.splunk_index_line_edit)
        self.team_layout.layout().addRow('Splunk Username', self.splunk_username_line_edit)
        self.team_layout.layout().addRow('Splunk Password', self.splunk_password_line_edit)

        self.established_connections = QLabel('')
        self.team_layout.layout().addRow('Established Connections', self.established_connections)
        self.lead_checkbox = QCheckBox()
        self.lead_checkbox.setObjectName('Check')
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
                    result = [0 <= int(x) < 256 for x in
                              re.split('\.', re.match(r'^\d+\.\d+\.\d+\.\d+$',
                                                      self.lead_ip_address_line_edit.text()).group(0))].count(True) == 4
                except AttributeError:
                    result = False

                non_lead_analyst = (self.lead_checkbox.isChecked() and socket.gethostbyname(socket.gethostname())
                                    != self.lead_ip_address_line_edit.text())

                empty_ip = self.lead_ip_address_line_edit.text() == ''

                if non_lead_analyst:
                    QMessageBox.critical(self, 'Connection Error',
                                         f'Non-Lead attempting to connect as lead\n'
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

                        try:
                            lead = self.lead_ip_address_line_edit.text().strip()
                            port = int(self.server_port_line_edit.text().strip())
                            index = self.splunk_index_line_edit.text().strip()
                            username = self.splunk_username_line_edit.text().strip()
                            password = self.splunk_password_line_edit.text().strip()
                            self.splunk_client = SplunkIntegrator(lead,port,index,username,password)

                            QMessageBox.information(self,
                                                    'Connection Successful',
                                                    f'Connection to server from IP {self.lead_ip_address_line_edit.text()}'
                                                    f' established !')

                            if not self.ip_validated:
                                label = QLabel('Lead IP Validated ✔.')
                                label.setStyleSheet("QLabel { color: green}")
                                self.team_layout.layout().addRow('', label)
                            self.lead_ip_address_line_edit.setEnabled(False)
                            self.ip_validated = True
                            self.established_connections.setText(str(1))
                        except ConnectionError:
                            QMessageBox.critical(self, 'Connection Error',
                                                 'A connection could not be established at this time.\n'
                                                 + 'Please confirm that the server is active and running\n'+
                                                 'and that login info is correct.')
                        except ValueError:
                            QMessageBox.critical(self, 'Port Number Error',
                                                 'Port Number must be numerical')

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
        folder_structure = self.root_directory_edit.text()
        if folder_structure != '':
            folders = os.listdir(folder_structure)
            valid_folder_count = len(folders) >= 3
            has_red, has_blue, has_white = 'red' in folders, 'blue' in folders, 'white' in folders

            if not valid_folder_count:
                QMessageBox.critical(self,"Root Directory Structure Error",
                                     f"Root Directory currently has {len(folders)} folders\n"
                                     f"Please choose a directory with at least 3 folders")

            if not has_red:
                QMessageBox.critical(self, "Root Directory Structure Error",
                                     f" A folder labeled red was not found in the root directory\n"
                                     f"Please make sure your folders are properly labeled.")



            if not has_blue:
                QMessageBox.critical(self, "Root Directory Structure Error",
                                     f" A folder labeled blue was not found in the root directory\n"
                                     f"Please make sure your folders are properly labeled.")


            if not has_white:
                QMessageBox.critical(self, "Root Directory Structure Error",
                                     f" A folder labeled white was not found in the root directory\n"
                                     f"Please make sure your folders are properly labeled.")


            else:

                self.red_directory_edit.setText(self.root_directory_edit.text() + '/red')
                self.blue_directory_edit.setText(self.root_directory_edit.text() + '/blue')
                self.white_directory_edit.setText(self.root_directory_edit.text() + '/white')
                buttonReply = QMessageBox.question(self,'PyQt5 message',
                                                   "Begin Ingestion?",
                                                   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                                   QMessageBox.Cancel)

                if not self.root_structure_validated:
                    label = QLabel('Root Structure Validated ✔.')
                    label.setStyleSheet("QLabel { color: green}")
                    self.directory_configuration_layout.layout().addRow('', label)

                self.root_structure_validated = True
                if buttonReply == QMessageBox.Yes:
                    if self.ip_validated and self.root_structure_validated:
                        toolbar_unlocked = True
                        self.configured.emit(toolbar_unlocked)
                        self.begin_ingestion(count=500)
                    else:
                        QMessageBox.critical(self,"Event and Team not Validated",
                                         "Please make sure event configuration and team configurations are "
                                         "validated before ingestion")

    def begin_ingestion(self,count):
        audio = ['mp3', 'wav']
        video = ['mp4']
        image = ['jpg', 'pdf', 'pnthg']
        cleansing_status, validation_status, ingestion_status, acknowledgement_status = False,False,False,False
        for filepath, folder, dir in os.walk('root'):
            for file in dir:
                path = os.path.join(filepath ,file)
                ext = path.split('.')[1]
                if ext in audio:
                    converted = self.splunk_client.file_converter.convert_audio_to_text(path)
                elif ext in video:
                    converted = self.splunk_client.file_converter.convert_video_to_audio(path)
                elif ext in image:
                    converted = self.splunk_client.file_converter.convert_image_to_text(path)
                else:
                    converted = path
                if converted:
                    self.files.add(converted)

        for file in self.files:
            cleansing_status = self.splunk_client.cleanse_file(file)
            validation_status = self.splunk_client.validate_file(file, self.start_date.text(), self.end_date.text())
            acknowledgement_status = cleansing_status and validation_status
            if acknowledgement_status:
                self.splunk_client.upload_file(file, self.splunk_index_line_edit.text().strip())
                ingestion_status = acknowledgement_status and cleansing_status and validation_status
            else:
                ingestion_status = False
            self.logs.append(LogFile(file, cleansing_status, validation_status, ingestion_status, acknowledgement_status))
        self.splunk_client.download_log_files(count=count,index=self.splunk_index_line_edit.text().strip())
        self.ingestion_complete.emit(True)
        self.logs_ingested.emit(True)
        self.reports_generated.emit(True)


