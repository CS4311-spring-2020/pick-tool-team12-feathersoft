
class LogFile:

    def __int__(self,name, cleansing_status, validation_status, ingestion_status,
                acknowledgement_status):
        """
        :param name: The name of a log file.
        :param cleansing_status: The cleansing status of a log file
        :param validation_status: The validation status of a log file
        :param ingestion_status: The ingestion status of a log
        :param acknowledgement_status:
        :return:
        """
        self._cleansing_status = cleansing_status
        self._validation_status = validation_status
        self._ingestion_status = ingestion_status
        self._acknowledgement_status = acknowledgement_status


