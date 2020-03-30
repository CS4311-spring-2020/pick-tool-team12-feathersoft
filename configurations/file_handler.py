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

import datefinder as ds
import dateparser as dp


class FileConverter():

    def __init__(self):
        self.speech_recognizer = sr.Recognizer()



    def convert_file(self, file):
        ext = file.split('.')[1]
        audio = ['mp3', 'wav']
        video = ['mp4']
        image = ['jpg', 'pdf', 'png']

        if ext in audio: self.convert_audio_to_text(file)
        elif ext in video: self.convert_video_to_audio(file)
        elif ext in image: self.convert_image_to_text(file)
        else: return file

    def convert_audio_to_text(self, audio_file):
        if '.mp3' in audio_file:
            src = audio_file
            dest = audio_file.split('.')[0] + '.wav'

            sound = AudioSegment.from_mp3(src)
            sound.export(dest, format="wav")
            audio_file = dest

        with sr.AudioFile(audio_file) as source:
            audio = self.speech_recognizer.record(source)
            text = self.speech_recognizer.recognize_sphinx(audio)
            with open(audio_file.split('.')[0] + '.txt', 'w') as output:
                output.write(text)

        return output

    def convert_video_to_audio(self, video_file):
        video = VideoFileClip(video_file)
        audio = video.audio
        file = video_file.split('.')[0] + '.wav'
        audio.write_audiofile(file)
        self.convert_audio_to_text(file)


    def convert_image_to_text(self, image_file):
        pt.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
        image = Image.open(image_file)
        text = pt.image_to_string(image, lang='eng')
        file = image_file.split('.')[0] + '.log'
        with open(file, 'w') as output:
            output.write(text)

        return output

    def handle_csv(self, csv_file):
        pass

    def default(self, file):
        return file


class FileCleanser():

    def cleanse_file(self, file):

        content = open(file,'r').readlines()
        for line in content:
            for char in line:
                if not char.isalpha() or char.isdigit() or char in ['*','.',':']:
                    char.replace(char, "")

        with open(file,'w') as output:
            output.writelines(content)

        return True



class FileValidator():

    def __init__(self,event_start, event_end):

        self.start_timestamp = event_start
        self.end_timestamp = event_end

    def validate_file(self,file):
        lines = [line for line in open(file, 'r').readlines()]
        timestamp_pattern = '\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}:\\d{1,2}:\\d{1,2}'
        timestamp_pattern = '\\d{2}[-]?\\d{1,2} \\d{1,2}:\\d{1,2}:\\d{1,2}.\\d{1,3}'
        formatting = '%m-%d %H:%M:%S.%f'
        enforcement_action_report = dict()
        enforcement_action_report['empty_lines'] = [i for i in range(len(lines)) if len(lines[i].strip()) == 0]
        enforcement_action_report['missing_time_stamp'] = [i for i in range(len(lines))
                                                           if not re.findall(timestamp_pattern, lines[i])]
        enforcement_action_report['invalid_time_stamp'] = \
            [i for i in range(len(lines)) if re.findall(timestamp_pattern, lines[i])
                and not datetime.strptime(self.start_timestamp.strip(), formatting)
                <= datetime.strptime(re.findall(timestamp_pattern.strip(), lines[i])[0], formatting)
                <= datetime.strptime(self.end_timestamp.strip(), formatting)]

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
                [i for i in range(len(lines)) if re.findall(timestamp_pattern, lines[i])
                 and not upper_bound <= datetime.strptime(re.findall(timestamp_pattern.strip(), lines[i])[0], formatting)
                 <= lower_bound]

        test_passed = all(value == [] for value in enforcement_action_report.values())
        if test_passed:
            return True
        else:
            return enforcement_action_report


if __name__ == '__main__':
    fv = FileValidator('03-17 16:13:38.811','03-18 16:16:09.141')



