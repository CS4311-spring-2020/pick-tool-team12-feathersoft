
class SignificantLogEntry:

    def __init__(self, log_entry_number, log_entry_timestamp, log_entry_content,
                 host, source, source_type):
        self._log_entry_number = log_entry_number
        self._log_entry_timestamp = log_entry_timestamp
        self._log_entry_content = log_entry_content
        self._host = host
        self._source = source
        self._source_type = source_type
