# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.9.1
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClusterSummaryDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'connected_nodes': 'str',
        'connected_node_count': 'int',
        'total_node_count': 'int',
        'clustered': 'bool',
        'connected_to_cluster': 'bool'
    }

    attribute_map = {
        'connected_nodes': 'connectedNodes',
        'connected_node_count': 'connectedNodeCount',
        'total_node_count': 'totalNodeCount',
        'clustered': 'clustered',
        'connected_to_cluster': 'connectedToCluster'
    }

    def __init__(self, connected_nodes=None, connected_node_count=None, total_node_count=None, clustered=None, connected_to_cluster=None):
        """
        ClusterSummaryDTO - a model defined in Swagger
        """

        self._connected_nodes = None
        self._connected_node_count = None
        self._total_node_count = None
        self._clustered = None
        self._connected_to_cluster = None

        if connected_nodes is not None:
          self.connected_nodes = connected_nodes
        if connected_node_count is not None:
          self.connected_node_count = connected_node_count
        if total_node_count is not None:
          self.total_node_count = total_node_count
        if clustered is not None:
          self.clustered = clustered
        if connected_to_cluster is not None:
          self.connected_to_cluster = connected_to_cluster

    @property
    def connected_nodes(self):
        """
        Gets the connected_nodes of this ClusterSummaryDTO.
        When clustered, reports the number of nodes connected vs the number of nodes in the cluster.

        :return: The connected_nodes of this ClusterSummaryDTO.
        :rtype: str
        """
        return self._connected_nodes

    @connected_nodes.setter
    def connected_nodes(self, connected_nodes):
        """
        Sets the connected_nodes of this ClusterSummaryDTO.
        When clustered, reports the number of nodes connected vs the number of nodes in the cluster.

        :param connected_nodes: The connected_nodes of this ClusterSummaryDTO.
        :type: str
        """

        self._connected_nodes = connected_nodes

    @property
    def connected_node_count(self):
        """
        Gets the connected_node_count of this ClusterSummaryDTO.
        The number of nodes that are currently connected to the cluster

        :return: The connected_node_count of this ClusterSummaryDTO.
        :rtype: int
        """
        return self._connected_node_count

    @connected_node_count.setter
    def connected_node_count(self, connected_node_count):
        """
        Sets the connected_node_count of this ClusterSummaryDTO.
        The number of nodes that are currently connected to the cluster

        :param connected_node_count: The connected_node_count of this ClusterSummaryDTO.
        :type: int
        """

        self._connected_node_count = connected_node_count

    @property
    def total_node_count(self):
        """
        Gets the total_node_count of this ClusterSummaryDTO.
        The number of nodes in the cluster, regardless of whether or not they are connected

        :return: The total_node_count of this ClusterSummaryDTO.
        :rtype: int
        """
        return self._total_node_count

    @total_node_count.setter
    def total_node_count(self, total_node_count):
        """
        Sets the total_node_count of this ClusterSummaryDTO.
        The number of nodes in the cluster, regardless of whether or not they are connected

        :param total_node_count: The total_node_count of this ClusterSummaryDTO.
        :type: int
        """

        self._total_node_count = total_node_count

    @property
    def clustered(self):
        """
        Gets the clustered of this ClusterSummaryDTO.
        Whether this NiFi instance is clustered.

        :return: The clustered of this ClusterSummaryDTO.
        :rtype: bool
        """
        return self._clustered

    @clustered.setter
    def clustered(self, clustered):
        """
        Sets the clustered of this ClusterSummaryDTO.
        Whether this NiFi instance is clustered.

        :param clustered: The clustered of this ClusterSummaryDTO.
        :type: bool
        """

        self._clustered = clustered

    @property
    def connected_to_cluster(self):
        """
        Gets the connected_to_cluster of this ClusterSummaryDTO.
        Whether this NiFi instance is connected to a cluster.

        :return: The connected_to_cluster of this ClusterSummaryDTO.
        :rtype: bool
        """
        return self._connected_to_cluster

    @connected_to_cluster.setter
    def connected_to_cluster(self, connected_to_cluster):
        """
        Sets the connected_to_cluster of this ClusterSummaryDTO.
        Whether this NiFi instance is connected to a cluster.

        :param connected_to_cluster: The connected_to_cluster of this ClusterSummaryDTO.
        :type: bool
        """

        self._connected_to_cluster = connected_to_cluster

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ClusterSummaryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
