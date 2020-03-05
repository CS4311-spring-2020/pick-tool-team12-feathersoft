import splunklib.client as client
import splunklib.results as results
import os
from configurations.rwo.significant_log_entry import SignificantLogEntry
import datetime

class splunk_integrator:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 8089
        self.INDEX = "main"
        self.USERNAME = "asosa19"
        self.PASSWORD = "stevenroach"
        self.entries = list()

        # Create a Service instance and log in

        self.service = client.connect(
            host=self.HOST,
            port=self.PORT,
            username=self.USERNAME,
            password=self.PASSWORD)


    # Takes a file as input and uploads to splunk
    def upload_file(self,path):
        index = self.service.indexes[self.INDEX]
        index.upload(path)



    def download_log_files(self):
        # Retrieve search jobs
        jobs = self.service.jobs
        # blocks until search is finished
        blocking_search = {"exec_mode":"blocking"}
        # Query criteria
        query = "search * | head 100"

        # Create search job
        job = jobs.create(query, **blocking_search)
        # Parse results
        job_results = results.ResultsReader(job.results())
        i = 0
        for result in job_results:
            if True:
                self.entries.append(SignificantLogEntry(i,result['_indextime'],result['index'],result['host'],result['source'],result['sourcetype']))
            i += 1
        return self.entries

    def display_entries(self):
        testlog = open('testlog.txt','w')
        for entry in self.entries:
            testlog.write(str(entry._log_entry_number) + " " + str(datetime.datetime.utcfromtimestamp(int(entry._log_entry_timestamp)))+ " " + str(entry._log_entry_content) + " " + str(entry._host) + " " + str(entry._source) + " " + str(entry._source_type) + '\n')
            entry.display()



if __name__ == '__main__':
    client = splunk_integrator()
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    dummy_file = os.path.join(THIS_FOLDER,'dummy_log.txt')
    client.download_log_files()
    client.display_entries()




