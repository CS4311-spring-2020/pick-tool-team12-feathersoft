from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.event_configuration import EventConfigurationWindow
from configurations.log_file_configuration import LogFileConfigurationWindow
from configurations.relationship_configuration import RelationshipConfigurationWindow
from configurations.vector_configuration import VectorConfiguration
from configurations.vector_db_configuration_lead import VectorDBConfigurationLead
from configurations.vector_configuration_non_lead import VectorDBConfigurationNonLead
from configurations.icon_configuration import IconConfiguration
from configurations.graph_configuration import GraphConfigurationWindow
from configurations.export_configuration import ExportConfigurationWindow
from configurations.change_configuration import ChangeConfigurationWindow
from configurations.graph_format_configuration import GraphFormatConfiguration
from configurations.tab_format_configuration import TabFormatConfiguration
from configurations.custom_widgets import CheckableComboBox


class PMR(QMainWindow):

    """
        The PMR class is the main window or controller between the configuration windows
    """

    def __init__(self):
        """ Main Window Constructor """
        super().__init__()

        self.setWindowTitle('Prevent Mitigate Recover')
        self.event_configuration = EventConfigurationWindow()
        self.vector_configuration = VectorConfiguration()
        self.log_file_configuration = LogFileConfigurationWindow()
        self.log_entry_configuration = LogEntryConfigurationWindow()
        self.export_configuration = ExportConfigurationWindow()
        self.change_configuration = ChangeConfigurationWindow()
        self.vector_db_configuration_lead = VectorDBConfigurationLead()
        self.vector_db_configuration_non_lead = VectorDBConfigurationNonLead()
        self.icon_configuration = IconConfiguration()
        self.graph_builder_configuration = GraphConfigurationWindow()
        self.graph_format_configuration = GraphFormatConfiguration()
        self.tab_format_configuration = TabFormatConfiguration()
        self.relationship_configuration = RelationshipConfigurationWindow()

        self.configurations_toolbar = QToolBar('PMR')
        self.configurations_toolbar.addAction('Event Configuration', self.event_configuration_clicked)
        self.configurations_toolbar.addAction('Log File Configuration', self.log_file_configuration_clicked)
        self.configurations_toolbar.addAction('Log Entry Configuration', self.log_entry_configuration_clicked)
        self.configurations_toolbar.addAction('Graph Configuration', self.graph_configuration_clicked)
        self.configurations_toolbar.addAction('Vector Configuration', self.vector_configuration_clicked)
        self.configurations_toolbar.addAction('Vector DB Configuration', self.vector_db_configuration_clicked)
        self.setGeometry(50, 50, 1100, 700)

        # MenuBar
        self.menubar = self.menuBar()
        self.file_menu = self.menubar.addMenu('File')
        self.export_menu = self.menubar.addMenu('Export')
        self.file_menu.addAction('Quit')

        # Disable access to the rest of the screens until an event has been configured.
        # This is because it would not make sense to continue until an event is valid.

        self.disable_toolbar()

        # Enable the rest of the toolbar after event has been configured
        self.event_configuration.configured.connect(self.enable_toolbar)

        # Populate the log file table after logs a have been ingested
        self.event_configuration.logs_ingested.connect(self.populate_log_files)

        # Popluate enforcement action reports
        self.event_configuration.reports_generated.connect(self.populate_er)

        # Populate the log entries table after ingestion
        self.event_configuration.ingestion_complete.connect(self.populate_log_entries)

        # Update the log entries table vector list each time a vector is added
        self.vector_configuration.vector_added.connect(self.update_log_entry_vectors)

        # Update the log entries table vector list each time a vector deleted.
        self.vector_configuration.vector_deleted.connect(self.update_log_entry_vectors)

        self.addToolBar(Qt.LeftToolBarArea, self.configurations_toolbar)
        self.setCentralWidget(self.event_configuration)
        self.statusBar().showMessage('Event Configuration')
        self.show()

    def event_configuration_clicked(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.event_configuration)
        self.statusBar().showMessage('Event Configuration')

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

    def disable_toolbar(self):
        for action in self.configurations_toolbar.actions():
            action.setEnabled(False if action.text() !='Event Configuration' else True)

    def enable_toolbar(self):
        for action in self.configurations_toolbar.actions():
            action.setEnabled(True)

    def populate_log_entries(self):
        self.log_entry_configuration.populate_table(self.event_configuration.splunk_client.entries)

    def populate_log_files(self):
        self.log_file_configuration.populate_table(self.event_configuration.logs)

    def populate_er(self):
        self.log_file_configuration.er_reports = self.event_configuration.splunk_client.file_validator.reports

    def update_log_entry_vectors(self):
        size = [str(i) for i in range(int(self.vector_configuration.table.rowCount()))]
        for i in range(self.log_entry_configuration.table.rowCount()):
            combobox = CheckableComboBox()
            combobox.addItems(size)
            self.log_entry_configuration.table.setCellWidget(i,6,combobox)

        # for i in range(self.vector_db_configuration_non_lead.table.rowCount()):
        #     combobox = CheckableComboBox()
        #     combobox.addItems(size)
        #     self.vector_db_configuration_non_lead.table.setCellWidget(i,1,combobox)
        #
        # for i in range(self.vector_db_configuration_non_lead.table.rowCount()):
        #     combobox = CheckableComboBox()
        #     combobox.addItems(size)
        #     self.vector_db_configuration_lead.table.setCellWidget(i,1,combobox)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Ubuntu')
    window = PMR()
    sys.exit(app.exec())




