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

    def get_users(self):
        kwargs_normalsearch = {"exec_mode": "normal",
                               "earliest_time": "-1m",
                               "latest_time": "now",}
        query = "| rest /services/authentication/current-context splunk_server=local|table username "
        job = self.service.jobs.create(query=query,**kwargs_normalsearch)

        # # Print the users' real names, usernames, and roles
        # print("Users:")
        # for user in users:
        #     print("%s (%s)" % (user.realname, user.name))
        #     for role in user.role_entities:
        #         print(" - ", role.name)
        job_results = results.ResultsReader(job.results())
        for job in job_results:
            print(job)

    def set_index(self, index_name):
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

    def create_user(self, username, password):
        # Create a new user
        newuser = self.service.users.create(username=username,
                                       password=password,
                                       roles=["user"])
        # Print the user's properties
        print("Properties of the new user '" + newuser.name + "':\n")
        print("Full name:  ", newuser["realname"])
        print("Default app:", newuser["defaultApp"])
        print("Time zone:  ", newuser["tz"])
        print("Role:")
        # Print the roles for the user
        for role in newuser.role_entities:
            print(" - ", role.name)

        # Change some properties and update the server
        kwargs = {"realname": "Test User",
                  "defaultApp": "launcher",
                  "tz": "Europe/Paris",
                  "roles": "can_delete"}
        newuser.update(**kwargs).refresh()

        # Print updated info
        print("\nUpdated properties")

    def download_log_files(self,count, index):
        # Retrieve search jobs
        self.set_index(index)
        jobs = self.service.jobs
        # blocks until search is finished
        blocking_search = {"exec_mode":"blocking"}
        # Query criteria
        query = "search root "

        # Create search job
        job = jobs.create(query, **blocking_search)

        # Parse results
        job_results = results.ResultsReader(job.results(count=count))
        i = 0
        for result in job_results:
            if True:
                self.entries.append(SignificantLogEntry(i, result['_indextime'],
                                                        result['_raw'], result['host'],
                                                        self.find_source_file('root',result['source']),
                                                        self.find_event_source('root',result['source'])))
            i += 1
        for entry in self.entries:
            print(entry)
        return self.entries

    def cleanse_file(self, file):
        return self.file_cleanser.cleanse_file(file)

    def enable_roles(self, role):
        permissions = ''
        role = self.service.roles[role]
        role.grant('change_own_password', 'search', 'input_file', 'admin_all_objects',
                   'rest_apps_management', 'rest_apps_view', 'rest_properties_get', 'rest_properties_set',
                   'edit_sourcetypes')

    def validate_file(self, file, event_start, event_end):
        self.file_validator.start_timestamp = event_start
        self.file_validator.end_timestamp = event_end
        return self.file_validator.validate_file(file)

    def find_source_file(self,root_folder, entry):
        for filepath, folder, dir in os.walk(root_folder):
            for file in dir:
                path = os.path.join(filepath,file)
                if entry.split('\\')[1] in path:
                    return path

    def find_event_source(self, root_folder, entry):
        if 'white' in self.find_source_file(root_folder,entry):
            return 'white'

        elif 'red' in self.find_source_file(root_folder, entry):
            return 'red'

        elif 'blue' in self.find_source_file(root_folder, entry):
            return 'blue'

        else:
            return 'root'