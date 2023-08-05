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


class V1SelfSubjectAccessReviewSpec(object):
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
        'non_resource_attributes': 'V1NonResourceAttributes',
        'resource_attributes': 'V1ResourceAttributes'
    }

    attribute_map = {
        'non_resource_attributes': 'nonResourceAttributes',
        'resource_attributes': 'resourceAttributes'
    }

    def __init__(self, non_resource_attributes=None, resource_attributes=None, local_vars_configuration=None):  # noqa: E501
        """V1SelfSubjectAccessReviewSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._non_resource_attributes = None
        self._resource_attributes = None
        self.discriminator = None

        if non_resource_attributes is not None:
            self.non_resource_attributes = non_resource_attributes
        if resource_attributes is not None:
            self.resource_attributes = resource_attributes

    @property
    def non_resource_attributes(self):
        """Gets the non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501


        :return: The non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1NonResourceAttributes
        """
        return self._non_resource_attributes

    @non_resource_attributes.setter
    def non_resource_attributes(self, non_resource_attributes):
        """Sets the non_resource_attributes of this V1SelfSubjectAccessReviewSpec.


        :param non_resource_attributes: The non_resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type: V1NonResourceAttributes
        """

        self._non_resource_attributes = non_resource_attributes

    @property
    def resource_attributes(self):
        """Gets the resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501


        :return: The resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :rtype: V1ResourceAttributes
        """
        return self._resource_attributes

    @resource_attributes.setter
    def resource_attributes(self, resource_attributes):
        """Sets the resource_attributes of this V1SelfSubjectAccessReviewSpec.


        :param resource_attributes: The resource_attributes of this V1SelfSubjectAccessReviewSpec.  # noqa: E501
        :type: V1ResourceAttributes
        """

        self._resource_attributes = resource_attributes

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
        if not isinstance(other, V1SelfSubjectAccessReviewSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1SelfSubjectAccessReviewSpec):
            return True

        return self.to_dict() != other.to_dict()
