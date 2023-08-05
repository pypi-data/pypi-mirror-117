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


class ExtensionsV1beta1ScaleStatus(object):
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
        'replicas': 'int',
        'selector': 'dict(str, str)',
        'target_selector': 'str'
    }

    attribute_map = {
        'replicas': 'replicas',
        'selector': 'selector',
        'target_selector': 'targetSelector'
    }

    def __init__(self, replicas=None, selector=None, target_selector=None, local_vars_configuration=None):  # noqa: E501
        """ExtensionsV1beta1ScaleStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._replicas = None
        self._selector = None
        self._target_selector = None
        self.discriminator = None

        self.replicas = replicas
        if selector is not None:
            self.selector = selector
        if target_selector is not None:
            self.target_selector = target_selector

    @property
    def replicas(self):
        """Gets the replicas of this ExtensionsV1beta1ScaleStatus.  # noqa: E501

        actual number of observed instances of the scaled object.  # noqa: E501

        :return: The replicas of this ExtensionsV1beta1ScaleStatus.  # noqa: E501
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """Sets the replicas of this ExtensionsV1beta1ScaleStatus.

        actual number of observed instances of the scaled object.  # noqa: E501

        :param replicas: The replicas of this ExtensionsV1beta1ScaleStatus.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and replicas is None:  # noqa: E501
            raise ValueError("Invalid value for `replicas`, must not be `None`")  # noqa: E501

        self._replicas = replicas

    @property
    def selector(self):
        """Gets the selector of this ExtensionsV1beta1ScaleStatus.  # noqa: E501

        label query over pods that should match the replicas count. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors  # noqa: E501

        :return: The selector of this ExtensionsV1beta1ScaleStatus.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this ExtensionsV1beta1ScaleStatus.

        label query over pods that should match the replicas count. More info: http://kubernetes.io/docs/user-guide/labels#label-selectors  # noqa: E501

        :param selector: The selector of this ExtensionsV1beta1ScaleStatus.  # noqa: E501
        :type: dict(str, str)
        """

        self._selector = selector

    @property
    def target_selector(self):
        """Gets the target_selector of this ExtensionsV1beta1ScaleStatus.  # noqa: E501

        label selector for pods that should match the replicas count. This is a serializated version of both map-based and more expressive set-based selectors. This is done to avoid introspection in the clients. The string will be in the same format as the query-param syntax. If the target type only supports map-based selectors, both this field and map-based selector field are populated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :return: The target_selector of this ExtensionsV1beta1ScaleStatus.  # noqa: E501
        :rtype: str
        """
        return self._target_selector

    @target_selector.setter
    def target_selector(self, target_selector):
        """Sets the target_selector of this ExtensionsV1beta1ScaleStatus.

        label selector for pods that should match the replicas count. This is a serializated version of both map-based and more expressive set-based selectors. This is done to avoid introspection in the clients. The string will be in the same format as the query-param syntax. If the target type only supports map-based selectors, both this field and map-based selector field are populated. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors  # noqa: E501

        :param target_selector: The target_selector of this ExtensionsV1beta1ScaleStatus.  # noqa: E501
        :type: str
        """

        self._target_selector = target_selector

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
        if not isinstance(other, ExtensionsV1beta1ScaleStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtensionsV1beta1ScaleStatus):
            return True

        return self.to_dict() != other.to_dict()
