
class EnforcementActionReport:

    """
        An enforcement action report is responsible for storing where errors occur in a log file and why they failed
        the validation test.

        Attributes:
            _line_number:(str) The location of where an error occurs in a log file.
            _error_message:(str) Explanation of why a specific line in the log file fails validation test.

    """

    def __init__(self, line_number, error_message):
        """
        :param line_number:(str) The location of where an error occurs in a log file.
        :param error_message:(str) Explanation of why a specific line in the log file fails validation test.
        """
        self._line_number = line_number
        self._error_message = error_message


