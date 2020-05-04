#!/user/bin/python3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, qApp, QMenu, QLineEdit, QTableWidget, \
    QTableWidgetItem, QComboBox, QGroupBox, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QDialog, QFileDialog
from PyQt5.uic import loadUi
import os

from PyQt5.uic.properties import QtCore
from filter_configuration import FilterConfig
import setting_view
from export_configuration import ExportConfig
from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
from QGraphViz.DotParser import Graph, GraphType
from QGraphViz.Engines import Dot
from vector_db_config import VectorDBConfig
from log_file_config import LogFileConfig


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('../ui/MainWindow.ui', self)

        self.FilterConfigButton = self.findChild(QPushButton, 'filterButton')
        self.FilterConfigButton.clicked.connect(self.openFilterConfig)

        self.settingsConfig = self.findChild(QAction, 'actionSettings')
        self.settingsConfig.triggered.connect(self.openSettings)

        #Search button functionality ##need to add keyword search still
        self.searchSearchButton = self.findChild(QPushButton, 'searchSearchButton')
        self.searchSearchButton.clicked.connect(self.openFilterConfig)

        # Enter press on qlineedit search tab triggers the search button
        self.searchLineEdit = self.findChild(QLineEdit, 'lineEdit_2')
        self.searchLineEdit.returnPressed.connect(self.searchSearchButton.click)

        #Search button on graph tab functionality ##need keyword functionality added
        self.graphSearchButton = self.findChild(QPushButton, 'graphSearchButton_2')

        # Enter press on qlineedit graph tab triggers search button
        self.graphSearchEdit = self.findChild(QLineEdit, 'graphLineEdit')
        self.graphSearchEdit.returnPressed.connect(self.graphSearchButton.click)

        #Exit menu option functionality
        self.CloseMenuSelect = self.findChild(QAction, 'actionClose_Exit')
        self.CloseMenuSelect.setShortcut('Ctrl+Q')
        self.CloseMenuSelect.triggered.connect(qApp.quit)

        #Export menu option functionality
        self.exportConfig = self.findChild(QAction, 'actionExport')
        self.exportConfig.setShortcut('Ctrl+E')
        self.exportConfig.triggered.connect(self.openExportConfig)

        #VectorDBConfig linked to menu option
        self.versionControl = self.findChild(QAction, 'actionVersion_Control')
        self.versionControl.setShortcut('Ctrl+S')
        self.versionControl.triggered.connect(self.openVectDBConfig)

        self.actionLogFile = self.findChild(QAction, 'actionFileConfig')
        self.actionLogFile.setShortcut('Ctrl+F')
        self.actionLogFile.triggered.connect(self.openLogConfig)

        self.GraphTable = self.findChild(QTableWidget, 'tableWidget')

        self.graphArea = self.findChild(QWidget, 'graphArea')
        self.graphArea.setLayout(QVBoxLayout())

        self.GraphTable.setItem(0, 0, QTableWidgetItem("Cell (1,1)"))

        # Events
        def node_selected(node):
            if qgv.manipulation_mode == QGraphVizManipulationMode.Node_remove_Mode:
                print("Node {} removed".format(node))
            else:
                print("Node selected {}".format(node))

        def edge_selected(edge):
            if qgv.manipulation_mode == QGraphVizManipulationMode.Edge_remove_Mode:
                print("Edge {} removed".format(edge))
            else:
                print("Edge selected {}".format(edge))

        def node_invoked(node):
            print("Node double clicked")

        def edge_invoked(node):
            print("Edge double clicked")

        def node_removed(node):
            print("Node removed")

        def edge_removed(node):
            print("Edge removed")

        # Create QGraphViz widget
        show_subgraphs = True
        qgv = QGraphViz(
            show_subgraphs=show_subgraphs,

            node_selected_callback=node_selected,
            edge_selected_callback=edge_selected,
            node_invoked_callback=node_invoked,
            edge_invoked_callback=edge_invoked,
            node_removed_callback=node_removed,
            edge_removed_callback=edge_removed,

            hilight_Nodes=True,
            hilight_Edges=True
        )
        qgv.setStyleSheet("background-color:white;")
        # Create A new Graph using Dot layout engine
        qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs))

        # Adding nodes with an image as its shape
        icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\dbicon.png"

        # Build the graph (the layout engine organizes where the nodes and connections are)
        qgv.build()
        # Save it to a file to be loaded by Graphviz if needed
        qgv.save("test.gv")

        # Add the QGraphViz object to the layout
        self.graphArea.layout().addWidget(qgv)

        # Add a horizontal layout (a pannel to select what to do)
        hpanel = QHBoxLayout()
        self.graphArea.layout().addLayout(hpanel)

        # Add few buttons to the panel

        def manipulate():
            qgv.manipulation_mode = QGraphVizManipulationMode.Nodes_Move_Mode

        def save():
            fname = QFileDialog.getSaveFileName(qgv, "Save", "", "*.json")
            if (fname[0] != ""):
                qgv.saveAsJson(fname[0])

        def new():
            qgv.engine.graph = Graph("MainGraph")
            qgv.build()
            qgv.repaint()

        def load():
            fname = QFileDialog.getOpenFileName(qgv, "Open", "", "*.json")
            if (fname[0] != ""):
                qgv.loadAJson(fname[0])

        def add_node():
            dlg = QDialog()
            dlg.ok = False
            dlg.node_name = ""
            dlg.node_label = ""
            dlg.node_type = "None"
            # Layouts
            main_layout = QVBoxLayout()
            l = QFormLayout()
            buttons_layout = QHBoxLayout()

            main_layout.addLayout(l)
            main_layout.addLayout(buttons_layout)
            dlg.setLayout(main_layout)

            leNodeName = QLineEdit()
            leNodeLabel = QLineEdit()
            cbxNodeType = QComboBox()
            leImagePath = QLineEdit()

            pbOK = QPushButton()
            pbCancel = QPushButton()

            cbxNodeType.addItems(["None", "circle", "box"])
            pbOK.setText("&OK")
            pbCancel.setText("&Cancel")

            l.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
            l.setWidget(0, QFormLayout.FieldRole, leNodeName)
            l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
            l.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
            l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Type"))
            l.setWidget(2, QFormLayout.FieldRole, cbxNodeType)
            l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Image"))
            l.setWidget(3, QFormLayout.FieldRole, leImagePath)

            def ok():
                dlg.OK = True
                dlg.node_name = leNodeName.text()
                dlg.node_label = leNodeLabel.text()
                if (leImagePath.text()):
                    dlg.node_type = leImagePath.text()
                else:
                    dlg.node_type = cbxNodeType.currentText()
                dlg.close()

            def cancel():
                dlg.OK = False
                dlg.close()

            pbOK.clicked.connect(ok)
            pbCancel.clicked.connect(cancel)

            buttons_layout.addWidget(pbOK)
            buttons_layout.addWidget(pbCancel)
            dlg.exec_()

            # node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
            if dlg.OK and dlg.node_name != '':
                qgv.addNode(qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_type)
                qgv.build()


        def add_node(node_id, node_name, node_timestamp, node_description, log_entry_reference, log_creator,
                 event_type,icon_type,source,visibility):

           qgv.addNode(qgv.engine.graph,node_name,label=node_description,shape='icons/blue_circle.png')

        def remove_node():
            qgv.manipulation_mode = QGraphVizManipulationMode.Node_remove_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnRemoveNode.setChecked(True)

        def remove_edge():
            qgv.manipulation_mode = QGraphVizManipulationMode.Edge_remove_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnRemoveEdge.setChecked(True)

        def add_edge():
            qgv.manipulation_mode = QGraphVizManipulationMode.Edges_Connect_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnAddEdge.setChecked(True)

        # Add buttons
        btnNew = QPushButton("New")
        btnNew.clicked.connect(new)
        btnOpen = QPushButton("Open")
        btnOpen.clicked.connect(load)

        btnSave = QPushButton("Save")
        btnSave.clicked.connect(save)

        hpanel.addWidget(btnNew)
        hpanel.addWidget(btnOpen)
        hpanel.addWidget(btnSave)

        buttons_list = []
        btnManip = QPushButton("Manipulate")
        btnManip.setCheckable(True)
        btnManip.setChecked(True)
        btnManip.clicked.connect(manipulate)
        hpanel.addWidget(btnManip)
        buttons_list.append(btnManip)

        btnAddNode = QPushButton("Add Node")
        btnAddNode.clicked.connect(add_node)
        hpanel.addWidget(btnAddNode)
        buttons_list.append(btnAddNode)

        btnRemoveNode = QPushButton("Remove Node")
        btnRemoveNode.setCheckable(True)
        btnRemoveNode.clicked.connect(remove_node)
        hpanel.addWidget(btnRemoveNode)
        buttons_list.append(btnRemoveNode)

        btnAddEdge = QPushButton("Add Edge")
        btnAddEdge.setCheckable(True)
        btnAddEdge.clicked.connect(add_edge)
        hpanel.addWidget(btnAddEdge)
        buttons_list.append(btnAddEdge)

        btnRemoveEdge = QPushButton("Remove Edge")
        btnRemoveEdge.setCheckable(True)
        btnRemoveEdge.clicked.connect(remove_edge)
        hpanel.addWidget(btnRemoveEdge)
        buttons_list.append(btnRemoveEdge)


        #drop down menus vector collumn search table
        self.searchSearchTableWidget = self.findChild(QTableWidget, 'tableWidget_2')
        i = 0
        while i < 10:
            combo = QComboBox()
            combo.addItems([' ', '1', '2', '3'])
            self.searchSearchTableWidget.setCellWidget(i, 3, combo)
            i += 1

        self.showMaximized()

    def openLogConfig(self):
        self.window = LogFileConfig()
        self.window.show()

    def openVectDBConfig(self):
        self.window = VectorDBConfig()
        self.window.show()

    def openExportConfig(self):
        self.window = ExportConfig()
        self.window.show()

    def openFilterConfig(self):
        self.window = FilterConfig()
        self.window.show()

    def openSettings(self):
        self.window = setting_view.SettingsWindow()
        self.window.show()


if __name__ == "__main__":
    import sys
    application = QApplication(sys.argv)
    window = MainWindow()
    application.exec_()