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


class V1CustomResourceColumnDefinition(object):
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
        'description': 'str',
        'format': 'str',
        'json_path': 'str',
        'name': 'str',
        'priority': 'int',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'format': 'format',
        'json_path': 'jsonPath',
        'name': 'name',
        'priority': 'priority',
        'type': 'type'
    }

    def __init__(self, description=None, format=None, json_path=None, name=None, priority=None, type=None, local_vars_configuration=None):  # noqa: E501
        """V1CustomResourceColumnDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._format = None
        self._json_path = None
        self._name = None
        self._priority = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if format is not None:
            self.format = format
        self.json_path = json_path
        self.name = name
        if priority is not None:
            self.priority = priority
        self.type = type

    @property
    def description(self):
        """Gets the description of this V1CustomResourceColumnDefinition.  # noqa: E501

        description is a human readable description of this column.  # noqa: E501

        :return: The description of this V1CustomResourceColumnDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this V1CustomResourceColumnDefinition.

        description is a human readable description of this column.  # noqa: E501

        :param description: The description of this V1CustomResourceColumnDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def format(self):
        """Gets the format of this V1CustomResourceColumnDefinition.  # noqa: E501

        format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.  # noqa: E501

        :return: The format of this V1CustomResourceColumnDefinition.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this V1CustomResourceColumnDefinition.

        format is an optional OpenAPI type definition for this column. The 'name' format is applied to the primary identifier column to assist in clients identifying column is the resource name. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.  # noqa: E501

        :param format: The format of this V1CustomResourceColumnDefinition.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def json_path(self):
        """Gets the json_path of this V1CustomResourceColumnDefinition.  # noqa: E501

        jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column.  # noqa: E501

        :return: The json_path of this V1CustomResourceColumnDefinition.  # noqa: E501
        :rtype: str
        """
        return self._json_path

    @json_path.setter
    def json_path(self, json_path):
        """Sets the json_path of this V1CustomResourceColumnDefinition.

        jsonPath is a simple JSON path (i.e. with array notation) which is evaluated against each custom resource to produce the value for this column.  # noqa: E501

        :param json_path: The json_path of this V1CustomResourceColumnDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and json_path is None:  # noqa: E501
            raise ValueError("Invalid value for `json_path`, must not be `None`")  # noqa: E501

        self._json_path = json_path

    @property
    def name(self):
        """Gets the name of this V1CustomResourceColumnDefinition.  # noqa: E501

        name is a human readable name for the column.  # noqa: E501

        :return: The name of this V1CustomResourceColumnDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this V1CustomResourceColumnDefinition.

        name is a human readable name for the column.  # noqa: E501

        :param name: The name of this V1CustomResourceColumnDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def priority(self):
        """Gets the priority of this V1CustomResourceColumnDefinition.  # noqa: E501

        priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0.  # noqa: E501

        :return: The priority of this V1CustomResourceColumnDefinition.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this V1CustomResourceColumnDefinition.

        priority is an integer defining the relative importance of this column compared to others. Lower numbers are considered higher priority. Columns that may be omitted in limited space scenarios should be given a priority greater than 0.  # noqa: E501

        :param priority: The priority of this V1CustomResourceColumnDefinition.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def type(self):
        """Gets the type of this V1CustomResourceColumnDefinition.  # noqa: E501

        type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.  # noqa: E501

        :return: The type of this V1CustomResourceColumnDefinition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this V1CustomResourceColumnDefinition.

        type is an OpenAPI type definition for this column. See https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md#data-types for details.  # noqa: E501

        :param type: The type of this V1CustomResourceColumnDefinition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if not isinstance(other, V1CustomResourceColumnDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CustomResourceColumnDefinition):
            return True

        return self.to_dict() != other.to_dict()
