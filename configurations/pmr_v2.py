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
from configurations.custom_widgets import CheckableComboBox
from configurations.rwo.vector import Vector
from configurations.rwo.node import Node


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
        self.log_entry_configuration = LogEntryConfigurationWindow(self.event_configuration.files)
        self.export_configuration = ExportConfigurationWindow()
        self.change_configuration = ChangeConfigurationWindow()
        self.vector_db_configuration_lead = VectorDBConfigurationLead()
        self.vector_db_configuration_non_lead = VectorDBConfigurationNonLead()
        self.icon_configuration = IconConfiguration()
        self.graph_builder_configuration = GraphConfigurationWindow()
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
        self.tools_menu = self.menubar.addMenu('Tools')
        self.file_menu.addAction('Quit')

        # Disable access to the rest of the screens until an event has been configured.
        # This is because it would not make sense to continue until an event is valid.

        #self.disable_toolbar()

        # Enable the rest of the toolbar after event has been configured
        self.event_configuration.configured.connect(self.enable_toolbar)

        # Populate the log file table after logs a have been ingested
        self.event_configuration.logs_ingested.connect(self.populate_log_files)

        # Populate enforcement action reports
        self.event_configuration.reports_generated.connect(self.populate_er)

        # Populate the log entries table after ingestion
        self.event_configuration.ingestion_complete.connect(self.populate_log_entries)

        # Update the log entries table vector list each time a vector is added
        self.vector_configuration.vector_added.connect(self.update_log_entry_vectors)

        # Update the log entries table vector list each time a vector deleted.
        self.vector_configuration.vector_deleted.connect(self.update_log_entry_vectors)

        # Update the vector db when vectors are checked
        self.vector_configuration.vector_selected.connect(self.update_vector_db)

        # Update the node table when significant log entries are flagged
        self.log_entry_configuration._log_entry_flagged.connect(self.update_nodes)

        # Undo log entries table filter
        self.log_entry_configuration._table_reverted.connect(self.revert_table)

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
            action.setEnabled(False if action.text() != 'Event Configuration' else True)

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
            self.log_entry_configuration.table.setCellWidget(i, 6, combobox)

    def update_vector_db(self):
        selected_vectors = set()
        for i in range(self.vector_configuration.table.rowCount()):
            if self.vector_configuration.table.cellWidget(i,2).isChecked():
                name, desc = self.vector_configuration.table.item(i,0),self.vector_configuration.table.item(i,1)
                if name is not None and desc is not None:
                    selected_vectors.add(Vector(name.text(),desc.text()))

        self.vector_db_configuration_non_lead.table.setRowCount(len(selected_vectors))
        for i in range(len(selected_vectors)):
            vec = selected_vectors.pop()
            self.vector_db_configuration_non_lead.table.setItem(i, 0, QTableWidgetItem(vec.get_vector_name))
            self.vector_db_configuration_non_lead.table.setItem(i, 1, QTableWidgetItem(vec.get_vector_description))
            self.vector_db_configuration_non_lead.table.setCellWidget(i, 2, QCheckBox())

    def update_nodes(self):
        selected_nodes = set()
        for i in range(self.log_entry_configuration.table.rowCount()):
            if self.log_entry_configuration.table.cellWidget(i,7).isChecked():
                node_id = str(i + 1)
                node_name = "Node " + str(i + 1)
                node_timestamp = self.log_entry_configuration.table.item(i,2).text()
                node_description = str(i) + 'th' + ' Node flagged'
                log_entry_reference = self.log_entry_configuration.table.item(i,4).text()
                if 'white' in log_entry_reference:
                    log_entry_source = 'white'
                elif 'red' in log_entry_reference:
                    log_entry_source = 'red'
                else:
                    log_entry_source = 'blue'

                event_type = log_entry_source
                if 'white' in log_entry_reference:
                    icon_type = 'white'
                elif 'red' in log_entry_reference:
                    icon_type = 'red'
                else:
                    icon_type = 'blue'
                source = log_entry_reference
                node_visibility = True
                selected_nodes.add(Node(node_id, node_name, node_timestamp, node_description, log_entry_reference,
                                        log_entry_source, event_type, icon_type, source, node_visibility))

        table = self.graph_builder_configuration.window.table
        table.setRowCount(len(selected_nodes))
        for i in range(table.rowCount()):
            node = selected_nodes.pop()
            table.setItem(i,0,QTableWidgetItem(node.get_node_id))
            table.setItem(i, 1, QTableWidgetItem(node.get_node_id))
            table.setItem(i, 2, QTableWidgetItem(node.get_node_name))
            table.setItem(i, 3, QTableWidgetItem(node.get_node_timestamp))
            table.setItem(i, 4, QTableWidgetItem(node.get_node_description))
            table.setItem(i, 5, QTableWidgetItem(node.get_log_entry_reference))
            table.setItem(i, 6, QTableWidgetItem(node.get_source))
            table.setItem(i, 7, QTableWidgetItem(node.get_event_type))
            table.setItem(i, 8, QTableWidgetItem(node.get_icon_type))
            table.setItem(i, 9, QTableWidgetItem(node.get_visibility))

        for i in range(table.rowCount()):
            self.graph_builder_configuration.window.addNode()

    def revert_table(self):
        self.log_entry_configuration.populate_table(self.event_configuration.splunk_client.entries)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Ubuntu')
    window = PMR()
    sys.exit(app.exec())




