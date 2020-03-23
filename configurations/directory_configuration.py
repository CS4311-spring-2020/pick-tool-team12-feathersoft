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
        root_directory_edit = QLineEdit()
        filebtn = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        root_directory_layout.layout().addWidget(root_directory_edit)
        root_directory_layout.layout().addWidget(filebtn)

        red_directory_layout = QWidget()
        red_directory_layout.setLayout(QHBoxLayout())
        red_directory_edit = QLineEdit()
        filebtn2 = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        red_directory_layout.layout().addWidget(red_directory_edit)
        red_directory_layout.layout().addWidget(filebtn2)

        blue_directory_layout = QWidget()
        blue_directory_layout.setLayout(QHBoxLayout())
        blue_directory_edit = QLineEdit()
        filebtn3 = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        blue_directory_layout.layout().addWidget(blue_directory_edit)
        blue_directory_layout.layout().addWidget(filebtn3)

        white_directory_layout = QWidget()
        white_directory_layout.setLayout(QHBoxLayout())
        white_directory_edit = QLineEdit()
        filebtn4 = QPushButton(self, clicked=self.open_file,icon=QIcon('folder.png'))
        white_directory_layout.layout().addWidget(white_directory_edit)
        white_directory_layout.layout().addWidget(filebtn4)

        main_layout.addRow('Root Directory',root_directory_layout)
        main_layout.addRow('Red Team Folder',red_directory_layout)
        main_layout.addRow('Blue Team Folder',blue_directory_layout)
        main_layout.addRow('White Team Folder',white_directory_layout)

        main_layout.setSpacing(30)

        self.setLayout(main_layout)





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

