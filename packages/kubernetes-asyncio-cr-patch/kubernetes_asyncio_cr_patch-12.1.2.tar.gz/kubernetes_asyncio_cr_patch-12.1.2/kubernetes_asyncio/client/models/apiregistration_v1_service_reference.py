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


class ApiregistrationV1ServiceReference(object):
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
        'namespace': 'str',
        'port': 'int'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'port': 'port'
    }

    def __init__(self, name=None, namespace=None, port=None, local_vars_configuration=None):  # noqa: E501
        """ApiregistrationV1ServiceReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._namespace = None
        self._port = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if namespace is not None:
            self.namespace = namespace
        if port is not None:
            self.port = port

    @property
    def name(self):
        """Gets the name of this ApiregistrationV1ServiceReference.  # noqa: E501

        Name is the name of the service  # noqa: E501

        :return: The name of this ApiregistrationV1ServiceReference.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiregistrationV1ServiceReference.

        Name is the name of the service  # noqa: E501

        :param name: The name of this ApiregistrationV1ServiceReference.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this ApiregistrationV1ServiceReference.  # noqa: E501

        Namespace is the namespace of the service  # noqa: E501

        :return: The namespace of this ApiregistrationV1ServiceReference.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ApiregistrationV1ServiceReference.

        Namespace is the namespace of the service  # noqa: E501

        :param namespace: The namespace of this ApiregistrationV1ServiceReference.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def port(self):
        """Gets the port of this ApiregistrationV1ServiceReference.  # noqa: E501

        If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).  # noqa: E501

        :return: The port of this ApiregistrationV1ServiceReference.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ApiregistrationV1ServiceReference.

        If specified, the port on the service that hosting webhook. Default to 443 for backward compatibility. `port` should be a valid port number (1-65535, inclusive).  # noqa: E501

        :param port: The port of this ApiregistrationV1ServiceReference.  # noqa: E501
        :type: int
        """

        self._port = port

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
        if not isinstance(other, ApiregistrationV1ServiceReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiregistrationV1ServiceReference):
            return True

        return self.to_dict() != other.to_dict()
