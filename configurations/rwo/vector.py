
class Vector:
    """

    """

    def __init__(self, vector_name, vector_description):
        """

        :param vector_name:
        :param vector_description:
        """
        self._vector_name = vector_name
        self._vector_description = vector_description

    @property
    def get_vector_name(self):
        return self._vector_name

    @property
    def get_vector_description(self):
        return self._vector_description

