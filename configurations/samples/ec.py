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
        # Creating the label for the window
        self.label = QLabel('Event Configuration', self)
        # Setting the window's font
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.move(175, 75)
        # self.setLayout(vbox)

        self.event_name_label = QLabel('Event Name', self)
        # Setting the window's font
        self.event_name_label.setFont(QFont('MS Shell Dlg 2', 8))
        self.event_name_label.move(30, 140)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(150, 130, 241, 51))

        self.event_description_label = QLabel('Event Description', self)
        self.event_description_label.setFont(QFont('MS Shell Dlg 2', 8))
        self.event_description_label.move(20, 230)


        self.textEdit_2 = QTextEdit(self)
        self.textEdit_2.setGeometry(QRect(150, 220, 241, 51))

        self.event_start_timestamp_label = QLabel('Event Start Timestamp', self)
        self.event_start_timestamp_label.setFont(QFont('MS Shell Dlg 2', 8))
        self.event_start_timestamp_label.move(8, 320)

        self.textEdit_3 = QTextEdit(self)
        self.textEdit_3.setGeometry(QRect(150, 310, 241, 51))

        self.event_start_timestamp_label = QLabel('Event End Timestamp', self)
        self.event_start_timestamp_label.setFont(QFont('MS Shell Dlg 2', 8))
        self.event_start_timestamp_label.move(8, 410)

        self.textEdit_4 = QTextEdit(self)
        self.textEdit_4.setGeometry(QRect(150, 400, 241, 51))

        self.save_event_button = QPushButton(self)
        self.save_event_button.setText('Save Event')
        self.save_event_button.setGeometry(QRect(150, 500, 241, 61))

        self.save_event_button.clicked.connect(self.disable)
        self.show()


    def disable(self):
        self.setDisabled(True)



        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = EventConfiguratation()
    sys.exit(App.exec())