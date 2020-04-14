import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
import os
import time
from datetime import datetime, timedelta
from configurations.custom_widgets import CheckableComboBox
from configurations.filter_configuration import FilterConfigurationWindow

"""This class will be used to build the UI Window for the Log Entry Configuration"""


class LogEntryConfigurationWindow(QWidget):
    _log_entry_flagged = pyqtSignal()

    def __init__(self, log_files):
        super().__init__()
        self.setGeometry(200, 400, 800, 620)
        self.setWindowTitle("Log Entry Configuration")
        self.filter = FilterConfigurationWindow()
        self.logs = log_files
        self.UI()

    def UI(self):
        # Creating the label for the window
        self.label = QLabel('Log Entry Configuration', self)
        # Setting the window's font
        self.label.setFont(QFont('MS Shell Dlg 2', 12))
        self.label.move(50, 50)

        # Creating the layout that the window will be stored
        self.layout = QGridLayout(self)

        # Creating the table
        self.table = QTableWidget(self)

        # Setting the amount of columns our table will have
        self.table.setColumnCount(8)
        self.slot_clicks = [1] * self.table.columnCount()
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('icons/up_arrow.png'), "List Number"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Log Entry Timestamp"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Log Entry Content"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Host"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Source"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Source type'))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem('Vector'))
        self.table.setHorizontalHeaderItem(7, QTableWidgetItem(QIcon('icon/unchecked.png'), "Select"))
        self.header = self.table.horizontalHeader()

        for i in range(self.table.columnCount()):
            self.header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        self.table.horizontalHeader().setProperty("showSortIndicator", False)
        self.table.verticalHeader().setProperty("showSortIndicator", False)
        self.header.setStretchLastSection(True)
        self.header.setCascadingSectionResizes(True)

        # Hiding the row labels in the table
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().sectionClicked.connect(self.header_clicked)
        self.widget = QWidget()
        self.layout2 = QHBoxLayout()
        self.layout2.addWidget(self.label)
        self.filter_button = QPushButton('Filter', clicked=self.filter_action)
        self.undo_filter_button = QPushButton('Undo Filter', clicked=self.revert_table)
        self.layout2.addWidget(self.filter_button)
        self.layout2.addWidget(self.undo_filter_button)
        self.widget.setLayout(self.layout2)
        self.layout.addWidget(self.widget)
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)

    def revert_table(self):
        self.table.setRowCount(0)
        self.populate_table(self.entries)

    def populate_table(self, entries):
        self.entries = entries
        self.table.setRowCount(len(entries))
        for i in range(len(entries)):
            # To store non string values in our table cells, we need to create widgets
            # that have a display role formatted for non string values.
            list_value = QTableWidgetItem()
            list_value.setData(Qt.DisplayRole, int(entries[i].get_log_entry_number))
            time_stamp = QTableWidgetItem()
            time_stamp.setData(Qt.DisplayRole, str(datetime.fromtimestamp(int(entries[i].get_log_entry_timestamp))))
            self.table.setItem(i, 0, list_value)
            self.table.setItem(i, 1, time_stamp)
            combobox = CheckableComboBox()

            self.table.setItem(i, 2, QTableWidgetItem(entries[i].get_log_entry_content, Qt.DisplayRole))
            self.table.setItem(i, 3, QTableWidgetItem(entries[i].get_host, Qt.DisplayRole))
            self.table.setItem(i, 4, QTableWidgetItem(entries[i].get_source, Qt.DisplayRole))
            self.table.setItem(i, 5, QTableWidgetItem(entries[i].get_source_type, Qt.DisplayRole))
            self.table.setCellWidget(i, 6, combobox)
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            checkbox.clicked.connect(self.update_graph)
            self.table.setCellWidget(i, 7, checkbox)

    def update_graph(self):
        self._log_entry_flagged.emit()

    def filter_action(self):
        self.filter.show()
        self.filter.closeEvent = self.apply_filter

    def in_source(self, source, entry):
        return any(value in self.find_filepath(entry.get_source) for value in source)

    def in_source_type(self, source_type, entry):
        return any(value in self.find_filepath(entry.get_source_type) for value in source_type)

    def in_keyword(self, keywords, entry):
        return any(value in entry.get_source or entry.get_source_type or entry.get_content for value in keywords)

    def in_timestamp_range(self, start, end, string):
        formatting = '%m/%d/%y %H:%M %p'
        return datetime.strptime(start.strip(), formatting) <= datetime.fromtimestamp(int(string)) <= \
               datetime.strptime(end.strip(), formatting)

    def find_filepath(self, search):
        for file in self.logs:
            if search in file:
                return file

    def apply_filter(self, event):
        criteria = self.filter.filter_criteria
        self.filtered_entries = list()
        keywords = list(criteria['Keywords'])
        creator = list(criteria['Creator'])
        event_type = list(criteria['Event Type'])
        timestamp = criteria['Timestamp']
        filter_source = [entry for entry in self.entries if self.in_source(event_type, entry)]
        filter_creator = [entry for entry in self.entries if self.in_source(creator, entry)]
        valid_timestamps = [entry for entry in self.entries if self.in_timestamp_range(timestamp[0], timestamp[1],
                                                                                       entry.get_log_entry_timestamp)]
        for entry in filter_source:
            self.filtered_entries.append(entry)

        for entry in filter_creator:
            self.filtered_entries.append(entry)

        for entry in valid_timestamps:
            self.filtered_entries.append(entry)

        self.table.setRowCount(0)
        self.populate_table(self.filtered_entries)

    def header_clicked(self):
        if not self.table.rowCount() == 0:
            col = self.table.currentColumn()
            if col == 0:
                items = [int(item.text()) for item in self.table.selectedItems()]
            elif col == 7:
                self.slot_clicks[col] += 1
                if self.slot_clicks[col] % 2 == 0:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/checked.png'))
                    for row in range(self.table.rowCount()):
                        self.table.cellWidget(row, 7).setCheckState(Qt.Checked)
                        self._log_entry_flagged.emit()


                else:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/unchecked.png'))
                    for row in range(self.table.rowCount()):
                        self.table.cellWidget(row, 7).setCheckState(Qt.Unchecked)
            else:
                items = [item.text() for item in self.table.selectedItems()]
            valid_col = col < 6
            if valid_col:
                self.slot_clicks[col] += 1
                if self.slot_clicks[col] % 2 != 0:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/up_arrow.png'))
                    self.table.sortByColumn(col, Qt.AscendingOrder)
                else:
                    self.table.horizontalHeaderItem(col).setIcon(QIcon('icons/down_arrow.png'))
                    self.table.sortByColumn(col, Qt.DescendingOrder)
