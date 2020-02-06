# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teamConfiguration.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


class TeamConfigurationWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.move(100, 10)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(10, 280, 381, 41))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 220, 101, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 350, 261, 81))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 120, 261, 51))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 200, 261, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 101, 16))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Team Configuration"))
        self.checkBox.setText(_translate("MainWindow", "Lead"))
        self.label_2.setText(_translate("MainWindow", "Lead IP address"))
        self.label_3.setText(_translate("MainWindow", "No. of established "))
        self.pushButton.setText(_translate("MainWindow", "Conect"))
        self.label_4.setText(_translate("MainWindow", "connections to the"))
        self.label_5.setText(_translate("MainWindow", "Lead\'s IP address"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = TeamConfigurationWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
