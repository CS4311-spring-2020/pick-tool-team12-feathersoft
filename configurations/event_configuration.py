import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import datetime


class EventConfiguratation(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 474, 664)
        self.setWindowTitle("Event Configuration")
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
        self.event_layout.layout().addWidget(self.label)
        self.name = QLineEdit()
        self.description = QLineEdit()
        self.start_date = QCalendarWidget()
        self.start_date.setMaximumHeight(200)
        self.end_date = QCalendarWidget()
        self.event_layout.layout().addRow('Event Name', self.name)
        self.event_layout.layout().addRow('Event Description', self.description)
        self.event_layout.layout().addRow('Event Start Date', self.start_date)
        self.event_layout.layout().addRow('', QDateTimeEdit())
        self.event_layout.layout().addRow('Event End Date', self.end_date)
        self.event_layout.layout().addRow('', QDateTimeEdit())


        self.save_event_button = QPushButton('Save Button', self)
        self.save_event_button.clicked.connect(self.disable)
        self.event_layout.layout().addRow('', self.save_event_button)

        self.team_label = QLabel("Team Configuration")
        self.team_label.setFont(QFont('MS Shell Dlg 2', 12))
        self.team_layout.layout().addWidget(self.team_label)

        self.lead_ip_address = QLineEdit()
        self.team_layout.layout().addRow('Lead IP Address', self.lead_ip_address)
        self.established_connections = QLabel('')
        self.team_layout.layout().addRow('Established Connections', self.established_connections)
        self.lead_checkbox = QCheckBox()
        self.team_layout.layout().addRow('Lead', self.lead_checkbox)
        self.connect_button = QPushButton('Connect')
        self.team_layout.layout().addRow('',self.connect_button)


        self.layout.addWidget(self.event_layout)
        self.layout.addWidget(self.team_layout)

        self.setLayout(self.layout)







    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print(QMouseEvent.x(), QMouseEvent.y())


    def disable(self):
        self.setDisabled(True)



        #self.show()


