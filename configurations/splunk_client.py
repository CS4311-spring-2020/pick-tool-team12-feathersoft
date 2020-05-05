import splunklib
import splunklib.client as client
import splunklib.results as results
import splunklib.binding as binding
import os
from configurations.rwo.significant_log_entry import SignificantLogEntry
from configurations.file_handler import *
import datetime


class SplunkIntegrator():

    def __init__(self):
        self.entries = list()
        self.file_cleanser = FileCleanser()
        self.file_converter = FileConverter()
        self.file_validator = FileValidator(datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                                            datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'))

        self.conf_path = "auth/splunk_auth.txt"
        self.credentials = open(self.conf_path).readline().split(' ')
        # Create a Service instance and log in

        # Takes a file as input and uploads to splunk

    def create_index(self, index_name):
        self.service.indexes.create(index_name)

    def connect(self):
        self.service = splunklib.client.Service(host=self.credentials[0], port=self.credentials[1])

    def connect_enterprise(self,username,password):
        self.service = splunklib.client.connect(host=self.credentials[0], port=self.credentials[1], username=username,
                                                password=password)

    def connect_via_token(self, token):
        self.service = splunklib.client.connect(token=token)

    def get_users(self, lead_ip):
        query = f'search index=demo3 clientip!="{lead_ip}"'
        blocking_search = {"exec_mode": "blocking",
                           "earliest_time": "-24h",
                           "latest_time": "now"}
        job = self.service.jobs.create(query=query, **blocking_search)
        job_results = results.ResultsReader(job.results())
        ip = [job['clientip'] for job in job_results]
        print(len(set(ip)))

    def set_index(self, index_name):
        self._index = index_name

    def upload_file(self, path, index):
        index = self.service.indexes[index]
        try:
            index.upload(os.path.abspath(path))
        except Exception as e:
            print(str(e))

    def view_indexes(self):
        for index in self.service.indexes:
            print(index.name)

    def get_index(self, index):
        return self.service.indexes.get(index)

    def get_content(self, index):
        self.set_index(index)
        for job in self.service.jobs:
            print(job)

    def get_connected_users(self):
        query = ' | rest /services/authentication/httpauth-tokens | ' \
                'search (NOT userName="splunk-system-user") searchId="" ' \
                '| table userName splunk_server timeAccessed'

        query = '| rest /services/authentication/httpauth-tokens splunk_server=local'

        query = ' | rest /services/authentication/httpauth-tokens splunk_server=local | stats max(updated) by userName'
        # query = 'search source="wineventlog:security" action=success Logon_Type=2 (EventCode=4624 OR EventCode=4634
        # OR EventCode=4779 OR EventCode=4800 OR EventCode=4801 OR EventCode=4802 OR EventCode=4803 OR EventCode=4804
        # ) user!="anonymous logon" user!="DWM-*" user!="UMFD-*" user!=SYSTEM user!=*$ (Logon_Type=2 OR Logon_Type=7
        # OR Logon_Type=10)| convert timeformat="%a %B %d %Y" ctime(_time) AS Date | streamstats earliest(_time) AS
        # login, latest(_time) AS logout by Date, host| eval session_duration=logout-login | eval h=floor(
        # session_duration/3600) | eval m=floor((session_duration-(h*3600))/60) | eval SessionDuration=h."h ".m."m "
        # | convert timeformat=" %m/%d/%y - %I:%M %P" ctime(login) AS login | convert timeformat=" %m/%d/%y - %I:%M
        # %P" ctime(logout) AS logout | stats count AS auth_event_count, earliest(login) as login,
        # max(SessionDuration) AS sesion_duration, latest(logout) as logout, values(Logon_Type) AS logon_types by
        # Date, host, user'

        query = 'search index=_internal source=*web_access.log* /app/   | rex "GET\s\/[^\/]+\/app\/(?P<app>[^\/]+)\/(' \
                '?P<view>[^\s|?]+) "  | search app=* view=*| stats count by user app view '
        # query = ' | rest /services/authentication/httpauth-tokens splunk_server=local | stats max(updated) by
        # userName'
        blocking_search = {"exec_mode": "blocking"}
        job = self.service.jobs.create(query=query, **blocking_search)
        job_results = results.ResultsReader(job.results())
        connected_users = [job for job in job_results]
        for user in connected_users:
            print(user)
        print(len(connected_users))

    def create_user(self, username, password, role):
        # Create a new user
        newuser = self.service.users.create(username=username,
                                            password=password,
                                            roles=[f"{role}"])
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
                  "tz": "Europe/Paris"}
        newuser.update(**kwargs).refresh()

        # Print updated info
        print("\nUpdated properties")

    def download_log_files(self, count):
        # Retrieve search jobs
        jobs = self.service.jobs
        # blocks until search is finished
        blocking_search = {"exec_mode": "blocking"}
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
                                                        self.find_source_file('root', result['source']),
                                                        self.find_event_source('root', result['source'])))
            i += 1

        for entry in self.entries:
            print()

    def cleanse_file(self, file):
        return self.file_cleanser.cleanse_file(file)

    def enable_roles(self, role):
        permissions = ''
        role = self.service.roles[role]
        role.grant('accelerate_datamodel', 'accelerate_search', 'admin_all_objects'
                                                                'change_authentication', 'change_own_password',
                   'delete_by_keyword',
                   'edit_deployment_client', 'edit_deployment_server', 'edit_dist_peer',
                   'edit_forwarders', 'edit_httpauths', 'edit_indexer_cluster', 'edit_input_defaults',
                   'edit_monitor', 'edit_roles', 'edit_roles_grantable', 'edit_scirpted',
                   'edit_search_head_clustering', 'edit_search_schedule_priority',
                   'edit_search_schedule_window', 'edit_search_scheduler', 'edit_search_server',
                   'edit_server_crl', 'edit_sourcetypes', 'edit_splunktcp', 'edit_splunk_ssl',
                   'edit_splunktcp_token', 'edit_tcp', 'edit_tcp_token', 'edit_telemetry_settings',
                   'edit_token_http', 'edit_upd', 'edit_user', 'edit_view_html', 'edit_web_settings',
                   'embed_report', 'export_results_is_visible', 'extra_x509_validation', 'get_diag',
                   'get_metadata', 'get_typeahead', 'indexes_edit', 'input_file', 'license_edit',
                   'licencse_tab', 'license_view_warnings', 'license_accelerate_search',
                   'list_deployment_client', 'list_deployment_server', 'list_forwarders',
                   'list_httpauths', 'list_indexer_cluster', 'list_indexerdiscovery', 'list_inpuuts',
                   'list_introspection', 'list_search_head_clustering', 'list_search_scheduler',
                   'list_settings', 'list_storage_passwords', 'output_file', 'pattern_detect',
                   'request_remote_tok', 'rest_apps_management', 'rest_apps_view', 'rest_properties_get',
                   'rest_properties_set', 'restart_splunkkd', 'rtsearch', 'run_debug_commands',
                   'run_multi_phased_searches', 'schedule_search', 'search', 'search_process_config_refresh',
                   'srchFilter', 'srchIndexesAllowed', 'srchIndexesDefault', 'srchJobsQuota', 'srchMaxTime',
                   'use_file_operator', 'web_debug')

    def get_session_token(self):
        return self.service.token

    def validate_file(self, file, event_start, event_end):
        self.file_validator.start_timestamp = event_start
        self.file_validator.end_timestamp = event_end
        return self.file_validator.validate_file(file)

    def find_source_file(self, root_folder, entry):
        for filepath, folder, dir in os.walk(root_folder):
            for file in dir:
                path = os.path.join(filepath, file)
                if entry.split('\\')[1] in path:
                    return path

    def find_event_source(self, root_folder, entry):
        if 'white' in self.find_source_file(root_folder, entry):
            return 'white'

        elif 'red' in self.find_source_file(root_folder, entry):
            return 'red'

        elif 'blue' in self.find_source_file(root_folder, entry):
            return 'blue'

        else:
            return 'root'


if __name__ == '__main__':
    client = SplunkIntegrator()
    client.connect()
    client.download_log_files(10)



