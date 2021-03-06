import QGraphViz
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from pymongo.errors import ConfigurationError

from configurations import rwo
from configurations.log_entry_configuration import LogEntryConfigurationWindow
from configurations.event_configuration import EventConfigurationWindow
from configurations.log_file_configuration import LogFileConfigurationWindow
from configurations.relationship_configuration import RelationshipConfigurationWindow
from configurations.rwo import NodeVisibility
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
import socket
import datetime
from datetime import datetime
from pymongo import MongoClient
from QGraphViz.DotParser import *
from QGraphViz.DotParser.Node import Node


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
        self.file_menu.addAction('Save',self.save)
        self.file_menu.addAction('Quit', self.close)


        self.approval_db_credentials = open('auth/db_approve_auth').readline().rstrip().split(' ')
        self.commit_db_credentials = open('auth/db_commit_auth').readline().rstrip().split(' ')

        self.event_configuration_obj = None

        self.disable_toolbar()

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

        # Update lead table
        self.vector_db_configuration_non_lead._push_signal.connect(self.update_lead_db)

        # Revalidate files
        self.log_file_configuration.revalidate_file.connect(self.revalidate_files)

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
        self.event_configuration_obj = self.event_configuration.event_configuration
        self.log_entry_configuration.populate_table(self.event_configuration.splunk_client.entries,
                                                    self.event_configuration_obj)

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
            if self.vector_configuration.table.cellWidget(i, 2).isChecked():
                name, desc = self.vector_configuration.table.item(i, 0), self.vector_configuration.table.item(i, 1)
                if name is not None and desc is not None:
                    selected_vectors.add(Vector(name.text(), desc.text()))

        self.vector_db_configuration_non_lead.table.setRowCount(len(selected_vectors))
        for i in range(len(selected_vectors)):
            vec = selected_vectors.pop()
            self.vector_db_configuration_non_lead.table.setItem(i, 0, QTableWidgetItem(vec.get_vector_name))
            self.vector_db_configuration_non_lead.table.setItem(i, 1, QTableWidgetItem(vec.get_vector_description))
            self.vector_db_configuration_non_lead.table.setCellWidget(i, 2, QCheckBox())

    def update_nodes(self):
        selected_nodes = set()
        node_item = None
        node_properties = None
        for i in range(self.log_entry_configuration.table.rowCount()):
            if self.log_entry_configuration.table.cellWidget(i, 7).isChecked():
                node_id = str(i + 1)
                node_name = "Node " + str(i + 1)
                node_timestamp = self.log_entry_configuration.table.item(i, 1).text()
                node_description = self.log_entry_configuration.table.item(i,2)
                log_entry_reference = self.log_entry_configuration.table.item(i, 4).text()
                log_entry_source = self.log_entry_configuration.table.item(i,5).text()

                event_type = log_entry_source
                if 'white' in log_entry_reference:
                    icon_type = 'white'
                elif 'red' in log_entry_reference:
                    icon_type = 'red'
                else:
                    icon_type = 'blue'
                source = log_entry_reference
                node_visibility = NodeVisibility(True, True, True, True, True, True, True, True, True, True)
                selected_nodes.add(rwo.Node(node_id, node_name, node_timestamp, node_description, log_entry_reference,
                                            log_entry_source, event_type, icon_type, source, node_visibility))

        table = self.graph_builder_configuration.window.table
        table.setRowCount(len(selected_nodes))


        for i in range(table.rowCount()):
            node = selected_nodes.pop()
            table.setItem(i, 0, QTableWidgetItem(node.get_node_id))
            table.setItem(i, 1, QTableWidgetItem(node.get_node_name))
            table.setItem(i, 2, QTableWidgetItem(node.get_node_timestamp))
            table.setItem(i, 3, QTableWidgetItem(node.get_node_description))
            table.setItem(i, 4, QTableWidgetItem(node.get_log_entry_reference))
            table.setItem(i, 5, QTableWidgetItem(node.get_source))
            table.setItem(i, 6, QTableWidgetItem(node.get_event_type))
            table.setItem(i, 7, QTableWidgetItem(node._icon_type))
            table.setItem(i, 8, QTableWidgetItem(node.get_source))
            node_visibility = CheckableComboBox()
            node_visibility.addItems(['node_visibility', 'node_id_visibility', 'node_name_visibility'
                                                                               'node_timestamp_visibility',
                                      'node_description_visibility',
                                      'log_entry_reference_visibility', 'log_creator_visibility',
                                      'event_type_visibility', 'icon_type_visibility', 'source_visibility'])
            table.setCellWidget(i, 9, node_visibility)


            if node.get_node_name not in self.graph_builder_configuration.window.graph_nodes:
                    self.graph_builder_configuration.window.add_node_param(
                                                                           node.get_node_name,
                                                                           node.get_node_timestamp,
                                                                           node.get_event_type

                                                                          )


    def revert_table(self):
        self.log_entry_configuration.populate_table(self.event_configuration.splunk_client.entries)

    def connect(self):
        try:
            self.cluster = \
                MongoClient(self.commit_db_credentials[0])

        # Defining our DB
        except ConnectionError:
            QMessageBox.critical(self, 'Connection Error', 'A connection could not be established at this time')
        except ConfigurationError:
            QMessageBox.critical(self, 'Configuration Error', 'Connection timeout after 20 seconds'
                                                              'Please be sure that your mongodb server is running')

    def update_lead_db(self):
        selected_vectors = set()
        for i in range(self.vector_db_configuration_non_lead.table.rowCount()):
            if self.vector_db_configuration_non_lead.table.cellWidget(i, 2).isChecked():
                name, desc, graph = self.vector_db_configuration_non_lead.table.item(i, 0), \
                                    self.vector_db_configuration_non_lead.table.item(i, 1), \
                                    self.vector_db_configuration_non_lead.table.item(i, 3)

                if name and desc and graph:
                    selected_vectors.add((name.text(), desc.text(), graph.text()))

        for i in range(len(selected_vectors)):
            name, desc, graph = selected_vectors.pop()
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            dateTimeObj = datetime.now()
            timestampStr = dateTimeObj.strftime('%m/%d/%y %H:%M %p')
            entry = {"_ip_address": ip_address, "_time_stamp": timestampStr, "_name": name, "_desc": desc,
                     "_commit": "Selected",
                     "_graph": graph, "_status": "pending"}
            self.connect()
            self.db = self.cluster[self.commit_db_credentials[1]]
            self.collection = self.db[self.commit_db_credentials[2]]
            self.collection.insert_one(entry)

    def revalidate_files(self):
        self.event_configuration.splunk_client.cleanse_file(
            self.log_file_configuration.table.item(self.log_file_configuration.index, 1).text())
        self.event_configuration.splunk_client.validate_file(
            self.log_file_configuration.table.item(self.log_file_configuration.index, 1).text(),
            self.event_configuration.start_date.text(),
            self.event_configuration.end_date.text())

    def save(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Ubuntu')
    window = PMR()
    sys.exit(app.exec())
