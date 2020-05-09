from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import re
import os
import socket

from configurations.rwo import EventConfiguration, LogFile
from configurations.splunk_client import SplunkIntegrator
from splunklib.binding import AuthenticationError



class EventConfigurationWindow(QWidget):
    """ The Event Configuration class is a UI Window that accepts all necessary input to
        to create an event and ingest and provide log files and entries to the rest of the configurations.
    """

    """
        Initially the UI is blocked until an event is successfully configured. Each of these signals will be emitted
        to the Main UI.
    """

    # This signal tells the UI when to unlock the toolbar.
    configured = pyqtSignal()
    # This signal tells the UI to populate the log entries table after ingestion.
    ingestion_complete = pyqtSignal()
    # This signal tells the UI to populate the log file table after ingestion.
    logs_ingested = pyqtSignal()
    # This signal tells the UI to populate the enforcement action reports for the log file table after ingestion.
    reports_generated = pyqtSignal()

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
        self.logs = set()
        self.files = set()
        self.splunk_client = SplunkIntegrator()
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

        # Creating our layouts for the Event, Team, and Directory configurations
        self.event_layout.layout().addRow(QLabel('Event Configuration', alignment=Qt.AlignLeft,
                                                 font=QFont('MS Shell Dlg 2', 12)))

        self.directory_configuration_layout = QWidget()
        self.directory_configuration_layout.setLayout(QFormLayout())

        # Input parameters for the Event Configuration
        self.name = QLineEdit()
        self.description = QLineEdit()
        self.start_date = QDateTimeEdit()
        self.start_date.setCalendarPopup(True)
        self.end_date = QDateTimeEdit()
        self.end_date.setCalendarPopup(True)

        # Adding our widgets to the layout for Event Configuration
        self.event_layout.layout().addRow('Event Name', self.name)
        self.event_layout.layout().addRow('Event Description', self.description)
        self.event_layout.layout().addRow('Event Start Date', self.start_date)
        self.event_layout.layout().addRow('Event End Date', self.end_date)
        self.save_event_button = QPushButton('Save Button')
        self.event_layout.layout().addRow('', self.save_event_button)

        self.save_event_button.clicked.connect(self.validate_timestamp)

        # Adding our widgets to the Team configuration layout

        self.team_layout.layout().addRow(QLabel('Team Configuration', alignment=Qt.AlignLeft,
                                                font=QFont('MS Shell Dlg 2', 12)))

        self.established_connections = QLabel('')
        self.team_layout.layout().addRow('Established Connections', self.established_connections)
        self.lead_checkbox = QCheckBox()
        self.lead_checkbox.setObjectName('Check')
        self.team_layout.layout().addRow('Lead', self.lead_checkbox)
        self.connect_button = QPushButton('Connect', clicked=self.validate_credentials)
        self.team_layout.layout().addRow('', self.connect_button)

        # Adding our widgets to the directory configuration layout
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
        self.directory_configuration_layout.layout().addRow('',
                                                            QPushButton('Ingest', clicked=self.validate_root_structure))

        # Adding our layouts to the main layout
        self.layout.addWidget(self.event_layout)
        self.layout.addWidget(self.team_layout)
        self.layout.addWidget(self.directory_configuration_layout)
        self.setLayout(self.layout)

    def validate_timestamp(self):
        """
        This method will be used to validate the timestamp ranges entered in the event configuration.
        The start timestamp should be less than the end timestamp.
        :return:
        """

        # Checks if there is a value in the "Event Name" field
        valid_name = self.name.text() != ''
        # Checks if there is a value in the  "Event Description" field
        valid_description = self.description.text() != ''
        # Checks if the start date is less than the end date
        valid_time_stamp_range = self.start_date.dateTime() < self.end_date.dateTime()

        # If all three fields are valid
        if valid_name and valid_description and valid_time_stamp_range:
            # Validate if the user has entered the correct timestamp range
            buttonReply = QMessageBox.question(self, 'PyQt5 message',
                                               "Are you sure this is the correct timestamp range",
                                               QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                               QMessageBox.Cancel)
            # Display success message if the user confirms the entered data
            if buttonReply == QMessageBox.Yes:
                label = QLabel('Event Timestamp Validated ✔.')
                label.setStyleSheet("QLabel { color: green}")
                if not self.time_stamp_validated:
                    self.event_layout.layout().addRow('', label)
                self.time_stamp_validated = True

            # Prompt the user to resubmit if the data entered is not correct
            elif buttonReply == QMessageBox.No:
                QMessageBox.information(self, 'No', 'Please be sure the information entered is correct')

        else:

            # Display error messages for empty name, description, or invalid timestamp ranges
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
        """ We can only connect to the server once so we don't want to run this again if the connection has
            already been established
            :return
        """

        if not self.ip_validated:
            # If we haven't already connected
            if self.splunk_client.credentials[0]:
                result = None
                try:
                    # Check if the entered IP address matches valid IPV4 structure
                    result = ([0 <= int(x) < 256 for x in
                              re.split('\.', re.match(r'^\d+\.\d+\.\d+\.\d+$',
                                                      self.splunk_client.credentials[0]).group(0))].count(True) == 4)\
                             or self.splunk_client.credentials[0] == "localhost"
                except AttributeError:
                    result = False

                # Check if the IP of the user connecting to the server matches the IP of the lead analyst
                self.non_lead_analyst = (self.lead_checkbox.isChecked() and socket.gethostbyname(socket.gethostname())
                                         != self.splunk_client.credentials[0])

                # Check if the IP address field has a value
                empty_ip = self.splunk_client.credentials[0] == ''

                # Display an error message if a non-lead is attempting to connect as the lead.
                if self.non_lead_analyst:
                    QMessageBox.critical(self, 'Connection Error',
                                         f'Non-Lead attempting to connect as lead\n'
                                         + 'Check lead box if lead IP entered\n'
                                         + 'Uncheck lead box if non-lead IP entered')

                # Display an error message if an IP address has not been entered.
                elif empty_ip:
                    QMessageBox.critical(self, 'Connection Error',
                                         'IP Address field left empty\n'
                                         + 'Enter a value from 0.0.0.0 to 255.255.255.255')

                # Display an error message if the IP address entered doesnt match IPV4 format
                elif not result or result is None:
                    QMessageBox.critical(self, 'Connection Error',
                                         'IP Address Invalid\n'
                                         + 'Enter a value from 0.0.0.0 to 255.255.255.255')

                else:

                    # If everything entered in the fields is valid.

                    try:
                        # Get the value entered into the "Lead IP Address field"
                        lead = self.splunk_client.credentials[0]

                        # Create a splunk instance and connect to the server.
                        self.splunk_client = SplunkIntegrator()
                        self.splunk_client.connect()

                        # Alert the user that a successful connection has been established.
                        QMessageBox.information(self,
                                                'Connection Successful',
                                                f'Connection to server from IP {socket.gethostname()}'
                                                f' established !')

                        # If we haven't already established a connection..
                        if not self.ip_validated:
                            # Display success message.
                            label = QLabel('Lead IP Validated ✔.')
                            label.setStyleSheet("QLabel { color: green}")
                            self.team_layout.layout().addRow('', label)
                        # Disable the option to re-connect
                        # self.lead_ip_address_line_edit.setEnabled(False)
                        self.lead_checkbox.setEnabled(False)
                        # Flag the ip-validation
                        self.ip_validated = True
                        # Update the number of established connections
                        self.established_connections.setText(str(1))

                    # Catch an error if a connection could not be established
                    except ConnectionError:
                        QMessageBox.critical(self, 'Connection Error',
                                             'A connection could not be established at this time.\n'
                                             + 'Please confirm that the server is active and running\n' +
                                             'and that login info is correct.')

                    # Catch an error if a non-numerical value was not entered for port
                    except ValueError:
                        QMessageBox.critical(self, 'Port Number Error',
                                             'Port Number must be numerical')

                    # Catch an error if the analyst enters the wrong connection information
                    except AuthenticationError:
                        QMessageBox.critical(self, 'Login Failed', 'Login failed.\n'
                                                                   'Please confirm that the information entered is '
                                                                   'correct.')
                        # Catch an error is the network is not reachable at this time.
                    except OSError:
                        QMessageBox.critical(self, 'Network Unreachable', 'Network Unreachable '
                                                                          'Please confirm that the information '
                                                                          'entered is correct.')

    def open_file(self):
        """
            This method opens a file dialog and allows a user to select the directory containing the files
            they want to ingest.
            :return:
        """
        # Open the file selection dialog
        file = str(QFileDialog.getExistingDirectory(QFileDialog(), "Select Directory",
                                                    directory=os.path.realpath(os.getcwd())))

        # If the button clicked was the root directory button set it's text with the chosen directory
        if self.sender() == self.root_directory_button:
            self.root_directory_edit.setText(file)

        # If the button clicked was the red directory button set it's text with the chosen directory
        elif self.sender() == self.red_directory_button:
            self.red_directory_edit.setText(file)

        # If the button clicked was the blue directory button set it's text with the chosen directory
        elif self.sender() == self.blue_directory_button:
            self.blue_directory_edit.setText(file)

        # If the button clicked was the white directory button set it's text with the chosen directory
        else:
            self.white_directory_edit.setText(file)

    def validate_root_structure(self):
        """
            This method will validate whether the chosen root directory contains at least three folders which contains
            the names 'red', 'blue', and 'white' respectively.
            :return
        """

        # Get the text from the root directory line edit
        root_dir = self.root_directory_edit.text()

        # If the root directory line edit is not empty
        if root_dir != '':
            # Check to see if there are folder in the root directory
            folders = os.listdir(root_dir)
            # Check if there are at least three folders
            valid_folder_count = len(folders) >= 3
            # Check if there is at least one folder labeled 'red', 'blue', and 'white'
            has_red, has_blue, has_white = 'red' in folders, 'blue' in folders, 'white' in folders

            # Display an alert if there are not enough folders display an error message
            if not valid_folder_count:
                QMessageBox.critical(self, "Root Directory Structure Error",
                                     f"Root Directory currently has {len(folders)} folders\n"
                                     f"Please choose a directory with at least 3 folders")

            # Display an alert if a red folder isn't found
            if not has_red:
                QMessageBox.critical(self, "Root Directory Structure Error",
                                     f" A folder labeled red was not found in the root directory\n"
                                     f"Please make sure your folders are properly labeled.")

            # Display an alert if a blue folder ins't found
            if not has_blue:
                QMessageBox.critical(self, "Root Directory Structure Error",
                                     f" A folder labeled blue was not found in the root directory\n"
                                     f"Please make sure your folders are properly labeled.")

            # Display an alert if a white folder isn't found
            if not has_white:
                QMessageBox.critical(self, "Root Directory Structure Error",
                                     f" A folder labeled white was not found in the root directory\n"
                                     f"Please make sure your folders are properly labeled.")

            else:
                """
                    If there exists at least three folders and the required folders are in the root directory
                    display the path of the chosen directory in each line edit.
                """
                self.red_directory_edit.setText(self.root_directory_edit.text() + '/red')
                self.blue_directory_edit.setText(self.root_directory_edit.text() + '/blue')
                self.white_directory_edit.setText(self.root_directory_edit.text() + '/white')



                # Prompt the user to begin ingestion
                buttonReply = QMessageBox.question(self, 'PyQt5 message',
                                                   "Begin Ingestion?",
                                                   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                                   QMessageBox.Cancel)

                # If we have not already validated the root directory structure
                if not self.root_structure_validated:
                    # Display an message saying we have
                    label = QLabel('Root Structure Validated ✔.')
                    label.setStyleSheet("QLabel { color: green}")
                    self.directory_configuration_layout.layout().addRow('', label)

                # Flag that the root directory structure is valid
                self.root_structure_validated = True

                # If the user chooses to ingest
                if buttonReply == QMessageBox.Yes:
                    # If event, team, and directory configurations are valid
                    if self.ip_validated and self.root_structure_validated:
                        # Unlock the main toolbar after the files have been ingested
                        toolbar_unlocked = True
                        self.event_configuration = EventConfiguration(event_name=self.name.text().strip(),
                                                                      event_description=self.description.text().strip(),
                                                                      event_start_timestamp=self.start_date.text().strip(),
                                                                      event_end_timestamp=self.end_date.text().strip(),
                                                                      root_directory=self.root_directory_edit.text().strip(),
                                                                      red_team_folder=self.red_directory_edit.text().strip(),
                                                                      blue_team_folder=self.blue_directory_edit.text().strip(),
                                                                      white_team_folder=self.white_directory_edit.text().strip(),
                                                                      lead=self.non_lead_analyst,
                                                                      ip_address=self.splunk_client.credentials[0],
                                                                      connection_established=True
                                                                      )
                        self.begin_ingestion(count=500)

                    else:
                        QMessageBox.critical(self, "Event and Team not Validated",
                                             "Please make sure event configuration and team configurations are "
                                             "validated before ingestion")

    def generate_files(self, dir):
        for filepath, folder, dir in os.walk(dir):
            for file in dir:
                path = os.path.join(filepath, file)
                self.files.add(path)

    def count_files(self,dir):
        i = 0
        for filepath, folder, dir in os.walk('root'):
            for file in dir:
                path = os.path.join(filepath, file)

                i += 1

        return i

    def begin_ingestion(self, count):
        """
        This method ingests log files into the system, populating our log file and log entry tables
        :param count: The number of entries to be displayed in the table
        :return:
        """
        self.label_animation = QLabel(self)
        self.label_animation.setWindowFlags(Qt.FramelessWindowHint)
        self.label_animation.setMask(QPixmap('Loading_2.gif').mask())
        self.movie = QMovie('Loading_2.gif')
        self.label_animation.setMovie(self.movie)

        try:
            timer = QTimer(self)
            self.movie.start()
            self.label.show()
            audio = ['mp3', 'wav']
            video = ['mp4']
            image = ['jpg', 'pdf', 'png']
            converted = ''
            for filepath, folder, dir in os.walk(self.root_directory_edit.text().strip()):
                cleansing_status, validation_status, ingestion_status, acknowledgement_status = False, False, False, \
                                                                                                False
                for file in dir:
                    path = os.path.join(filepath, file)
                    print(path)
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
            self.event_configuration.logs = self.files
            for file in self.files:
                cleansing_status = self.splunk_client.cleanse_file(file)
                validation_status = self.splunk_client.validate_file(converted, self.start_date.text(),
                                                                     self.end_date.text())
                acknowledgement_status = cleansing_status and validation_status
                if acknowledgement_status:
                    self.splunk_client.upload_file(file, self.splunk_client.credentials[2])
                    ingestion_status = acknowledgement_status and cleansing_status and validation_status
                else:
                    ingestion_status = False
                self.logs.add(
                    LogFile(file, cleansing_status, validation_status, ingestion_status, acknowledgement_status))

            self.movie.stop()
            self.label.close()


        except AuthenticationError:
            QMessageBox.critical(self, "Authentication Error", "Request Aborted: not logged in")

        try:
            self.splunk_client.download_log_files(count=count)

        except IndexError:
            QMessageBox.critical(f"Index out of bounds",f"Please sure your index has at least {count} entries")



        self.configured.emit()
        self.ingestion_complete.emit()
        self.logs_ingested.emit()
        self.reports_generated.emit()




