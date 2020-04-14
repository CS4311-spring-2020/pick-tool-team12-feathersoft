
class SignificantLogEntry:

    """
    The significant log entry class represents a log entry created by Splunk to be associated to a vector by a user.
    Attributes:
        _log_entry_number: (int) Unique identifier of a log entry.
        _log_entry_timestamp: (str) The time and date of when the activity described by the log entry took
         place.
        _log_entry_content: (str) The description of the activity.
        _host:(str) IP Address.
        _source: (str) The name and location from which a particular activity originates.
        _source_type: (str) Refers to how the Splunk software processes the incoming data stream into individual
        _activities according to the nature of the data.
        _vectors: The set of vectors that the entry belongs to

    """

    def __init__(self, log_entry_number, log_entry_timestamp, log_entry_content,
                 host, source, source_type):
        """
        :param log_entry_number: (int) Unique identifier of a log entry.
        :param log_entry_timestamp: (str) The time and date of when the activity described by the log entry took
        place.
        :param log_entry_content: (str) The description of the activity.
        :param host:(str) IP Address.
        :param source (str): The name and location from which a particular activity originates.
        :param source_type (str): Refers to how the Splunk software processes the incoming data.
        stream into individual activities according to the nature of the data.
        """
        self._log_entry_number = log_entry_number
        self._log_entry_timestamp = log_entry_timestamp
        self._log_entry_content = log_entry_content
        self._host = host
        self._source = source
        self._source_type = source_type
        self._vectors = set()

    @property
    def get_log_entry_number(self):
        return self._log_entry_number

    @property
    def get_log_entry_timestamp(self):
        return self._log_entry_timestamp

    @property
    def get_log_entry_content(self):
        return self._log_entry_content

    @property
    def get_host(self):
        return self._host

    @property
    def get_source(self):
        return self._source

    @property
    def get_source_type(self):
        return self._source_type

    def __str__(self):
        return f"Number: {self._log_entry_number} \nTimestamp: {self._log_entry_timestamp} + \n + Content: {self._log_entry_content} \n " \
               f"Host: {self._host}\n Source: {self._source}\n Source Type {self._source_type}"
