import speech_recognition as sr
from moviepy.editor import *
import pytesseract as pt
import ffmpeg
import os
import pocketsphinx
from PIL import Image
from pydub import AudioSegment
import subprocess
import re
from datetime import datetime, timedelta
import datefinder




class FileConverter():

    def __init__(self):
        self.speech_recognizer = sr.Recognizer()


    def convert_audio_to_text(self, audio_file):
        if audio_file:
            converted = audio_file.split('.')[0] + '.txt'
            if '.mp3' in audio_file:
                src = audio_file
                dest = audio_file.split('.')[0] + '.wav'

                sound = AudioSegment.from_mp3(src)
                sound.export(dest, format="wav")
                audio_file = dest

            with sr.AudioFile(audio_file) as source:
                audio = self.speech_recognizer.record(source)
                text = self.speech_recognizer.recognize_sphinx(audio)

                with open(converted, 'w') as output:
                    output.writelines(text)

                lines = open(audio_file.split('.')[0] + '.txt').readlines()
                with open(audio_file.split('.')[0] + '.txt', 'w')as f:
                    f.writelines(datetime.utcfromtimestamp(os.path.getmtime(audio_file)).strftime('%m/%d/%y %H:%M %p') + ' '
                                 + line for line in lines if line.strip())
                    f.truncate()
            print(converted)
            return converted

    def convert_video_to_audio(self, video_file):
        if video_file:
            video = VideoFileClip(video_file)
            audio = video.audio
            file = video_file.split('.')[0] + '.wav'
            audio.write_audiofile(file)
            return self.convert_audio_to_text(file)

    def convert_image_to_text(self, image_file):
        if image_file:
            converted = image_file.split('.')[0] + '.txt'
            pt.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
            image = Image.open(image_file)
            text = pt.image_to_string(image, lang='eng')
            file = image_file.split('.')[0] + '.txt'
            with open(file, 'w') as output:
                output.write(text)


            lines = open(converted).readlines()
            with open(image_file.split('.')[0] + '.txt', 'w')as f:
                f.writelines(
                    datetime.utcfromtimestamp(os.path.getmtime(image_file)).strftime('%m/%d/%y %H:%M %p') + ' ' + line for
                    line in lines if line.strip())
                f.truncate()


            return converted

    def handle_csv(self, csv_file):
        pass

    def default(self, file):
        return file


class FileCleanser():

    def cleanse_file(self, file):
        if file:
            lines = open(file, encoding='utf_8').readlines()
            lines = [re.sub(r'[\x7f\x80]', '', line) for line in lines]
            lines = [re.sub(r'[^\sA-Za-z0-9.: /=\]\[\-\n]+', '', line) for line in lines]
            lines = [re.sub('(.)\1{4,}', r'\1', line) for line in lines]
            with open(file, 'w')as f:
                f.writelines(line for line in lines if line.strip())
                f.truncate()
            return True


class FileValidator():

    def __init__(self,event_start, event_end):

        self.start_timestamp = event_start
        self.end_timestamp = event_end
        self.reports = list()

    def validate_file(self,file):
        if file:
            lines = [line for line in open(file, 'r').readlines()]
            # For this formatting pattern y should be lowercase on linux and uppercase on windows.
            formatting = '%m/%d/%y %H:%M %p'
            enforcement_action_report = dict()
            enforcement_action_report['empty_lines'] = [i for i in range(len(lines)) if len(lines[i].strip()) == 0]
            enforcement_action_report['missing_time_stamp'] = [i for i in range(len(lines)) if len(lines[i].strip()) == 0 or len(list(datefinder.find_dates(lines[i]))) == 0]
            enforcement_action_report['invalid_time_stamp'] = \
                [i for i in range(len(lines)) if len(list(datefinder.find_dates(lines[i]))) > 0
                    and not datetime.strptime(self.start_timestamp.strip(), formatting)
                    <= list(datefinder.find_dates(lines[i]))[0]
                    < datetime.strptime(self.end_timestamp.strip(), formatting)]
            # #
            if '.cvs' in file and 'white' in file:
                year = (int(datetime.strptime(self.start_timestamp.strip(), formatting).year) + \
                           int(datetime.strptime(self.start_timestamp.strip(), formatting).year)) // 2

                month = (int(datetime.strptime(self.start_timestamp.strip(), formatting).month) + \
                            int(datetime.strptime(self.start_timestamp.strip(), formatting).month)) // 2

                date = (int(datetime.strptime(self.start_timestamp.strip(), formatting).day) + \
                            int(datetime.strptime(self.start_timestamp.strip(), formatting).day)) // 2

                upper_bound = datetime(year, month,date) - timedelta(0,23,59)
                lower_bound = datetime(year, month,date) + timedelta(0,23,59)

                enforcement_action_report['invalid_time_stamp_cvs'] = \
                    [i for i in range(len(lines)) if list(datefinder.find_dates(lines[i]))[0]
                     and not upper_bound <= datetime.strptime(list(datefinder.find_dates(lines[i]))[0])
                     <= lower_bound]

            self.reports.append(enforcement_action_report)
            return all(value == [] for value in enforcement_action_report.values())


if __name__ == '__main__':
    fv = FileValidator('1/1/00 12:00 AM','1/1/00 12:00 AM')
    fv.validate_file('root/sample_audio.txt')



