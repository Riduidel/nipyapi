# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.5.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Link(object):
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
        'type': 'str',
        'rels': 'list[str]',
        'uri': 'str',
        'params': 'dict(str, str)',
        'title': 'str',
        'uri_builder': 'UriBuilder',
        'rel': 'str'
    }

    attribute_map = {
        'type': 'type',
        'rels': 'rels',
        'uri': 'uri',
        'params': 'params',
        'title': 'title',
        'uri_builder': 'uriBuilder',
        'rel': 'rel'
    }

    def __init__(self, type=None, rels=None, uri=None, params=None, title=None, uri_builder=None, rel=None):
        """
        Link - a model defined in Swagger
        """

        self._type = None
        self._rels = None
        self._uri = None
        self._params = None
        self._title = None
        self._uri_builder = None
        self._rel = None

        if type is not None:
          self.type = type
        if rels is not None:
          self.rels = rels
        if uri is not None:
          self.uri = uri
        if params is not None:
          self.params = params
        if title is not None:
          self.title = title
        if uri_builder is not None:
          self.uri_builder = uri_builder
        if rel is not None:
          self.rel = rel

    @property
    def type(self):
        """
        Gets the type of this Link.

        :return: The type of this Link.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Link.

        :param type: The type of this Link.
        :type: str
        """

        self._type = type

    @property
    def rels(self):
        """
        Gets the rels of this Link.

        :return: The rels of this Link.
        :rtype: list[str]
        """
        return self._rels

    @rels.setter
    def rels(self, rels):
        """
        Sets the rels of this Link.

        :param rels: The rels of this Link.
        :type: list[str]
        """

        self._rels = rels

    @property
    def uri(self):
        """
        Gets the uri of this Link.

        :return: The uri of this Link.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Link.

        :param uri: The uri of this Link.
        :type: str
        """

        self._uri = uri

    @property
    def params(self):
        """
        Gets the params of this Link.

        :return: The params of this Link.
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this Link.

        :param params: The params of this Link.
        :type: dict(str, str)
        """

        self._params = params

    @property
    def title(self):
        """
        Gets the title of this Link.

        :return: The title of this Link.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Link.

        :param title: The title of this Link.
        :type: str
        """

        self._title = title

    @property
    def uri_builder(self):
        """
        Gets the uri_builder of this Link.

        :return: The uri_builder of this Link.
        :rtype: UriBuilder
        """
        return self._uri_builder

    @uri_builder.setter
    def uri_builder(self, uri_builder):
        """
        Sets the uri_builder of this Link.

        :param uri_builder: The uri_builder of this Link.
        :type: UriBuilder
        """

        self._uri_builder = uri_builder

    @property
    def rel(self):
        """
        Gets the rel of this Link.

        :return: The rel of this Link.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """
        Sets the rel of this Link.

        :param rel: The rel of this Link.
        :type: str
        """

        self._rel = rel

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
        if not isinstance(other, Link):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other