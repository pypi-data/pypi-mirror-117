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


class ExtensionsV1beta1AllowedFlexVolume(object):
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
        'driver': 'str'
    }

    attribute_map = {
        'driver': 'driver'
    }

    def __init__(self, driver=None, local_vars_configuration=None):  # noqa: E501
        """ExtensionsV1beta1AllowedFlexVolume - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._driver = None
        self.discriminator = None

        self.driver = driver

    @property
    def driver(self):
        """Gets the driver of this ExtensionsV1beta1AllowedFlexVolume.  # noqa: E501

        driver is the name of the Flexvolume driver.  # noqa: E501

        :return: The driver of this ExtensionsV1beta1AllowedFlexVolume.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this ExtensionsV1beta1AllowedFlexVolume.

        driver is the name of the Flexvolume driver.  # noqa: E501

        :param driver: The driver of this ExtensionsV1beta1AllowedFlexVolume.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and driver is None:  # noqa: E501
            raise ValueError("Invalid value for `driver`, must not be `None`")  # noqa: E501

        self._driver = driver

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
        if not isinstance(other, ExtensionsV1beta1AllowedFlexVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtensionsV1beta1AllowedFlexVolume):
            return True

        return self.to_dict() != other.to_dict()
