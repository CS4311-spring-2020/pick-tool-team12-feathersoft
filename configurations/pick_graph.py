
from PyQt5.QtWidgets import QFileDialog, QDialog, QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, \
    QFormLayout, QComboBox, QPushButton, QInputDialog, QLineEdit, QLabel
import sys
import os

sys.path.insert(1, os.path.dirname(__file__) + "/..")
print(sys.path)
from QGraphViz.QGraphViz import QGraphViz, QGraphVizManipulationMode
from QGraphViz.DotParser import Graph, GraphType
from QGraphViz.Engines import Dot


if __name__ == '__main__':
     import pygraphviz as pgv
     G = pgv.AGraph()
     G.add_node('a')
     G.add_edge('b', 'c')
