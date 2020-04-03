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
import parsedatetime
import dateparser
from dateparser.search import search_dates
from dateutil.parser import parse


class FileConverter():
    """
        The FileConverter class provides all options needed to convert non-textual files in to text-based log files
        (i.e video to audio, audio to text, image to text .. etc).
    """

    def __init__(self):

        # Offline speech recognizer will be used to parse text from audio.
        self.speech_recognizer = sr.Recognizer()

    def convert_audio_to_text(self, audio_file):
        """
        :param audio_file:(str) Path of the audio file to be converted to text.
        :return: Path to the file containing the converted audio text.
        """
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
        """
        :param video_file:(str) The file to be converted into audio.
        :return:(str) The path to the converted audio file.
        """
        if video_file:
            video = VideoFileClip(video_file)
            audio = video.audio
            file = video_file.split('.')[0] + '.wav'
            audio.write_audiofile(file)
            return self.convert_audio_to_text(file)

    def convert_image_to_text(self, image_file):
        """
        :param image_file: (str) Image file from which text is to be extracted.
        :return:(str) The path to the file containing the extracted image text.
        """
        if image_file:
            converted = image_file.split('.')[0] + '.txt'

            """
                The path to the executable program must be provided within the method before text is extracted.
                Please be sure to install tesseract on your OS and configure your path env variable before running.
            """
            pt.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

            # Open image file.
            image = Image.open(image_file)
            # Convert to to string.
            text = pt.image_to_string(image, lang='eng')
            # Create new file of the same name with .txt extension
            file = image_file.split('.')[0] + '.txt'

            # Write text to file.
            with open(file, 'w') as output:
                output.write(text)

            # Write a timestamp to each file for validation (The last date modified)
            lines = open(converted).readlines()
            with open(image_file.split('.')[0] + '.txt', 'w')as f:
                f.writelines(
                    datetime.utcfromtimestamp(os.path.getmtime(image_file)).strftime('%m/%d/%y %H:%M %p') + ' ' + line
                    for line in lines if line.strip())
                f.truncate()

            # Return the path to the converted file
            return converted

    def handle_csv(self, csv_file):
        pass

    def default(self, file):
        return file


class FileCleanser():

    """
        The FileCleanser class is used to perform the cleansing operation on a log file.
        It should remove any unwanted characters as well as empty lines for every line in the file.
    """

    def cleanse_file(self, file):
        """
        :param file:(str) The file to be cleansed
        :return:(boolean) Original file cleansed of unwanted characters and empty lines.
        TODO: Add functionality to remove repetitive sequences of characters (i.e CCCCCCCCCCCCCC$$$$$$%%%%%%%%%)
        """

        # Check if file is null
        if file:
            lines = open(file, encoding='utf_8').readlines()


            apache = [re.findall(r'\[(\d{2})/([a-zA-Z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2})]',line) for line in lines]
            valid_times = []
            if apache:
                for apache_timestamp in apache:
                    for day, month, year, hour, min, sec in apache_timestamp:
                        valid_times.append(month + ' ' + day + ' ' + year + ' ' + hour + ':' + min + ':' + sec)

            # Replace all unwanted characters with empty strings using regular expressions to match unwanted patterns.

            lines = [re.sub(r'[\x7f\x80]', '', line) for line in lines]
            lines = [re.sub(r'[^\sA-Za-z0-9.: /=\-\n\[\]]+', '', line) for line in lines]

            # Datefinder has trouble parsing apache logs so here's some regex to handle that.

            if len(valid_times) > 0:
                lines = [re.sub(r'(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})', ' ', line) for line in lines]
                lines = [re.sub(r'\[(\d{2})/([a-zA-Z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2})]', valid_times[i], lines[i]) for
                         i in range(len(lines))]
            with open(file, 'w')as f:
                f.writelines(line for line in lines if line.strip())
                # Remove all empty lines.
                f.truncate()
            return True


class FileValidator():

    """
        The FileValidator class is responsible for performing the validation operation of a log file.
        (i.e Checking for empty lines, missing timestamps and ensuring all timestamps in the file are within
        range of the start and end dates provided in the event configuration.)
    """

    def __init__(self,event_start, event_end):

        """

        :param event_start: The start date and start time of an event.
        :param event_end: The end date and end time of an event.
        """

        self.start_timestamp = event_start
        self.end_timestamp = event_end
        self.reports = list()

    def validate_file(self,file):

        """
        :param file:(str) The file to be validated.
        :return:(bool) Validation status of a file
        """

        # Check if file is not null before performing any operations
        if file:
            # Get all lines in file.
            lines = [line for line in open(file, 'r').readlines()]
            # For this formatting pattern y should be lowercase on linux and uppercase on windows.
            # Setting date time format for datetime parser
            formatting = '%m/%d/%y %H:%M %p'
            # An enforcement action report is a dict of values containing the lines that errors occur on in a log file
            enforcement_action_report = dict()
            # Getting all indexes that contain empty lines.
            enforcement_action_report['empty_lines'] = \
                [i for i in range(len(lines)) if len(lines[i].strip()) == 0]

            # Getting all indexes that contain missing timestamps (i.e) empty line or missing timestamps
            enforcement_action_report['missing_time_stamp'] = \
                [i for i in range(len(lines)) if len(lines[i].strip()) ==
                    0 or not len(list(datefinder.find_dates(lines[i])))]

            # Getting all indexes that fall outside the timestamp range from the event configuration.
            # (i.e all non start_time <= current_time <==end_time)
            enforcement_action_report['invalid_time_stamp'] = \
                [i for i in range(len(lines)) if len(list(datefinder.find_dates(lines[i]))) > 0
                    and not datetime.strptime(self.start_timestamp.strip(), formatting)
                    <= list(datefinder.find_dates(lines[i]))[0]
                    <= datetime.strptime(self.end_timestamp.strip(), formatting)]

            # If the file extension is CVS and  it came from the white directory..
            if '.csv' in file and 'white' in file:

                # Take the average of the year month and date values
                year = (int(datetime.strptime(self.start_timestamp.strip(), formatting).year) + \
                           int(datetime.strptime(self.start_timestamp.strip(), formatting).year)) // 2

                month = (int(datetime.strptime(self.start_timestamp.strip(), formatting).month) + \
                            int(datetime.strptime(self.start_timestamp.strip(), formatting).month)) // 2

                date = (int(datetime.strptime(self.start_timestamp.strip(), formatting).day) + \
                            int(datetime.strptime(self.start_timestamp.strip(), formatting).day)) // 2

                # Subtract 23:59 from the upper bound.
                upper_bound = datetime(year, month,date) - timedelta(0,23,59)
                # Add 23:59 to the lower bound.
                lower_bound = datetime(year, month,date) + timedelta(0,23,59)

                # Invalid CVS files timestamps are those that fall outside the range of start <= current < end
                enforcement_action_report['invalid_time_stamp_cvs'] = \
                    [i for i in range(len(lines)) if list(datefinder.find_dates(lines[i]))[0]
                     and not upper_bound <= datetime.strptime(list(datefinder.find_dates(lines[i]))[0])
                     <= lower_bound]

            # File validator will keep track of all enforcement action reports
            self.reports.append(enforcement_action_report)
            # If all lists in the dictionary are empty that means no errors were found
            return all(value == [] for value in enforcement_action_report.values())


if __name__ == '__main__':
    fc = FileCleanser()
    fc.cleanse_file('root/white/www1/apache.log')
    fv = FileValidator('1/1/00 12:00 AM','4/1/20 12:00 AM')
    fv.validate_file('root/white/www1/apache.log')
    print((search_dates('17 May 2015:10:05:10')))



