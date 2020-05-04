import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ExportConfigurationWindow(QWidget):
    """
        The Export Configuration Window is used to allow the user to select the format they want to export the graph
        into.
    """
    def __init__(self):
        super().__init__()
        self.setGeometry(650,300, 600,400)
        self.setWindowTitle('Export Configuration')
        self.setMaximumSize(600,400)
        self.file_name = ''
        self.extension = ''
        self.UI()

    def UI(self):
        self.layout = QVBoxLayout()
        self.save_as = QLineEdit()
        self.label = QLabel('EXPORT FORMAT',self)
        self.combobox = QComboBox(self)
        self.combobox.addItems(['', 'jpg', 'png', 'pdf'])
        self.btn = QPushButton('Export',self,clicked=self.button_clicked)
        self.layout.addWidget(self.save_as)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combobox)
        self.layout.addWidget(self.btn)
        self.setLayout(self.layout)

    def button_clicked(self):
        self.file_name = self.save_as.text()
        self.extension = str(self.combobox.currentText())
        self.close()



if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = ExportConfigurationWindow()
    sys.exit(App.exec())