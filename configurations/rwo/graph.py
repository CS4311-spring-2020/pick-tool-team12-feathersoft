
class Graph:

    """
        Class used to represent a graph object for the PICK PMR tool.
        Attributes:
        _export_format: Format in which the graph image will be exported
        _orientation: The method in which the graph will be displayed
        _interval_units:
        _interval:
        _position_of_nodes:
        _position_of_relationships:

    """

    def __init__(self, export_format, orientation, interval_units, interval, position_of_nodes,
                 position_of_relationships):
        """

        :param export_format:
        :param orientation:
        :param interval_units:
        :param interval:
        :param position_of_nodes:
        :param position_of_relationships:
        """
        self._export_format = export_format
        self._orientation = orientation
        self._interval_units = interval_units
        self._interval = interval
        self._position_of_nodes = position_of_nodes
        self._position_of_relationships = position_of_relationships
