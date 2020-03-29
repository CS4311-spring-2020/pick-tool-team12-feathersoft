import speech_recognition as sr
from moviepy.editor import *
import pytesseract as pt
import ffmpeg
import os
import pocketsphinx
from PIL import Image
from pydub import AudioSegment
import subprocess


class FileHandler():

    def __init__(self, files):
        self.speech_recognizer = sr.Recognizer()
        self._files = files

    def handle_audio(self, audio_file):
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

    def handle_video(self, video_file):
        video = VideoFileClip(video_file)
        audio = video.audio
        file = video_file.split('.')[0] + '.wav'
        audio.write_audiofile(file)
        self.handle_audio(file)
        return file

    def handle_image(self, image_file):
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

    def run(self, cpp_file, file ,output):
        #os.system('make')
       if subprocess.run(f'{cpp_file} {file} {output}') == 0:
           print('success')

if __name__ == '__main__':
    h = FileHandler(None)
    h.run('cleansing_script/typescript2txt.exe','01_input.txt', '01_input.txt_clean')




