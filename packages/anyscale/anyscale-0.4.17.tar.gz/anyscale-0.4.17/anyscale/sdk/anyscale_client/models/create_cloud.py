# coding: utf-8

"""
    Anyscale API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from anyscale_client.configuration import Configuration


class CreateCloud(object):
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
        'name': 'str',
        'provider': 'CloudProviders',
        'region': 'str',
        'credentials': 'str',
        'config': 'CloudConfig',
        'is_k8s': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'provider': 'provider',
        'region': 'region',
        'credentials': 'credentials',
        'config': 'config',
        'is_k8s': 'is_k8s'
    }

    def __init__(self, name=None, provider=None, region=None, credentials=None, config=None, is_k8s=False, local_vars_configuration=None):  # noqa: E501
        """CreateCloud - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._provider = None
        self._region = None
        self._credentials = None
        self._config = None
        self._is_k8s = None
        self.discriminator = None

        self.name = name
        self.provider = provider
        self.region = region
        self.credentials = credentials
        if config is not None:
            self.config = config
        if is_k8s is not None:
            self.is_k8s = is_k8s

    @property
    def name(self):
        """Gets the name of this CreateCloud.  # noqa: E501

        Name of this Cloud.  # noqa: E501

        :return: The name of this CreateCloud.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateCloud.

        Name of this Cloud.  # noqa: E501

        :param name: The name of this CreateCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def provider(self):
        """Gets the provider of this CreateCloud.  # noqa: E501

        Provider of this Cloud (e.g. AWS).  # noqa: E501

        :return: The provider of this CreateCloud.  # noqa: E501
        :rtype: CloudProviders
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this CreateCloud.

        Provider of this Cloud (e.g. AWS).  # noqa: E501

        :param provider: The provider of this CreateCloud.  # noqa: E501
        :type: CloudProviders
        """
        if self.local_vars_configuration.client_side_validation and provider is None:  # noqa: E501
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def region(self):
        """Gets the region of this CreateCloud.  # noqa: E501

        Region this Cloud is operating in. This value needs to be supported by this Cloud's provider. (e.g. us-west-2)  # noqa: E501

        :return: The region of this CreateCloud.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CreateCloud.

        Region this Cloud is operating in. This value needs to be supported by this Cloud's provider. (e.g. us-west-2)  # noqa: E501

        :param region: The region of this CreateCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and region is None:  # noqa: E501
            raise ValueError("Invalid value for `region`, must not be `None`")  # noqa: E501

        self._region = region

    @property
    def credentials(self):
        """Gets the credentials of this CreateCloud.  # noqa: E501

        Credentials needed to interact with this Cloud.  # noqa: E501

        :return: The credentials of this CreateCloud.  # noqa: E501
        :rtype: str
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """Sets the credentials of this CreateCloud.

        Credentials needed to interact with this Cloud.  # noqa: E501

        :param credentials: The credentials of this CreateCloud.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and credentials is None:  # noqa: E501
            raise ValueError("Invalid value for `credentials`, must not be `None`")  # noqa: E501

        self._credentials = credentials

    @property
    def config(self):
        """Gets the config of this CreateCloud.  # noqa: E501

        Additional configurable properties of this Cloud.  # noqa: E501

        :return: The config of this CreateCloud.  # noqa: E501
        :rtype: CloudConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this CreateCloud.

        Additional configurable properties of this Cloud.  # noqa: E501

        :param config: The config of this CreateCloud.  # noqa: E501
        :type: CloudConfig
        """

        self._config = config

    @property
    def is_k8s(self):
        """Gets the is_k8s of this CreateCloud.  # noqa: E501

        Whether this cloud is managed via K8s  # noqa: E501

        :return: The is_k8s of this CreateCloud.  # noqa: E501
        :rtype: bool
        """
        return self._is_k8s

    @is_k8s.setter
    def is_k8s(self, is_k8s):
        """Sets the is_k8s of this CreateCloud.

        Whether this cloud is managed via K8s  # noqa: E501

        :param is_k8s: The is_k8s of this CreateCloud.  # noqa: E501
        :type: bool
        """

        self._is_k8s = is_k8s

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
        if not isinstance(other, CreateCloud):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateCloud):
            return True

        return self.to_dict() != other.to_dict()
