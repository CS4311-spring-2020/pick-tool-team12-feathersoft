import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.eventConfiguration import EventConfigurationWindow
from configurations.export_configuration import ExportConfigurationWindow
from configurations.teamConfiguration import TeamConfigurationWindow
from configurations.change_configuration import ChangeConfigurationWindow
from configurations.teamConfiguration import TeamConfigurationWindow
from configurations.eventConfiguration import EventConfigurationWindow
from configurations.directoryConfiguration import DirectoryConfigurationWindow
from configurations.VectorDBConfigurationLead import VectorDBConfigurationLeadWindow
from configurations.GraphConfiguration import GraphConfigurationWindow
from configurations.IconConfiguration import IconConfigurationWindow
from configurations.VectorDBConfigurationNonLead import VectorDBConfigurationNonLeadWindow

class PMR(QWidget):

    def __init__(self):
        super(PMR, self).__init__()
        self.configurations = QListWidget()
        self.configurations.setFixedWidth(250)
        self.configurations.setFixedHeight(800)
        self.configurations.move(300,1200)
        self.configurations.insertItem(0,'Log Entry Configuration')
        self.configurations.insertItem(1,'Change Configuration')
        self.configurations.insertItem(2,'Vector DB Lead Configuration')
        self.eventStack = QWidget()
        self.changeStack = QWidget()
        self.vectordbleadstack = QWidget()

        self.configurations.currentRowChanged.connect(self.display)
        self.logeventUI()
        self.changeEventUI()
        self.vectorDBLeadUI()

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.eventStack)
        self.stack.addWidget(self.changeStack)
        self.stack.addWidget(self.vectordbleadstack)

        HBox = QHBoxLayout(self)
        HBox.addWidget(self.configurations)
        HBox.addWidget(self.stack)

        self.setLayout(HBox)
        self.setGeometry(300,50,1400,1200)
        self.setWindowTitle('PMR')
        self.show()

    def logeventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(LogEntryConfigurationWindow())
        self.eventStack.setLayout(h)

    def changeEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(ChangeConfigurationWindow())
        self.changeStack.setLayout(h)

    def vectorDBLeadUI(self):
        h = QHBoxLayout(self)
        h.addWidget(TeamConfigurationWindow())
        self.vectordbleadstack.setLayout(h)

    def display(self,i):
        self.stack.setCurrentIndex(i)



def main():
    app = QApplication(sys.argv)
    ex = PMR()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
