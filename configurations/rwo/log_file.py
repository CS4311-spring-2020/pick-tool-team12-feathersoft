
class LogFile:

    def __int__(self, cleansing_status, validation_status, ingestion_status,
                acknowledgement_status):
        """

        :param cleansing_status:
        :param validation_status:
        :param ingestion_status:
        :param acknowledgement_status:
        :return:
        """
        self._cleansing_status = cleansing_status
        self._validation_status = validation_status
        self._ingestion_status = ingestion_status
        self._acknowledgement_status = acknowledgement_status


