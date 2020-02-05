import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.eventConfiguration import EventConfigurationWindow
from configurations.teamConfiguration import TeamConfigurationWindow
from configurations.change_configuration import ChangeConfigurationWindow
from configurations.teamConfiguration import TeamConfigurationWindow
from configurations.eventConfiguration import EventConfigurationWindow
from configurations.directoryConfiguration import DirectoryConfigurationWindow
from configurations.VectorDBConfigurationLead import Window

class PMR(QTabWidget):
    def __init__(self,parent=None):
        super(PMR,self).__init__(parent)
        self.setWindowTitle("PICK PMR")
        self.setGeometry(50,50,2000,1800)
        self.UI()

    def UI(self):
        self.mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()


        self.tabs.addTab(TeamConfigurationWindow(), "Team Configuration")
        # self.tabs.addTab(EventConfigurationWindow(), "Event Configuration")
        self.tabs.addTab(DirectoryConfigurationWindow(), "Directory Configuration")
        #self.tabs.addTab(ChangeConfigurationWindow(), "Change Configuration")
        self.tabs.addTab(Window(), 'VectorDBConfiguration')
        self.tabs.addTab(LogEntryConfigurationWindow(), "Log Event Configuration")


        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)
        self.show()

    def logEventConfigurationUI(self):
        self.lecLayout = QVBoxLayout()
        lec = LogEntryConfigurationWindow()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PMR()
    sys.exit(app.exec_())


