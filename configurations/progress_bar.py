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
        self.setGeometry(50, 50, 700, 200)
        self.setWindowTitle("PyQT tuts!")
        self.setWindowIcon(QIcon('pythonlogo.png'))



        self.statusBar()



        self.home()

    def home(self):
        self.progress = QProgressBar(self)
        self.progress.setGeometry(50, 50, 600, 40)
        self.show()

    def count_files(self,dir):
        i = 0
        for filepath, folder, dir in os.walk('root'):
            for file in dir:
                path = os.path.join(filepath, file)
                i += 1

        return i

    def download(self,files,client,start,end,logs):
        self.completed = 0
        try:
            audio = ['mp3', 'wav']
            video = ['mp4']
            image = ['jpg', 'pdf', 'png']
            cleansing_status, validation_status, ingestion_status, acknowledgement_status = False, False, False, False
            converted = ''
            num_files = self.count_files('root')
            for filepath, folder, dir in os.walk('root'):
                for file in dir:
                    path = os.path.join(filepath, file)
                    print(path)
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
                self.completed += 100/num_files
                self.progress.setValue(self.completed)
            self.close()

        except AuthenticationError:
            QMessageBox.critical(self, "Authentication Error", "Request Aborted: not logged in")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ProgressBarWindow()
    sys.exit(app.exec_())


