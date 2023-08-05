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


class AWSNodeOptions(object):
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
        'block_device_mappings': 'list[BlockDeviceMapping]',
        'iam_instance_profile': 'IamInstanceProfileSpecification',
        'security_group_ids': 'list[str]',
        'subnet_id': 'str',
        'tag_specifications': 'list[AWSTagSpecification]',
        'network_interfaces': 'list[NetworkInterface]'
    }

    attribute_map = {
        'block_device_mappings': 'BlockDeviceMappings',
        'iam_instance_profile': 'IamInstanceProfile',
        'security_group_ids': 'SecurityGroupIds',
        'subnet_id': 'SubnetId',
        'tag_specifications': 'TagSpecifications',
        'network_interfaces': 'NetworkInterfaces'
    }

    def __init__(self, block_device_mappings=None, iam_instance_profile=None, security_group_ids=None, subnet_id=None, tag_specifications=None, network_interfaces=None, local_vars_configuration=None):  # noqa: E501
        """AWSNodeOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._block_device_mappings = None
        self._iam_instance_profile = None
        self._security_group_ids = None
        self._subnet_id = None
        self._tag_specifications = None
        self._network_interfaces = None
        self.discriminator = None

        if block_device_mappings is not None:
            self.block_device_mappings = block_device_mappings
        if iam_instance_profile is not None:
            self.iam_instance_profile = iam_instance_profile
        if security_group_ids is not None:
            self.security_group_ids = security_group_ids
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if tag_specifications is not None:
            self.tag_specifications = tag_specifications
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces

    @property
    def block_device_mappings(self):
        """Gets the block_device_mappings of this AWSNodeOptions.  # noqa: E501


        :return: The block_device_mappings of this AWSNodeOptions.  # noqa: E501
        :rtype: list[BlockDeviceMapping]
        """
        return self._block_device_mappings

    @block_device_mappings.setter
    def block_device_mappings(self, block_device_mappings):
        """Sets the block_device_mappings of this AWSNodeOptions.


        :param block_device_mappings: The block_device_mappings of this AWSNodeOptions.  # noqa: E501
        :type: list[BlockDeviceMapping]
        """

        self._block_device_mappings = block_device_mappings

    @property
    def iam_instance_profile(self):
        """Gets the iam_instance_profile of this AWSNodeOptions.  # noqa: E501


        :return: The iam_instance_profile of this AWSNodeOptions.  # noqa: E501
        :rtype: IamInstanceProfileSpecification
        """
        return self._iam_instance_profile

    @iam_instance_profile.setter
    def iam_instance_profile(self, iam_instance_profile):
        """Sets the iam_instance_profile of this AWSNodeOptions.


        :param iam_instance_profile: The iam_instance_profile of this AWSNodeOptions.  # noqa: E501
        :type: IamInstanceProfileSpecification
        """

        self._iam_instance_profile = iam_instance_profile

    @property
    def security_group_ids(self):
        """Gets the security_group_ids of this AWSNodeOptions.  # noqa: E501


        :return: The security_group_ids of this AWSNodeOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._security_group_ids

    @security_group_ids.setter
    def security_group_ids(self, security_group_ids):
        """Sets the security_group_ids of this AWSNodeOptions.


        :param security_group_ids: The security_group_ids of this AWSNodeOptions.  # noqa: E501
        :type: list[str]
        """

        self._security_group_ids = security_group_ids

    @property
    def subnet_id(self):
        """Gets the subnet_id of this AWSNodeOptions.  # noqa: E501


        :return: The subnet_id of this AWSNodeOptions.  # noqa: E501
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this AWSNodeOptions.


        :param subnet_id: The subnet_id of this AWSNodeOptions.  # noqa: E501
        :type: str
        """

        self._subnet_id = subnet_id

    @property
    def tag_specifications(self):
        """Gets the tag_specifications of this AWSNodeOptions.  # noqa: E501


        :return: The tag_specifications of this AWSNodeOptions.  # noqa: E501
        :rtype: list[AWSTagSpecification]
        """
        return self._tag_specifications

    @tag_specifications.setter
    def tag_specifications(self, tag_specifications):
        """Sets the tag_specifications of this AWSNodeOptions.


        :param tag_specifications: The tag_specifications of this AWSNodeOptions.  # noqa: E501
        :type: list[AWSTagSpecification]
        """

        self._tag_specifications = tag_specifications

    @property
    def network_interfaces(self):
        """Gets the network_interfaces of this AWSNodeOptions.  # noqa: E501

        The network interfaces to associate with the instance. If you specify a network interface, you must specify any security groups and subnets as part of the network interface.  # noqa: E501

        :return: The network_interfaces of this AWSNodeOptions.  # noqa: E501
        :rtype: list[NetworkInterface]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        """Sets the network_interfaces of this AWSNodeOptions.

        The network interfaces to associate with the instance. If you specify a network interface, you must specify any security groups and subnets as part of the network interface.  # noqa: E501

        :param network_interfaces: The network_interfaces of this AWSNodeOptions.  # noqa: E501
        :type: list[NetworkInterface]
        """

        self._network_interfaces = network_interfaces

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
        if not isinstance(other, AWSNodeOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AWSNodeOptions):
            return True

        return self.to_dict() != other.to_dict()
