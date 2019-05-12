# coding: utf-8

"""
    Cloudera Edge Flow Manager REST API

    This REST API provides remote access to the EFM Server.                                             Endpoints that are marked as [BETA] are subject to change in future releases of the application without backwards compatibility and without a major version change.

    OpenAPI spec version: 1.0.0-SNAPSHOT
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class NiFiRegistryInfo(object):
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
        'base_url': 'str',
        'bucket_id': 'str',
        'bucket_name': 'str'
    }

    attribute_map = {
        'base_url': 'baseUrl',
        'bucket_id': 'bucketId',
        'bucket_name': 'bucketName'
    }

    def __init__(self, base_url=None, bucket_id=None, bucket_name=None):
        """
        NiFiRegistryInfo - a model defined in Swagger
        """

        self._base_url = None
        self._bucket_id = None
        self._bucket_name = None

        if base_url is not None:
          self.base_url = base_url
        if bucket_id is not None:
          self.bucket_id = bucket_id
        if bucket_name is not None:
          self.bucket_name = bucket_name

    @property
    def base_url(self):
        """
        Gets the base_url of this NiFiRegistryInfo.
        The base url of the NiFi Registry instance that this C2 server is configured with

        :return: The base_url of this NiFiRegistryInfo.
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """
        Sets the base_url of this NiFiRegistryInfo.
        The base url of the NiFi Registry instance that this C2 server is configured with

        :param base_url: The base_url of this NiFiRegistryInfo.
        :type: str
        """

        self._base_url = base_url

    @property
    def bucket_id(self):
        """
        Gets the bucket_id of this NiFiRegistryInfo.
        The bucket id in the NiFi Registry instance that this C2 server is configured with. Only one of bucket id or bucket name will be populated.

        :return: The bucket_id of this NiFiRegistryInfo.
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """
        Sets the bucket_id of this NiFiRegistryInfo.
        The bucket id in the NiFi Registry instance that this C2 server is configured with. Only one of bucket id or bucket name will be populated.

        :param bucket_id: The bucket_id of this NiFiRegistryInfo.
        :type: str
        """

        self._bucket_id = bucket_id

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this NiFiRegistryInfo.
        The bucket name in the NiFi Registry that this C2 server is configured with. Only one of bucket id or bucket name will be populated.

        :return: The bucket_name of this NiFiRegistryInfo.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this NiFiRegistryInfo.
        The bucket name in the NiFi Registry that this C2 server is configured with. Only one of bucket id or bucket name will be populated.

        :param bucket_name: The bucket_name of this NiFiRegistryInfo.
        :type: str
        """

        self._bucket_name = bucket_name

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
        if not isinstance(other, NiFiRegistryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other