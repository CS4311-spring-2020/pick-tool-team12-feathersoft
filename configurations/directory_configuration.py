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

        self.label = QLabel('Directory Configuration')
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        main_layout = QFormLayout()

        main_layout.addRow(QLabel('Directory Configuration', alignment=Qt.AlignLeft, font=QFont('MS Shell Dlg 2', 12)))
        root_directory_layout = QWidget()
        root_directory_layout.setLayout(QHBoxLayout())
        self.root_directory_edit = QLineEdit()
        self.filebtn = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        root_directory_layout.layout().addWidget(self.root_directory_edit)
        root_directory_layout.layout().addWidget(self.filebtn)


        red_directory_layout = QWidget()
        red_directory_layout.setLayout(QHBoxLayout())
        self.red_directory_edit = QLineEdit()
        self.filebtn2 = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        red_directory_layout.layout().addWidget(self.red_directory_edit)
        red_directory_layout.layout().addWidget(self.filebtn2)


        blue_directory_layout = QWidget()
        blue_directory_layout.setLayout(QHBoxLayout())
        self.blue_directory_edit = QLineEdit()
        self.filebtn3 = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        blue_directory_layout.layout().addWidget(self.blue_directory_edit)
        blue_directory_layout.layout().addWidget(self.filebtn3)

        white_directory_layout = QWidget()
        white_directory_layout.setLayout(QHBoxLayout())
        self.white_directory_edit = QLineEdit()
        self.filebtn4 = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        white_directory_layout.layout().addWidget(self.white_directory_edit)
        white_directory_layout.layout().addWidget(self.filebtn4)

        main_layout.addRow('Root Directory',root_directory_layout)
        main_layout.addRow('Red Team Folder',red_directory_layout)
        main_layout.addRow('Blue Team Folder',blue_directory_layout)
        main_layout.addRow('White Team Folder',white_directory_layout)
        main_layout.addRow('',QPushButton('Ingest',clicked=self.validate_root_structure))

        main_layout.setSpacing(30)

        self.setLayout(main_layout)

    def open_file(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory",directory=os.path.realpath(os.getcwd())))
        if self.sender() == self.filebtn:
            self.root_directory_edit.setText(file)

        elif self.sender() == self.filebtn2:
            self.red_directory_edit.setText(file)

        elif self.sender() == self.filebtn3:
            self.blue_directory_edit.setText(file)

        else:
            self.white_directory_edit.setText(file)

    def validate_root_structure(self):
        if self.root_directory_edit.text() != '':
            if len(os.listdir(self.root_directory_edit.text())) != 3:
                QMessageBox.critical(self,"Root Directory Structure Error",
                                     "Root Directory does not provide all required folders")

            else:
                buttonReply = QMessageBox.question(self, 'PyQt5 message',
                                                   "Begin Ingestion?",
                                                   QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel,
                                                   QMessageBox.Cancel)
                if buttonReply == QMessageBox.Yes:
                    self.begin_ingestion()

    def begin_ingestion(self):
        pass


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

