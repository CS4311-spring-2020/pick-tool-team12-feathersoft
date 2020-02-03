
class Graph:

    def __init__(self, export_format, orientation, interval_units, interval, position_of_nodes,
                 position_of_relationships):

        self._export_format = export_format
        self._orientation = orientation
        self._interval_units = interval_units
        self._interval = interval
        self._position_of_nodes = position_of_nodes
        self._position_of_relationships = position_of_relationships
