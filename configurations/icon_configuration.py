import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class IconConfiguration(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 50, 850, 800)
        self.setWindowTitle("Icon Configuration")
        self.UI()

    def UI(self):

        mainImage = QLabel(self)
        mainImage.setPixmap(QPixmap('analyst_small.png'))
        mainImage.setGeometry(520,70,350,350)

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

        vbox = QGridLayout()
        iconTable = QTableWidget(self)
        iconTable.setColumnCount(4)
        iconTable.setRowCount(10)

        iconTable.setHorizontalHeaderItem(0, QTableWidgetItem(""))
        iconTable.setHorizontalHeaderItem(1,QTableWidgetItem(QIcon('up-down-arrow.png'), "Icon Name"))
        iconTable.setHorizontalHeaderItem(2,QTableWidgetItem(QIcon('up-down-arrow.png'), "Icon Source"))
        iconTable.setHorizontalHeaderItem(3,QTableWidgetItem( " Image Preview"))

        header = iconTable.horizontalHeader()

        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1,QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3,QHeaderView.ResizeToContents)

        for i in range(iconTable.rowCount()):

            checkbox = QTableWidgetItem()
            checkbox.setCheckState(Qt.Unchecked)

            analystImage = QTableWidgetItem()
            analystImage.setIcon(QIcon('analyst.png'))


            iconName = QTableWidgetItem()
            iconName.setData(Qt.DisplayRole, 'Cloud')

            iconSource = QTableWidgetItem()
            iconSource.setData(Qt.DisplayRole, 'example/icon/lib/cloud.png')

            iconTable.setItem(i, 1, iconName)
            iconTable.setItem(i, 2, iconSource)
            iconTable.setItem(i,0,checkbox)

            iconTable.setItem(i, 3, analystImage)


        iconTable.setGeometry(50, 100, 400, 300)

        buttonAdd = QPushButton(self)
        buttonAdd.setGeometry(700,400,70,30)
        buttonAdd.setText('Add Icon')

        buttonEdit = QPushButton(self)
        buttonEdit.setGeometry(600, 400, 70, 30)
        buttonEdit.setText('Edit Icon')

        buttonDelete = QPushButton(self)
        buttonDelete.setGeometry(500, 400, 70, 30)
        buttonDelete.setText('Delete Icon')

        vbox.addWidget(mainMenu)
        vbox.addWidget(iconTitle)
        vbox.addWidget(iconTable)
        vbox.addWidget(mainImage)
        vbox.addWidget(buttonAdd)
        vbox.addWidget(buttonEdit)
        vbox.addWidget(buttonDelete)

        #self.setLayout(vbox)
        #self.show()


if __name__ == '__main__':
    App = QApplication(sys.argv)
    window = IconConfiguration()
    sys.exit(App.exec())