# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerLrqTVY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *


class LogFileConfigWindow(QWidget):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(435, 325)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.tableWidget_2 = QTableWidget(Form)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget_2.rowCount() < 3):
            self.tableWidget_2.setRowCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem10)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setSortingEnabled(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidget_2, 1, 0, 1, 4)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 2)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 2, 1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"File Name: ", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Line Number 	\u25bc", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Error Message \u25bc", None));

        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"10", None));
        ___qtablewidgetitem3 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Invalid Format", None));
        ___qtablewidgetitem4 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"55", None));
        ___qtablewidgetitem5 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Invalid Character", None));
        ___qtablewidgetitem6 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"93", None));
        ___qtablewidgetitem7 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Missing Space", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("Form", u"Log File 1.txt", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Validate", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancel", None))
    # retranslateUi


class Ui_MainWindow(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(700, 350)
        Form.setMinimumSize(QSize(700, 350))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75);
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 6):
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
        if (self.tableWidget.rowCount() < 5):
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
        self.tableWidget.setMinimumSize(QSize(680, 55))
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Log File Configuration", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"File Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Source", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Cleansing Status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Validation Status", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Ingestion Status", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"View Enforcement Action Report", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Log File 1.txt", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"users/fakepath", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Cleansed", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Validated", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Ingested", None));
        ___qtablewidgetitem11 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Log File 2.txt", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"users/fakepath", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Cleansed", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Validated", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Ingested", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"Log File 3.txt", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"users/fakepath", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Cleansed", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"Validated", None));
        ___qtablewidgetitem20 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"Ingested", None));
        ___qtablewidgetitem21 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Log File 4.txt", None));
        ___qtablewidgetitem22 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"users/fakepath", None));
        ___qtablewidgetitem23 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"In Progress", None));
        ___qtablewidgetitem24 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"Error Found", None));
        ___qtablewidgetitem25 = self.tableWidget.item(3, 4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"Not Ingested", None));
        ___qtablewidgetitem26 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Form", u"Log File 5.txt", None));
        ___qtablewidgetitem27 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Form", u"users/fakepath", None));
        ___qtablewidgetitem28 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Form", u"Cleansed", None));
        ___qtablewidgetitem29 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Form", u"Error Found", None));
        ___qtablewidgetitem30 = self.tableWidget.item(4, 4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Form", u"Not Ingested", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        # Enforcement Report Column
        enforcement = [1]
        for i in range(5):
            enforcement.append(i)
            enforcement[i] = self.tableWidget.item(i, 5)
            enforcement[i] = QPushButton(self.tableWidget, u"View")
            enforcement[i].setText("View")
            enforcement[i].clicked.connect(self.window2)
            self.tableWidget.setCellWidget(i, 5, enforcement[i])

    # retranslateUi

    def window2(self):
        self.w = LogFileConfigWindow()
        ui = LogFileConfigWindow()
        ui.setupUi(self.w)
        self.w.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())