

class EventConfiguration:

    def __init__(self, **kwargs):
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







