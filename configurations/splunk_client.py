import splunklib.client as client
import splunklib.results as results
import os

class splunk_integrator:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 8089
        self.INDEX = "main"
        self.USERNAME = "Feathersoft"
        self.PASSWORD = "stevenroach"

        # Create a Service instance and log in

        self.service = client.connect(
            host=self.HOST,
            port=self.PORT,
            username=self.USERNAME,
            password=self.PASSWORD)

    def upload_file(self,path):
        index = self.service.indexes[self.INDEX]
        index.upload(path)


    def download_log_files(self):
        jobs = self.service.jobs
        entries = list()
        blocking_search = {"exec_mode":"blocking"}
        query = "search * | head 10"

        job = jobs.create(query, **blocking_search)
        job_results = results.ResultsReader(job.results())

        for result in job_results:
            if True:
                print(result)
                entries.append(result)
        return entries


if __name__ == '__main__':
    client = splunk_integrator()
    client.upload_file('C:/Users/jayjj/Documents/Spring 2020/Software 2/pick-tool-team12-feathersoft/configurations/root/white/wlog.txt')
    client.download_log_files()




