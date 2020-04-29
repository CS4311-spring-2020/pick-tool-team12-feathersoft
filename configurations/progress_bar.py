import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QStandardItem
from PyQt5.QtCore import *
from splunklib.binding import AuthenticationError

from configurations.rwo import LogFile


class ProgressBarWindow(QMainWindow):

    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QIcon('pythonlogo.png'))

        extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        self.home()

    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0, 100)

        extractAction = QAction(QIcon('todachoppa.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        checkBox = QCheckBox('Shrink Window', self)
        checkBox.move(100, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        self.progress = QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)



    def download(self,files,client,start,end,logs):
        self.completed = 0
        try:
            audio = ['mp3', 'wav']
            video = ['mp4']
            image = ['jpg', 'pdf', 'png']
            cleansing_status, validation_status, ingestion_status, acknowledgement_status = False, False, False, False
            converted = ''
            onlyfiles = next(os.walk('root'))[2]
            for filepath, folder, dir in os.walk('root'):
                for file in dir:
                    path = os.path.join(filepath, file)
                    ext = path.split('.')[1]
                    if ext in audio:
                        converted = client.file_converter.convert_audio_to_text(path)
                    elif ext in video:
                        converted = client.file_converter.convert_video_to_audio(path)
                    elif ext in image:
                        converted = client.file_converter.convert_image_to_text(path)
                    else:
                        converted = path
                    if converted:
                        files.add(converted)

                cleansing_status = client.cleanse_file(converted)
                validation_status = client.validate_file(converted, start, end)
                acknowledgement_status = cleansing_status and validation_status
                if acknowledgement_status:
                    client.upload_file(converted, client.credentials[2])
                    ingestion_status = acknowledgement_status and cleansing_status and validation_status
                else:
                    ingestion_status = False
                logs.append(
                    LogFile(converted, cleansing_status, validation_status, ingestion_status, acknowledgement_status))
            self.completed += 100/len(onlyfiles)
            self.progress.setValue(self.completed)


        except AuthenticationError:
            QMessageBox.critical(self, "Authentication Error", "Request Aborted: not logged in")

        self.close()

        # while self.completed < 100 and i < len(files):
        #     self.completed += 0.0001
        #     self.progress.setValue(self.completed)


    def enlarge_window(self, state):
        if state == Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)

    def close_application(self):
        choice = QMessageBox.question(self, 'Extract!',
                                            "Get into the chopper?",
                                            QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Extracting Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ProgressBarWindow()
    sys.exit(app.exec_())


