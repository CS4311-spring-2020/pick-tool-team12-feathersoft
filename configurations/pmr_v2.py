from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

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


class PMR(QMainWindow):

    def __init__(self):
        """ Main Window Constructor """
        super().__init__()

        self.setWindowTitle('Prevent Mitigate Recover')
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

        self.layout = QFormLayout()

        self.setGeometry(50, 50, 1000, 800)
        # MenuBar

        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        export_menu = menubar.addMenu('Export')
        file_menu.addAction('Quit')



        configurations_toolbar = QToolBar('PMR')
        configurations_toolbar.addAction('Event Configuration',self.event_configuration_clicked)
        configurations_toolbar.addAction('Directory Configuration',self.directory_configuration_clicked)
        configurations_toolbar.addAction('Graph Configuration', self.graph_configuration_clicked)
        configurations_toolbar.addAction('Log File Configuration', self.log_file_configuration_clicked)
        configurations_toolbar.addAction('Log Entry Configuration',self.log_entry_configuration_clicked)
        configurations_toolbar.addAction('Vector Configuration',self.vector_configuration_clicked)
        configurations_toolbar.addAction('Vector DB Configuration', self.vector_db_configuration_clicked)

        self.addToolBar(Qt.LeftToolBarArea, configurations_toolbar)

        self.show()

    def event_configuration_clicked(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.event_configuration)
        self.statusBar().showMessage('Event Configuration')

    def directory_configuration_clicked(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.directory_configuration)
        self.statusBar().showMessage('Directory Configuration')

    def graph_configuration_clicked(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.graph_builder_configuration)
        self.statusBar().showMessage('Graph Configuration')

    def log_file_configuration_clicked(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.log_file_configuration)
        self.statusBar().showMessage('Event Configuration')

    def log_entry_configuration_clicked(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.log_entry_configuration)
        self.statusBar().showMessage('Log Entry Configuration')

    def vector_configuration_clicked(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.vector_configuration)
        self.statusBar().showMessage('Vector Configuration')

    def vector_db_configuration_clicked(self):
        self.takeCentralWidget()
        if self.event_configuration.lead_checkbox.isChecked():
            self.setCentralWidget(self.vector_db_configuration_lead)
            self.statusBar().showMessage('Vector DB Lead')

        else:
            self.setCentralWidget(self.vector_db_configuration_non_lead)
            self.statusBar().showMessage('Vector DB Non Lead')





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PMR()
    sys.exit(app.exec())




