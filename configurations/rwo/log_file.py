
class LogFile:

    """
    The log file class represents a log file that is to be ingested into the system.
        Attributes:
            _name:(str) The name of a log file.
            _cleansing_status:(bool) The cleansing status of a log file.
            _validation_status:(bool) The validation status of a log file.
            _ingestion_status:(bool) The ingestion status of a log file.
            _acknowledgement_status:(bool) The acknowledgement status of a log file.
    """

    def __init__(self,name, cleansing_status, validation_status, ingestion_status, acknowledgement_status):
        """
        :param name: The name of a log file.
        :param cleansing_status: The cleansing status of a log file.
        :param validation_status: The validation status of a log file.
        :param ingestion_status: The ingestion status of a log.
        :param acknowledgement_status: The acknowledgement status of a log file.
        """
        self._name = name
        self._cleansing_status = cleansing_status
        self._validation_status = validation_status
        self._ingestion_status = ingestion_status
        self._acknowledgement_status = acknowledgement_status

    @property
    def get_name(self):
        return self._name

    @property
    def get_cleansing_status(self):
        return self._cleansing_status

    @property
    def get_validation_status(self):
        return self._validation_status

    @property
    def get_ingestion_status(self):
        return self._ingestion_status

    @property
    def get_acknowledgement_status(self):
        return self._acknowledgement_status


