
class NodeVisibility:

    """

    """

    def __init__(self, **kwargs):
        """

        :param kwargs:
        """
        self._node_visibility = kwargs['node_visibility']
        self._node_id_visibility = kwargs['node_id_visibility']
        self._node_name_visibility = kwargs['node_name_visibility']
        self._node_timestamp_visibility = kwargs['node_timestamp_visibility']
        self._node_description_visibility = kwargs['node_description_visibility']
        self._log_entry_reference_visibility = kwargs['log_entry_reference_visibility']
        self._log_creator_visibility = kwargs['log_creator_visibility']
        self._event_type_visibility = kwargs['event_type_visibility']
        self._icon_type_visibility = kwargs['icon_type_visibility']
        self._source_visibility = kwargs['source_visibility']
