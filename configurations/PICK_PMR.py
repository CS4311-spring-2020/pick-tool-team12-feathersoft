import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.eventConfiguration import EventConfigurationWindow


class PMR(QTabWidget):
    def __init__(self,parent=None):
        super(PMR,self).__init__(parent)
        self.setWindowTitle("PICK PMR")
        self.setGeometry(50,50,1000,800)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()
        self.teamConfiguration = QWidget()
        self.eventConfiguration = QWidget()
        self.directoryConfiguration = QWidget()
        self.vectorConfiguration = QWidget()
        self.logFileConfiguration = QWidget()
        self.filterConfiguration = QWidget()

        # self.tabs.addTab(self.teamConfiguration, "Team Configuration")
        # self.tabs.addTab(self.eventConfiguration, "Event Configuration")
        # self.tabs.addTab(self.directoryConfiguration, "Directory Configuration")
        # self.tabs.addTab(self.vectorConfiguration, "Vector Configuration")
        # self.tabs.addTab(self.logFileConfiguration, "Log Event Configuration")
        

        mainLayout.addWidget(self.tabs)
        self.setLayout(mainLayout)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PMR()
    sys.exit(app.exec_())


