# coding: utf-8

"""
    Managed Ray API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class InstanceInternalIP(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instance_id': 'str',
        'internal_ip': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'internal_ip': 'internal_ip'
    }

    def __init__(self, instance_id=None, internal_ip=None, local_vars_configuration=None):  # noqa: E501
        """InstanceInternalIP - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instance_id = None
        self._internal_ip = None
        self.discriminator = None

        self.instance_id = instance_id
        if internal_ip is not None:
            self.internal_ip = internal_ip

    @property
    def instance_id(self):
        """Gets the instance_id of this InstanceInternalIP.  # noqa: E501


        :return: The instance_id of this InstanceInternalIP.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this InstanceInternalIP.


        :param instance_id: The instance_id of this InstanceInternalIP.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def internal_ip(self):
        """Gets the internal_ip of this InstanceInternalIP.  # noqa: E501


        :return: The internal_ip of this InstanceInternalIP.  # noqa: E501
        :rtype: str
        """
        return self._internal_ip

    @internal_ip.setter
    def internal_ip(self, internal_ip):
        """Sets the internal_ip of this InstanceInternalIP.


        :param internal_ip: The internal_ip of this InstanceInternalIP.  # noqa: E501
        :type: str
        """

        self._internal_ip = internal_ip

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstanceInternalIP):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceInternalIP):
            return True

        return self.to_dict() != other.to_dict()
