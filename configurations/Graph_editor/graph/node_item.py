from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import *
from PyQt5.Qt import QGraphicsLineItem

from configurations.Graph_editor.graph.relationship_item import RelationshipItem
from configurations.rwo import node, Node
from configurations.rwo import node_visibility
from configurations.Graph_editor.graph.graph_editor_scene import GraphEditorScene


class NodeItem(QGraphicsItem):
    '''
        NodeItem is a graphical item class that draws nodes and hold node information and relationships

        Attributes
        ----------
        width : float
            width of node
        height : float
            height of node
        relationship : dict
            RelationshipItem that links one node to another
    '''
    width: float = 100.0
    height: float = 100.0
    relationships = {}

    def __init__(self, pos_x: float, post_y: float, name: str, type: str, scene, parent=None):
        super().__init__(parent)
        self.pos_x = pos_x
        self.pos_y = post_y
        self.name = name
        self.type = type
        self.isSelected = False
        self.num_clicks = 1
        self.init_ui()
        self.node = Node('', '', '', '', '', '', '', '', '', '')
        self.scene = scene

    def init_ui(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setAcceptHoverEvents(True)
        self.setAcceptDrops(True)

    '''
        Returns the center position of a node
    '''

    def center_pos(self):
        return self.boundingRect().center()

    '''
        Add a relationship to the node
        
        Parameters
        ----------
        key : str
            unique identifier for the relationship
        relationship : RelationshipItem
            graphics object that connects to this node       
    '''

    def add_relationship(self, key: str, relationship):
        self.relationships[key] = relationship

    '''
        Defines QRect bounding rectangle which contains this node
        
        Return
        ------
        QRectF
            bounding rectangle for this node
    '''

    def boundingRect(self) -> QRectF:
        return QRectF(self.pos_x, self.pos_y, self.width, self.height).normalized()

    '''
        This funtion which is usually called by QGraphicsView, paints the contents of an item in local coordinates.
        
        Parameters
        ----------    
        painter: QPainter
            Class that handles painter the item on the scene
        style: QStyleOptionGraphicsItem
            Style options used on this item, usually defaulted
        widget : QWidget
            Widget to paint this item on
    '''

    def paint(self, painter: QPainter, style: QStyleOptionGraphicsItem, widget=None):
        node_outline = QPainterPath()
        node_outline.addEllipse(self.pos_x, self.pos_y, self.width, self.height)
        pen = QPen(Qt.black if not self.isSelected else Qt.yellow)
        pen.setWidth(3)
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.red))
        painter.drawPath(node_outline.simplified())

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent') -> None:
        if self.node:
            self.setToolTip(f"Node ID: {self.node._node_id}\n"
                            f"Node Name: {self.node._node_name}\n"
                            f"Node Timestamp: {self.node._node_timestamp}\n"
                            f"Node Description: {self.node._node_description}\n"
                            f"Log Entry Reference: {self.node._log_entry_reference}\n"
                            f"Log Creator: {self.node._log_creator}\n"
                            f"Event Type: {self.node._event_type}\n"
                            f"Icon Type: {self.node._icon_type}\n"
                            f"Source: {self.node._source}\n"
                            f"Visibility: ALL")


    def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        self.num_clicks += 1
        if self.num_clicks % 2 == 0:
            self.isSelected = True
            self.start = event.pos()
            self.parent = self.scene.itemAt(self.mapToScene(self.start), QTransform())

        else:
            self.isSelected = False

        self.update()

    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        if self.isSelected:
            self.end = event.pos()
            self.child = self.scene.itemAt(self.mapToScene(self.end), QTransform())
            self.add_relationships(self.parent, self.child)

    def set_node_properties(self, node_id, node_name, node_timestamp, node_description, log_entry_reference,
                            log_creator,
                            event_type, icon_type, source, visibility):

        self.node = Node(node_id, node_name, node_timestamp, node_description, log_entry_reference, log_creator,
                         event_type, icon_type, source, visibility)

    def add_relationships(self, parent_node, child_node):
            relationship = RelationshipItem("Parent", "Child",
                                            parent_node.center_pos(), child_node.center_pos(), parent_node)
            self.scene.addItem(relationship)
