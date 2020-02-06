# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerYOubjO.ui'
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

class VectorConfigurationWindow(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(482, 432)
        print(type(Form))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vectorConfigLabel = QLabel(Form)
        self.vectorConfigLabel.setObjectName(u"vectorConfigLabel")
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75);
        self.vectorConfigLabel.setFont(font)

        self.gridLayout.addWidget(self.vectorConfigLabel, 0, 0, 1, 2)

        self.editButton = QPushButton(Form)
        self.editButton.setObjectName(u"editButton")

        self.gridLayout.addWidget(self.editButton, 7, 0, 1, 1)

        self.addVectorButton = QPushButton(Form)
        self.addVectorButton.setObjectName(u"addVectorButton")

        self.gridLayout.addWidget(self.addVectorButton, 7, 1, 1, 1)

        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem11)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 6, 4)
        self.deleteButton = QPushButton(Form)
        self.deleteButton.setObjectName(u"deleteButton")

        self.gridLayout.addWidget(self.deleteButton, 7, 2, 1, 2)

        self.verticalScrollBar = QScrollBar(Form)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout.addWidget(self.verticalScrollBar, 1, 4, 6, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.vectorConfigLabel.setText(QCoreApplication.translate("Form", u"Vector Configuration", None))
        self.editButton.setText(QCoreApplication.translate("Form", u"Edit Vector", None))
        self.addVectorButton.setText(QCoreApplication.translate("Form", u"Add Vector", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Vector Name 	\u25bc", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Description 	\u25bc", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Select", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Vector 1", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Vector 2", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Vector 3", None));

        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem6 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"DoS Attack", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Denial of Service", None));
        ___qtablewidgetitem8 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"MitM", None));
        ___qtablewidgetitem9 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Man in the middle", None));
        ___qtablewidgetitem10 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"SQL Injection", None));
        ___qtablewidgetitem11 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"SQL Injection", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.deleteButton.setText(QCoreApplication.translate("Form", u"Delete Vector", None))
    # retranslateUi


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = VectorConfigurationWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())


