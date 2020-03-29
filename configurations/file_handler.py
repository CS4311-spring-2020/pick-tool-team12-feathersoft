import speech_recognition as sr
from moviepy.editor import *
import pytesseract as pt
import ffmpeg
import os
import pocketsphinx
from PIL import Image

from pydub import AudioSegment


class FileHandler():

    def __init__(self, files):
        self.speech_recognizer = sr.Recognizer()
        self._files = files

    def handle_file(self,file):
        switcher = {
            '.wav' or '.mp3' in file: self.handle_audio(file),
            '.mp4' in file: self.handle_image(file),
            '.jpeg' or '.png' or '.pdf' in file: self.handle_image(file)
        }

        return switcher.get(file, 'Invalid file extension')

    def handle_files(self, files):
        return self._files.append(self.handle_file(file) for file in files)

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


if __name__ == '__main__':
    handler = FileHandler(None)
    handler.handle_audio('root/red/audio-sample-1.mp3')
    #handler.handle_video('audio-sample-1.mp3')
    handler.handle_image('root/blue/Barcode/barcode1.jpg')



