# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogFileConfigympruX.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        self.label.move(201,31)
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75);
        self.label.setFont(font)
        self.tableWidget = QTableWidget(self.centralwidget)
        if self.tableWidget.columnCount() < 6:
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if self.tableWidget.rowCount() < 5:
            self.tableWidget.setRowCount(5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(0, 5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(3, 4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(4, 4, __qtablewidgetitem36)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 80, 611, 171))
        self.tableWidget_2 = QTableWidget(self.centralwidget)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem47)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(320, 320, 211, 111))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 300, 81, 16))
        font1 = QFont()
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 300, 91, 16))
        self.label_3.setFont(font1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(310, 440, 112, 32))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(420, 440, 112, 32))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(560, 100, 71, 31))
        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(560, 130, 71, 31))
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(560, 160, 71, 31))
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(560, 190, 71, 31))
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(560, 220, 71, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Log File Configuration", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"File Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Cleansing Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Validation Status", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ingestion Status", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"View Enforcement Action Report", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Log File 1.txt", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"users/fakepath", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Cleansed", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Validated", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Ingested", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Log File 2.txt", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"users/fakepath", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Cleansed", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Validated", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Ingested", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Log File 3.txt", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"users/fakepath", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Cleansed", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Validated", None));
        ___qtablewidgetitem20 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Ingested", None));
        ___qtablewidgetitem21 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Log File 4.txt", None));
        ___qtablewidgetitem22 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"users/fakepath", None));
        ___qtablewidgetitem23 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"In Progress", None));
        ___qtablewidgetitem24 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Error Found", None));
        ___qtablewidgetitem25 = self.tableWidget.item(3, 4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Not Ingested", None));
        ___qtablewidgetitem26 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Log File 5.txt", None));
        ___qtablewidgetitem27 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"users/fakepath", None));
        ___qtablewidgetitem28 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Cleansed", None));
        ___qtablewidgetitem29 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Error Found", None));
        ___qtablewidgetitem30 = self.tableWidget.item(4, 4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Not Ingested", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem31 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Line Number 	\u25bc", None));
        ___qtablewidgetitem32 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Error Message \u25bc", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem33 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem34 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Invalid Format", None));
        ___qtablewidgetitem35 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"55", None));
        ___qtablewidgetitem36 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Invalid Character", None));
        ___qtablewidgetitem37 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"93", None));
        ___qtablewidgetitem38 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Missing Space", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"File Name: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Log File 1.txt", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Validate", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"View", None))

        header = self.tableWidget.horizontalHeader()
        for i in range(header.count()):
            header.setSectionResizeMode(i,QHeaderView.ResizeToContents)

    # retranslateUi

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())