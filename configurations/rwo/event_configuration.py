import os


class EventConfiguration:

    """ The event configuration class is responsible for storing all necessary information to configure an event

        Attributes:
        _event_name: (str) Name of the AA event.
        _event_description: (str) Description of the AA event.
        _event_start_timestamp: (str) Start date  and time of the AA event.
        _event_end_timestamp: (str) End date and time of the AA event.
        _root_directory: (str) Path to where the log files are stored.
        _red_team_folder: (str) Name of the folder where all the red team log files are stored.
        _white_team_folder:(str) Name of the folder where all the white team log files are stored.
        _blue_team_folder: (str) Name of the folder where all the blue team log files are stored.
        _lead: (bool) Indicator of the host machine where the master vector DB is stored.
        _lead_ip_address: (str) Required; Editable	Identifier of the host machine where the master vector DB is stored.
        _connections_established (int) Number of established connections to the host machine.

    """

    def __init__(self, **kwargs):
        """
        args:
            **kwargs:
             event_name: (str) Name of the AA event.
             event_description: (str) Description of the AA event.
             event_start_timestamp: (str) Start date  and time of the AA event.
             event_end_timestamp: (str) End date and time of the AA event.
             root_directory: (str) Path to where the log files are stored.
             red_team_folder: (str) Name of the folder where all the red team log files are stored.
             white_team_folder:(str) Name of the folder where all the white team log files are stored.
             blue_team_folder: (str) Name of the folder where all the blue team log files are stored.
             lead: (bool) Indicator of the host machine where the master vector DB is stored.
             lead_ip_address: (str) Required; Editable	Identifier of the host machine where the master vector DB is
             stored.
             connections_established (int) Number of established connections to the host machine.

            """
        self._event_name = kwargs['event_name']
        self._event_description = kwargs['event_description']
        self._event_start_timestamp = ['event_start_timestamp']
        self._event_end_timestamp = kwargs['event_end_timestamp']
        self._root_directory = kwargs['root_directory']
        self._red_team_folder = kwargs['red_team_folder']
        self._white_team_folder = kwargs['white_team_folder']
        self._blue_team_folder = kwargs['blue_team_folder']
        self._lead = kwargs['lead']
        self._leads_ip_address = kwargs['ip_address']
        self._connection_established = kwargs['connection_established']
        self.logs = []

    def find_source_file(self, entry):
        print(entry)
        for log in self.logs:
            print(log)
            if log.find(entry):
                return log

    def find_event_source(self, entry):
        print(entry)
        source = ['red','blue','white']
        for log in self.logs:
            path = log.split('/')
            test = path[-2] + "/" + path[-1]
            if test in entry:
                for s in source:
                    if s in path:
                        return s










