
class SignificantLogEntry:

    def __init__(self, log_entry_number, log_entry_timestamp, log_entry_content,
                 host, source, source_type):
        """

        :param log_entry_number:
        :param log_entry_timestamp:
        :param log_entry_content:
        :param host:
        :param source:
        :param source_type:
        """
        self._log_entry_number = log_entry_number
        self._log_entry_timestamp = log_entry_timestamp
        self._log_entry_content = log_entry_content
        self._host = host
        self._source = source
        self._source_type = source_type

    def display(self):
        print(f"Log Entry Number: {self._log_entry_number}")
        print(f"Log Entry Timestamp: {self._log_entry_timestamp}")
        print(f"Log Entry Content:{self._log_entry_content}")
        print(f"Host: {self._host}")
        print(f"Source: {self._source}")
        print(f"Source Type{self._source_type}")

    def get_log_entry_number(self):
        return self._log_entry_number

    def get_log_entry_timestamp(self):
        return self._log_entry_timestamp

    def get_log_entry_content(self):
        return self._log_entry_content

    def get_host(self):
        return self._host

    def get_source(self):
        return self._source

    def get_source_type(self):
        return self._source_type

