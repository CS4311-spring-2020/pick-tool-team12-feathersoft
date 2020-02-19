import sys
from PyQt5.QtWidgets import *
from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.graph_format_configuration import GraphFormatConfiguration
from configurations.tab_format_configuration import TabFormatConfiguration
from configurations.directory_configuration import DirectoryConfiguration
from configurations.event_configuration import EventConfiguratation
from configurations.log_file_configuration import LogFileConfiguration
from configurations.relationship_configuration import RelationshipConfiguration
from configurations.team_configuration import TeamConfiguratation
from configurations.vector_configuration import VectorConfiguration
from configurations.vector_db_configuration_lead import VectorDBConfigurationLeadWindow
from configurations.vector_configuration_non_lead import VectorDBConfigurationNonLeadWindow
from configurations.icon_configuration import IconConfigurationWindow
from configurations.graph_configuration import GraphConfigurationWindow


class PMR(QWidget):
    def __init__(self):
        super(PMR, self).__init__()
        self.configurations = QListWidget()
        self.configurations.setFixedWidth(300)
        self.configurations.setFixedHeight(800)
        self.configurations.move(300, 1200)
        self.configurations.insertItem(0, 'Team Configuration')
        self.configurations.insertItem(1, 'Event Configuration')
        self.configurations.insertItem(2, 'Directory Configuration')
        self.configurations.insertItem(3, 'Vector Configuration')
        self.configurations.insertItem(4, 'Log File Configuration')
        self.configurations.insertItem(5, 'Log Entry Configuration')
        self.configurations.insertItem(6, 'Vector DB Configuration')
        self.configurations.insertItem(7, 'Icon Configuration')
        self.configurations.insertItem(8, 'Graph Builder Configuration')
        self.configurations.insertItem(9, 'Nodes Configuration')
        self.configurations.insertItem(10, 'Relationship Configuration')

        self.teamStack = QWidget()
        self.eventStack = QWidget()
        self.directoryStack = QWidget()
        self.vectorStack = QWidget()
        self.logFileStack = QWidget()
        self.logEntryStack = QWidget()
        self.vectorDBStack = QWidget()
        self.iconStack = QWidget()
        self.graphBuilderStack = QWidget()
        self.nodesStack = QWidget()
        self.relationshipStack = QWidget()

        self.configurations.currentRowChanged.connect(self.display)
        self.teamEventUI()
        self.eventEventUI()
        self.directoryEventUI()
        self.vectorEventUI()
        self.logFileEventUI()
        self.logEntryEventUI()
        self.vectorDBEventUI()
        self.iconEventUI()
        self.graphBuilderEventUI()
        self.nodesEventUI()
        self.relationshipsEventUI()

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.teamStack)
        self.stack.addWidget(self.eventStack)
        self.stack.addWidget(self.directoryStack)
        self.stack.addWidget(self.vectorStack)
        self.stack.addWidget(self.logFileStack)
        self.stack.addWidget(self.logEntryStack)
        self.stack.addWidget(self.vectorDBStack)
        self.stack.addWidget(self.iconStack)
        self.stack.addWidget(self.graphBuilderStack)
        self.stack.addWidget(self.nodesStack)
        self.stack.addWidget(self.relationshipStack)

        HBox = QHBoxLayout(self)
        HBox.addWidget(self.configurations)
        HBox.addWidget(self.stack)

        self.setLayout(HBox)
        self.setGeometry(300, 50, 1300, 1000)
        self.setWindowTitle('PMR')
        self.show()

    def teamEventUI(self):
        h = QHBoxLayout(self)
        tc = TeamConfiguratation()
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

    def logEntryEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(LogEntryConfigurationWindow())
        self.logEntryStack.setLayout(h)

    def vectorDBEventUI(self):
        h = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.addTab(VectorDBConfigurationLeadWindow(),'Vector DB Lead')
        self.tabs.addTab(VectorDBConfigurationNonLeadWindow(), 'Vector DB Non-Lead')
        h.addWidget(self.tabs)
        self.vectorDBStack.setLayout(h)

    def iconEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(IconConfigurationWindow())
        self.iconStack.setLayout(h)

    def graphBuilderEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(GraphConfigurationWindow())
        self.graphBuilderStack.setLayout(h)

    def nodesEventUI(self):
        h = QHBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.addTab(TabFormatConfiguration(),'Tab Format Configuration')
        self.tabs.addTab(GraphFormatConfiguration(), 'Graph Format Configuration')
        h.addWidget(self.tabs)
        self.nodesStack.setLayout(h)


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
