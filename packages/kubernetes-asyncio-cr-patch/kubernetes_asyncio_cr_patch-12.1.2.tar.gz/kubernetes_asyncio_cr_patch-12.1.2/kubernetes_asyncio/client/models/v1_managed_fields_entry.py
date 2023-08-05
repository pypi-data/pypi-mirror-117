# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.16.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes_asyncio.client.configuration import Configuration


class V1ManagedFieldsEntry(object):
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
        'api_version': 'str',
        'fields_type': 'str',
        'fields_v1': 'object',
        'manager': 'str',
        'operation': 'str',
        'time': 'datetime'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'fields_type': 'fieldsType',
        'fields_v1': 'fieldsV1',
        'manager': 'manager',
        'operation': 'operation',
        'time': 'time'
    }

    def __init__(self, api_version=None, fields_type=None, fields_v1=None, manager=None, operation=None, time=None, local_vars_configuration=None):  # noqa: E501
        """V1ManagedFieldsEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._fields_type = None
        self._fields_v1 = None
        self._manager = None
        self._operation = None
        self._time = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if fields_type is not None:
            self.fields_type = fields_type
        if fields_v1 is not None:
            self.fields_v1 = fields_v1
        if manager is not None:
            self.manager = manager
        if operation is not None:
            self.operation = operation
        if time is not None:
            self.time = time

    @property
    def api_version(self):
        """Gets the api_version of this V1ManagedFieldsEntry.  # noqa: E501

        APIVersion defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.  # noqa: E501

        :return: The api_version of this V1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1ManagedFieldsEntry.

        APIVersion defines the version of this resource that this field set applies to. The format is \"group/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted.  # noqa: E501

        :param api_version: The api_version of this V1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def fields_type(self):
        """Gets the fields_type of this V1ManagedFieldsEntry.  # noqa: E501

        FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: \"FieldsV1\"  # noqa: E501

        :return: The fields_type of this V1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._fields_type

    @fields_type.setter
    def fields_type(self, fields_type):
        """Sets the fields_type of this V1ManagedFieldsEntry.

        FieldsType is the discriminator for the different fields format and version. There is currently only one possible value: \"FieldsV1\"  # noqa: E501

        :param fields_type: The fields_type of this V1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._fields_type = fields_type

    @property
    def fields_v1(self):
        """Gets the fields_v1 of this V1ManagedFieldsEntry.  # noqa: E501

        FieldsV1 holds the first JSON version format as described in the \"FieldsV1\" type.  # noqa: E501

        :return: The fields_v1 of this V1ManagedFieldsEntry.  # noqa: E501
        :rtype: object
        """
        return self._fields_v1

    @fields_v1.setter
    def fields_v1(self, fields_v1):
        """Sets the fields_v1 of this V1ManagedFieldsEntry.

        FieldsV1 holds the first JSON version format as described in the \"FieldsV1\" type.  # noqa: E501

        :param fields_v1: The fields_v1 of this V1ManagedFieldsEntry.  # noqa: E501
        :type: object
        """

        self._fields_v1 = fields_v1

    @property
    def manager(self):
        """Gets the manager of this V1ManagedFieldsEntry.  # noqa: E501

        Manager is an identifier of the workflow managing these fields.  # noqa: E501

        :return: The manager of this V1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this V1ManagedFieldsEntry.

        Manager is an identifier of the workflow managing these fields.  # noqa: E501

        :param manager: The manager of this V1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._manager = manager

    @property
    def operation(self):
        """Gets the operation of this V1ManagedFieldsEntry.  # noqa: E501

        Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.  # noqa: E501

        :return: The operation of this V1ManagedFieldsEntry.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this V1ManagedFieldsEntry.

        Operation is the type of operation which lead to this ManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'.  # noqa: E501

        :param operation: The operation of this V1ManagedFieldsEntry.  # noqa: E501
        :type: str
        """

        self._operation = operation

    @property
    def time(self):
        """Gets the time of this V1ManagedFieldsEntry.  # noqa: E501

        Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'  # noqa: E501

        :return: The time of this V1ManagedFieldsEntry.  # noqa: E501
        :rtype: datetime
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this V1ManagedFieldsEntry.

        Time is timestamp of when these fields were set. It should always be empty if Operation is 'Apply'  # noqa: E501

        :param time: The time of this V1ManagedFieldsEntry.  # noqa: E501
        :type: datetime
        """

        self._time = time

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
        if not isinstance(other, V1ManagedFieldsEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ManagedFieldsEntry):
            return True

        return self.to_dict() != other.to_dict()
