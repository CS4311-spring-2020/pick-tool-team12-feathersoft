import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.samples.dc import DirectoryConfiguration
from configurations.eventConfiguration import EventConfigurationWindow
from configurations.export_configuration import ExportConfigurationWindow
from configurations.teamConfiguration import TeamConfigurationWindow
from configurations.eventConfiguration import EventConfigurationWindow
from configurations.directoryConfiguration import DirectoryConfigurationWindow
from configurations.VectorDBConfigurationLead import VectorDBConfigurationLeadWindow
from configurations.GraphConfiguration import GraphConfigurationWindow
from configurations.IconConfiguration import IconConfigurationWindow
from configurations.VectorDBConfigurationNonLead import VectorDBConfigurationNonLeadWindow
from configurations.change_configuration import ChangeConfigurationWindow



class PMR(QTabWidget):
    def __init__(self,parent=None):
        super(PMR,self).__init__(parent)
        self.setWindowTitle("PICK PMR")
        self.setGeometry(50,50,1500,1300)
        self.UI()

    def UI(self):
        self.mainLayout = QVBoxLayout()
        self.tabs = QTabWidget()



        self.tabs.addTab(TeamConfigurationWindow(), "Team Configuration")
        self.tabs.addTab(EventConfigurationWindow(), "Event Configuration")
        self.tabs.addTab(DirectoryConfiguration(), "Directory Configuration")
        self.tabs.addTab(ChangeConfigurationWindow(), "Change Configuration")
        self.tabs.addTab(VectorDBConfigurationLeadWindow(), 'VectorDB Configuration Lead')
        self.tabs.addTab(VectorDBConfigurationNonLeadWindow(), 'VectorDB Configuration Non Lead')
        self.tabs.addTab(LogEntryConfigurationWindow(), "Log Event Configuration")

        self.tabs.addTab(ExportConfigurationWindow(), "Export Configuration")
        self.tabs.addTab(GraphConfigurationWindow(), "Graph Configuration")

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


