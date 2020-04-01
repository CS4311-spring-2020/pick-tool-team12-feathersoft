
class LogFile:

    def __init__(self,name, cleansing_status, validation_status, ingestion_status,
                acknowledgement_status):
        """
        :param name: The name of a log file.
        :param cleansing_status: The cleansing status of a log file
        :param validation_status: The validation status of a log file
        :param ingestion_status: The ingestion status of a log
        :param acknowledgement_status:
        :return:
        """
        self.name = name
        self.cleansing_status = cleansing_status
        self.validation_status = validation_status
        self.ingestion_status = ingestion_status
        self.acknowledgement_status = acknowledgement_status


