# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'FilterConfiggqdfbA.ui'
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


class FilterConfigurationWindow(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(468, 459)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")

        self.startTimestampEdit = QDateTimeEdit(Form)
        self.startTimestampEdit.setObjectName(u"startTimestampEdit")
        self.gridLayout.addWidget(self.startTimestampEdit, 10, 1, 1, 1)

        self.blueButton2 = QRadioButton(Form)
        self.blueButton2.setObjectName(u"blueButton2")
        self.blueButton2.setAutoExclusive(False)
        self.gridLayout.addWidget(self.blueButton2, 7, 1, 1, 1)

        self.redButton1 = QRadioButton(Form)
        self.redButton1.setObjectName(u"redButton1")
        self.redButton1.setAutoExclusive(False)
        self.gridLayout.addWidget(self.redButton1, 3, 1, 1, 1)

        self.startTimestampLabel = QLabel(Form)
        self.startTimestampLabel.setObjectName(u"startTimestampLabel")
        font = QFont()
        font.setPointSize(16)
        self.startTimestampLabel.setFont(font)
        self.gridLayout.addWidget(self.startTimestampLabel, 10, 0, 1, 1)

        self.blueButton1 = QRadioButton(Form)
        self.blueButton1.setObjectName(u"blueButton1")
        self.blueButton1.setAutoExclusive(False)
        self.gridLayout.addWidget(self.blueButton1, 4, 1, 1, 1)

        self.endTimestampLabel = QLabel(Form)
        self.endTimestampLabel.setObjectName(u"endTimestampLabel")
        self.endTimestampLabel.setFont(font)
        self.gridLayout.addWidget(self.endTimestampLabel, 12, 0, 1, 1)

        self.applyButton = QPushButton(Form)
        self.applyButton.setObjectName(u"applyButton")
        self.gridLayout.addWidget(self.applyButton, 13, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.filterConfigurationLabel = QLabel(Form)
        self.filterConfigurationLabel.setObjectName(u"filterConfigurationLabel")
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        font1.setWeight(75);
        self.filterConfigurationLabel.setFont(font1)
        self.gridLayout.addWidget(self.filterConfigurationLabel, 0, 0, 1, 1)

        self.whiteButton2 = QRadioButton(Form)
        self.whiteButton2.setObjectName(u"whiteButton2")
        self.whiteButton2.setAutoExclusive(False)
        self.gridLayout.addWidget(self.whiteButton2, 8, 1, 1, 1)

        self.redButton2 = QRadioButton(Form)
        self.redButton2.setObjectName(u"redButton2")
        self.redButton2.setAutoExclusive(False)
        self.gridLayout.addWidget(self.redButton2, 6, 1, 1, 1)

        self.whiteButton1 = QRadioButton(Form)
        self.whiteButton1.setObjectName(u"whiteButton1")
        self.whiteButton1.setAutoExclusive(False)
        self.gridLayout.addWidget(self.whiteButton1, 5, 1, 1, 1)

        self.endTimestampEdit = QDateTimeEdit(Form)
        self.endTimestampEdit.setObjectName(u"endTimestampEdit")
        self.gridLayout.addWidget(self.endTimestampEdit, 12, 1, 1, 1)

        self.eventTypeLabel = QLabel(Form)
        self.eventTypeLabel.setObjectName(u"eventTypeLabel")
        self.eventTypeLabel.setFont(font)
        self.gridLayout.addWidget(self.eventTypeLabel, 6, 0, 1, 1)

        self.creatorLabel = QLabel(Form)
        self.creatorLabel.setObjectName(u"creatorLabel")
        self.creatorLabel.setFont(font)
        self.gridLayout.addWidget(self.creatorLabel, 3, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.blueButton2.setText(QCoreApplication.translate("Form", u"Blue", None))
        self.redButton1.setText(QCoreApplication.translate("Form", u"Red", None))
        self.startTimestampLabel.setText(QCoreApplication.translate("Form", u"Start Timestamp:", None))
        self.blueButton1.setText(QCoreApplication.translate("Form", u"Blue", None))
        self.endTimestampLabel.setText(QCoreApplication.translate("Form", u"End Timestamp:", None))
        self.applyButton.setText(QCoreApplication.translate("Form", u"Apply Filter", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Keyword Search", None))
        self.filterConfigurationLabel.setText(QCoreApplication.translate("Form", u"Filter Configuration", None))
        self.whiteButton2.setText(QCoreApplication.translate("Form", u"White", None))
        self.redButton2.setText(QCoreApplication.translate("Form", u"Red", None))
        self.whiteButton1.setText(QCoreApplication.translate("Form", u"White", None))
        self.eventTypeLabel.setText(QCoreApplication.translate("Form", u"Event Type: ", None))
        self.creatorLabel.setText(QCoreApplication.translate("Form", u"Creator:", None))
    # retranslateUi


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = FilterConfigurationWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())