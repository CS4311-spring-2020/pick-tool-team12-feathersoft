import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.change_configuration import ChangeConfigurationWindow
from configurations.samples.cgf import GraphFormatConfiguration
from configurations.samples.ctf import TabFormatConfiguration
from configurations.samples.dc import DirectoryConfiguration
from configurations.samples.ec import EventConfiguratation
from configurations.samples.fc import FilterConfiguratation
from configurations.samples.lfc import LogFileConfiguration
from configurations.samples.rc import RelationshipConfiguration
from configurations.samples.tc import TeamConfiguratation
from configurations.samples.vc import VectorConfiguration
from configurations.export_configuration import ExportConfigurationWindow
from configurations.VectorDBConfigurationLead import VectorDBConfigurationLeadWindow
from configurations.VectorDBConfigurationNonLead import VectorDBConfigurationNonLeadWindow
from configurations.IconConfiguration import IconConfigurationWindow
from configurations.GraphConfiguration import GraphConfigurationWindow
class PMR(QWidget):

    def __init__(self):
        super(PMR, self).__init__()
        self.configurations = QListWidget()
        self.configurations.setFixedWidth(300)
        self.configurations.setFixedHeight(800)
        self.configurations.move(300,1200)
        self.configurations.insertItem(0,'Team Configuration')
        self.configurations.insertItem(1,'Event Configuration')
        self.configurations.insertItem(2,'Directory Configuration')
        self.configurations.insertItem(3, 'Vector Configuration')
        self.configurations.insertItem(4, 'Log File Configuration')
        self.configurations.insertItem(5, 'Filter Configuration')
        self.configurations.insertItem(6, 'Log Entry Configuration')
        self.configurations.insertItem(7, 'Export Configuration')
        self.configurations.insertItem(8, 'Change Configuration')
        self.configurations.insertItem(9, 'Vector DB Configuration')
        self.configurations.insertItem(10, 'Icon Configuration')
        self.configurations.insertItem(12, 'Graph Builder Configuration')
        self.configurations.insertItem(13, 'Nodes Configuration in Tabular Format')
        self.configurations.insertItem(14, 'Nodes Configuration in Graphical Format')
        self.configurations.insertItem(15, 'Relationship Configuration')
        self.teamStack = QWidget()
        self.eventStack = QWidget()
        self.directoryStack = QWidget()
        self.vectorStack = QWidget()
        self.logFileStack = QWidget()
        self.filterStack = QWidget()
        self.logEntryStack = QWidget()
        self.exportStack = QWidget()
        self.changeStack = QWidget()
        self.vectorDBStack = QWidget()
        self.iconStack = QWidget()
        self.graphBuilderStack = QWidget()
        self.nodeTabStack = QWidget()
        self.nodeGraphStack = QWidget()
        self.relationshipStack = QWidget()

        self.configurations.currentRowChanged.connect(self.display)
        self.teamEventUI()
        self.eventEventUI()
        self.directoryEventUI()
        self.vectorEventUI()
        self.logFileEventUI()
        self.filterEventUI()
        self.logEntryEventUI()
        self.exportEventUI()
        self.changeEventUI()
        self.vectorDBEventUI()
        self.iconEventUI()
        self.graphBuilderEventUI()
        self.nodesGraphEventUI()
        self.nodesTabEventUI()
        self.relationshipsEventUI()

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.teamStack)
        self.stack.addWidget(self.eventStack)
        self.stack.addWidget(self.directoryStack)
        self.stack.addWidget(self.vectorStack)
        self.stack.addWidget(self.logFileStack)
        self.stack.addWidget(self.filterStack)
        self.stack.addWidget(self.logEntryStack)
        self.stack.addWidget(self.exportStack)
        self.stack.addWidget(self.changeStack)
        self.stack.addWidget(self.vectorDBStack)
        self.stack.addWidget(self.iconStack)
        self.stack.addWidget(self.graphBuilderStack)
        self.stack.addWidget(self.nodeTabStack)
        self.stack.addWidget(self.nodeGraphStack)
        self.stack.addWidget(self.relationshipStack)

        HBox = QHBoxLayout(self)
        HBox.addWidget(self.configurations)
        HBox.addWidget(self.stack)

        self.setLayout(HBox)
        self.setGeometry(300,50,1400,1200)
        self.setWindowTitle('PMR')
        self.show()

    def teamEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(TeamConfiguratation())
        self.teamStack.setLayout(h)

    def eventEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(EventConfiguratation())
        self.eventStack.setLayout(h)

    def directoryEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(DirectoryConfiguration())
        self.directoryStack.setLayout(h)

    def vectorEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(VectorConfiguration())
        self.vectorStack.setLayout(h)

    def logFileEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(LogFileConfiguration())
        self.logFileStack.setLayout(h)

    def filterEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(FilterConfiguratation())
        self.filterStack.setLayout(h)

    def logEntryEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(LogEntryConfigurationWindow())
        self.logEntryStack.setLayout(h)

    def exportEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(ExportConfigurationWindow())
        self.exportStack.setLayout(h)

    def changeEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(ChangeConfigurationWindow())
        self.changeStack.setLayout(h)

    def vectorDBEventUI(self):
        h = QVBoxLayout(self)
        h.addWidget(VectorDBConfigurationLeadWindow())
        h.addWidget(VectorDBConfigurationNonLeadWindow())
        self.vectorDBStack.setLayout(h)

    def iconEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(IconConfigurationWindow())
        self.iconStack.setLayout(h)

    def graphBuilderEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(GraphConfigurationWindow())
        self.graphBuilderStack.setLayout(h)

    def nodesGraphEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(GraphFormatConfiguration())
        self.nodeGraphStack.setLayout(h)

    def nodesTabEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(TabFormatConfiguration())
        self.nodeTabStack.setLayout(h)

    def relationshipsEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(RelationshipConfiguration())
        self.relationshipStack.setLayout(h)


    def display(self,i):
        self.stack.setCurrentIndex(i)



def main():
    app = QApplication(sys.argv)
    ex = PMR()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
