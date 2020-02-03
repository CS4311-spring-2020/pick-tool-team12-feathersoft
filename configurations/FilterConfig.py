# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FilterConfigjYfehu.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import PySide2
from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide2.QtGui import (QFont)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 171, 31))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75);
        self.label.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(230, 20, 241, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 58, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 90, 71, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 120, 111, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 150, 111, 16))
        self.dateTimeEdit = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(140, 120, 194, 22))
        self.dateTimeEdit_2 = QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")
        self.dateTimeEdit_2.setGeometry(QRect(140, 150, 194, 22))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(110, 90, 100, 20))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(220, 90, 100, 20))
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(340, 90, 100, 20))
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(220, 60, 100, 20))
        self.radioButton_5 = QRadioButton(self.centralwidget)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(110, 60, 100, 20))
        self.radioButton_6 = QRadioButton(self.centralwidget)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(340, 60, 100, 20))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 200, 112, 32))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Filter Configuration", None))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Keyword Search", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Creator:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Event Type: ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Timestamp:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"End Timestamp:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"White", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"White", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply Filter", None))
    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())