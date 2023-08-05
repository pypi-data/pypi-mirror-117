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


class V1ServiceStatus(object):
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
        'load_balancer': 'V1LoadBalancerStatus'
    }

    attribute_map = {
        'load_balancer': 'loadBalancer'
    }

    def __init__(self, load_balancer=None, local_vars_configuration=None):  # noqa: E501
        """V1ServiceStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._load_balancer = None
        self.discriminator = None

        if load_balancer is not None:
            self.load_balancer = load_balancer

    @property
    def load_balancer(self):
        """Gets the load_balancer of this V1ServiceStatus.  # noqa: E501


        :return: The load_balancer of this V1ServiceStatus.  # noqa: E501
        :rtype: V1LoadBalancerStatus
        """
        return self._load_balancer

    @load_balancer.setter
    def load_balancer(self, load_balancer):
        """Sets the load_balancer of this V1ServiceStatus.


        :param load_balancer: The load_balancer of this V1ServiceStatus.  # noqa: E501
        :type: V1LoadBalancerStatus
        """

        self._load_balancer = load_balancer

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
        if not isinstance(other, V1ServiceStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1ServiceStatus):
            return True

        return self.to_dict() != other.to_dict()
