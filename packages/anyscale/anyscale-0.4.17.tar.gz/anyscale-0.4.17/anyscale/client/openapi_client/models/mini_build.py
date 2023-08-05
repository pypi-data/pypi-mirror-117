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


class MiniBuild(object):
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
        'id': 'str',
        'revision': 'int',
        'status': 'BuildStatus',
        'application_template_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'revision': 'revision',
        'status': 'status',
        'application_template_name': 'application_template_name'
    }

    def __init__(self, id=None, revision=None, status=None, application_template_name=None, local_vars_configuration=None):  # noqa: E501
        """MiniBuild - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._revision = None
        self._status = None
        self._application_template_name = None
        self.discriminator = None

        self.id = id
        self.revision = revision
        self.status = status
        self.application_template_name = application_template_name

    @property
    def id(self):
        """Gets the id of this MiniBuild.  # noqa: E501

        Server assigned unique identifier.  # noqa: E501

        :return: The id of this MiniBuild.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MiniBuild.

        Server assigned unique identifier.  # noqa: E501

        :param id: The id of this MiniBuild.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def revision(self):
        """Gets the revision of this MiniBuild.  # noqa: E501

        Auto incrementing version number for this Build  # noqa: E501

        :return: The revision of this MiniBuild.  # noqa: E501
        :rtype: int
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this MiniBuild.

        Auto incrementing version number for this Build  # noqa: E501

        :param revision: The revision of this MiniBuild.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and revision is None:  # noqa: E501
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def status(self):
        """Gets the status of this MiniBuild.  # noqa: E501

             Status of the Build.      `pending` - Build operation is queued and has not started yet.     `in_progress` - Build operation is in progress.     `succeeded` - Build operation completed successfully.     `failed` - Build operation completed unsuccessfully.     `pending_cancellation` - Build operation is marked for cancellation.     `cancelled` - Build operation was cancelled before it completed.       # noqa: E501

        :return: The status of this MiniBuild.  # noqa: E501
        :rtype: BuildStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MiniBuild.

             Status of the Build.      `pending` - Build operation is queued and has not started yet.     `in_progress` - Build operation is in progress.     `succeeded` - Build operation completed successfully.     `failed` - Build operation completed unsuccessfully.     `pending_cancellation` - Build operation is marked for cancellation.     `cancelled` - Build operation was cancelled before it completed.       # noqa: E501

        :param status: The status of this MiniBuild.  # noqa: E501
        :type: BuildStatus
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def application_template_name(self):
        """Gets the application_template_name of this MiniBuild.  # noqa: E501

        The name of the App Config this build belongs to  # noqa: E501

        :return: The application_template_name of this MiniBuild.  # noqa: E501
        :rtype: str
        """
        return self._application_template_name

    @application_template_name.setter
    def application_template_name(self, application_template_name):
        """Sets the application_template_name of this MiniBuild.

        The name of the App Config this build belongs to  # noqa: E501

        :param application_template_name: The application_template_name of this MiniBuild.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and application_template_name is None:  # noqa: E501
            raise ValueError("Invalid value for `application_template_name`, must not be `None`")  # noqa: E501

        self._application_template_name = application_template_name

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
        if not isinstance(other, MiniBuild):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MiniBuild):
            return True

        return self.to_dict() != other.to_dict()
