import splunklib.client as client
import splunklib.results as results
import os
from configurations.rwo.significant_log_entry import SignificantLogEntry
from configurations.file_handler import *
import datetime


class SplunkIntegrator():

    def __init__(self,host,port,index,username,password):
        self._host = host
        self._port = port
        self._index = index
        self._username = username
        self._password = password
        self.entries = list()
        self.file_cleanser = FileCleanser()
        self.file_converter = FileConverter()
        self.file_validator = FileValidator(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                                            datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))



        # Create a Service instance and log in

        self.service = client.connect(
            host=self._host,
            port=self._port,
            username=self._username,
            password=self._password)


    # Takes a file as input and uploads to splunk

    def create_index(self,index_name):
        self.service.indexes.create(index_name)

    def set_index(self,index_name):
        self._index = index_name

    def upload_file(self,path,index):
        index = self.service.indexes[index]
        try:
            index.upload(os.path.abspath(path))
        except Exception as e:
            print(str(e))

    def view_indexes(self):
        for index in self.service.indexes:
            print(index.name)

    def get_index(self,index):
        return self.service.indexes.get(index)

    def get_content(self,index):
        self.set_index(index)
        for job in self.service.jobs:
            print(job)

    def download_log_files(self,count):
        # Retrieve search jobs
        jobs = self.service.jobs
        # blocks until search is finished
        blocking_search = {"exec_mode":"blocking"}
        # Query criteria
        query = "search * root"

        # Create search job
        job = jobs.create(query, **blocking_search)

        # Parse results
        job_results = results.ResultsReader(job.results(count=count))
        i = 0
        for result in job_results:
            if True:
                self.entries.append(SignificantLogEntry(i,result['_indextime'],result['index'],result['host'],result['source'],result['sourcetype']))
            i += 1

        return self.entries

    def cleanse_file(self,file):
        return self.file_cleanser.cleanse_file(file)

    def validate_file(self,file,event_start, event_end):
        self.file_validator.start_timestamp = event_start
        self.file_validator.end_timestamp = event_end
        return self.file_validator.validate_file(file)


if __name__ == '__main__':
    client = SplunkIntegrator('192.168.81.1', 8089, 'feathersoft', 'Feathersoft', 'stevenroach')
    client.create_index('sw2')






