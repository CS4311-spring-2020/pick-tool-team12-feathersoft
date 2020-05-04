
class Node:

    """

    """

    def __init__(self, node_id, node_name, node_timestamp, node_description, log_entry_reference, log_creator,
                 event_type,icon_type,source,visibility):

        self._node_id = node_id
        self._node_name = node_name
        self._node_timestamp = node_timestamp
        self._node_description = node_description
        self._log_entry_reference = log_entry_reference
        self._log_creator = log_creator
        self._event_type = event_type
        self._icon_type = icon_type
        self._source = source
        self._visibility = visibility

    @property
    def get_node_id(self):
        return self._node_id

    @property
    def get_node_name(self):
        return self._node_name

    @property
    def get_node_timestamp(self):
        return self._node_timestamp

    @property
    def get_node_description(self):
        return self._node_description

    @property
    def get_log_entry_reference(self):
        return self._log_entry_reference

    @property
    def get_log_creator(self):
        return self._log_creator

    @property
    def get_event_type(self):
        return self._event_type

    @property
    def get_icon_type(self):
        return self._icon_type

    @property
    def get_source(self):
        return self._source

    @property
    def get_visibility(self):
        return self._visibility





