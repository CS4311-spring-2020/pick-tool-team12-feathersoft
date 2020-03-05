import sys
from PyQt5.QtWidgets import *
from configurations.log_entry_configuration import LogEntryConfiguration
from configurations.directory_configuration import DirectoryConfiguration
from configurations.event_configuration import EventConfiguratation
from configurations.log_file_configuration import LogFileConfiguration
from configurations.relationship_configuration import RelationshipConfiguration
from configurations.team_configuration import TeamConfiguratation
from configurations.vector_configuration import VectorConfiguration
from configurations.vector_db_configuration_lead import VectorDBConfigurationLead
from configurations.vector_configuration_non_lead import VectorDBConfigurationNonLead
from configurations.icon_configuration import IconConfiguration
from configurations.graph_configuration import GraphConfiguration
from configurations.filter_configuration import FilterConfiguration
from configurations.export_configuration import ExportConfiguration
from configurations.change_configuration import ChangeConfiguration
from configurations.graph_format_configuration import GraphFormatConfiguration
from configurations.tab_format_configuration import TabFormatConfiguration
from configurations.splunk_client import splunk_integrator
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class PMR(QWidget):
    def __init__(self):
        super(PMR, self).__init__()

        # Creating references to each window being used in the system.
        self.team_configuration = TeamConfiguratation()
        self.event_configuration = EventConfiguratation()
        self.directory_configuration = DirectoryConfiguration()
        self.vector_configuration = VectorConfiguration()
        self.log_file_configuration = LogFileConfiguration()
        self.log_entry_configuration = LogEntryConfiguration()
        self.export_configuration = ExportConfiguration()
        self.change_configuration = ChangeConfiguration()
        self.vector_db_configuration_lead = VectorDBConfigurationLead()
        self.vector_db_configuration_non_lead = VectorDBConfigurationNonLead()
        self.icon_configuration = IconConfiguration()
        self.graph_builder_configuration = GraphConfiguration()
        self.graph_format_configuration = GraphFormatConfiguration()
        self.tab_format_configuration = TabFormatConfiguration()
        self.relationship_configuration = RelationshipConfiguration()




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
        self.team_configuration.pushButton.clicked.connect(self.team_button_clicked)
        h.addWidget(self.team_configuration,stretch=0)
        self.teamStack.setLayout(h)

    def eventEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(self.event_configuration)
        self.eventStack.setLayout(h)

    def directoryEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(self.directory_configuration)
        self.directoryStack.setLayout(h)

    def vectorEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(self.vector_configuration)
        self.vectorStack.setLayout(h)

    def logFileEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(self.log_file_configuration)
        self.logFileStack.setLayout(h)

    def logEntryEventUI(self):
        h = QVBoxLayout(self)
        h.addWidget(self.log_entry_configuration,stretch=0)

        self.logEntryStack.setLayout(h)

    def vectorDBEventUI(self):
         lead_layout = QHBoxLayout()
        # lead_layout.addWidget(self.vector_db_configuration_lead)
        # non_lead_layout = QHBoxLayout()
        # non_lead_layout.addWidget(self.vector_db_configuration_non_lead)
        # if self.team_configuration.checkBox.isChecked():
        #     print('is checked')
        #     self.vectorDBStack.setLayout(lead_layout)
        # else:
        #     self.vectorDBStack.setLayout(non_lead_layout)

    def iconEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(self.icon_configuration)
        self.iconStack.setLayout(h)

    def graphBuilderEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(self.graph_builder_configuration)
        self.graphBuilderStack.setLayout(h)

    def nodesEventUI(self):
        h = QHBoxLayout(self)
        self.tabs = QTabWidget()
        self.tabs.addTab(self.tab_format_configuration,'Tab Format Configuration')
        self.tabs.addTab(self.graph_format_configuration, 'Graph Format Configuration')
        h.addWidget(self.tabs)
        self.nodesStack.setLayout(h)

    def team_button_clicked(self):
        layout = QHBoxLayout()
        if self.team_configuration.checkBox.isChecked():
            self.vectorDBStack.destroy()
            layout.addWidget(self.vector_db_configuration_lead)

        else:
            layout.addWidget(self.vector_db_configuration_non_lead)
        self.vectorDBStack.setLayout(layout)

    def relationshipsEventUI(self):
        h = QHBoxLayout(self)
        h.addWidget(self.relationship_configuration)
        self.relationshipStack.setLayout(h)

    def display(self,i):
        self.stack.setCurrentIndex(i)


def main():
    app = QApplication(sys.argv)
    ex = PMR()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
