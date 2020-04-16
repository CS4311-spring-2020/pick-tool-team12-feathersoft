from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel
from configurations.node_socket import *

MODE_NO_OPERATION = 1
MODE_EDGE_DRAG = 2

EDGE_DRAG_START = 10

class QDMGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self.grScene = scene

        self.initUI()

        self.setScene(self.grScene)

        self.mode = MODE_NO_OPERATION

        self.zoomInFactor = 1.25
        self.zoomClamp = False
        self.zoom = 10
        self.zoomStep = 1
        self.zoomRange = [0, 10]
        self.setMouseTracking(True)

    def initUI(self):
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        #self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.Key_TouchpadOn:
            self.middleMouseButtonPress(QMouseEvent)
        else:
            super().mousePressEvent(QMouseEvent)

    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.MiddleButton:
            self.middleMouseButtonRelease(QMouseEvent)
        else:
            super().mouseReleaseEvent(QMouseEvent)


    def middleMouseButtonPress(self,event):
        item = self.getItemAtClick(event)

        self.last_click_scene_pos = self.mapToScene(event.pos())
        if type(item) is QDMGraphicsSocket:
            if self.mode == MODE_NO_OPERATION:
                self.mode = MODE_EDGE_DRAG
                self.edgeDragStart(item)
                return


        if self.mode == MODE_EDGE_DRAG:
            res = self.edgeDragEnd(item)
            if res:
                return

        super().mousePressEvent(event)


    def distanceBetweenClickAndReleaseOff(self,event):
        new_pos_release_scene_pos = self.mapToScene(event.pos())
        dist_scene_pos = self.last_click_scene_pos

        return (dist_scene_pos.x() * dist_scene_pos.x() + dist_scene_pos.y() * dist_scene_pos.y()) > EDGE_DRAG_START * EDGE_DRAG_START

    def middleMouseButtonReleased(self, event):

        item = self.getItemAtClick(event)

        if self.mode == MODE_EDGE_DRAG:
            if self.distanceBetweenClickAndReleaseOff(event):
                res = self.edgeDragEnd(item)
                if res:
                    return


        super().mouseReleaseEvent(event)

    def getItemAtClick(self, event):
        pos = event.pos()
        obj = self.itemAt(pos)
        return obj

    def edgeDragEnd(self,item):
        self.mode = MODE_NO_OPERATION
        if type(item) is QDMGraphicsSocket:
            return True

        return False

    def edgeDragStart(self,item):
        pass



    # Adding the zoom functionality

    def wheelEvent(self, QWheelEvent):
        # Calculate our zoom factor

        zoomOutFactor = 1 / self.zoomInFactor



        # calculate the zoom
        if QWheelEvent.angleDelta().y() > 0:
            zoomFactor = self.zoomInFactor
            self.zoom += self.zoomStep

        else:
            zoomFactor = zoomOutFactor
            self.zoom -= self.zoomStep


        clamped = False
        if self.zoom < self.zoomRange[0] : self.zoom, clamped = self.zoomRange[0], True
        if self.zoom > self.zoomRange[1] : self.zoom, clamped = self.zoomRange[1], False

        # Set Scene scale
        if not clamped or self.zoomClamp is False:
            self.scale(zoomFactor, zoomFactor)
    #
    # def mouseMoveEvent(self, event):
    #     self.grScene.x = event.x()
    #     self.grScene.y = event.y()
    #
    #     print(event.x(), event.y())





