import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import os

class DirectoryConfiguration(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 744, 600)
        self.setWindowTitle("Directory Configuration")
        self.UI()

    def UI(self):
        # Creating the label for the window
        self.label = QLabel('Directory Configuration', self)
        # Setting the window's font
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.move(280, 40)
        # self.setLayout(vbox)


        self.root_directory_label = QLabel('Root Directory', self)
        # Setting the window's font
        self.root_directory_label.setFont(QFont('MS Shell Dlg 2', 8))
        self.root_directory_label.move(30, 120)


        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(QRect(150, 110, 451, 41))
        self.textEdit.setText("configurations/samples/root")
        filebtn = QPushButton(self)
        filebtn.setFixedHeight(40)
        filebtn.setIcon(QIcon('folder.png'))
        filebtn.move(610,110)
        filebtn.clicked.connect(self.open_file)

        self.event_start_timestamp_label = QLabel('Red Team Folder', self)
        filebtn_r = QPushButton(self)
        filebtn_r.setFixedHeight(40)
        filebtn_r.setIcon(QIcon('folder.png'))
        filebtn_r.move(610, 260)
        filebtn_r.clicked.connect(self.open_file)
        self.event_start_timestamp_label.setFont(QFont('MS Shell Dlg 2', 8))
        self.event_start_timestamp_label.move(20,270)

        self.textEdit_3 = QTextEdit(self)
        self.textEdit_3.setGeometry(QRect(150, 260, 451, 41))

        self.event_start_timestamp_label = QLabel('Blue Team Folder', self)
        filebtn_b = QPushButton(self)
        filebtn_b.setFixedHeight(40)
        filebtn_b.setIcon(QIcon('folder.png'))
        filebtn_b.move(610, 340)
        filebtn_b.clicked.connect(self.open_file)

        self.event_start_timestamp_label.setFont(QFont('MS Shell Dlg 2', 8))
        self.event_start_timestamp_label.move(20, 350)

        self.textEdit_4 = QTextEdit(self)
        self.textEdit_4.setGeometry(QRect(150, 340, 451, 41))

        self.white_team_label = QLabel('White Team Folder',self)
        self.white_team_label.move(10,430)
        self.textEdit_5 = QTextEdit(self)
        self.textEdit_5.setGeometry(QRect(150, 420, 451, 41))
        filebtn_b = QPushButton(self)
        filebtn_b.setFixedHeight(40)
        filebtn_b.setIcon(QIcon('folder.png'))
        filebtn_b.move(610, 420)
        filebtn_b.clicked.connect(self.open_file)



        self.save_event_button = QPushButton(self)
        self.save_event_button.setText('Save Data Ingestion')
        self.save_event_button.setGeometry(QRect(150, 480, 451, 41))
        #self.show()
        #self.open_file()





    def open_file(self):
        url = QFileDialog.getOpenFileName(self,'Open a file',"","All Files(*);;*txt")
        print(url)


class EnforcementAction(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 744, 600)
        self.setWindowTitle("Enforcement Action")
        self.UI()

    def UI(self):
        # Creating the label for the window
        self.label = QLabel('Enforcement Action', self)
        # Setting the window's font
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.move(280, 40)
        #self.show()
        # self.setLayout(vbox)

