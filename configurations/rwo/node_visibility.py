
class NodeVisibility:

    """

    """

    def __init__(self,node_visibility, node_id_visibility, node_name_visibility,node_timestamp_visibility,
                 node_description_visibility,log_entry_reference_visibility, log_creator_visibility,
                 event_type_visibility, icon_type_visibility, source_visibility):

        """

        :param node_visibility:
        :param node_id_visibility:
        :param node_name_visibility:
        :param node_timestamp_visibility:
        :param node_description_visibility:
        :param log_entry_reference_visibility:
        :param log_creator_visibility:
        :param event_type_visibility:
        :param icon_type_visibility:
        :param source_visibility:
        """
        self._node_visibility = node_visibility
        self._node_id_visibility = node_id_visibility
        self._node_name_visibility = node_name_visibility
        self._node_timestamp_visibility = node_timestamp_visibility
        self._node_description_visibility = node_description_visibility
        self._log_entry_reference_visibility = log_entry_reference_visibility
        self._log_creator_visibility = log_creator_visibility
        self._event_type_visibility = event_type_visibility
        self._icon_type_visibility = icon_type_visibility
        self._source_visibility = source_visibility
