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


class FileConverter():

    def __init__(self):
        self.speech_recognizer = sr.Recognizer()

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

    def convert_video_to_audio(self, video_file):
        video = VideoFileClip(video_file)
        audio = video.audio
        file = video_file.split('.')[0] + '.wav'
        audio.write_audiofile(file)
        self.convert_audio_to_text(file)
        return file

    def convert_image_to_text(self, image_file):
        pt.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
        image = Image.open(image_file)
        text = pt.image_to_string(image, lang='eng')
        file = image_file.split('.')[0] + '.log'
        with open(file, 'w') as output:
            output.write(text)

    def handle_csv(self, csv_file):
        pass

    def default(self, file):
        return file


class FileCleanser():


    def cleanse_file(self, cpp_file, file,output):
        os.chdir('cleansing_script/tests')
        os.system(f'script  -a {file}')
        if os.system(f'./{cpp_file}  <{file}>  {output}') == 0:
            print('Successfully Cleansed')
            return True
        else:
            os.remove(output)
        os.chdir('..')
        print(os.getcwd())
        return False


class FileValidator():

    def __init__(self,event_start, event_end):

        self.start_timestamp = event_start
        self.end_timestamp = event_end


    def validate_file(self,file):
        enforcement_action_report = dict()
        enforcement_action_report['empty_lines'] = list()
        enforcement_action_report['missing_time_stamp'] = list()
        enforcement_action_report['invalid_time_stamp'] = list()

        valid_file = False

        timestamp_pattern = '\\d{4}[-]?\\d{1,2}[-]?\\d{1,2} \\d{1,2}:\\d{1,2}:\\d{1,2}'
        sample = '2020-03-29 18:07:10'

        with open(file,'r') as test_file:
            lines = [line for line in test_file.readlines()]
            i = 1
            for line in lines:
                if len(line.strip()) == 0:
                    enforcement_action_report['empty_lines'].append(i)

                if not re.findall(timestamp_pattern,line):
                    enforcement_action_report['missing_time_stamp'].append(i)
                else:
                    if re.findall(timestamp_pattern,line):
                        pass
                i += 1



            print(enforcement_action_report)







if __name__ == '__main__':
    h = FileConverter(None)
    fv = FileValidator()
    fv.validate_file('sample_image.log')


