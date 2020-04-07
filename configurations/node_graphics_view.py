from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel


class QDMGraphicsView(QGraphicsView):
    def __init__(self, scene, parent=None):
        super().__init__(parent)
        self.grScene = scene

        self.initUI()

        self.setScene(self.grScene)

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
        releaseEvent = QMouseEvent(QEvent.MouseButtonRelease, event.localPos(), event.screenPos())

        self.setDragMode(QGraphicsView)

    def middleMouseButtonReleased(self, event):
        print("MMB released")


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





