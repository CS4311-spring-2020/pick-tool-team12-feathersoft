import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from QGraphViz.DotParser import Graph
from QGraphViz.Engines import Dot
from QGraphViz.QGraphViz import QGraphVizManipulationMode, QGraphViz

from configurations import rwo
from configurations.export_configuration import ExportConfigurationWindow
from configurations.rwo import Node
from QGraphViz.DotParser.Node import Node


class GraphConfigurationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 850, 600)
        self.setWindowTitle("Graph Configuration")
        self.node_indexes = []
        self.UI()

    def UI(self):

        self.window = NodeEditorWindow()
        self.setCentralWidget(self.window)

    def do_nothing(self):
        pass


class NodeEditorWindow(QWidget):
    vectors: dict
    nodes: dict
    relationships: dict
    export_signal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.vectors = {}
        self.nodes = {}
        self.relationships = {}

        self.scene_width = 64000
        self.scene_height = 64000
        self.setMouseTracking(True)
        self.initUI()
        self.export_window = ExportConfigurationWindow()
        self.export_signal.connect(self.export_image)
        self.ok = True
    def initUI(self):
        self.setGeometry(200, 200, 800, 600)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
        # Create graphics scene


        # Creating the tablular view
        self.table = QTableWidget(0, 10, self)
        # self.table.setFixedWidth(850)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node ID"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node Name"))
        self.table.setHorizontalHeaderItem(2, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node Timestamp"))
        self.table.setHorizontalHeaderItem(3, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Node Description"))
        self.table.setHorizontalHeaderItem(4, QTableWidgetItem(QIcon('icons/up_arrow.png'), "Log Entry Reference"))
        self.table.setHorizontalHeaderItem(5, QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Log Creator'))
        self.table.setHorizontalHeaderItem(6, QTableWidgetItem('Event Type'))
        self.table.setHorizontalHeaderItem(7, QTableWidgetItem(QIcon('icon/unchecked.png'), "Icon Type"))
        self.table.setHorizontalHeaderItem(8, QTableWidgetItem(QIcon('icons/up_arrow.png'), 'Source'))
        self.table.setHorizontalHeaderItem(9, QTableWidgetItem('Node Visibility'))
        self.header = self.table.horizontalHeader()
        for i in range(self.table.columnCount()):
            self.header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        # Creating the Graphical View
        self.layout.addWidget(self.table, 1)
        self.setWindowTitle('Node Editor')


        # Events
        def node_selected(node):
            if self.qgv.manipulation_mode == QGraphVizManipulationMode.Node_remove_Mode:
                print("Node {} removed".format(node))
            if self.qgv.manipulation_mode == QGraphVizManipulationMode.Nodes_Move_Mode:
                pass
            else:
                print("Node selected {}".format(node))

        def edge_selected(edge):
            if self.qgv.manipulation_mode == QGraphVizManipulationMode.Edge_remove_Mode:
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
        self.qgv = QGraphViz(
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
        self.qgv.setStyleSheet("background-color:white;")
        # Create A new Graph using Dot layout engine
        self.qgv.new(Dot(Graph("Main_Graph"), show_subgraphs=show_subgraphs))

        # Adding nodes with an image as its shape
        icon_path = os.path.dirname(os.path.abspath(__file__)) + r"\dbicon.png"

        # Build the graph (the layout engine organizes where the nodes and connections are)
        self.qgv.build()
        # Save it to a file to be loaded by Graphviz if needed
        self.qgv.save("test.gv")




        self.graphArea = QWidget()

        # Add the QGraphViz object to the layout
        self.graphArea.setLayout(QVBoxLayout())
        self.graphArea.layout().addWidget(self.qgv)

        # Add a horizontal layout (a pannel to select what to do)
        hpanel = QHBoxLayout()
        self.graphArea.layout().addLayout(hpanel)
        self.layout.addWidget(self.graphArea)

        # Add few buttons to the panel

        def manipulate():
            self.qgv.manipulation_mode = QGraphVizManipulationMode.Nodes_Move_Mode

        def save():
            fname = QFileDialog.getSaveFileName(self.qgv, "Save", "", "*.json")
            if (fname[0] != ""):
                self.qgv.saveAsJson(fname[0])

        def new():
            self.qgv.engine.graph = Graph("MainGraph")
            self.qgv.build()
            self.qgv.repaint()

        def load():
            fname = QFileDialog.getOpenFileName(self.qgv, "Open", "", "*.json")
            if (fname[0] != ""):
                self.qgv.loadAJson(fname[0])

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
            self.leImagePath = QLineEdit()
            leImageBtn = QPushButton(clicked=self.open_file, icon=QIcon('icons/folder.png'))

            pbOK = QPushButton()
            pbCancel = QPushButton()

            cbxNodeType.addItems(["Red Node", "Blue Node", "White Node"])
            pbOK.setText("&OK")
            pbCancel.setText("&Cancel")

            l.setWidget(0, QFormLayout.LabelRole, QLabel("Node Name"))
            l.setWidget(0, QFormLayout.FieldRole, leNodeName)
            l.setWidget(1, QFormLayout.LabelRole, QLabel("Node Label"))
            l.setWidget(1, QFormLayout.FieldRole, leNodeLabel)
            l.setWidget(2, QFormLayout.LabelRole, QLabel("Node Type"))
            l.setWidget(2, QFormLayout.FieldRole, cbxNodeType)
            l.setWidget(3, QFormLayout.LabelRole, QLabel("Node Image"))
            l.setWidget(3, QFormLayout.FieldRole, self.leImagePath)
            l.addWidget(leImageBtn)

            def ok():
                dlg.OK = True
                dlg.node_name = leNodeName.text()
                dlg.node_label = leNodeLabel.text()
                if self.leImagePath.text():
                    dlg.node_type = self.leImagePath.text()
                else:
                    if 'Red Node' in cbxNodeType.currentText():
                        dlg.node_type = 'icons/red_circle.png'
                    if 'Blue Node' in cbxNodeType.currentText():
                        dlg.node_type = 'icons/blue_circle.png'
                    if 'White Node' in cbxNodeType.currentText():
                        dlg.node_type = 'icons/white_circle.png'

                dlg.close()

            def cancel():
                self.ok = False
                dlg.close()

            pbOK.clicked.connect(ok)
            pbCancel.clicked.connect(cancel)

            buttons_layout.addWidget(pbOK)
            buttons_layout.addWidget(pbCancel)
            dlg.exec_()

            # node_name, okPressed = QInputDialog.getText(wi, "Node name","Node name:", QLineEdit.Normal, "")
            if self.ok and dlg.node_name != '':
                self.qgv.addNode(self.qgv.engine.graph, dlg.node_name, label=dlg.node_label, shape=dlg.node_type)
                self.qgv.build()


        def remove_node():
            self.qgv.manipulation_mode = QGraphVizManipulationMode.Node_remove_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnRemoveNode.setChecked(True)

        def remove_edge():
            self.qgv.manipulation_mode = QGraphVizManipulationMode.Edge_remove_Mode
            for btn in buttons_list:
                btn.setChecked(False)
            btnRemoveEdge.setChecked(True)

        def add_edge():
            self.qgv.manipulation_mode = QGraphVizManipulationMode.Edges_Connect_Mode
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

        btnExport = QPushButton("Export Graph")
        btnExport.clicked.connect(self.export_action)
        hpanel.addWidget(btnExport)
        buttons_list.append(btnExport)

        self.setWindowTitle('Graph View')
        self.setLayout(self.layout)

        # self.addDebugContent()

    def add_node_param(self,node_id, node_name, node_timestamp, node_description, log_entry_reference,
                       log_entry_source, event_type, icon_type, source, node_visibility):
        n = rwo.Node(node_id, node_name, node_timestamp, node_description, log_entry_reference,
                 log_entry_source, event_type, icon_type, source, node_visibility)
        img = ''
        if 'blue' in event_type:
            img = 'icons/blue_circle.png'

        if 'red' in event_type:
            img = 'icons/red_circle.png'

        if 'white' in event_type:
            img = 'icons/white_circle.png'

        self.qgv.addNode(self.qgv.engine.graph, node_name, label=node_timestamp, shape=img)
        self.qgv.build()



    def export_action(self):
        self.export_window.show()
        self.export_window.closeEvent = self.export_image

    def export_image(self,event):
        print(self.export_window.file_name,self.export_window.extension)
        if self.export_window.file_name == '' or self.export_window.extension == '':
            QMessageBox.critical(self,"Empty", 'Enter values for both the filename and extension fields')
        else:
            self.qgv.core.grab().save(self.export_window.file_name + '.' + self.export_window.extension,
                                      self.export_window.extension)
            QMessageBox.information(self,'Success', 'File Successfully Exported!!!!')


    def addEdge(self):
        pass

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button == Qt.RightButton:
            self.contextMenuEvent(QMouseEvent)

    def open_file(self):
        """
            This method opens a file dialog and allows a user to select the directory containing the files
            they want to ingest.
            :return:
        """
        # Open the file selection dialog
        file, options = QFileDialog.getOpenFileName(QFileDialog())
        self.leImagePath.setText(str(file))






if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = GraphConfigurationWindow()
    sys.exit(App.exec())

