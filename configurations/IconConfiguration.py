import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 850, 600)
        self.setWindowTitle("Icon Configuration")
        self.UI()

    def UI(self):

        mainImage = QLabel(self)
        mainImage.setPixmap(QPixmap('blueTeam.png'))
        mainImage.setGeometry(470,70,350,350)


        mainMenu = QMenuBar(self)
        mainMenu.addMenu('File')
        mainMenu.addMenu('Edit')
        mainMenu.addMenu('View')
        mainMenu.addMenu('Search')
        mainMenu.addMenu('Tools')
        mainMenu.addMenu('Help')

        iconTitle = QLabel('Icon Configuration', self)
        iconTitle.setFont(QFont('MS Shell Dlg 2', 12))
        iconTitle.move(50,70)

        vbox = QVBoxLayout()
        iconTable = QTableWidget(self)
        iconTable.setColumnCount(4)
        iconTable.setRowCount(5)

        iconTable.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        iconTable.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('up-down-arrow.png'), "Icon Name"))
        iconTable.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('up-down-arrow.png'), "Icon Source"))
        iconTable.setHorizontalHeaderItem(3,QTableWidgetItem( " Image Preview"))

        header = iconTable.horizontalHeader()
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3,QHeaderView.ResizeToContents)

        for i in range(iconTable.rowCount()):
            iconTable.setVerticalHeaderItem(i,QTableWidgetItem(''))
        log = [line.split(' ') for line in open('example.txt').readlines()]
        for i in range(len(log)):
            iconTable.setItem(i,0,QTableWidgetItem(str(i + 1)))
            iconTable.setItem(i,1,QTableWidgetItem(str(log[i][0])))

            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)

            iconName = QTableWidget()
            iconName.setRowCount(4)
            iconName.setVerticalHeaderItem(0, QTableWidgetItem('Cloud'))
            iconName.setVerticalHeaderItem(1, QTableWidgetItem('Red Team'))
            iconName.setVerticalHeaderItem(2, QTableWidgetItem('Blue Team'))
            iconName.setVerticalHeaderItem(3, QTableWidgetItem('Analyst'))

            iconSource = QTableWidget()
            iconSource.setRowCount(4)
            iconSource.setVerticalHeaderItem(0, QTableWidgetItem('example/icon/lib/cloud.png'))
            iconSource.setVerticalHeaderItem(1, QTableWidgetItem('example/icon/lib/redTeam.png'))
            iconSource.setVerticalHeaderItem(2, QTableWidgetItem('example/icon/lib/blueTeam.png'))
            iconSource.setVerticalHeaderItem(3, QTableWidgetItem('example/icon/lib/analyst.png'))

            iconTable.setCellWidget(i, 2, iconSource)
            iconTable.setCellWidget(i, 1, iconName)
            iconTable.setItem(i,0,checkbox)

        upDownImage = QTableWidgetItem()
        upDownImage.setIcon(QIcon('cloud.png'))

        redTeamImage = QTableWidgetItem()
        redTeamImage.setIcon(QIcon('redTeam.png'))

        blueTeamImage = QTableWidgetItem()
        blueTeamImage.setIcon(QIcon('blueTeam.png'))

        analystImage = QTableWidgetItem()
        analystImage.setIcon(QIcon('analyst.png'))





        iconTable.setItem(0, 3, upDownImage)
        iconTable.setItem(1, 3, redTeamImage)
        iconTable.setItem(2, 3, blueTeamImage)
        iconTable.setItem(3, 3, analystImage)


        iconTable.setGeometry(50, 100, 400, 300)

        buttonAdd = QPushButton(self)
        buttonAdd.setGeometry(700,400,70,30)
        buttonAdd.setText('Add Icon')

        buttonEdit = QPushButton(self)
        buttonEdit.setGeometry(600, 400, 70, 30)
        buttonEdit.setText('Edit Icon')

        buttonDelete = QPushButton(self)
        buttonDelete.setGeometry(500, 400, 70, 30)
        buttonDelete.setGeometry(500, 400, 70, 30)
        buttonDelete.setText('Delete Icon')

        vbox.addWidget(iconTable)
        vbox.addWidget(buttonAdd)
        vbox.addWidget(buttonEdit)
        vbox.addWidget(buttonDelete)


        self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())